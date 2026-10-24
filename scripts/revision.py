"""Re-analyses added at revision (all on the same public data and feature caches).

  R1  decision table: for e_req in {3, 5, 8, 12} % and alpha in {0.90, 0.95, 0.99}, every sensor suite per
      alternative and failure-mode class with the bootstrap probability that it MEETS the requirement, where
      "meets" is the joint event {MDE <= e_req and detectable share for e >= e_req at least DS_REQ}; the fixed
      feature is chosen inside every resample (nested selection), the null quantile is re-estimated from a
      cluster resample of all recordings, operating-point trials are resampled within each physical extent
      level, and verdicts are monotone over nested suites (a suite inherits the best verdict of its subsets).
      Computed on three-cycle windows for all three alternatives and on five-cycle windows for the PMSG/SCIG.
  R2  requirement-writable quantities: MDE as a bracket on the physical levels, detectable share conditional on
      e >= e_req, nested (leave-one-tap-pair-out) selection of the fixed feature, empirical false-alarm rate
  R3  numerator / denominator decomposition of the SCIG / PMSG ratio of median SDR (5-cycle windows), in the
      relative form of the SDR and in absolute units of each feature
  R4  transfer metrics on out-of-reference negatives, with a per-operating-point commissioning baseline as a
      fourth referencing rule and cluster-bootstrap intervals over trials for AUC and TPR at 1 % FPR
  R5  the list of features that fail the reliability screen, per machine and window length
  R12 inter-turn results per faulted phase and per tap pair (magnitude features against phasor residuals)

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
from compare3 import (MACH, SUBSETS, SUITES3, WFSG_ZF_MATCH, level_col, load3, mde_bracket, per_feature,
                      sdr_from_windows, unreliable, wilson)

COST_RANK = {"drive-internal": 0, "excitation (WFSG only)": 0, "3 CT": 1, "3 CT + 3 VT": 2, "3 CT + 3 VT + drive": 3}
E_REQ = [3, 5, 8, 12]
ALPHAS = [0.90, 0.95, 0.99]
DS_REQ = 0.9      # stated power: detectable share required for e >= e_req
B = 1000
B_TRANSFER = 500
SCALAR = [f for f in C.ALL_FEATS if f not in C.RESID]


# ----------------------------------------------------------------------------- R2 definitions
def mde_monotone(s, col, by=None):
    return C3.min_detectable(s, col, by)


def ds_conditional(s, col, e_req, by=None):
    by = by or level_col(s)
    sub = s[s[by] >= e_req]
    return float((sub[col] >= 1).mean()) if len(sub) else np.nan


def fixed_feature(f, feats):
    return C3.select_feature(f, feats)


def nested_share(f, feats):
    """Leave-one-tap-pair-out: choose the fixed feature on the other tap pairs, score the held-out pair."""
    hits, n = 0, 0
    for case, held in f.groupby("case"):
        rest = f[f.case != case]
        best = fixed_feature(rest, feats)
        hits += int((held[f"{best}__sdr"] >= 1).sum())
        n += len(held)
    return hits / n if n else np.nan


# ----------------------------------------------------------------------------- R1 decision table
def decision_table(win, feats, B=B, seed=7, ds_req=DS_REQ, machines=MACH):
    rng = np.random.RandomState(seed)
    rows = []
    for alpha in ALPHAS:
        sdr, qv_a = sdr_from_windows(win, feats, q=alpha)
        det = per_feature(sdr, feats, qv_a)
        for m in machines:
            rec = sdr[sdr.machine == m]
            if not len(rec):
                continue
            bad = unreliable(det, m, alpha)
            ncl = np.where(rec.is_fault, rec.case.astype(str), "HEALTHY")
            cl_names = np.unique(ncl)
            cl_rows = {c: np.flatnonzero(ncl == c) for c in cl_names}
            for ft in ["TURNS", "WINDINGS"]:
                f = rec[rec.ftype == ft]
                fm = f if m != "WFSG" else f[np.isclose(f.zf_ohm, WFSG_ZF_MATCH)]
                if not len(fm):
                    continue
                by = level_col(fm)
                fm = fm[fm[by].notna()]
                levels = np.sort(fm[by].unique())
                lev = fm[by].to_numpy()
                idx_by_level = [np.flatnonzero(lev == k) for k in levels]
                for suite, sfeats in SUITES3.items():
                    if suite.startswith("excitation") and m != "WFSG":
                        continue
                    sfeats = [x for x in sfeats if x not in bad and f"{x}__sdr" in fm.columns and fm[f"{x}__sdr"].notna().any()]
                    if not sfeats:
                        continue
                    D = fm[[f"{x}__delta" for x in sfeats]].abs().to_numpy()
                    N = rec[[f"{x}__null" for x in sfeats]].abs().to_numpy()
                    best = fixed_feature(fm, sfeats)
                    col = f"{best}__sdr"
                    lo, mde = mde_bracket(fm, col, by)
                    hits = {e: 0 for e in E_REQ}
                    hits_mde = {e: 0 for e in E_REQ}
                    chosen = {}
                    for b in range(B):
                        idx = np.concatenate([rng.choice(ix, size=len(ix), replace=True) for ix in idx_by_level])
                        pick = rng.choice(cl_names, size=len(cl_names), replace=True)
                        nidx = np.concatenate([cl_rows[c] for c in pick])
                        qb = np.nanquantile(N[nidx], alpha, axis=0)
                        S = D[idx] / qb
                        levb = lev[idx]
                        # nested selection by the same rule as the point estimate: smallest MDE, then share, then median
                        lev_med = np.array([np.nanmedian(S[levb == k], axis=0) for k in levels])   # levels x feats
                        okm = lev_med >= 1
                        suffix = np.flip(np.cumprod(np.flip(okm, axis=0), axis=0), axis=0).astype(bool)
                        mde_f = np.array([levels[np.flatnonzero(suffix[:, jj])[0]] if suffix[:, jj].any() else np.inf
                                          for jj in range(S.shape[1])])
                        ds_f = np.nanmean(S >= 1, axis=0)
                        med_f = np.nan_to_num(np.nanmedian(S, axis=0), nan=-1)
                        j = int(np.lexsort((-med_f, -ds_f, mde_f))[0])
                        chosen[sfeats[j]] = chosen.get(sfeats[j], 0) + 1
                        s = S[:, j]
                        mde_b = mde_f[j]
                        for e in E_REQ:
                            sub = s[levb >= e]
                            ds = np.nanmean(sub >= 1) if len(sub) else np.nan
                            if mde_b <= e:
                                hits_mde[e] += 1
                                if ds >= ds_req:
                                    hits[e] += 1
                    top = max(chosen, key=chosen.get)
                    for e in E_REQ:
                        rows.append(dict(alpha=alpha, e_req_pct=e, machine=m, ftype=ft, suite=suite, cost_rank=COST_RANK[suite],
                                         fixed_feature=best, feature_most_often=top, selection_stability=chosen[top] / B,
                                         mde_monotone_pct=mde, mde_bracket_lo_pct=lo,
                                         p_mde=hits_mde[e] / B, p_meets_own=hits[e] / B,
                                         ds_conditional=ds_conditional(fm, col, e, by), ds_all=float((fm[col] >= 1).mean()),
                                         smallest_extent_tested_pct=float(levels.min())))
    d = pd.DataFrame(rows)
    # monotone inheritance over nested suites: a suite may use the features of its subsets
    p_mono, inherited = [], []
    for i, r in d.iterrows():
        g = d[(d.alpha == r.alpha) & (d.e_req_pct == r.e_req_pct) & (d.machine == r.machine) & (d.ftype == r.ftype)]
        cand = g[g.suite.isin([r.suite] + SUBSETS.get(r.suite, []))]
        k = cand.p_meets_own.idxmax()
        p_mono.append(float(cand.loc[k, "p_meets_own"]))
        inherited.append("" if cand.loc[k, "suite"] == r.suite else cand.loc[k, "suite"])
    d["p_meets"] = p_mono
    d["inherited_from"] = inherited
    d["verdict"] = np.where(d.p_meets >= 0.95, "meets", np.where(d.p_meets <= 0.05, "fails", "uncertain"))
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
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            if not len(f):
                continue
            fm = f if m != "WFSG" else f[np.isclose(f.zf_ohm, WFSG_ZF_MATCH)]
            by = level_col(fm)
            for suite, sfeats in SUITES3.items():
                if suite.startswith("excitation") and m != "WFSG":
                    continue
                sfeats = [x for x in sfeats if x not in bad and f"{x}__sdr" in fm.columns and fm[f"{x}__sdr"].notna().any()]
                if not sfeats:
                    continue
                best = fixed_feature(fm, sfeats)
                col = f"{best}__sdr"
                lo, mde = mde_bracket(fm, col, by)
                k = int((h[col] >= 1).sum()) if len(h) else np.nan
                wl, wh = wilson(k, len(h)) if len(h) else (np.nan, np.nan)
                rows.append(dict(machine=m, ftype=ft, suite=suite, cost_rank=COST_RANK[suite], fixed_feature=best,
                                 n_candidates=len(sfeats), mde_bracket_lo_pct=lo, mde_monotone_pct=mde,
                                 ds_all=float((fm[col] >= 1).mean()),
                                 ds_ge_5pct=ds_conditional(fm, col, 5, by), ds_ge_8pct=ds_conditional(fm, col, 8, by),
                                 ds_nested=nested_share(fm, sfeats),
                                 healthy_false_alarm=(k / len(h)) if len(h) else np.nan, fa_wilson_lo=wl, fa_wilson_hi=wh,
                                 smallest_extent_tested_pct=float(fm[by].min())))
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
                allm = sdr[sdr.machine == m]
                r[f"level_{m}"] = float(f[f"{feat}__lvl"].abs().median())
                r[f"abs_delta_median_{m}"] = float(f[f"{feat}__delta"].abs().median())
                r[f"q95_{m}"] = float(qv.loc[m, feat])
                r[f"sdr_median_{m}"] = float(f[f"{feat}__sdr"].median())
                r[f"dabs_median_{m}"] = float(f[f"{feat}__dabs"].abs().median())
                r[f"nabs_q95_{m}"] = float(allm[f"{feat}__nabs"].abs().quantile(0.95))
                r[f"sdr_abs_median_{m}"] = float((f[f"{feat}__dabs"].abs() / r[f"nabs_q95_{m}"]).median())
            r["ratio_sdr"] = r["sdr_median_SCIG"] / r["sdr_median_PMSG"]
            r["ratio_numerator"] = r["abs_delta_median_SCIG"] / r["abs_delta_median_PMSG"]
            r["ratio_denominator"] = r["q95_PMSG"] / r["q95_SCIG"]   # a quieter SCIG null inflates its SDR
            r["ratio_sdr_abs"] = r["sdr_abs_median_SCIG"] / r["sdr_abs_median_PMSG"]
            r["ratio_numerator_abs"] = r["dabs_median_SCIG"] / r["dabs_median_PMSG"]
            r["ratio_denominator_abs"] = r["nabs_q95_PMSG"] / r["nabs_q95_SCIG"]
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


def boot_metrics(y, s, groups, oor, B=B_TRANSFER, seed=3):
    """Cluster bootstrap over trials (tap pairs, healthy speed groups) of the test set: percentile intervals for
    the AUC and the TPR at 1 % FPR on the out-of-reference windows. Overlapping windows of one trial are never
    split between resamples."""
    rng = np.random.RandomState(seed)
    names = np.unique(groups)
    rows = {g: np.flatnonzero(groups == g) for g in names}
    auc, tpr = [], []
    for _ in range(B):
        pick = rng.choice(names, size=len(names), replace=True)
        idx = np.concatenate([rows[g] for g in pick])
        yy, ss, oo = y[idx], s[idx], oor[idx]
        if yy[oo].sum() == 0 or (yy[oo] == 0).sum() == 0:
            continue
        auc.append(roc_auc_score(yy[oo], ss[oo]))
        tpr.append(C.tpr_at_fpr(yy[oo], ss[oo]))
    return dict(auc_oor_ci_lo=np.percentile(auc, 2.5), auc_oor_ci_hi=np.percentile(auc, 97.5),
                tpr_oor_ci_lo=np.percentile(tpr, 2.5), tpr_oor_ci_hi=np.percentile(tpr, 97.5), n_boot=len(auc))


def transfer_oor(win):
    """As compare3.transfer3, but every metric is also computed on the windows outside the normalising
    reference interval (positives + fault-time windows of healthy trials + recovery windows), with
    cluster-bootstrap intervals over the trials of the tested machine."""
    w, feats = C.build_window_table(win, C3.COMMON)
    X = C.calibrate(w, feats, "self-ref").to_numpy()
    y = w.y.to_numpy()
    grp = w.group.to_numpy()
    oor_all = ~C.norm_mask(w)
    hflt = ((w.ftype == "HEALTHY") & (w.segment == "FLT")).to_numpy()
    mk = lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)
    rows = []
    for m in MACH:
        idx = (w.machine == m).to_numpy()
        Xm, ym, gm = X[idx], y[idx], grp[idx]
        s = np.zeros(len(ym))
        for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
            s[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
        rows.append(dict(train=m, test=m, **_metrics(ym, s, oor_all[idx], hflt[idx]), **boot_metrics(ym, s, gm, oor_all[idx])))
    for a in MACH:
        for b in MACH:
            if a == b:
                continue
            tr, te = (w.machine == a).to_numpy(), (w.machine == b).to_numpy()
            s = mk().fit(X[tr], y[tr]).predict_proba(X[te])[:, 1]
            rows.append(dict(train=a, test=b, **_metrics(y[te], s, oor_all[te], hflt[te]), **boot_metrics(y[te], s, grp[te], oor_all[te])))
    for b in MACH:
        tr, te = (w.machine != b).to_numpy(), (w.machine == b).to_numpy()
        s = mk().fit(X[tr], y[tr]).predict_proba(X[te])[:, 1]
        rows.append(dict(train="+".join(m for m in MACH if m != b), test=b, **_metrics(y[te], s, oor_all[te], hflt[te]),
                         **boot_metrics(y[te], s, grp[te], oor_all[te])))
    counts = w.assign(oor=oor_all, hflt=hflt).groupby("machine").agg(n_windows=("y", "size"), n_pos=("y", "sum"),
                                                                    n_oor=("oor", "sum"), n_healthy_flt=("hflt", "sum"),
                                                                    n_trials=("rid", "nunique"))
    return pd.DataFrame(rows), counts


def transfer2_oor(win5, modes=("raw", "healthy-z", "healthy-z-op", "self-ref")):
    """PMSG/SCIG, 5-cycle windows, four referencing rules x two models, with out-of-reference metrics and
    cluster-bootstrap intervals."""
    w, feats = C.build_window_table(win5)
    y = w.y.to_numpy()
    grp = w.group.to_numpy()
    oor_all = ~C.norm_mask(w)
    hflt = ((w.ftype == "HEALTHY") & (w.segment == "FLT")).to_numpy()
    models = {"logistic": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=1.0)),
              "gbdt": lambda: HistGradientBoostingClassifier(max_depth=3, max_iter=200, learning_rate=0.08, random_state=0)}
    rows = []
    for mode in modes:
        X = C.calibrate(w, feats, mode).to_numpy()
        for mname, mk in models.items():
            for m in ["PMSG", "SCIG"]:
                idx = (w.machine == m).to_numpy()
                Xm, ym, gm = X[idx], y[idx], grp[idx]
                s = np.zeros(len(ym))
                for tr, te in GroupKFold(n_splits=5).split(Xm, ym, gm):
                    s[te] = mk().fit(Xm[tr], ym[tr]).predict_proba(Xm[te])[:, 1]
                rows.append(dict(calibration=mode, model=mname, train=m, test=m, **_metrics(ym, s, oor_all[idx], hflt[idx]),
                                 **boot_metrics(ym, s, gm, oor_all[idx])))
            for a, b in [("PMSG", "SCIG"), ("SCIG", "PMSG")]:
                tr, te = (w.machine == a).to_numpy(), (w.machine == b).to_numpy()
                s = mk().fit(X[tr], y[tr]).predict_proba(X[te])[:, 1]
                rows.append(dict(calibration=mode, model=mname, train=a, test=b, **_metrics(y[te], s, oor_all[te], hflt[te]),
                                 **boot_metrics(y[te], s, grp[te], oor_all[te])))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R12 phase and tap-pair tables
PHASE_FEATS = ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "D2_D1", "D2r_D1", "Id_2fe", "Vq_2fe"]


def phase_table(sdr, feats=PHASE_FEATS):
    """Inter-turn median SDR and detectable share per faulted phase: the magnitude features depend on the angle
    between the inherent and the fault-induced asymmetry, which rotates with the faulted phase; the phasor
    residuals should not."""
    rows = []
    for m in ["PMSG", "SCIG"]:
        f = sdr[(sdr.machine == m) & (sdr.ftype == "TURNS")]
        for ph, g in f.groupby(f.phases.str[0]):
            for feat in feats:
                col = f"{feat}__sdr"
                if col not in g.columns:
                    continue
                rows.append(dict(machine=m, phase=ph, n_trials=len(g), n_pairs=g.case.nunique(),
                                 extents=", ".join(f"{v:.1f}" for v in sorted(g.sev_pct.unique())), feature=feat,
                                 median_sdr=g[col].median(), ds=(g[col] >= 1).mean()))
    return pd.DataFrame(rows)


def pair_table(sdr, files, feats=PHASE_FEATS):
    """Median SDR per tap pair with its phase, design-level extent, physical level and fault current."""
    fc = files[files.is_fault].groupby(["machine", "case"]).Ifault_rms_flt.median()
    rows = []
    for (m, ft, case), g in sdr[sdr.is_fault].groupby(["machine", "ftype", "case"]):
        r = dict(machine=m, ftype=ft, case=case, phase=g.phases.iloc[0][0], sev_pct=g.sev_pct.iloc[0],
                 level_pct=g.level_pct.iloc[0] if "level_pct" in g.columns else np.nan, n=len(g),
                 Ifault_A=fc.get((m, case), np.nan))
        for feat in feats:
            col = f"{feat}__sdr"
            if col in g.columns:
                r[f"{feat}_median_sdr"] = g[col].median()
                r[f"{feat}_ds"] = (g[col] >= 1).mean()
        rows.append(r)
    return pd.DataFrame(rows).sort_values(["machine", "ftype", "sev_pct"])


# ----------------------------------------------------------------------------- R9-R11 further checks
def null_exceedance_by_speed(win5, feats, key):
    """Share of trials whose healthy relative change exceeds the pooled q95, per machine and speed."""
    sdr, q = sdr_from_windows(win5, feats, q=0.95)
    null = sdr[[f"{f}__null" for f in key]].abs().set_axis(key, axis=1)
    exc = null > q[key].reindex(sdr.machine).set_axis(null.index)
    out = exc.groupby([sdr.machine, sdr.speed_rpm]).mean().reset_index()
    out["n"] = exc[key[0]].groupby([sdr.machine, sdr.speed_rpm]).size().to_numpy()
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
    dV2/dI2 under fault from the magnitude increments (Lee et al. 2003): a current-regulated drive yields a
    large |dV2/dI2|. The complex (phasor-residual) version is computed in z2_complex from the window cache."""
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


def z2_complex(win):
    """Incremental negative-sequence impedance from the phasor residuals: |dV2c| / |dI2c| where dX2c is the complex
    change of the phase-referenced negative-sequence component between the reference and the faulted interval,
    rescaled to volts and amperes by the positive-sequence magnitudes (V1, I1 of the reference interval)."""
    w, pre_e, pre_l, flt = C.interval_means(win, ["I2r_I1", "V2r_V1", "I1", "V1"])
    meta = w.groupby("rid")[["machine", "ftype", "zf_ohm"]].first() if "zf_ohm" in w.columns else w.groupby("rid")[["machine", "ftype"]].first()
    di = ((flt.I2c_re + 1j * flt.I2c_im) - (pre_l.I2c_re + 1j * pre_l.I2c_im)) * pre_l.I1
    dv = ((flt.V2c_re + 1j * flt.V2c_im) - (pre_l.V2c_re + 1j * pre_l.V2c_im)) * pre_l.V1
    z = (dv / di)
    out = meta.join(pd.DataFrame({"dI2c_A": di.abs() / np.sqrt(2), "dV2c_V": dv.abs() / np.sqrt(2), "Z2_ohm": z.abs(),
                                  "Z2_angle_deg": np.degrees(np.angle(z))}))
    rows = []
    for m in MACH:
        for ft in ["TURNS", "WINDINGS"]:
            s = out[(out.machine == m) & (out.ftype == ft)]
            if m == "WFSG" and "zf_ohm" in s.columns:
                s = s[np.isclose(s.zf_ohm, WFSG_ZF_MATCH)]
            if not len(s):
                continue
            rows.append(dict(machine=m, ftype=ft, n=len(s), dI2c_A_rms=s.dI2c_A.median(), dV2c_V_rms=s.dV2c_V.median(),
                             Z2_ohm=s.Z2_ohm.median(), Z2_q25=s.Z2_ohm.quantile(.25), Z2_q75=s.Z2_ohm.quantile(.75),
                             Z2_angle_deg=s.Z2_angle_deg.median()))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R7 commissioning-baseline (between-trial) null
def between_trial(win5, feats, key):
    """PMSG/SCIG, 5-cycle windows. Reference = the healthy trial at the same operating point (recorded at a
    different time) instead of the trial's own preceding interval; the null is the drift of the healthy
    reference intervals of all fault trials relative to that baseline. Residual features use the complex mean."""
    w = win5.replace([np.inf, -np.inf], np.nan)
    cols = [c for c in C.window_cols(feats) if c in w.columns]
    pre = w[w.segment == "PRE"].groupby("rid")[cols].mean()
    flt = w[w.segment == "FLT"].groupby("rid")[cols].mean()
    meta = w.groupby("rid")[["machine", "ftype", "sev_pct", "speed_rpm", "torque_Nm", "case"]].first()

    def cx(df, f):   # complex (residual) or real column of a feature
        if f in C.RESID:
            re_, im_ = C.RESID[f]
            return df[re_] + 1j * df[im_]
        return df[f]

    sdr_w, q_w = sdr_from_windows(win5, feats, q=0.95)
    rows = []
    for m in ["PMSG", "SCIG"]:
        mm = meta[meta.machine == m]
        healthy = mm[mm.ftype == "HEALTHY"]
        base_rid = {(r.speed_rpm, r.torque_Nm): rid for rid, r in healthy.iterrows()}
        faults = mm[mm.ftype != "HEALTHY"]
        brid = [base_rid[(r.speed_rpm, r.torque_Nm)] for _, r in faults.iterrows()]
        for feat in key:
            b = cx(pre.loc[brid], feat).to_numpy()
            x = cx(flt.loc[faults.index], feat).to_numpy()
            p = cx(pre.loc[faults.index], feat).to_numpy()
            delta = np.abs(x - b) / np.abs(b)
            null = np.abs(p - b) / np.abs(b)
            q_b = np.nanquantile(null, 0.95)
            sdr_b = pd.Series(delta / q_b, index=faults.index)
            for ft in ["TURNS", "WINDINGS"]:
                idx = faults.index[faults.ftype == ft]
                rows.append(dict(machine=m, ftype=ft, feature=feat,
                                 q95_within=float(q_w.loc[m, feat]), q95_between=float(q_b),
                                 median_sdr_within=float(sdr_w.loc[idx, f"{feat}__sdr"].median()),
                                 ds_within=float((sdr_w.loc[idx, f"{feat}__sdr"] >= 1).mean()),
                                 median_sdr_between=float(sdr_b.loc[idx].median()),
                                 ds_between=float((sdr_b.loc[idx] >= 1).mean())))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- R8 absolute-change variant
def absolute_variant(win5, feats):
    """SDR with absolute instead of relative changes (no |phi_R| in numerator or null): does the feature
    ranking depend on the baseline level of the feature?"""
    from scipy.stats import spearmanr
    sdr, _ = sdr_from_windows(win5, feats, q=0.95)
    rows = []
    for m in ["PMSG", "SCIG"]:
        allm = sdr[sdr.machine == m]
        q = allm[[f"{f}__nabs" for f in feats]].abs().quantile(0.95).set_axis(feats)
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            ma = (f[[f"{x}__dabs" for x in feats]].abs().set_axis(feats, axis=1) / q).median()
            mr = f[[f"{x}__sdr" for x in feats]].median().set_axis(feats)
            ok = ma.notna() & mr.notna()
            rho = spearmanr(ma[ok], mr[ok]).correlation
            sa = f[[f"{x}__dabs" for x in feats]].abs().set_axis(feats, axis=1) / q
            rows.append(dict(machine=m, ftype=ft, spearman_rank_corr=rho,
                             top3_relative=", ".join(mr[ok].sort_values(ascending=False).index[:3]),
                             top3_absolute=", ".join(ma[ok].sort_values(ascending=False).index[:3]),
                             ds_top_relative=float((f[mr[ok].idxmax() + "__sdr"] >= 1).mean()),
                             ds_top_absolute=float((sa[ma[ok].idxmax()] >= 1).mean())))
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
                if f"{feat}__sdr" not in h.columns:
                    continue
                k = int((h[f"{feat}__sdr"] >= 1).sum())
                if C.screen_flag(k, len(h), 0.95):
                    rows.append(dict(window_cycles=ncyc, machine=m, feature=feat, healthy_false_alarm=k / len(h), n_false=k))
    return pd.DataFrame(rows)


def main():
    files, win = load3()
    feats = [f for f in C3.FEATS3 if f in win.columns or f in C.RESID]
    sdr, qv = sdr_from_windows(win, feats)
    det = per_feature(sdr, feats, qv)

    dec, sel = decision_table(win, feats)
    dec.to_csv(C.TAB / "R_decision_table.csv", index=False)
    sel.to_csv(C.TAB / "R_decision_cheapest.csv", index=False)
    req = requirement_quantities(sdr, det)
    req.to_csv(C.TAB / "R_requirement_quantities.csv", index=False)

    files5, win5 = C.load()
    dec5, sel5 = decision_table(win5, C.ALL_FEATS, machines=["PMSG", "SCIG"])
    dec5.to_csv(C.TAB / "R_decision_table_5c.csv", index=False)
    sel5.to_csv(C.TAB / "R_decision_cheapest_5c.csv", index=False)

    key = ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe", "Vqconv_2fe", "D2_D1", "D2r_D1"]
    dec3 = decomposition(win5, C.ALL_FEATS, key)
    dec3.to_csv(C.TAB / "R_decomposition.csv", index=False)

    sdr5, _ = sdr_from_windows(win5, C.ALL_FEATS, q=0.95)
    ph = phase_table(sdr5)
    ph.to_csv(C.TAB / "R_phase_table.csv", index=False)
    pt = pair_table(sdr5, files5)
    pt.to_csv(C.TAB / "R_pair_table.csv", index=False)
    pt3 = pair_table(sdr, files)
    pt3.to_csv(C.TAB / "R_pair_table_3c.csv", index=False)

    tr3, counts = transfer_oor(win)
    tr3.to_csv(C.TAB / "R_transfer3_oor.csv", index=False)
    counts.to_csv(C.TAB / "R_transfer3_counts.csv")
    tr2 = transfer2_oor(win5)
    tr2.to_csv(C.TAB / "R_transfer2_oor.csv", index=False)

    scr = screen_list()
    scr.to_csv(C.TAB / "R_screened_features.csv", index=False)

    z2 = baselines_and_z2(files)
    z2.to_csv(C.TAB / "R_baselines_z2.csv", index=False)
    z2c = z2_complex(win5)
    z2c.to_csv(C.TAB / "R_z2_complex.csv", index=False)
    bt = between_trial(win5, C.ALL_FEATS, ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe", "D2_D1"])
    bt.to_csv(C.TAB / "R_between_trial_null.csv", index=False)
    av = absolute_variant(win5, C.ALL_FEATS)
    av.to_csv(C.TAB / "R_absolute_variant.csv", index=False)
    ex = null_exceedance_by_speed(win5, C.ALL_FEATS, ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe"])
    ex.to_csv(C.TAB / "R_null_exceedance_by_speed.csv", index=False)
    rk = ranking_similarity(pd.read_csv(C.TAB / "B_sdr_by_feature.csv"))
    rk.to_csv(C.TAB / "R_ranking_similarity.csv", index=False)
    ww = wfsg_windows(files)
    ww.to_csv(C.TAB / "R_wfsg_windows.csv", index=False)
    lev = C.assign_levels(files)
    lev.to_csv(C.TAB / "R_levels.csv", index=False)

    L = ["# Revision re-analyses\n",
         "## R12 inter-turn SDR by faulted phase (5-cycle windows)\n", C.md_table(ph.round(3)),
         "\n## R12 per tap pair (5-cycle windows)\n", C.md_table(pt.round(3)),
         "\n## physical extent levels\n", C.md_table(lev),
         "\n## R9 null exceedance by speed (pooled q95, 5-cycle windows)\n", C.md_table(ex.round(3)),
         "\n## R10 PMSG vs SCIG feature-ranking similarity (5-cycle windows)\n", C.md_table(rk.round(3)),
         "\n## R11 WFSG fault windows per trial (3-cycle windows)\n", C.md_table(ww.round(2)),
         "## R6 healthy baselines and incremental negative-sequence impedance dV2/dI2 (RMS units)\n", C.md_table(z2.round(4)),
         "\n## R6 complex incremental negative-sequence impedance from the phasor residuals\n", C.md_table(z2c.round(3)),
         "\n## R7 within-trial vs commissioning-baseline (between-trial) null, PMSG/SCIG, 5-cycle windows\n", C.md_table(bt.round(3)),
         "\n## R8 relative vs absolute change: feature ranking\n", C.md_table(av.round(3)),
         "## R1 cheapest suite per requirement, 3-cycle windows (meets: P >= 0.95 of {MDE <= e_req and DS(e >= e_req) >= 0.9})\n", C.md_table(sel),
         "\n## R1 full decision table (alpha = 0.95, 3-cycle windows)\n", C.md_table(dec[dec.alpha == 0.95].drop(columns=["alpha"]).round(3)),
         "\n## R1 cheapest suite per requirement, 5-cycle windows (PMSG, SCIG)\n", C.md_table(sel5),
         "\n## R1 full decision table (alpha = 0.95, 5-cycle windows)\n", C.md_table(dec5[dec5.alpha == 0.95].drop(columns=["alpha"]).round(3)),
         "\n## R2 requirement-writable quantities (alpha = 0.95, 3-cycle windows)\n", C.md_table(req.round(3)),
         "\n## R3 SCIG / PMSG ratio decomposition (5-cycle windows), relative and absolute\n", C.md_table(dec3.round(5)),
         "\n## R4 transfer, three alternatives (self-ref, GBDT): all negatives vs out-of-reference negatives, with intervals\n",
         C.md_table(tr3.round(3)), "\n", C.md_table(counts.reset_index()),
         "\n## R4 transfer, PMSG/SCIG (5-cycle windows), four referencing rules\n", C.md_table(tr2.round(3)),
         "\n## R5 features failing the reliability screen\n", C.md_table(scr.round(3))]
    (C.RES / "summary_revision.md").write_text("\n".join(L))
    print(ph.round(2).to_string(index=False))
    print(sel.to_string(index=False))
    print(dec3.round(4).to_string(index=False))
    print(tr3.round(3).to_string(index=False))
    print("done -> results/summary_revision.md")


if __name__ == "__main__":
    main()
