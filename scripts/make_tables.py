"""Write the data tables of the manuscript from the result CSVs.

Every number in a table comes from a CSV in results/; nothing is typed by hand. Each table sits between
'%% BEGIN GENERATED <name>' and '%% END GENERATED <name>' in paper/main.tex. The results that the paper does not
tabulate are in the result files and their summaries (results/summary_*.md), which are part of the archive.

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
CORE = ["M0", "M1", "M1s", "M2", "M5", "M5n", "NN"]
FURTHER = ["M0w", "Mc", "M3", "M4", "M1n", "M1sn", "M2n"]          # the order of Table 2
RULES = CORE + FURTHER
POINT = {"M0", "M1", "M1s", "Mc", "M1n", "M1sn", "NN"}
SHORT = {r: r for r in RULES} | {"M4": "M3n", "M6": "M6"}
DD = r"$\delta_\mathrm{d}/\delta_\mathrm{s}$"


# ── writing ───────────────────────────────────────────────────────────────────
def write_block(name: str, body: str) -> None:
    s = MAIN.read_text()
    start, end = f"%% BEGIN GENERATED {name}", f"%% END GENERATED {name}"
    if start not in s:
        raise KeyError(f"no block {name}")
    i, j = s.index(start), s.index(end)
    k = s.index("\n", i) + 1
    MAIN.write_text(s[:k] + body.rstrip("\n") + "\n" + s[j:])


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


def dist(x: float) -> str:
    """A distance in floors: two decimals below one (the 0.05 grid), one decimal below 10, whole floors above;
    infinity when a rule never qualifies."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "--"
    if not np.isfinite(x):
        return r"$\infty$"
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


def pair(x, m: str) -> str:
    """decisive/safe; a point rule (always decides) shows one number."""
    return dist(x["resolution_floors"]) if m in POINT else f"{dist(x['resolution_floors'])}/{dist(x['safe_floors'])}"


def table(rows, caption, label, cols, head, colsep=None, note=None, place="t", size=r"\tabsize"):
    sep = f"\\setlength{{\\tabcolsep}}{{{colsep}}}\n" if colsep else ""
    foot = f"\\footnotetext{{{note}}}\n" if note else ""
    body = " \\\\\n".join(r.rstrip().rstrip("\\").rstrip() for r in rows)
    return (f"\\begin{{table}}[{place}]\n{size}\n{sep}\\caption{{{caption.rstrip('.')}}}\\label{{{label}}}\n"
            f"\\begin{{tabular}}{{@{{}}{cols}@{{}}}}\n\\toprule\n{head} \\\\\n\\midrule\n{body} \\\\\n"
            f"\\botrule\n\\end{{tabular}}\n{foot}\\end{{table}}\n")


def read(name: str, **kw) -> pd.DataFrame:
    return pd.read_csv(RESULTS / name, **kw)


def resolution() -> pd.DataFrame:
    r = read("dec_resolution.csv")
    return r[r["qc"] == "all"].set_index(["scope", "method"])


# ── tables ────────────────────────────────────────────────────────────────────
def t_floors() -> str:
    fl = read("alt_floor.csv").set_index("qc")
    dr = read("sens_drift.csv").set_index("qc")
    fp = read("panel_floor_protocol.csv").set_index(["qc", "geometry"])
    geos = ("concave", "convex")
    rows = []
    for c in SHARED:
        f = fl.loc[c]
        per_geo = [sig(f[f"floor_{g}"]) for g in geos]
        lt = "/".join(f"{fp.loc[(c, g), 'floor_over_sigma_lt']:.1f}" for g in geos)
        sb = "/".join(f"{fp.loc[(c, g), 'sigma_between_batch'] / fp.loc[(c, g), 'floor']:.2f}" for g in geos)
        sw = "/".join(f"{fp.loc[(c, g), 'sigma_within_batch'] / fp.loc[(c, g), 'floor']:.2f}" for g in geos)
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & {sig(f['floor'])} & {sig(f['floor_lo'])}--{sig(f['floor_hi'])} & "
                    f"{per_geo[0]} & {per_geo[1]} & {lt} & {sb} & {sw} & {dr.loc[c, 'drift_inflation']:.1f}")
    head = (r"Characteristic & $F$ & 95\,\% interval & Concave & Convex & $F/\sigma_\mathrm{LT}$ & "
            r"$\sigma_\mathrm{b}/F$ & $\sigma_\mathrm{w}/F$ & Drift")
    return table(rows, "Production floor per characteristic, pooled and per geometry, with its components",
                 "tab:floors", "lrrrrrrrr", head, colsep="2.0pt",
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of their 10\,\% trimmed "
                      r"means; interval from 2000 resamples of batches within series. Ratios per geometry (concave/convex), "
                      r"classical statistics pooled over the series as root mean squares: $\sigma_\mathrm{LT}$, standard "
                      r"deviation of the parts of a series; $\sigma_\mathrm{b}$, between batch means, corrected for "
                      r"$\sigma_\mathrm{w}^2/50$; $\sigma_\mathrm{w}$, within batches. Drift: floor over the floor of "
                      r"randomly permuted series.")


def t_distances() -> str:
    """All rules and scopes in one table: the seven core rules with bootstrap intervals, then the further rules."""
    r = resolution()
    scopes = ["within", "setting", "setting/interpolation", "setting/extrapolation", "transfer", "pooled",
              "pooled-setting"]
    with_fa = ("within", "setting", "transfer")
    rob = read("rob_decisions.csv")
    m6 = rob[rob["variant"] == "M6 conformalised GP"].set_index("scope")
    src = read("panel_source_floor.csv")
    src = src[(src["floor"] == "source family") & (src["qc"] == "all")].set_index("method")   # produced family's floor

    def get(s, m):
        if s == "transfer":
            return src.loc[m] if m in src.index else None
        if m == "M6":
            return m6.loc[s] if s in m6.index else None
        return r.loc[(s, m)] if (s, m) in r.index else None

    def cells(m):
        out = []
        for s in scopes:
            x = get(s, m)
            out.append("--" if x is None else pair(x, m))
            if s in with_fa:
                out.append("--" if x is None else dist(x["safe_failing"]))
        return out

    def interval(m):
        """Bootstrap intervals of the decisive distance and, for a new family and the rules with an interval,
        of the safe distance."""
        ci = []
        for s in scopes:
            x = get(s, m)
            cell = "" if s in ("pooled", "pooled-setting") else f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}"
            if s == "transfer" and m not in POINT:
                cell += f"/{dist(x['safe_lo'])}--{dist(x['safe_hi'])}"
            ci.append(cell)
            if s in with_fa:
                ci.append("")
        return r"\quad interval & " + " & ".join(ci)

    rows = []
    for m in CORE:
        rows.append(f"{SHORT[m]} & " + " & ".join(cells(m)))
        if m in ("M1s", "M2", "M5", "M5n", "NN"):
            rows.append(interval(m))
    for k, m in enumerate(FURTHER + ["M6"]):
        lead = r"\midrule " if k == 0 else ""
        rows.append(f"{lead}{SHORT[m]} & " + " & ".join(cells(m)))
        if m == "M3":
            rows.append(interval(m))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{4}{c}{New process setting} & "
            r"\multicolumn{2}{c}{New family} & \multicolumn{2}{c}{Pooled} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}" "\n"
            f"Rule & {DD} & FA & {DD} & FA & interp. & extrap. & {DD} & FA & variant & setting")
    return table(rows, "Decisive and safe distances (floors) by the relation of the new design to the produced "
                       "evidence", "tab:distances", "l" + "r" * 10, head, colsep="1.9pt",
                 note=r"Over all seven characteristics; one number for rules that always decide. FA: safe distance on "
                      r"the false-accept side (failing alternatives). Interval: bootstrap 95\,\% interval of the decisive "
                      r"distance and, for a new family, of the safe distance (fits fixed). 126 cases per relation (42 "
                      r"interpolated, interp.; 84 extrapolated, extrap.); a new family rests on two transfers and is scored in the floor of "
                      r"the produced family (Section~\ref{sec:floor}). Pooled: the other geometry's alternatives added to "
                      r"the calibration set. Below the line, the further rules (M1sn: the force trend, the counterpart of "
                      r"M1s without the simulation) and, as a robustness variant, M6 (the M5 mean with a conformal margin "
                      r"on standardised leave-one-out residuals).")


def t_robust() -> str:
    r = read("rob_decisions.csv").set_index(["variant", "scope", "method"])
    order = [("reference", "Reference"), ("temperature-adjusted", "Temperature-adjusted"),
             ("first 150 parts dropped", "Warm-up dropped"),
             ("floor between series", "Floor between series"),
             ("floor with batch 25 and quantile 0.95", "Floor: batches of 25"),
             ("floor with batch 100 and quantile 0.95", "Floor: batches of 100"),
             ("floor with batch 50 and quantile 0.90", r"Floor: 90\,\% quantile"),
             ("floor with batch 50 and quantile 0.99", r"Floor: 99\,\% quantile"),
             ("calibration series of 50 parts", "Calibration: 50 parts"),
             ("calibration series of 250 parts", "Calibration: 250 parts"),
             ("adequacy share 0.90", r"Conformance $p=0.90$"), ("adequacy share 0.99", r"Conformance $p=0.99$"),
             ("interval level 0.80", "Interval level 0.80"), ("interval level 0.95", "Interval level 0.95"),
             ("smoothed simulation", "Response surface"), ("GP se_floor", "GP: sampling bound")]
    cols = [("within", "M1s"), ("within", "M2"), ("within", "M5"), ("within", "NN"), ("setting", "M2"),
            ("setting", "M5"), ("setting", "NN"), ("setting", "M1sn"), ("transfer", "M2"), ("transfer", "M5")]

    def cell(v, scope, m):
        key = (v, scope, m)
        return pair(r.loc[key], m) if key in r.index else ""

    rows = [f"{name} & " + " & ".join(cell(v, s, m) for s, m in cols) for v, name in order
            if any((v, s, m) in r.index for s, m in cols)]
    u = read("panel_q95_unit.csv").set_index(["scope", "method"])
    rows.append(r"Unit: $q_{95}$ floor & " + " & ".join(pair(u.loc[(s, m)], m) if (s, m) in u.index else ""
                                                                for s, m in cols))
    ref = read("rob_refit.csv").set_index(["scope", "method"])

    def ci(scope, m):
        if (scope, m) not in ref.index:
            return ""
        x = ref.loc[(scope, m)]
        return f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}"

    rows.append(r"\midrule Refit, $\delta_\mathrm{d}$ & " + " & ".join(ci(s, m) for s, m in cols))
    head = (r" & \multicolumn{4}{c}{New variant} & \multicolumn{4}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-11}" "\n"
            r"Variant & M1s & M2 & M5 & NN & M2 & M5 & NN & M1sn & M2 & M5")
    return table(rows, "Decisive/safe distances (floors) under the robustness variants", "tab:robust",
                 "l" + "r" * 10, head, colsep="1.6pt", place="!ht",
                 note=r"Rules refitted for every variant; empty cells: the variant does not affect the rule; a new family in "
                      r"its own floor. The floor between series contains the lubrication effect and, for a new variant, the "
                      r"series that NN averages. Warm-up: first 150 parts. Calibration: calibration $q_{95}$ from the first $n$ "
                      r"parts, truths and floors from the full series. Response surface: simulations from a quadratic fit over thickness and "
                      r"friction; other GP kernels and descriptors move M5 by at most 0.4 floors. Unit: the $q_{95}$ "
                      r"floor, 95\,\% quantile of the difference between the $q_{95}$ of two batches of 100 parts. "
                      r"Refit: 95\,\% interval of the decisive distance over 200 draws of each geometry's lubrication patterns with "
                      r"replacement, every rule refitted (Section~\ref{sec:evaldesign}).")



STEP6_RULES = ["M1", "M1s", "M2", "M5", "M5n", "NN", "M3", "M4", "M1sn"]
RELATIONS = [("within", "Sibling produced"), ("setting/interpolation", "Interpolated setting"),
             ("setting/extrapolation", "Extrapolated setting")]


def t_step6() -> str:
    """The procedure's decision rule (step 6) by relation: guard band, distances and trial shares."""
    s6 = read("panel_step6.csv").set_index(["scope", "method"])
    rows = []
    for m in STEP6_RULES:
        cells = []
        for scope, _ in RELATIONS:
            x = s6.loc[(scope, m)]
            if not np.isfinite(x["guard_band"]):
                cells += ["none", "--", "100", "100"]
                continue
            cells += [band(x["guard_band"]), f"{dist(x['decisive_step6'])}/{dist(x['safe_step6'])}",
                      pct(x["trial_10_step6"]), pct(x["trial_20_step6"])]
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (" & " + " & ".join(rf"\multicolumn{{4}}{{c}}{{{lab}}}" for _, lab in RELATIONS) + r" \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}" "\n"
            "Rule" + rf" & $g$ & {DD} & $T_{{10}}$ & $T_{{20}}$" * len(RELATIONS))
    return table(rows, "The procedure's decision rule (step 6) by relation: guard band, distances and trial shares",
                 "tab:step6", "l" + "r" * 12, head, colsep="2.2pt", place="!ht",
                 note=r"$g$: guard band (floors) under the reference prior (Section~\ref{sec:procedure}); "
                      r"$\delta_\mathrm{d}/\delta_\mathrm{s}$: distances of the rule with its interval widened by $g$; "
                      r"$T_{10}$, $T_{20}$: share of verdicts sent to trial (\%) at requirements 10 and 20 floors from the "
                      r"truth. None: no band up to 20 floors reaches 95\,\%, so the procedure sends every design to trial; "
                      r"so also M0 and M0w in every relation, Mc with a sibling and for an extrapolated setting (for an "
                      r"interpolated one $g=18$), and every rule for a new family, scored in the produced family's floor.")


def t_intervals() -> str:
    """Coverage, half-width and centre of the interval rules by relation; a new family in the produced
    family's floor (computed here from the stored intervals with decisions.coverage)."""
    import decisions as D

    cov = read("dec_coverage.csv").set_index(["scope", "method"])
    iv = read("dec_intervals.csv")
    floors = D.load_floors()
    other = {"concave": "convex", "convex": "concave"}
    tr = iv[iv["scope"] == "transfer"]
    tr = tr.assign(floor=[floors[(q, other[g])] for q, g in zip(tr["qc"], tr["geometry"])])
    src = D.coverage(tr).set_index(["scope", "method"])
    rels = RELATIONS + [("transfer", "New family")]
    rows = []
    for m in ["M2", "M2n", "M3", "M4", "M5", "M5n"]:
        cells = []
        for scope, _ in rels:
            x = (src if scope == "transfer" else cov).loc[(scope, m)]
            cells += [pct(x["coverage"]), dist(x["half_width_floors"]), dist(x["centre_decisive"])]
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (" & " + " & ".join(rf"\multicolumn{{3}}{{c}}{{{lab}}}" for _, lab in rels) + r" \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}\cmidrule(lr){11-13}" "\n"
            "Rule" + r" & Cov & HW & Ctr" * len(rels))
    gp = read("dec_gp.csv").set_index(["scope", "method"])
    bound = [gp.loc[("within", m), "noise_at_bound"] for m in ("M5", "M5n")]
    return table(rows, "Interval rules by relation: coverage, half-width and the interval centre as a point rule",
                 "tab:intervals", "l" + "r" * 12, head, colsep="2.6pt", place="!ht",
                 note=rf"Cov: share of cases whose true $q_{{95}}$ lies in the interval (\%; nominal 90). HW: median "
                      rf"half-width (floors). Ctr: decisive distance of the interval centre used as a point rule (floors). "
                      rf"A new family in the floor of the produced family. The GP noise variance sits at its lower bound in "
                      rf"{pct(bound[0])} and {pct(bound[1])}\,\% of the M5 and M5n fits with a sibling and in every other fit.")

TABLES = {"floors": t_floors, "distances": t_distances, "robust": t_robust, "step6": t_step6,
          "intervals": t_intervals}


def main() -> None:
    text = MAIN.read_text()
    for name, fn in TABLES.items():
        if f"%% BEGIN GENERATED {name}" not in text:
            sys.exit(f"{name}: no block in {MAIN.name}")
        write_block(name, fn())
        print(f"{name}: written")


if __name__ == "__main__":
    main()
