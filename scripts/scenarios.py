"""Requirement scenarios from general tolerances (ISO 2768).

decisions.py scores the rules against requirements placed at known distances
from the truth. Here the requirements are those a drawing would carry under
general tolerances, so that the verdicts can be read as real design-stage
decisions:

* wall angle after drawing: ISO 2768-1 angular tolerance on the design wall
  angle of the tool (concave 20 deg, convex 10 deg); the shorter leg is the
  wall, about 28 mm high, so the row 'over 10 up to 50 mm' applies. Every part
  is steeper than the design angle, so the upper limit design + T is the one
  that binds;
* arm angle after cutting: the arms are taken as nominally flat, |angle| <= T,
  same row of ISO 2768-1;
* bottom dome after cutting: ISO 2768-2 flatness of the bottom over the
  evaluation circle of 80 mm (nominal length over 30 up to 100 mm),
  |sag| <= T.

For every characteristic and tolerance class the truth is whether an
alternative's 95th percentile meets the limit; the verdict of every rule and
calibration scope comes from its interval in dec_intervals.csv.

The values were checked against the text of ISO 2768-1:1989 and ISO 2768-2:1989
and several independent tables (f and m share one row for angles). ISO 2768-1
covers parts formed from sheet metal; ISO 2768-2 mainly addresses machined
features and was withdrawn in 2021 (replaced by ISO 22081, which has no class
table), so its flatness classes serve as a representative general flatness
requirement for the nominally flat cup bottom. DIN 6930-2 (stamped parts) has
no flatness tolerance and refers bent angles to DIN 6935 (+-2 deg up to 30 mm),
which equals class v for the wall.

Outputs: results/scen_truth.csv, scen_scores.csv, summary_scenarios.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import RESULTS  # noqa: E402

DESIGN_WALL_DEG = {"concave": 20.0, "convex": 10.0}          # DDACS wall angle of the RDDAC tools
ANGULAR_10_50 = {"f/m": 0.5, "c": 1.0, "v": 2.0}             # ISO 2768-1, shorter leg over 10 up to 50 mm (deg)
FLATNESS_30_100 = {"H": 0.1, "K": 0.2, "L": 0.4}             # ISO 2768-2, nominal length over 30 up to 100 mm (mm)
SCENARIOS = [("wall_op10", ANGULAR_10_50, "ISO 2768-1"), ("arm_op20", ANGULAR_10_50, "ISO 2768-1"),
             ("dome_op20", FLATNESS_30_100, "ISO 2768-2")]


def limit(qc: str, geometry: str, tol: float) -> float:
    return DESIGN_WALL_DEG[geometry] + tol if qc == "wall_op10" else tol


def main() -> None:
    iv = pd.read_csv(RESULTS / "dec_intervals.csv")
    truth, verdicts = [], []
    for qc, classes, std in SCENARIOS:
        sub = iv[iv["qc"] == qc]
        for cls, tol in classes.items():
            R = np.array([limit(qc, g, tol) for g in sub["geometry"]])
            v = np.where(sub["hi"] <= R, "meets", np.where(sub["lo"] > R, "fails", "uncertain"))
            meets = sub["real_q95"].to_numpy() <= R
            verdicts.append(sub[["scope", "calibration", "alternative", "geometry", "qc", "method"]].assign(
                standard=std, tol_class=cls, limit=R, verdict=v, adequate=meets))
            alts = sub.drop_duplicates("alternative")
            truth += [{"qc": qc, "standard": std, "tol_class": cls, "alternative": a, "geometry": g,
                       "real_q95": q, "limit": limit(qc, g, tol), "meets": q <= limit(qc, g, tol),
                       "margin_floors": (limit(qc, g, tol) - q) / f}
                      for a, g, q, f in zip(alts["alternative"], alts["geometry"], alts["real_q95"], alts["floor"])]
    truth = pd.DataFrame(truth)
    truth.to_csv(RESULTS / "scen_truth.csv", index=False)
    v = pd.concat(verdicts, ignore_index=True)
    v["correct"] = ((v["verdict"] == "meets") & v["adequate"]) | ((v["verdict"] == "fails") & ~v["adequate"])
    v["false_accept"] = (v["verdict"] == "meets") & ~v["adequate"]
    v["false_reject"] = (v["verdict"] == "fails") & v["adequate"]
    v["uncertain"] = v["verdict"] == "uncertain"
    cols = ["correct", "false_accept", "false_reject", "uncertain"]
    sc = v.groupby(["scope", "method"])[cols].mean().reset_index()
    sc_cls = v.groupby(["scope", "method", "qc", "tol_class"])[cols].mean().reset_index()
    sc.assign(level="all").to_csv(RESULTS / "scen_scores.csv", index=False)
    sc_cls.to_csv(RESULTS / "scen_scores_by_class.csv", index=False)
    tt = truth.pivot_table(index="qc", columns="tol_class", values="meets", aggfunc="sum")
    lines = ["# Requirement scenarios from general tolerances", "",
             "Number of the 18 alternatives whose 95th percentile meets the limit:", "", tt.to_markdown(), "",
             "## Verdicts over all scenarios (correct / false accept / false reject / uncertain)", "",
             sc.pivot_table(index="method", columns="scope", values="correct").round(3).to_markdown(), "",
             sc.round(3).to_markdown(index=False), "",
             "## Per characteristic and class, within the family", "",
             sc_cls[sc_cls["scope"] == "within"].round(3).to_markdown(index=False)]
    (RESULTS / "summary_scenarios.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
