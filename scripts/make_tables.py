"""Write the manuscript's data tables from the result CSVs into the marked blocks of paper/main.tex.

Every number in a table comes from a CSV in results/; nothing is typed by hand. Each table sits between
'%% BEGIN GENERATED <name>' and '%% END GENERATED <name>' in the single-file manuscript.

Usage: python scripts/make_tables.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS, ROOT  # noqa: E402
from qc import SHARED  # noqa: E402

MAIN = ROOT / "paper" / "main.tex"
LABEL = {"drawin_mid": "Draw-in, mid-side", "drawin_corner": "Draw-in, corner", "waviness": "Flange waviness",
         "wall_op10": "Wall angle", "arm_op20": "Arm angle, cut", "depth_op10": "Cup depth",
         "dome_op20": "Bottom dome, cut"}
UNIT = {"drawin_mid": "mm", "drawin_corner": "mm", "waviness": "mm", "wall_op10": r"$^\circ$",
        "arm_op20": r"$^\circ$", "depth_op10": "mm", "dome_op20": "mm"}
RULE = {"M0": "M0 nominal simulation", "M1": "M1 bias-corrected", "M2": "M2 envelope + conformal margin",
        "M5": "M5 Gaussian-process calibration", "M3": "M3 simulation + learned discrepancy",
        "M4": "M4 learned, no simulation"}
RULES = ["M0", "M1", "M2", "M5", "M3", "M4"]


def write_block(name: str, body: str) -> None:
    s = MAIN.read_text()
    start, end = f"%% BEGIN GENERATED {name}", f"%% END GENERATED {name}"
    i, j = s.index(start), s.index(end)
    k = s.index("\n", i) + 1
    MAIN.write_text(s[:k] + body.rstrip("\n") + "\n" + s[j:])


def sig(x: float, n: int = 2) -> str:
    """Round to n significant figures, without scientific notation."""
    if x is None or not np.isfinite(x):
        return "--"
    if x == 0:
        return "0"
    d = max(n - int(np.floor(np.log10(abs(x)))) - 1, 0)
    return f"{x:.{d}f}"


def num(x: float) -> str:
    if not np.isfinite(x):
        return r"$\infty$" if x > 0 else "--"
    return f"{x:g}"


def pct(x: float) -> str:
    return "--" if not np.isfinite(x) else f"{100 * x:.0f}"


def table(rows, caption, label, cols, head, colsep=None, note=None, star=False, size=r"\tabsize"):
    env = "table*" if star else "table"
    sep = f"\\setlength{{\\tabcolsep}}{{{colsep}}}\n" if colsep else ""
    foot = f"\\footnotetext{{{note}}}\n" if note else ""
    body = " \\\\\n".join(r.rstrip().rstrip("\\").rstrip() for r in rows)
    return (f"\\begin{{{env}}}[t]\n{size}\n{sep}\\caption{{{caption.rstrip('.')}}}\\label{{{label}}}\n"
            f"\\begin{{tabular}}{{@{{}}{cols}@{{}}}}\n\\toprule\n{head} \\\\\n\\midrule\n{body} \\\\\n"
            f"\\botrule\n\\end{{tabular}}\n{foot}\\end{{{env}}}\n")


def t_floors() -> str:
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    dr = pd.read_csv(RESULTS / "sens_drift.csv").set_index("qc")
    rows = []
    for c in SHARED:
        f = fl.loc[c]
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & {sig(f['floor'])} & {sig(f['floor_lo'])}--{sig(f['floor_hi'])} & "
                    f"{sig(f['floor_concave'])} & {sig(f['floor_convex'])} & {sig(f['sd_within'])} & "
                    f"{dr.loc[c, 'drift_inflation']:.1f}")
    head = (r"Characteristic & Floor $F$ & 95\,\% CI & Concave & Convex & Part SD & Drift factor")
    return table(rows, "Production floor per characteristic, pooled and per geometry", "tab:floors",
                 "lrrrrrr", head, colsep="5pt",
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of batch centres; "
                      r"CI from 2000 resamples of the batches. Part SD: median within-alternative standard "
                      r"deviation of single parts. Drift factor: floor over the floor of randomly permuted series.")


def t_resolve() -> str:
    e = pd.read_csv(RESULTS / "alt_effects.csv")
    m = pd.read_csv(RESULTS / "alt_mrc.csv")
    m = m[m["factor"] == "bhf_kN"].set_index("qc")
    rows = []
    for c in SHARED:
        g = e[e["qc"] == c]
        cells = []
        for fam in ["geometry", "bhf", "lubrication"]:
            h = g[g["family"] == fam]
            cells.append(f"{int((h['esr'] >= 1).sum())}/{len(h)} & {h['esr'].median():.1f}")
        mr = m.loc[c]
        rows.append(f"{LABEL[c]} & " + " & ".join(cells) +
                    f" & {mr['mrc']:.0f} ({mr['mrc_lo']:.0f}--{mr['mrc_hi']:.0f})")
    tot = []
    for fam in ["geometry", "bhf", "lubrication"]:
        h = e[e["family"] == fam]
        tot.append(f"{int((h['esr'] >= 1).sum())}/{len(h)} & {h['esr'].median():.1f}")
    rows.append(r"\midrule All & " + " & ".join(tot) + " & ")
    head = (r" & \multicolumn{2}{c}{Geometry} & \multicolumn{2}{c}{Blank-holder force} & "
            r"\multicolumn{2}{c}{Lubrication} & Force MRC \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Characteristic & ESR\,$\geq$\,1 & Median & ESR\,$\geq$\,1 & Median & ESR\,$\geq$\,1 & Median & kN (95\,\% CI)")
    return table(rows, "Single-factor contrasts that production resolves and minimum resolvable force change",
                 "tab:resolve", "lrrrrrrr", head, colsep="4pt",
                 note=r"ESR: effect-to-scatter ratio of two alternatives that differ in one factor; counts of "
                      r"contrasts with ESR\,$\geq$\,1 and median ESR. MRC: floor over the sensitivity of the "
                      r"alternative centres to blank-holder force.")


def t_offsets() -> str:
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    t["F"] = [fl.loc[q, f"floor_{g}"] for q, g in zip(t["qc"], t["geometry"])]
    t["off_F"] = (t["real_q95"] - t["sim_nominal"]) / t["F"]
    rows = []
    for c in SHARED:
        g = t[t["qc"] == c]
        cells = []
        for geo in ["concave", "convex"]:
            h = g[g["geometry"] == geo]
            cells.append(f"{h['off_F'].median():.0f} & {h['off_F'].max() - h['off_F'].min():.0f}")
        gm = [g[g["geometry"] == geo]["gap_matched"].median() for geo in ["concave", "convex"]]
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & " + " & ".join(cells) + f" & {gm[0]:+.2f} & {gm[1]:+.2f}")
    head = (r" & \multicolumn{2}{c}{Concave} & \multicolumn{2}{c}{Convex} & \multicolumn{2}{c}{Matched, units} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Characteristic & Offset & Spread & Offset & Spread & Concave & Convex")
    return table(rows, "Offset between the parts' 95th percentile and the nominal simulation, in floors",
                 "tab:offsets", "lrrrrrr", head, colsep="5pt",
                 note=r"Offset: median over the nine alternatives of a geometry of $(q_{95}-$ nominal "
                      r"simulation$)/F$; spread: its range over the alternatives. Matched: median difference "
                      r"between the centre of the parts and of their matched simulations, in the "
                      r"characteristic's unit.")


def t_distances() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r[r["qc"] == "all"].set_index(["scope", "method"])
    cv = pd.read_csv(RESULTS / "dec_curve.csv")
    at10 = cv[cv["d"].abs() == 10].groupby(["scope", "method"])[["correct", "false_accept", "false_reject",
                                                                  "abstain"]].mean()
    rows = []
    for m in RULES:
        cells = []
        for scope in ["within", "pooled", "transfer"]:
            x = r.loc[(scope, m)]
            cells.append(f"{num(x['resolution_floors'])} & {num(x['safe_floors'])}")
        a = at10.loc[("within", m)]
        rows.append(f"{RULE[m]} & " + " & ".join(cells) +
                    f" & {pct(a['correct'])} & {pct(a['false_accept'] + a['false_reject'])} & {pct(a['abstain'])}")
    head = (r" & \multicolumn{2}{c}{Within family} & \multicolumn{2}{c}{Pooled} & \multicolumn{2}{c}{Transfer} & "
            r"\multicolumn{3}{c}{Within, $|d|=10$ (\%)} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-10}" "\n"
            r"Rule & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & "
            r"$\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & right & wrong & trial")
    ci = r.loc[("within", "M5")]
    note = (r"Decisive ($\delta_\mathrm{d}$) and safe ($\delta_\mathrm{s}$) distances in floors over all seven "
            r"characteristics and held-out alternatives; the distance grid ends at 500 floors. Bootstrap 95\,\% "
            r"intervals over the design cases are given in Table~\ref{tab:distci}; for example M5 within the family: "
            f"$\\delta_\\mathrm{{d}}$ {num(ci['resolution_lo'])}--{num(ci['resolution_hi'])}, "
            f"$\\delta_\\mathrm{{s}}$ {num(ci['safe_lo'])}--{num(ci['safe_hi'])}.")
    return table(rows, "Decisive and safe distances of the six rules in production floors", "tab:distances",
                 "lrrrrrrrrr", head, colsep="3.2pt", note=note)


def t_distci() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r[r["qc"] == "all"].set_index(["scope", "method"])
    rows = []
    for m in RULES:
        cells = []
        for scope in ["within", "pooled", "transfer"]:
            x = r.loc[(scope, m)]
            cells.append(f"{num(x['resolution_lo'])}--{num(x['resolution_hi'])} & "
                         f"{num(x['safe_lo'])}--{num(x['safe_hi'])}")
        rows.append(f"{RULE[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{Within family} & \multicolumn{2}{c}{Pooled} & \multicolumn{2}{c}{Transfer} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Rule & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & "
            r"$\delta_\mathrm{d}$ & $\delta_\mathrm{s}$")
    return table(rows, r"Bootstrap 95\,\% intervals of the decisive and safe distances (floors)", "tab:distci",
                 "lrrrrrr", head, colsep="5pt",
                 note=r"1000 resamples of the held-out alternatives; interval ends on the distance grid.")


def t_qc_distances() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r[r["scope"] == "within"].set_index(["qc", "method"])
    rows = []
    for c in SHARED:
        rows.append(f"{LABEL[c]} & " + " & ".join(
            f"{num(r.loc[(c, m), 'resolution_floors'])}/{num(r.loc[(c, m), 'safe_floors'])}" for m in RULES))
    head = "Characteristic & " + " & ".join(RULES)
    return table(rows, "Decisive/safe distance per characteristic, calibrated within the family (floors)",
                 "tab:qcdist", "l" + "r" * len(RULES), head, colsep="5pt")


def t_scenarios() -> str:
    s = pd.read_csv(RESULTS / "scen_scores.csv").set_index(["scope", "method"])
    tr = pd.read_csv(RESULTS / "scen_truth.csv")
    rows = []
    for m in RULES:
        cells = []
        for scope in ["within", "transfer"]:
            x = s.loc[(scope, m)]
            cells.append(f"{pct(x['correct'])} & {pct(x['false_accept'])} & {pct(x['false_reject'])} & "
                         f"{pct(x['uncertain'])}")
        rows.append(f"{RULE[m]} & " + " & ".join(cells))
    n = tr.groupby(["qc", "tol_class"])["meets"].sum()
    note = (r"Nine requirements (wall angle and arm angle: ISO 2768-1 classes f/m, c, v; bottom flatness: "
            r"ISO 2768-2 classes H, K, L) for 18 alternatives, 162 decisions per rule and scope. Alternatives "
            f"meeting the limit: wall angle f/m {n[('wall_op10', 'f/m')]}, c {n[('wall_op10', 'c')]}, "
            f"v {n[('wall_op10', 'v')]}; arm angle f/m {n[('arm_op20', 'f/m')]}, c {n[('arm_op20', 'c')]}, "
            f"v {n[('arm_op20', 'v')]}; flatness H {n[('dome_op20', 'H')]}, K {n[('dome_op20', 'K')]}, "
            f"L {n[('dome_op20', 'L')]}.")
    head = (r" & \multicolumn{4}{c}{Within family (\%)} & \multicolumn{4}{c}{Transfer (\%)} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}" "\n"
            r"Rule & right & FA & FR & trial & right & FA & FR & trial")
    note += r" FA: false accept; FR: false reject; trial: uncertain."
    return table(rows, "Verdicts against requirements from general tolerances", "tab:scenarios",
                 "lrrrrrrrr", head, colsep="4pt", note=note)


def t_design_space() -> str:
    s = pd.read_csv(RESULTS / "ds_sensitivity.csv")
    s = s[s["factor"].isin(["bhf_kN", "friction_coefficient", "sheet_metal_thickness"])]
    s["ratio"] = s["sim_sensitivity"] / s["real_sensitivity"]
    p = s.pivot_table(index="qc", columns=["factor", "geometry"], values="ratio")
    rows = []
    for c in SHARED:
        rows.append(f"{LABEL[c]} & " + " & ".join(
            sig(p.loc[c, (f, g)], 2) for f in ["bhf_kN", "sheet_metal_thickness", "friction_coefficient"]
            for g in ["concave", "convex"]))
    head = (r" & \multicolumn{2}{c}{Blank-holder force} & \multicolumn{2}{c}{Sheet thickness} & "
            r"\multicolumn{2}{c}{Friction} \\" "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Characteristic & Conc. & Conv. & Conc. & Conv. & Conc. & Conv.")
    return table(rows, "Simulated over measured sensitivity per factor", "tab:dsratio", "lrrrrrr", head,
                 colsep="5pt",
                 note=r"Ratio of the slope of the characteristic on the factor in the matched simulations to the "
                      r"slope measured in production (blank-holder force: between cells; sheet thickness and "
                      r"friction equivalent of the oil film: within series). A negative ratio is an effect of the "
                      r"opposite sign.")


def t_inline() -> str:
    a = pd.read_csv(RESULTS / "inline_lod.csv").set_index("qc")
    b = pd.read_csv(RESULTS / "inline_drift.csv").set_index("qc")
    rows = []
    for c in SHARED:
        rows.append(f"{LABEL[c]} & {a.loc[c, 'r2_oof']:.2f} & {a.loc[c, 'r2_oof_linear']:.2f} & "
                    f"{a.loc[c, 'lod_over_sd']:.1f} & {b.loc[c, 'r2_oof_batch']:.2f} & "
                    f"{100 * b.loc[c, 'floor_reduction']:.0f}")
    head = (r" & \multicolumn{3}{c}{Part level} & \multicolumn{2}{c}{Batch level} \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(lr){5-6}" "\n"
            r"Characteristic & $R^2$ GB & $R^2$ ridge & LOD/SD & $R^2$ & Floor change (\%)")
    return table(rows, "In-line verifiability of the characteristics from the press-force record", "tab:inline",
                 "lrrrrr", head, colsep="5pt",
                 note=r"Out-of-fold $R^2$ of gradient boosting (GB) and ridge regression on force, sheet-thickness "
                      r"and oil-film features, folds by production batch; LOD: limit of detection of a deviation "
                      r"(5\,\% false alarms, 95\,\% detection) over the within-alternative SD. Batch level: drift "
                      r"between batch centres predicted with folds by alternative, and the reduction of the floor "
                      r"after removing it (negative: the floor grows).")


def t_design() -> str:
    d = pd.read_csv(RESULTS / "budget_design.csv")
    d = d[(d["class_type"] == "brackets") & d["k"].isin([2, 3, 4, 5])].set_index(["method", "class", "k"])
    rows = []
    for m in ["M1", "M2", "M5"]:
        for cls, name in ((True, "brackets"), (False, "extrapolates")):
            cells = []
            for k in [2, 3, 4, 5]:
                x = d.loc[(m, cls, k)]
                cells.append(f"{num(x['safe_floors'])} & {pct(x['error_at_10'])}")
            rows.append(f"{RULE[m]} & {name} & " + " & ".join(cells))
    head = ("Rule & Calibration set & " + " & ".join(f"\\multicolumn{{2}}{{c}}{{$k={k}$}}" for k in [2, 3, 4, 5])
            + r" \\" "\n" r"\cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}\cmidrule(lr){9-10}" "\n"
            r" & & $\delta_\mathrm{s}$ & wrong & $\delta_\mathrm{s}$ & wrong & $\delta_\mathrm{s}$ & wrong & "
            r"$\delta_\mathrm{s}$ & wrong")
    return table(rows, "Calibration design: safe distance and wrong verdicts at 10 floors by calibration set",
                 "tab:design", "llrrrrrrrr", head, colsep="3.5pt",
                 note=r"All subsets of $k$ produced alternatives of the family; ``brackets'': the blank-holder forces "
                      r"of the calibration alternatives enclose that of the new design. Safe distance in floors; "
                      r"wrong: share of wrong verdicts at $|d|=10$ (\%).")


TABLES = {"floors": t_floors, "resolve": t_resolve, "offsets": t_offsets, "distances": t_distances,
          "distci": t_distci, "qcdist": t_qc_distances, "scenarios": t_scenarios, "dsratio": t_design_space,
          "inline": t_inline, "design": t_design}


def main() -> None:
    s = MAIN.read_text()
    for name, fn in TABLES.items():
        if f"%% BEGIN GENERATED {name}" in s:
            write_block(name, fn())
            print(f"{name}: written")


if __name__ == "__main__":
    main()
