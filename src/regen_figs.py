"""Regenerate the two quantitative figures that directly parallel reconciled
Tables VI and VIII, so figure values match the tables exactly. Reads
results/reconciled.json; error bars are the Type A expanded uncertainty (U95),
matching the +/- shown in the tables. Style matches the original figures
(run_c_multiseed.py, run_harden.py)."""
from __future__ import annotations
import os, json, shutil
import numpy as np
import matplotlib.pyplot as plt
import viz

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
IOP_FIG = os.path.join(os.path.dirname(os.path.dirname(__file__)), "paper",
                       "Deployment-Realistic Performance Measurement of Low-Cost MEMS "
                       "Sensing for IoT-Based Condition Monitoring of Induction Machines (IOP MST)",
                       "Figures")

viz.set_style()
R = json.load(open(os.path.join(RES, "reconciled.json")))


# ---- Figure: optimism gap (Table VI) ----
VI = R["VI"]
order_keys = ["RANDOM", "GROUP", "SPEED", "LOAD"]
labels = ["RANDOM", "GROUP", "CROSS-SPEED", "CROSS-LOAD"]
models = ["RF", "KNN", "SVM"]
fig, ax = plt.subplots(figsize=(7.2, 3.8))
xpos = np.arange(len(order_keys)); w = 0.25
for i, m in enumerate(models):
    means = [VI[m][k]["mean"] for k in order_keys]
    errs = [VI[m][k]["U95"] for k in order_keys]
    ax.bar(xpos + (i - 1) * w, means, w, yerr=errs, capsize=3, label=m)
ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel("Accuracy (%)"); ax.set_ylim(0, 100)
ax.axhline(100 / 6, ls="--", c="0.5", lw=1)
ax.text(len(order_keys) - 0.5, 100 / 6 + 2, "chance (1/6)", color="0.4", fontsize=8, ha="right")
ax.set_title("Optimism gap under leakage-free evaluation (5 seeds)")
ax.legend(ncol=3, frameon=False, loc="upper right")
viz.savefig(fig, os.path.join(RES, "fig_optimism_gap.png"))


# ---- Figure: recipe stacking (Table VIII) ----
VIII = R["VIII"]
short = {"Baseline (100 Hz, 6 ch, 2 s)": "Baseline\n100 Hz/6 ch/2 s",
         "+ 25 Hz": "+25 Hz",
         "+ raw 3 ch": "+raw 3 ch",
         "+ 4 s window (optimal)": "+4 s (optimal)"}
labels = [short.get(r["label"], r["label"]) for r in VIII]
fig, ax = plt.subplots(figsize=(7.6, 4.0))
xpos = np.arange(len(VIII)); w = 0.25
for i, m in enumerate(["RF", "KNN", "LogReg"]):
    means = [r[m]["mean"] for r in VIII]
    errs = [r[m]["U95"] for r in VIII]
    ax.bar(xpos + (i - 1) * w, means, w, yerr=errs, capsize=3, label=m)
ax.set_xticks(xpos); ax.set_xticklabels(labels, rotation=15, ha="right", fontsize=8)
ax.set_ylabel("GROUP accuracy (%)"); ax.set_ylim(0, 100)
ax.axhline(100 / 6, ls="--", c="0.6", lw=1)
ax.set_title("Frugal choices stack: the resource-optimal node beats the naive baseline")
ax.legend(ncol=3, frameon=False, loc="upper left")
viz.savefig(fig, os.path.join(RES, "fig_recipe_stacking.png"))


# ---- copy both into the IOP submission Figures/ folder ----
for fn in ["fig_optimism_gap.png", "fig_recipe_stacking.png"]:
    shutil.copy(os.path.join(RES, fn), os.path.join(IOP_FIG, fn))
    print("copied to IOP:", fn)
