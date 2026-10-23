"""Write the data tables of the manuscript and of its Online Resource 1 from the result CSVs.

Every number in a table comes from a CSV in results/; nothing is typed by hand. Each table sits between
'%% BEGIN GENERATED <name>' and '%% END GENERATED <name>' in paper/main.tex (main text and appendix) or
paper/supplement.tex (Online Resource 1, tables S1-S20). The results that neither tabulates are in the result
files and their summaries (results/summary_*.md), which are part of the archive.

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
SUPP = ROOT / "paper" / "supplement.tex"
LABEL = {"drawin_mid": "Draw-in, mid-side", "drawin_corner": "Draw-in, corner", "waviness": "Flange waviness",
         "wall_op10": "Wall angle", "arm_op20": "Arm angle, cut", "depth_op10": "Cup depth",
         "dome_op20": "Bottom dome, cut"}
UNIT = {"drawin_mid": "mm", "drawin_corner": "mm", "waviness": "mm", "wall_op10": r"$^\circ$",
        "arm_op20": r"$^\circ$", "depth_op10": "mm", "dome_op20": "mm"}
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


def pair(x, m: str, below_one: bool = False) -> str:
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
    return (f"\\begin{{table}}[{place}]\n{size}\n{sep}\\caption{{{caption.rstrip('.')}}}\\label{{{label}}}\n"
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
                     m6[m6["scope"] != "transfer"]], ignore_index=True)
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
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & {sig(f['floor'])} & {sig(f['floor_lo'])}--{sig(f['floor_hi'])} & "
                    f"{sig(f['floor_lo_alt'])}--{sig(f['floor_hi_alt'])} & {sig(f['floor_concave'])} & "
                    f"{sig(f['floor_convex'])} & {r['run_floor_min']:.2f}--{r['run_floor_max']:.2f} & "
                    f"{r['warm_up_ratio']:.2f} & {lt}")
    head = (r"Characteristic & $F$ & Batches & Clusters & Concave & Convex & Single runs & No warm-up & "
            r"$F/\sigma_\mathrm{LT}$")
    return table(rows, "Within-run floor per characteristic, pooled and per geometry, with its spread over runs",
                 "tab:floors", "lrrrrrrrr", head, colsep="2.4pt",
                 note=r"Batches of 50 consecutive parts, 95\,\% quantile of the difference of their 10\,\% trimmed "
                      r"means. Batches, Clusters: 95\,\% intervals from 2000 resamples of batches and of whole "
                      r"alternatives. Single runs: floor of one run over that of its geometry, range over the 18 runs. "
                      r"No warm-up: floor without the first 150 parts over the reference. $\sigma_\mathrm{LT}$: "
                      r"standard deviation of the parts of a series (concave/convex); $\sigma_\mathrm{b}$, "
                      r"$\sigma_\mathrm{w}$ and the drift in \esm{Table~S20}.")


def t_qcs() -> str:
    m = read("meas_characteristics.csv").set_index("qc")
    fl = read("alt_floor.csv").set_index("qc")
    rows = []
    for c in SHARED:
        x = m.loc[c]
        step = float(x["resolution_step"])
        bias = str(x["known_biases"]).replace("deg", r"$^\circ$").replace("sd(", r"$\sigma$(").replace("Wy - Wx", r"$W_y-W_x$").replace("-", "--").replace("----", "--")
        bias = "--" if bias.strip() == "--" else bias
        rows.append(f"{LABEL[c]} & {x['operation']} & {x['region']}; {x['directions']} & "
                    f"{sig(step, 2)} ({x['step_over_floor']:.2f}) & {bias}")
    head = r"Characteristic & Op. & Region; directions used & Step ($/F$) & Direction-dependent differences"
    return table(rows, "The quality characteristics and their measurement by the laser scanner", "tab:qcs",
                 r"L{1.85cm}L{0.65cm}L{3.55cm}L{1.35cm}L{4.95cm}", head, colsep="2.6pt",
                 note=r"Op.: operation measured (OP10 after drawing, OP20 after cutting). Step: median step between "
                      r"adjacent values in one series (unit of the characteristic) and over the floor. Differences "
                      r"from the redundancy of the four sides, series medians (\esm{Table~S20}); the directions used "
                      r"avoid them, their residual bias is unknown. Absolute values are not calibrated against a "
                      r"reference at the size of the part.")


def t_distances() -> str:
    r = distances_all()
    trial = read("qual_trial.csv").set_index("rule")
    rows = []
    for m in MAIN_RULES:
        cells = []
        for scope, _ in RELS:
            x = get(r, scope, m)
            cells += [pair(x, m, True), "--" if x is None else dist(x["safe_failing"], True)]
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
                    " & ".join([dist(x["resolution_floors"]), dist(x["safe_failing"])] * 4))
    head = (r" & \multicolumn{2}{c}{Sibling} & \multicolumn{2}{c}{Interpolated} & \multicolumn{2}{c}{Extrapolated} & "
            r"\multicolumn{2}{c}{New family} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}" "\n"
            f"Rule & {DD} & FA & {DD} & FA & {DD} & FA & {DD} & FA")
    return table(rows, "Decisive and safe distances (floors) by the relation of the new design to the produced "
                       "evidence", "tab:distances", "l" + "r" * 8, head, colsep="3.4pt",
                 note=r"Over all seven characteristics; one number for rules that always decide; $<$1: below one floor. "
                      r"FA: safe distance on the false-accept side. 126 cases with a sibling and for a new family, 42 "
                      r"interpolated, 84 extrapolated; a new family in the produced family's floor (in its own floor in "
                      r"\esm{Table~S1}). Interval: 95\,\% over 1000 resamples of the held-out alternatives, fits fixed. "
                      r"Trial: the first $n$ parts of the design's own run, a within-run lower bound. $^\dagger$, "
                      r"$^\ddagger$: added after the first results and in revision.")


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
                      r"bands per family, out of sample and under other priors in \esm{Tables~S7--S10}.")


# ── appendix ──────────────────────────────────────────────────────────────────
FURTHER_DEF = {
    "M1": "M0 plus the median offset of the calibration alternatives",
    "M1n": "median $q_p$ of the calibration alternatives",
    "M2n": "M1n with the largest-residual margin",
    "M5n": "GP of $q_p$ over the descriptors, ML-II, noise-variance bound",
    "M7": "M7n with the nominal simulation in the mean (AR(1) multi-fidelity)",
    "Mc": "friction per pattern fitted to the draw-ins, least squares, plus offset",
    "Mcd": "friction calibrated with a GP discrepancy; posterior mixture",
    "M0w": "range of the simulation over thickness and friction",
    "M3": "matched simulation plus boosted discrepancy, parts; jackknife+",
    "M4": "boosted model of the characteristic, parts; jackknife+",
    "M6": "M5 mean with a conformal margin on standardised residuals",
}


def t_further() -> str:
    r = distances_all()
    rows = []
    for m in FURTHER:
        cells = [pair(get(r, s, m), m) for s, _ in RELS]
        rows.append(f"{SHORT[m]}{MARK.get(m, '')} & {FURTHER_DEF[m]} & " + " & ".join(cells))
    head = "Rule & Prediction of $q_p$ & Sibling & Interp. & Extrap. & New family"
    return table(rows, "The further rules and their decisive/safe distances (floors) by relation", "tab:further",
                 r"lL{5.0cm}rrrr", head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"M1, M1n, M2n, M5n and M7 pair with M1s, M2, M5 and M7n with and without the simulation; M3n is "
                      r"M4 in the code; M6 is a robustness variant. A new family in the produced family's floor. "
                      r"Pooled scopes and intervals in \esm{Table~S1}.")


def t_gp() -> str:
    g = read("learn_gp_diagnostics.csv").set_index(["relation_scope", "method"])
    rels = [("sibling", "Sibling"), ("interpolation", "Interpolated"), ("extrapolation", "Extrapolated"),
            ("new family", "New family")]
    rows = []
    for rel, lab in rels:
        for m in ["M5", "M5n", "M7n"]:
            if (rel, m) not in g.index:
                continue
            x = g.loc[(rel, m)]
            noise = (f"{x['median_noise_over_bound']:.2f}" if m != "M7n"
                     else f"{x['median_nugget_floors'] / x['median_se_floors']:.1f}")
            low = pct(x["ls_at_lower_share"]) if m != "M7n" else "--"
            lead = lab if m == "M5" else ""
            rows.append(f"{lead} & {m} & {int(x['fits'])} & {x['median_ls_bhf']:.2f} & {low} & {noise} & "
                        f"{dist(x['median_d_calib_mean'])} & {pct(x['share_within_001_of_calib_mean'])} & "
                        f"{dist(x['median_d_nn'])} & {dist(x['median_d_m1sn'])} & {dist(x['median_half_width'])}")
    head = (r"Relation & Rule & Fits & $\ell_F$ & At bound & Noise & $\Delta$mean & ${\le}0.01$ & $\Delta$NN & "
            r"$\Delta$M1sn & HW")
    return table(rows, "Fitted Gaussian processes by relation: hyperparameters and where their centres lie", "tab:gp",
                 "llrrrrrrrrr", head, colsep="2.6pt", place="p", size=r"\tabsizesmall",
                 note=r"$\ell_F$: median force length scale (100\,kN). At bound: fits with $\ell_F$ at its lower bound "
                      r"(\%). Noise: fitted noise over its bound (M5, M5n) or nugget over the sampling error of the "
                      r"truths (M7n), median. $\Delta$mean, $\Delta$NN, $\Delta$M1sn: median distance (floors) of the "
                      r"centre from the calibration mean, NN and M1sn; ${\le}0.01$: cases within 0.01 floor of the "
                      r"calibration mean (\%). HW: median half-width (floors).")


def t_crossing() -> str:
    r = distances_all()
    cov = read("qual_coverage.csv")
    cov = cov[cov["subset"] == "all"].set_index(["relation", "method"])
    relmap = {"within": "sibling", "setting/interpolation": "interpolation", "setting/extrapolation": "extrapolation",
              "transfer": "new family"}
    rows = []
    for p in ["NN", "M1sn", "M1s", "M5n", "M5", "M4", "M7n", "M7"]:
        m = f"{p}+RM"
        cells = []
        for scope, _ in RELS:
            x = get(r, scope, m)
            c = cov.loc[(relmap[scope], m)]["coverage"] if (relmap[scope], m) in cov.index else np.nan
            cells += [pair(x, m, True), pct(c)]
        rows.append(f"{SHORT.get(m, m)} & " + " & ".join(cells))
    rows.append(r"\midrule \multicolumn{9}{@{}l}{\emph{The rules with their own intervals}} \\")
    for m in ["M2", "M3", "M5", "M7n"]:
        cells = []
        for scope, _ in RELS:
            x = get(r, scope, m)
            c = cov.loc[(relmap[scope], m)]["coverage"] if (relmap[scope], m) in cov.index else np.nan
            cells += [pair(x, m, True), pct(c)]
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{Sibling} & \multicolumn{2}{c}{Interpolated} & \multicolumn{2}{c}{Extrapolated} & "
            r"\multicolumn{2}{c}{New family} \\" "\n"
            r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}" "\n"
            f"Predictor + interval & {DD} & Cov & {DD} & Cov & {DD} & Cov & {DD} & Cov")
    return table(rows, "Point predictors with a relation-matched interval, against the rules' own intervals",
                 "tab:crossing", "l" + "r" * 8, head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"P+RM: the prediction of P (for interval rules the interval centre) with the 90\,\% split-conformal "
                      r"quantile of P's absolute errors (floors) over the cases of the same relation in the other family "
                      r"(sibling 63, interpolated 21, extrapolated 42, new family 63). Cov: coverage of the true $q_{95}$ "
                      r"(\%); cluster intervals and interval scores in \esm{Table~S4}. A new family in the produced "
                      r"family's floor.")


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
            cells.append(f"{dist(x['resolution_floors'])} ({sig(x['decisive_units'])})")
        x = p.loc[("sibling", "NN", c)]
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & " + " & ".join(cells) + f" & {x['ppk_at_decisive_median']:.1f}")
    head = (r" & \multicolumn{3}{c}{NN} & M1sn & M1s & M5 & \\" "\n"
            r"\cmidrule(lr){2-4}" "\n"
            r"Characteristic & Sibling & Interp. & Extrap. & Extrap. & Extrap. & New family & $P_\mathrm{pk}$")
    return table(rows, "Decisive distance per characteristic in floors and, in brackets, in its unit", "tab:groups",
                 "lrrrrrrr", head, colsep="2.4pt", place="p", size=r"\tabsizesmall",
                 note=r"18 cases per characteristic with a sibling and for a new family, 6 interpolated, 12 "
                      r"extrapolated; units through the pooled floor of the characteristic; a new family in the "
                      r"produced family's floor. $P_\mathrm{pk}$: median performance index of a requirement at the "
                      r"decisive distance of NN with a sibling. All rules and the safe distances in \esm{Table~S15}.")


def t_validation() -> str:
    v = read("sim_validation.csv")
    rows = []
    for c in SHARED:
        g = v[v["qc"] == c]
        d, dfl = g["sim_minus_measured"], g["sim_minus_measured_floors"]
        nz = g["sim_xy_sd_floors"].dropna()
        rows.append(f"{LABEL[c]} ({UNIT[c]}) & {sig(g['measured_centre'].min(), 3)}--{sig(g['measured_centre'].max(), 3)} & "
                    f"{sig(d.min())} to {sig(d.max())} & {dfl.min():.0f} to {dfl.max():.0f} & "
                    f"{int(g['measured_inside_friction_range'].sum())} & "
                    f"{g['closest_mu'].min():.2f}--{g['closest_mu'].max():.2f} & "
                    f"{('--' if nz.empty else f'{nz.min():.1f}--{nz.max():.1f}')} & "
                    f"{g['sim_roughness_sd_floors'].min():.1f}--{g['sim_roughness_sd_floors'].max():.1f}")
    head = (r"Characteristic & Measured & Sim.\,$-$\,meas. & In floors & Inside & Closest $\mu$ & $x$--$y$ & "
            r"Roughness")
    return table(rows, "The simulation dataset against the measurement, over the six geometry--force cells",
                 "tab:validation", "lrrrrrrr", head, colsep="2.4pt", place="p", size=r"\tabsizesmall",
                 note=r"Measured: range of the cells' centres (signed). Sim.\,$-$\,meas.: simulation at 0.99\,mm and "
                      r"friction 0.10 minus the measured centre, in the unit and in floors. Inside: cells whose measured "
                      r"centre lies within the simulated range over the friction grid (of 6). Closest $\mu$: grid "
                      r"friction nearest the measurement. $x$--$y$, Roughness: standard deviation of the difference "
                      r"between the two directions of the quarter model and roughness along the friction grid (floors), "
                      r"the extraction noise of the simulation. Per cell in \esm{Table~S18}.")


# ── Online Resource 1 ─────────────────────────────────────────────────────────
def s_all_rules() -> str:
    r = distances_all()
    scopes = [("within", "Sibling"), ("setting", "Setting"), ("setting/interpolation", "Interp."),
              ("setting/extrapolation", "Extrap."), ("transfer", "Fam., prod."), ("transfer/own", "Fam., own"),
              ("pooled", "Pooled var."), ("pooled-setting", "Pooled set.")]
    rows = []
    for m in ALL_RULES + ["M1sn+RM", "M5n+RM", "M7n+RM", "M4+RM", "M5+RM", "M1s+RM", "M7+RM"]:
        cells = [pair(get(r, s, m), m) for s, _ in scopes]
        if all(c == "--" for c in cells):
            continue
        rows.append(f"{SHORT.get(m, m)} & " + " & ".join(cells))
        ci = []
        for s, _ in scopes:
            x = get(r, s, m)
            ci.append("" if x is None or "resolution_lo" not in x or not np.isfinite(x["resolution_lo"]) else
                      f"{dist(x['resolution_lo'])}--{dist(x['resolution_hi'])}")
        rows.append(r"\quad interval & " + " & ".join(ci))
    head = "Rule & " + " & ".join(lab for _, lab in scopes)
    return table(rows, "All rules: decisive/safe distances (floors) by scope, with the 95 % interval of the decisive "
                       "distance", "tab:s-all", "l" + "r" * len(scopes), head, colsep="2pt", place="p",
                 size=r"\tabsizesmall",
                 note=r"Fam., prod. and Fam., own: a new family in the produced family's floor and in its own. Pooled: "
                      r"the other geometry's alternatives added to the calibration set. Intervals over 1000 resamples of "
                      r"the held-out alternatives with the fits fixed.")


def s_variants() -> str:
    rob = read("rob_decisions.csv").set_index(["variant", "scope", "method"])
    var = read("qual_variants.csv")
    env = read("sim_envelope_variant.csv")
    order = [("reference", "Reference"), ("temperature-adjusted", "Temperature-adjusted"),
             ("first 150 parts dropped", "Warm-up dropped"), ("floor between series", "Floor between series"),
             ("floor with batch 25 and quantile 0.95", "Floor: batches of 25"),
             ("floor with batch 100 and quantile 0.95", "Floor: batches of 100"),
             ("floor with batch 50 and quantile 0.90", r"Floor: 90\,\% quantile"),
             ("floor with batch 50 and quantile 0.99", r"Floor: 99\,\% quantile"),
             ("calibration series of 50 parts", "Calibration: 50 parts"),
             ("adequacy share 0.90", r"Conformance $p=0.90$"), ("adequacy share 0.99", r"Conformance $p=0.99$"),
             ("interval level 0.80", "Interval level 0.80"), ("interval level 0.95", "Interval level 0.95"),
             ("smoothed simulation", "Response surface"), ("GP se_floor", "GP: sampling bound")]
    cols = [("within", "M1s"), ("within", "M2"), ("within", "M5"), ("within", "NN"), ("setting", "M2"),
            ("setting", "M5"), ("setting", "NN"), ("setting", "M1sn")]
    rows = []
    for v, name in order:
        cells = [pair(rob.loc[(v, s, m)], m) if (v, s, m) in rob.index else "" for s, m in cols]
        if any(cells):
            rows.append(f"{name} & " + " & ".join(cells))
    relmap = {"within": "sibling", "setting": None}
    for label in ["lower limits (5th percentile)", "short runs: first 20 parts", "short runs: first 50 parts",
                  "decided statistic: centre + 3.99 sd"]:
        g = var[var["variant"] == label].set_index(["relation", "method"])
        cells = []
        for s, m in cols:
            rel = "sibling" if s == "within" else "extrapolation"
            key = (rel, m)
            cells.append(pair(g.loc[key], m) if key in g.index else "")
        name = {"lower limits (5th percentile)": r"Lower limits (5th percentile)$^*$",
                "short runs: first 20 parts": "Short runs: 20 parts$^*$", "short runs: first 50 parts":
                "Short runs: 50 parts$^*$", "decided statistic: centre + 3.99 sd": r"Statistic $\bar m+4\sigma$$^*$"}[label]
        rows.append(f"{name} & " + " & ".join(cells))
    e = env[env["envelope"] == "measured incoming variation"].set_index(["scope", "method"])
    cells = []
    for s, m in cols:
        key = ("within" if s == "within" else "setting/extrapolation", m)
        cells.append(f"{dist(e.loc[key, 'resolution_floors'])}/{dist(e.loc[key, 'safe_floors'])}" if key in e.index else "")
    rows.append(r"Envelope over measured inputs$^*$ & " + " & ".join(cells))
    ref = read("rob_refit.csv").set_index(["scope", "method"])
    rows.append(r"\midrule Refit, $\delta_\mathrm{d}$ & " + " & ".join(
        f"{dist(ref.loc[(s, m), 'resolution_lo'])}--{dist(ref.loc[(s, m), 'resolution_hi'])}" if (s, m) in ref.index else ""
        for s, m in cols))
    head = (r" & \multicolumn{4}{c}{Sibling} & \multicolumn{4}{c}{New setting} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}" "\n"
            r"Variant & M1s & M2 & M5 & NN & M2 & M5 & NN & M1sn")
    return table(rows, "Decisive/safe distances (floors) under the robustness and sensitivity variants", "tab:s-variants",
                 "l" + "r" * 8, head, colsep="2.4pt", place="p", size=r"\tabsizesmall",
                 note=r"Rules refitted for every variant. $^*$: added in revision; their new-setting columns are the "
                      r"extrapolated setting. Lower limits: draw-ins, wall angle and depth. Short runs: calibration and "
                      r"truths from the first $n$ parts. Envelope over measured inputs: thickness and mapped friction "
                      r"between the 5th and 95th percentiles of the parts. Refit: 95\,\% interval over 200 draws of each "
                      r"geometry's lubrication patterns with replacement.")


def s_strata() -> str:
    s = read("qual_strata.csv").set_index(["stratum", "method"])
    o = read("panel_sibling_strata.csv").set_index(["resolved_siblings", "method"])
    rows = []
    for m in ["NN", "M1sn", "M1s", "M2", "M5", "M7n", "NN+RM"]:
        cells = []
        for st in ("siblings not resolvable", "siblings resolvable"):
            x = s.loc[(st, m)]
            cells += [pair(x, m), f"{x['abs_error_p90']:.2f}"]
        for k in (0, 1, 2):
            cells.append(pair(o.loc[(k, m)], m) if (k, m) in o.index else "--")
        rows.append(f"{SHORT.get(m, m)} & " + " & ".join(cells))
    cnt = s.xs("NN", level="method")
    head = (r" & \multicolumn{4}{c}{Decision time: produced siblings} & \multicolumn{3}{c}{Outcome (diagnostic)} \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-8}" "\n"
            f"Rule & not resolvable & p90 & resolvable & p90 & 0 & 1 & 2")
    return table(rows, "Sibling strata: from decision-time information and, as a diagnostic, from the outcome",
                 "tab:s-strata", "l" + "r" * 7, head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=rf"Decision time: the two produced siblings differ resolvably from each other or not "
                      rf"({int(cnt.loc['siblings not resolvable', 'cases'])} and {int(cnt.loc['siblings resolvable', 'cases'])} "
                      rf"cases on {int(cnt.loc['siblings not resolvable', 'alternatives'])} and "
                      rf"{int(cnt.loc['siblings resolvable', 'alternatives'])} alternatives). p90: 90th percentile of the "
                      rf"absolute error of the centre (floors). Outcome: number of siblings that differ resolvably from the "
                      rf"held-out alternative itself, which uses its production (58, 34 and 34 cases).")


def s_coverage() -> str:
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
            cells += [f"{pct(x['coverage'])} ({pct(x['coverage_lo'])}--{pct(x['coverage_hi'])})", f"{x['interval_score']:.0f}"]
        lvl = a[(a["method"] == m) & (a["relation"] == "sibling")]["level"].iloc[0]
        rows.append(f"{SHORT.get(m, m)} & {lvl.split(' (')[0]} & " + " & ".join(cells))
    for m in ["NN", "M1sn", "M1s"]:
        cells = []
        for rel in rels:
            x = a[(a["relation"] == rel) & (a["method"] == m)]
            cells += ["--", f"{x.iloc[0]['interval_score']:.0f}" if not x.empty else "--"]
        rows.append(f"{m} & point & " + " & ".join(cells))
    head = (r" & & \multicolumn{2}{c}{Sibling} & \multicolumn{2}{c}{Interpolated} & \multicolumn{2}{c}{Extrapolated} & "
            r"\multicolumn{2}{c}{New family} \\" "\n" r"\cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}\cmidrule(lr){9-10}"
            "\n" r"Rule & Level & Cov & IS & Cov & IS & Cov & IS & Cov & IS")
    return table(rows, "Interval rules: coverage with cluster-bootstrap intervals and interval score by relation",
                 "tab:s-coverage", "ll" + "r" * 8, head, colsep="2pt", place="p", size=r"\tabsizesmall",
                 note=r"Level: guaranteed (largest residual, jackknife+; with a sibling) or nominal coverage. Cov: coverage "
                      r"(\%) with a 95\,\% interval over 2000 resamples of the alternatives within each geometry. IS: mean "
                      r"interval score (Gneiting and Raftery 2007) at $\alpha=0.1$, floors; lower is better; for point "
                      r"rules $20\,|e|$. A new family in the produced family's floor.")


def s_coverage_qc() -> str:
    c = read("qual_coverage.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation"]:
        for m in ["M5", "M5n", "M7n", "M3", "NN+RM"]:
            x = c[(c["relation"] == rel) & (c["method"] == m)].set_index("subset")
            cells = [pct(x.loc[q, "coverage"]) if q in x.index else "--" for q in SHARED]
            st = [f"{pct(x.loc[s, 'coverage'])}" if s in x.index else "--" for s in ("siblings not resolvable", "siblings resolvable")]
            rows.append(f"{rel if m == 'M5' else ''} & {SHORT.get(m, m)} & " + " & ".join(cells) + " & " + " & ".join(st))
    head = ("Relation & Rule & " + " & ".join(LABEL[q].replace("Draw-in, ", "D-i ").replace(", cut", "") for q in SHARED)
            + r" & Not res. & Res.")
    return table(rows, "Coverage (%) of the interval rules per characteristic and decision-time stratum", "tab:s-coverage-qc",
                 "ll" + "r" * 9, head, colsep="2pt", place="p", size=r"\tabsizesmall",
                 note=r"18 cases per characteristic with a sibling, 6 interpolated, 12 extrapolated. Not res., Res.: "
                      r"the produced siblings do not or do differ resolvably from each other (75 and 51 cases).")


def s_step6() -> str:
    s6 = read("panel_step6.csv").set_index(["scope", "method"])
    rels = [("within", "Sibling"), ("setting/interpolation", "Interpolated"), ("setting/extrapolation", "Extrapolated")]
    rows = []
    for m in ["M1", "M1s", "M2", "M5", "M5n", "NN", "M3", "M4", "M1sn"]:
        cells = []
        for scope, _ in rels:
            x = s6.loc[(scope, m)]
            if not np.isfinite(x["guard_band"]):
                cells += ["none", "--", "100", "100"]
                continue
            cells += [band(x["guard_band"]), f"{dist(x['decisive_step6'])}/{dist(x['safe_step6'])}",
                      pct(x["trial_10_step6"]), pct(x["trial_20_step6"])]
        rows.append(f"{SHORT[m]} & " + " & ".join(cells))
    head = (" & " + " & ".join(rf"\multicolumn{{4}}{{c}}{{{lab}}}" for _, lab in rels) + r" \\" "\n"
            r"\cmidrule(lr){2-5}\cmidrule(lr){6-9}\cmidrule(lr){10-13}" "\n"
            "Rule" + rf" & $g$ & {DD} & $T_{{10}}$ & $T_{{20}}$" * len(rels))
    return table(rows, "The decision rule of step 6, pooled over the families: band, distances and trial shares",
                 "tab:s-step6", "l" + "r" * 12, head, colsep="2.2pt", place="p", size=r"\tabsizesmall", full=True,
                 note=r"$g$: guard band (floors) under the reference prior; $\delta_\mathrm{d}/\delta_\mathrm{s}$: distances "
                      r"of the rule with its interval widened by $g$; $T_{10}$, $T_{20}$: share of verdicts sent to trial "
                      r"(\%) at requirements 10 and 20 floors from the truth. None: no band up to 20 floors reaches 95\,\%; "
                      r"so also M0 and M0w in every relation and every rule for a new family.")


def s_guard_family() -> str:
    g = read("qual_guard_family.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        for m in ["NN", "M1sn", "M2", "M5", "M5n", "M7n", "Mcd", "NN+RM"]:
            x = g[(g["relation"] == rel) & (g["method"] == m)]
            if x.empty:
                continue
            x = x.iloc[0]
            rows.append(f"{rel if m == 'NN' else ''} & {SHORT.get(m, m)} & {band(x['band_pooled'])} & "
                        f"{band(x['band_concave'])} & {pct(x['correct_concave'])} & {pct(x['correct_concave_with_other_band'])} & "
                        f"{band(x['band_convex'])} & {pct(x['correct_convex'])} & {pct(x['correct_convex_with_other_band'])}")
    head = (r" & & & \multicolumn{3}{c}{Concave} & \multicolumn{3}{c}{Convex} \\" "\n"
            r"\cmidrule(lr){4-6}\cmidrule(lr){7-9}" "\n"
            r"Relation & Rule & Pooled $g$ & $g$ & Correct & Other $g$ & $g$ & Correct & Other $g$")
    return table(rows, "Guard bands estimated per family and moved between the families", "tab:s-guard-family",
                 "ll" + "r" * 7, head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"Reference prior. Correct: share correct among decided verdicts (\%) with the family's own band; "
                      r"Other $g$: with the band of the other family. For a new family, the family is the target of the "
                      r"transfer. --: every design to trial.")


def s_guard_oos() -> str:
    o = read("qual_guard_oos.csv")
    rows = []
    for prior in ["reference (+-20)", "release-like (+-5)"]:
        for rel in ["sibling", "interpolation", "extrapolation"]:
            for m in ["NN", "M1sn", "M2", "M5", "M7n", "NN+RM"]:
                x = o[(o["prior"] == prior) & (o["relation"] == rel) & (o["method"] == m)].set_index("scheme")
                cells = []
                for sch in ("LOAO within family", "LOAO pooled", "leave force cell out"):
                    if sch not in x.index:
                        cells += ["", ""]
                        continue
                    y = x.loc[sch]
                    cells += ["--" if not np.isfinite(y["share_correct"]) else
                              f"{pct(y['share_correct'])} ({pct(y['share_correct_lo'])}--{pct(y['share_correct_hi'])})",
                              pct(y["trial_rate"])]
                y = x.iloc[0]
                lead = (prior.split(" (")[0] + ", " if rel == "sibling" and m == "NN" else "") + (rel if m == "NN" else "")
                rows.append(f"{lead} & {SHORT.get(m, m)} & {band(y['in_sample_band'])} & {pct(y['in_sample_correct'])} & "
                            + " & ".join(cells))
    head = (r" & & \multicolumn{2}{c}{In sample} & \multicolumn{2}{c}{LOAO, family} & \multicolumn{2}{c}{LOAO, pooled} & "
            r"\multicolumn{2}{c}{Force cell out} \\" "\n"
            r"\cmidrule(lr){3-4}\cmidrule(lr){5-6}\cmidrule(lr){7-8}\cmidrule(lr){9-10}" "\n"
            r"Prior, relation & Rule & $g$ & Corr. & Corr. & T & Corr. & T & Corr. & T")
    return table(rows, "Guard bands validated out of sample under the reference and the release-like prior",
                 "tab:s-guard-oos", "ll" + "r" * 8, head, colsep="1.8pt", place="p", size=r"\tabsizesmall",
                 note=r"Corr.: share correct among decided verdicts (\%), with a 95\,\% cluster interval out of sample; "
                      r"T: share sent to trial (\%). LOAO: band estimated without the held-out alternative, within its "
                      r"family or pooled over both; force cell out: without the held-out geometry--force cell.")


def s_prior_width() -> str:
    w = read("qual_guard_prior_width.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation"]:
        for m in ["NN", "M1sn", "M2", "M5", "M7n", "NN+RM"]:
            x = w[(w["relation"] == rel) & (w["method"] == m)].set_index("prior_half_width")
            cells = [f"{band(x.loc[h, 'band'])} ({pct(x.loc[h, 'trial_rate'])})" for h in (3.0, 5.0, 10.0, 20.0, 50.0)]
            rows.append(f"{rel if m == 'NN' else ''} & {SHORT.get(m, m)} & " + " & ".join(cells))
    head = r"Relation & Rule & $\pm3$ & $\pm5$ & $\pm10$ & $\pm20$ & $\pm50$"
    return table(rows, "Guard band (floors) and trial rate (%, in brackets) against the half-width of the prior",
                 "tab:s-prior", "ll" + "r" * 5, head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"Prior: the evaluation grid of requirement distances within the half-width, equal weights; $\pm20$ "
                      r"is the reference prior and $\pm5$ the release-like one. No rule qualifies for a new family.")


def s_guard_qc() -> str:
    g = read("qual_guard_characteristic.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation"]:
        for m in ["NN", "M1sn", "M2", "M5", "M7n"]:
            x = g[(g["relation"] == rel) & (g["method"] == m)].set_index("name")
            if x.empty or not np.isfinite(x["pooled_band"].iloc[0]):
                continue
            cells = [pct(x.loc[q, "share_correct"]) if q in x.index else "--" for q in SHARED]
            cls = [f"{band(x.loc[c, 'own_band'])}" for c in ("process indicators", "drawn geometry", "cut part")]
            rows.append(f"{rel if m == 'NN' else ''} & {SHORT.get(m, m)} & {band(x['pooled_band'].iloc[0])} & "
                        + " & ".join(cells) + " & " + " & ".join(cls))
    head = ("Relation & Rule & $g$ & " + " & ".join(LABEL[q].replace("Draw-in, ", "D-i ").replace(", cut", "") for q in SHARED)
            + r" & $g_\mathrm{P}$ & $g_\mathrm{G}$ & $g_\mathrm{C}$")
    return table(rows, "Share correct (%) per characteristic with the pooled band, and bands per class of characteristic",
                 "tab:s-guard-qc", "ll" + "r" * 11, head, colsep="1.6pt", place="p", size=r"\tabsizesmall",
                 note=r"Reference prior. $g_\mathrm{P}$, $g_\mathrm{G}$, $g_\mathrm{C}$: bands estimated for the process "
                      r"indicators (draw-ins, waviness), the drawn geometry (wall angle, depth) and the cut part (arm, dome).")


def s_costs() -> str:
    c = read("qual_costs.csv")
    c = c[c["prior"] == "reference (+-20)"]
    rows = []
    rules = ["M2", "M5", "M7n", "NN", "M1sn", "NN+RM", "M3"]
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        for cfr in (0.25, 0.5, 1.0):
            g = c[(c["relation"] == rel) & np.isclose(c["c_fr"], cfr)]
            cells = []
            for ct in (0.02, 0.05, 0.1, 0.2, 0.5):
                h = g[np.isclose(g["c_trial"], ct) & g["method"].isin(rules)]
                best = h.loc[h["cost_opt"].idxmin()]
                name = "trial" if best["cost_opt"] >= ct - 1e-12 else SHORT.get(best["method"], best["method"])
                nn = h[h["method"] == "NN"].iloc[0]
                cells.append(f"{name} {best['cost_opt']:.3f} ({band(nn['band_opt']) if nn['cost_opt'] < ct - 1e-12 else 'trial'})")
            rows.append(f"{rel if cfr == 0.25 else ''} & {cfr:g} & " + " & ".join(cells))
    head = r"Relation & $c_\mathrm{FR}$ & $c_\mathrm{T}=0.02$ & 0.05 & 0.1 & 0.2 & 0.5"
    return table(rows, "Cheapest rule and its expected cost per verdict, with the cost-minimising band of NN",
                 "tab:s-costs", "lr" + "r" * 5, head, colsep="2.4pt", place="p", size=r"\tabsizesmall",
                 note=r"Costs relative to a false accept; reference prior; each rule with its cost-minimising band (0 to "
                      r"40 floors). Trial: sending every design to trial (cost $c_\mathrm{T}$) is cheapest. In brackets: "
                      r"the cost-minimising band of NN (floors).")


def s_between() -> str:
    b = read("qual_between_run.csv")
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        for m in ["NN", "M1sn", "M1s", "M2", "M5", "M7n"]:
            x = b[(b["relation"] == rel) & (b["method"] == m)].set_index("tau")
            cells = [f"{dist(x.loc[t, 'decisive_median'])} ({band(x.loc[t, 'band_median'])})" for t in
                     ("0.0", "1.0", "2.0", "3.0", "bound")]
            rows.append(f"{rel if m == 'NN' else ''} & {SHORT.get(m, m)} & " + " & ".join(cells))
        best = b[b["relation"] == rel].drop_duplicates("tau").set_index("tau")
        rows.append(r"& \emph{record rule best} & " + " & ".join(pct(best.loc[t, "share_record_rule_best"]) for t in
                                                                 ("0.0", "1.0", "2.0", "3.0", "bound")))
    head = r"Relation & Rule & $\tau=0$ & 1 & 2 & 3 & bound"
    return table(rows, "Decisive distance and guard band (floors, in brackets) with a between-run component added to "
                       "the truths", "tab:s-between", "ll" + "r" * 5, head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"Medians over 200 draws (bands over 50); $\tau$: standard deviation of the component (floors); bound: "
                      r"each characteristic's variation between series, $\tau=1.2$--$9.8/2.77$. Record rule best: share of "
                      r"draws in which NN, M1sn or M1n is the most decisive rule (\%).")


def s_crossfit() -> str:
    x = read("qual_crossfit.csv")
    rows = []
    for _, r in x.iterrows():
        if r["criterion"] == "step 6":
            if r["rule"] == "none qualifies":
                continue
            rows.append(f"{r['relation']} & step 6 & {r['selected_on']} & {SHORT.get(r['rule'], r['rule'])} & "
                        f"{dist(r['in_sample'])} & {dist(r['cross_fitted'])} & {band(r['band'])} & "
                        f"{pct(r['share_correct'])} & {pct(r['trial_rate'])}")
        else:
            crit = "decisive" if r["criterion"].startswith("resolution") else "safe"
            rows.append(f"{r['relation']} & {crit}, {r['pool']} & {r['selected_on']} & {SHORT.get(r['rule'], r['rule'])} & "
                        f"{dist(r['in_sample'])} & {dist(r['cross_fitted'])} & & & ")
    head = r"Relation & Criterion & Selected on & Rule & In sample & Other & $g$ & Corr. & T"
    return table(rows, "Rules and guard bands selected on one geometry and evaluated on the other", "tab:s-crossfit",
                 "llllrrrrr", head, colsep="2.4pt", place="p", size=r"\tabsizesmall",
                 note=r"Selection by the smallest decisive or safe distance among all rules or the pre-specified ones, or by "
                      r"the smallest decisive distance of step 6; for a new family, selected on one transfer. Other: the "
                      r"distance on the other geometry. Corr., T: share correct and trial rate (\%) there.")


def s_per_qc() -> str:
    p = read("qual_per_characteristic.csv")
    p = p[p["subset"].isin(SHARED)]
    rows = []
    for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
        for m in ["M0", "M1s", "M2", "M5", "M7n", "NN", "M1sn", "M3"]:
            x = p[(p["relation"] == rel) & (p["method"] == m)].set_index("subset")
            if x.empty:
                continue
            cells = [pair(x.loc[q], m) for q in SHARED]
            rows.append(f"{rel if m == 'M0' else ''} & {SHORT.get(m, m)} & " + " & ".join(cells))
    head = "Relation & Rule & " + " & ".join(LABEL[q].replace("Draw-in, ", "D-i ").replace(", cut", "") for q in SHARED)
    return table(rows, "Decisive/safe distances (floors) per characteristic", "tab:s-qc", "ll" + "r" * 7, head,
                 colsep="2pt", place="p", size=r"\tabsizesmall",
                 note=r"In the floor of the characteristic's geometry; a new family in the produced family's floor. 18 "
                      r"cases per characteristic with a sibling and for a new family, 6 interpolated, 12 extrapolated.")


def s_design() -> str:
    d = read("qual_design_level.csv")
    rows = []
    for m in ["M0", "M1s", "M2", "M5", "M7n", "NN", "M1sn", "NN+RM", "M3"]:
        cells = []
        for rel in ["sibling", "interpolation", "extrapolation", "new family"]:
            x = d[(d["relation"] == rel) & (d["method"] == m)]
            if x.empty:
                cells += ["--", "--"]
                continue
            x = x.iloc[0]
            cells += [f"{dist(x['design_decisive'])}/{dist(x['design_safe'])}",
                      f"{dist(x['marginal_decisive'])}/{dist(x['marginal_safe'])}"]
        rows.append(f"{SHORT.get(m, m)} & " + " & ".join(cells))
    head = (r" & \multicolumn{2}{c}{Sibling} & \multicolumn{2}{c}{Interpolated} & \multicolumn{2}{c}{Extrapolated} & "
            r"\multicolumn{2}{c}{New family} \\" "\n" r"\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}"
            "\n" r"Rule & Design & Marginal & Design & Marginal & Design & Marginal & Design & Marginal")
    return table(rows, "Design-level verdicts: a design meets only if all seven characteristics meet", "tab:s-design",
                 "l" + "r" * 8, head, colsep="2.4pt", place="p", size=r"\tabsizesmall",
                 note=r"Decisive/safe distances (floors). Design: requirements on every characteristic $\delta$ floors above "
                      r"its truth (adequate design) or one characteristic $\delta$ floors below and the others above (failing "
                      r"design), both sides weighted equally. Marginal: per characteristic, as in the main text.")


def s_fewshot() -> str:
    f = read("learn_fewshot.csv")
    rows = []
    for k in (1, 2, 3):
        for rel in ["all", "sibling", "interpolation", "extrapolation"]:
            x = f[(f["k"] == k) & (f["relation"] == rel)].set_index("method")
            if x.empty:
                continue
            cells = []
            for m in ["NN-target", "shift", "ICM", "ICM+sim"]:
                y = x.loc[m]
                cells.append(f"{dist(y['resolution_floors'])}" + ("" if m in ("NN-target", "shift") else f"/{dist(y['safe_floors'])}"))
            rows.append(f"{k if rel == 'all' else ''} & {rel} & {int(x['cases'].iloc[0])} & " + " & ".join(cells) +
                        f" & {pct(x.loc['ICM', 'coverage'])}")
    head = r"$k$ & Relation & Cases & NN in family & Shifted record & ICM & ICM+sim & Cov ICM"
    return table(rows, "Few-shot transfer to a new family with k produced alternatives of the target family",
                 "tab:s-fewshot", "rlrrrrrr", head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"Decisive (and safe) distances in the target family's floor over every subset of $k$ produced "
                      r"alternatives; relation of the judged alternative to the $k$. NN in family: nearest produced setting "
                      r"among the $k$; shifted record: the other family's $q_{95}$ at the same setting plus the median offset "
                      r"of the $k$; ICM: two-task GP with family intercepts and a free inter-family correlation; ICM+sim: "
                      r"with the nominal simulation in the mean. Cov: coverage of the ICM interval (\%).")


def s_validation_full() -> str:
    v = read("sim_validation.csv")
    rows = []
    for c in SHARED:
        for _, r in v[v["qc"] == c].iterrows():
            rows.append(f"{LABEL[c] if r['geometry'] == 'concave' and r['bhf_kN'] == 100 else ''} & {r['geometry']} & "
                        f"{int(r['bhf_kN'])} & {sig(r['measured_centre'], 4)} & {sig(r['sim_nominal'], 4)} & "
                        f"{sig(r['sim_min_over_friction'], 4)}--{sig(r['sim_max_over_friction'], 4)} & "
                        f"{'yes' if r['measured_inside_friction_range'] else 'no'} & {r['closest_mu']:.2f} & "
                        f"{r['residual_at_closest_floors']:.1f}")
    mc = read("sim_mc_friction.csv")
    head = r"Characteristic & Geometry & kN & Measured & Sim., $\mu=0.10$ & Sim. range & Inside & Closest $\mu$ & Residual"
    return table(rows, "The simulation dataset against the measurement per geometry and force", "tab:s-validation",
                 "llrrrrlrr", head, colsep="2.6pt", place="p", size=r"\tabsizesmall",
                 note=rf"Signed values in the unit of the characteristic, simulation at 0.99\,mm. Sim. range: over the "
                      rf"friction grid 0.05--0.15. Residual: simulation at the closest grid friction minus the measurement "
                      rf"(floors). Mc's friction fits end at the upper edge of the grid in {int(mc['at_upper_edge'].sum())} "
                      rf"of {len(mc)} within-family calibrations.")


def s_sim_checks() -> str:
    o = read("sim_oil_mapping.csv")
    d = read("sim_depth_offset.csv")
    t = read("meas_tooling_reference.csv")
    rows = []
    for _, r in o.iterrows():
        rows.append(f"oil film & {r['geometry']}, {int(r['bhf_kN'])}\\,kN, {LABEL[r['qc']].lower()} & "
                    f"{r['implied_mm_per_gm2']:.2f} & {r['within_run_mm_per_gm2']:.3f} & "
                    f"{r['between_patterns_min']:.2f} to {r['between_patterns_max']:.2f} & ")
    rows.append(r"\midrule \multicolumn{6}{@{}l}{\emph{Cup depth, flange rise and wall position at 15 mm depth (mm, simulation at nominal)}} \\")
    for _, r in d.iterrows():
        rows.append(f"depth & {r['geometry']}, {int(r['bhf_kN'])}\\,kN & {r['depth_sim_minus_measured']:.2f} & "
                    f"{r['flange_rise_measured']:.2f} / {r['flange_rise_sim']:.2f} & "
                    f"{r['wall_r15_measured_minus_sim']:.2f} & {r['press_bdc_sd_mm']:.3f}")
    rows.append(r"\midrule \multicolumn{6}{@{}l}{\emph{A dimension fixed by the tooling: cup width at 15 mm depth}} \\")
    for _, r in t.iterrows():
        rows.append(f"tooling & {r['geometry']} & {r['r_wx_cupwidth']:.2f} & {r['floor_cup_width_mm']:.3f} & "
                    f"{r['floor_wx_mm']:.3f} & {100 * r['lateral_scale_drift_bound']:.3f}")
    head = r"Check & Case & a & b & c & d"
    return table(rows, "Checks of the simulation's oil-film mapping, the cup-depth offset and the scanner's lateral scale",
                 "tab:s-checks", "llrrrr", head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"Oil film: a, change of draw-in per g/m$^2$ implied by the mapping and the simulated friction "
                      r"sensitivity (mm); b, within-run slope; c, slopes between the lubrication patterns. Depth: a, "
                      r"simulated minus measured depth; b, flange rise measured/simulated; c, wall position at 15\,mm depth, "
                      r"measured minus simulated (radius); d, standard deviation of the press position at bottom dead centre "
                      r"within the series. Tooling: a, correlation of the batch centres of flange width and cup width; b, c, "
                      r"floors of the cup width and the flange width (mm); d, bound of a lateral scale drift (\%).")


def s_measurement() -> str:
    m = read("meas_scan.csv")
    fp = read("panel_floor_protocol.csv").set_index(["qc", "geometry"])
    dr = read("sens_drift.csv").set_index("qc")
    rows = []
    for _, r in m.iterrows():
        rows.append(f"{r['alternative']} & {r['wy_minus_wx']:.2f} & {r['sd_wy'] / r['sd_wx']:.1f} & {r['r_wx_wy']:.2f} & "
                    f"{r['diag_difference']:.2f} & {r['N_minus_EW']:.2f} & {r['r_E_W']:.2f}")
    rows.append(r"\midrule \multicolumn{7}{@{}l}{\emph{Components of the floor, concave/convex}} \\")
    for c in SHARED:
        sb = "/".join(f"{fp.loc[(c, g), 'sigma_between_batch'] / fp.loc[(c, g), 'floor']:.2f}" for g in ("concave", "convex"))
        sw = "/".join(f"{fp.loc[(c, g), 'sigma_within_batch'] / fp.loc[(c, g), 'floor']:.2f}" for g in ("concave", "convex"))
        rows.append(f"{LABEL[c]} & $\\sigma_\\mathrm{{b}}/F$ {sb} & $\\sigma_\\mathrm{{w}}/F$ {sw} & drift "
                    f"{dr.loc[c, 'drift_inflation']:.1f} & & & ")
    head = r"Series & $W_y-W_x$ & $\sigma_y/\sigma_x$ & $r_{xy}$ & Diagonals & N$-$EW & $r_\mathrm{EW}$"
    return table(rows, "Redundancy of the scans per series, and the components of the floor", "tab:s-scan",
                 "lrrrrrr", head, colsep="3pt", place="p", size=r"\tabsizesmall",
                 note=r"$W_y-W_x$: flange width along minus across the scan lines (mm); $\sigma_y/\sigma_x$: ratio of their "
                      r"part-to-part standard deviations; $r_{xy}$: their correlation; diagonals: difference of the two "
                      r"flange diagonals (mm); N$-$EW: north wall angle minus the mean of east and west ($^\circ$); "
                      r"$r_\mathrm{EW}$: correlation of east and west. Components: $\sigma_\mathrm{b}$ between batch means, "
                      r"$\sigma_\mathrm{w}$ within batches, drift: floor over that of permuted series.")


MAIN_TABLES = {"floors": t_floors, "qcs": t_qcs, "distances": t_distances, "guards": t_guards, "further": t_further,
               "gp": t_gp, "crossing": t_crossing, "groups": t_groups, "validation": t_validation}
SUPP_TABLES = {"s-all": s_all_rules, "s-variants": s_variants, "s-strata": s_strata, "s-coverage": s_coverage,
               "s-coverage-qc": s_coverage_qc, "s-step6": s_step6, "s-guard-family": s_guard_family,
               "s-guard-oos": s_guard_oos, "s-prior": s_prior_width, "s-guard-qc": s_guard_qc, "s-costs": s_costs,
               "s-between": s_between, "s-crossfit": s_crossfit, "s-qc": s_per_qc, "s-design": s_design,
               "s-fewshot": s_fewshot, "s-validation": s_validation_full, "s-checks": s_sim_checks,
               "s-scan": s_measurement}


def main() -> None:
    for path, tables in ((MAIN, MAIN_TABLES), (SUPP, SUPP_TABLES)):
        if not path.exists():
            print(f"{path.name}: missing, skipped")
            continue
        text = path.read_text()
        for name, fn in tables.items():
            if f"%% BEGIN GENERATED {name}" not in text:
                print(f"{name}: no block in {path.name}, skipped")
                continue
            write_block(path, name, fn())
            print(f"{path.name} {name}: written")


if __name__ == "__main__":
    main()
