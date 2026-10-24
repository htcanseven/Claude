"""Write the data tables of the manuscript from the result CSVs.

Every number in a table comes from a CSV in results/; nothing is typed by hand. Each table sits between
'%% BEGIN GENERATED <name>' and '%% END GENERATED <name>' in paper/main.tex. The results that the paper does not
tabulate are in the result files and their summaries (results/summary_*.md), which are part of the archive;
results/findings.md maps every number of the paper to its file.

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
    start, end = f"%% BEGIN GENERATED {name}", f"%% END GENERATED {name}"
    if start not in s:
        raise KeyError(f"no block {name} in {path.name}")
    i, j = s.index(start), s.index(end)
    k = s.index("\n", i) + 1
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
    """A guard band on its 0.25-floor grid: quarters keep two decimals; 'none' when no band qualifies."""
    if x is None or not np.isfinite(x):
        return "none"
    if abs(x) < 1e-6:
        return "0"
    q = round(4 * x) % 4
    return f"{x:.2f}" if q in (1, 3) else (f"{x:.1f}" if x < 10 else f"{x:.0f}")


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
                      r"$\sigma_\mathrm{w}$ and the drift ratio are in the archived results.")


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
    for m in MAIN_RULES:
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
                      r"interpolated, 84 extrapolated; a new family in the produced family's floor (in its own floor in "
                      r"the archived results). Interval: 95\,\% over 1000 resamples of the held-out alternatives, fits fixed. "
                      r"Trial: the first $n$ parts of the design's own run, a within-run lower bound. $^\dagger$, "
                      r"$^\ddagger$: added after the first results and for this version.")


def t_guards() -> str:
    oos = read("qual_guard_oos.csv")
    rels = [("sibling", "Sibling"), ("interpolation", "Interpolated"), ("extrapolation", "Extrapolated")]
    rows = []
    for m in ["NN", "M1sn", "M2", "M5", "M7n", "NN+RM"]:
        cells = []
        for rel, _ in rels:
            ref = oos[(oos["prior"] == "reference (+-20)") & (oos["relation"] == rel) & (oos["method"] == m)
                      & (oos["scheme"] == "LOAO within family")]
            rel5 = oos[(oos["prior"] == "release-like (+-5)") & (oos["relation"] == rel) & (oos["method"] == m)
                       & (oos["scheme"] == "LOAO within family")]
            if ref.empty:
                cells += ["--"] * 4
                continue
            a, b = ref.iloc[0], rel5.iloc[0]
            cells += [band(a["in_sample_band"]), band(b["in_sample_band"]),
                      pct(a["share_correct"]) if np.isfinite(a["in_sample_band"]) else "--",
                      pct(a["in_sample_trial"])]
        rows.append(f"{SHORT[m]}{MARK.get(m, '')} & " + " & ".join(cells))
    head = (" & " + " & ".join(rf"\multicolumn{{4}}{{c}}{{{lab}}}" for _, lab in rels) + r" \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}" "\n"
            "Rule" + r" & $g$ & $g_5$ & OOS & T" * len(rels))
    return table(rows, "Guard bands of step 6 (floors), their out-of-sample share correct and the trial rate",
                 "tab:guards", "l" + "r" * 12, head, colsep="2.2pt", full=True,
                 note=r"$g$, $g_5$: guard band under the reference prior and under the release-like prior (requirements "
                      r"within $\pm5$ floors); none: no band up to 20 floors reaches 95\,\%. OOS: share correct (\%) "
                      r"among decided verdicts with the band estimated leaving each alternative out within its family. "
                      r"T: share of verdicts sent to trial (\%), reference prior. No rule qualifies for a new family; "
                      r"bands per family, out of sample and under other priors are in the archived results.")


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
                      r"extrapolated; units through the pooled floor of the characteristic; a new family in the "
                      r"produced family's floor. $P_\mathrm{pk}$: median performance index of a requirement at the "
                      r"decisive distance of NN with a sibling. All rules and the safe distances are in the archived results.")


MAIN_TABLES = {"floors": t_floors, "qcs": t_qcs, "distances": t_distances, "groups": t_groups, "guards": t_guards}


def main() -> None:
    text = MAIN.read_text()
    for name, fn in MAIN_TABLES.items():
        if f"%% BEGIN GENERATED {name}" not in text:
            print(f"{name}: no block in {MAIN.name}, skipped")
            continue
        write_block(MAIN, name, fn())
        print(f"{MAIN.name} {name}: written")


if __name__ == "__main__":
    main()
