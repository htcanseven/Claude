"""Robustness of the PMSG vs SCIG conclusions to the analysis choices, plus bootstrap uncertainty.

  (a) null quantile used in the SDR denominator: 0.90 / 0.95 / 0.99
  (b) window length: 3 / 5 / 8 electrical cycles (features re-extracted with --ncyc)
  (c) bootstrap over recordings: 95 % percentile intervals for the share detectable, the median SDR,
      the PMSG–SCIG difference in median SDR, and the minimum detectable extent (resampling the
      operating-point recordings within each tap pair)

Outputs: results/tables/H_*.csv, results/figures/H_bootstrap.png|pdf, results/summary_sensitivity.md
"""
import numpy as np
import pandas as pd

import compare as C
from compare3 import sdr_from_windows, min_detectable

KEY = ["V2_V1", "I2_I1", "Id_2fe", "PId_2fe", "Vq_2fe"]
MACH = ["PMSG", "SCIG"]


def metrics(sdr, feats, alpha=0.95):
    rows = []
    for m in MACH:
        h = sdr[(sdr.machine == m) & ~sdr.is_fault]
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            for feat in feats:
                col = f"{feat}__sdr"
                k = int((h[col] >= 1).sum())
                rows.append(dict(machine=m, ftype=ft, feature=feat, median_sdr=f[col].median(),
                                 share_detectable=(f[col] >= 1).mean(), min_detectable_pct=min_detectable(f, col),
                                 healthy_false_alarms=k, screened=C.screen_flag(k, len(h), alpha)))
    return pd.DataFrame(rows)


def load_windows(suffix):
    w = pd.read_csv(C.RES / f"features_windows{suffix}.csv.gz")
    w["rid"] = w.machine + "/" + w.file
    w["sev_pct"] = w.sev_pct.round(1)   # pool equal extents from different tap pairs
    return w


def wilson(k, n, z=1.96):
    if n == 0:
        return np.nan, np.nan
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def mde_boot(f, col, B, rng):
    """Resample the operating-point trials within each extent level; monotone-safe MDE per resample."""
    groups = {k: g[col].to_numpy() for k, g in f.groupby("sev_pct")}
    keys = sorted(groups)
    ok = np.zeros((B, len(keys)), dtype=bool)
    for j, k in enumerate(keys):
        v = groups[k]
        ok[:, j] = np.nanmedian(v[rng.randint(0, len(v), size=(B, len(v)))], axis=1) >= 1
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
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), gridspec_kw={"wspace": 0.35, "width_ratios": [1, 1, 0.9]})
    fig.subplots_adjust(top=0.78, bottom=0.2)
    labels = [f"{C.FT_LABEL[ft]} · {C.lab(feat)}" for ft in ["TURNS", "WINDINGS"] for feat in KEY]
    y = np.arange(len(labels))[::-1]
    for ax, col, title in zip(axes[:2], ["median_sdr", "share"], ["Median SDR", "Share detectable"]):
        for m, off in (("PMSG", 0.15), ("SCIG", -0.15)):
            sub = pd.concat([bs[(bs.ftype == ft) & (bs.feature == feat) & (bs.machine == m)] for ft in ["TURNS", "WINDINGS"] for feat in KEY])
            ax.errorbar(sub[col], y + off, xerr=[sub[col] - sub[f"{col}_ci_lo"], sub[f"{col}_ci_hi"] - sub[col]],
                        fmt="o", ms=4, color=C.COL[m], ecolor=C.COL[m], elinewidth=1, capsize=2, label=m)
        ax.set_yticks(y); ax.set_yticklabels(labels if ax is axes[0] else [], fontsize=7.5)
        ax.set_title(title, fontsize=9); ax.grid(axis="y", visible=False)
        if col == "median_sdr":
            ax.set_xscale("log"); ax.axvline(1, color=C.AXIS, lw=0.8, ls="--")
        else:
            ax.set_xlim(0, 1.05); ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
    ax = axes[2]
    sub = pd.concat([bs[(bs.ftype == ft) & (bs.feature == feat) & (bs.machine.str.startswith("SCIG/PMSG"))] for ft in ["TURNS", "WINDINGS"] for feat in KEY])
    ax.errorbar(sub.median_sdr, y, xerr=[sub.median_sdr - sub.median_sdr_ci_lo, sub.median_sdr_ci_hi - sub.median_sdr],
                fmt="o", ms=4, color=C.INK2, ecolor=C.INK2, elinewidth=1, capsize=2)
    ax.axvline(1, color=C.AXIS, lw=0.8, ls="--"); ax.set_xscale("log"); ax.set_yticks(y); ax.set_yticklabels([])
    ax.set_title("SCIG / PMSG ratio of median SDR", fontsize=9); ax.grid(axis="y", visible=False)
    axes[0].legend(loc="lower right", fontsize=7.5)
    C.header(fig, "Recording-level uncertainty of the PMSG–SCIG comparison",
             "Bootstrap over recordings (2000 resamples), 95 % percentile intervals; 5-cycle windows, α = 0.95.", top=0.78)
    C.savefig_both(fig, "H_bootstrap")


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
    # (c) bootstrap (ncyc 5, q 0.95). Median SDR and share: cluster bootstrap over the 12 tap pairs, the same
    # resampled pairs for both machines (matched); Wilson intervals for the shares. MDE: operating-point
    # trials resampled within each extent level. The null quantile is held fixed (estimated from all 225 trials).
    sdr, _ = sdr_from_windows(win5, feats, q=0.95)
    rng = np.random.RandomState(1)
    B = 2000
    rows = []
    for ft in ["TURNS", "WINDINGS"]:
        cases = sorted(sdr[sdr.ftype == ft].case.unique())
        cidx = rng.randint(0, len(cases), size=(B, len(cases)))
        for feat in KEY:
            col = f"{feat}__sdr"
            samples = {}
            for m in MACH:
                f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
                v = f[col].to_numpy()
                percase = [f[f.case == c][col].to_numpy() for c in cases]
                med = np.empty(B)
                share = np.empty(B)
                for b in range(B):
                    vv = np.concatenate([percase[i] for i in cidx[b]])
                    med[b] = np.nanmedian(vv)
                    share[b] = np.nanmean(vv >= 1)
                samples[m] = dict(median=med, share=share)
                mde = mde_boot(f, col, B, rng)
                k = int((v >= 1).sum())
                wl, wh = wilson(k, len(v))
                rows.append(dict(ftype=ft, feature=feat, machine=m,
                                 median_sdr=np.nanmedian(v), median_sdr_ci_lo=np.percentile(med, 2.5),
                                 median_sdr_ci_hi=np.percentile(med, 97.5),
                                 share=np.nanmean(v >= 1), share_ci_lo=np.percentile(share, 2.5),
                                 share_ci_hi=np.percentile(share, 97.5), share_wilson_lo=wl, share_wilson_hi=wh,
                                 mde=min_detectable(f, col), mde_ci_lo=np.nanpercentile(mde, 2.5) if np.isfinite(mde).any() else np.nan,
                                 mde_ci_hi=np.nanpercentile(mde, 97.5) if np.isfinite(mde).any() else np.nan,
                                 mde_undetectable_frac=np.mean(np.isnan(mde))))
            diff = np.log(samples["SCIG"]["median"]) - np.log(samples["PMSG"]["median"])
            rows.append(dict(ftype=ft, feature=feat, machine="SCIG/PMSG ratio of medians",
                             median_sdr=np.exp(np.median(diff)), median_sdr_ci_lo=np.exp(np.percentile(diff, 2.5)),
                             median_sdr_ci_hi=np.exp(np.percentile(diff, 97.5)),
                             share=samples["SCIG"]["share"].mean() - samples["PMSG"]["share"].mean(),
                             share_ci_lo=np.percentile(samples["SCIG"]["share"] - samples["PMSG"]["share"], 2.5),
                             share_ci_hi=np.percentile(samples["SCIG"]["share"] - samples["PMSG"]["share"], 97.5)))
    bs = pd.DataFrame(rows)
    bs.to_csv(C.TAB / "H_bootstrap.csv", index=False)
    figure(bs)

    L = ["# Sensitivity and uncertainty (PMSG vs SCIG)\n",
         "## (a) Null quantile in the SDR denominator\n", C.md_table(qa.round(3)),
         "\n## (b) Window length\n", C.md_table(wb.round(3)),
         "\n## (c) Bootstrap over recordings (2000 resamples, 95 % percentile intervals)\n", C.md_table(bs.round(3))]
    (C.RES / "summary_sensitivity.md").write_text("\n".join(L))
    print(bs.round(3).to_string(index=False))
    print("done -> results/summary_sensitivity.md")


if __name__ == "__main__":
    main()
