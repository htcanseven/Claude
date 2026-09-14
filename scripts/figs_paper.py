"""Compact manuscript figures (run after compare3.py):
  G_sdr_by_feature_3alt   the feature-ranking figure at a height that fits two thirds of a page
  G_severity_combined     SDR of V2/V1 and I2/I1 against the design-level extent (left) and the physical
                          severity axis (right), three alternatives, in one figure
"""
import os

os.environ["PAPER_FIGS"] = "1"
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import compare as C
import compare3 as C3


def combined(sdr, files, feats=("V2_V1", "I2_I1")):
    f = sdr[sdr.is_fault].join(files.set_index(files.machine + "/" + files.file)[["Ifault_rms_flt", "I1_pre"]])
    f["ratio"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))
    panels = [("extent", "TURNS"), ("extent", "WINDINGS"), ("physical", "TURNS"), ("physical", "WINDINGS")]
    fig, axes = plt.subplots(len(feats), 4, figsize=(10.5, 2.15 * len(feats) + 0.5), sharey=True,
                             gridspec_kw={"hspace": 0.3, "wspace": 0.08})
    rng = np.random.RandomState(0)
    for i, feat in enumerate(feats):
        for j, (axis, ft) in enumerate(panels):
            ax = axes[i, j]
            for m in C3.MACH:
                s = f[(f.machine == m) & (f.ftype == ft)].dropna(subset=[f"{feat}__sdr"])
                if axis == "extent":
                    jit = np.exp((rng.rand(len(s)) - 0.5) * 0.08)
                    ax.plot(s.sev_pct * jit, s[f"{feat}__sdr"].clip(lower=0.02), "o", ms=2.0, alpha=0.28, color=C3.COL3[m], mec="none")
                    for zf, g in s.groupby("zf_ohm"):
                        med = g.groupby("sev_pct")[f"{feat}__sdr"].median()
                        ax.plot(med.index, med.values.clip(0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=5.5, color=C3.COL3[m],
                                mec=C.SURF, mew=0.8, label=m if zf in (2.6, 2.83) else None, zorder=3)
                    ax.set_xticks([2, 3, 5, 10, 20, 40]); ax.set_xticklabels(["2", "3", "5", "10", "20", "40"])
                else:
                    s = s.dropna(subset=["ratio"])
                    for zf, g in s.groupby("zf_ohm"):
                        ax.plot(g.ratio, g[f"{feat}__sdr"].clip(lower=0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=3.0,
                                alpha=0.55, color=C3.COL3[m], mec="none")
                    ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5]); ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "5"])
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.03, 400)
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            if i == 0:
                ax.set_title(f"{C.FT_LABEL[ft]}, {'design-level extent' if axis == 'extent' else 'physical severity'}", fontsize=8.5)
            if j == 0:
                ax.set_ylabel(f"{C.lab(feat)}\nSDR")
            if i == len(feats) - 1:
                ax.set_xlabel("Winding fraction between taps (%)" if axis == "extent" else "Fault current / stator current (RMS)", fontsize=8.5)
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    axes[0, 0].legend(uniq.values(), uniq.keys(), loc="upper left", fontsize=7.5)
    fig.subplots_adjust(top=0.92, bottom=0.14, left=0.07, right=0.99)
    C3.save(fig, "G_severity_combined")


if __name__ == "__main__":
    files, win = C3.load3()
    feats = [f for f in C3.FEATS3 if f in win.columns]
    sdr, qv = C3.sdr_from_windows(win, feats)
    det = C3.per_feature(sdr, feats, qv)
    C3.fig_features(det, feats, figsize=(9.0, 6.6), fsize=7.2)
    combined(sdr, files)
    print("figures written")
