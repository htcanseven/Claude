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
RULE = {"M0": "M0 nominal simulation", "M0w": "M0w worst case of the process window",
        "M1": "M1 bias-corrected simulation", "Mc": "Mc friction-calibrated simulation",
        "M2": "M2 envelope + residual margin", "M3": "M3 simulation + boosting", "M5": "M5 GP correction of the envelope",
        "M1n": "M1n median of the produced", "NN": "NN nearest produced setting", "M2n": "M2n median + residual margin",
        "M4": "M4 boosting, no simulation", "M5n": "M5n GP of $q_{95}$, no simulation"}
RULES = ["M0", "M0w", "M1", "Mc", "M2", "M3", "M5", "M1n", "NN", "M2n", "M4", "M5n"]
GROUPS = [("Simulation only", ["M0", "M0w"]), ("Simulation and production record", ["M1", "Mc", "M2", "M3", "M5"]),
          ("Production record only", ["M1n", "NN", "M2n", "M4", "M5n"])]
POINT = {"M0", "M1", "Mc", "M1n", "NN"}
RULE_MED = {"M0": "M0 nominal simulation", "M0w": "M0w process-window worst case", "M1": "M1 bias-corrected",
            "Mc": "Mc friction-calibrated", "M2": "M2 envelope + margin", "M3": "M3 simulation + boosting",
            "M5": "M5 GP correction", "M1n": "M1n median", "NN": "NN nearest setting", "M2n": "M2n median + margin",
            "M4": "M4 boosting", "M5n": "M5n GP of $q_{95}$"}
RULE_SHORT = {"M0": "M0", "M0w": "M0w", "M1": "M1", "Mc": "Mc", "M2": "M2", "M3": "M3", "M5": "M5", "M1n": "M1n",
              "NN": "NN", "M2n": "M2n", "M4": "M4", "M5n": "M5n"}
SCOPES = [("within", "New variant"), ("setting", "New setting"), ("setting/interpolation", "Interpolation"),
          ("setting/extrapolation", "Extrapolation"), ("transfer", "New family")]


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


def dist(x: float) -> str:
    """A distance in floors: one decimal below 10, whole floors above; infinity when a rule never qualifies."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "--"
    if not np.isfinite(x):
        return r"$\infty$"
    x = x + 1e-9                                  # distances lie on a 0.05 grid: round halves up
    return f"{x:.1f}" if x < 10 else f"{x:.0f}"


def pair(x: pd.Series, m: str) -> str:
    """decisive/safe; a point rule (always decides) shows one number."""
    return dist(x["resolution_floors"]) if m in POINT else f"{dist(x['resolution_floors'])}/{dist(x['safe_floors'])}"


def t_floors() -> str:
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    dr = pd.read_csv(RESULTS / "sens_drift.csv").set_index("qc")
    rows = []
    for c in SHARED:
        f = fl.loc[c]
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & {sig(f['floor'])} & {sig(f['floor_lo'])}--{sig(f['floor_hi'])} & "
                    f"{sig(f['floor_lo_alt'])}--{sig(f['floor_hi_alt'])} & {sig(f['floor_concave'])} & "
                    f"{sig(f['floor_convex'])} & {sig(f['sd_within'])} & {dr.loc[c, 'drift_inflation']:.1f}")
    head = (r" & & \multicolumn{2}{c}{95\,\% interval} & & & & \\" "\n" r"\cmidrule(lr){3-4}" "\n"
            r"Characteristic & $F$ & batches & alternatives & Concave & Convex & Part SD & Drift")
    return table(rows, "Production floor per characteristic, pooled and per geometry", "tab:floors",
                 "lrrrrrrr", head, colsep="2.6pt",
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of batch centres. "
                      r"Intervals: 2000 resamples of the batches within the alternatives, and of whole alternatives "
                      r"(clusters). Part SD: median within-alternative standard deviation of single parts. Drift "
                      r"factor: floor over the floor of randomly permuted series. The decision analysis uses the "
                      r"per-geometry floors.")


def t_components() -> str:
    m = pd.read_csv(RESULTS / "meas_floor.csv").set_index("qc")
    rows = []
    for c in SHARED:
        x = m.loc[c]
        rows.append(f"{LABEL[c]} & {x['lt_over_st']:.2f} & {100 * x['white_share']:.0f} & "
                    f"{x['floor_first_half_floors']:.2f} & {x['q95_floor_b100_floors']:.2f} & "
                    f"{x['between_series_median_floors']:.1f} & {x['between_series_q95_floors']:.1f}")
    head = (r" & & & & & \multicolumn{2}{c}{Between series} \\" "\n" r"\cmidrule(lr){6-7}" "\n"
            r"Characteristic & $\sigma_\mathrm{LT}/\sigma_\mathrm{ST}$ & White share (\%) & First half & "
            r"$q_{95}$ floor & median & 95\,\%")
    return table(rows, "What the production floor contains: components and variants in floors", "tab:components",
                 "lrrrrrr", head, colsep="4.5pt",
                 note=r"$\sigma_\mathrm{ST}$: standard deviation within subgroups of five consecutive parts; "
                      r"$\sigma_\mathrm{LT}$: of the whole series (medians over series). White share: the floor that "
                      r"independent part-to-part noise alone would produce, $1.96\sqrt{2/B}$ times the "
                      r"successive-difference standard deviation, over $F$; it bounds the share a scanner's "
                      r"repeatability can explain. First half: floor of the first 250 parts of each series. $q_{95}$ "
                      r"floor: 95\,\% quantile of the difference between the 95th percentiles of two batches of 100 "
                      r"parts. Between series: difference between the centres of the three lubrication series of one "
                      r"geometry and force, an upper bound of the variation between runs (lubrication effects included).")


def t_resolve() -> str:
    e = pd.read_csv(RESULTS / "alt_effects.csv")
    p = pd.read_csv(RESULTS / "rob_bhf_pairs.csv").set_index(["qc", "pair"])
    rows = []
    for c in SHARED:
        g = e[e["qc"] == c]
        cells = []
        for fam in ["geometry", "bhf", "lubrication"]:
            h = g[g["family"] == fam]
            cells.append(f"{int((h['esr'] >= 1).sum())}/{len(h)} & {h['esr'].median():.1f}")
        rows.append(f"{LABEL[c]} & " + " & ".join(cells) +
                    f" & {p.loc[(c, '100->300'), 'mrc_kN']:.0f} & {p.loc[(c, '300->500'), 'mrc_kN']:.0f}")
    tot = []
    for fam in ["geometry", "bhf", "lubrication"]:
        h = e[e["family"] == fam]
        tot.append(f"{int((h['esr'] >= 1).sum())}/{len(h)} & {h['esr'].median():.1f}")
    rows.append(r"\midrule All & " + " & ".join(tot) + " & & ")
    head = (r" & \multicolumn{2}{c}{Geometry} & \multicolumn{2}{c}{Blank-holder force} & "
            r"\multicolumn{2}{c}{Lubrication} & \multicolumn{2}{c}{Force MRC (kN)} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}" "\n"
            r"Characteristic & ESR\,$\geq$\,1 & Median & ESR\,$\geq$\,1 & Median & ESR\,$\geq$\,1 & Median & "
            r"100--300 & 300--500")
    return table(rows, "Single-factor contrasts that production resolves and minimum resolvable force change",
                 "tab:resolve", "lrrrrrrrr", head, colsep="3.5pt",
                 note=r"ESR: effect-to-scatter ratio of two alternatives that differ in one factor; counts of "
                      r"contrasts with ESR\,$\geq$\,1 and median ESR. MRC: floor over the sensitivity of the "
                      r"alternative centres to blank-holder force, between 100 and 300\,kN (the stroke speed also "
                      r"changes) and between 300 and 500\,kN (same speed); the sensitivity is local.")


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
        gm = [g[g["geometry"] == geo]["gap_matched_signed"].median() for geo in ["concave", "convex"]]
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & " + " & ".join(cells) + f" & {gm[0]:+.2f} & {gm[1]:+.2f}")
    head = (r" & \multicolumn{2}{c}{Concave} & \multicolumn{2}{c}{Convex} & \multicolumn{2}{c}{Matched, signed} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Characteristic & Offset & Spread & Offset & Spread & Concave & Convex")
    return table(rows, "Offset between the parts' 95th percentile and the nominal simulation, in floors",
                 "tab:offsets", "lrrrrrr", head, colsep="5pt",
                 note=r"Offset: median over the nine alternatives of a geometry of $(q_{95}-$ nominal "
                      r"simulation$)/F$ on the decision scale (absolute values for the arm angle and the dome); "
                      r"spread: its range over the alternatives. Matched, signed: median difference between the "
                      r"centre of the parts and of their matched simulations, in the characteristic's unit, with "
                      r"signs; the simulated arm angle of the concave cup has the opposite sign of the parts'.")


def t_distances() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r[r["qc"] == "all"].set_index(["scope", "method"])
    rows = []
    for gname, rules in GROUPS:
        rows.append(rf"\multicolumn{{6}}{{@{{}}l}}{{\emph{{{gname}}}}}")
        for m in rules:
            rows.append(f"{RULE_MED[m]} & " + " & ".join(pair(r.loc[(s, m)], m) if (s, m) in r.index else "--"
                                                          for s, _ in SCOPES))
    head = (r" & New & \multicolumn{3}{c}{New process setting} & New \\" "\n" r"\cmidrule(lr){3-5}" "\n"
            r"Rule & variant & all & interpolation & extrapolation & family")
    n = r.loc[("within", "M1"), "n_cases"]
    return table(rows, "Decisive and safe distances (floors) by the relation of the new design to the produced "
                       "evidence", "tab:distances", "lrrrrr", head, colsep="3.5pt",
                 note=r"Decisive/safe distance $\delta_\mathrm{d}/\delta_\mathrm{s}$ over all seven characteristics; "
                      r"one number for rules that always decide ($\delta_\mathrm{d}=\delta_\mathrm{s}$). New variant: a "
                      r"sibling at the same blank-holder force is produced (leave one alternative out within the "
                      r"family); new setting: all alternatives of one force are held out (interpolation at 300\,kN, "
                      r"extrapolation at 100 or 500\,kN); new family: calibration on the other geometry. "
                      f"{int(n)} cases per rule (42 for interpolation, 84 for extrapolation). Intervals in "
                      r"Table~\ref{tab:distci}.")


def t_distci() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r[r["qc"] == "all"].set_index(["scope", "method"])
    rows = []
    for m in RULES:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            if (scope, m) not in r.index:
                cells.append("-- & --")
                continue
            x = r.loc[(scope, m)]
            cells.append(f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])} & "
                         f"{dist(x['safe_lo'])}--{dist(x['safe_hi'])}")
        rows.append(f"{RULE_SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{2}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Rule & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & "
            r"$\delta_\mathrm{d}$ & $\delta_\mathrm{s}$")
    return table(rows, r"Bootstrap 95\,\% intervals of the decisive and safe distances (floors)", "tab:distci",
                 "lrrrrrr", head, colsep="4pt",
                 note=r"1000 resamples of the held-out alternatives within each geometry, each with a "
                      r"block-bootstrap replicate of the true $q_{95}$; the fits are held fixed (refitting: "
                      r"Table~\ref{tab:robust}). A new family rests on two calibrations, one per direction.")


def t_onesided() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r[r["qc"] == "all"].set_index(["scope", "method"])
    rules = ["M0", "M1", "M2", "M3", "M5", "NN", "M4", "M5n"]
    rows = []
    for m in rules:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            x = r.loc[(scope, m)]
            cells.append(f"{dist(x['safe_failing'])} & {dist(x['safe_adequate'])}")
        rows.append(f"{RULE_SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{2}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Rule & FA side & FR side & FA side & FR side & FA side & FR side")
    return table(rows, "One-sided safe distances (floors): false accepts and false rejects", "tab:onesided",
                 "lrrrrrr", head, colsep="4.5pt",
                 note=r"FA side: smallest distance beyond which at most 5\,\% of the verdicts on failing alternatives "
                      r"($d<0$) are false accepts; FR side: the same for false rejects of adequate alternatives "
                      r"($d\ge0$). Requirements below zero are left out.")


def t_coverage() -> str:
    c = pd.read_csv(RESULTS / "dec_coverage.csv").set_index(["scope", "method"])
    rules = ["M0w", "M2", "M3", "M5", "M2n", "M4", "M5n"]
    rows = []
    for m in rules:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            if (scope, m) not in c.index:
                cells.append("-- & -- & --")
                continue
            x = c.loc[(scope, m)]
            cells.append(f"{pct(x['coverage'])} & {dist(x['half_width_floors'])} & {dist(x['centre_decisive'])}")
        rows.append(f"{RULE_SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{3}{c}{New variant} & \multicolumn{3}{c}{New setting} & \multicolumn{3}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}" "\n"
            r"Rule & cov. & half & centre & cov. & half & centre & cov. & half & centre")
    return table(rows, "Interval rules: coverage of the true $q_{95}$, interval width and the accuracy of the centre",
                 "tab:coverage", "lrrrrrrrrr", head, colsep="3.5pt",
                 note=r"cov.: share of cases whose true $q_{95}$ lies in the interval (\%; nominal level 90\,\%; the "
                      r"maximum-residual margin of M2 and M2n attains at most $n/(n+1)$ with $n$ calibration "
                      r"alternatives); half: median half-width (floors); centre: decisive distance of the interval "
                      r"centre used as a point rule (floors).")


def t_paired() -> str:
    p = pd.read_csv(RESULTS / "dec_paired.csv").set_index(["scope", "rule_a", "rule_b"])
    pairs = [("M5", "M5n"), ("M2", "M2n"), ("M1", "M1n"), ("M5", "NN"), ("M5", "M2"), ("M5", "M4"), ("M3", "M4"),
             ("Mc", "M1")]
    rows = []
    for a, b in pairs:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            if (scope, a, b) not in p.index:
                cells.append("--")
                continue
            x = p.loc[(scope, a, b)]
            cells.append(f"{x['resolution_diff']:+.1f} ({x['resolution_diff_lo']:+.1f}, {x['resolution_diff_hi']:+.1f})")
        rows.append(f"{a} $-$ {b} & " + " & ".join(cells))
    head = r"Pair & New variant & New setting & New family"
    return table(rows, "Paired differences of the decisive distance between rules (floors)", "tab:paired",
                 "lrrr", head, colsep="5pt",
                 note=r"Difference and 95\,\% interval from the common resamples of Table~\ref{tab:distci}; a negative "
                      r"difference means that the first rule decides closer to the requirement. M5$-$M5n, M2$-$M2n "
                      r"and M1$-$M1n isolate what the simulation adds to a rule.")


def t_qc_distances() -> str:
    r = pd.read_csv(RESULTS / "dec_resolution.csv")
    r = r.set_index(["scope", "qc", "method"])
    rules = ["M1", "M2", "M5", "NN", "M5n"]
    rows = []
    for c in SHARED:
        cells = []
        for scope in ["within", "setting"]:
            cells += [pair(r.loc[(scope, c, m)], m) for m in rules]
        rows.append(f"{LABEL[c]} & " + " & ".join(cells))
    head = (r" & \multicolumn{5}{c}{New variant} & \multicolumn{5}{c}{New setting} \\" "\n"
            r"\cmidrule(lr){2-6}\cmidrule(lr){7-11}" "\n"
            "Characteristic & " + " & ".join(rules + rules))
    return table(rows, "Decisive/safe distance per characteristic (floors)", "tab:qcdist", "l" + "r" * 10, head,
                 colsep="2.6pt",
                 note=r"18 held-out alternatives per characteristic and scope (36 verdicts per distance and side); "
                      r"one wrong verdict moves a share by 2.8 percentage points.")


def t_design() -> str:
    d = pd.read_csv(RESULTS / "budget_design.csv").set_index(["relation", "method", "k"])
    ks = [1, 2, 4, 6]
    rows = []
    for rel, rname in (("sibling", "sibling"), ("interpolation", "interpolation"), ("extrapolation", "extrapolation")):
        for m in ["M1", "M2", "M5", "NN"]:
            cells = []
            for k in ks:
                if (rel, m, k) not in d.index:
                    cells.append("-- & --")
                    continue
                x = d.loc[(rel, m, k)]
                cells.append(f"{pair(x, m)} & {pct(x['error_at_10'])}")
            rows.append(f"{rname} & {m} & " + " & ".join(cells))
    head = ("Relation & Rule & " + " & ".join(f"\\multicolumn{{2}}{{c}}{{$k={k}$}}" for k in ks) + r" \\" "\n"
            + "".join(f"\\cmidrule(lr){{{3 + 2 * i}-{4 + 2 * i}}}" for i in range(len(ks))) + "\n"
            + " & & " + " & ".join([r"$\delta_\mathrm{d}/\delta_\mathrm{s}$ & wrong"] * len(ks)))
    return table(rows, "Calibration design: distances and wrong verdicts at 10 floors by the relation of the new "
                       "design to the produced alternatives", "tab:design", "llrrrrrrrr", head, colsep="3pt",
                 note=r"All subsets of $k$ produced alternatives of the family. Sibling: the subset holds an alternative "
                      r"at the new design's force; interpolation: no sibling, forces on both sides; extrapolation: no "
                      r"sibling, the new force outside. Wrong: share of wrong verdicts at $|d|=10$ (\%). M5 from $k=2$; "
                      r"interpolation needs at least two alternatives.")


def t_guard() -> str:
    g = pd.read_csv(RESULTS / "dec_guard.csv").set_index(["guard", "scope", "method"])
    rows = []
    for scope, sname in (("setting", "New setting"), ("transfer", "New family")):
        for guard in ["none", "range", "novelty"]:
            cells = []
            for m in ["M2", "M5", "NN"]:
                x = g.loc[(guard, scope, m)]
                cells.append(f"{pair(x, m)} & {int(x['wrong_through'])}/{int(x['verdicts_through'])}")
            fa = g.loc[(guard, scope, "M5")]
            rows.append(f"{sname if guard == 'none' else ''} & {guard} & {int(fa['cases_guarded'])} & "
                        + " & ".join(cells))
    head = (r" & & & \multicolumn{2}{c}{M2} & \multicolumn{2}{c}{M5} & \multicolumn{2}{c}{NN} \\" "\n"
            r"\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}" "\n"
            r"Scope & Guard & Guarded & $\delta_\mathrm{d}/\delta_\mathrm{s}$ & wrong & $\delta_\mathrm{d}/\delta_\mathrm{s}$ & "
            r"wrong & $\delta_\mathrm{d}$ & wrong")
    return table(rows, "Applicability guards: distances and wrong verdicts among the cases a guard lets through",
                 "tab:guard", "llrrrrrrr", head, colsep="3.5pt",
                 note=r"Guarded: cases (of 126) sent to trial. Range guard: geometry not calibrated or blank-holder "
                      r"force outside the calibrated range; novelty guard: simulated $q_{95}$ outside the range of the "
                      r"calibration alternatives. Wrong: wrong verdicts at $|d|=10$ among the verdicts the guard lets "
                      r"through. The family guard equals the range guard for a new family and never fires for a new "
                      r"setting.")


def t_scenarios() -> str:
    s = pd.read_csv(RESULTS / "scen_scores.csv").set_index(["scope", "method"])
    st = pd.read_csv(RESULTS / "scen_strata.csv")
    st = st[st["stratum"] == "0-5"].set_index(["scope", "method"])
    tr = pd.read_csv(RESULTS / "scen_truth.csv")
    rules = ["M0", "M1", "M2", "M5", "NN", "M5n"]
    rows = []
    for m in rules:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            x, y = s.loc[(scope, m)], st.loc[(scope, m)]
            cells.append(f"{pct(x['correct'])} & {pct(y['correct'])} & {pct(x['false_accept_given_fails'])} & "
                         f"{pct(x['uncertain'])}")
        rows.append(f"{RULE_SHORT[m]} & " + " & ".join(cells))
    n_fail = int((~tr["meets"]).sum())
    n_near = int((tr["margin_floors"].abs() < 5).sum())
    head = (r" & \multicolumn{4}{c}{New variant (\%)} & \multicolumn{4}{c}{New setting (\%)} & "
            r"\multicolumn{4}{c}{New family (\%)} \\" "\n" r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}" "\n"
            r"Rule & right & ${<}5$ & FA & trial & right & ${<}5$ & FA & trial & right & ${<}5$ & FA & trial")
    return table(rows, "Verdicts against requirements from general angular tolerances (ISO 2768-1)", "tab:scenarios",
                 "l" + "r" * 12, head, colsep="2.4pt",
                 note=f"Wall and arm angle, classes f/m, c and v, 18 alternatives: {len(tr)} decisions per rule and "
                      f"scope, {n_fail} with a failing alternative and {n_near} with the limit within 5 floors of the "
                      r"truth. right: correct verdicts; ${<}5$: correct verdicts among the decisions within 5 floors; "
                      r"FA: false accepts among the failing alternatives; trial: sent to trial.")


def t_robust() -> str:
    r = pd.read_csv(RESULTS / "rob_decisions.csv").set_index(["variant", "scope", "method"])
    order = [("reference", "Reference"), ("temperature-adjusted", "Temperature-adjusted"),
             ("smoothed simulation", "Smoothed simulation"), ("adequacy share 0.90", "Adequacy share 0.90"),
             ("adequacy share 0.99", "Adequacy share 0.99"),
             ("floor with batch 25 and quantile 0.95", "Floor: batches of 25"),
             ("floor with batch 100 and quantile 0.95", "Floor: batches of 100"),
             ("floor with batch 50 and quantile 0.90", r"Floor: 90\,\% quantile"),
             ("floor with batch 50 and quantile 0.99", r"Floor: 99\,\% quantile"),
             ("resolution target 0.90", r"Target 90\,\%"), ("resolution target 0.99", r"Target 99\,\%"),
             ("interval level 0.80", "Interval level 0.80"), ("interval level 0.95", "Interval level 0.95"),
             ("GP matern", r"GP: Mat\'ern 5/2"), ("GP linear", "GP: linear trend"),
             ("GP onehot", "GP: one-hot lubrication"), ("GP ls_floor", "GP: length-scale floor"),
             ("GP no_noise_floor", "GP: no noise floor")]
    cols = [("within", "M1"), ("within", "M2"), ("within", "M5"), ("within", "NN"), ("setting", "M2"),
            ("setting", "M5"), ("setting", "NN"), ("transfer", "M2"), ("transfer", "M5")]

    def cell(v, scope, m):
        key = (v, scope, m)
        return pair(r.loc[key], m) if key in r.index else ""

    rows = [f"{name} & " + " & ".join(cell(v, s, m) for s, m in cols) for v, name in order]
    lolo = [("leave one pattern out", "lubricant", m) for m in ["M1", "M2", "M5", "NN"]]
    rows.append("Leave one pattern out & " + " & ".join(
        pair(r.loc[k], k[2]) if k in r.index else "" for k in lolo) + " & & & & & ")
    ref = pd.read_csv(RESULTS / "rob_refit.csv").set_index(["scope", "method"])

    def ci(scope, m):
        if (scope, m) not in ref.index:
            return ""
        x = ref.loc[(scope, m)]
        return f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}"

    rows.append(r"\midrule Refit bootstrap, $\delta_\mathrm{d}$ & " +
                " & ".join(ci(s, m) if s != "transfer" else "" for s, m in cols))
    head = (r" & \multicolumn{4}{c}{New variant} & \multicolumn{3}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-5}\cmidrule(lr){6-8}\cmidrule(lr){9-10}" "\n"
            r"Variant & M1 & M2 & M5 & NN & M2 & M5 & NN & M2 & M5")
    return table(rows, "Decisive/safe distances (floors) under the robustness variants", "tab:robust",
                 "l" + "r" * 9, head, colsep="2.6pt",
                 note=r"Alternative-level rules refitted for every variant; empty cells: the variant does not affect "
                      r"the rule. Smoothed simulation: nominal value and envelope from a quadratic response surface "
                      r"over thickness and friction. Floor variants rescale the distances with other floors. Leave one "
                      r"pattern out: columns M1, M2, M5 and NN of the first block. Refit bootstrap: 95\,\% interval of "
                      r"the decisive distance when the alternatives of each geometry are resampled and every rule is "
                      r"refitted (200 resamples).")


def t_tuning() -> str:
    t = pd.read_csv(RESULTS / "tune_decisions.csv").set_index(["scope", "rule", "setting"])
    settings = [("reference", "reference"), ("regularised", "regularised"), ("flexible", "flexible"),
                ("ridge", "ridge"), ("quantile", "quantile loss"), ("selected", "selected")]
    rows = []
    for s, name in settings:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            for rule in ["M3", "M4"]:
                x = t.loc[(scope, rule, s)]
                cells.append(f"{dist(x['resolution_floors'])}/{dist(x['safe_floors'])}")
        rows.append(f"{name} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{2}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Learner & M3 & M4 & M3 & M4 & M3 & M4")
    return table(rows, "Part-level rules M3 and M4 under other learners and settings (decisive/safe, floors)",
                 "tab:tuning", "lrrrrrr", head, colsep="4pt",
                 note=r"Reference: histogram gradient boosting, depth 3, 200 iterations, rate 0.08. Regularised: depth "
                      r"2, 100 iterations, rate 0.05, L2 penalty 1. Flexible: depth 6, 400 iterations, rate 0.1. Ridge: "
                      r"linear regression on the standardised inputs. Quantile loss: boosting of the 95th percentile, "
                      r"no resampled residuals. Selected: the boosting setting with the smallest leave-one-out error "
                      r"over the calibration alternatives.")


def t_scan() -> str:
    s = pd.read_csv(RESULTS / "meas_scan.csv")
    rows = []
    for geo, g in s.groupby("geometry"):
        rng_ = lambda c, f="{:.2f}": f"{f.format(g[c].min())}--{f.format(g[c].max())}"  # noqa: E731
        rows.append(f"{geo} & {rng_('sd_wx')} & {rng_('sd_wy')} & {rng_('r_wx_wy')} & {rng_('wy_minus_wx', '{:.1f}')} & "
                    f"{rng_('sd_EW_mean')} & {rng_('sd_N')} & {rng_('N_minus_EW', '{:.1f}')} & {rng_('r_E_W')}")
    head = (r" & \multicolumn{4}{c}{Flange widths (mm)} & \multicolumn{4}{c}{Wall angles ($^\circ$)} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}" "\n"
            r"Geometry & SD $W_x$ & SD $W_y$ & $r(W_x,W_y)$ & $W_y-W_x$ & SD E/W & SD N & N$-$E/W & $r$(E,W)")
    return table(rows, "Redundancy of the scans: ranges over the nine series of each geometry", "tab:scan",
                 "l" + "r" * 8, head, colsep="2.8pt",
                 note=r"$W_x$, $W_y$: flange width across the cup in the two scan directions; E/W: mean of the east and "
                      r"west walls; N: north wall; $r$: correlation over the parts of a series.")


def t_simnoise() -> str:
    s = pd.read_csv(RESULTS / "meas_sim.csv").set_index(["qc", "geometry"])
    rows = []
    for c in SHARED:
        cells = []
        for geo in ["concave", "convex"]:
            x = s.loc[(c, geo)]
            cells.append(f"{x['roughness_sd_floors']:.1f} & {x['env_hi_minus_smooth_floors_max']:.1f}")
        rows.append(f"{LABEL[c]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{Concave} & \multicolumn{2}{c}{Convex} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}" "\n"
            r"Characteristic & noise & envelope & noise & envelope")
    return table(rows, "Extraction noise of the simulated characteristics (floors)", "tab:simnoise", "lrrrr", head,
                 colsep="6pt",
                 note=r"Noise: standard deviation of the second difference of the simulated value along the friction "
                      r"grid over $\sqrt{1.5}$ (white noise of the extraction). Envelope: largest difference between "
                      r"the maximum of the simulated values of a geometry and force and the maximum of a quadratic "
                      r"response surface over thickness and friction.")


def t_gp() -> str:
    g = pd.read_csv(RESULTS / "dec_gp.csv").set_index(["scope", "method"])
    rows = []
    for scope, name in (("within", "New variant"), ("setting", "New setting"), ("pooled", "Pooled variant"),
                        ("transfer", "New family")):
        cells = []
        for m in ["M5", "M5n"]:
            x = g.loc[(scope, m)]
            cells.append(f"{int(x['fits'])} & {pct(x['noise_at_bound'])} & {pct(x['length_scale_at_bound'])}")
        rows.append(f"{name} & " + " & ".join(cells))
    head = (r" & \multicolumn{3}{c}{M5} & \multicolumn{3}{c}{M5n} \\" "\n" r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}" "\n"
            r"Scope & fits & noise (\%) & length (\%) & fits & noise (\%) & length (\%)")
    return table(rows, "Gaussian-process fits with a hyperparameter at a bound", "tab:gp", "lrrrrrr", head,
                 colsep="5pt",
                 note=r"Share of the fits (calibration set and characteristic) whose noise level sits at its lower "
                      r"bound, the sampling variance of the calibration alternatives' $q_{95}$, and with at least one "
                      r"length scale at a bound (0.1 or 100 in units of 100\,kN or one lubrication step).")


TABLES = {"floors": t_floors, "components": t_components, "resolve": t_resolve, "offsets": t_offsets,
          "distances": t_distances, "distci": t_distci, "onesided": t_onesided, "coverage": t_coverage,
          "paired": t_paired, "qcdist": t_qc_distances, "design": t_design, "guard": t_guard,
          "scenarios": t_scenarios, "robust": t_robust, "tuning": t_tuning, "scan": t_scan, "simnoise": t_simnoise,
          "gp": t_gp}


def main() -> None:
    s = MAIN.read_text()
    failed = []
    for name, fn in TABLES.items():
        if f"%% BEGIN GENERATED {name}" not in s:
            print(f"{name}: no block in main.tex")
            continue
        try:
            write_block(name, fn())
            print(f"{name}: written")
        except (KeyError, FileNotFoundError, ValueError) as e:      # a result file not yet regenerated
            failed.append(name)
            print(f"{name}: FAILED ({type(e).__name__}: {e})")
    if failed:
        sys.exit(f"tables not written: {', '.join(failed)}")


if __name__ == "__main__":
    main()
