"""Figures of the findings, in the paper's style.

Style (as in the first paper): serif Computer Modern at 10 pt, figures drawn at
the journal text width (5.15 in), a sub-caption under every panel, colours from
a validated categorical palette (concave = blue, convex = orange) with marker
shapes as a second encoding; blank-holder force on a validated ordinal blue
ramp.

Usage: python scripts/figs.py [--src DIR]   (default: results/)
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

logging.getLogger("fontTools").setLevel(logging.ERROR)   # cmr10 header timestamps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import FIGURES, RESULTS, centre  # noqa: E402
from qc import SHARED, parts_qc  # noqa: E402

WIDTH_IN = 5.15
GEO_COLOUR = {"concave": "#2a78d6", "convex": "#eb6834"}     # validated categorical slots 1-2
GEO_MARKER = {"concave": "o", "convex": "s"}
BHF_COLOUR = {100: "#86b6ef", 300: "#2a78d6", 500: "#104281"}  # validated ordinal ramp
LUB_MARKER = {"coarse": "o", "medium": "s", "fine": "^"}
OUTCOME_COLOUR = {"correct": "#0ca30c", "abstain": "#c3c2b7", "false_reject": "#ec835a", "false_accept": "#d03b3b"}
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e1e0d9"
SHORT = {"drawin_mid": "draw-in, mid-side", "drawin_corner": "draw-in, corner", "waviness": "flange waviness",
         "wall_op10": "wall angle", "arm_op20": "arm angle (cut)", "depth_op10": "cup depth",
         "dome_op20": "bottom dome (cut)"}
ROW_LABEL = {"drawin_mid": "draw-in,\nmid-side (mm)", "drawin_corner": "draw-in,\ncorner (mm)",
             "waviness": "waviness\n(mm)", "wall_op10": "wall angle\n($^{\\circ}$)",
             "arm_op20": "arm angle,\ncut ($^{\\circ}$)", "depth_op10": "cup depth\n(mm)",
             "dome_op20": "dome,\ncut (mm)"}


def style() -> None:
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["cmr10", "Computer Modern Roman", "DejaVu Serif"],
        "mathtext.fontset": "cm", "axes.formatter.use_mathtext": True, "font.size": 10,
        "axes.titlesize": 10, "axes.labelsize": 10, "xtick.labelsize": 10, "ytick.labelsize": 10,
        "legend.fontsize": 10, "pdf.fonttype": 42, "ps.fonttype": 42, "axes.edgecolor": MUTED,
        "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED, "axes.grid": True,
        "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True, "lines.linewidth": 1.2,
        "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
    })


def subcaption(ax, letter: str, text: str, xlabel: str = "") -> None:
    """Sub-caption with a bold panel letter, appended as the last line of the x-label (as in the first paper)."""
    ax.set_xlabel((xlabel + "\n" if xlabel else "") + rf"$\mathbf{{({letter})}}$ {text}", linespacing=1.6)


def save(fig, name: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{name}.pdf")
    fig.savefig(FIGURES / f"{name}.png", dpi=200)
    plt.close(fig)


def fig_alternatives(src: Path) -> None:
    """Centre (10 % trimmed mean) and 5-95 % range of each characteristic per alternative, with the floor."""
    q = parts_qc(pd.read_csv(src / "features_rddac.csv", low_memory=False))
    fl = pd.read_csv(src / "alt_floor.csv").set_index("qc")
    rows = SHARED
    fig, axs = plt.subplots(len(rows), 2, figsize=(WIDTH_IN, 1.0 * len(rows) + 0.6), squeeze=False)
    for i, qc in enumerate(rows):
        for j, geo in enumerate(["concave", "convex"]):
            ax = axs[i, j]
            g = q[q["geometry"] == geo]
            for k, bhf in enumerate([100, 300, 500]):
                for m, lub in enumerate(["coarse", "medium", "fine"]):
                    v = g[(g["bhf_kN"] == bhf) & (g["oil_type"] == lub)][qc].dropna()
                    if v.empty:
                        continue
                    x = k + (m - 1) * 0.22
                    lo, hi = np.quantile(v, [0.05, 0.95])
                    ax.plot([x, x], [lo, hi], color=GEO_COLOUR[geo], lw=1.0)
                    ax.plot(x, centre(v), LUB_MARKER[lub], color=GEO_COLOUR[geo], ms=4.5, mfc="white", mew=1.1)
            F = fl.loc[qc, f"floor_{geo}"]
            y0 = ax.get_ylim()[0]
            ax.plot([2.45, 2.45], [y0 + 0.05 * np.ptp(ax.get_ylim()), y0 + 0.05 * np.ptp(ax.get_ylim()) + F],
                    color=INK, lw=2.2, solid_capstyle="butt")
            ax.set_xticks([0, 1, 2], ["100", "300", "500"] if i == len(rows) - 1 else ["", "", ""])
            ax.set_xlim(-0.5, 2.6)
            ax.yaxis.set_major_locator(plt.MaxNLocator(3))
            ax.grid(axis="x", visible=False)
            if j == 0:
                ax.set_ylabel(ROW_LABEL[qc], fontsize=9)
            if i == len(rows) - 1:
                subcaption(ax, "ab"[j], geo, "blank-holder force (kN)")
    handles = [plt.Line2D([], [], ls="", label="lubrication:")]
    handles += [plt.Line2D([], [], ls="", marker=LUB_MARKER[k], mfc="white", mec=MUTED, label=k) for k in LUB_MARKER]
    handles.append(plt.Line2D([], [], color=INK, lw=2.2, label="floor"))
    fig.legend(handles=handles, loc="upper center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 1.0),
               handlelength=1.2, columnspacing=1.0, handletextpad=0.4)
    fig.tight_layout(rect=(0, 0, 1, 0.97), h_pad=0.4, w_pad=0.8)
    save(fig, "F1_alternatives")


def fig_sensitivity(src: Path) -> None:
    """Simulated over measured sensitivity per factor and characteristic (log scale)."""
    s = pd.read_csv(src / "ds_sensitivity.csv")
    factors = [("bhf_kN", "blank-holder force"), ("friction_coefficient", "friction"),
               ("sheet_metal_thickness", "sheet thickness")]
    fig, axs = plt.subplots(1, 3, figsize=(WIDTH_IN, 2.9), sharey=True)
    ylabels = [SHORT[c] for c in SHARED]
    for ax, (fac, name), letter in zip(axs, factors, "abc"):
        for geo, dy in (("concave", -0.12), ("convex", 0.12)):
            sub = s[(s["factor"] == fac) & (s["geometry"] == geo)].set_index("qc").reindex(SHARED)
            ratio = (sub["sim_sensitivity"] / sub["real_sensitivity"]).to_numpy()
            y = np.arange(len(SHARED)) + dy
            same = ratio > 0
            r = np.abs(ratio)
            ax.plot(r[same], y[same], GEO_MARKER[geo], color=GEO_COLOUR[geo], ms=5, label=f"{geo}")
            ax.plot(r[~same], y[~same], GEO_MARKER[geo], color=GEO_COLOUR[geo], ms=5, mfc="white", mew=1.2)
        ax.axvspan(0.5, 2.0, color=GRID, alpha=0.7, lw=0)
        ax.axvline(1.0, color=MUTED, lw=0.8)
        ax.set_xscale("log")
        ax.set_xlim(0.02, 2000)
        ax.set_yticks(range(len(SHARED)), ylabels)
        ax.invert_yaxis()
        subcaption(ax, letter, name, "ratio")
    handles = [plt.Line2D([], [], ls="", marker=GEO_MARKER[g], color=GEO_COLOUR[g], label=g) for g in GEO_COLOUR]
    handles.append(plt.Line2D([], [], ls="", marker="o", mfc="white", mec=MUTED, label="opposite sign"))
    fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.55, 1.04))
    fig.tight_layout(rect=(0, 0, 1, 0.95), w_pad=0.6)
    save(fig, "F2_sensitivity")


def fig_decisions(src: Path, scope: str = "within") -> None:
    """Verdict shares against the requirement distance, per decision rule."""
    c = pd.read_csv(src / "dec_curve.csv")
    c = c[c["scope"] == scope]
    methods = [m for m in ["M0", "M1", "M2", "M5", "M3", "M4"] if m in set(c["method"])]
    nrow = 1 if len(methods) <= 3 else 2
    ncol = int(np.ceil(len(methods) / nrow))
    fig, axs = plt.subplots(nrow, ncol, figsize=(WIDTH_IN, 2.3 * nrow + 0.25), sharey=True, squeeze=False)
    for ax in axs.ravel()[len(methods):]:
        ax.set_visible(False)
    names = {"M0": "nominal simulation", "M1": "bias-corrected", "M2": "envelope + margin",
             "M3": "simulation + ML", "M4": "ML only", "M5": "GP calibration"}
    for ax, m, letter in zip(axs.ravel(), methods, "abcdef"):
        g = c[c["method"] == m].sort_values("d")
        x = g["d"].to_numpy()
        ys = [g["correct"], g["abstain"], g["false_reject"], g["false_accept"]]
        ax.stackplot(x, *ys, colors=[OUTCOME_COLOUR[k] for k in ["correct", "abstain", "false_reject", "false_accept"]],
                     lw=0)
        ax.set_xscale("symlog", linthresh=1.0)
        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(0, 1)
        ax.set_xticks([-100, -10, 0, 10, 100], ["$-100$", "", "0", "", "100"], fontsize=9)
        ax.set_xticks([-500, -50, -5, 5, 50, 500], minor=True)
        ax.axvline(0, color=INK, lw=0.6)
        subcaption(ax, letter, names[m], "distance $d$ (floors)")
    for ax in axs[:, 0]:
        ax.set_ylabel("share of verdicts")
    for ax in axs[:, 1:].ravel():
        ax.tick_params(labelleft=False)
    labels = {"correct": "correct", "abstain": "uncertain", "false_reject": "false reject", "false_accept": "false accept"}
    handles = [plt.Rectangle((0, 0), 1, 1, color=OUTCOME_COLOUR[k], label=labels[k]) for k in labels]
    top = 1.0 - 0.17 / (2.3 * nrow + 0.25)
    fig.legend(handles=handles, loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.0 + 0.02 / nrow))
    fig.tight_layout(rect=(0, 0, 1, top - 0.04 / nrow), w_pad=0.8, h_pad=0.6)
    save(fig, f"F3_decisions_{scope}")


def fig_budget(src: Path) -> None:
    """Safe and decisive distances against the number of calibration alternatives (within geometry)."""
    r = pd.read_csv(src / "budget_resolution.csv")
    r = r[r["qc"] == "all"].sort_values("k")
    m1, m2 = r[r["method"] == "M1"], r[r["method"] == "M2"]
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 2.5))
    ax.plot(m1["k"], m1["resolution_floors"], "-s", color=MUTED, ms=4.5, mfc="white", mew=1.1,
            label="M1, safe = decisive")
    ax.plot(m2["k"], m2["resolution_floors"], "-o", color=INK, ms=4.5, label="M2, decisive")
    ax.plot(m2["k"], m2["safe_floors"], "--o", color=INK, ms=4.5, mfc="white", mew=1.1, label="M2, safe")
    last = int(r["k"].max())
    fig.legend(loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.02))
    ax.set_xlim(0.7, last + 0.3)
    ax.set_ylim(0, None)
    ax.set_xticks(range(1, last + 1))
    ax.set_xlabel("calibration alternatives $k$ (same geometry)")
    ax.set_ylabel("distance $|d|$ (floors)")
    fig.tight_layout(rect=(0, 0, 1, 0.9))
    save(fig, "F4_budget")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(RESULTS))
    args = ap.parse_args()
    src = Path(args.src)
    style()
    fig_alternatives(src)
    fig_sensitivity(src)
    for scope in ("within", "pooled", "transfer"):
        fig_decisions(src, scope)
    if (src / "budget_resolution.csv").exists():
        fig_budget(src)
    print(f"figures written to {FIGURES}")


if __name__ == "__main__":
    main()
