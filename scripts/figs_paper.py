"""Manuscript figures drawn at the final text width of the journal template (about 13.1 cm) so that the
lettering stays at 7.5-9 pt in print (Springer artwork guidelines: 8-12 pt):
  G_sdr_by_feature_3alt   feature ranking, three alternatives
  G_severity_combined     SDR of V2/V1 and I2/I1 against the design-level extent (left column) and the
                          physical severity axis (right column), three alternatives, panels a-h
Run after compare3.py.
"""
import os

os.environ["PAPER_FIGS"] = "1"
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import compare as C
import compare3 as C3

W = 5.15   # inches, text width of the sn-jnl class
FS = 7.5


def panel_letter(ax, k):
    ax.text(0.015, 0.97, f"({chr(97 + k)})", transform=ax.transAxes, ha="left", va="top", fontsize=FS + 0.5,
            fontweight="bold", color=C.INK)


def combined(sdr, files, feats=("V2_V1", "I2_I1")):
    f = sdr[sdr.is_fault].join(files.set_index(files.machine + "/" + files.file)[["Ifault_rms_flt", "I1_pre"]])
    f["ratio"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))
    rows = [(feat, ft) for feat in feats for ft in ["TURNS", "WINDINGS"]]
    fig, axes = plt.subplots(len(rows), 2, figsize=(W, 1.22 * len(rows) + 0.45), sharey="row",
                             gridspec_kw={"hspace": 0.32, "wspace": 0.06})
    rng = np.random.RandomState(0)
    k = 0
    for i, (feat, ft) in enumerate(rows):
        for j, axis in enumerate(["extent", "physical"]):
            ax = axes[i, j]
            ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.03, 400)
            for m in C3.MACH:
                s = f[(f.machine == m) & (f.ftype == ft)].dropna(subset=[f"{feat}__sdr"])
                if axis == "extent":
                    jit = np.exp((rng.rand(len(s)) - 0.5) * 0.08)
                    ax.plot(s.sev_pct * jit, s[f"{feat}__sdr"].clip(lower=0.02), ".", ms=2.2, alpha=0.25, color=C3.COL3[m], mec="none")
                    for zf, g in s.groupby("zf_ohm"):
                        med = g.groupby("sev_pct")[f"{feat}__sdr"].median()
                        ax.plot(med.index, med.values.clip(0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=4.5, color=C3.COL3[m],
                                mec=C.SURF, mew=0.6, label=m if zf in (2.6, 2.83) else None, zorder=3)
                else:
                    s = s.dropna(subset=["ratio"])
                    for zf, g in s.groupby("zf_ohm"):
                        ax.plot(g.ratio, g[f"{feat}__sdr"].clip(lower=0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=2.6,
                                alpha=0.5, color=C3.COL3[m], mec="none")
            if axis == "extent":
                ax.set_xlim(1.9, 48); ax.set_xticks([2, 3, 5, 10, 20, 40]); ax.set_xticklabels(["2", "3", "5", "10", "20", "40"], fontsize=FS)
            else:
                ax.set_xlim(0.08, 8); ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5]); ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "5"], fontsize=FS)
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.tick_params(axis="y", labelsize=FS)
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
            panel_letter(ax, k); k += 1
            if j == 0:
                ax.set_ylabel(f"{C.lab(feat)}, {C.FT_LABEL[ft].lower()}\nSDR", fontsize=FS)
            if i == 0:
                ax.set_title("Design-level extent" if axis == "extent" else "Physical severity", fontsize=FS + 1)
            if i == len(rows) - 1:
                ax.set_xlabel("Winding fraction between taps (%)" if axis == "extent" else "Fault current / stator current (RMS)", fontsize=FS)
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    axes[0, 0].legend(uniq.values(), uniq.keys(), loc="lower right", fontsize=FS - 0.5, handletextpad=0.3, ncol=3, columnspacing=0.8)
    fig.subplots_adjust(top=0.95, bottom=0.085, left=0.13, right=0.99)
    C3.save(fig, "G_severity_combined")


if __name__ == "__main__":
    files, win = C3.load3()
    feats = [f for f in C3.FEATS3 if f in win.columns]
    sdr, qv = C3.sdr_from_windows(win, feats)
    det = C3.per_feature(sdr, feats, qv)
    C3.fig_features(det, feats, figsize=(W, 4.6), fsize=FS)
    combined(sdr, files)
    print("figures written")
