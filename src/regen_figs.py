"""Regenerate the paper figures at publication resolution (viz.savefig.dpi=400,
IOP asks for >=300 dpi for raster artwork) without re-running the analyses:
everything is replotted from the cached results JSON, except the two
signal-domain figures, which are cheap to recompute from the recordings.

Covered here:
  fig_optimism_gap.png     <- reconciled.json  (Table VI)
  fig_recipe_stacking.png  <- reconciled.json  (Table VIII)
  fig_channel_mi.png       <- analysis_B.json
  fig_tradeoffs_main.png   <- analysis_D.json
  fig_psd_usable_band.png  <- recomputed (Welch PSD of six recordings)
  fig_example_signals.png  <- delegated to fig_dataset.main()

fig_confusion_group.png is regenerated separately by regen_confusion.py, which
needs out-of-fold predictions. Figures are copied into the IOP submission
folder so the manuscript picks them up.
"""
from __future__ import annotations
import os, json, shutil
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
import viz

from dataio import list_recordings, load_signal, CLASSES, FS

ROOT = os.path.dirname(os.path.dirname(__file__))
RES = os.path.join(ROOT, "results")
IOP_FIG = os.path.join(ROOT, "paper",
                       "Deployment-Realistic Performance Measurement of Low-Cost MEMS "
                       "Sensing for IoT-Based Condition Monitoring of Induction Machines (IOP MST)",
                       "Figures")

viz.set_style()
R = json.load(open(os.path.join(RES, "reconciled.json")))
B = json.load(open(os.path.join(RES, "analysis_B.json")))
D = json.load(open(os.path.join(RES, "analysis_D.json")))


# ---- Fig: optimism gap (Table VI) ---------------------------------------
VI = R["VI"]
order_keys = ["RANDOM", "GROUP", "SPEED", "LOAD"]
labels = ["RANDOM", "GROUP", "CROSS-SPEED", "CROSS-LOAD"]
fig, ax = plt.subplots(figsize=(7.2, 3.8))
xpos = np.arange(len(order_keys)); w = 0.25
for i, m in enumerate(["RF", "KNN", "SVM"]):
    ax.bar(xpos + (i - 1) * w, [VI[m][k]["mean"] for k in order_keys], w,
           yerr=[VI[m][k]["U95"] for k in order_keys], capsize=3, label=m)
ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel("Accuracy (%)"); ax.set_ylim(0, 100)
ax.axhline(100 / 6, ls="--", c="0.5", lw=1)
ax.text(len(order_keys) - 0.5, 100 / 6 + 2, "chance (1/6)", color="0.4", fontsize=8, ha="right")
ax.set_title("Optimism gap under leakage-free evaluation (5 seeds)")
ax.legend(ncol=3, frameon=False, loc="upper right")
viz.savefig(fig, os.path.join(RES, "fig_optimism_gap.png"))


# ---- Fig: recipe stacking (Table VIII) ----------------------------------
VIII = R["VIII"]
short = {"Baseline (100 Hz, 6 ch, 2 s)": "Baseline\n100 Hz/6 ch/2 s",
         "+ 25 Hz": "+25 Hz", "+ raw 3 ch": "+raw 3 ch",
         "+ 4 s window (optimal)": "+4 s (optimal)"}
fig, ax = plt.subplots(figsize=(7.6, 4.0))
xpos = np.arange(len(VIII)); w = 0.25
for i, m in enumerate(["RF", "KNN", "LogReg"]):
    ax.bar(xpos + (i - 1) * w, [r[m]["mean"] for r in VIII], w,
           yerr=[r[m]["U95"] for r in VIII], capsize=3, label=m)
ax.set_xticks(xpos)
ax.set_xticklabels([short.get(r["label"], r["label"]) for r in VIII],
                   rotation=15, ha="right", fontsize=8)
ax.set_ylabel("GROUP accuracy (%)"); ax.set_ylim(0, 100)
ax.axhline(100 / 6, ls="--", c="0.6", lw=1)
ax.set_title("Frugal choices stack: the resource-optimal node beats the naive baseline")
ax.legend(ncol=3, frameon=False, loc="upper left")
viz.savefig(fig, os.path.join(RES, "fig_recipe_stacking.png"))


# ---- Fig: per-channel mutual information --------------------------------
ch_mi = B["per_channel_mean_MI"]
order = sorted(ch_mi, key=ch_mi.get, reverse=True)
fig, ax = plt.subplots(figsize=(6.2, 3.4))
ax.bar(range(6), [ch_mi[c] for c in order], color=viz.PALETTE[0])
ax.set_xticks(range(6)); ax.set_xticklabels(order)
ax.set_ylabel("mean MI with fault label")
ax.set_title("Per-channel diagnostic informativeness")
viz.savefig(fig, os.path.join(RES, "fig_channel_mi.png"))


# ---- Fig: accuracy-resource trade-offs ----------------------------------
fig, axes = plt.subplots(1, 3, figsize=(12, 3.6))
d1 = D["D1_sampling"]
axes[0].errorbar([x["bitrate_kbps"] for x in d1], [x["acc"] for x in d1],
                 yerr=[x["acc_std"] for x in d1], marker="o", capsize=3)
for x in d1:
    axes[0].annotate(f"{x['fs']:g}Hz", (x["bitrate_kbps"], x["acc"]),
                     fontsize=7, xytext=(3, 3), textcoords="offset points")
axes[0].set_xlabel("raw stream bitrate (kbps, 6ch·int16)")
axes[0].set_ylabel("GROUP accuracy (%)"); axes[0].set_title("D1 sampling rate")
d3 = D["D3_window"]
axes[1].errorbar([x["latency_s"] for x in d3], [x["acc"] for x in d3],
                 yerr=[x["acc_std"] for x in d3], marker="s", color=viz.PALETTE[1], capsize=3)
axes[1].set_xlabel("window / detection latency (s)")
axes[1].set_title("D3 window length")
d2 = D["D2_channels"]
axes[2].bar(range(len(d2)), [x["acc"] for x in d2],
            yerr=[x["acc_std"] for x in d2], capsize=3, color=viz.PALETTE[2])
axes[2].set_xticks(range(len(d2)))
axes[2].set_xticklabels([x["subset"] for x in d2], rotation=30, ha="right")
axes[2].set_title("D2 channel subset")
for ax in axes:
    ax.axhline(100 / 6, ls="--", c="0.6", lw=1)
viz.savefig(fig, os.path.join(RES, "fig_tradeoffs_main.png"))


# ---- Fig: usable-band PSD ------------------------------------------------
rec_by = {r.name: r for r in list_recordings()}
fig, ax = plt.subplots(figsize=(7.2, 4.0))
for c in CLASSES:
    s = load_signal(rec_by[f"{c}_1_50Hz"], ["gUserX"])[:, 0]
    f, pxx = welch(s, fs=FS, nperseg=2048)
    ax.semilogy(f, pxx, label=c, lw=1.3)
ax.set_xlim(0, 50); ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("PSD of gUserX (g²/Hz)")
ax.set_title("Usable band is capped at 50 Hz (Nyquist @ 100 Hz)")
ax.axvline(50, ls="--", c="0.5", lw=1)
ax.legend(ncol=3, fontsize=8, frameon=False, title="class (loaded, 50 Hz supply)")
viz.savefig(fig, os.path.join(RES, "fig_psd_usable_band.png"))


# ---- Fig: example signals (reuse the original generator) -----------------
import fig_dataset
fig_dataset.main()


# ---- copy into the IOP submission folder --------------------------------
for fn in ["fig_optimism_gap.png", "fig_recipe_stacking.png", "fig_channel_mi.png",
           "fig_tradeoffs_main.png", "fig_psd_usable_band.png", "fig_example_signals.png"]:
    shutil.copy(os.path.join(RES, fn), os.path.join(IOP_FIG, fn))
    print("copied to IOP:", fn)
