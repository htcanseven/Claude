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
RULES = ["M0", "M0w", "M1", "M1s", "Mc", "M2", "M3", "M5", "M1n", "NN", "M2n", "M4", "M5n"]
CORE = ["M0", "M1", "M1s", "M2", "M5", "M5n", "NN"]
POINT = {"M0", "M1", "M1s", "Mc", "M1n", "NN"}
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
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of batch centres; interval from "
                      r"2000 resamples of batches within series. Ratios per geometry (concave/convex): $\sigma_\mathrm{LT}$, "
                      r"median long-term standard deviation of the parts; $\sigma_\mathrm{b}$, standard deviation between "
                      r"batch means corrected for $\sigma_\mathrm{w}^2/50$; $\sigma_\mathrm{w}$, within batches. Drift: floor "
                      r"over the floor of randomly permuted series.")


def t_distances() -> str:
    """All rules and scopes in one table: the seven core rules with bootstrap intervals, then the further rules."""
    r = resolution()
    scopes = ["within", "setting", "setting/interpolation", "setting/extrapolation", "transfer", "pooled",
              "pooled-setting"]
    with_fa = ("within", "setting", "transfer")
    rob = read("rob_decisions.csv")
    m6 = rob[rob["variant"] == "M6 conformalised GP"].set_index("scope")

    def cells(get, m):
        out = []
        for s in scopes:
            x = get(s)
            out.append("--" if x is None else pair(x, m))
            if s in with_fa:
                out.append("--" if x is None else dist(x["safe_failing"]))
        return out

    rows = []
    for m in CORE:
        rows.append(f"{SHORT[m]} & " + " & ".join(cells(lambda s: r.loc[(s, m)] if (s, m) in r.index else None, m)))
        if m in ("M1s", "M5", "M5n", "NN"):
            ci = []
            for s in scopes:
                x = r.loc[(s, m)]
                ci.append(f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}"
                          if s not in ("pooled", "pooled-setting") else "")
                if s in with_fa:
                    ci.append("")
            rows.append(r"\quad interval & " + " & ".join(ci))
    further = [m for m in RULES if m not in CORE]
    for k, m in enumerate(further):
        lead = r"\midrule " if k == 0 else ""
        rows.append(f"{lead}{SHORT[m]} & " + " & ".join(cells(lambda s: r.loc[(s, m)] if (s, m) in r.index else None, m)))
    if len(m6):
        rows.append("M6 & " + " & ".join(cells(lambda s: m6.loc[s] if s in m6.index else None, "M6")))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{4}{c}{New process setting} & "
            r"\multicolumn{2}{c}{New family} & \multicolumn{2}{c}{Pooled} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}" "\n"
            f"Rule & {DD} & FA & {DD} & FA & interpolated & extrapolated & {DD} & FA & variant & setting")
    return table(rows, "Decisive and safe distances (floors) by the relation of the new design to the produced "
                       "evidence", "tab:distances", "l" + "r" * 10, head, colsep="2.2pt",
                 note=r"Over all seven characteristics; one number for rules that always decide. FA: safe distance on "
                      r"the false-accept side (failing alternatives). Interval: bootstrap 95\,\% interval of the decisive "
                      r"distance (fits fixed). 126 cases per relation (42 interpolated, 84 extrapolated); a new family "
                      r"rests on two transfers. Pooled: the other geometry's alternatives added to the calibration set. "
                      r"Below the line, the further rules; M6, the M5 mean with a conformal margin on standardised "
                      r"leave-one-out residuals, appears only in the robustness analysis.")


def t_robust() -> str:
    r = read("rob_decisions.csv").set_index(["variant", "scope", "method"])
    order = [("reference", "Reference"), ("temperature-adjusted", "Temperature-adjusted"),
             ("first 150 parts dropped", "First 150 parts dropped"),
             ("floor between series", "Floor between series"),
             ("floor with batch 25 and quantile 0.95", "Floor: batches of 25"),
             ("floor with batch 100 and quantile 0.95", "Floor: batches of 100"),
             ("floor with batch 50 and quantile 0.90", r"Floor: 90\,\% quantile"),
             ("floor with batch 50 and quantile 0.99", r"Floor: 99\,\% quantile"),
             ("calibration series of 50 parts", "Calibration series of 50"),
             ("calibration series of 100 parts", "Calibration series of 100"),
             ("calibration series of 250 parts", "Calibration series of 250"),
             ("adequacy share 0.90", r"Conformance $p=0.90$"), ("adequacy share 0.99", r"Conformance $p=0.99$"),
             ("interval level 0.80", "Interval level 0.80"), ("interval level 0.95", "Interval level 0.95"),
             ("smoothed simulation", "Response surface"),
             ("GP se_floor", "GP: sampling noise floor"), ("GP no_noise_floor", "GP: no noise floor")]
    cols = [("within", "M1s"), ("within", "M2"), ("within", "M5"), ("within", "NN"), ("setting", "M2"),
            ("setting", "M5"), ("setting", "NN"), ("transfer", "M2"), ("transfer", "M5")]

    def cell(v, scope, m):
        key = (v, scope, m)
        return pair(r.loc[key], m) if key in r.index else ""

    rows = [f"{name} & " + " & ".join(cell(v, s, m) for s, m in cols) for v, name in order
            if any((v, s, m) in r.index for s, m in cols)]
    u = read("panel_q95_unit.csv").set_index(["scope", "method"])
    rows.append(r"Unit: $q_{95}$ reproducibility & " + " & ".join(pair(u.loc[(s, m)], m) if (s, m) in u.index else ""
                                                                for s, m in cols))
    ref = read("rob_refit.csv").set_index(["scope", "method"])

    def ci(scope, m):
        if (scope, m) not in ref.index:
            return ""
        x = ref.loc[(scope, m)]
        return f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}"

    rows.append(r"\midrule Refit bootstrap, $\delta_\mathrm{d}$ & " + " & ".join(ci(s, m) for s, m in cols))
    head = (r" & \multicolumn{4}{c}{New variant} & \multicolumn{3}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-5}\cmidrule(lr){6-8}\cmidrule(lr){9-10}" "\n"
            r"Variant & M1s & M2 & M5 & NN & M2 & M5 & NN & M2 & M5")
    return table(rows, "Decisive/safe distances (floors) under the robustness variants", "tab:robust",
                 "l" + "r" * 9, head, colsep="2.4pt", place="h",
                 note=r"Rules refitted for every variant; empty cells: the variant does not affect the rule. Floor variants "
                      r"and the unit of $q_{95}$ reproducibility (95\,\% quantile of the difference between the $q_{95}$ of "
                      r"two batches of 100 parts) rescale the distances. Calibration series of $n$: the calibration "
                      r"alternatives' $q_{95}$ from their first $n$ parts. Conformance $p$: the decided statistic is the $p$-quantile. "
                      r"Response surface: nominal simulation and envelope from a quadratic fit over thickness and friction. "
                      r"Other kernels and descriptors of the GPs move M5 "
                      r"by at most 0.4 floors. Refit bootstrap: 95\,\% interval when the lubrication patterns of each "
                      r"geometry are resampled and every rule is refitted (200 resamples).")


TABLES = {"floors": t_floors, "distances": t_distances, "robust": t_robust}


def main() -> None:
    text = MAIN.read_text()
    for name, fn in TABLES.items():
        if f"%% BEGIN GENERATED {name}" not in text:
            sys.exit(f"{name}: no block in {MAIN.name}")
        write_block(name, fn())
        print(f"{name}: written")


if __name__ == "__main__":
    main()
