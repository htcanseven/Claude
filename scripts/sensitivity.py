"""Robustness of the PMSG vs SCIG conclusions to the analysis choices, plus bootstrap uncertainty.

  (a) null quantile used in the SDR denominator: 0.90 / 0.95 / 0.99
  (b) window length: 3 / 5 / 8 electrical cycles (features re-extracted with --ncyc)
  (c) bootstrap over recordings: 95 % percentile intervals for the share detectable, the median SDR, the
      SCIG/PMSG ratio of median SDR and the minimum detectable extent. Tap pairs are the resampling unit for the
      median SDR and the share (the same resampled pairs for both machines); operating-point trials within each
      physical extent level for the MDE. In every resample the null quantile is re-estimated from a cluster
      resample of all recordings of the machine (24 tap pairs + the healthy set), so the intervals carry the
      sampling variability of the denominator as well as of the numerator.
  (d) the sampling interval of the null quantile itself (cluster and iid bootstrap)

Outputs: results/tables/H_*.csv, results/figures/H_bootstrap.png|pdf, results/summary_sensitivity.md
"""
import numpy as np
import pandas as pd

import compare as C
from compare3 import sdr_from_windows, min_detectable, level_col

KEY = ["V2_V1", "V2r_V1", "I2_I1", "I2r_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]
MACH = ["PMSG", "SCIG"]
B = 2000


def metrics(sdr, feats, alpha=0.95):
    rows = []
    for m in MACH:
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            for feat in feats:
                col = f"{feat}__sdr"
                if col not in f.columns:
                    continue
                k = int((h[col] >= 1).sum())
                rows.append(dict(machine=m, ftype=ft, feature=feat, median_sdr=f[col].median(),
                                 share_detectable=(f[col] >= 1).mean(), min_detectable_pct=min_detectable(f, col),
                                 healthy_false_alarms=k, screened=C.screen_flag(k, len(h), alpha)))
    return pd.DataFrame(rows)


def load_windows(suffix):
    files = pd.read_csv(C.RES / f"features_files{suffix}.csv")
    files["is_fault"] = files.ftype != "HEALTHY"
    files["sev_pct"] = files.sev_pct.round(1)
    w = pd.read_csv(C.RES / f"features_windows{suffix}.csv.gz")
    w["rid"] = w.machine + "/" + w.file
    w["sev_pct"] = w.sev_pct.round(1)   # pool equal extents from different tap pairs
    files, w, _ = C.add_levels(files, w)
    return w


def wilson(k, n, z=1.96):
    if n == 0:
        return np.nan, np.nan
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def null_clusters(sdr, m, feat):
    """|null| values of feature `feat` for every recording of machine m, grouped by resampling cluster (tap pair, or
    the healthy set)."""
    r = sdr[sdr.machine == m]
    cl = np.where(r.is_fault, r.case.astype(str), "HEALTHY")
    v = r[f"{feat}__null"].abs().to_numpy()
    return {c: v[cl == c] for c in np.unique(cl)}


def resample_null_q(clusters, rng, q=0.95, B=B, fixed=None):
    """q-quantile of |null| in B cluster resamples; `fixed` = clusters whose resample is imposed (the class's own
    tap pairs, resampled jointly with the numerator) as a list of cluster names per resample."""
    names = sorted(clusters)
    out = np.empty(B)
    for b in range(B):
        if fixed is not None:
            free = [c for c in names if c not in fixed["pool"]]
            pick = list(fixed["draws"][b]) + list(rng.choice(free, size=len(free), replace=True))
        else:
            pick = rng.choice(names, size=len(names), replace=True)
        vals = np.concatenate([clusters[c] for c in pick])
        out[b] = np.nanquantile(vals, q)
    return out


def mde_boot(f, dcol, nq, B, rng, by):
    """Resample the operating-point trials within each physical level and, per resample, divide the absolute
    relative changes by the resampled null quantile nq[b]; monotone-safe MDE per resample."""
    groups = {k: g[dcol].abs().to_numpy() for k, g in f.groupby(by)}
    keys = sorted(groups)
    ok = np.zeros((B, len(keys)), dtype=bool)
    for j, k in enumerate(keys):
        v = groups[k]
        med = np.nanmedian(v[rng.randint(0, len(v), size=(B, len(v)))], axis=1)
        ok[:, j] = med / nq >= 1
    suffix_ok = np.flip(np.cumprod(np.flip(ok, axis=1), axis=1), axis=1).astype(bool)
    out = np.full(B, np.nan)
    for b in range(B):
        w = np.where(suffix_ok[b])[0]
        if len(w):
            out[b] = keys[w[0]]
    return out


def figure(bs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    key = [k for k in KEY if k in set(bs.feature)]
    fig, axes = plt.subplots(3, 1, figsize=(5.15, 8.2), gridspec_kw={"hspace": 0.55})
    labels = [f"{C.FT_LABEL[ft]}, {C.lab(feat)}" for ft in ["TURNS", "WINDINGS"] for feat in key]
    y = np.arange(len(labels))[::-1]
    for ax, col, cap in zip(axes[:2], ["median_sdr", "share"], ["(a) Median SDR", "(b) Share of trials detectable"]):
        for m, off in (("PMSG", 0.15), ("SCIG", -0.15)):
            sub = pd.concat([bs[(bs.ftype == ft) & (bs.feature == feat) & (bs.machine == m)] for ft in ["TURNS", "WINDINGS"] for feat in key])
            ax.errorbar(sub[col], y + off, xerr=[sub[col] - sub[f"{col}_ci_lo"], sub[f"{col}_ci_hi"] - sub[col]],
                        fmt=C.MARK[m], ms=4, color=C.COL[m], ecolor=C.COL[m], elinewidth=1, capsize=2, label=m)
        ax.set_yticks(y); ax.set_yticklabels(labels); ax.grid(axis="y", visible=False)
        if col == "median_sdr":
            ax.set_xscale("log"); ax.axvline(1, color=C.AXIS, lw=0.8, ls="--"); ax.set_xlabel("Median SDR")
        else:
            ax.set_xlim(0, 1.05); ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
            ax.set_xlabel("Share of trials with SDR $\\geq 1$")
        C.subcaption(ax, cap)
    ax = axes[2]
    sub = pd.concat([bs[(bs.ftype == ft) & (bs.feature == feat) & (bs.machine.str.startswith("SCIG/PMSG"))] for ft in ["TURNS", "WINDINGS"] for feat in key])
    ax.errorbar(sub.median_sdr, y, xerr=[sub.median_sdr - sub.median_sdr_ci_lo, sub.median_sdr_ci_hi - sub.median_sdr],
                fmt="o", ms=4, color=C.INK2, ecolor=C.INK2, elinewidth=1, capsize=2)
    ax.axvline(1, color=C.AXIS, lw=0.8, ls="--"); ax.set_xscale("log"); ax.set_yticks(y); ax.set_yticklabels(labels)
    ax.grid(axis="y", visible=False); ax.set_xlabel("SCIG / PMSG ratio of median SDR")
    C.subcaption(ax, "(c) SCIG/PMSG ratio of median SDR")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.62, 1.0))
    fig.subplots_adjust(left=0.34, right=0.98, top=0.965, bottom=0.07)
    C.savefig_both(fig, "H_bootstrap")


def bootstrap(sdr, key, rng, B=B):
    """(c): cluster bootstrap over tap pairs with the null re-estimated in every resample."""
    rows = []
    for ft in ["TURNS", "WINDINGS"]:
        cases = sorted(sdr[(sdr.ftype == ft) & sdr.is_fault].case.unique())
        cidx = rng.randint(0, len(cases), size=(B, len(cases)))
        draws = [[cases[i] for i in cidx[b]] for b in range(B)]
        for feat in key:
            dcol, col = f"{feat}__delta", f"{feat}__sdr"
            if col not in sdr.columns:
                continue
            samples = {}
            for m in MACH:
                f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
                v = f[col].to_numpy()
                percase = {c: f[f.case == c][dcol].abs().to_numpy() for c in cases}
                clusters = null_clusters(sdr, m, feat)
                nq = resample_null_q(clusters, rng, 0.95, B, fixed=dict(pool=set(cases), draws=draws))
                med, share = np.empty(B), np.empty(B)
                for b in range(B):
                    vv = np.concatenate([percase[c] for c in draws[b]]) / nq[b]
                    med[b] = np.nanmedian(vv)
                    share[b] = np.nanmean(vv >= 1)
                samples[m] = dict(median=med, share=share)
                by = level_col(f)
                nq_free = resample_null_q(clusters, rng, 0.95, B)
                mde = mde_boot(f, dcol, nq_free, B, rng, by)
                k = int((v >= 1).sum())
                wl, wh = wilson(k, len(v))
                rows.append(dict(ftype=ft, feature=feat, machine=m,
                                 median_sdr=np.nanmedian(v), median_sdr_ci_lo=np.percentile(med, 2.5),
                                 median_sdr_ci_hi=np.percentile(med, 97.5),
                                 share=np.nanmean(v >= 1), share_ci_lo=np.percentile(share, 2.5),
                                 share_ci_hi=np.percentile(share, 97.5), share_wilson_lo=wl, share_wilson_hi=wh,
                                 mde=min_detectable(f, col), mde_ci_lo=np.nanpercentile(mde, 2.5) if np.isfinite(mde).any() else np.nan,
                                 mde_ci_hi=np.nanpercentile(mde, 97.5) if np.isfinite(mde).any() else np.nan,
                                 mde_undetectable_frac=np.mean(np.isnan(mde)),
                                 null_q95=np.nanquantile(sdr[sdr.machine == m][f"{feat}__null"].abs(), 0.95),
                                 null_q95_ci_lo=np.percentile(nq_free, 2.5), null_q95_ci_hi=np.percentile(nq_free, 97.5)))
            diff = np.log(samples["SCIG"]["median"]) - np.log(samples["PMSG"]["median"])
            # point estimate = ratio of the full-sample medians (the same estimator as the decomposition table);
            # interval from the matched tap-pair resamples
            p_med = {m: np.nanmedian(sdr[(sdr.machine == m) & (sdr.ftype == ft)][col]) for m in MACH}
            rows.append(dict(ftype=ft, feature=feat, machine="SCIG/PMSG ratio of medians",
                             median_sdr=p_med["SCIG"] / p_med["PMSG"], median_sdr_ci_lo=np.exp(np.percentile(diff, 2.5)),
                             median_sdr_ci_hi=np.exp(np.percentile(diff, 97.5)),
                             share=samples["SCIG"]["share"].mean() - samples["PMSG"]["share"].mean(),
                             share_ci_lo=np.percentile(samples["SCIG"]["share"] - samples["PMSG"]["share"], 2.5),
                             share_ci_hi=np.percentile(samples["SCIG"]["share"] - samples["PMSG"]["share"], 97.5)))
    return pd.DataFrame(rows)


def null_quantile_ci(sdr, key, rng, B=B):
    """(d): sampling interval of the null quantile q95 per machine and feature, cluster and iid bootstrap."""
    rows = []
    for m in MACH:
        for feat in key:
            if f"{feat}__null" not in sdr.columns:
                continue
            clusters = null_clusters(sdr, m, feat)
            allv = np.concatenate(list(clusters.values()))
            cl = resample_null_q(clusters, rng, 0.95, B)
            iid = np.array([np.nanquantile(allv[rng.randint(0, len(allv), len(allv))], 0.95) for _ in range(B)])
            q = np.nanquantile(allv, 0.95)
            # Gaussian reference and kurtosis on the SIGNED relative change (a residual feature's null is a
            # magnitude by construction, so the comparison does not apply to it)
            signed = sdr[sdr.machine == m][f"{feat}__null"].dropna().to_numpy()
            scalar = feat not in C.RESID
            rows.append(dict(machine=m, feature=feat, n=len(allv), q95=q,
                             cluster_ci_lo=np.percentile(cl, 2.5), cluster_ci_hi=np.percentile(cl, 97.5),
                             iid_ci_lo=np.percentile(iid, 2.5), iid_ci_hi=np.percentile(iid, 97.5),
                             ratio_hi_lo_cluster=np.percentile(cl, 97.5) / np.percentile(cl, 2.5),
                             q95_over_1p96sd=q / (1.96 * np.nanstd(signed)) if scalar else np.nan,
                             excess_kurtosis=float(pd.Series(signed).kurt()) if scalar else np.nan))
    return pd.DataFrame(rows)


def main():
    feats = C.ALL_FEATS
    win5 = load_windows("")
    # (a) null quantile
    rows = []
    for q in [0.90, 0.95, 0.99]:
        sdr, _ = sdr_from_windows(win5, feats, q=q)
        rows.append(metrics(sdr, KEY, alpha=q).assign(null_quantile=q))
    qa = pd.concat(rows)
    qa.to_csv(C.TAB / "H_sensitivity_quantile.csv", index=False)
    # (b) window length
    rows = []
    for ncyc, suffix in [(3, "_ncyc3"), (5, ""), (8, "_ncyc8")]:
        try:
            w = load_windows(suffix)
        except FileNotFoundError:
            print("missing", suffix)
            continue
        sdr, _ = sdr_from_windows(w, feats, q=0.95)
        rows.append(metrics(sdr, KEY).assign(window_cycles=ncyc))
    wb = pd.concat(rows)
    wb.to_csv(C.TAB / "H_sensitivity_window.csv", index=False)
    # (c) bootstrap (ncyc 5, q 0.95) with the null re-estimated in every resample
    sdr, _ = sdr_from_windows(win5, feats, q=0.95)
    rng = np.random.RandomState(1)
    bs = bootstrap(sdr, KEY, rng)
    bs.to_csv(C.TAB / "H_bootstrap.csv", index=False)
    figure(bs)
    # (d) null quantile sampling interval
    nq = null_quantile_ci(sdr, KEY, np.random.RandomState(2))
    nq.to_csv(C.TAB / "H_null_quantile_ci.csv", index=False)

    L = ["# Sensitivity and uncertainty (PMSG vs SCIG)\n",
         "## (a) Null quantile in the SDR denominator\n", C.md_table(qa.round(3)),
         "\n## (b) Window length\n", C.md_table(wb.round(3)),
         "\n## (c) Bootstrap over recordings (2000 resamples, 95 % percentile intervals, null re-estimated per resample)\n",
         C.md_table(bs.round(3)),
         "\n## (d) Sampling interval of the null quantile q95\n", C.md_table(nq.round(3))]
    (C.RES / "summary_sensitivity.md").write_text("\n".join(L))
    print(bs.round(3).to_string(index=False))
    print(nq.round(3).to_string(index=False))
    print("done -> results/summary_sensitivity.md")


if __name__ == "__main__":
    main()
