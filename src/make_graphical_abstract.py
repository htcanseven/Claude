"""Elsevier graphical abstract: the leakage ladder in one panel.
Minimum size required by Elsevier is 1328 x 531 px."""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
D = json.load(open(os.path.join(RES, "leakage_decomposition.json")))

steps = [
    ("RANDOM\n50% overlap", "random_overlap", "shared samples\n+ proximity\n+ recording identity"),
    ("RANDOM\nno overlap",  "random_nonoverlap", "proximity\n+ recording identity"),
    ("BLOCKED\nin recording", "blocked_nonoverlap", "recording identity"),
    ("GROUP\nrecording held out", "group_overlap", "none"),
]
vals = [D[k]["acc_mean"] for _, k, _ in steps]
errs = [D[k]["acc_ci95"] for _, k, _ in steps]
labels = [s[0] for s in steps]
notes = ["shared samples,\nproximity, identity", "proximity,\nidentity", "identity", "none"]

BLUE, RED, GREEN, GREY = "#0072B2", "#D55E00", "#009E73", "#8a8a8a"
colors = [RED, RED, RED, GREEN]

fig, ax = plt.subplots(figsize=(13.28, 5.31), dpi=100)
x = np.arange(4)
ax.bar(x, vals, width=0.52, color=colors, edgecolor="black", linewidth=0.8, zorder=3)
ax.errorbar(x, vals, yerr=errs, fmt="none", ecolor="black", capsize=5, lw=1.2, zorder=4)

for xi, v, e in zip(x, vals, errs):
    ax.text(xi, v + e + 2.5, f"{v:.1f}%", ha="center", va="bottom",
            fontsize=17, fontweight="bold", zorder=5)
for xi, n in zip(x, notes):
    ax.text(xi, -6, n, ha="center", va="top", fontsize=10, color=GREY, linespacing=1.3)

ax.axhline(100/6, ls="--", c="0.55", lw=1.2, zorder=2)
ax.text(3.58, 100/6 + 2.5, "chance (1/6)", fontsize=10, color="0.45", ha="right")

# bracket over the three protocols that change nothing
ax.annotate("", xy=(2.30, 118), xytext=(-0.30, 118),
            arrowprops=dict(arrowstyle="|-|", lw=1.3, color=GREY), zorder=6)
ax.text(1.0, 122, "removing window overlap and temporal proximity changes nothing",
        fontsize=12, color=GREY, ha="center", style="italic")

# callout in the clear space above the GROUP bar
ax.annotate("", xy=(3.0, 77), xytext=(3.0, 106),
            arrowprops=dict(arrowstyle="-|>", lw=2.6, color=BLUE), zorder=6)
ax.text(3.0, 117, "recording identity\n$-46.7$ points", color=BLUE, fontsize=14.5,
        fontweight="bold", ha="center", va="center", linespacing=1.35, zorder=7,
        bbox=dict(boxstyle="round,pad=0.45", fc="white", ec=BLUE, lw=1.6))

ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=12.5, linespacing=1.4)
ax.set_ylabel("Leakage-free accuracy (%)", fontsize=13.5)
ax.set_ylim(0, 140); ax.set_xlim(-0.62, 3.62)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.tick_params(axis="y", labelsize=11.5)
ax.tick_params(axis="x", pad=30)
ax.set_title("What actually inflates smartphone-MEMS fault-diagnosis accuracy",
             fontsize=16.5, fontweight="bold", pad=12)
for sp in ("top", "right"):
    ax.spines[sp].set_visible(False)
ax.grid(axis="y", alpha=0.25, zorder=0)
ax.set_axisbelow(True)
plt.subplots_adjust(bottom=0.30, top=0.88, left=0.07, right=0.985)

out = os.path.join(RES, "graphical_abstract.png")
fig.savefig(out, dpi=100)
plt.close(fig)
from PIL import Image
print("wrote", out, Image.open(out).size)
