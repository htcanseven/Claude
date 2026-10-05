"""Write the data tables of the manuscript and of its Electronic Supplementary Material from the result CSVs.

Every number in a table comes from a CSV in results/; nothing is typed by hand. Each table sits between
'%% BEGIN GENERATED <name>' and '%% END GENERATED <name>' in paper/main.tex or paper/esm.tex. The ESM tables are
numbered S1, S2, ... in the order of their blocks in esm.tex; that order is written to paper/esm_labels.tex, which
main.tex reads, so that the text cites ESM tables by name (\\esm{<name>}).

Usage: python scripts/make_tables.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS, ROOT  # noqa: E402
from qc import SHARED  # noqa: E402

MAIN = ROOT / "paper" / "main.tex"
ESM = ROOT / "paper" / "esm.tex"
LABELS = ROOT / "paper" / "esm_labels.tex"
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
    for path in (MAIN, ESM):
        s = path.read_text()
        start, end = f"%% BEGIN GENERATED {name}", f"%% END GENERATED {name}"
        if start in s:
            i, j = s.index(start), s.index(end)
            k = s.index("\n", i) + 1
            path.write_text(s[:k] + body.rstrip("\n") + "\n" + s[j:])
            return
    raise KeyError(f"no block {name}")


def esm_labels() -> None:
    names = re.findall(r"%% BEGIN GENERATED (\S+)", ESM.read_text())
    lines = [f"\\expandafter\\def\\csname esm@{n}\\endcsname{{S{i}}}" for i, n in enumerate(names, 1)]
    lines.append(f"\\expandafter\\def\\csname esm@last\\endcsname{{S{len(names)}}}")
    LABELS.write_text("%% Written by scripts/make_tables.py: numbers of the ESM tables, by block name.\n"
                      + "\n".join(lines) + "\n")


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
    return "--" if x is None or not np.isfinite(x) else f"{100 * x:.0f}"


def signed(x: float, d: int = 1, plus: bool = True) -> str:
    """A number with a typographic minus, halves rounded away from zero; a zero carries no sign."""
    if x is None or not np.isfinite(x):
        return "--"
    s = f"{x + np.sign(x) * 1e-9:{'+' if plus else ''}.{d}f}"
    if float(s) == 0:
        s = f"{0:.{d}f}"
    return s.replace("-", "$-$")


def rng(lo: float, hi: float, d: int = 2) -> str:
    """A range; written with 'to' when an end is negative, so that the dash cannot read as a minus."""
    a, b = signed(lo, d, plus=False), signed(hi, d, plus=False)
    return f"{a} to {b}" if "$-$" in a + b else f"{a}--{b}"


def dist(x: float) -> str:
    """A distance in floors: one decimal below 10, whole floors above; infinity when a rule never qualifies."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "--"
    if not np.isfinite(x):
        return r"$\infty$"
    x = x + 1e-9                                  # distances lie on a 0.05 grid: round halves up
    return f"{x:.1f}" if x < 10 else f"{x:.0f}"


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


# ── main text ─────────────────────────────────────────────────────────────────
def t_floors() -> str:
    fl = read("alt_floor.csv").set_index("qc")
    dr = read("sens_drift.csv").set_index("qc")
    fp = read("panel_floor_protocol.csv").set_index(["qc", "geometry"])
    st = read("panel_resolution_steps.csv").set_index("qc")
    rows = []
    for c in SHARED:
        f = fl.loc[c]
        ratio = "/".join(f"{fp.loc[(c, g), 'floor_over_sigma_lt']:.1f}" for g in ("concave", "convex"))
        step = st.loc[c, "step_over_floor"]
        step = f"{step:.2f}" if step >= 0.01 else "${<}$0.01"
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & {sig(f['floor'])} & {sig(f['floor_lo'])}--{sig(f['floor_hi'])} & "
                    f"{sig(f['floor_lo_alt'])}--{sig(f['floor_hi_alt'])} & {sig(f['floor_concave'])} & "
                    f"{sig(f['floor_convex'])} & {ratio} & {dr.loc[c, 'drift_inflation']:.1f} & {step}")
    head = (r" & & \multicolumn{2}{c}{95\,\% interval} & & & & & \\" "\n" r"\cmidrule(lr){3-4}" "\n"
            r"Characteristic & $F$ & batches & series & Concave & Convex & $F/\sigma_\mathrm{LT}$ & Drift & Step")
    return table(rows, "Production floor per characteristic, pooled and per geometry", "tab:floors",
                 "lrrrrrrrr", head, colsep="1.8pt",
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of batch centres. Intervals: "
                      r"2000 resamples of batches within series, and of whole series. $F/\sigma_\mathrm{LT}$: "
                      r"floor over the median long-term standard deviation of the parts (concave/convex). Drift: floor "
                      r"over the floor of randomly permuted series. Step: measurement resolution in floors.")


def t_distances() -> str:
    r = resolution()
    scopes = ["within", "setting", "setting/interpolation", "setting/extrapolation", "transfer"]
    rows = []
    for m in CORE:
        cells = []
        for s in scopes:
            x = r.loc[(s, m)]
            cells.append(pair(x, m))
            if s in ("within", "setting", "transfer"):
                cells.append(dist(x["safe_failing"]))
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
        if m in ("M1s", "M5", "M5n", "NN"):
            ci = []
            for s in scopes:
                x = r.loc[(s, m)]
                ci.append(f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}")
                if s in ("within", "setting", "transfer"):
                    ci.append("")
            rows.append(r"\quad interval & " + " & ".join(ci))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{4}{c}{New process setting} & "
            r"\multicolumn{2}{c}{New family} \\" "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-7}\cmidrule(lr){8-9}" "\n"
            f"Rule & {DD} & FA & {DD} & FA & interpolated & extrapolated & {DD} & FA")
    return table(rows, "Decisive and safe distances (floors) by the relation of the new design to the produced "
                       "evidence", "tab:distances", "lrrrrrrrr", head, colsep="3pt",
                 note=r"Over all seven characteristics; one number for rules that always decide. FA: safe distance on "
                      r"the false-accept side (failing alternatives). Interval: bootstrap 95\,\% interval of the decisive "
                      r"distance (fits fixed). 126 cases per relation (42 interpolated, 84 extrapolated); a new family "
                      r"rests on two transfers. All rules: ESM Table~\esm{alldist}.")


def t_drivers() -> str:
    st = read("panel_sibling_strata.csv").set_index(["resolved_siblings", "method"])
    fl = read("panel_force_levels.csv").set_index(["bhf_kN", "method"])
    r = resolution()
    rules = ["NN", "M1s", "M2", "M5", "M5n"]
    n_strata = st.reset_index().drop_duplicates("resolved_siblings").set_index("resolved_siblings")["cases"]
    rows = [r"\multicolumn{6}{@{}l}{\emph{New variant, siblings resolvably different}}"]
    for k, name in ((0, "neither"), (1, "one"), (2, "both")):
        rows.append(f"{name} ({int(n_strata.loc[k])}) & " + " & ".join(pair(st.loc[(k, m)], m) for m in rules))
    rows.append(r"\multicolumn{6}{@{}l}{\emph{New process setting, held-out force}}")
    for b, name in ((100, "100\\,kN, slower stroke"), (300, "300\\,kN, interpolated"), (500, "500\\,kN")):
        rows.append(f"{name} ({int(fl.loc[(b, 'NN'), 'cases'])}) & " + " & ".join(pair(fl.loc[(b, m)], m) for m in rules))
    rows.append(r"\multicolumn{6}{@{}l}{\emph{Other family's alternatives added to the calibration}}")
    for s, name in (("pooled", "new variant"), ("pooled-setting", "new process setting")):
        rows.append(f"{name} (126) & " + " & ".join(pair(r.loc[(s, m)], m) for m in rules))
    head = "Cases & " + " & ".join(SHORT[m] for m in rules)
    return table(rows, "Where the distances come from: decisive/safe distances (floors) of subsets and variants of "
                       "the cases", "tab:drivers", "lrrrrr", head, colsep="5pt",
                 note=r"Siblings resolvably different: effect-to-scatter ratio of at least one between the held-out "
                      r"alternative and its sibling. Pooled: the alternatives of the other geometry are added to the "
                      r"calibration set (Section~\ref{M-sec:evaldesign}).")


def t_design() -> str:
    d = read("budget_design.csv").set_index(["relation", "method", "k"])
    ks = [1, 2, 4, 6]
    rows = []
    for rel in ("sibling", "interpolation", "extrapolation"):
        for m in ["M1", "M2", "M5", "NN"]:
            cells = []
            for k in ks:
                if (rel, m, k) not in d.index:
                    cells.append("-- & --")
                    continue
                x = d.loc[(rel, m, k)]
                cells.append(f"{pair(x, m)} & {pct(x['error_at_10'])}")
            rows.append(f"{rel} & {m} & " + " & ".join(cells))
    head = ("Relation & Rule & " + " & ".join(f"\\multicolumn{{2}}{{c}}{{$k={k}$}}" for k in ks) + r" \\" "\n"
            + "".join(f"\\cmidrule(lr){{{3 + 2 * i}-{4 + 2 * i}}}" for i in range(len(ks))) + "\n"
            + " & & " + " & ".join([f"{DD} & wrong"] * len(ks)))
    return table(rows, "Calibration budget: distances and wrong verdicts at 10 floors by the relation of the new design "
                       "to the produced alternatives", "tab:design", "llrrrrrrrr", head, colsep="3pt",
                 note=r"All subsets of $k$ produced alternatives of the family. Sibling: the subset holds an alternative "
                      r"at the new design's force; interpolation: no sibling, forces on both sides; extrapolation: no "
                      r"sibling, the new force outside. Wrong: share of wrong verdicts at $|d|=10$ (\%). M5 from $k=2$.")


# ── ESM ───────────────────────────────────────────────────────────────────────
QC_DEFINITIONS = [
    ("drawin_mid", "process indicator", r"$(210 - W_x)/2$; $W_x$: flange width across the cup centre, across the scan lines"),
    ("drawin_corner", "process indicator", r"$(2\sqrt{2}\cdot 210 - L_1 - L_2)/4$; $L$: distance between opposite corner tips "
                                           r"of the flange"),
    ("waviness", "process indicator", "robust standard deviation of the flange about a fitted quadratic surface"),
    ("wall_op10", "drawing", r"inclination of the wall from the punch axis between 10 and 20\,mm depth, mean of the east "
                             r"and west walls (design angle 20$^\circ$ concave, 10$^\circ$ convex)"),
    ("arm_op20", "drawing", "inclination of the flat segment of the cut arms, mean of four arms (requirement on its "
                            "absolute value)"),
    ("depth_op10", "drawing", "median depth of the flange below the plane of the cup bottom after drawing"),
    ("dome_op20", "drawing", r"sag of the bottom at 40\,mm radius from a fitted paraboloid (requirement on its absolute "
                             r"value)"),
]


def t_qcs() -> str:
    rows = [f"{LABEL[c]} & {UNIT[c]} & {role} & {text}" for c, role, text in QC_DEFINITIONS]
    return table(rows, "Quality characteristics, extracted with the same definitions from the scans and the simulated "
                       "nodes", "tab:qcs", "L{2.5cm}L{0.6cm}L{1.6cm}L{7.0cm}",
                 "Characteristic & Unit & Role & Definition", colsep="4pt", place="h",
                 note="All depths are referred to the plane of the cup bottom; definitions of the extraction in "
                      "Section~S1.")

def t_components() -> str:
    m = read("meas_floor.csv").set_index("qc")
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
                 "lrrrrrr", head, colsep="4.5pt", place="h",
                 note=r"$\sigma_\mathrm{ST}$: standard deviation within subgroups of five consecutive parts; "
                      r"$\sigma_\mathrm{LT}$: of the whole series (medians). White share: the floor that independent "
                      r"part-to-part noise alone would produce, $1.96\sqrt{2/B}$ times the successive-difference standard "
                      r"deviation, over $F$; it bounds the share a scanner's repeatability can explain. First half: floor "
                      r"of the first 250 parts. $q_{95}$ floor: 95\,\% quantile of the difference between the 95th "
                      r"percentiles of two batches of 100 parts. Between series: difference between the centres of the "
                      r"three lubrication series of one geometry and force.")


def t_protocol() -> str:
    p = read("panel_floor_protocol.csv")
    rows = []
    for c in SHARED:
        for g in ("concave", "convex"):
            x = p[(p["qc"] == c) & (p["geometry"] == g)].iloc[0]
            rows.append(f"{LABEL[c] if g == 'concave' else ''} & {g} & {sig(x['floor'])} & {sig(x['sigma_lt'])} & "
                        f"{sig(x['sigma_st'])} & {sig(x['sigma_within_batch'])} & {sig(x['sigma_between_batch'])} & "
                        f"{x['floor_over_sigma_lt']:.2f} & {x['floor_over_sigma_st']:.2f} & {sig(x['normal_model_floor'])}")
    head = (r"Characteristic & Geometry & $F$ & $\sigma_\mathrm{LT}$ & $\sigma_\mathrm{ST}$ & $\sigma_\mathrm{w}$ & "
            r"$\sigma_\mathrm{b}$ & $F/\sigma_\mathrm{LT}$ & $F/\sigma_\mathrm{ST}$ & model $F$")
    return table(rows, "Floor protocol: variance components and the floor in units of the part scatter",
                 "tab:protocol", "llrrrrrrrr", head, colsep="3pt", place="h",
                 note=r"Units of the characteristic. $\sigma_\mathrm{w}$: pooled standard deviation within batches of 50; "
                      r"$\sigma_\mathrm{b}$: between batch means, corrected for $\sigma_\mathrm{w}^2/50$; model $F$: "
                      r"$1.96\sqrt{2}\sqrt{\sigma_\mathrm{b}^2+\sigma_\mathrm{w}^2/50}$. Medians over the nine series.")


def t_lags() -> str:
    v = read("panel_variogram.csv")
    w = v.groupby(["lag_batches", "qc"])["q95_floors"].mean().unstack()
    rows = [f"{lag} ({50 * lag}) & " + " & ".join(f"{w.loc[lag, c]:.2f}" for c in SHARED) for lag in w.index]
    head = r"Lag (parts) & " + " & ".join(["DM", "DC", "Wav", "Wall", "Arm", "Depth", "Dome"])
    return table(rows, "The floor by the time between the batches compared, in floors", "tab:lags",
                 "lrrrrrrr", head, colsep="5pt", place="h",
                 note=r"95\,\% quantile of the difference between batch centres a given number of batches apart, over "
                      r"the floor (mean of the two geometries). DM, DC: mid-side and corner draw-in; Wav: flange waviness.")


def t_resolve() -> str:
    e = read("alt_effects.csv")
    p = read("rob_bhf_pairs.csv").set_index(["qc", "pair"])

    def mrc(x):
        return r"$>$200" if x > 200 else f"{x:.0f}"

    rows = []
    for c in SHARED:
        g = e[e["qc"] == c]
        cells = []
        for fam in ["geometry", "bhf", "lubrication"]:
            h = g[g["family"] == fam]
            cells.append(f"{int((h['esr'] >= 1).sum())}/{len(h)} & {h['esr'].median():.1f}")
        rows.append(f"{LABEL[c]} & " + " & ".join(cells) +
                    f" & {mrc(p.loc[(c, '100->300'), 'mrc_kN'])} & {mrc(p.loc[(c, '300->500'), 'mrc_kN'])}")
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
                 "tab:resolve", "lrrrrrrrr", head, colsep="3.5pt", place="h",
                 note=r"ESR: effect-to-scatter ratio of two alternatives that differ in one factor. MRC: floor over the "
                      r"local sensitivity of the alternative centres to blank-holder force, between 100 and 300\,kN (the "
                      r"stroke speed also changes) and between 300 and 500\,kN; $>$200: beyond the interval.")


def t_offsets() -> str:
    t = read("dec_alternatives.csv")
    fl = read("alt_floor.csv").set_index("qc")
    t["F"] = [fl.loc[q, f"floor_{g}"] for q, g in zip(t["qc"], t["geometry"])]
    t["off_F"] = (t["real_q95"] - t["sim_nominal"]) / t["F"]
    rows = []
    for c in SHARED:
        g = t[t["qc"] == c]
        cells = []
        for geo in ["concave", "convex"]:
            h = g[g["geometry"] == geo]
            cells.append(f"{signed(h['off_F'].median(), 0, plus=False)} & "
                         f"{signed(h['off_F'].max() - h['off_F'].min(), 0, plus=False)}")
        gm = [g[g["geometry"] == geo]["gap_matched_signed"].median() for geo in ["concave", "convex"]]
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & " + " & ".join(cells) + f" & {signed(gm[0], 2)} & {signed(gm[1], 2)}")
    m0 = read("panel_m0_split.csv")
    head = (r" & \multicolumn{2}{c}{Concave} & \multicolumn{2}{c}{Convex} & \multicolumn{2}{c}{Matched, signed} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Characteristic & Offset & Spread & Offset & Spread & Concave & Convex")
    return table(rows, "Offset between the parts' 95th percentile and the nominal simulation, in floors",
                 "tab:offsets", "lrrrrrr", head, colsep="5pt", place="h",
                 note=r"Offset: median over the nine alternatives of a geometry of $(q_{95}-s_0)/F$, $s_0$ the nominal "
                      r"simulation, on the decision scale; spread: its range. Matched, signed: median difference between "
                      r"the centre of the parts and of their matched simulations, in the unit, with signs. Removing the "
                      f"cup-depth reference offset brings the decisive distance of M0 from {dist(m0['resolution_floors'].iloc[0])} "
                      f"to {dist(m0['resolution_floors'].iloc[1])} floors.")


def t_simnoise() -> str:
    s = read("meas_sim.csv").set_index(["qc", "geometry"])
    sg = read("ds_surrogate.csv").set_index(["qc", "geometry"])
    rows = []
    for c in SHARED:
        cells = []
        for geo in ["concave", "convex"]:
            x = s.loc[(c, geo)]
            cells.append(f"{x['roughness_sd_floors']:.1f} & {x['env_hi_minus_smooth_floors_max']:.1f} & "
                         f"{sg.loc[(c, geo), 'rmse_over_floor']:.1f}")
        rows.append(f"{LABEL[c]} & " + " & ".join(cells))
    head = (r" & \multicolumn{3}{c}{Concave} & \multicolumn{3}{c}{Convex} \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}" "\n"
            r"Characteristic & noise & envelope & surrogate & noise & envelope & surrogate")
    return table(rows, "Extraction noise of the simulated characteristics and accuracy of a surrogate (floors)",
                 "tab:simnoise", "lrrrrrr", head, colsep="4.5pt", place="h",
                 note=r"Noise: standard deviation of the second difference along the friction grid over $\sqrt{1.5}$. "
                      r"Envelope: largest difference between the maximum of the simulated values of a geometry and force "
                      r"and that of a quadratic response surface. Surrogate: leave-one-out error of a Gaussian-process "
                      r"surrogate of the simulations over process conditions.")


def t_scan() -> str:
    s = read("meas_scan.csv")
    quantities = [("sd_wx", r"Flange width $W_x$, SD (mm)", 2), ("sd_wy", r"Flange width $W_y$, SD (mm)", 2),
                  ("r_wx_wy", r"Correlation of $W_x$ and $W_y$", 2), ("wy_minus_wx", r"$W_y-W_x$ (mm)", 1),
                  ("sd_EW_mean", r"Wall angle, mean of E and W, SD ($^\circ$)", 2),
                  ("sd_N", r"Wall angle N, SD ($^\circ$)", 2),
                  ("N_minus_EW", r"Wall angle N minus mean of E and W ($^\circ$)", 1),
                  ("r_E_W", r"Correlation of the E and W wall angles", 2)]
    rows = [f"{name} & " + " & ".join(rng(s.loc[s["geometry"] == g, c].min(), s.loc[s["geometry"] == g, c].max(), d)
                                      for g in ("concave", "convex")) for c, name, d in quantities]
    return table(rows, "Redundancy of the scans: ranges over the nine series of each geometry", "tab:scan",
                 "lrr", r"Quantity & Concave & Convex", colsep="6pt", place="h",
                 note=r"$W_x$, $W_y$: flange width across the cup centre, across and along the scan lines; E, W, N: east, "
                      r"west and north walls; SD and correlation over the parts of a series.")


def t_resolution() -> str:
    r = read("panel_resolution_steps.csv").set_index("qc")
    rows = []
    for c in SHARED:
        x = r.loc[c]
        rows.append(f"{LABEL[c]} & {sig(x['median_step'], 2) if x['median_step'] > 0 else '0'} & "
                    f"{x['step_over_floor']:.3f} & {int(x['distinct_per_series_median'])} "
                    f"({int(x['distinct_per_series_min'])}--{int(x['distinct_per_series_max'])}) & "
                    f"{int(x['alternatives_with_zero_q95_se'])}")
    head = r"Characteristic & Step (unit) & Step/$F$ & Distinct values per series & Zero SE of $q_{95}$"
    return table(rows, "Measurement resolution of the characteristics", "tab:resolution", "lrrrr", head,
                 colsep="6pt", place="h",
                 note=r"Step: median difference between adjacent distinct values within a series. Zero SE: alternatives "
                      r"whose block-bootstrap standard error of $q_{95}$ is zero (the quantile does not move).")


def t_runs() -> str:
    r = read("panel_runs.csv")
    rows = [" & ".join(a.split("/")) + f" & {x:.1f} & {y:.1f} & {z:.1f} & {s / 1000:.3f} & {v:.0f}"
            for a, x, y, z, s, v in zip(r["alternative"], r["start_temp_C"], r["rise_first_150_K"], r["rise_series_K"],
                                        r["sheet_median_um"], r["stroke_speed_mm_s"])]
    head = (r" & & & \multicolumn{3}{c}{Punch temperature} & & \\" "\n" r"\cmidrule(lr){4-6}" "\n"
            r"Geometry & Force (kN) & Oiling & start ($^\circ$C) & rise, 150 (K) & rise, all (K) & Sheet (mm) & "
            r"Speed (mm/s)")
    return table(rows, "Run metadata of the 18 series", "tab:runs", "llrrrrrr", head, colsep="2.8pt", place="h",
                 note=r"Punch temperature at the start (median of the first ten parts) and its rise over the first 150 "
                      r"parts and over the series; median sheet "
                      r"thickness; median forming speed. The order and dates of the series are not documented.")


def t_weights() -> str:
    w = read("panel_failing_weight.csv")
    rows = [f"{d:g} & {int(f)} of {int(n)} & {x:.2f}" for d, f, n, x in
            zip(w["delta"], w["feasible_failing"], w["cases"], w["weight_failing"])]
    return table(rows, "Weight of the failing side at given distances", "tab:weights", "rrr",
                 r"$\delta$ (floors) & Feasible failing requirements & Weight of the failing side", colsep="8pt",
                 place="h", note=r"A requirement $q_{95}-\delta F$ below zero is no requirement for a non-negative "
                                 r"characteristic; every feasible verdict has equal weight (Section~\ref{M-sec:distances} of the paper).")


def t_alldist() -> str:
    r = resolution()
    scopes = ["within", "setting", "setting/interpolation", "setting/extrapolation", "transfer", "pooled",
              "pooled-setting"]
    rows = [f"{SHORT[m]} & " + " & ".join(pair(r.loc[(s, m)], m) if (s, m) in r.index else "--" for s in scopes)
            for m in RULES]
    rob = read("rob_decisions.csv")
    m6 = rob[rob["variant"] == "M6 conformalised GP"].set_index("scope")
    if len(m6):
        rows.append("M6 & " + " & ".join(f"{dist(m6.loc[s, 'resolution_floors'])}/{dist(m6.loc[s, 'safe_floors'])}"
                                         if s in m6.index else "--" for s in scopes))
    head = (r" & New & \multicolumn{3}{c}{New process setting} & New & \multicolumn{2}{c}{Pooled} \\" "\n"
            r"\cmidrule(lr){3-5}\cmidrule(lr){7-8}" "\n"
            r"Rule & variant & all & interpolated & extrapolated & family & variant & setting")
    return table(rows, "Decisive and safe distances (floors) of all rules and scopes", "tab:alldist", "lrrrrrrr",
                 head, colsep="4pt", place="h",
                 note=r"$\delta_\mathrm{d}/\delta_\mathrm{s}$; one number for rules that always decide. Pooled: the other "
                      r"geometry's alternatives added to the calibration set. M3n is M4 in the code. M6: M5 mean with a "
                      r"conformal margin on standardised leave-one-out residuals.")


def t_distci() -> str:
    r = resolution()
    rows = []
    for m in RULES:
        cells = []
        for s in ["within", "setting", "transfer"]:
            x = r.loc[(s, m)]
            cells.append(f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])} & "
                         f"{dist(x['safe_lo'])}--{dist(x['safe_hi'])}")
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{2}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Rule & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & $\delta_\mathrm{d}$ & $\delta_\mathrm{s}$ & "
            r"$\delta_\mathrm{d}$ & $\delta_\mathrm{s}$")
    return table(rows, r"Bootstrap 95\,\% intervals of the decisive and safe distances (floors)", "tab:distci",
                 "lrrrrrr", head, colsep="4pt", place="h",
                 note=r"1000 resamples of the held-out alternatives within each geometry, each with a block-bootstrap "
                      r"replicate of the true $q_{95}$; the fits are held fixed (refitting: Table~\ref{tab:robust}).")


def t_onesided() -> str:
    r = resolution()
    rows = []
    for m in RULES:
        cells = [f"{dist(r.loc[(s, m), 'safe_failing'])} & {dist(r.loc[(s, m), 'safe_adequate'])}"
                 for s in ["within", "setting", "transfer"]]
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{2}{c}{New setting} & \multicolumn{2}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}" "\n"
            r"Rule & FA side & FR side & FA side & FR side & FA side & FR side")
    return table(rows, "One-sided safe distances (floors): false accepts and false rejects", "tab:onesided",
                 "lrrrrrr", head, colsep="4.5pt", place="h",
                 note=r"FA side: smallest distance beyond which at most 5\,\% of the verdicts on failing alternatives are "
                      r"false accepts; FR side: the same for false rejects of adequate alternatives.")


def t_paired() -> str:
    p = read("dec_paired.csv").set_index(["scope", "rule_a", "rule_b"])
    pairs = [("M5", "M5n"), ("M2", "M2n"), ("M1", "M1n"), ("M1s", "M1n"), ("M1s", "M1"), ("M1s", "NN"), ("M5", "NN"),
             ("M5n", "NN"), ("M2", "NN"), ("M5", "M2"), ("M5", "M4"), ("M3", "M4"), ("Mc", "M1")]
    rows = []
    for a, b in pairs:
        cells = []
        for s in ["within", "setting", "transfer"]:
            if (s, a, b) not in p.index:
                cells.append("--")
                continue
            x = p.loc[(s, a, b)]
            cells.append(f"{signed(x['resolution_diff'])} ({signed(x['resolution_diff_lo'])}, "
                         f"{signed(x['resolution_diff_hi'])})")
        rows.append(f"{SHORT[a]} $-$ {SHORT[b]} & " + " & ".join(cells))
    rp = RESULTS / "rob_refit_paired.csv"
    if rp.exists():
        q = pd.read_csv(rp)
        q = q[q["kind"] == "resolution_floors"].set_index(["scope", "rule_a", "rule_b"])
        rows.append(r"\multicolumn{4}{@{}l}{\emph{Refitting bootstrap (lubrication patterns resampled)}}")
        for a, b in [("NN", "M5"), ("NN", "M5n"), ("M5", "M5n"), ("M2", "M2n"), ("M1s", "NN"), ("M1", "M1n")]:
            cells = []
            for s in ["within", "setting", "transfer"]:
                if (s, a, b) not in q.index:
                    cells.append("--")
                    continue
                x = q.loc[(s, a, b)]
                cells.append(f"{signed(x['diff'])} ({signed(x['diff_lo'])}, {signed(x['diff_hi'])})")
            rows.append(f"{SHORT[a]} $-$ {SHORT[b]} & " + " & ".join(cells))
    head = r"Pair & New variant & New setting & New family"
    return table(rows, "Paired differences of the decisive distance between rules (floors)", "tab:paired", "lrrr",
                 head, colsep="5pt", place="h",
                 note=r"Difference and 95\,\% interval; a negative difference means that the first rule decides closer to "
                      r"the requirement. Upper block: common resamples of Table~\ref{tab:distci} (fits fixed); lower "
                      r"block: refitted rules.")


def t_coverage() -> str:
    c = read("dec_coverage.csv").set_index(["scope", "method"])
    rules = ["M0w", "M2", "M3", "M5", "M2n", "M4", "M5n"]
    rows = []
    for m in rules:
        cells = []
        for s in ["within", "setting", "transfer", "pooled"]:
            x = c.loc[(s, m)]
            cells.append(f"{pct(x['coverage'])} & {dist(x['half_width_floors'])} & {dist(x['centre_decisive'])}")
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{3}{c}{New variant} & \multicolumn{3}{c}{New setting} & \multicolumn{3}{c}{New family} & "
            r"\multicolumn{3}{c}{Pooled variant} \\" "\n"
            r"\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}\cmidrule(lr){11-13}" "\n"
            r"Rule & cov. & half & centre & cov. & half & centre & cov. & half & centre & cov. & half & centre")
    return table(rows, "Interval rules: coverage of the true $q_{95}$, half-width and the accuracy of the centre",
                 "tab:coverage", "l" + "r" * 12, head, colsep="2.6pt", place="h",
                 note=r"cov.: share of cases whose true $q_{95}$ lies in the interval (\%; nominal 90\,\%; the largest "
                      r"residual attains at most $n/(n+1)$); half: median half-width (floors); centre: decisive distance "
                      r"of the interval centre used as a point rule (floors).")


def t_qcdist() -> str:
    r = read("dec_resolution.csv").set_index(["scope", "qc", "method"])
    rules = ["M1s", "M2", "M5", "M5n", "NN"]
    rows = []
    for c in SHARED:
        cells = []
        for s in ["within", "setting"]:
            cells += [pair(r.loc[(s, c, m)], m) for m in rules]
        rows.append(f"{LABEL[c]} & " + " & ".join(cells))
    head = (r" & \multicolumn{5}{c}{New variant} & \multicolumn{5}{c}{New setting} \\" "\n"
            r"\cmidrule(lr){2-6}\cmidrule(lr){7-11}" "\n" "Characteristic & " + " & ".join(rules + rules))
    return table(rows, "Decisive/safe distance per characteristic (floors)", "tab:qcdist", "l" + "r" * 10, head,
                 colsep="2.4pt", place="h",
                 note=r"18 held-out alternatives per characteristic and scope; one wrong verdict moves a share by about "
                      r"three percentage points.")


def t_units() -> str:
    u = read("panel_physical_units.csv").set_index(["scope", "method", "qc"])
    cols = [("within", "NN"), ("within", "M5"), ("setting", "NN"), ("setting", "M5"), ("transfer", "M1"),
            ("transfer", "M2"), ("transfer", "M5")]
    rows = [f"{LABEL[c]} ({UNIT[c]}) & " + " & ".join(sig(u.loc[(s, m, c), "resolution_floors"], 2) for s, m in cols)
            for c in SHARED]
    head = (r" & \multicolumn{2}{c}{New variant} & \multicolumn{2}{c}{New setting} & \multicolumn{3}{c}{New family} \\"
            "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-8}" "\n"
            r"Characteristic & NN & M5 & NN & M5 & M1 & M2 & M5")
    return table(rows, "Decisive distances per characteristic in its unit", "tab:units", "lrrrrrrr", head,
                 colsep="4pt", place="h",
                 note=r"The decisive distance computed with a unit floor, in the unit of the characteristic.")


def t_transfer() -> str:
    s = read("panel_source_floor.csv").set_index(["method", "floor"])
    rules = ["M0", "M1", "M1s", "Mc", "M2", "M3", "M5", "NN"]
    rows = [f"{SHORT[m]} & {pair(s.loc[(m, 'target family')], m)} & {pair(s.loc[(m, 'source family')], m)}"
            for m in rules]
    rows.append(r"\multicolumn{3}{@{}l}{\emph{Wall angle only: decisive/safe distance; median and 90\,\% absolute error}}")
    n = read("panel_nominal_offset.csv")
    for _, x in n.iterrows():
        m = x["method"]
        label = "nominal + offset" if m == "nominal + offset" else SHORT.get(m, m)
        pm = m if m in POINT or m == "nominal + offset" else None
        dd = dist(x["resolution_floors"]) if pm else f"{dist(x['resolution_floors'])}/{dist(x['safe_floors'])}"
        rows.append(f"{label} & {dd} & {x['median_abs_error']:.1f}; {x['abs_error_p90']:.1f}")
    head = r"Rule & target family's floor & source family's floor"
    return table(rows, "A new family: distances in the floor of the produced family, and a baseline from the drawing "
                       "nominal", "tab:transfer", "lrr", head, colsep="8pt", place="h",
                 note=r"Upper block: all characteristics, $\delta_\mathrm{d}/\delta_\mathrm{s}$ (floors). Lower block: wall "
                      r"angle of a new family (18 cases); nominal + offset: the design angle of the new family plus the "
                      r"median deviation $q_{95}-$ design angle of the produced family.")


def t_tuning() -> str:
    t = read("tune_decisions.csv").set_index(["scope", "rule", "setting"])
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
            r"Learner & M3 & M3n & M3 & M3n & M3 & M3n")
    return table(rows, "Part-level rules M3 and M3n under other learners and settings (decisive/safe, floors)",
                 "tab:tuning", "lrrrrrr", head, colsep="4pt", place="h",
                 note=r"Reference: histogram gradient boosting, depth 3, 200 iterations, rate 0.08. Regularised: depth 2, "
                      r"100 iterations, rate 0.05, L2 penalty 1. Flexible: depth 6, 400 iterations, rate 0.1. Ridge: linear "
                      r"regression on standardised inputs. Quantile loss: boosting of the 95th percentile. Selected: the "
                      r"boosting setting with the smallest leave-one-out error. Intervals: jackknife+.")


def t_gp() -> str:
    g = read("dec_gp.csv").set_index(["scope", "method"])
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
                 colsep="5pt", place="h",
                 note=r"Share of the fits whose noise level sits at its lower bound, the variance between the series of "
                      r"one geometry and force, and with a length scale at a bound (0.1 or 100).")


def t_step6() -> str:
    s = read("panel_step6.csv").set_index(["scope", "method"])
    rules = ["M1s", "M2", "M5", "M5n", "NN", "M2n", "M4"]
    scopes = [("within", "variant"), ("setting/interpolation", "interpolated"), ("setting/extrapolation", "extrapolated"),
              ("transfer", "new family")]
    rows = []
    for sc, name in scopes:
        for m in rules:
            x = s.loc[(sc, m)]
            g = x["guard_band"]
            alone = f"{dist(x['decisive_alone'])}/{dist(x['safe_alone'])}"
            if np.isfinite(g):
                step = f"{dist(x['decisive_step6'])}/{dist(x['safe_step6'])}"
                tr = f"{pct(x['trial_10_alone'])} $\\to$ {pct(x['trial_10_step6'])}"
            else:
                step, tr = "trial", f"{pct(x['trial_10_alone'])} $\\to$ 100"
            rows.append(f"{name if m == rules[0] else ''} & {SHORT[m]} & {dist(g)} & {alone} & {step} & {tr}")
    head = r"Relation & Rule & $g$ & rule alone & step 6 & trial at 10 floors (\%)"
    return table(rows, "The procedure's decision rule: guard band and operating characteristics", "tab:step6",
                 "llrrrr", head, colsep="6pt", place="h",
                 note=r"$g$: smallest observable margin (floors) beyond which at least 95\,\% of the decided verdicts are "
                      r"correct for requirements on the grid within 20 floors of the truth; $\infty$: never, the procedure "
                      r"sends every design to trial. Distances $\delta_\mathrm{d}/\delta_\mathrm{s}$ in floors.")


def t_guard() -> str:
    g = read("dec_guard.csv").set_index(["guard", "scope", "method"])
    rows = []
    for scope, sname in (("setting", "New setting"), ("transfer", "New family")):
        for guard in ["none", "range", "novelty"]:
            cells = []
            for m in ["M2", "M5", "NN"]:
                x = g.loc[(guard, scope, m)]
                cells.append(f"{pair(x, m)} & {int(x['wrong_through'])}/{int(x['verdicts_through'])}")
            fa = g.loc[(guard, scope, "M5")]
            rows.append(f"{sname if guard == 'none' else ''} & {guard} & {int(fa['cases_guarded'])} & " + " & ".join(cells))
    head = (r" & & & \multicolumn{2}{c}{M2} & \multicolumn{2}{c}{M5} & \multicolumn{2}{c}{NN} \\" "\n"
            r"\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}" "\n"
            f"Scope & Guard & Guarded & {DD} & wrong & {DD} & wrong & $\\delta_\\mathrm{{d}}$ & wrong")
    return table(rows, "Applicability guards: distances and wrong verdicts among the cases a guard lets through",
                 "tab:guard", "llrrrrrrr", head, colsep="3.5pt", place="h",
                 note=r"Guarded: cases (of 126) sent to trial. Range guard: geometry not calibrated or force outside the "
                      r"calibrated range; novelty guard: simulated $q_{95}$ outside the calibration range. Wrong: wrong "
                      r"verdicts at $|d|=10$ among those let through.")


def t_capability() -> str:
    c = read("panel_capability.csv").set_index(["ppk", "scope", "method"])
    ppk = [1.0, 1.33, 1.67, 2.0]
    rules = ["NN", "M1s", "M1", "M2", "M5", "M5n"]
    rows = []
    for scope, name in (("within", "New variant"), ("setting", "New setting"), ("transfer", "New family")):
        for m in rules:
            cells = [f"{pct(c.loc[(p, scope, m), 'right'])}/{pct(c.loc[(p, scope, m), 'trial'])}" for p in ppk]
            rows.append(f"{name if m == rules[0] else ''} & {SHORT[m]} & " + " & ".join(cells))
    med = read("panel_capability.csv").groupby("ppk")["median_d"].median()
    head = "Relation & Rule & " + " & ".join(f"$P_\\mathrm{{pk}}={p:g}$" for p in ppk)
    return table(rows, "Requirements anchored in capability: right and trial verdicts (\\%)", "tab:capability",
                 "llrrrr", head, colsep="6pt", place="h",
                 note=r"Upper limit at centre $+\,3P_\mathrm{pk}$ standard deviations of each alternative's parts; every "
                      r"alternative meets it, so the rest of the verdicts are false rejects. The limits lie a median "
                      + ", ".join(f"{med.loc[p]:.1f}" for p in ppk) + r" floors above $q_{95}$.")


def t_scenarios() -> str:
    s = read("scen_scores.csv").set_index(["scope", "method"])
    st = read("scen_strata.csv")
    st = st[st["stratum"] == "0-5"].set_index(["scope", "method"])
    tr = read("scen_truth.csv")
    rules = ["M0", "M1", "M1s", "M2", "M5", "NN", "M5n"]
    rows = []
    for m in rules:
        cells = []
        for scope in ["within", "setting", "transfer"]:
            x, y = s.loc[(scope, m)], st.loc[(scope, m)]
            cells.append(f"{pct(x['correct'])} & {pct(y['correct'])} & {pct(x['false_accept_given_fails'])} & "
                         f"{pct(x['uncertain'])}")
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    n_fail = int((~tr["meets"]).sum())
    n_near = int((tr["margin_floors"].abs() < 5).sum())
    head = (r" & \multicolumn{4}{c}{New variant (\%)} & \multicolumn{4}{c}{New setting (\%)} & "
            r"\multicolumn{4}{c}{New family (\%)} \\" "\n" r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}" "\n"
            r"Rule & right & ${<}5$ & FA & trial & right & ${<}5$ & FA & trial & right & ${<}5$ & FA & trial")
    return table(rows, "Verdicts against requirements from general angular tolerances (ISO 2768-1)", "tab:scenarios",
                 "l" + "r" * 12, head, colsep="2.4pt", place="h",
                 note=f"Wall and arm angle, classes f/m, c and v: {len(tr)} decisions per rule and scope, {n_fail} with a "
                      f"failing alternative, {n_near} with the limit within 5 floors of the truth. right: correct verdicts; "
                      r"${<}5$: correct among the decisions within 5 floors; FA: false accepts among the failing "
                      r"alternatives; trial: sent to trial.")


def t_costmap() -> str:
    c = read("scen_cost_map.csv")
    cts = sorted(c["c_trial"].unique())
    rows = []
    for scope, name in (("within", "New variant"), ("setting", "New setting"), ("transfer", "New family")):
        for cfr in sorted(c["c_fr"].unique()):
            g = c[(c["scope"] == scope) & (c["c_fr"] == cfr)].set_index("c_trial")
            cells = ["/".join(SHORT.get(x, x) for x in g.loc[ct, "cheapest"].split("/")) for ct in cts]
            rows.append(f"{name if cfr == min(c['c_fr']) else ''} & {cfr:g} & " + " & ".join(cells))
    head = r"Relation & $c_\mathrm{FR}$ & " + " & ".join(f"{ct:g}" for ct in cts)
    return table(rows, "Cheapest rule in the tolerance scenario by the costs of a false reject and a trial",
                 "tab:costmap", "lr" + "l" * len(cts), head, colsep="4pt", place="h",
                 note=r"Costs relative to a false accept; columns: cost of a trial $c_\mathrm{T}$. Ties joined by a slash.")


def t_inline() -> str:
    d = read("inline_drift.csv").set_index("qc")
    rows = [f"{LABEL[c]} ({UNIT[c]}) & {int(d.loc[c, 'n_batches'])} & {signed(d.loc[c, 'r2_oof_batch'], 2, plus=False)} & "
            f"{sig(d.loc[c, 'floor'])} & {sig(d.loc[c, 'floor_drift_removed'])} & "
            f"{signed(-100 * d.loc[c, 'floor_reduction'], 0)}" for c in SHARED]
    head = r"Characteristic & Batches & $R^2$, out of fold & $F$ & $F$, drift removed & Change (\%)"
    return table(rows, "Drift of the batch centres explained by the process signals", "tab:inline", "lrrrrr", head,
                 colsep="5pt", place="h",
                 note=r"Ridge regression of the batch centres on the batch centres of press force, punch temperature, sheet "
                      r"thickness and oil film, folds by alternative; $F$ recomputed after removing the predicted drift.")


def t_robust() -> str:
    r = read("rob_decisions.csv").set_index(["variant", "scope", "method"])
    order = [("reference", "Reference"), ("temperature-adjusted", "Temperature-adjusted"),
             ("first 150 parts dropped", "First 150 parts dropped"), ("smoothed simulation", "Smoothed simulation"),
             ("adequacy share 0.90", "Adequacy share 0.90"), ("adequacy share 0.99", "Adequacy share 0.99"),
             ("floor with batch 25 and quantile 0.95", "Floor: batches of 25"),
             ("floor with batch 100 and quantile 0.95", "Floor: batches of 100"),
             ("floor with batch 50 and quantile 0.90", r"Floor: 90\,\% quantile"),
             ("floor with batch 50 and quantile 0.99", r"Floor: 99\,\% quantile"),
             ("floor between series", "Floor between series"),
             ("resolution target 0.90", r"Target 90\,\%"), ("resolution target 0.99", r"Target 99\,\%"),
             ("calibration series of 50 parts", "Calibration series of 50"),
             ("calibration series of 100 parts", "Calibration series of 100"),
             ("calibration series of 250 parts", "Calibration series of 250"),
             ("interval level 0.80", "Interval level 0.80"), ("interval level 0.95", "Interval level 0.95"),
             ("GP matern", r"GP: Mat\'ern 5/2"), ("GP linear", "GP: linear trend"),
             ("GP onehot", "GP: one-hot lubrication"), ("GP ls_floor", "GP: length-scale floor"),
             ("GP no_noise_floor", "GP: no noise floor"), ("GP se_floor", "GP: sampling noise floor")]
    cols = [("within", "M1s"), ("within", "M2"), ("within", "M5"), ("within", "NN"), ("setting", "M2"),
            ("setting", "M5"), ("setting", "NN"), ("transfer", "M2"), ("transfer", "M5")]

    def cell(v, scope, m):
        key = (v, scope, m)
        return pair(r.loc[key], m) if key in r.index else ""

    rows = [f"{name} & " + " & ".join(cell(v, s, m) for s, m in cols) for v, name in order
            if any((v, s, m) in r.index for s, m in cols)]
    lolo = [("leave one pattern out", "lubricant", m) for m in ["M1s", "M2", "M5", "NN"]]
    rows.append("Leave one pattern out & " + " & ".join(pair(r.loc[k], k[2]) if k in r.index else "" for k in lolo)
                + " & & & & & ")
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
                 note=r"Alternative-level rules refitted for every variant; empty cells: the variant does not affect the "
                      r"rule. Floor variants rescale the distances with other floors. Calibration series of $n$: the "
                      r"calibration alternatives' $q_{95}$ from their first $n$ parts. Leave one pattern out: columns M1s, "
                      r"M2, M5 and NN of the first block. Refit bootstrap: 95\,\% interval when the lubrication patterns of "
                      r"each geometry are resampled and every rule is refitted (200 resamples).")


TABLES = {"floors": t_floors, "distances": t_distances, "drivers": t_drivers, "design": t_design,
          "qcs": t_qcs, "components": t_components, "protocol": t_protocol, "lags": t_lags, "resolve": t_resolve,
          "offsets": t_offsets, "simnoise": t_simnoise, "scan": t_scan, "resolution": t_resolution, "runs": t_runs,
          "weights": t_weights, "alldist": t_alldist, "distci": t_distci, "onesided": t_onesided, "paired": t_paired,
          "coverage": t_coverage, "qcdist": t_qcdist, "units": t_units, "transfer": t_transfer, "tuning": t_tuning,
          "gp": t_gp, "step6": t_step6, "guard": t_guard, "capability": t_capability, "scenarios": t_scenarios,
          "costmap": t_costmap, "inline": t_inline, "robust": t_robust}


def main() -> None:
    texts = MAIN.read_text() + ESM.read_text()
    failed = []
    for name, fn in TABLES.items():
        if f"%% BEGIN GENERATED {name}" not in texts:
            print(f"{name}: no block")
            continue
        try:
            write_block(name, fn())
            print(f"{name}: written")
        except (KeyError, FileNotFoundError, ValueError, IndexError) as e:     # a result file not yet regenerated
            failed.append(name)
            write_block(name, table([r"\multicolumn{2}{l}{(not yet generated)}"], f"{name} (pending)", f"tab:{name}",
                                    "ll", "Pending & ", place="h"))
            print(f"{name}: FAILED ({type(e).__name__}: {e})")
    esm_labels()
    if failed:
        sys.exit(f"tables not written: {', '.join(failed)}")


if __name__ == "__main__":
    main()
