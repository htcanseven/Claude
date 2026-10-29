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


def trace_figure(path=None, name="G_sdr_illustration"):
    """Illustration of the SDR on one trial: per window, the relative deviation of the phase-referenced
    negative-sequence ratio from its mean over R2, for the terminal voltage and the stator current; the bars give
    the healthy change (R1 against R2) and the change under fault (F against R2), the dashed line the machine's
    null quantile, so that SDR is the ratio of the second bar to the dashed line."""
    t = pd.read_csv(path or (C.TAB / "R3_trace_example.csv"))
    t = t[t.segment.isin(["PRE", "FLT"])].copy()
    r1 = (t.segment == "PRE") & (t.t_end <= 0.62)
    r2 = (t.segment == "PRE") & (t.t_start >= 0.62)
    fl = t.segment == "FLT"
    q = {"V": 0.123, "I": 0.242}   # PMSG null quantiles of the two residual features, five-cycle windows
    fig, axes = plt.subplots(2, 1, figsize=(W, 3.2), sharex=True, gridspec_kw={"hspace": 0.3})
    for ax, key, lab in zip(axes, ["V", "I"], [r"$|\bar V_2 - \bar V_{2,R_2}|/|\bar V_{2,R_2}|$", r"$|\bar I_2 - \bar I_{2,R_2}|/|\bar I_{2,R_2}|$"]):
        z = t[f"{key}2c_re"].to_numpy() + 1j * t[f"{key}2c_im"].to_numpy()
        m1, m2, mf = z[r1].mean(), z[r2].mean(), z[fl].mean()
        dev = np.abs(z - m2) / abs(m2)
        tm = 0.5 * (t.t_start + t.t_end)
        ax.axvspan(t.t_start[r1].min(), t.t_end[r1].max(), color=C3.COL3["PMSG"], alpha=0.08, lw=0)
        ax.axvspan(t.t_start[r2].min(), t.t_end[r2].max(), color=C3.COL3["PMSG"], alpha=0.16, lw=0)
        ax.axvspan(t.t_start[fl].min(), t.t_end[fl].max(), color=C3.COL3["SCIG"], alpha=0.12, lw=0)
        ax.plot(tm, dev, ".-", ms=3, lw=0.8, color=C.AXIS)
        d0, d = abs(m1 - m2) / abs(m2), abs(mf - m2) / abs(m2)
        ax.hlines(d0, t.t_start[r1].min(), t.t_end[r1].max(), color=C3.COL3["PMSG"], lw=1.8)
        ax.hlines(d, t.t_start[fl].min(), t.t_end[fl].max(), color=C3.COL3["SCIG"], lw=1.8)
        ax.axhline(q[key], color=C.AXIS, lw=0.8, ls="--")
        ax.text(1.395, d, f"$\\delta$ = {d:.2f}", ha="right", va="bottom", fontsize=8, color=C3.COL3["SCIG"])
        ax.text(0.305, d0, f"$\\delta^0$ = {d0:.2f}", ha="left", va="top", fontsize=8, color=C3.COL3["PMSG"])
        ax.text(0.97, q[key], f"$q_{{0.95}}$ = {q[key]:.2f}", ha="right", va="bottom", fontsize=8, color=C.AXIS)
        ax.set_ylabel(lab, fontsize=8)
        ax.set_xlim(0.25, 1.42)
        ax.set_ylim(0, max(dev.max(), q[key]) * 1.25)
    y0 = axes[0].get_ylim()[1]
    for x, s in [(0.46, "$R_1$"), (0.80, "$R_2$"), (1.21, "$F$")]:
        axes[0].text(x, y0 * 0.98, s, ha="center", va="top", fontsize=9)
    axes[1].set_xlabel("Time (s)")
    fig.subplots_adjust(top=0.97, bottom=0.16, left=0.15, right=0.98)
    C3.save(fig, name)


def pod_figure(path=None, name="G_pod"):
    """Detectable share of the fixed features at each physical extent level with 95 % bootstrap intervals
    (probability-of-detection curves on the tested grid), PMSG and SCIG, five-cycle windows."""
    p = pd.read_csv(path or (C.TAB / "R3_pod.csv"))
    fig, axes = plt.subplots(1, 2, figsize=(W, 2.6), gridspec_kw={"wspace": 0.12}, sharey=True)
    marks = {"V2r_V1": "o", "I2r_I1": "s", "D2r_D1": "^"}
    for ax, ft in zip(axes, ["TURNS", "WINDINGS"]):
        for m in ["PMSG", "SCIG"]:
            for f, mk in marks.items():
                s = p[(p.machine == m) & (p.ftype == ft) & (p.feature == f)].sort_values("level_pct")
                if not len(s):
                    continue
                off = 1.0 + (0.025 if m == "SCIG" else -0.025) + {"V2r_V1": -0.01, "I2r_I1": 0.0, "D2r_D1": 0.01}[f]
                x = s.level_pct * off
                ax.errorbar(x, s.share, yerr=[s.share - s.ci_lo, s.ci_hi - s.share], fmt=mk, ms=4, color=C3.COL3[m],
                            mec=C.SURF, mew=0.5, lw=0.8, capsize=0, label=f"{m}, {C.lab(f)}")
                ax.plot(x, s.share, "-", lw=0.7, color=C3.COL3[m], alpha=0.6)
        ax.axhline(0.9, color=C.AXIS, lw=0.8, ls="--")
        ax.set_xscale("log")
        ax.set_ylim(-0.03, 1.05)
        if ft == "TURNS":
            ax.set_xticks([3, 7.5, 11.8]); ax.set_xticklabels(["3.0", "7.5", "11.8"]); ax.set_xlim(2.4, 14.5)
        else:
            ax.set_xticks([2.8, 10.1, 14.6, 21.9, 35.9]); ax.set_xticklabels(["2.8", "10.1", "14.6", "21.9", "35.9"]); ax.set_xlim(2.2, 50)
        ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
        ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
        ax.set_xlabel("Physical extent level (% of a branch)")
        C.subcaption(ax, f"({'a' if ft == 'TURNS' else 'b'}) {C.FT_LABEL[ft]} faults")
    axes[0].set_ylabel("Detectable share")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.56, 1.0), columnspacing=1.0, handletextpad=0.3, fontsize=8)
    fig.subplots_adjust(top=0.80, bottom=0.26, left=0.11, right=0.99)
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
    trace_figure()
    pod_figure()
    print("figures written")
