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
# verdict outcomes: categorical slots blue / orange / violet (validated for colour-vision deficiency, adjacent pairs
# in stacking order) and a neutral grey for the abstention
OUTCOME_COLOUR = {"correct": "#2a78d6", "abstain": "#c3c2b7", "false_reject": "#eb6834", "false_accept": "#4a3aa7"}
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
    fig, axs = plt.subplots(len(rows), 2, figsize=(WIDTH_IN, 0.9 * len(rows) + 0.6), squeeze=False)
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
        ax.set_xscale("symlog", linthresh=10.0, linscale=1.5)    # linear within +-10 floors, log beyond
        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(0, 1)
        ax.set_xticks([-100, -10, 0, 10, 100], ["", "$-10$", "0", "10", "100"], fontsize=9)
        ax.set_xticks([-500, -300, -200, -50, -30, -20, -5, 5, 20, 30, 50, 200, 300, 500], minor=True)
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


RULE_COLOUR = {"M1": MUTED, "M2": INK, "M5": "#2a78d6", "NN": "#eb6834", "M5n": "#1baf7a"}   # slots 1-3 + neutrals
RULE_MARKER = {"M1": "s", "M2": "o", "M5": "^", "NN": "D", "M5n": "v"}


def fig_decisions_compare(src: Path) -> None:
    """Verdict shares of four rules for a new variant, a new process setting and a new family, with the decisive
    (solid) and safe (dashed) distances marked."""
    c = pd.read_csv(src / "dec_curve.csv")
    res = pd.read_csv(src / "dec_resolution.csv")
    res = res[res["qc"] == "all"].set_index(["scope", "method"])
    methods = ["M2", "M5", "M5n", "NN"]
    scopes = [("within", "new variant"), ("setting", "new setting"), ("transfer", "new family")]
    fig, axs = plt.subplots(len(scopes), len(methods), figsize=(WIDTH_IN, 4.45), sharey=True, squeeze=False)
    letters = iter("abcdefghijkl")
    for i, (scope, sname) in enumerate(scopes):
        for j, m in enumerate(methods):
            ax = axs[i, j]
            g = c[(c["scope"] == scope) & (c["method"] == m)].sort_values("d")
            x = g["d"].to_numpy()
            ax.stackplot(x, g["correct"], g["abstain"], g["false_reject"], g["false_accept"],
                         colors=[OUTCOME_COLOUR[k] for k in ["correct", "abstain", "false_reject", "false_accept"]],
                         edgecolor="white", lw=0.4)
            if (scope, m) in res.index:
                for col, ls in (("resolution_floors", "-"), ("safe_floors", "--")):
                    dv = float(res.loc[(scope, m), col])
                    if np.isfinite(dv) and dv < 100:
                        for sgn in (-1, 1):
                            ax.axvline(sgn * dv, color=INK, lw=0.9, ls=ls)
            ax.set_xscale("symlog", linthresh=10.0, linscale=1.5)
            ax.set_xlim(-100, 100)
            ax.set_ylim(0, 1)
            ax.set_xticks([-100, -10, 0, 10, 100], ["", "$-10$", "0", "10", "100"], fontsize=8)
            ax.set_xticks([-50, -30, -20, -5, 5, 20, 30, 50], minor=True)
            ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"])
            ax.tick_params(axis="y", labelsize=8)
            ax.axvline(0, color=INK, lw=0.6)
            subcaption(ax, next(letters), m, "$d$ (floors)" if i == len(scopes) - 1 else "")
        axs[i, 0].set_ylabel(f"{sname}\nshare of verdicts", fontsize=9)
    labels = {"correct": "correct", "abstain": "trial", "false_reject": "false reject", "false_accept": "false accept"}
    handles = [plt.Rectangle((0, 0), 1, 1, color=OUTCOME_COLOUR[k], label=labels[k]) for k in labels]
    handles += [plt.Line2D([], [], color=INK, lw=0.9, ls="-", label=r"$\pm\delta_\mathrm{d}$"),
                plt.Line2D([], [], color=INK, lw=0.9, ls="--", label=r"$\pm\delta_\mathrm{s}$")]
    fig.legend(handles=handles, loc="upper center", ncol=6, frameon=False, bbox_to_anchor=(0.5, 1.01),
               handlelength=1.4, columnspacing=1.0, fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.965), w_pad=0.5, h_pad=0.5)
    save(fig, "F3_decisions_compare")


def fig_reliability(src: Path) -> None:
    """Share of correct verdicts among the decided ones whose observable margin between the predicted interval and
    the requirement is at least the value on the axis (reference prior: the requirement grid within 20 floors of
    the truth), by evidence relation, with each rule's guard band g marked where one qualifies."""
    c = pd.read_csv(src / "panel_step6_curves.csv")
    bands = pd.read_csv(src / "panel_step6.csv").set_index(["scope", "method"])["guard_band"]
    scopes = [("within", "sibling"), ("setting/interpolation", "interpolated"),
              ("setting/extrapolation", "extrapolated"), ("transfer", "new family")]
    fig, axs = plt.subplots(1, len(scopes), figsize=(WIDTH_IN, 2.35), sharey=True, squeeze=False)
    letters = iter("abcd")
    for j, (scope, sname) in enumerate(scopes):
        ax = axs[0, j]
        for m in ("M1", "M2", "M5", "M5n", "NN"):
            g = c[(c["scope"] == scope) & (c["method"] == m)].sort_values("margin")
            ax.plot(g["margin"], g["correct_when_decided"], "-", color=RULE_COLOUR[m], lw=1.1, label=m,
                    marker=RULE_MARKER[m], markevery=16, ms=3.0, mfc="white", mew=0.9)
            band = bands.get((scope, m), np.inf)
            if np.isfinite(band):
                y = np.interp(band, g["margin"], g["correct_when_decided"])
                ax.plot([band], [y], marker=RULE_MARKER[m], color=RULE_COLOUR[m], ms=5.0, mec="white", mew=0.6,
                        zorder=5)
        ax.axhline(0.95, color=MUTED, lw=0.8, ls=":")
        ax.set_xlim(0, 20)
        ax.set_ylim(0.5, 1.005)
        ax.set_xticks([0, 10, 20])
        ax.tick_params(labelsize=8)
        subcaption(ax, next(letters), sname, "margin (floors)")
    axs[0, 0].set_ylabel("correct among\ndecided verdicts", fontsize=9)
    h, lab = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, lab, loc="upper center", ncol=5, frameon=False, bbox_to_anchor=(0.5, 1.04), fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.92), w_pad=1.0)
    save(fig, "F5_reliability")


def fig_budget(src: Path) -> None:
    """Decisive and safe distances against the number of produced alternatives, by the relation of the new
    design to them (sibling, interpolation, extrapolation), with bands from resampling the targets."""
    r = pd.read_csv(src / "budget_design.csv").replace([np.inf, -np.inf], np.nan)
    rels = [("sibling", "sibling produced"), ("interpolation", "interpolation"), ("extrapolation", "extrapolation")]
    kinds = [("resolution", "decisive"), ("safe", "safe")]
    fig, axs = plt.subplots(2, 3, figsize=(WIDTH_IN, 3.2), sharex=True, sharey="row", squeeze=False)
    letters = iter("abcdef")
    for i, (col, kname) in enumerate(kinds):
        for j, (rel, rname) in enumerate(rels):
            ax = axs[i, j]
            for m in ("M1", "M2", "M5", "NN"):
                g = r[(r["relation"] == rel) & (r["method"] == m)].sort_values("k")
                if m == "M5":                          # a GP needs more than two points for its hyperparameters
                    g = g[g["k"] >= 3]
                if g.empty:
                    continue
                ax.fill_between(g["k"], g[f"{col}_lo"], g[f"{col}_hi"], color=RULE_COLOUR[m], alpha=0.12, lw=0)
                ax.plot(g["k"], g[f"{col}_floors"], "-" + RULE_MARKER[m], color=RULE_COLOUR[m], ms=3.5, lw=1.0,
                        mfc="white", mew=1.0, label=m)
            ax.set_xticks(range(1, 9))
            ax.set_xlim(0.7, 8.3)
            ax.tick_params(labelsize=8)
            subcaption(ax, next(letters), rname, "produced alternatives $k$" if i == 1 and j == 1 else ("$k$" if i == 1 else ""))
        axs[i, 0].set_ylabel(f"{kname} distance\n(floors)", fontsize=9)
    h, lab = axs[0, 0].get_legend_handles_labels()
    fig.legend(h, lab, loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.02))
    fig.tight_layout(rect=(0, 0, 1, 0.95), w_pad=0.5, h_pad=0.6)
    save(fig, "F4_budget")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(RESULTS))
    args = ap.parse_args()
    src = Path(args.src)
    style()
    fig_alternatives(src)
    fig_decisions_compare(src)
    if (src / "budget_design.csv").exists():
        fig_budget(src)
    if (src / "panel_step6_curves.csv").exists():
        fig_reliability(src)
    print(f"figures written to {FIGURES}")


if __name__ == "__main__":
    main()
