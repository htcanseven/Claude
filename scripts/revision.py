"""Re-analyses added at revision (all on the same public data and feature caches).

  R1  decision table: for e_req in {3, 5, 8, 12} % and alpha in {0.90, 0.95, 0.99}, the cheapest observation
      suite per alternative and failure-mode class, classified meets / uncertain / fails from a bootstrap
      over trials (operating points resampled within each tap pair)
  R2  requirement-writable quantities: monotone-safe MDE (smallest tested extent above which every tested
      extent is detectable) and the detectable share conditional on e >= e_req; nested (leave-one-tap-pair-
      out) selection of the fixed feature next to the in-sample selection
  R3  numerator / denominator decomposition of the SCIG / PMSG ratio of median SDR (5-cycle windows)
  R4  transfer metrics restricted to out-of-reference negatives (fault-time windows of healthy trials and
      recovery windows), next to the all-negatives metrics
  R5  the list of features that fail the reliability screen, per machine and window length

Outputs: results/tables/R_*.csv and results/summary_revision.md
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

import compare as C
import compare3 as C3
from compare3 import MACH, SUITES3, WFSG_ZF_MATCH, load3, per_feature, sdr_from_windows, unreliable

COST_RANK = {"drive-internal": 0, "excitation (WFSG only)": 0, "3 CT": 1, "3 CT + 3 VT": 2, "3 CT + 3 VT + drive": 3}
E_REQ = [3, 5, 8, 12]
ALPHAS = [0.90, 0.95, 0.99]
B = 1000
RNG = np.random.RandomState(7)


# ----------------------------------------------------------------------------- R2 definitions
def mde_monotone(s, col):
    """Smallest tested extent e* such that every tested extent >= e* has median SDR >= 1 (NaN if the largest
    tested extent is not detectable)."""
    med = s.groupby("sev_pct")[col].median().sort_index()
    ok = (med >= 1).to_numpy()
    idx = len(ok)
    for i in range(len(ok) - 1, -1, -1):
        if ok[i]:
            idx = i
        else:
            break
    return float(med.index[idx]) if idx < len(ok) else np.nan


def ds_conditional(s, col, e_req):
    sub = s[s.sev_pct >= e_req]
    return float((sub[col] >= 1).mean()) if len(sub) else np.nan


def fixed_feature(f, feats):
    cols = [f"{x}__sdr" for x in feats]
    med = f[cols].median().set_axis(feats)
    return med.idxmax()


def nested_share(f, feats):
    """Leave-one-tap-pair-out: choose the fixed feature on the other tap pairs, score the held-out pair."""
    hits, n = 0, 0
    for case, held in f.groupby("case"):
        rest = f[f.case != case]
        best = fixed_feature(rest, feats)
        hits += int((held[f"{best}__sdr"] >= 1).sum())
        n += len(held)
    return hits / n if n else np.nan


def bootstrap_mde(f, col, e_reqs, B=B):
    """Resample the operating-point trials within each tap pair; return P(MDE <= e_req) per e_req."""
    groups = {k: g[col].to_numpy() for k, g in f.groupby("sev_pct")}
    keys = sorted(groups)
    ok_mat = np.zeros((B, len(keys)), dtype=bool)
    for j, k in enumerate(keys):
        v = groups[k]
        idx = RNG.randint(0, len(v), size=(B, len(v)))
        ok_mat[:, j] = np.nanmedian(v[idx], axis=1) >= 1
    # monotone-safe MDE per resample: smallest key index from which all later are ok
    suffix_ok = np.flip(np.cumprod(np.flip(ok_mat, axis=1), axis=1), axis=1).astype(bool)
    mde = np.full(B, np.nan)
    for b in range(B):
        w = np.where(suffix_ok[b])[0]
        if len(w):
            mde[b] = keys[w[0]]
    return {e: float(np.mean(mde <= e)) for e in e_reqs}, mde


# ----------------------------------------------------------------------------- R1 decision table
def decision_table(win, feats):
    rows = []
    for alpha in ALPHAS:
        sdr, qv_a = sdr_from_windows(win, feats, q=alpha)
        det = per_feature(sdr, feats, qv_a)
        for m in MACH:
            bad = unreliable(det, m, alpha)
            for ft in ["TURNS", "WINDINGS"]:
                f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
                if not len(f):
                    continue
                fm = f if m != "WFSG" else f[np.isclose(f.zf_ohm, WFSG_ZF_MATCH)]
                for suite, sfeats in SUITES3.items():
                    if suite.startswith("excitation") and m != "WFSG":
                        continue
                    sfeats = [x for x in sfeats if x not in bad and f"{x}__sdr" in fm.columns and fm[f"{x}__sdr"].notna().any()]
                    if not sfeats:
                        continue
                    best = fixed_feature(fm, sfeats)
                    col = f"{best}__sdr"
                    p_ok, mde_bs = bootstrap_mde(fm, col, E_REQ)
                    mde = mde_monotone(fm, col)
                    for e in E_REQ:
                        p = p_ok[e]
                        verdict = "meets" if p >= 0.95 else ("fails" if p <= 0.05 else "uncertain")
                        rows.append(dict(alpha=alpha, e_req_pct=e, machine=m, ftype=ft, suite=suite, cost_rank=COST_RANK[suite],
                                         fixed_feature=best, mde_monotone_pct=mde,
                                         mde_ci_lo=np.nanpercentile(mde_bs, 2.5) if np.isfinite(mde_bs).any() else np.nan,
                                         mde_ci_hi=np.nanpercentile(mde_bs, 97.5) if np.isfinite(mde_bs).any() else np.nan,
                                         p_meets=p, verdict=verdict,
                                         ds_conditional=ds_conditional(fm, col, e), ds_all=float((fm[col] >= 1).mean()),
                                         smallest_extent_tested_pct=float(fm.sev_pct.min())))
    d = pd.DataFrame(rows)
    # cheapest suite that meets, and cheapest that does not fail, per (alpha, e_req, machine, ftype)
    sel = []
    for key, g in d.groupby(["alpha", "e_req_pct", "machine", "ftype"]):
        g = g.sort_values("cost_rank")
        meets = g[g.verdict == "meets"]
        notfail = g[g.verdict != "fails"]
        sel.append(dict(zip(["alpha", "e_req_pct", "machine", "ftype"], key),
                        cheapest_meets=meets.suite.iloc[0] if len(meets) else "none",
                        cheapest_meets_feature=meets.fixed_feature.iloc[0] if len(meets) else "",
                        cheapest_not_failing=notfail.suite.iloc[0] if len(notfail) else "none",
                        n_uncertain=int((g.verdict == "uncertain").sum())))
    return d, pd.DataFrame(sel)


# ----------------------------------------------------------------------------- R2 requirement-writable quantities
def requirement_quantities(sdr, det):
    rows = []
    for m in MACH:
        bad = unreliable(det, m)
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            if not len(f):
                continue
            fm = f if m != "WFSG" else f[np.isclose(f.zf_ohm, WFSG_ZF_MATCH)]
            for suite, sfeats in SUITES3.items():
                if suite.startswith("excitation") and m != "WFSG":
                    continue
                sfeats = [x for x in sfeats if x not in bad and f"{x}__sdr" in fm.columns and fm[f"{x}__sdr"].notna().any()]
                if not sfeats:
                    continue
                best = fixed_feature(fm, sfeats)
                col = f"{best}__sdr"
                rows.append(dict(machine=m, ftype=ft, suite=suite, cost_rank=COST_RANK[suite], fixed_feature=best,
                                 n_candidates=len(sfeats),
                                 mde_first_pct=C3.min_detectable(fm, col), mde_monotone_pct=mde_monotone(fm, col),
                                 ds_all=float((fm[col] >= 1).mean()),
                                 ds_ge_5pct=ds_conditional(fm, col, 5), ds_ge_8pct=ds_conditional(fm, col, 8),
                                 ds_nested=nested_share(fm, sfeats),
                                 smallest_extent_tested_pct=float(fm.sev_pct.min())))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R3 decomposition
def decomposition(win5, feats, key):
    sdr, qv = sdr_from_windows(win5, feats, q=0.95)
    rows = []
    for ft in ["TURNS", "WINDINGS"]:
        for feat in key:
            r = dict(ftype=ft, feature=feat)
            for m in ["PMSG", "SCIG"]:
                f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
                r[f"abs_delta_median_{m}"] = float(f[f"{feat}__delta"].abs().median())
                r[f"q95_{m}"] = float(qv.loc[m, feat])
                r[f"sdr_median_{m}"] = float(f[f"{feat}__sdr"].median())
            r["ratio_sdr"] = r["sdr_median_SCIG"] / r["sdr_median_PMSG"]
            r["ratio_numerator"] = r["abs_delta_median_SCIG"] / r["abs_delta_median_PMSG"]
            r["ratio_denominator"] = r["q95_PMSG"] / r["q95_SCIG"]   # a quieter SCIG null inflates its SDR
            rows.append(r)
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R4 transfer on out-of-reference negatives
def _metrics(y, s, oor, hflt):
    """all = every window; oor = windows outside the normalising reference windows (second half of the
    reference interval, fault-time windows of healthy trials, recovery windows); hflt = fault-time windows
    of healthy trials (contactor operation without a fault), scored at the threshold that gives 1 % FPR on
    all negatives."""
    out = dict(auc_all=roc_auc_score(y, s), tpr_all=C.tpr_at_fpr(y, s))
    if oor.sum() and y[oor].sum() and (~y[oor].astype(bool)).sum():
        out.update(auc_oor=roc_auc_score(y[oor], s[oor]), tpr_oor=C.tpr_at_fpr(y[oor], s[oor]))
    else:
        out.update(auc_oor=np.nan, tpr_oor=np.nan)
    neg = s[y == 0]
    t = np.quantile(neg, 0.99) if len(neg) else np.nan
    out["fpr_healthy_flt_at_1pct"] = float((s[hflt] > t).mean()) if hflt.sum() else np.nan
    out["n_healthy_flt"] = int(hflt.sum())
    return out


def transfer_oor(win):
    """As compare3.transfer3, but every metric is also computed on the windows outside the normalising
    reference interval (positives + fault-time windows of healthy trials + recovery windows)."""
    w = win[win.segment.isin(["PRE", "FLT", "POST"])].copy()
    w["y"] = ((w.segment == "FLT") & (w.ftype != "HEALTHY")).astype(int)
    w["group"] = C.make_groups(w)
    feats = C3.COMMON
    w = w.replace([np.inf, -np.inf], np.nan).dropna(subset=feats)
    X = C.calibrate(w, feats, "self-ref").to_numpy()
    y = w.y.to_numpy()
    oor_all = ~C.norm_mask(w)
    hflt = ((w.ftype == "HEALTHY") & (w.segment == "FLT")).to_numpy()
    mk = lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
    rows = []
    for m in MACH:
        idx = (w.machine == m).to_numpy()
        Xm, ym, gm = X[idx], y[idx], w.group[idx].to_numpy()
        s = np.zeros(len(ym))
        for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
            s[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
        rows.append(dict(train=m, test=m, **_metrics(ym, s, oor_all[idx], hflt[idx])))
    for a in MACH:
        for b in MACH:
            if a == b:
                continue
            tr, te = (w.machine == a).to_numpy(), (w.machine == b).to_numpy()
            s = mk().fit(X[tr], y[tr]).predict_proba(X[te])[:, 1]
            rows.append(dict(train=a, test=b, **_metrics(y[te], s, oor_all[te], hflt[te])))
    for b in MACH:
        tr, te = (w.machine != b).to_numpy(), (w.machine == b).to_numpy()
        s = mk().fit(X[tr], y[tr]).predict_proba(X[te])[:, 1]
        rows.append(dict(train="+".join(m for m in MACH if m != b), test=b, **_metrics(y[te], s, oor_all[te], hflt[te])))
    counts = w.assign(oor=oor_all, hflt=hflt).groupby("machine").agg(n_windows=("y", "size"), n_pos=("y", "sum"),
                                                                    n_oor=("oor", "sum"), n_healthy_flt=("hflt", "sum"))
    return pd.DataFrame(rows), counts


def transfer2_oor(win5):
    """PMSG/SCIG, 5-cycle windows, three referencing rules x two models, with out-of-reference metrics."""
    w, feats = C.build_window_table(win5)
    y = w.y.to_numpy()
    oor_all = ~C.norm_mask(w)
    hflt = ((w.ftype == "HEALTHY") & (w.segment == "FLT")).to_numpy()
    models = {"logistic": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=1.0)),
              "gbdt": lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)}
    rows = []
    for mode in ["raw", "healthy-z", "self-ref"]:
        X = C.calibrate(w, feats, mode).to_numpy()
        for mname, mk in models.items():
            for m in ["PMSG", "SCIG"]:
                idx = (w.machine == m).to_numpy()
                Xm, ym, gm = X[idx], y[idx], w.group[idx].to_numpy()
                s = np.zeros(len(ym))
                for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
                    s[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
                rows.append(dict(calibration=mode, model=mname, train=m, test=m, **_metrics(ym, s, oor_all[idx], hflt[idx])))
            for a, b in [("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                tr, te = (w.machine == a).to_numpy(), (w.machine == b).to_numpy()
                s = mk().fit(X[tr], y[tr]).predict_proba(X[te])[:, 1]
                rows.append(dict(calibration=mode, model=mname, train=a, test=b, **_metrics(y[te], s, oor_all[te], hflt[te])))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R9-R11 further checks
def null_exceedance_by_speed(win5, feats, key):
    """Share of trials whose healthy relative change exceeds the pooled q95, per machine and speed."""
    w = win5.replace([np.inf, -np.inf], np.nan)
    pre = w.segment == "PRE"
    pre_e = w[pre & (w.t_start < C.PRE_SPLIT)].groupby("rid")[feats].mean()
    pre_l = w[pre & (w.t_start >= C.PRE_SPLIT)].groupby("rid")[feats].mean()
    meta = w.groupby("rid")[["machine", "speed_rpm", "torque_Nm"]].first()
    null = ((pre_l - pre_e) / pre_e.abs()).abs()
    q = null.groupby(meta.machine).quantile(0.95)
    exc = null > q.reindex(meta.machine).set_axis(null.index)
    out = exc[key].groupby([meta.machine, meta.speed_rpm]).mean().reset_index()
    out["n"] = exc[key[0]].groupby([meta.machine, meta.speed_rpm]).size().to_numpy()
    return out


def ranking_similarity(det):
    """Spearman correlation between the PMSG and SCIG rankings of features by median SDR."""
    from scipy.stats import spearmanr
    rows = []
    for ft in ["TURNS", "WINDINGS"]:
        p = det[(det.machine == "PMSG") & (det.ftype == ft)].set_index("feature").median_sdr
        s = det[(det.machine == "SCIG") & (det.ftype == ft)].set_index("feature").median_sdr
        common = p.index.intersection(s.index)
        rows.append(dict(ftype=ft, n_features=len(common), spearman=spearmanr(p[common], s[common]).correlation,
                         top5_PMSG=", ".join(p[common].sort_values(ascending=False).index[:5]),
                         top5_SCIG=", ".join(s[common].sort_values(ascending=False).index[:5])))
    return pd.DataFrame(rows)


def wfsg_windows(files):
    f = files[(files.machine == "WFSG") & files.is_fault]
    g = f.groupby("speed_rpm").agg(n_trials=("file", "size"), fe0_Hz=("fe0_Hz", "median"),
                                   n_flt_median=("n_flt", "median"), n_flt_min=("n_flt", "min"),
                                   trials_without_fault_window=("n_flt", lambda x: int((x == 0).sum())),
                                   trials_below_3_windows=("n_flt", lambda x: int((x < 3).sum()))).reset_index()
    return g


# ----------------------------------------------------------------------------- R6 baselines and negative-sequence impedance
def baselines_and_z2(files):
    """Healthy baselines of the three asymmetry ratios and the incremental negative-sequence impedance
    dV2/dI2 under fault (Lee et al. 2003): a current-regulated drive yields a large |dV2/dI2|."""
    f = files[files.is_fault].copy()
    f["V2_pre"] = f.V2_V1__pre * f.V1__pre
    f["V2_flt"] = f.V2_V1__flt * f.V1__flt
    f["dI2"] = f.I2__flt - f.I2__pre
    f["dV2"] = f.V2_flt - f.V2_pre
    f["dV2_dI2"] = f.dV2 / f.dI2
    rows = []
    for m in MACH:
        for ft in ["TURNS", "WINDINGS"]:
            s = f[(f.machine == m) & (f.ftype == ft)]
            if m == "WFSG":
                s = s[np.isclose(s.zf_ohm, WFSG_ZF_MATCH)]
            if not len(s):
                continue
            rows.append(dict(machine=m, ftype=ft, n=len(s),
                             I2_I1_pre=s.I2_I1__pre.median(), V2_V1_pre=s.V2_V1__pre.median(), D2_D1_pre=s.D2_D1__pre.median(),
                             I1_pre_A_rms=(s.I1__pre / np.sqrt(2)).median(), I2_pre_A_rms=(s.I2__pre / np.sqrt(2)).median(),
                             dI2_A_rms=(s.dI2 / np.sqrt(2)).median(), dV2_V_rms=(s.dV2 / np.sqrt(2)).median(),
                             dV2_dI2_ohm=s.dV2_dI2.median(), dV2_dI2_q25=s.dV2_dI2.quantile(.25), dV2_dI2_q75=s.dV2_dI2.quantile(.75)))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R7 commissioning-baseline (between-trial) null
def between_trial(win5, feats, key):
    """PMSG/SCIG, 5-cycle windows. Reference = the healthy trial at the same operating point (recorded at a
    different time) instead of the trial's own preceding interval; the null is the drift of the healthy
    reference intervals of all fault trials relative to that baseline."""
    w = win5.replace([np.inf, -np.inf], np.nan)
    pre = w[w.segment == "PRE"].groupby("rid")[feats].mean()
    flt = w[w.segment == "FLT"].groupby("rid")[feats].mean()
    meta = w.groupby("rid")[["machine", "ftype", "sev_pct", "speed_rpm", "torque_Nm", "case"]].first()
    sdr_w, q_w = sdr_from_windows(win5, feats, q=0.95)
    rows = []
    for m in ["PMSG", "SCIG"]:
        mm = meta[meta.machine == m]
        healthy = mm[mm.ftype == "HEALTHY"]
        base = {(r.speed_rpm, r.torque_Nm): pre.loc[rid] for rid, r in healthy.iterrows()}
        faults = mm[mm.ftype != "HEALTHY"]
        b = pd.DataFrame([base[(r.speed_rpm, r.torque_Nm)] for _, r in faults.iterrows()], index=faults.index)
        delta = (flt.loc[faults.index] - b) / b.abs()
        null = (pre.loc[faults.index] - b) / b.abs()
        q_b = null.abs().quantile(0.95)
        sdr_b = delta.abs() / q_b
        for ft in ["TURNS", "WINDINGS"]:
            idx = faults.index[faults.ftype == ft]
            for feat in key:
                rows.append(dict(machine=m, ftype=ft, feature=feat,
                                 q95_within=float(q_w.loc[m, feat]), q95_between=float(q_b[feat]),
                                 median_sdr_within=float(sdr_w.loc[idx, f"{feat}__sdr"].median()),
                                 ds_within=float((sdr_w.loc[idx, f"{feat}__sdr"] >= 1).mean()),
                                 median_sdr_between=float(sdr_b.loc[idx, feat].median()),
                                 ds_between=float((sdr_b.loc[idx, feat] >= 1).mean())))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R8 absolute-change variant
def absolute_variant(win5, feats):
    """SDR with absolute instead of relative changes (no |phi_R| in numerator or null): does the feature
    ranking depend on the baseline level of the feature?"""
    from scipy.stats import spearmanr
    w = win5.replace([np.inf, -np.inf], np.nan)
    pre = w.segment == "PRE"
    pre_e = w[pre & (w.t_start < C.PRE_SPLIT)].groupby("rid")[feats].mean()
    pre_l = w[pre & (w.t_start >= C.PRE_SPLIT)].groupby("rid")[feats].mean()
    flt = w[w.segment == "FLT"].groupby("rid")[feats].mean()
    meta = w.groupby("rid")[["machine", "ftype"]].first()
    q = (pre_l - pre_e).abs().groupby(meta.machine).quantile(0.95)
    sdr_abs = (flt - pre_l).abs() / q.reindex(meta.machine).set_axis(flt.index)
    sdr_rel, _ = sdr_from_windows(win5, feats, q=0.95)
    rows = []
    for m in ["PMSG", "SCIG"]:
        for ft in ["TURNS", "WINDINGS"]:
            idx = meta.index[(meta.machine == m) & (meta.ftype == ft)]
            ma = sdr_abs.loc[idx].median()
            mr = sdr_rel.loc[idx, [f"{f}__sdr" for f in feats]].median().set_axis(feats)
            ok = ma.notna() & mr.notna()
            rho = spearmanr(ma[ok], mr[ok]).correlation
            rows.append(dict(machine=m, ftype=ft, spearman_rank_corr=rho,
                             top3_relative=", ".join(mr[ok].sort_values(ascending=False).index[:3]),
                             top3_absolute=", ".join(ma[ok].sort_values(ascending=False).index[:3]),
                             ds_top_relative=float((sdr_rel.loc[idx, mr[ok].idxmax() + "__sdr"] >= 1).mean()),
                             ds_top_absolute=float((sdr_abs.loc[idx, ma[ok].idxmax()] >= 1).mean())))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R5 screen list
def screen_list():
    rows = []
    for ncyc, suffix in [(3, "_ncyc3"), (5, ""), (8, "_ncyc8")]:
        w = pd.read_csv(C.RES / f"features_windows{suffix}.csv.gz")
        w["rid"] = w.machine + "/" + w.file
        sdr, _ = sdr_from_windows(w, C.ALL_FEATS, q=0.95)
        for m in ["PMSG", "SCIG"]:
            h = sdr[(sdr.machine == m) & ~sdr.is_fault]
            for feat in C.ALL_FEATS:
                fa = float((h[f"{feat}__sdr"] >= 1).mean())
                if fa > C.MAX_FALSE_ALARM:
                    rows.append(dict(window_cycles=ncyc, machine=m, feature=feat, healthy_false_alarm=fa,
                                     n_false=int((h[f"{feat}__sdr"] >= 1).sum())))
    return pd.DataFrame(rows)


def main():
    files, win = load3()
    feats = [f for f in C3.FEATS3 if f in win.columns]
    sdr, qv = sdr_from_windows(win, feats)
    det = per_feature(sdr, feats, qv)

    dec, sel = decision_table(win, feats)
    dec.to_csv(C.TAB / "R_decision_table.csv", index=False)
    sel.to_csv(C.TAB / "R_decision_cheapest.csv", index=False)
    req = requirement_quantities(sdr, det)
    req.to_csv(C.TAB / "R_requirement_quantities.csv", index=False)

    win5 = pd.read_csv(C.RES / "features_windows.csv.gz")
    win5["rid"] = win5.machine + "/" + win5.file
    win5["sev_pct"] = win5.sev_pct.round(1)
    key = ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe", "Vqconv_2fe", "D2_D1"]
    dec3 = decomposition(win5, C.ALL_FEATS, key)
    dec3.to_csv(C.TAB / "R_decomposition.csv", index=False)

    tr3, counts = transfer_oor(win)
    tr3.to_csv(C.TAB / "R_transfer3_oor.csv", index=False)
    counts.to_csv(C.TAB / "R_transfer3_counts.csv")
    tr2 = transfer2_oor(win5)
    tr2.to_csv(C.TAB / "R_transfer2_oor.csv", index=False)

    scr = screen_list()
    scr.to_csv(C.TAB / "R_screened_features.csv", index=False)

    z2 = baselines_and_z2(files)
    z2.to_csv(C.TAB / "R_baselines_z2.csv", index=False)
    bt = between_trial(win5, C.ALL_FEATS, ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe", "D2_D1"])
    bt.to_csv(C.TAB / "R_between_trial_null.csv", index=False)
    av = absolute_variant(win5, C.ALL_FEATS)
    av.to_csv(C.TAB / "R_absolute_variant.csv", index=False)
    ex = null_exceedance_by_speed(win5, C.ALL_FEATS, ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe"])
    ex.to_csv(C.TAB / "R_null_exceedance_by_speed.csv", index=False)
    rk = ranking_similarity(pd.read_csv(C.TAB / "B_sdr_by_feature.csv"))
    rk.to_csv(C.TAB / "R_ranking_similarity.csv", index=False)
    ww = wfsg_windows(files)
    ww.to_csv(C.TAB / "R_wfsg_windows.csv", index=False)

    L = ["# Revision re-analyses\n",
         "## R9 null exceedance by speed (pooled q95, 5-cycle windows)\n", C.md_table(ex.round(3)),
         "\n## R10 PMSG vs SCIG feature-ranking similarity (5-cycle windows)\n", C.md_table(rk.round(3)),
         "\n## R11 WFSG fault windows per trial (3-cycle windows)\n", C.md_table(ww.round(2)),
         "## R6 healthy baselines and incremental negative-sequence impedance dV2/dI2 (RMS units)\n", C.md_table(z2.round(4)),
         "\n## R7 within-trial vs commissioning-baseline (between-trial) null, PMSG/SCIG, 5-cycle windows\n", C.md_table(bt.round(3)),
         "\n## R8 relative vs absolute change: feature ranking\n", C.md_table(av.round(3)),
         "## R1 cheapest suite per requirement (bootstrap verdicts: meets P>=0.95, fails P<=0.05)\n", C.md_table(sel),
         "\n## R1 full decision table (alpha = 0.95)\n", C.md_table(dec[dec.alpha == 0.95].drop(columns=["alpha"]).round(3)),
         "\n## R2 requirement-writable quantities (alpha = 0.95, 3-cycle windows)\n", C.md_table(req.round(3)),
         "\n## R3 SCIG / PMSG ratio decomposition (5-cycle windows)\n", C.md_table(dec3.round(4)),
         "\n## R4 transfer, three alternatives (self-ref, GBDT): all negatives vs out-of-reference negatives\n",
         C.md_table(tr3.round(3)), "\n", C.md_table(counts.reset_index()),
         "\n## R4 transfer, PMSG/SCIG (5-cycle windows)\n", C.md_table(tr2.round(3)),
         "\n## R5 features failing the reliability screen (> 1 of 9 healthy trials)\n", C.md_table(scr.round(3))]
    (C.RES / "summary_revision.md").write_text("\n".join(L))
    print(sel.to_string(index=False))
    print(req.round(3).to_string(index=False))
    print(dec3.round(3).to_string(index=False))
    print(tr3.round(3).to_string(index=False))
    print(scr.to_string(index=False))
    print("done -> results/summary_revision.md")


if __name__ == "__main__":
    main()
