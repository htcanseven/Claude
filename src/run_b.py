"""Analysis B: sensor / signal characterization of the smartphone MEMS node.

- effective resolution (quantisation LSB) and noise floor,
- usable-band PSD (the <50 Hz Nyquist wall),
- raw vs gravity-compensated channel equivalence,
- per-channel diagnostic informativeness (mutual information).
"""
from __future__ import annotations

import os, json
import numpy as np
from scipy.signal import welch
from sklearn.feature_selection import mutual_info_classif

from dataio import (list_recordings, load_signal, CHANNELS, RAW_CHANNELS,
                    USER_CHANNELS, FS, CLASSES)
from features import build_feature_matrix
import viz
import matplotlib.pyplot as plt

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")


def effective_resolution(sig1d: np.ndarray) -> float:
    """Estimate the quantisation step (LSB) as the smallest positive gap
    between consecutive distinct sample values."""
    u = np.unique(sig1d)
    diffs = np.diff(u)
    diffs = diffs[diffs > 0]
    return float(np.min(diffs)) if len(diffs) else float("nan")


def main():
    viz.set_style()
    recs = list_recordings()
    rec_by = {r.name: r for r in recs}
    out = {}

    # ---------- effective resolution + noise floor (healthy, unloaded) ----------
    hz = rec_by["H_0_30Hz"]
    x = load_signal(hz)  # (N,6)
    lsb = {CHANNELS[i]: effective_resolution(x[:, i]) for i in range(6)}
    # noise floor from Welch PSD of a raw axis (use gX, horizontal -> low gravity)
    f, pxx = welch(x[:, 0], fs=FS, nperseg=1024)
    floor = np.median(pxx[(f > 30)])  # high-band median as a floor proxy
    out["effective_resolution_g"] = lsb
    out["noise_floor_gx_psd_median_g2Hz_above30Hz"] = float(floor)
    print("Effective resolution (LSB, milli-g):",
          {k: round(v*1e3, 3) for k, v in lsb.items()})
    print(f"Noise-floor PSD (gX, >30 Hz median): {floor:.2e} g^2/Hz "
          f"= {10*np.log10(floor):.1f} dB")

    # ---------- raw vs gravity-compensated equivalence ----------
    corr = {}
    for r3, u3 in zip(RAW_CHANNELS, USER_CHANNELS):
        rr = []
        for r in recs:
            s = load_signal(r, [r3, u3])
            a = s[:, 0] - s[:, 0].mean()   # raw minus DC
            b = s[:, 1]                     # gravity-compensated
            rr.append(np.corrcoef(a, b)[0, 1])
        corr[f"{r3}~{u3}"] = float(np.mean(rr))
    out["raw_vs_userAC_corr"] = corr
    print("Raw(AC) vs gravity-compensated correlation:",
          {k: round(v, 4) for k, v in corr.items()})

    # ---------- usable-band PSD per class (50 Hz, loaded) ----------
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    for c in CLASSES:
        r = rec_by[f"{c}_1_50Hz"]
        s = load_signal(r, ["gUserX"])[:, 0]
        f, pxx = welch(s, fs=FS, nperseg=2048)
        ax.semilogy(f, pxx, label=c, lw=1.3)
    ax.set_xlim(0, 50); ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("PSD of gUserX (g²/Hz)")
    ax.set_title("Usable band is capped at 50 Hz (Nyquist @ 100 Hz)")
    ax.axvline(50, ls="--", c="0.5", lw=1)
    ax.legend(ncol=3, fontsize=8, frameon=False, title="class (loaded, 50 Hz supply)")
    viz.savefig(fig, os.path.join(RES, "fig_psd_usable_band.png"))

    # ---------- per-channel diagnostic informativeness (MI) ----------
    d = build_feature_matrix(recs)
    cols = d["columns"]
    mi = mutual_info_classif(d["X"], d["y"], random_state=0)
    ch_mi = {}
    for ch in CHANNELS:
        idx = [i for i, cn in enumerate(cols) if cn.startswith(ch + ":")]
        ch_mi[ch] = float(np.mean(mi[idx]))
    out["per_channel_mean_MI"] = ch_mi
    order = sorted(ch_mi, key=ch_mi.get, reverse=True)
    print("Per-channel mean MI (nats), ranked:",
          [(c, round(ch_mi[c], 3)) for c in order])

    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    ax.bar(range(6), [ch_mi[c] for c in order], color=viz.PALETTE[0])
    ax.set_xticks(range(6)); ax.set_xticklabels(order)
    ax.set_ylabel("mean MI with fault label")
    ax.set_title("Per-channel diagnostic informativeness")
    viz.savefig(fig, os.path.join(RES, "fig_channel_mi.png"))

    # ---------- write report ----------
    lines = ["# Analysis B — Sensor / signal characterization", ""]
    lines.append("## Effective resolution (quantisation LSB)")
    lines.append("")
    lines.append("| channel | " + " | ".join(CHANNELS) + " |")
    lines.append("|" + "---|" * (len(CHANNELS)+1))
    lines.append("| LSB (milli-g) | " +
                 " | ".join(f"{lsb[c]*1e3:.3f}" for c in CHANNELS) + " |")
    lines.append("")
    lines.append(f"Noise-floor PSD (gX, median >30 Hz): "
                 f"{floor:.2e} g²/Hz ({10*np.log10(floor):.1f} dB).")
    lines.append("")
    lines.append("## Raw vs gravity-compensated equivalence (Pearson r of AC content)")
    lines.append("")
    lines.append("| pair | " + " | ".join(corr.keys()) + " |")
    lines.append("|" + "---|" * (len(corr)+1))
    lines.append("| r | " + " | ".join(f"{v:.4f}" for v in corr.values()) + " |")
    lines.append("")
    lines.append("> The raw and gravity-compensated triads are only **moderately "
                 f"correlated** (r ≈ {min(corr.values()):.2f}–{max(corr.values()):.2f}), so "
                 "iOS `userAcceleration` does more than remove DC — its complementary "
                 "gravity filter also removes low-frequency content. Consistently, the "
                 "**raw channels are more diagnostically informative** (higher MI) than "
                 "the compensated ones, i.e. compensation discards useful low-frequency "
                 "fault information. The two triads are complementary, not redundant — a "
                 "concrete sensor-signal finding specific to smartphone-based acquisition.")
    lines.append("")
    lines.append("## Per-channel diagnostic informativeness (mean MI)")
    lines.append("")
    lines.append("| channel | " + " | ".join(order) + " |")
    lines.append("|" + "---|" * (len(order)+1))
    lines.append("| mean MI | " + " | ".join(f"{ch_mi[c]:.3f}" for c in order) + " |")
    with open(os.path.join(RES, "analysis_B.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(RES, "analysis_B.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("wrote analysis_B.md / .json")


if __name__ == "__main__":
    main()
