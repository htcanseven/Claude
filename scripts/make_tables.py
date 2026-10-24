"""Write the data tables of the manuscript from the result CSVs.

Every number in a table comes from a CSV in results/; nothing is typed by hand. Each table sits between
'%% BEGIN GENERATED <name>' and '%% END GENERATED <name>' in paper/main.tex or paper/online_resource_1.tex (the
electronic supplementary material, Tables S1-S15). The results that neither tabulates are in the result files and
their summaries (results/summary_*.md); results/findings.md maps every number of the paper to its file.

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
OR1 = ROOT / "paper" / "online_resource_1.tex"
LABEL = {"drawin_mid": "Draw-in, mid-side", "drawin_corner": "Draw-in, corner", "waviness": "Flange waviness",
         "wall_op10": "Wall angle", "arm_op20": "Arm angle, cut", "depth_op10": "Cup depth",
         "dome_op20": "Bottom dome, cut"}
UNIT = {"drawin_mid": "mm", "drawin_corner": "mm", "waviness": "mm", "wall_op10": r"$^\circ$",
        "arm_op20": r"$^\circ$", "depth_op10": "mm", "dome_op20": "mm"}
QSHORT = {"drawin_mid": "Mid-side", "drawin_corner": "Corner", "waviness": "Wavin.", "wall_op10": "Wall",
          "arm_op20": "Arm", "depth_op10": "Depth", "dome_op20": "Dome"}
MAIN_RULES = ["M0", "M1s", "M2", "M5", "M7n", "NN", "M1sn", "NN+RM"]
FURTHER = ["M1", "M1n", "M2n", "M5n", "M7", "Mc", "Mcd", "M0w", "M3", "M4", "M6"]
ALL_RULES = MAIN_RULES + FURTHER
POINT = {"M0", "M1", "M1s", "Mc", "M1n", "M1sn", "NN"}
SHORT = {r: r for r in ALL_RULES} | {"M4": "M3n", "M4+RM": "M3n+RM", "NN+RM": "NN+RM"}
MARK = {"M1s": r"$^\dagger$", "NN": r"$^\dagger$", "M1sn": r"$^\dagger$", "M1n": r"$^\dagger$", "M2n": r"$^\dagger$",
        "M5n": r"$^\dagger$", "M0w": r"$^\dagger$", "Mc": r"$^\dagger$", "M6": r"$^\dagger$", "M7n": r"$^\ddagger$",
        "M7": r"$^\ddagger$", "Mcd": r"$^\ddagger$", "NN+RM": r"$^\ddagger$"}
DD = r"$\delta_\mathrm{d}/\delta_\mathrm{s}$"
REL = [("within", "setting/interpolation", "setting/extrapolation", "transfer")]
RELS = [("within", "Sibling"), ("setting/interpolation", "Interpolated"), ("setting/extrapolation", "Extrapolated"),
        ("transfer", "New family")]


# ── writing ───────────────────────────────────────────────────────────────────
def write_block(path: Path, name: str, body: str) -> None:
    s = path.read_text()
    start, end = f"%% BEGIN GENERATED {name}\n", f"%% END GENERATED {name}\n"   # whole lines: s-prior is not s-priors
    if start not in s:
        raise KeyError(f"no block {name} in {path.name}")
    k = s.index(start) + len(start)
    j = s.index(end, k)
    path.write_text(s[:k] + body.rstrip("\n") + "\n" + s[j:])


# ── formatting ────────────────────────────────────────────────────────────────
def sig(x: float, n: int = 2) -> str:
    """Round to n significant figures, without scientific notation."""
    if x is None or not np.isfinite(x):
        return "--"
    if x == 0:
        return "0"
    d = max(n - int(np.floor(np.log10(abs(x)))) - 1, 0)
    return f"{x:.{d}f}"


def pct(x: float) -> str:
    """A share as a whole percentage."""
    return "--" if x is None or not np.isfinite(x) else f"{100 * x + 1e-9:.0f}"


def dist(x: float, below_one: bool = False) -> str:
    """A distance in floors: two decimals below one (the 0.05 grid), one decimal below 10, whole floors above;
    infinity when a rule never qualifies; '<1' below one floor when below_one (beyond what production confirms)."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "--"
    if not np.isfinite(x):
        return r"$\infty$"
    if below_one and x < 1 - 1e-9:
        return "$<$1"
    if abs(x) < 1e-6:
        return "0"
    x = x + 1e-9                                  # distances lie on a 0.05 grid: round halves up
    return f"{x:.2f}" if x < 1 else (f"{x:.1f}" if x < 10 else f"{x:.0f}")


def band(x: float) -> str:
    """A guard band on its 0.25-floor grid: quarters keep two decimals, halves one; 'none' when no band qualifies."""
    if x is None or not np.isfinite(x):
        return "none"
    if abs(x) < 1e-6:
        return "0"
    q = round(4 * x) % 4
    if q in (1, 3):
        return f"{x:.2f}"
    return f"{x:.1f}" if q == 2 or x < 10 else f"{x:.0f}"


def pair(x, m: str, below_one: bool = True) -> str:
    """decisive/safe; a point rule (always decides) shows one number."""
    if x is None:
        return "--"
    d = dist(x["resolution_floors"], below_one)
    return d if m in POINT else f"{d}/{dist(x['safe_floors'], below_one)}"


def table(rows, caption, label, cols, head, colsep=None, note=None, place="t", size=r"\tabsize", full=False):
    """A table float; full=True stretches it to the text width (tabular*)."""
    sep = f"\\setlength{{\\tabcolsep}}{{{colsep}}}\n" if colsep else ""
    foot = f"\\footnotetext{{{note}}}\n" if note else ""
    body = " \\\\\n".join(r.rstrip().rstrip("\\").rstrip() for r in rows)
    begin, end = ((f"\\begin{{tabular*}}{{\\textwidth}}{{@{{\\extracolsep{{\\fill}}}}{cols}@{{}}}}", "\\end{tabular*}") if full
                  else (f"\\begin{{tabular}}{{@{{}}{cols}@{{}}}}", "\\end{tabular}"))
    import re
    caption = re.sub(r"(?<!\\)%", r"\\%", caption.rstrip(".")).replace(" \\%", "\\,\\%")
    return (f"\\begin{{table}}[{place}]\n{size}\n{sep}\\caption{{{caption}}}\\label{{{label}}}\n"
            f"{begin}\n\\toprule\n{head} \\\\\n\\midrule\n{body} \\\\\n"
            f"\\botrule\n{end}\n{foot}\\end{{table}}\n")


def read(name: str, **kw) -> pd.DataFrame:
    return pd.read_csv(RESULTS / name, **kw)


def distances_all() -> pd.DataFrame:
    """Distances over all characteristics of every rule and scope, a new family in the produced family's floor
    ('transfer') and in its own ('transfer/own')."""
    r = pd.concat([read("dec_resolution.csv"), read("learn_resolution.csv")])
    r = r[r["qc"] == "all"]
    own = r[r["scope"] == "transfer"].assign(scope="transfer/own")
    rob = read("rob_decisions.csv")
    m6 = rob[rob["variant"] == "M6 conformalised GP"].assign(method="M6", qc="all")
    src = pd.concat([read("panel_source_floor.csv"), read("learn_source_floor.csv")])
    src = src[(src["floor"] == "source family") & (src["qc"] == "all")].drop_duplicates("method")
    out = pd.concat([r[r["scope"] != "transfer"], own, src.assign(scope="transfer"),
                     m6[m6["scope"] != "transfer"], m6[m6["scope"] == "transfer"].assign(scope="transfer/own")],
                    ignore_index=True)
    return out.drop_duplicates(["scope", "method"]).set_index(["scope", "method"])


def get(r: pd.DataFrame, scope: str, m: str):
    return r.loc[(scope, m)] if (scope, m) in r.index else None


# ── main text ─────────────────────────────────────────────────────────────────
def t_floors() -> str:
    fl = read("alt_floor.csv").set_index("qc")
    rf = read("meas_run_floors.csv").set_index("qc")
    fp = read("panel_floor_protocol.csv").set_index(["qc", "geometry"])
    geos = ("concave", "convex")
    rows = []
    for c in SHARED:
        f, r = fl.loc[c], rf.loc[c]
        lt = "/".join(f"{fp.loc[(c, g), 'floor_over_sigma_lt']:.1f}" for g in geos)
        rows.append(f"{QSHORT[c]} ({UNIT[c]}) & {sig(f['floor'])} & "
                    f"{sig(f['floor_lo_alt'])}--{sig(f['floor_hi_alt'])} & {sig(f['floor_concave'])}/{sig(f['floor_convex'])} & "
                    f"{r['run_floor_min']:.2f}--{r['run_floor_max']:.2f} & {r['warm_up_ratio']:.2f} & {lt}")
    head = (r"Characteristic & $F$ & Interval & Concave/convex & Single runs & No warm-up & "
            r"$F/\sigma_\mathrm{LT}$")
    return table(rows, "Within-run floor per characteristic, pooled and per geometry, with its spread over runs",
                 "tab:floors", "lrrrrrr", head, colsep="3pt", full=True,
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of their 10\,\% trimmed "
                      r"means. Interval: 95\,\% over 2000 resamples of whole alternatives (the narrower interval over "
                      r"resampled batches is in the archive). Single runs: floor of one run over that of its geometry, range over the 18 runs. "
                      r"No warm-up: floor without the first 150 parts over the reference. $\sigma_\mathrm{LT}$: "
                      r"standard deviation of the parts of a series (concave/convex); $\sigma_\mathrm{b}$, "
                      r"$\sigma_\mathrm{w}$ and the drift ratio in Online Resource~1, Table~S4.")


REGION = {"drawin_mid": r"flange mid-sides; $(210-W_x)/2$, $W_x$ along the laser line",
          "drawin_corner": "flange corners; mean of the two diagonals",
          "waviness": "flange; residual SD about a quadratic surface",
          "wall_op10": "side walls at mid-depth; mean of east and west",
          "arm_op20": "cut arms, centre lines; mean of the four arms",
          "depth_op10": "flange above the bottom plane; median",
          "dome_op20": r"bottom sag at $r=40$\,mm; paraboloid fit"}


def num(x: float, d: int = 2, plus: bool = False) -> str:
    """A signed number with a typographic minus."""
    s = f"{abs(x):.{d}f}"
    return f"$-${s}" if x < 0 and float(s) != 0 else (f"+{s}" if plus and x > 0 else s)


def span(a: float, b: float, d: int = 2, unit: str = "") -> str:
    """A range: 'a--b' for positive ends, 'a to b' when an end is negative."""
    if f"{a:.{d}f}" == f"{b:.{d}f}":
        return f"{num(a, d)}{unit}"
    if min(a, b) < 0:
        return f"{num(a, d)} to {num(b, d, plus=a < 0 < b)}{unit}"
    return f"{a:.{d}f}--{b:.{d}f}{unit}"


def t_qcs() -> str:
    import re
    m = read("meas_characteristics.csv").set_index("qc")
    cut = read("meas_cut_walls.csv").iloc[0]
    rows = []
    for c in SHARED:
        x = m.loc[c]
        v = [float(t) for t in re.findall(r"-?\d+\.\d+", str(x["known_biases"]))]
        if c == "drawin_mid":
            bias = f"$W_y-W_x$ {span(v[0], v[1])}\\,mm; $W_y$, in the direction of motion, scatters {v[2]:.1f}--{v[3]:.1f} times more"
        elif c == "drawin_corner":
            bias = f"the two diagonals differ by {span(v[0], v[1])}\\,mm"
        elif c == "wall_op10":
            cw = [float(t) for t in re.findall(r"-?\d+\.\d+", str(cut["cut_wall_north_minus_east_convex"]))]
            bias = (f"convex: north wall {span(v[0], v[1])}$^\\circ$ from east/west (concave {span(v[2], v[3])}$^\\circ$); "
                    f"south wall shadowed, {v[4]:.1f}--{v[5]:.1f}$^\\circ$ off; after the cut, north {span(cw[0], cw[1], 1)}"
                    f"$^\\circ$ off (convex)")
        elif c == "depth_op10":
            bias = "the flange plane is cut away at OP20"
        else:
            bias = "--"
        step = float(x["step_over_floor"])
        rows.append(f"{LABEL[c]} & {x['operation']} & {REGION[c]} & "
                    f"{(f'{step:.2f}' if step >= 0.01 else '$<$0.01')} & {str(x['distinct_per_series']).replace('-', '--')} & {bias}")
    head = r"Characteristic & Op. & Region; definition & Step$/F$ & Values & Direction-dependent differences"
    return table(rows, "The quality characteristics and their measurement by the laser scanner", "tab:qcs",
                 r"L{1.75cm}L{0.75cm}L{3.15cm}rrL{3.85cm}", head, colsep="2.4pt",
                 note=r"Op.: operation measured (OP10 after drawing, OP20 after cutting). Step$/F$: median step between "
                      r"adjacent values in one series over the floor; Values: distinct values per series. Differences from "
                      r"the redundancy of the four sides, ranges of the series medians; the directions "
                      r"used avoid them, their residual bias is unknown. Absolute values are not calibrated against a "
                      r"reference at the size of the part.")


def t_distances() -> str:
    r = distances_all()
    trial = read("qual_trial.csv").set_index("rule")
    rows = []
    for m in MAIN_RULES + ["Mcd"]:
        cells = []
        for scope, _ in RELS:
            x = get(r, scope, m)
            cells += [pair(x, m, True), "--" if x is None else
                      f"{dist(x['safe_failing'], True)}/{dist(x['safe_adequate'], True)}"]
        rows.append(f"{SHORT[m]}{MARK.get(m, '')} & " + " & ".join(cells))
        if m in ("M5", "M7n", "NN"):
            ci = []
            for scope, _ in RELS:
                x = get(r, scope, m)
                ci += ["" if x is None else f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}", ""]
            rows.append(r"\quad interval of $\delta_\mathrm{d}$ & " + " & ".join(ci))
    for n in (20, 50):
        x = trial.loc[f"trial, first {n} parts"]
        rows.append((r"\midrule " if n == 20 else "") + f"Trial, first {n} parts & " +
                    " & ".join([dist(x["resolution_floors"]),
                                f"{dist(x['safe_failing'])}/{dist(x['safe_adequate'])}"] * 4))
    head = (r" & \multicolumn{2}{c}{Sibling} & \multicolumn{2}{c}{Interpolated} & \multicolumn{2}{c}{Extrapolated} & "
            r"\multicolumn{2}{c}{New family} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}" "\n"
            f"Rule & {DD} & FA/FR & {DD} & FA/FR & {DD} & FA/FR & {DD} & FA/FR")
    return table(rows, "Decisive and safe distances (floors) by the relation of the new design to the produced "
                       "evidence", "tab:distances", "l" + "r" * 8, head, colsep="3.4pt",
                 note=r"Over all seven characteristics; one number for rules that always decide; $<$1: below one floor. "
                      r"FA/FR: safe distances on the false-accept and the false-reject side. 126 cases with a sibling and for a new family, 42 "
                      r"interpolated, 84 extrapolated; a new family in the produced family's floor (in its own floor, and "
                      r"all rules, in Online Resource~1, Table~S1). Interval: 95\,\% over 1000 resamples of the held-out "
                      r"alternatives, fits fixed. Mcd: friction calibration with a discrepancy term (Section~\ref{sec:rules}). "
                      r"Trial: the first $n$ parts of the design's own run, a within-run lower bound. $^\dagger$, "
                      r"$^\ddagger$: added after the first results and in the revisions for this journal.")


def t_guards() -> str:
    gd = read("qual_guard_decision.csv")
    rels = [("sibling", "Sibling"), ("interpolation", "Interpolated"), ("extrapolation", "Extrapolated")]
    rows = []

    def bands(x) -> str:
        bc, bv = x["band_concave"], x["band_convex"]
        return band(bc) if band(bc) == band(bv) else f"{band(bc)}/{band(bv)}"

    for prior, lab in (("reference (+-20)", "Reference prior"), ("release-like (+-5)", r"Release-like prior ($\pm5$ floors)")):
        rows.append(rf"\multicolumn{{10}}{{@{{}}l}}{{\emph{{{lab}}}}}")
        for m in ["NN", "M1sn", "M2", "M5", "M7n", "NN+RM"]:
            cells = []
            for rel, _ in rels:
                x = gd[(gd["prior"] == prior) & (gd["relation"] == rel) & (gd["method"] == m)].iloc[0]
                cells += [bands(x), pct(x["share_correct"]) if x["decided"] > 0 else "--", pct(x["trial_rate"])]
            rows.append(f"{SHORT[m]}{MARK.get(m, '')} & " + " & ".join(cells))
    head = (" & " + " & ".join(rf"\multicolumn{{3}}{{c}}{{{lab}}}" for _, lab in rels) + r" \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}" "\n"
            "Rule" + r" & $g$ & Correct & T" * len(rels))
    return table(rows, "Guard bands available when deciding (floors), with their share correct and trial rate",
                 "tab:guards", "l" + "r" * 9, head, colsep="2.2pt", full=True,
                 note=r"$g$: band of the family's own sibling cases with a sibling; for a new setting, which a family "
                      r"produced at two forces cannot exercise, the band of the same relation in the other family "
                      r"(concave/convex; one number when equal; none: no band up to 20 floors reaches 95\,\%). Correct: "
                      r"share correct among decided verdicts (\%), with a sibling leaving one alternative out within its "
                      r"family, for a new setting the other family's band applied to this family. T: share of verdicts "
                      r"sent to trial (\%). No rule qualifies for a new family. Intervals, verdict counts and the "
                      r"characteristics in Online Resource~1, Tables~S10 and S11.")


# ── results per characteristic ────────────────────────────────────────────────
def t_groups() -> str:
    p = read("qual_per_characteristic.csv")
    p = p[p["subset"].isin(SHARED)].set_index(["relation", "method", "subset"])
    cols = [("sibling", "NN"), ("interpolation", "NN"), ("extrapolation", "NN"), ("extrapolation", "M1sn"),
            ("extrapolation", "M1s"), ("new family", "M5")]
    rows = []
    for c in SHARED:
        cells = []
        for rel, m in cols:
            x = p.loc[(rel, m, c)]
            if x["resolution_floors"] < 1 - 1e-9:
                cells.append(f"$<$1 ($<${sig(x['pooled_floor'])})")
            else:
                cells.append(f"{dist(x['resolution_floors'])} ({sig(x['decisive_units'])})")
        x = p.loc[("sibling", "NN", c)]
        rows.append(f"{QSHORT[c]} ({UNIT[c]}) & " + " & ".join(cells) + f" & {x['ppk_at_decisive_median']:.1f}")
    head = (r" & \multicolumn{3}{c}{NN} & M1sn & M1s & M5 & \\" "\n"
            r"\cmidrule(lr){2-4}" "\n"
            r"Characteristic & Sibling & Interp. & Extrap. & Extrap. & Extrap. & New family & $P_\mathrm{pk}$")
    return table(rows, "Decisive distance per characteristic in floors and, in brackets, in its unit", "tab:groups",
                 "lrrrrrrr", head, colsep="1pt", full=True,
                 note=r"18 cases per characteristic with a sibling and for a new family, 6 interpolated, 12 "
                      r"extrapolated; a new family in the produced family's floor. In brackets: the decisive distance "
                      r"computed in the unit, every case scored in the pooled floor (not the distance in floors times a "
                      r"floor). $P_\mathrm{pk}$: median performance index of a requirement at the decisive distance of NN "
                      r"with a sibling. All main rules with both distances in Online Resource~1, Table~S2.")



# ── Online Resource 1 ─────────────────────────────────────────────────────────
SMALL = r"\tabsizesmall"
RELNAME = {"sibling": "Sibling", "interpolation": "Interpolated", "extrapolation": "Extrapolated",
           "new family": "New family"}
SCOPE_OF = {"sibling": "within", "interpolation": "setting/interpolation", "extrapolation": "setting/extrapolation",
            "new family": "transfer"}


def o_all_rules() -> str:
    r = distances_all()
    scopes = [("within", "Sibling"), ("setting/interpolation", "Interpolated"), ("setting/extrapolation", "Extrapolated"),
              ("transfer", "New family"), ("transfer/own", "Own floor")]
    rows = []
    for m in ALL_RULES + ["M1sn+RM", "M1s+RM", "M5n+RM", "M5+RM", "M4+RM", "M7n+RM", "M7+RM"]:
        cells = [pair(get(r, sc, m), m) for sc, _ in scopes]
        if all(c == "--" for c in cells):
            continue
        rows.append(f"{SHORT.get(m, m)}{MARK.get(m, '')} & " + " & ".join(cells))
        ci = []
        for sc, _ in scopes:
            x = get(r, sc, m)
            ci.append("" if x is None or "resolution_lo" not in x or not np.isfinite(x["resolution_lo"]) else
                      f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}")
        if any(ci):
            rows.append(r"\quad interval & " + " & ".join(ci))
    head = "Rule & " + " & ".join(lab for _, lab in scopes)
    return table(rows, "All rules: decisive/safe distances (floors) by relation, with the 95 % interval of the decisive "
                       "distance", "tab:s-all", "l" + "r" * len(scopes), head, colsep="4pt", place="p", size=SMALL,
                 note=r"One number for rules that always decide. New family: in the produced family's floor, as step 6 "
                      r"scores it; own floor: in the new family's floor. Intervals over 1000 resamples of the held-out "
                      r"alternatives, fits fixed. M3n is M4 in the code; P+RM: predictor P with the relation-matched "
                      r"interval. $^\dagger$, $^\ddagger$: added after the first results and in the revisions for this "
                      r"journal. Source: \texttt{dec\_resolution}, \texttt{learn\_resolution}, \texttt{panel\_source\_floor}, "
                      r"\texttt{learn\_source\_floor}, \texttt{rob\_decisions}.")


def o_per_qc() -> str:
    pq = read("qual_per_characteristic.csv")
    pq = pq[pq["subset"].isin(SHARED)]
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        rows.append(rf"\multicolumn{{8}}{{@{{}}l}}{{\emph{{{RELNAME[rel]}}}}}")
        for m in ["M0", "M1s", "M2", "M5", "M7n", "M7", "NN", "M1sn", "M3"]:
            x = pq[(pq["relation"] == rel) & (pq["method"] == m)].set_index("subset")
            if x.empty:
                continue
            cells = [pair(x.loc[q], m) for q in SHARED]
            rows.append(f"{SHORT.get(m, m)} & " + " & ".join(cells))
    fl = read("alt_floor.csv").set_index("qc")["floor"]
    rows.append(r"\midrule Pooled floor & " + " & ".join(f"{sig(fl[q])}" for q in SHARED))
    head = "Rule & " + " & ".join(f"{QSHORT[q]} ({UNIT[q]})" for q in SHARED)
    return table(rows, "Decisive/safe distances (floors) per characteristic", "tab:s-qc", "l" + "r" * 7, head,
                 colsep="2.4pt", place="p", size=SMALL,
                 note=r"In the floor of the characteristic's geometry; a new family in the produced family's floor. 18 "
                      r"cases per characteristic with a sibling and for a new family, 6 interpolated, 12 extrapolated. "
                      r"Pooled floor: to read the distances in the unit. Source: \texttt{qual\_per\_characteristic}.")


def o_validation() -> str:
    v = read("sim_validation.csv")

    def val(x: float) -> str:
        t = sig(abs(x), 4)
        return f"$-${t}" if x < 0 and float(t) != 0 else t

    rows = []
    for c in SHARED:
        for _, r in v[v["qc"] == c].iterrows():
            lo, hi = r["sim_min_over_friction"], r["sim_max_over_friction"]
            rng = f"{val(lo)} to {val(hi)}" if min(lo, hi) < 0 else f"{val(lo)}--{val(hi)}"
            res = r["residual_at_closest_floors"]
            first = r["bhf_kN"] == 100
            xy = "" if not first or not np.isfinite(r["sim_xy_sd_floors"]) else f"{r['sim_xy_sd_floors']:.1f}"
            rough = f"{r['sim_roughness_sd_floors']:.1f}" if first else ""
            if r["geometry"] == "concave" and first:
                rows.append(rf"\multicolumn{{10}}{{@{{}}l}}{{\emph{{{LABEL[c]} ({UNIT[c]})}}}}")
            rows.append(f"{r['geometry'] if first else ''} & "
                        f"{int(r['bhf_kN'])} & {val(r['measured_centre'])} & {val(r['sim_nominal'])} & "
                        f"{num(r['sim_minus_measured_floors'], 0)} & {rng} & {r['closest_mu']:.2f} & "
                        f"{num(res, 1) if abs(res) >= 0.05 else '0.0'} & {xy} & {rough}")
    mc = read("sim_mc_friction.csv")
    head = (r"Geometry & kN & Measured & $\mu=0.10$ & Floors & Range over $\mu$ & Closest $\mu$ & "
            r"Residual & $x$--$y$ & Rough.")
    return table(rows, "The simulation dataset against the measurement per characteristic, geometry and force",
                 "tab:s-validation", "lrrrrrrrrr", head, colsep="3pt", place="p", size=SMALL,
                 note=rf"Values in the unit of the characteristic (signed); simulation at 0.99\,mm. $\mu=0.10$: the "
                      rf"nominal simulation; floors: its difference from the measurement. Range over $\mu$: over the "
                      rf"friction grid 0.05--0.15; closest $\mu$: grid friction nearest the measurement, residual there "
                      rf"(floors). $x$--$y$, Rough.: extraction noise of the simulated characteristic, standard deviation "
                      rf"of the difference between the two directions of the quarter model and roughness along the friction "
                      rf"grid (floors). Levels depend on the assumed blank (210\,mm) and the scanner's scales; the force "
                      rf"effects, the concave wall-angle trend, the arm sign and the dome ranking do not. Mc's friction fits "
                      rf"end at the upper edge of the grid in {int(mc['at_upper_edge'].sum())} of {len(mc)} within-family "
                      rf"calibrations. Source: \texttt{{sim\_validation}}, \texttt{{sim\_mc\_friction}}.")


def o_scan() -> str:
    m = read("meas_scan.csv")
    fp = read("panel_floor_protocol.csv").set_index(["qc", "geometry"])
    dr = read("sens_drift.csv").set_index("qc")
    rows = []
    for _, r in m.iterrows():
        rows.append(f"{r['alternative']} & {r['wy_minus_wx']:.2f} & {r['sd_wy'] / r['sd_wx']:.1f} & {r['r_wx_wy']:.2f} & "
                    f"{r['diag_difference']:.2f} & {r['N_minus_EW']:.2f} & {r['r_E_W']:.2f}")
    rows.append(r"\midrule \multicolumn{7}{@{}l}{\emph{Components of the floor (fractions of the floor), concave/convex}} \\")
    rows.append(r"Characteristic & \multicolumn{2}{c}{$\sigma_\mathrm{b}/F$} & \multicolumn{2}{c}{$\sigma_\mathrm{w}/F$} & "
                r"\multicolumn{2}{c}{Drift ratio}")
    for c in SHARED:
        sb = "/".join(f"{fp.loc[(c, g), 'sigma_between_batch'] / fp.loc[(c, g), 'floor']:.2f}" for g in ("concave", "convex"))
        sw = "/".join(f"{fp.loc[(c, g), 'sigma_within_batch'] / fp.loc[(c, g), 'floor']:.2f}" for g in ("concave", "convex"))
        rows.append(f"{LABEL[c]} & \\multicolumn{{2}}{{c}}{{{sb}}} & \\multicolumn{{2}}{{c}}{{{sw}}} & "
                    f"\\multicolumn{{2}}{{c}}{{{dr.loc[c, 'drift_inflation']:.1f}}}")
    head = r"Series & $W_y-W_x$ & $\sigma_y/\sigma_x$ & $r_{xy}$ & Diagonals & N$-$EW & $r_\mathrm{EW}$"
    return table(rows, "Redundancy of the scans per series, and the components of the floor", "tab:s-scan",
                 "lrrrrrr", head, colsep="4pt", place="p", size=SMALL,
                 note=r"$W_y-W_x$: flange width in the direction of motion minus that along the laser line (mm); "
                      r"$\sigma_y/\sigma_x$: ratio of their part-to-part standard deviations; $r_{xy}$: their correlation; "
                      r"diagonals: difference of the two flange diagonals (mm); N$-$EW: north wall angle minus the mean of "
                      r"east and west ($^\circ$); $r_\mathrm{EW}$: correlation of east and west. $\sigma_\mathrm{b}$: "
                      r"standard deviation between batch means; $\sigma_\mathrm{w}$: within batches; drift ratio: floor over "
                      r"that of the series in random order. Source: \texttt{meas\_scan}, \texttt{panel\_floor\_protocol}, "
                      r"\texttt{sens\_drift}.")


def o_gp() -> str:
    g = read("learn_gp_diagnostics.csv").set_index(["relation_scope", "method"])
    rels = [("sibling", "Sibling"), ("interpolation", "Interpolated"), ("extrapolation", "Extrapolated"),
            ("new family", "New family"), ("pooled interpolation", "Pooled interp."),
            ("pooled extrapolation", "Pooled extrap.")]
    rows = []
    for rel, lab in rels:
        for m in ["M5", "M5n", "M7n", "M7"]:
            if (rel, m) not in g.index:
                continue
            x = g.loc[(rel, m)]
            noise = (f"{x['median_noise_over_bound']:.2f}" if m in ("M5", "M5n")
                     else f"{x['median_nugget_floors'] / x['median_se_floors']:.1f}")
            low = pct(x["ls_at_lower_share"]) if m in ("M5", "M5n") else "--"
            lead = lab if m == "M5" else ""
            rows.append(f"{lead} & {m} & {int(x['fits'])} & {x['median_ls_bhf']:.2f} & {low} & {noise} & "
                        f"{dist(x['median_d_calib_mean'])} & {pct(x['share_within_001_of_calib_mean'])} & "
                        f"{dist(x['median_d_nn'])} & {dist(x['median_d_m1sn'])} & {dist(x['median_half_width'])}")
    head = (r"Relation & Rule & Fits & $\ell_F$ & At bound & Noise & $\Delta$mean & ${\le}0.01$ & $\Delta$NN & "
            r"$\Delta$M1sn & HW")
    return table(rows, "Fitted Gaussian processes by relation: hyperparameters and where their centres lie", "tab:s-gp",
                 "llrrrrrrrrr", head, colsep="3pt", place="p", size=SMALL,
                 note=r"$\ell_F$: median force length scale (100\,kN). At bound: fits with $\ell_F$ at its lower bound "
                      r"(\%). Noise: fitted noise over its bound (M5, M5n) or nugget over the sampling error of the truths "
                      r"(M7n, M7), median. $\Delta$mean, $\Delta$NN, $\Delta$M1sn: median distance (floors) of the centre "
                      r"from the calibration mean, NN and M1sn; ${\le}0.01$: cases within 0.01 floor of the calibration mean "
                      r"(\%). HW: median half-width (floors). Pooled: both families calibrate, with a family term. Source: "
                      r"\texttt{learn\_gp\_diagnostics}.")


def o_priors() -> str:
    s_ = read("learn_m7n_priors.csv")
    rels = ["sibling", "interpolation", "extrapolation"]
    order = ["reference"] + [v for v in s_["variant"].unique() if v != "reference"]
    rows = []
    for v in order:
        cells = []
        for rel in rels:
            x = s_[(s_["variant"] == v) & (s_["relation"] == rel)].iloc[0]
            cells += [f"{dist(x['resolution_floors'], True)}/{dist(x['safe_floors'], True)}", pct(x["coverage"]),
                      f"{x['median_half_width']:.1f}"]
            if rel != "sibling":
                cells.append(f"{x['median_d_force_trend']:.2f}")
        rows.append(f"{v} & " + " & ".join(cells))
    head = (r" & \multicolumn{3}{c}{Sibling} & \multicolumn{4}{c}{Interpolated} & \multicolumn{4}{c}{Extrapolated} \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(lr){5-8}\cmidrule(lr){9-12}" "\n"
            f"Prior median & {DD} & Cov & HW & {DD} & Cov & HW & $\\Delta$M1sn & {DD} & Cov & HW & $\\Delta$M1sn")
    return table(rows, "The trend GP M7n with each of its four prior medians halved or doubled", "tab:s-priors",
                 "l" + "r" * 11, head, colsep="2.4pt", place="p", size=SMALL,
                 note=r"Reference medians: force length scale 200\,kN, lubrication length scale one pattern step, GP "
                      r"standard deviation two floors, nugget standard deviation one floor; one median changed at a time, "
                      r"every calibration set refitted. Cov: coverage of the 90\,\% interval (\%); HW: median half-width "
                      r"(floors); $\Delta$M1sn: median distance of the centre from the force trend (floors). For a new family "
                      r"every variant decides beyond 131 floors and covers no truth. The reference row reproduces the "
                      r"stored intervals exactly. Source: \texttt{learn\_m7n\_priors}.")


def o_crossing() -> str:
    r = distances_all()
    cov = read("qual_coverage.csv")
    allc = cov[cov["subset"] == "all"].set_index(["relation", "method"])
    fam = cov[cov["subset"].str.startswith("family", na=False)]
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        rows.append(rf"\multicolumn{{7}}{{@{{}}l}}{{\emph{{{RELNAME[rel]}}}}}")
        entries = [(f"{p}+RM", f"{SHORT.get(p, p)}+RM", SCOPE_OF[rel], rel) for p in
                   ["NN", "M1sn", "M1s", "M5n", "M5", "M4", "M7n", "M7"]]
        entries += [(m, f"{SHORT.get(m, m)} (own)", SCOPE_OF[rel], rel) for m in ["M2", "M3", "M5", "M7n"]]
        if rel != "new family":
            psc = {"sibling": "pooled", "interpolation": "pooled-setting/interpolation",
                   "extrapolation": "pooled-setting/extrapolation"}[rel]
            entries.append(("M7n", "M7n, both families", psc, f"pooled {rel}"))
        for m, lab, scope, crel in entries:
            x = get(r, scope, m)
            if x is None:
                continue
            c = allc.loc[(crel, m)] if (crel, m) in allc.index else None
            q = ""
            if m.endswith("+RM"):
                f = fam[(fam["relation"] == rel) & (fam["method"] == m)].set_index("subset")
                if len(f) == 2:
                    q = f"{f.loc['family: concave', 'rm_quantile_floors']:.1f}/{f.loc['family: convex', 'rm_quantile_floors']:.1f}"
            if c is not None:
                n = c.get("rm_n", np.nan)
                cov_s, isc, n_s = pct(c["coverage"]), f"{c['interval_score']:.0f}", str(int(n)) if np.isfinite(n) else ""
            else:
                cov_s, isc, n_s = "--", "--", ""
            rows.append(f"{lab} & {pair(x, m, True)} & {dist(x['safe_failing'], True)} & {cov_s} & {isc} & {q} & {n_s}")
    head = f"Predictor and interval & {DD} & FA & Cov & IS & $q$ (c/v) & $n$"
    return table(rows, "Point predictors crossed with the relation-matched interval, against the rules' own intervals and "
                       "a trend GP calibrated on both families", "tab:s-crossing", "lrrrrrr", head, colsep="4pt",
                 place="p", size=SMALL,
                 note=r"P+RM: the prediction of P (for interval rules the interval centre) with the 90\,\% split-conformal "
                      r"quantile $q$ of P's absolute errors (floors) over the $n$ cases of the same relation in the other "
                      r"family; c/v: the quantile borrowed by the concave and by the convex cup. These $n$ cases come from "
                      r"one family and from one or a few shared fits, so the interval carries no coverage guarantee. Own: "
                      r"the rule's own interval. Both families: M7n calibrated on both families with a family term. FA: safe "
                      r"distance on the false-accept side; Cov: coverage (\%); IS: mean interval score at $\alpha=0.1$ "
                      r"(floors). A new family in the produced family's floor. Source: \texttt{learn\_resolution}, "
                      r"\texttt{qual\_coverage}.")


def o_coverage() -> str:
    c = read("qual_coverage.csv")
    a = c[c["subset"] == "all"]
    rows = []
    rels = ["sibling", "interpolation", "extrapolation", "new family"]
    for m in ["M2", "M2n", "M3", "M4", "M5", "M5n", "M7", "M7n", "Mcd", "NN+RM", "M1sn+RM", "M7n+RM"]:
        cells = []
        for rel in rels:
            x = a[(a["relation"] == rel) & (a["method"] == m)]
            if x.empty:
                cells += ["--", "--"]
                continue
            x = x.iloc[0]
            cv = (f"{pct(x['coverage'])} ({pct(x['coverage_lo'])}--{pct(x['coverage_hi'])})" if rel == "sibling"
                  else pct(x["coverage"]))
            cells += [cv, f"{x['interval_score']:.0f}"]
        lvl = a[(a["method"] == m) & (a["relation"] == "sibling")]["level"].iloc[0]
        lvl = lvl.split(" (")[0].replace(" nominal", "")
        rows.append(f"{SHORT.get(m, m)} & {lvl} & " + " & ".join(cells))
    m6 = read("qual_m6_coverage.csv").set_index("relation")
    cells = []
    for rel in rels:
        x = m6.loc[rel]
        cv = (f"{pct(x['coverage'])} ({pct(x['coverage_lo'])}--{pct(x['coverage_hi'])})" if rel == "sibling"
              else pct(x["coverage"]))
        cells += [cv, f"{x['interval_score']:.0f}"]
    rows.append("M6 & 0.90 & " + " & ".join(cells))
    for m in ["NN", "M1sn", "M1s"]:
        cells = []
        for rel in rels:
            x = a[(a["relation"] == rel) & (a["method"] == m)]
            cells += ["--", f"{x.iloc[0]['interval_score']:.0f}" if not x.empty else "--"]
        rows.append(f"{m} & point & " + " & ".join(cells))
    head = (r" & & \multicolumn{2}{c}{Sibling} & \multicolumn{2}{c}{Interpolated} & \multicolumn{2}{c}{Extrapolated} & "
            r"\multicolumn{2}{c}{New family} \\" "\n" r"\cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}\cmidrule(lr){9-10}"
            "\n" r"Rule & Level & Cov & IS & Cov & IS & Cov & IS & Cov & IS")
    return table(rows, "Interval rules: coverage and interval score by relation", "tab:s-coverage", "ll" + "r" * 8,
                 head, colsep="3pt", place="p", size=SMALL,
                 note=r"Level: guaranteed with a sibling (largest residual, jackknife+) or nominal (model-based intervals "
                      r"and P+RM, whose guarantee would need exchangeable families). Cov: coverage (\%), with a sibling with "
                      r"a 95\,\% interval over 2000 resamples of the alternatives within each geometry; for a new setting or "
                      r"family the alternatives of one held-out cell or family share one fit, so no interval over "
                      r"alternatives is given. IS: mean interval score (Gneiting and Raftery 2007) at $\alpha=0.1$, floors; "
                      r"lower is better; for point rules $20\,|e|$. M6: conformal margin on standardised residuals of the "
                      r"calibration set. Source: \texttt{qual\_coverage}, \texttt{qual\_m6\_coverage}.")


def o_coverage_detail() -> str:
    c = read("qual_coverage.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation"]:
        for m in ["M5", "M5n", "M7n", "M3", "Mcd", "NN+RM", "M7n+RM"]:
            x = c[(c["relation"] == rel) & (c["method"] == m)].set_index("subset")
            if x.empty:
                continue
            fam = [pct(x.loc[k, "coverage"]) if k in x.index else "--" for k in ("family: concave", "family: convex")]
            qcs = [pct(x.loc[q, "coverage"]) if q in x.index else "--" for q in SHARED]
            st = [pct(x.loc[k, "coverage"]) if k in x.index else "" for k in ("siblings not resolvable", "siblings resolvable")]
            rows.append(f"{RELNAME[rel] if m == 'M5' else ''} & {SHORT.get(m, m)} & " + " & ".join(fam + qcs + st))
    head = ("Relation & Rule & Conc. & Conv. & " + " & ".join(QSHORT[q] for q in SHARED) + r" & Not res. & Res.")
    return table(rows, "Coverage (%) per family, characteristic and decision-time stratum", "tab:s-coverage-detail",
                 "ll" + "r" * 11, head, colsep="2.1pt", place="p", size=SMALL,
                 note=r"Conc., Conv.: held-out alternatives of the concave and the convex cup (63 cases with a sibling, 21 "
                      r"interpolated, 42 extrapolated each). 18 cases per characteristic with a sibling, 6 interpolated, 12 "
                      r"extrapolated. Not res., Res.: the produced siblings do not or do differ resolvably from each other "
                      r"(75 and 51 cases). Source: \texttt{qual\_coverage}.")


def o_guards() -> str:
    gd = read("qual_guard_decision.csv")
    oos = read("qual_guard_oos.csv")
    rows = []

    def bands(x) -> str:
        bc, bv = x["band_concave"], x["band_convex"]
        return band(bc) if band(bc) == band(bv) else f"{band(bc)}/{band(bv)}"

    for prior, lab in (("reference (+-20)", "Reference prior"), ("release-like (+-5)", r"Release-like prior")):
        rows.append(rf"\multicolumn{{9}}{{@{{}}l}}{{\emph{{{lab}}}}}")
        for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
            for m in ["NN", "M1sn", "M2", "M5", "M5n", "M7n", "Mcd", "NN+RM"]:
                x = gd[(gd["prior"] == prior) & (gd["relation"] == rel) & (gd["method"] == m)]
                if x.empty:
                    continue
                x = x.iloc[0]
                if rel == "new family" and x["decided"] == 0:
                    continue
                share = "--" if x["decided"] == 0 else (
                    f"{pct(x['share_correct'])} ({pct(x['share_correct_lo'])}--{pct(x['share_correct_hi'])})"
                    if np.isfinite(x["share_correct_lo"]) else pct(x["share_correct"]))
                cell_out = ""
                if rel in ("interpolation", "extrapolation"):
                    y = oos[(oos["prior"] == prior) & (oos["relation"] == rel) & (oos["method"] == m)
                            & (oos["scheme"] == "leave force cell out")]
                    if len(y) and np.isfinite(y.iloc[0]["share_correct"]):
                        cell_out = pct(y.iloc[0]["share_correct"])
                worst = ("" if not isinstance(x["worst_characteristic"], str) else
                         f"{QSHORT[x['worst_characteristic']]} {pct(x['worst_share_correct'])}")
                rows.append(f"{RELNAME[rel] if m == 'NN' or (rel == 'new family' and m == 'Mcd') else ''} & "
                            f"{SHORT.get(m, m)} & {bands(x)} & {share} & {pct(x['trial_rate'])} & "
                            f"{int(x['decided'])}/{int(x['verdicts'])} & {100 * x['false_accept_share']:.1f} & {worst} & {cell_out}")
    head = r"Relation & Rule & $g$ (c/v) & Correct & T & Decided & FA & Worst characteristic & Cell out"
    return table(rows, "Guard bands available when deciding, by relation and prior, validated by the matching scheme",
                 "tab:s-guards", "llrrrrrlr", head, colsep="3pt", place="p", size=SMALL,
                 note=r"$g$: band (floors) of the family's own sibling cases (with a sibling) or of the same relation in the "
                      r"other family (new setting, new family), for the concave/convex cup; none: no band up to 20 floors "
                      r"qualifies. Correct: share correct among decided verdicts (\%), with a sibling leaving one alternative "
                      r"out within its family (95\,\% cluster interval over alternatives), otherwise the other family's band on "
                      r"this family. T: share sent to trial (\%). Decided: decided and all verdicts. FA: false accepts (\% of "
                      r"verdicts). Worst characteristic: lowest share correct (\%). Cell out: share correct with the family's "
                      r"own band estimated without the held-out geometry--force cell. New-family rows only where a rule "
                      r"decides. Source: \texttt{qual\_guard\_decision}, \texttt{qual\_guard\_oos}.")


def o_guard_qc() -> str:
    gd = read("qual_guard_decision.csv")
    rows = []
    for prior, lab in (("reference (+-20)", "Reference"), ("release-like (+-5)", "Release-like")):
        for rel in ["sibling", "interpolation", "extrapolation"]:
            for m in ["NN", "M1sn", "M2", "M5", "M7n", "NN+RM"]:
                x = gd[(gd["prior"] == prior) & (gd["relation"] == rel) & (gd["method"] == m)].iloc[0]
                cells = [pct(x.get(f"share_{q}", np.nan)) if x.get(f"decided_{q}", 0) >= 20 else "--" for q in SHARED]
                lead = (f"{lab}, " if rel == "sibling" and m == "NN" else "") + (RELNAME[rel] if m == "NN" else "")
                rows.append(f"{lead} & {SHORT.get(m, m)} & " + " & ".join(cells))
    head = "Prior, relation & Rule & " + " & ".join(QSHORT[q] for q in SHARED)
    return table(rows, "Share correct (%) per characteristic under the guard bands available when deciding",
                 "tab:s-guard-qc", "ll" + "r" * 7, head, colsep="3pt", place="p", size=SMALL,
                 note=r"Bands and validation as in Table~\ref{tab:s-guards}; --: fewer than 20 decided verdicts. Source: "
                      r"\texttt{qual\_guard\_decision}.")


def o_prior_width() -> str:
    w = read("qual_guard_prior_width.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation"]:
        for m in ["NN", "M1sn", "M2", "M5", "M7n", "NN+RM"]:
            x = w[(w["relation"] == rel) & (w["method"] == m)].set_index("prior_half_width")
            cells = [f"{band(x.loc[h, 'band'])} ({pct(x.loc[h, 'trial_rate'])})" for h in (3.0, 5.0, 10.0, 20.0, 50.0)]
            rows.append(f"{RELNAME[rel] if m == 'NN' else ''} & {SHORT.get(m, m)} & " + " & ".join(cells))
    head = r"Relation & Rule & $\pm3$ & $\pm5$ & $\pm10$ & $\pm20$ & $\pm50$"
    return table(rows, "Guard band (floors) and trial rate (%, in brackets) against the half-width of the prior",
                 "tab:s-prior", "ll" + "r" * 5, head, colsep="4pt", place="p", size=SMALL,
                 note=r"Prior: the evaluation grid of requirement distances within the half-width, equal weights; $\pm20$ "
                      r"is the reference prior and $\pm5$ the release-like one. Bands pooled over the families, in sample, "
                      r"to show the dependence on the prior. No rule qualifies for a new family. Source: "
                      r"\texttt{qual\_guard\_prior\_width}.")


def o_costs() -> str:
    c = read("qual_cost_cheapest.csv")
    tc = read("qual_trial_cost.csv")
    rows = []

    def short(name: str) -> str:
        if name == "trial every design":
            return "trial"
        names = name.split(" = ")
        return "NN$^*$" if set(names) == {"NN", "M1sn"} else " = ".join(SHORT.get(n, n) for n in names)

    for prior, lab in (("reference (+-20)", "Reference prior"), ("release-like (+-5)", "Release-like prior")):
        rows.append(rf"\multicolumn{{5}}{{@{{}}l}}{{\emph{{{lab}}}}}")
        for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
            for ct in (0.02, 0.05, 0.1, 0.2, 0.5):
                cells = []
                for cfr in (0.25, 0.5, 1.0):
                    x = c[(c["prior"] == prior) & np.isclose(c["c_fr"], cfr) & (c["relation"] == rel)
                          & np.isclose(c["c_trial"], ct)].iloc[0]
                    cells.append(f"{short(x['cheapest'])} {x['cost']:.3f}")
                rows.append(f"{RELNAME[rel] if ct == 0.02 else ''} & {ct:g} & " + " & ".join(cells))
    t20 = tc[(tc["rule"] == "trial, first 20 parts") & np.isclose(tc["c_fr"], 0.5)].set_index("prior")
    head = r"Relation & $c_\mathrm{T}$ & $c_\mathrm{FR}=0.25$ & $c_\mathrm{FR}=0.5$ & $c_\mathrm{FR}=1$"
    return table(rows, "Cheapest option and its expected cost per verdict by relation, trial cost, prior and cost ratio",
                 "tab:s-costs", "lrlll", head, colsep="5pt", place="p", size=SMALL,
                 note=rf"Costs relative to a false accept. Each rule with its cost-minimising band (0 to 40 floors), chosen "
                      rf"in sample and pooled over the families; trial: sending every design to trial (cost $c_\mathrm{{T}}$) "
                      rf"is cheapest; NN$^*$: NN and M1sn, which coincide at 300\,kN. Differences of a few thousandths are "
                      rf"not resolved by this design. Trials are priced as error-free: the errors of a 20-part trial cost "
                      rf"{t20.loc['reference (+-20)', 'error_cost']:.3f} per verdict under the reference prior and "
                      rf"{t20.loc['release-like (+-5)', 'error_cost']:.3f} under the release-like prior ($c_\mathrm{{FR}}=0.5$); "
                      rf"both priors place {pct(t20.iloc[0]['failing_share_of_verdicts'])}\,\% of the verdicts on failing "
                      rf"designs. Source: \texttt{{qual\_costs}}, \texttt{{qual\_cost\_cheapest}}, \texttt{{qual\_trial\_cost}}.")


def o_between() -> str:
    b = read("qual_between_run.csv")
    tr = read("qual_between_run_trial.csv")
    taus = ("0.0", "1.0", "2.0", "3.0", "bound")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        for m in ["NN", "M1sn", "M1s", "M2", "M5", "M7n"]:
            x = b[(b["relation"] == rel) & (b["method"] == m)].set_index("tau")
            cells = [f"{dist(x.loc[t, 'decisive_median'])} ({band(x.loc[t, 'band_median'])})" for t in taus]
            rows.append(f"{RELNAME[rel] if m == 'NN' else ''} & {SHORT.get(m, m)} & " + " & ".join(cells))
        best = b[b["relation"] == rel].drop_duplicates("tau").set_index("tau")
        rows.append(r"& \emph{record rule best} & " + " & ".join(pct(best.loc[t, "share_record_rule_best"]) for t in taus))
    rows.append(r"\midrule \multicolumn{7}{@{}l}{\emph{The trial, same draws (any relation)}} \\")
    for n in (20, 50):
        x = tr[tr["rule"] == f"trial, first {n} parts"].set_index("tau")
        rows.append(f" & first {n} parts & " + " & ".join(dist(x.loc[t, "decisive_median"]) for t in taus))
    head = r"Relation & Rule & $\tau=0$ & 1 & 2 & 3 & bound"
    return table(rows, "Decisive distance and guard band (floors, in brackets) with a between-run component added to "
                       "the truths, and the trial under the same component", "tab:s-between", "ll" + "r" * 5, head,
                 colsep="4pt", place="p", size=SMALL,
                 note=r"Medians over 200 draws (bands over 50, pooled over the families); $\tau$: standard deviation of the "
                      r"component (floors); bound: each characteristic's variation between series, $\tau=1.2$--$9.8/2.77$. "
                      r"Record rule best: share of draws in which NN, M1sn or M1n is the most decisive rule (\%). The trial "
                      r"saw the observed run; a future run's 95th percentile differs from it by the same component. Source: "
                      r"\texttt{qual\_between\_run}, \texttt{qual\_between\_run\_trial}.")


def o_crossfit() -> str:
    x = read("qual_crossfit.csv")
    rows = []
    for _, r in x.iterrows():
        if r["criterion"] == "step 6":
            if r["rule"] == "none qualifies" or not np.isfinite(r.get("share_correct", np.nan)):
                rows.append(f"{RELNAME[r['relation']]} & step 6 & {r['selected_on']} & "
                            f"{SHORT.get(r['rule'], r['rule'])} & & & {band(r['band']) if 'band' in r and np.isfinite(r['band']) else ''} & -- & 100")
                continue
            rows.append(f"{RELNAME[r['relation']]} & step 6 & {r['selected_on']} & {SHORT.get(r['rule'], r['rule'])} & "
                        f"{dist(r['in_sample'])} & {dist(r['cross_fitted'])} & {band(r['band'])} & "
                        f"{pct(r['share_correct'])} & {pct(r['trial_rate'])}")
        else:
            crit = "decisive" if r["criterion"].startswith("resolution") else "safe"
            rows.append(f"{RELNAME[r['relation']]} & {crit}, {r['pool']} & {r['selected_on']} & "
                        f"{SHORT.get(r['rule'], r['rule'])} & {dist(r['in_sample'])} & {dist(r['cross_fitted'])} & & & ")
    head = r"Relation & Criterion & Selected on & Rule & In sample & Other & $g$ & Correct & T"
    return table(rows, "Rules and guard bands selected on one geometry and evaluated on the other", "tab:s-crossfit",
                 "llllrrrrr", head, colsep="3pt", place="p", size=SMALL,
                 note=r"Selection by the smallest decisive or safe distance among all rules or the pre-specified ones, or by "
                      r"the smallest decisive distance of step 6 (rule and band together); for a new family, selected on one "
                      r"transfer. Other: the distance on the other geometry. Correct, T: share correct among decided "
                      r"verdicts and trial rate there (\%). Source: \texttt{qual\_crossfit}.")


OR_TABLES = {"s-all": o_all_rules, "s-qc": o_per_qc, "s-validation": o_validation, "s-scan": o_scan, "s-gp": o_gp,
             "s-priors": o_priors, "s-crossing": o_crossing, "s-coverage": o_coverage,
             "s-coverage-detail": o_coverage_detail, "s-guards": o_guards, "s-guard-qc": o_guard_qc,
             "s-prior": o_prior_width, "s-costs": o_costs, "s-between": o_between, "s-crossfit": o_crossfit}

MAIN_TABLES = {"floors": t_floors, "qcs": t_qcs, "distances": t_distances, "groups": t_groups, "guards": t_guards}


def main() -> None:
    for path, tables in ((MAIN, MAIN_TABLES), (OR1, OR_TABLES)):
        if not path.exists():
            print(f"{path.name}: missing, skipped")
            continue
        text = path.read_text()
        for name, fn in tables.items():
            if f"%% BEGIN GENERATED {name}\n" not in text:
                print(f"{name}: no block in {path.name}, skipped")
                continue
            write_block(path, name, fn())
            print(f"{path.name} {name}: written")


if __name__ == "__main__":
    main()
