"""Analyses for the external reviews (round 3): comparator statistics (per-feature AUC, Cohen's d on the drift
scale) against the SDR ranking and MDE; per-speed null; interval-geometry ablation; reference-horizon MDE;
e90 and e90/95 per suite; null shape (kurtosis); synthetic leakage check of the negative-sequence estimate at
short windows; WFSG pooling bias; POD-curve data; an example feature trace; nested-selection shares at five
cycles. PMSG/SCIG five-cycle cache unless stated. Writes results/tables/R3_*.csv and results/summary_round3.md."""
import numpy as np
import pandas as pd
from scipy.stats import spearmanr, kurtosis, rankdata

import compare as C
import compare3 as C3
import revision as R
from compare3 import SUITES3, level_col, mde_bracket, sdr_from_windows, per_feature, unreliable

TAB = C.TAB
KEY = ["V2r_V1", "I2r_I1", "D2r_D1", "Id_2fe", "PId_2fe", "Vq_2fe"]
FIXED = {"PMSG": ["V2r_V1", "D2r_D1", "I2r_I1"], "SCIG": ["I2r_I1", "D2r_D1", "V2r_V1"]}
LEVELS = {"TURNS": [3.0, 7.5, 11.8], "WINDINGS": [2.8, 10.1, 14.6, 21.9, 35.9, 40.2]}


def auc(pos, neg):
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    pos, neg = pos[np.isfinite(pos)], neg[np.isfinite(neg)]
    if not len(pos) or not len(neg):
        return np.nan
    r = rankdata(np.concatenate([pos, neg]))
    return (r[: len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))


def comparators(sdr, feats):
    """Per machine, class and feature: median SDR, AUC of |delta| (fault trials) against |null| (all records),
    AUC against the nine healthy trials' fault-interval change, Cohen's d on the drift scale, and the MDE under
    the SDR and under a Gaussian-scale rule |delta| >= 1.96 sd(null)."""
    rows, summ = [], []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        healthy = rec[~rec.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = rec[rec.ftype == ft].copy()
            by = level_col(f)
            tab = []
            for feat in feats:
                d = f[f"{feat}__delta"].abs()
                n0 = rec[f"{feat}__null"].abs()
                if d.isna().all() or n0.isna().all():
                    continue
                sd0 = np.nanstd(n0)
                f[f"{feat}__gsdr"] = d / (1.96 * sd0) if sd0 > 0 else np.nan
                lo_s, mde_s = mde_bracket(f, f"{feat}__sdr", by)
                lo_g, mde_g = mde_bracket(f, f"{feat}__gsdr", by)
                tab.append(dict(machine=m, ftype=ft, feature=feat, median_sdr=float(f[f"{feat}__sdr"].median()),
                                auc_vs_null=auc(d, n0), auc_vs_healthy=auc(d, healthy[f"{feat}__delta"].abs()),
                                cohen_d_drift=float((np.nanmean(d) - np.nanmean(n0)) / sd0) if sd0 > 0 else np.nan,
                                mde_sdr=mde_s, mde_gauss=mde_g, ds_sdr=float((f[f"{feat}__sdr"] >= 1).mean()),
                                ds_gauss=float((f[f"{feat}__gsdr"] >= 1).mean())))
            t = pd.DataFrame(tab)
            rows += tab
            top = lambda c: set(t.nlargest(3, c).feature)
            summ.append(dict(machine=m, ftype=ft, n_features=len(t),
                             rho_sdr_auc_null=spearmanr(t.median_sdr, t.auc_vs_null, nan_policy="omit")[0],
                             rho_sdr_auc_healthy=spearmanr(t.median_sdr, t.auc_vs_healthy, nan_policy="omit")[0],
                             rho_sdr_cohen=spearmanr(t.median_sdr, t.cohen_d_drift, nan_policy="omit")[0],
                             top3_shared_auc_null=len(top("median_sdr") & top("auc_vs_null")),
                             top3_shared_cohen=len(top("median_sdr") & top("cohen_d_drift")),
                             n_mde_equal_gauss=int((t.mde_sdr == t.mde_gauss).sum())))
    return pd.DataFrame(rows), pd.DataFrame(summ)


def per_speed_null(sdr, feats=KEY):
    rows = []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        for feat in feats:
            q_sp = rec.groupby("speed_rpm")[f"{feat}__null"].apply(lambda s: np.nanquantile(s.abs(), 0.95))
            q_pool = np.nanquantile(rec[f"{feat}__null"].abs(), 0.95)
            s = rec[rec.is_fault].copy()
            s["sdr_sp"] = s[f"{feat}__delta"].abs() / s.speed_rpm.map(q_sp)
            for ft in ["TURNS", "WINDINGS"]:
                g = s[s.ftype == ft]
                by = level_col(g)
                lo_p, mde_p = mde_bracket(g, f"{feat}__sdr", by)
                lo_s, mde_s = mde_bracket(g, "sdr_sp", by)
                # worst speed: smallest level detected (median >= 1) at every speed
                worst = np.inf
                for lv in sorted(g[by].dropna().unique()):
                    ok = all((g[(g[by] == lv) & (g.speed_rpm == sp)].sdr_sp.median() >= 1) for sp in sorted(g.speed_rpm.unique()))
                    if ok and worst == np.inf:
                        worst = lv
                    if not ok:
                        worst = np.inf
                first = g[by].min()
                rows.append(dict(machine=m, ftype=ft, feature=feat, q95_pooled=q_pool,
                                 **{f"q95_{int(sp)}": v for sp, v in q_sp.items()},
                                 mde_pooled=mde_p, mde_per_speed=mde_s, ds_pooled=float((g[f"{feat}__sdr"] >= 1).mean()),
                                 ds_per_speed=float((g.sdr_sp >= 1).mean()),
                                 ds_at_first_level_1200=float((g[(g[by] == first) & (g.speed_rpm == 1200)].sdr_sp >= 1).mean()),
                                 ds_at_first_level_1200_pooled=float((g[(g[by] == first) & (g.speed_rpm == 1200)][f"{feat}__sdr"] >= 1).mean())))
    return pd.DataFrame(rows)


def interval_ablation(win5, feats=KEY):
    """SDR of the key features under alternative interval geometries on the common bench: baseline; faulted
    interval starting 120 ms after the contactor command (after relay pick-up); first 150 ms of the fault with
    reference halves of 190 ms each (the WFSG geometry)."""
    w = win5.replace([np.inf, -np.inf], np.nan)
    cols = [c for c in C.window_cols(feats) if c in w.columns]
    meta = w.groupby("rid")[["machine", "ftype", "level_pct", "sev_pct"]].first()
    pre, flt = (w.segment == "PRE").to_numpy(), (w.segment == "FLT").to_numpy()
    ts, te = w.t_start.to_numpy(), w.t_end.to_numpy()
    geoms = {
        "baseline": (pre & (te <= 0.62), pre & (ts >= 0.62), flt),
        "strict start (+120 ms)": (pre & (te <= 0.62), pre & (ts >= 0.62), flt & (ts >= 1.12)),
        "WFSG geometry (150 ms fault, 190 ms halves)": (pre & (te <= 0.62) & (ts >= 0.43), pre & (ts >= 0.62) & (te <= 0.81), flt & (ts <= 1.03 + 0.15)),
    }
    rows = []
    for name, (m1, m2, mf) in geoms.items():
        pre_e = w[m1].groupby("rid")[cols].mean()
        pre_l = w[m2].groupby("rid")[cols].mean()
        fl = w[mf].groupby("rid")[cols].mean()
        idx = pre_e.index.intersection(pre_l.index).intersection(fl.index)
        delta, null, _, _ = C.changes(pre_e.loc[idx], pre_l.loc[idx], fl.loc[idx], feats)
        mm = meta.loc[idx]
        for m in ["PMSG", "SCIG"]:
            sel = mm.machine == m
            for feat in feats:
                if feat not in delta.columns:
                    continue
                q = np.nanquantile(null.loc[sel, feat].abs(), 0.95)
                s = pd.DataFrame({"sdr": delta.loc[sel, feat].abs() / q}).join(mm)
                for ft in ["TURNS", "WINDINGS"]:
                    g = s[s.ftype == ft]
                    lo, mde = mde_bracket(g, "sdr", "level_pct")
                    rows.append(dict(geometry=name, machine=m, ftype=ft, feature=feat, n=len(g), q95=q,
                                     median_sdr=float(g.sdr.median()), ds=float((g.sdr >= 1).mean()), mde=mde, mde_lo=lo))
    return pd.DataFrame(rows)


def reference_horizon(win5, feats=KEY):
    """MDE bracket, median SDR and share under the within-trial null (reference immediately before the fault)
    and under the between-trial null (healthy trial at the same operating point recorded at another time)."""
    w = win5.replace([np.inf, -np.inf], np.nan)
    cols = [c for c in C.window_cols(feats) if c in w.columns]
    pre = w[w.segment == "PRE"].groupby("rid")[cols].mean()
    flt = w[w.segment == "FLT"].groupby("rid")[cols].mean()
    meta = w.groupby("rid")[["machine", "ftype", "level_pct", "speed_rpm", "torque_Nm"]].first()

    def cx(df, f):
        if f in C.RESID:
            re_, im_ = C.RESID[f]
            return df[re_] + 1j * df[im_]
        return df[f]
    sdr_w, _ = sdr_from_windows(win5, feats, q=0.95)
    rows = []
    for m in ["PMSG", "SCIG"]:
        mm = meta[meta.machine == m]
        healthy = mm[mm.ftype == "HEALTHY"]
        base = {(r.speed_rpm, r.torque_Nm): rid for rid, r in healthy.iterrows()}
        faults = mm[mm.ftype != "HEALTHY"]
        brid = [base[(r.speed_rpm, r.torque_Nm)] for _, r in faults.iterrows()]
        for feat in feats:
            b = cx(pre.loc[brid], feat).to_numpy(); x = cx(flt.loc[faults.index], feat).to_numpy(); p = cx(pre.loc[faults.index], feat).to_numpy()
            delta = np.abs(x - b) / np.abs(b); null = np.abs(p - b) / np.abs(b)
            sb = pd.DataFrame({"sdr_b": delta / np.nanquantile(null, 0.95)}, index=faults.index).join(faults)
            for ft in ["TURNS", "WINDINGS"]:
                g = sb[sb.ftype == ft]; gw = sdr_w.loc[g.index]
                lo_w, mde_w = mde_bracket(gw, f"{feat}__sdr", "level_pct")
                lo_b, mde_b = mde_bracket(g, "sdr_b", "level_pct")
                rows.append(dict(machine=m, ftype=ft, feature=feat, mde_within=mde_w, mde_between=mde_b,
                                 median_within=float(gw[f"{feat}__sdr"].median()), median_between=float(g.sdr_b.median()),
                                 ds_within=float((gw[f"{feat}__sdr"] >= 1).mean()), ds_between=float((g.sdr_b >= 1).mean())))
    return pd.DataFrame(rows)


def e90(path5=TAB / "R_decision_table_5c.csv"):
    """Per suite: the MDE (median crossing), e90 (smallest tested level with share >= 0.9 at the level) and e90/95
    (smallest level with bootstrap support >= 0.95 for share >= 0.9 at the level), alpha = 0.95."""
    d = pd.read_csv(path5)
    d = d[np.isclose(d.alpha, 0.95) & (d.verdict != "untested")]
    rows = []
    for (m, ft, s), g in d.groupby(["machine", "ftype", "suite"]):
        g = g.sort_values("e_req_pct")
        ok90 = g[g.ds_at_level >= 0.9]
        ok95 = g[g.p_meets_level >= 0.95]
        # monotone: every tested level from the chosen one up must satisfy the rule
        def first_mono(flag):
            v = flag.to_numpy()
            for i in range(len(v)):
                if v[i:].all():
                    return float(g.e_req_pct.iloc[i])
            return np.inf
        rows.append(dict(machine=m, ftype=ft, suite=s, fixed_feature=g.fixed_feature.iloc[0], mde=float(g.mde_monotone_pct.iloc[0]),
                         e90=first_mono(g.ds_at_level >= 0.9), e90_95=first_mono(g.p_meets_level >= 0.95)))
    return pd.DataFrame(rows)


def null_shape(sdr, feats=KEY):
    rows = []
    for m in ["PMSG", "SCIG"]:
        rec = sdr[sdr.machine == m]
        for feat in feats:
            n = rec[f"{feat}__null"].dropna()
            n = n[np.isfinite(n)]
            rows.append(dict(machine=m, feature=feat, n=len(n), excess_kurtosis=float(kurtosis(n, fisher=True)),
                             q95=float(np.quantile(n.abs(), 0.95)), gauss_1p96_sd=float(1.96 * n.std()),
                             ratio_q95_to_gauss=float(np.quantile(n.abs(), 0.95) / (1.96 * n.std()))))
    return pd.DataFrame(rows)


def leakage_check(fs=20000.0, fe=40.0, i2_i1=0.006, cycles=(3, 5, 8), fe_err=(0.0, 0.005, 0.01)):
    """Synthetic three-phase current with a known negative-sequence ratio: the symmetrical-component estimate of
    I2/I1 with a Hann window of n_c cycles, with and without an error in the electrical frequency used."""
    rows = []
    a = np.exp(2j * np.pi / 3)
    for nc in cycles:
        N = int(round(nc * fs / fe))
        n = np.arange(N)
        t = n / fs
        w = np.hanning(N)
        phases = np.array([0, -2 * np.pi / 3, 2 * np.pi / 3])
        # positive sequence 1 A peak, negative sequence i2_i1 with an arbitrary angle, plus a third harmonic
        x = np.stack([np.cos(2 * np.pi * fe * t + p) + i2_i1 * np.cos(2 * np.pi * fe * t - p + 0.7) + 0.02 * np.cos(6 * np.pi * fe * t) for p in phases])
        for err in fe_err:
            f = fe * (1 + err)
            X = (2 / w.sum()) * (x * w) @ np.exp(-2j * np.pi * f * n / fs)
            Xp = (X[0] + a * X[1] + a ** 2 * X[2]) / 3
            Xn = (X[0] + a ** 2 * X[1] + a * X[2]) / 3
            rows.append(dict(cycles=nc, fe_error=err, I2_I1_true=i2_i1, I2_I1_est=float(abs(Xn) / abs(Xp)),
                             bias_rel=float(abs(Xn) / abs(Xp) / i2_i1 - 1)))
    return pd.DataFrame(rows)


def wfsg_pooling(path=TAB / "G_sdr_per_recording_3alt.csv", feats=("V2r_V1", "I2r_I1", "If_2fe")):
    g = pd.read_csv(path)
    w = g[g.machine == "WFSG"]
    rows = []
    for ft in ["TURNS", "WINDINGS"]:
        s = w[w.ftype == ft]
        for f in feats:
            if f"{f}__sdr" not in s.columns:
                continue
            rows.append(dict(ftype=ft, feature=f, median_all=float(s[f"{f}__sdr"].median()),
                             median_2p83=float(s[np.isclose(s.zf_ohm, 2.83)][f"{f}__sdr"].median()),
                             ds_all=float((s[f"{f}__sdr"] >= 1).mean()), ds_2p83=float((s[np.isclose(s.zf_ohm, 2.83)][f"{f}__sdr"] >= 1).mean())))
    return pd.DataFrame(rows)


def pod_data(sdr, B=1000, seed=11):
    """Detectable share at each physical level with a percentile bootstrap over the trials of the level, for the
    fixed features of the two machines (POD-curve data)."""
    rng = np.random.RandomState(seed)
    rows = []
    for m, feats in FIXED.items():
        rec = sdr[(sdr.machine == m) & sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            g = rec[rec.ftype == ft]
            by = level_col(g)
            for feat in feats:
                for lv, s in g.groupby(by):
                    v = (s[f"{feat}__sdr"] >= 1).to_numpy().astype(float)
                    bs = np.array([v[rng.randint(0, len(v), len(v))].mean() for _ in range(B)])
                    rows.append(dict(machine=m, ftype=ft, feature=feat, level_pct=lv, n=len(v), share=v.mean(),
                                     ci_lo=np.quantile(bs, 0.025), ci_hi=np.quantile(bs, 0.975),
                                     median_sdr=float(s[f"{feat}__sdr"].median())))
    return pd.DataFrame(rows)


def trace_example(win5, rid=None):
    """Per-window magnitude of the phase-referenced negative-sequence ratio of voltage and current for one
    PMSG inter-turn trial at the middle level, with interval labels, for the illustration figure."""
    w = win5
    if rid is None:
        cand = w[(w.machine == "PMSG") & (w.ftype == "TURNS") & (w.level_pct == 7.5) & (w.speed_rpm == 1500) & (w.torque_Nm == 6.4)]
        rid = sorted(cand.rid.unique())[0]
    s = w[w.rid == rid].sort_values("t_start")
    out = pd.DataFrame({"rid": rid, "t_start": s.t_start, "t_end": s.t_end, "segment": s.segment,
                        "V2bar_abs": np.abs(s.V2c_re + 1j * s.V2c_im), "I2bar_abs": np.abs(s.I2c_re + 1j * s.I2c_im),
                        "V2c_re": s.V2c_re, "V2c_im": s.V2c_im, "I2c_re": s.I2c_re, "I2c_im": s.I2c_im})
    return out


def nested_5c(sdr):
    rows = []
    det = per_feature(sdr, C.ALL_FEATS, None) if False else None
    for m in ["PMSG", "SCIG"]:
        rec = sdr[(sdr.machine == m) & sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = rec[rec.ftype == ft]
            for suite, sf in SUITES3.items():
                if suite.startswith("excitation"):
                    continue
                sf = [x for x in sf if f"{x}__sdr" in f.columns and f[f"{x}__sdr"].notna().any()]
                if not sf:
                    continue
                rows.append(dict(machine=m, ftype=ft, suite=suite, ds_fixed=float((f[f"{C3.select_feature(f, sf)}__sdr"] >= 1).mean()),
                                 ds_nested=R.nested_share(f, sf)))
    return pd.DataFrame(rows)


def main():
    files5, win5 = C.load()
    sdr5, qv5 = sdr_from_windows(win5, C.ALL_FEATS, q=0.95)
    feats = [f for f in C.ALL_FEATS if f"{f}__sdr" in sdr5.columns]
    out = {}
    out["comparators"], out["comparators_summary"] = comparators(sdr5, feats)
    out["per_speed_null"] = per_speed_null(sdr5)
    out["interval_ablation"] = interval_ablation(win5)
    out["reference_horizon"] = reference_horizon(win5)
    out["e90"] = e90()
    out["null_shape"] = null_shape(sdr5)
    out["leakage"] = leakage_check()
    out["wfsg_pooling"] = wfsg_pooling()
    out["pod"] = pod_data(sdr5)
    out["trace_example"] = trace_example(win5)
    out["nested_5c"] = nested_5c(sdr5)
    L = ["# Round-3 analyses (external reviews)\n"]
    for k, v in out.items():
        v.to_csv(TAB / f"R3_{k}.csv", index=False)
        if k != "trace_example":
            L += [f"\n## {k}\n", C.md_table(v.round(3))]
    (C.RES / "summary_round3.md").write_text("\n".join(L))
    for k in ["comparators_summary", "per_speed_null", "interval_ablation", "reference_horizon", "e90", "null_shape", "leakage", "wfsg_pooling", "nested_5c"]:
        print("==", k); print(out[k].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
