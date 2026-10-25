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
import pandas as pd

import compare as C
import compare3 as C3

W = 5.15   # inches, text width of the sn-jnl class



def combined(sdr, files, feats=("V2_V1", "I2_I1")):
    """SDR against the design-level extent (left) and the physical severity axis (right); one sub-caption under
    every panel, lettering from the rcParams (Computer Modern, 10 pt)."""
    f = sdr[sdr.is_fault].join(files.set_index(files.machine + "/" + files.file)[["Ifault_rms_flt", "I1_pre"]])
    f["ratio"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))
    rows = [(feat, ft) for feat in feats for ft in ["TURNS", "WINDINGS"]]
    fig, axes = plt.subplots(len(rows), 2, figsize=(W, 1.12 * len(rows) + 0.25), sharey="row",
                             gridspec_kw={"hspace": 0.72, "wspace": 0.1})
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
                    ax.plot(s.sev_pct * jit, s[f"{feat}__sdr"].clip(lower=0.02), ".", ms=2.4, alpha=0.25, color=C3.COL3[m], mec="none")
                    for zf, g in s.groupby("zf_ohm"):
                        med = g.groupby("sev_pct")[f"{feat}__sdr"].median()
                        ax.plot(med.index, med.values.clip(0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=5, color=C3.COL3[m],
                                mec=C.SURF, mew=0.6, label=m if zf in (2.6, 2.83) else None, zorder=3)
                else:
                    s = s.dropna(subset=["ratio"])
                    for zf, g in s.groupby("zf_ohm"):
                        ax.plot(g.ratio, g[f"{feat}__sdr"].clip(lower=0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=2.8,
                                alpha=0.5, color=C3.COL3[m], mec="none")
            # the axis quantity is the same down each column, so its label is set once, on the bottom row;
            # the upper rows carry only their tick labels and sub-caption and fit in the row gap
            last = i == len(rows) - 1
            if axis == "extent":
                ax.set_xlim(1.9, 48); ax.set_xticks([2, 3, 5, 10, 20, 40]); ax.set_xticklabels(["2", "3", "5", "10", "20", "40"])
                if last:
                    ax.set_xlabel("Winding fraction between taps (%)")
            else:
                ax.set_xlim(0.08, 8); ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5]); ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "5"])
                if last:
                    ax.set_xlabel("Fault current / stator current (RMS)")
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
            if j == 0:
                ax.set_ylabel("SDR")
            C.subcaption(ax, f"({chr(97 + k)}) {C.lab(feat)}, {C.FT_LABEL[ft].lower()} faults"); k += 1
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    fig.legend(uniq.values(), uniq.keys(), loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.56, 1.0), columnspacing=1.2)
    fig.subplots_adjust(top=0.955, bottom=0.13, left=0.12, right=0.99)
    C3.save(fig, "G_severity_combined")


def severity_physical(sdr, files, feats=("V2r_V1", "I2r_I1"), name="G_severity_physical"):
    """Compact version of `combined`: the SDR of two features against the physical severity axis only, one row per
    feature and one column per fault class (four panels)."""
    f = sdr[sdr.is_fault].join(files.set_index(files.machine + "/" + files.file)[["Ifault_rms_flt", "I1_pre"]])
    f["ratio"] = f.Ifault_rms_flt / (f.I1_pre / np.sqrt(2))
    fig, axes = plt.subplots(len(feats), 2, figsize=(W, 1.55 * len(feats) + 0.55), sharey="row",
                             gridspec_kw={"hspace": 0.62, "wspace": 0.1})
    k = 0
    for i, feat in enumerate(feats):
        for j, ft in enumerate(["TURNS", "WINDINGS"]):
            ax = axes[i, j]
            ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.03, 400)
            for m in C3.MACH:
                s = f[(f.machine == m) & (f.ftype == ft)].dropna(subset=[f"{feat}__sdr", "ratio"])
                for zf, g in s.groupby("zf_ohm"):
                    ax.plot(g.ratio, g[f"{feat}__sdr"].clip(lower=0.02), C3.ZF_MARK.get(round(zf, 2), "o"), ms=2.8,
                            alpha=0.5, color=C3.COL3[m], mec="none", label=m if zf in (2.6, 2.83) else None)
            ax.set_xlim(0.08, 8); ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 5]); ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "5"])
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
            if i == len(feats) - 1:
                ax.set_xlabel("Fault current / stator current (RMS)")
            if j == 0:
                ax.set_ylabel("SDR")
            C.subcaption(ax, f"({chr(97 + k)}) {C.lab(feat)}, {C.FT_LABEL[ft].lower()} faults"); k += 1
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    fig.legend(uniq.values(), uniq.keys(), loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.56, 1.0), columnspacing=1.2)
    fig.subplots_adjust(top=0.9, bottom=0.17, left=0.12, right=0.99)
    C3.save(fig, name)


PHASE_MARK = {"A": "o", "B": "s", "C": "^"}


def pairs_figure(pt, feats=(("V2_V1", "V2r_V1"), ("I2_I1", "I2r_I1")), name="G_pairs_by_phase"):
    """Median SDR per tap pair for inter-turn faults against the design-level extent: magnitude feature (left
    column) against its phasor residual (right column); marker = faulted phase, colour = machine. Shows the
    dependence of the magnitude features on the faulted phase and its removal by the residual."""
    f = pt[pt.ftype == "TURNS"]
    fig, axes = plt.subplots(len(feats), 2, figsize=(W, 1.5 * len(feats) + 1.0), sharey="row", squeeze=False,
                             gridspec_kw={"hspace": 0.7, "wspace": 0.1})
    k = 0
    for i, pair in enumerate(feats):
        for j, feat in enumerate(pair):
            ax = axes[i, j]
            for m in ["PMSG", "SCIG"]:
                s = f[f.machine == m]
                for ph, mk in PHASE_MARK.items():
                    g = s[s.phase == ph]
                    ax.plot(g.sev_pct, g[f"{feat}_median_sdr"].clip(lower=0.02), mk, ms=5, color=C3.COL3[m], mec=C.SURF,
                            mew=0.5, label=f"{m}, phase {ph}", zorder=3)
            ax.axhline(1, color=C.AXIS, lw=0.8, ls="--")
            ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(0.1, 100)
            ax.set_xlim(2.3, 14); ax.set_xticks([3, 5, 8, 12]); ax.set_xticklabels(["3", "5", "8", "12"])
            ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
            ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
            if i == len(feats) - 1:
                ax.set_xlabel("Winding fraction between taps (%)")
            if j == 0:
                ax.set_ylabel("Median SDR per tap pair")
            C.subcaption(ax, f"({chr(97 + k)}) {C.lab(feat)}"); k += 1
    h, l = axes[0, 0].get_legend_handles_labels()
    uniq = dict(zip(l, h))
    fig.legend(uniq.values(), uniq.keys(), loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.56, 1.0),
               columnspacing=1.0, handletextpad=0.3)
    fig.subplots_adjust(top=0.86 if len(feats) > 1 else 0.80, bottom=0.17 if len(feats) > 1 else 0.26, left=0.12, right=0.99)
    C3.save(fig, name)


if __name__ == "__main__":
    files, win = C3.load3()
    feats = [f for f in C3.FEATS3 if f in win.columns or f in C.RESID]
    sdr, qv = C3.sdr_from_windows(win, feats)
    det = C3.per_feature(sdr, feats, qv)
    C3.fig_features(det, feats, figsize=(W, 6.3))
    C3.fig_features(det, feats, figsize=(W, 4.1), fsize=8, name="G_sdr_by_feature_3alt_compact")
    combined(sdr, files, feats=("V2r_V1", "I2r_I1"))
    severity_physical(sdr, files, feats=("V2r_V1", "I2r_I1"))
    pt = pd.read_csv(C.TAB / "R_pair_table.csv")
    pairs_figure(pt)
    pairs_figure(pt, feats=(("V2_V1", "V2r_V1"),), name="G_pairs_by_phase_compact")
    print("figures written")
