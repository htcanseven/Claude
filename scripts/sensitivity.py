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


def metrics(sdr, feats):
    rows = []
    for m in MACH:
        for ft in ["TURNS", "WINDINGS"]:
            f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
            for feat in feats:
                col = f"{feat}__sdr"
                rows.append(dict(machine=m, ftype=ft, feature=feat, median_sdr=f[col].median(),
                                 share_detectable=(f[col] >= 1).mean(), min_detectable_pct=min_detectable(f, col)))
    return pd.DataFrame(rows)


def load_windows(suffix):
    w = pd.read_csv(C.RES / f"features_windows{suffix}.csv.gz")
    w["rid"] = w.machine + "/" + w.file
    return w


def figure(bs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.6), gridspec_kw={"wspace": 0.35, "width_ratios": [1, 1, 0.9]})
    fig.subplots_adjust(top=0.78, bottom=0.2)
    labels = [f"{ft[:1] + ft[1:].lower()} · {feat}" for ft in ["TURNS", "WINDINGS"] for feat in KEY]
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
        rows.append(metrics(sdr, KEY).assign(null_quantile=q))
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
    # (c) bootstrap (ncyc 5, q 0.95)
    sdr, _ = sdr_from_windows(win5, feats, q=0.95)
    rng = np.random.RandomState(1)
    B = 2000
    rows = []
    for ft in ["TURNS", "WINDINGS"]:
        for feat in KEY:
            col = f"{feat}__sdr"
            samples = {}
            for m in MACH:
                f = sdr[(sdr.machine == m) & (sdr.ftype == ft)]
                v = f[col].to_numpy()
                idx = rng.randint(0, len(v), size=(B, len(v)))
                bs = v[idx]
                samples[m] = dict(median=np.nanmedian(bs, axis=1), share=np.nanmean(bs >= 1, axis=1))
                # MDE: resample operating points within each tap pair
                mde = []
                groups = {k: g[col].to_numpy() for k, g in f.groupby("sev_pct")}
                for b in range(B):
                    meds = {k: np.nanmedian(v_[rng.randint(0, len(v_), len(v_))]) for k, v_ in groups.items()}
                    ok = [k for k, mv in meds.items() if mv >= 1]
                    mde.append(min(ok) if ok else np.nan)
                mde = np.array(mde, dtype=float)
                rows.append(dict(ftype=ft, feature=feat, machine=m,
                                 median_sdr=np.nanmedian(v), median_sdr_ci_lo=np.percentile(samples[m]["median"], 2.5),
                                 median_sdr_ci_hi=np.percentile(samples[m]["median"], 97.5),
                                 share=np.nanmean(v >= 1), share_ci_lo=np.percentile(samples[m]["share"], 2.5),
                                 share_ci_hi=np.percentile(samples[m]["share"], 97.5),
                                 mde=min_detectable(f, col), mde_ci_lo=np.nanpercentile(mde, 2.5), mde_ci_hi=np.nanpercentile(mde, 97.5),
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
