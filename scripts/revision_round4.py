"""Analyses for the second round of external reviews (round 4). PMSG/SCIG five-cycle cache unless stated.

  held_out        the complete procedure (pooled null quantile, screen, fixed-feature selection) fitted on the
                  development tap pairs and frozen, scored on the held-out tap pair; per level, suite and class;
                  leave-one-healthy-trial-out false alarms of the frozen procedure
  by_level        decision table with a requirement-specific selection rule (largest share at the level) against
                  the fixed-feature rule (smallest median-crossing MDE)
  borderline      the primary decision table (alpha = 0.95, trials unit) at 10 000 resamples; cells within two
                  Monte-Carlo standard errors of a verdict boundary at 1000 resamples
  null_reference  empirical null quantile against the parametric reference of the right shape: Rayleigh for the
                  phasor residuals (magnitude of a complex difference), folded normal for the scalar features;
                  kurtosis by speed; MDE under the parametric rule
  absolute        MDE, e90 and fixed feature per suite under the absolute-change variant of the SDR
  pod_fit         log-logistic POD model in extent for the inter-winding fixed features (six levels): a50, a90 and
                  the bootstrap upper bound of a90
  severity_rated  fault current in per unit of the nameplate current per level
  spectrum_60hz   joint least-squares fit of the fundamental and a grid-frequency component to the healthy stator
                  current (raw records): is there a 60 Hz component beside the SCIG's 59.6 Hz fundamental?

Writes results/tables/R4_*.csv, replaces the alpha = 0.95 rows of R_decision_table_5c.csv by the 10 000-resample
values (the 1000-resample table is kept as R_decision_table_5c_B1000.csv), refreshes R3_e90.csv, and writes
results/summary_round4.md."""
import sys
import numpy as np
import pandas as pd
from scipy.stats import kurtosis

import compare as C
import compare3 as C3
import revision as R
import revision_round3 as R3
from compare3 import SUITES3, level_col, mde_bracket, sdr_from_windows, per_feature, unreliable, min_detectable

TAB = C.TAB
KEY = R3.KEY
FIXED = R3.FIXED
RAW = C.ROOT / "data" / "extracted" / "InnovaPower-MitDev-Eletrica-22fdf0b" if hasattr(C, "ROOT") else None


def e90_of(shares_by_level, req=0.9):
    """Smallest tested level from which the share at the level is >= req at every level up (inf if none)."""
    s = shares_by_level.sort_index()
    v = (s >= req).to_numpy()
    for i in range(len(v)):
        if v[i:].all():
            return float(s.index[i])
    return np.inf


# ----------------------------------------------------------------------------- held-out procedure
def held_out(sdr, feats, qv, alpha=0.95):
    rows, fa_rows = [], []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        healthy = rec[~rec.is_fault]
        D = rec[[f"{x}__delta" for x in feats]].abs().set_axis(feats, axis=1)
        N = rec[[f"{x}__null" for x in feats]].abs().set_axis(feats, axis=1)

        def fit(dev_index):
            """Null quantile, screen and per-suite fixed feature (per class) on the development records."""
            qd = N.loc[dev_index].quantile(alpha)
            Sd = D.loc[dev_index].div(qd, axis=1)
            fa = (Sd.loc[healthy.index.intersection(dev_index)] >= 1).sum()
            nh = len(healthy.index.intersection(dev_index))
            bad = {x for x in feats if (not np.isfinite(qd[x])) or qd[x] > 1 or C.screen_flag(int(fa[x]), nh, alpha)}
            best = {}
            for ft in ["TURNS", "WINDINGS"]:
                devf = rec.loc[dev_index]
                devf = devf[devf.ftype == ft].copy()
                for x in feats:
                    devf[f"{x}__sdr"] = Sd.loc[devf.index, x]
                by = level_col(devf)
                for suite, sf in SUITES3.items():
                    if suite.startswith("excitation"):
                        continue
                    sf = [x for x in sf if x not in bad and devf[f"{x}__sdr"].notna().any()]
                    best[(ft, suite)] = C3.select_feature(devf, sf, by) if sf else None
            return qd, best

        # leave-one-tap-pair-out over the fault trials
        for case in sorted(rec[rec.is_fault].case.unique()):
            held = rec[rec.case == case]
            dev_index = rec.index[rec.case != case]
            qd, best = fit(dev_index)
            ft = held.ftype.iloc[0]
            by = level_col(held)
            for suite in SUITES3:
                if suite.startswith("excitation") or best.get((ft, suite)) is None:
                    continue
                x = best[(ft, suite)]
                s = D.loc[held.index, x] / qd[x]
                for rid, v in s.items():
                    rows.append(dict(machine=m, ftype=ft, suite=suite, case=case, level_pct=float(held.loc[rid, by]),
                                     rid=rid, feature=x, detected=bool(v >= 1)))
        # leave-one-healthy-trial-out false alarms of the frozen procedure
        for h in healthy.index:
            dev_index = rec.index[rec.index != h]
            qd, best = fit(dev_index)
            for (ft, suite), x in best.items():
                if x is None:
                    continue
                fa_rows.append(dict(machine=m, ftype=ft, suite=suite, rid=h, feature=x,
                                    false_alarm=bool(D.loc[h, x] / qd[x] >= 1)))
    d = pd.DataFrame(rows)
    fa = pd.DataFrame(fa_rows)
    # in-sample counterpart: the paper's fixed feature on all trials (alpha = 0.95 null, screen on all records)
    qv_all = {m: sdr[sdr.machine == m][[f"{x}__null" for x in feats]].abs().quantile(alpha).set_axis(feats) for m in ["PMSG", "SCIG"]}
    det = per_feature(sdr, feats, qv)
    ins = []
    for m in ["PMSG", "SCIG"]:
        bad = unreliable(det, m, alpha)
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            by = level_col(f)
            for suite, sf in SUITES3.items():
                if suite.startswith("excitation"):
                    continue
                sf = [x for x in sf if x not in bad and f[f"{x}__sdr"].notna().any()]
                x = C3.select_feature(f, sf, by)
                for lv, g in f.groupby(by):
                    ins.append(dict(machine=m, ftype=ft, suite=suite, level_pct=float(lv), feature_in=x,
                                    share_in=float((g[f"{x}__sdr"] >= 1).mean()), n=len(g)))
    ins = pd.DataFrame(ins)
    agg = (d.groupby(["machine", "ftype", "suite", "level_pct"])
           .agg(share_heldout=("detected", "mean"), n_heldout=("detected", "size"),
                features_heldout=("feature", lambda s: "/".join(sorted(set(s)))))
           .reset_index())
    lev = ins.merge(agg, on=["machine", "ftype", "suite", "level_pct"], how="left")
    lev["differs"] = (lev.share_in >= 0.9) != (lev.share_heldout >= 0.9)
    # suite-level: e90 in-sample and held-out, false alarms of the frozen procedure
    su = []
    for (m, ft, s), g in lev.groupby(["machine", "ftype", "suite"]):
        g = g.set_index("level_pct")
        f = fa[(fa.machine == m) & (fa.ftype == ft) & (fa.suite == s)]
        su.append(dict(machine=m, ftype=ft, suite=s, feature_in=g.feature_in.iloc[0],
                       features_heldout="/".join(sorted(set("/".join(g.features_heldout).split("/")))),
                       e90_in=e90_of(g.share_in), e90_heldout=e90_of(g.share_heldout),
                       fa_heldout=int(f.false_alarm.sum()), n_healthy=int(len(f))))
    su = pd.DataFrame(su)
    su["e90_differs"] = su.e90_in != su.e90_heldout
    return lev, su, d


# ----------------------------------------------------------------------------- null references
def null_reference(sdr, feats, alpha=0.95):
    rows = []
    c_ray = np.sqrt(-2 * np.log(1 - alpha)) / np.sqrt(2)     # q_alpha / RMS for a Rayleigh variable
    c_fold = 1.959964 if alpha == 0.95 else np.nan           # q_alpha(|x|) / sigma for a zero-mean normal
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        for x in feats:
            n = rec[f"{x}__null"].dropna()
            n = n[np.isfinite(n)]
            if not len(n):
                continue
            resid = x in C.RESID
            rms = float(np.sqrt(np.mean(n ** 2)))
            q = float(np.quantile(n.abs(), alpha))
            ref = rms * (c_ray if resid else c_fold)
            kurt = float(kurtosis(n if not resid else n, fisher=True))     # of |x| for residuals, of signed x otherwise
            rows.append(dict(machine=m, feature=x, kind="residual (Rayleigh)" if resid else "scalar (folded normal)",
                             n=len(n), q_emp=q, q_ref=ref, ratio=q / ref, excess_kurtosis=kurt,
                             kurtosis_reference=0.245 if resid else 0.0))
    return pd.DataFrame(rows)


def kurtosis_by_speed(sdr, feats=KEY):
    rows = []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        for x in feats:
            for sp, g in rec.groupby("speed_rpm"):
                n = g[f"{x}__null"].dropna()
                n = n[np.isfinite(n)]
                rows.append(dict(machine=m, feature=x, speed_rpm=int(sp), n=len(n),
                                 excess_kurtosis=float(kurtosis(n, fisher=True)), rms=float(np.sqrt(np.mean(n ** 2))),
                                 q95=float(np.quantile(n.abs(), 0.95))))
    return pd.DataFrame(rows)


def mde_parametric(sdr, feats, alpha=0.95):
    """MDE per feature under the SDR and under a parametric rule with the reference of the right shape."""
    ref = null_reference(sdr, feats, alpha).set_index(["machine", "feature"]).q_ref
    rows, summ = [], []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        for ft in ["TURNS", "WINDINGS"]:
            f = rec[rec.ftype == ft].copy()
            by = level_col(f)
            tab = []
            for x in feats:
                if (m, x) not in ref.index or f[f"{x}__sdr"].isna().all():
                    continue
                f[f"{x}__psdr"] = f[f"{x}__delta"].abs() / ref[(m, x)]
                tab.append(dict(machine=m, ftype=ft, feature=x, mde_sdr=mde_bracket(f, f"{x}__sdr", by)[1],
                                mde_param=mde_bracket(f, f"{x}__psdr", by)[1],
                                ds_sdr=float((f[f"{x}__sdr"] >= 1).mean()), ds_param=float((f[f"{x}__psdr"] >= 1).mean())))
            t = pd.DataFrame(tab)
            rows += tab
            eq = ((t.mde_sdr == t.mde_param) | (t.mde_sdr.isna() & t.mde_param.isna())).sum()
            summ.append(dict(machine=m, ftype=ft, n_features=len(t), n_mde_equal=int(eq),
                             n_resid_equal=int(((t.feature.isin(C.RESID)) & ((t.mde_sdr == t.mde_param) | (t.mde_sdr.isna() & t.mde_param.isna()))).sum()),
                             n_resid=int(t.feature.isin(C.RESID).sum())))
    return pd.DataFrame(rows), pd.DataFrame(summ)


# ----------------------------------------------------------------------------- absolute variant
def absolute_verdicts(sdr, feats, qv, alpha=0.95):
    det = per_feature(sdr, feats, qv)
    rows = []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        bad = unreliable(det, m, alpha)
        qa = rec[[f"{x}__nabs" for x in feats]].abs().quantile(alpha).set_axis(feats)
        for ft in ["TURNS", "WINDINGS"]:
            f = rec[rec.ftype == ft].copy()
            by = level_col(f)
            fa = f.copy()
            for x in feats:
                fa[f"{x}__sdr"] = f[f"{x}__dabs"].abs() / qa[x]
            for suite, sf in SUITES3.items():
                if suite.startswith("excitation"):
                    continue
                sf = [x for x in sf if x not in bad and f[f"{x}__sdr"].notna().any()]
                xr, xa = C3.select_feature(f, sf, by), C3.select_feature(fa, sf, by)
                sh_r = f.groupby(by)[f"{xr}__sdr"].apply(lambda s: float((s >= 1).mean()))
                sh_a = fa.groupby(by)[f"{xa}__sdr"].apply(lambda s: float((s >= 1).mean()))
                rows.append(dict(machine=m, ftype=ft, suite=suite, feature_rel=xr, feature_abs=xa,
                                 mde_rel=min_detectable(f, f"{xr}__sdr", by), mde_abs=min_detectable(fa, f"{xa}__sdr", by),
                                 e90_rel=e90_of(sh_r), e90_abs=e90_of(sh_a),
                                 ds_rel=float((f[f"{xr}__sdr"] >= 1).mean()), ds_abs=float((fa[f"{xa}__sdr"] >= 1).mean())))
    d = pd.DataFrame(rows)
    d["changes"] = (d.mde_rel != d.mde_abs) | (d.e90_rel != d.e90_abs)
    return d


# ----------------------------------------------------------------------------- POD model fit
def pod_fit(sdr, B=1000, seed=5):
    from sklearn.linear_model import LogisticRegression
    rng = np.random.RandomState(seed)
    rows = []

    def fit_a(x, y):
        if y.all() or (~y).all():
            return np.nan, np.nan, np.nan
        lr = LogisticRegression(C=1e6, solver="lbfgs", max_iter=1000).fit(x[:, None], y)
        b, a = float(lr.coef_[0, 0]), float(lr.intercept_[0])
        if b <= 0:
            return np.nan, np.nan, np.nan
        a50 = np.exp(-a / b)
        a90 = np.exp((np.log(9) - a) / b)
        return a50, a90, b
    for m, feats in FIXED.items():
        g = sdr[(sdr.machine == m) & (sdr.ftype == "WINDINGS")]
        by = level_col(g)
        g = g[g[by].notna()]
        x = np.log(g[by].to_numpy(float))
        lev = g[by].to_numpy(float)
        for feat in feats:
            y = (g[f"{feat}__sdr"] >= 1).to_numpy()
            a50, a90, slope = fit_a(x, y)
            bs = []
            idx_by_level = [np.flatnonzero(lev == k) for k in np.unique(lev)]
            for _ in range(B):
                idx = np.concatenate([rng.choice(ix, size=len(ix), replace=True) for ix in idx_by_level])
                bs.append(fit_a(x[idx], y[idx])[1])
            bs = np.array(bs, float)
            ok = np.isfinite(bs)
            rows.append(dict(machine=m, feature=feat, n=len(y), share_all=float(y.mean()), a50=a50, a90=a90, slope_log=slope,
                             a90_boot_q95=float(np.quantile(bs[ok], 0.95)) if ok.sum() > 50 else np.nan,
                             n_boot_defined=int(ok.sum()), smallest_level=float(lev.min()),
                             share_smallest=float(y[lev == lev.min()].mean())))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- severity in per unit
def severity_rated(files):
    f = files[files.is_fault & files.machine.isin(["PMSG", "SCIG"])].copy()
    by = "level_pct" if "level_pct" in f.columns else "sev_pct"
    f["Ifault_pu"] = f.Ifault_rms_flt / f.machine.map(C.RATED_A)
    f["Ifault_over_I1"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))
    g = (f.groupby(["machine", "ftype", by]).agg(n=("machine", "size"), Ifault_A=("Ifault_rms_flt", "median"),
                                                 Ifault_pu=("Ifault_pu", "median"), Ifault_over_I1=("Ifault_over_I1", "median"))
         .reset_index().rename(columns={by: "level_pct"}))
    g["rated_A"] = g.machine.map(C.RATED_A)
    return g


# ----------------------------------------------------------------------------- 60 Hz component in the healthy current
def spectrum_60hz(raw_root=None, machines=("SCIG", "PMSG")):
    """Joint least-squares fit of the stator current of every healthy record to a fundamental (frequency free on a
    fine grid) plus a component at the grid frequency (frequency free in 59.8-60.2 Hz), excluding the contactor
    operation (0.95-1.45 s). Reports the amplitude ratio of the two and the variance reduction the second term
    brings; at 1200 and 1500 rpm the two are far apart and the fit is a plain check, at 1800 rpm (SCIG: 59.6 Hz)
    they are 0.4 Hz apart and the 3 s record separates them (T*df = 1.2)."""
    from scipy.io import loadmat
    from pathlib import Path
    root = Path(raw_root) if raw_root else Path("data/extracted/InnovaPower-MitDev-Eletrica-22fdf0b")
    rows = []
    for m in machines:
        for p in sorted((root / f"{m}-3phase-Dataset").glob("HEALTHY_*.mat")):
            d = loadmat(p, squeeze_me=True)
            t = np.asarray(d["t"], float)
            ia = np.asarray(d["Ia"], float)
            keep = (t < 0.95) | (t > 1.45)
            t, ia = t[keep], ia[keep]
            ia = ia - ia.mean()
            fs = 20000.0
            # fundamental from the phase slope, then a fine grid of +-0.3 Hz around it
            fe0, _ = __import__("features").fundamental(np.asarray(d["Ia"], float)[keep], np.asarray(d["Ib"], float)[keep],
                                                         np.asarray(d["Ic"], float)[keep], fs)

            def design(f1, f2=None):
                cols = [np.cos(2 * np.pi * f1 * t), np.sin(2 * np.pi * f1 * t)]
                if f2 is not None:
                    cols += [np.cos(2 * np.pi * f2 * t), np.sin(2 * np.pi * f2 * t)]
                return np.column_stack(cols)

            def rss(f1, f2=None):
                X = design(f1, f2)
                beta, res, *_ = np.linalg.lstsq(X, ia, rcond=None)
                r = ia - X @ beta
                return float(r @ r), beta
            grid1 = fe0 + np.arange(-0.3, 0.3001, 0.01)
            r1 = [rss(f)[0] for f in grid1]
            f1 = float(grid1[int(np.argmin(r1))])
            rss1, beta1 = rss(f1)
            grid2 = np.arange(59.8, 60.2001, 0.01)
            best = None
            for f2 in grid2:
                if abs(f2 - f1) < 0.15:
                    continue
                r, beta = rss(f1, f2)
                if best is None or r < best[0]:
                    best = (r, f2, beta)
            rss2, f2, beta2 = best
            a1 = float(np.hypot(beta2[0], beta2[1]))
            a2 = float(np.hypot(beta2[2], beta2[3]))
            rows.append(dict(machine=m, record=p.name, speed_rpm=int(p.stem.split("_S")[1].split("_")[0]),
                             fe_fit_hz=f1, f_grid_fit_hz=f2, A_fund=a1, A_grid=a2, ratio_grid_to_fund=a2 / a1,
                             rss_reduction_pct=100 * (rss1 - rss2) / rss1))
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- main
def main(run_10k=True):
    files5, win5 = C.load()
    sdr5, qv5 = sdr_from_windows(win5, C.ALL_FEATS, q=0.95)
    feats = [f for f in C.ALL_FEATS if f"{f}__sdr" in sdr5.columns]
    out = {}
    print("== held-out", flush=True)
    out["heldout_levels"], out["heldout_suites"], _trials = held_out(sdr5, feats, qv5)
    print("== null references", flush=True)
    out["null_reference"] = null_reference(sdr5, feats)
    out["kurtosis_by_speed"] = kurtosis_by_speed(sdr5)
    out["mde_parametric"], out["mde_parametric_summary"] = mde_parametric(sdr5, feats)
    print("== absolute", flush=True)
    out["absolute"] = absolute_verdicts(sdr5, feats, qv5)
    print("== pod fit", flush=True)
    out["pod_fit"] = pod_fit(sdr5)
    out["severity_rated"] = severity_rated(files5)
    print("== spectrum", flush=True)
    try:
        out["spectrum_60hz"] = spectrum_60hz()
    except Exception as ex:   # raw data absent
        print("spectrum skipped:", ex)
    print("== decision table, selection by level", flush=True)
    dl, _ = R.decision_table(win5, C.ALL_FEATS, machines=["PMSG", "SCIG"], alphas=[0.95], select="level")
    out["decision_bylevel"] = dl
    if run_10k:
        print("== decision table at 10 000 resamples", flush=True)
        d10, s10 = R.decision_table(win5, C.ALL_FEATS, machines=["PMSG", "SCIG"], alphas=[0.95], B=10000)
        d10.to_csv(TAB / "R_decision_table_5c_B10k.csv", index=False)
        base = pd.read_csv(TAB / "R_decision_table_5c.csv")
        if not (TAB / "R_decision_table_5c_B1000.csv").exists():
            base.to_csv(TAB / "R_decision_table_5c_B1000.csv", index=False)
        b1000 = pd.read_csv(TAB / "R_decision_table_5c_B1000.csv")
        merged = pd.concat([b1000[~np.isclose(b1000.alpha, 0.95)], d10], ignore_index=True).sort_values(["alpha", "machine", "ftype", "suite", "e_req_pct"])
        merged.to_csv(TAB / "R_decision_table_5c.csv", index=False)
        sel = pd.read_csv(TAB / "R_decision_cheapest_5c.csv")
        pd.concat([sel[~np.isclose(sel.alpha, 0.95)], s10], ignore_index=True).to_csv(TAB / "R_decision_cheapest_5c.csv", index=False)
        R3.e90().to_csv(TAB / "R3_e90.csv", index=False)
        # borderline cells: within two Monte-Carlo standard errors of 0.05 or 0.95 at 1000 resamples
        k = ["machine", "ftype", "suite", "e_req_pct"]
        a = b1000[np.isclose(b1000.alpha, 0.95)][k + ["p_meets_level"]].rename(columns={"p_meets_level": "p_1000"})
        b = d10[k + ["p_meets_level"]].rename(columns={"p_meets_level": "p_10000"})
        cmp = a.merge(b, on=k)
        se = np.sqrt(cmp.p_1000 * (1 - cmp.p_1000) / 1000).clip(lower=np.sqrt(0.05 * 0.95 / 1000))
        cmp["borderline_1000"] = (abs(cmp.p_1000 - 0.05) <= 2 * se) | (abs(cmp.p_1000 - 0.95) <= 2 * se)
        se10 = np.sqrt(cmp.p_10000 * (1 - cmp.p_10000) / 10000).clip(lower=np.sqrt(0.05 * 0.95 / 10000))
        cmp["borderline_10000"] = (abs(cmp.p_10000 - 0.05) <= 2 * se10) | (abs(cmp.p_10000 - 0.95) <= 2 * se10)
        cls = lambda p: np.where(p.isna(), "untested", np.where(p >= 0.95, "meets", np.where(p <= 0.05, "fails", "uncertain")))
        cmp["class_1000"], cmp["class_10000"] = cls(cmp.p_1000), cls(cmp.p_10000)
        out["borderline"] = cmp[cmp.borderline_1000 | cmp.borderline_10000 | (cmp.class_1000 != cmp.class_10000)]
    # selection rule comparison on the primary table
    prim = pd.read_csv(TAB / "R_decision_table_5c.csv")
    prim = prim[np.isclose(prim.alpha, 0.95)]
    k = ["machine", "ftype", "suite", "e_req_pct"]
    c = prim[k + ["fixed_feature", "p_meets_level", "ds_at_level"]].merge(
        dl[k + ["fixed_feature", "p_meets_level", "ds_at_level"]], on=k, suffixes=("_mde", "_level"))
    cls = lambda p: np.where(p.isna(), "untested", np.where(p >= 0.95, "meets", np.where(p <= 0.05, "fails", "uncertain")))
    c["class_mde"], c["class_level"] = cls(c.p_meets_level_mde), cls(c.p_meets_level_level)
    out["bylevel_changes"] = c[(c.class_mde != c.class_level) | (c.fixed_feature_mde != c.fixed_feature_level)]
    L = ["# Round-4 analyses (second round of external reviews)\n"]
    for kk, v in out.items():
        v.to_csv(TAB / f"R4_{kk}.csv", index=False)
        if kk not in ("decision_bylevel", "null_reference", "mde_parametric"):
            L += [f"\n## {kk}\n", C.md_table(v.round(3))]
    (C.RES / "summary_round4.md").write_text("\n".join(L))
    for kk in ["heldout_suites", "mde_parametric_summary", "absolute", "pod_fit", "severity_rated", "spectrum_60hz", "borderline", "bylevel_changes"]:
        if kk in out:
            print("==", kk); print(out[kk].round(3).to_string(index=False))


if __name__ == "__main__":
    main(run_10k="--no10k" not in sys.argv)
