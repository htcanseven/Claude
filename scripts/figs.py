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
    """Verdict shares of four rules for a new variant, a new process setting and a new family (in the produced
    family's floor), with the decisive (solid) and safe (dashed) distances marked."""
    c = pd.read_csv(src / "dec_curve.csv")
    res = pd.read_csv(src / "dec_resolution.csv")
    res = res[res["qc"] == "all"].set_index(["scope", "method"])
    # a new family in the produced family's floor, as the procedure prescribes
    c = pd.concat([c[c["scope"] != "transfer"], pd.read_csv(src / "panel_source_floor_curve.csv")])
    sf = pd.read_csv(src / "panel_source_floor.csv")
    sf = sf[(sf["qc"] == "all") & (sf["floor"] == "source family")].set_index(["scope", "method"])
    res = pd.concat([res.drop(index="transfer", level=0), sf[res.columns.intersection(sf.columns)]])
    methods = ["M2", "M5", "M5n", "NN"]
    scopes = [("within", "new variant"), ("setting", "new setting"), ("transfer", "new family")]
    fig, axs = plt.subplots(len(scopes), len(methods), figsize=(WIDTH_IN, 3.8), sharey=True, squeeze=False)
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
        axs[i, 0].set_ylabel(f"{sname}\nshare of verdicts", fontsize=8)
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
    fig, axs = plt.subplots(2, 3, figsize=(WIDTH_IN, 2.9), sharex=True, sharey="row", squeeze=False)
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


RULE_COLOUR.update({"M7n": "#1baf7a", "M1sn": "#4a3aa7", "M1s": MUTED, "NN+RM": "#eb6834"})
RULE_MARKER.update({"M7n": "v", "M1sn": "P", "M1s": "s", "NN+RM": "d"})


def all_intervals(src: Path) -> pd.DataFrame:
    """Stored intervals of decisions.py and learners.py, with the relation scopes and a new family in the
    produced family's floor (as step 6 scores it)."""
    import decisions as D
    import panel as P

    iv = pd.concat([pd.read_csv(src / "dec_intervals.csv"), pd.read_csv(src / "learn_intervals.csv")], ignore_index=True)
    return P.in_produced_floor(D.with_relation_scopes(iv), D.load_floors())


def fig_schematic(src: Path, method: str = "M7n", scope: str = "setting/extrapolation") -> None:
    """Operating characteristics of one rule: shares of correct and wrong verdicts against the requirement distance,
    with the decisive and safe distances, and the share correct among decided verdicts against the observable
    margin, with the guard band."""
    import decisions as D
    import panel as P

    iv = all_intervals(src)
    g = iv[(iv["scope"] == scope) & (iv["method"] == method)]
    grid = D.FINE[D.FINE <= 40]
    s = D.share_curves(*D.exclusion(g), grid=grid)
    dd = D.first_beyond(s["correct"], grid)
    ds = D.first_beyond(1 - s["wrong"], grid)
    band, curve = P.guard_band(g)
    fig, axs = plt.subplots(1, 2, figsize=(WIDTH_IN, 2.2), squeeze=False)
    ax = axs[0, 0]
    trial = 1 - s["correct"] - s["wrong"]
    ax.stackplot(grid, s["correct"], trial, s["wrong"], colors=[OUTCOME_COLOUR["correct"], OUTCOME_COLOUR["abstain"],
                                                                 OUTCOME_COLOUR["false_accept"]], edgecolor="white", lw=0.3)
    ax.axhline(0.95, color=INK, lw=0.7, ls=":")         # delta_d: correct share reaches 95 %; delta_s: wrong share < 5 %
    ax.text(39.5, 0.925, "95 %", fontsize=7, ha="right", va="top", color="white")
    for x, lab, ls in ((dd, r"$\delta_\mathrm{d}$", "-"), (ds, r"$\delta_\mathrm{s}$", "--")):
        ax.axvline(x, color=INK, lw=1.0, ls=ls)
        ax.text(x + 0.4, 0.42, lab, fontsize=9, color="white", va="center")
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 1)
    ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"])
    ax.tick_params(labelsize=8)
    ax.set_ylabel("share of verdicts", fontsize=9)
    ax.text(28, 0.6, r"correct, $\kappa$", fontsize=8, color="white", ha="center")
    ax.text(2.2, 0.86, "trial", fontsize=7, color=INK, ha="left", va="center")
    subcaption(ax, "a", r"verdicts at $|d|=\delta$", r"requirement distance $\delta$ (floors)")
    ax = axs[0, 1]
    ax.plot(curve["margin"], curve["correct_when_decided"], "-", color=OUTCOME_COLOUR["correct"], lw=1.3)
    ax.axhline(0.95, color=INK, lw=0.7, ls=":")
    if np.isfinite(band):
        ax.axvline(band, color=INK, lw=1.0)
        ax.text(band + 0.4, 0.62, rf"$g={band:g}$", fontsize=9)
    ax.set_xlim(0, 20)
    ax.set_ylim(0.6, 1.005)
    ax.tick_params(labelsize=8)
    ax.set_ylabel("correct among\ndecided verdicts", fontsize=9)
    subcaption(ax, "b", "a single verdict", "observable margin (floors)")
    handles = [plt.Rectangle((0, 0), 1, 1, color=OUTCOME_COLOUR[k], label=lab) for k, lab in
               (("correct", "correct"), ("abstain", "trial"), ("false_accept", r"wrong, $\omega$"))]
    fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.04), fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.93), w_pad=1.2)
    save(fig, "F_schematic")


def fig_parts(src: Path) -> None:
    """One part of each geometry after drawing (OP10) and after cutting (OP20), as the scanner sees it: depth below
    the plane of the cup bottom, with the regions and directions of the seven characteristics."""
    import io
    import zipfile

    import h5py

    import features_rddac as FR
    from common import CACHE, RDDAC_FILES, fetch_small

    zf = zipfile.ZipFile(fetch_small(RDDAC_FILES["sample.zip"], CACHE / "rddac_sample.zip"))
    fig, axs = plt.subplots(2, 3, figsize=(WIDTH_IN, 3.75), squeeze=False,
                            gridspec_kw={"width_ratios": [1, 1, 1.25]})
    letters = iter("abcdef")
    for i, (geo, member, label) in enumerate((("concave", "2500.h5", "concave, 300 kN"),
                                               ("convex", "7000.h5", "convex, 300 kN"))):
        with h5py.File(io.BytesIO(zf.read(member)), "r") as h5:
            frames = {}
            for op in ("op10", "op20"):
                Z, _ = FR.load_scan(h5, op)
                frames[op] = FR.part_frame(FR.block_median(Z))
        for j, op in enumerate(("op10", "op20")):
            fr = frames[op]
            X, Y, Dm = fr["X"] - fr["xc"], fr["Y"] - fr["yc"], np.where(fr["fin"], fr["D"], np.nan)
            ax = axs[i, j]
            ax.pcolormesh(X, Y, Dm, cmap="Blues", vmin=-2, vmax=34, shading="auto", rasterized=True)
            ax.set_aspect("equal")
            ax.set_xlim(-118, 118)
            ax.set_ylim(-118, 118)
            ax.set_xticks([-100, 0, 100])
            ax.set_yticks([-100, 0, 100])
            ax.tick_params(labelsize=7)
            ax.grid(False)
            if op == "op10":
                ax.plot([-105, 105], [0, 0], color=OUTCOME_COLOUR["false_reject"], lw=1.0)          # mid-side widths (x)
                ax.plot([-80, 80], [-80, 80], color=OUTCOME_COLOUR["false_accept"], lw=0.9, ls="--")   # diagonals
                ax.plot([-80, 80], [80, -80], color=OUTCOME_COLOUR["false_accept"], lw=0.9, ls="--")
                for sgn in (-1, 1):                     # east and west bands: wall at 10-20 mm depth, flange angle
                    ax.add_patch(plt.Rectangle((0 if sgn > 0 else -105, -5), 105, 10, fill=False, ec=INK, lw=0.7))
            else:
                for ux, uy in ((1, 0), (-1, 0), (0, 1), (0, -1)):                                    # arm bands
                    ax.add_patch(plt.Rectangle((min(0, ux * 105) - (5 if ux == 0 else 0),
                                                min(0, uy * 105) - (5 if uy == 0 else 0)),
                                               10 if ux == 0 else 105, 10 if uy == 0 else 105, fill=False,
                                               ec=INK, lw=0.7))
                ax.add_patch(plt.Circle((0, 0), 40, fill=False, ec=OUTCOME_COLOUR["false_reject"], lw=1.0))
            if j == 0:
                ax.set_ylabel(f"{label}\ny (mm)", fontsize=8)
            subcaption(ax, next(letters), "after drawing" if op == "op10" else "after cutting",
                       "x (mm)" if i == 1 else "")
        fr = frames["op10"]
        X, Y, Dm = fr["X"] - fr["xc"], fr["Y"] - fr["yc"], fr["D"]
        band = fr["fin"] & (np.abs(Y) <= 2.0)
        x, d = X[band], Dm[band]
        edges = np.arange(-115, 116, 1.0)
        idx = np.digitize(x, edges)
        prof = np.array([np.nanmedian(d[idx == k]) if np.sum(idx == k) > 2 else np.nan for k in range(1, len(edges))])
        xc = edges[:-1] + 0.5
        ax = axs[i, 2]
        ax.plot(xc, prof, "-", color=GEO_COLOUR[geo], lw=1.2)
        ax.invert_yaxis()
        ax.set_xlim(-115, 115)
        ax.set_ylim(33, -3)
        ax.axhspan(10, 20, color=GRID, lw=0)                         # straight part of the wall used for the angle
        ax.text(0, 15, "wall angle\nbetween 10 and 20 mm", ha="center", va="center", fontsize=6.5, color=MUTED)
        rim = (np.abs(xc) > 75) & np.isfinite(prof)
        flange = float(np.nanmedian(prof[rim])) if rim.any() else 29.0
        xa = float(np.nanmax(np.abs(xc[rim]))) - 3 if rim.any() else 85.0
        ax.annotate("", xy=(xa, flange), xytext=(xa, 0), arrowprops=dict(arrowstyle="<->", lw=0.8, color=INK))
        ax.text(xa - 2, 6, "depth", rotation=90, fontsize=6.5, ha="right", va="center")
        ax.text(0, 4, "bottom: datum\n(dome after cutting)", ha="center", va="center", fontsize=6.5, color=MUTED)
        ax.text(-xa + 1, flange - 2.5, "flange", fontsize=6.5, va="bottom", color=MUTED)
        ax.tick_params(labelsize=7)
        ax.set_ylabel("depth (mm)", fontsize=8)
        subcaption(ax, next(letters), "section y = 0, after drawing", "x (mm)" if i == 1 else "")
    fig.tight_layout(h_pad=0.4, w_pad=0.6)
    save(fig, "F_parts")


def fig_batches(src: Path, alt: str = "concave/300/medium") -> None:
    """The parts of one run in production order with the centres of its ten batches of 50, and the floor of the
    characteristic (95 % of batch pairs of an alternative differ by less)."""
    q = parts_qc(pd.read_csv(src / "features_rddac.csv", low_memory=False))
    fl = pd.read_csv(src / "alt_floor.csv").set_index("qc")
    g = q[q["alternative"] == alt].reset_index(drop=True)
    geo = alt.split("/")[0]
    fig, axs = plt.subplots(2, 1, figsize=(WIDTH_IN, 3.0), sharex=True, squeeze=False)
    for ax, qc, letter in zip(axs[:, 0], ("drawin_mid", "wall_op10"), "ab"):
        y = g[qc].to_numpy(float)
        n = np.arange(1, len(y) + 1)
        ax.plot(n, y, ".", color=MUTED, ms=1.6, alpha=0.6)
        cen = [centre(y[k:k + 50]) for k in range(0, len(y), 50)]
        for k, c in enumerate(cen):
            ax.plot([k * 50 + 1, k * 50 + 50], [c, c], "-", color=GEO_COLOUR[geo], lw=2.0, solid_capstyle="butt")
        F = float(fl.loc[qc, f"floor_{geo}"])
        lo, hi = np.nanpercentile(y, [1, 99])
        ax.set_ylim(lo - 0.1 * (hi - lo), hi + 0.1 * (hi - lo))
        x0 = 512
        mid = np.nanmean(cen)
        ax.plot([x0, x0], [mid - F / 2, mid + F / 2], color=INK, lw=2.4, solid_capstyle="butt", clip_on=False)
        ax.text(x0 + 6, mid, f"floor\n{F:.3g} {QCS_UNIT[qc]}", fontsize=7, va="center", clip_on=False)
        ax.set_xlim(0, 505)
        ax.tick_params(labelsize=8)
        ax.set_ylabel(ROW_LABEL[qc], fontsize=8)
        geo_, bhf_, lub_ = alt.split("/")
        subcaption(ax, letter, f"{SHORT[qc]}: {geo_} cup, {bhf_} kN, {lub_} lubrication",
                   "part in production order" if letter == "b" else "")
    fig.tight_layout(h_pad=0.4, rect=(0, 0, 0.93, 1))
    save(fig, "F_batches")


QCS_UNIT = {"drawin_mid": "mm", "drawin_corner": "mm", "waviness": "mm", "wall_op10": "$^{\\circ}$",
            "arm_op20": "$^{\\circ}$", "depth_op10": "mm", "dome_op20": "mm"}


def fig_costs(src: Path, c_fr: float = 0.5) -> None:
    """Expected cost per verdict against the cost of a trial (both relative to a false accept; a false reject costs
    c_fr), under the reference prior, for each rule with its cost-minimising guard band, and the cost of trying every
    design; lower row: the cost-minimising band."""
    c = pd.read_csv(src / "qual_costs.csv")
    c = c[(c["prior"] == "reference (+-20)") & np.isclose(c["c_fr"], c_fr)]
    rels = [("sibling", "sibling"), ("interpolation", "interpolated"), ("extrapolation", "extrapolated"),
            ("new family", "new family")]
    rules = ["M2", "M5", "NN", "M1sn", "M7n", "NN+RM"]
    fig, axs = plt.subplots(2, 4, figsize=(WIDTH_IN, 3.4), sharex=True, sharey="row", squeeze=False)
    letters = {(i, j): "abcdefgh"[4 * i + j] for i in range(2) for j in range(4)}
    for j, (rel, name) in enumerate(rels):
        for i, col in enumerate(("cost_opt", "band_opt")):
            ax = axs[i, j]
            for m in rules:
                g = c[(c["relation"] == rel) & (c["method"] == m)].sort_values("c_trial")
                if g.empty:
                    continue
                y = g[col].to_numpy(float)
                if col == "band_opt":
                    y = np.where(g["cost_opt"].to_numpy() >= g["c_trial"].to_numpy() - 1e-12, np.nan, y)
                ax.plot(g["c_trial"], y, "--" if m.endswith("+RM") else "-", marker=RULE_MARKER.get(m, "o"),
                        color=RULE_COLOUR.get(m, MUTED), lw=1.0, ms=3.2, mfc="white", mew=0.9, label=m)
            if col == "cost_opt":
                xs = np.array([0.01, 0.5])
                ax.plot(xs, xs, color=INK, lw=0.9, ls="--", label="trial every design")
            ax.set_xscale("log")
            ax.set_xticks([0.01, 0.1, 0.5], ["0.01", "0.1", "0.5"])
            ax.tick_params(labelsize=7)
            subcaption(ax, letters[(i, j)], name, r"$c_\mathrm{T}/c_\mathrm{FA}$" if i == 1 else "")
        axs[0, 0].set_ylabel("expected cost\nper verdict", fontsize=8)
        axs[1, 0].set_ylabel("cost-minimising\nband (floors)", fontsize=8)
    h, lab = axs[0, 1].get_legend_handles_labels()
    fig.legend(h, lab, loc="upper center", ncol=7, frameon=False, bbox_to_anchor=(0.5, 1.03), fontsize=8,
               handlelength=1.6, columnspacing=0.8)
    fig.tight_layout(rect=(0, 0, 1, 0.94), w_pad=0.4, h_pad=0.5)
    save(fig, "F_costs")


def fig_decisions_main(src: Path) -> None:
    """Verdict shares of three rules against the requirement distance, by relation (a new family in the produced
    family's floor), with the decisive (solid) and safe (dashed) distances."""
    import decisions as D

    iv = all_intervals(src)
    methods = [("NN", "nearest setting"), ("M5", "GP-corrected envelope"), ("M7n", "trend GP")]
    scopes = [("within", "sibling"), ("setting", "new setting"), ("transfer", "new family")]
    fig, axs = plt.subplots(len(scopes), len(methods), figsize=(WIDTH_IN, 4.1), sharey=True, squeeze=False)
    letters = iter("abcdefghi")
    for i, (scope, sname) in enumerate(scopes):
        for j, (m, mname) in enumerate(methods):
            ax = axs[i, j]
            g = iv[(iv["scope"] == scope) & (iv["method"] == m)]
            d = D.verdict_frame(g).assign(scope=scope)
            cv = D.score(d, ["d"]).reset_index().sort_values("d")
            x = cv["d"].to_numpy()
            ax.stackplot(x, cv["correct"], cv["abstain"], cv["false_reject"], cv["false_accept"],
                         colors=[OUTCOME_COLOUR[k] for k in ["correct", "abstain", "false_reject", "false_accept"]],
                         edgecolor="white", lw=0.4)
            r = D.distance_pair(*D.exclusion(g))
            for col, ls in (("resolution_floors", "-"), ("safe_floors", "--")):
                dv = r[col]
                if np.isfinite(dv) and dv < 100:
                    for sgn in (-1, 1):
                        ax.axvline(sgn * dv, color=INK, lw=0.9, ls=ls)
            ax.set_xscale("symlog", linthresh=10.0, linscale=1.5)
            ax.set_xlim(-100, 100)
            ax.set_ylim(0, 1)
            ax.set_xticks([-100, -10, 0, 10, 100], ["$-100$", "$-10$", "0", "10", "100"], fontsize=7)
            ax.set_xticks([-50, -30, -20, -5, 5, 20, 30, 50], minor=True)
            ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"])
            ax.tick_params(axis="y", labelsize=8)
            ax.axvline(0, color=INK, lw=0.6)
            if i == 0:
                ax.set_title(mname, fontsize=8, color=INK)
            subcaption(ax, next(letters), f"{m}, {sname}", "$d$ (floors)" if i == len(scopes) - 1 else "")
        axs[i, 0].set_ylabel("share of verdicts", fontsize=8)
    labels = {"correct": "correct", "abstain": "trial", "false_reject": "false reject", "false_accept": "false accept"}
    handles = [plt.Rectangle((0, 0), 1, 1, color=OUTCOME_COLOUR[k], label=labels[k]) for k in labels]
    handles += [plt.Line2D([], [], color=INK, lw=0.9, ls="-", label=r"$\pm\delta_\mathrm{d}$"),
                plt.Line2D([], [], color=INK, lw=0.9, ls="--", label=r"$\pm\delta_\mathrm{s}$")]
    fig.legend(handles=handles, loc="upper center", ncol=6, frameon=False, bbox_to_anchor=(0.5, 1.01),
               handlelength=1.4, columnspacing=1.0, fontsize=8)
    fig.tight_layout(rect=(0, 0, 1, 0.955), w_pad=0.5, h_pad=0.5)
    save(fig, "F3_decisions_main")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(RESULTS))
    ap.add_argument("--only", nargs="*", help="names of the figure functions to run (default: all)")
    args = ap.parse_args()
    src = Path(args.src)
    style()
    figs = {"alternatives": fig_alternatives, "decisions_compare": fig_decisions_compare}
    if (src / "budget_design.csv").exists():
        figs["budget"] = fig_budget
    if (src / "panel_step6_curves.csv").exists():
        figs["reliability"] = fig_reliability
    if (src / "learn_intervals.csv").exists():
        figs.update({"schematic": fig_schematic, "decisions_main": fig_decisions_main})
    if (src / "qual_costs.csv").exists():
        figs["costs"] = fig_costs
    figs.update({"parts": fig_parts, "batches": fig_batches})
    for name, fn in figs.items():
        if not args.only or name in args.only:
            fn(src)
    print(f"figures written to {FIGURES}")


if __name__ == "__main__":
    main()
