"""Requirement scenarios from general angular tolerances (ISO 2768-1).

decisions.py scores the rules against requirements placed at known distances from the truth. Here the
requirements are those a drawing would carry under general angular tolerances, so that the verdicts can be
read as design-stage decisions with realistic margins:

* wall angle after drawing (mean of the east and west walls): ISO 2768-1 angular tolerance on the design
  wall angle of the tool (concave 20 deg, convex 10 deg). The wall, about 28 mm high, is the shorter leg,
  so the row 'over 10 up to 50 mm' applies (f/m 0.5, c 1, v 2 deg). Every part is steeper than the design
  angle, so the upper limit design + T binds;
* arm angle after cutting (mean of the four arms): the arms are nominally flat, |angle| <= T. The flat arm
  is the shorter leg; its measured length plus the two 1 mm end margins is about 18 mm on the concave and
  9 mm on the convex cups (ARM_LEG_MM), so the rows 'over 10 up to 50 mm' and 'up to 10 mm' (f/m 1, c 1.5,
  v 3 deg) apply.

ISO 2768-1 covers parts formed from sheet metal; a drawing of a deep-drawn part would normally carry
profile and position tolerances to datums (ISO 1101), which the data do not allow to evaluate. The
flatness classes of ISO 2768-2 (withdrawn in 2021) are not used: the dome sag of a fitted paraboloid is not
a minimum-zone flatness. A general tolerance applies to every feature, whereas the characteristics are
means over sides; the script counts the decisions whose truth would change if the worst side were decided.

For every characteristic, tolerance class and alternative the truth is whether the alternative's 95th
percentile meets the limit; the verdict of every rule and scope comes from its interval in
dec_intervals.csv. Rates are reported over all decisions, conditional on the truth (false accepts among
failing alternatives, false rejects among adequate ones) and stratified by the distance of the limit from
the truth in floors. The expected cost per decision, c_FA * P(false accept) + c_FR * P(false reject) +
c_T * P(trial), is compared between rules over a range of trial costs.

Outputs: results/scen_truth.csv, scen_scores.csv, scen_strata.csv, scen_cost.csv, scen_cost_map.csv,
summary_scenarios.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS  # noqa: E402

DESIGN_WALL_DEG = {"concave": 20.0, "convex": 10.0}          # DDACS wall angle of the RDDAC tools
ANGULAR = {"10-50": {"f/m": 0.5, "c": 1.0, "v": 2.0},        # ISO 2768-1, length of the shorter leg (mm)
           "0-10": {"f/m": 1.0, "c": 1.5, "v": 3.0}}
ARM_LEG_MM = {"concave": 18.0, "convex": 8.8}                 # measured flat length + 2 x 1 mm margins
STRATA = [(0, 5), (5, 10), (10, np.inf)]
C_FA, C_FR = 1.0, 0.5                                          # costs relative to a false accept
C_TRIAL = [0.02, 0.05, 0.1, 0.2, 0.3, 0.5]
C_FR_MAP = [0.25, 0.5, 1.0, 2.0]                               # sensitivity map over the false-reject cost


def row_of(qc: str, geometry: str) -> str:
    leg = 28.0 if qc == "wall_op10" else ARM_LEG_MM[geometry]
    return "0-10" if leg <= 10 else "10-50"


def limit(qc: str, geometry: str, cls: str) -> float:
    tol = ANGULAR[row_of(qc, geometry)][cls]
    return DESIGN_WALL_DEG[geometry] + tol if qc == "wall_op10" else tol


def per_side_truth(f: pd.DataFrame) -> pd.DataFrame:
    """q95 of the worst side (largest east/west wall angle; largest |arm angle| of four) per alternative."""
    f = f[f["status"] == "ok"]
    alt = f["geometry"] + "/" + f["bhf_kN"].astype(str) + "/" + f["oil_type"]
    worst = pd.DataFrame({"alternative": alt, "geometry": f["geometry"],
                          "wall_op10": f[["op10_wall_angle_E_deg", "op10_wall_angle_W_deg"]].max(axis=1),
                          "arm_op20": f[[f"op20_theta_{s}_deg" for s in "EWSN"]].abs().max(axis=1)})
    return worst.groupby(["alternative", "geometry"])[["wall_op10", "arm_op20"]].quantile(0.95).reset_index()


def rates(v: pd.DataFrame, by: list[str]) -> pd.DataFrame:
    g = v.groupby(by)
    out = g[["correct", "false_accept", "false_reject", "uncertain"]].mean()
    out["n"] = g.size()
    out["false_accept_given_fails"] = g.apply(lambda h: h.loc[~h["adequate"], "false_accept"].mean(),
                                              include_groups=False)
    out["false_reject_given_meets"] = g.apply(lambda h: h.loc[h["adequate"], "false_reject"].mean(),
                                              include_groups=False)
    out["n_failing"] = g.apply(lambda h: int((~h["adequate"]).sum()), include_groups=False)
    return out.reset_index()


def main() -> None:
    iv = pd.read_csv(RESULTS / "dec_intervals.csv")
    worst = per_side_truth(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False)).set_index("alternative")
    truth, verdicts = [], []
    for qc in ("wall_op10", "arm_op20"):
        sub = iv[iv["qc"] == qc]
        for cls in ("f/m", "c", "v"):
            R = np.array([limit(qc, g, cls) for g in sub["geometry"]])
            v = np.where(sub["hi"] <= R, "meets", np.where(sub["lo"] > R, "fails", "uncertain"))
            verdicts.append(sub[["scope", "calibration", "relation", "alternative", "geometry", "qc", "method"]].assign(
                tol_class=cls, limit=R, verdict=v, adequate=sub["real_q95"].to_numpy() <= R,
                margin_floors=(R - sub["real_q95"].to_numpy()) / sub["floor"].to_numpy()))
            alts = sub.drop_duplicates("alternative")
            for a, g, q, F in zip(alts["alternative"], alts["geometry"], alts["real_q95"], alts["floor"]):
                L = limit(qc, g, cls)
                truth.append({"qc": qc, "tol_class": cls, "row_mm": row_of(qc, g), "alternative": a, "geometry": g,
                              "real_q95": q, "limit": L, "meets": q <= L, "margin_floors": (L - q) / F,
                              "worst_side_q95": float(worst.loc[a, qc]), "worst_side_meets": worst.loc[a, qc] <= L})
    truth = pd.DataFrame(truth)
    truth.to_csv(RESULTS / "scen_truth.csv", index=False)
    v = pd.concat(verdicts, ignore_index=True)
    v["correct"] = ((v["verdict"] == "meets") & v["adequate"]) | ((v["verdict"] == "fails") & ~v["adequate"])
    v["false_accept"] = (v["verdict"] == "meets") & ~v["adequate"]
    v["false_reject"] = (v["verdict"] == "fails") & v["adequate"]
    v["uncertain"] = v["verdict"] == "uncertain"
    v["stratum"] = pd.cut(v["margin_floors"].abs(), [s[0] for s in STRATA] + [np.inf], right=False,
                          labels=[f"{a:g}-{b:g}" for a, b in STRATA])
    sc = rates(v, ["scope", "method"])
    sc.to_csv(RESULTS / "scen_scores.csv", index=False)
    st = rates(v, ["scope", "method", "stratum"])
    st.to_csv(RESULTS / "scen_strata.csv", index=False)
    cost = []
    for (scope, method), g in sc.groupby(["scope", "method"]):
        for ct in C_TRIAL:
            r = g.iloc[0]
            cost.append({"scope": scope, "method": method, "c_trial": ct,
                         "cost": C_FA * r["false_accept"] + C_FR * r["false_reject"] + ct * r["uncertain"]})
    cost = pd.DataFrame(cost)
    cost.to_csv(RESULTS / "scen_cost.csv", index=False)
    cmap = []                                       # cheapest rule(s) over false-reject and trial costs
    core = sc[sc["scope"].isin(["within", "setting", "transfer"])]
    trial = pd.DataFrame([{"scope": sc_, "method": "trial", "false_accept": 0.0, "false_reject": 0.0, "uncertain": 1.0}
                          for sc_ in ["within", "setting", "transfer"]])
    core = pd.concat([core, trial], ignore_index=True)    # current practice: a physical trial for every design
    for scope, g in core.groupby("scope"):
        for cfr in C_FR_MAP:
            for ct in C_TRIAL:
                c = C_FA * g["false_accept"] + cfr * g["false_reject"] + ct * g["uncertain"]
                best_rules = g.loc[np.isclose(c, c.min()), "method"]
                cmap.append({"scope": scope, "c_fr": cfr, "c_trial": ct, "cost": float(c.min()),
                             "cheapest": "/".join(sorted(best_rules))})
    cmap = pd.DataFrame(cmap)
    cmap.to_csv(RESULTS / "scen_cost_map.csv", index=False)
    best = cost.loc[cost.groupby(["scope", "c_trial"])["cost"].idxmin()]
    n_dec = len(truth)
    changed = int((truth["meets"] != truth["worst_side_meets"]).sum())
    lines = ["# Requirement scenarios from general angular tolerances", "",
             f"{n_dec} decisions (2 characteristics x 3 classes x 18 alternatives); "
             f"{int((~truth['meets']).sum())} with a failing alternative; limit within 5 floors of the truth in "
             f"{int((truth['margin_floors'].abs() < 5).sum())}, within 10 in {int((truth['margin_floors'].abs() < 10).sum())}. "
             f"Deciding the worst side instead of the mean would change the truth in {changed} decisions.", "",
             "Alternatives meeting the limit:", "",
             truth.pivot_table(index="qc", columns="tol_class", values="meets", aggfunc="sum").to_markdown(), "",
             "## Rates over all decisions", "", sc.round(3).to_markdown(index=False), "",
             "## Rates by the distance of the limit from the truth (floors)", "",
             st[st["scope"].isin(["within", "setting", "transfer"])].round(3).to_markdown(index=False), "",
             f"## Expected cost per decision (c_FA = {C_FA:g}, c_FR = {C_FR:g}): cheapest rule per trial cost", "",
             best.round(4).to_markdown(index=False), "",
             "## Cheapest rule(s) over false-reject and trial costs (c_FA = 1)", "",
             cmap.pivot_table(index=["scope", "c_fr"], columns="c_trial", values="cheapest", aggfunc="first")
             .to_markdown()]
    (RESULTS / "summary_scenarios.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:12]))


if __name__ == "__main__":
    main()
