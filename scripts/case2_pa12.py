"""Second demonstration: build orientation in laser powder bed fusion of PA12.

EXPLORATORY; NOT USED IN THE PAPER. It was removed in the revision: a batch here (an orientation class
within a build) mixes six or seven orientations, so it is not a batch of one design as the floor requires;
builds are blocks shared by all classes; and the floor rests on 18 build-centre differences. A proper
version would take the floor from the eight identical anchor specimens per build (or from the residuals of
an orientation + build + position model). Kept for reference; run_all.sh does not run it.

Data: Leirmo and Semeniuta (2021), DataverseNO doi:10.18710/DHACHZ (CC0). One test artefact printed as 135
specimens in three builds on an EOSINT P395 (PA2200, 120 um layers): 37 build orientations (0-180 deg in
5-deg steps about one axis), each printed once in every build, plus eight anchor specimens per build; CMM
characteristics measured three times per specimen (the mean is used).

Design question: does a feature of the artefact, built in orientation class o, meet a requirement on the
95th percentile of its deviation? The alternatives are six orientation classes of 30 deg; a batch is one
class within one build (6-7 specimens), so the production floor is the ALPHA-quantile of the difference
between the build centres of one class, pooled over classes. There is no process simulation: the
design-stage evidence is the production record of the other orientation classes. Rules: M0 the nominal
geometry (zero deviation), M1 the median 95th percentile of the other classes, M2 the same with a conformal
margin, M5 a Gaussian process over the class's orientation. Each class is held out in turn, requirements are
placed at distances d (floors) from its true 95th percentile, and the decisive and safe distances are
computed as in decisions.py; the calibration budget uses every subset of the other classes.

Outputs: results/case2_floor.csv, case2_effects.csv, case2_resolution.csv, case2_budget.csv, summary_case2.md
"""

from __future__ import annotations

import io
import itertools
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parent))
from alternatives import ALPHA, floor_from  # noqa: E402
from common import CACHE, RESULTS, centre, group_centres  # noqa: E402
from decisions import CONF_LEVEL, D_GRID, beyond, conformal_margin, distance_table, verdicts  # noqa: E402

DATAVERSE = "https://dataverse.no/api/access/datafile/{}?format=original"
FILES = {"results.csv": 104153, "layout.csv": 104156, "characteristics.csv": 104163}
#: characteristic -> requirement statistic: 'abs' = |deviation from nominal| (dimensions), 'max' = value (tolerances)
QCS2 = {"Diameter_Cyl_8mm_Pos": "abs", "Diameter_Cyl_24mm_Pos": "abs", "Diameter_Cyl_8mm_Neg": "abs",
        "Diameter_Cyl_24mm_Neg": "abs", "Dist_HX1_1-4": "abs", "Cylindricity_Cyl_24mm_Pos": "max",
        "Flatness_Base_Plate": "max", "Position_Cyl_24mm_Pos": "max"}
LABEL2 = {"Diameter_Cyl_8mm_Pos": "Diameter, 8 mm pin", "Diameter_Cyl_24mm_Pos": "Diameter, 24 mm pin",
          "Diameter_Cyl_8mm_Neg": "Diameter, 8 mm hole", "Diameter_Cyl_24mm_Neg": "Diameter, 24 mm hole",
          "Dist_HX1_1-4": "Hexagon across flats", "Cylindricity_Cyl_24mm_Pos": "Cylindricity, 24 mm pin",
          "Flatness_Base_Plate": "Flatness, base plate", "Position_Cyl_24mm_Pos": "Position, 24 mm pin"}
CLASS_DEG = 30                       # width of an orientation class
GP_RESTARTS = 3


def fetch(name: str) -> Path:
    import requests

    path = CACHE / "ntnu_pa12" / name
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        r = requests.get(DATAVERSE.format(FILES[name]), timeout=300)
        r.raise_for_status()
        path.write_bytes(r.content)
    return path


def load() -> pd.DataFrame:
    """Specimen x characteristic table: orientation class, build, requirement statistic."""
    res = pd.read_csv(io.BytesIO(fetch("results.csv").read_bytes()), low_memory=False, encoding="latin-1")
    lay = pd.read_csv(fetch("layout.csv"), sep=";", encoding="utf-8-sig")
    res = res[res["Characteristic"].isin(QCS2)]
    g = res.groupby(["Characteristic", "K53 Order number"]).agg(
        value=("K1 Measured value", "mean"), nominal=("K2101 Nominal value", "first")).reset_index()
    ids = g["K53 Order number"].str.extract(r"Build(\d+)_#(\d+)").astype(int)
    g["build"], g["part_index"] = ids[0], ids[1]
    g = g.merge(lay[["build", "part_index", "angle", "z_pos"]], on=["build", "part_index"])
    g = g[g["angle"] >= 0].copy()                                 # anchor specimens (-90 deg) are not alternatives
    g["deviation"] = g["value"] - g["nominal"]
    g["y"] = [abs(d) if QCS2[c] == "abs" else v for c, d, v in zip(g["Characteristic"], g["deviation"], g["value"])]
    g["alternative"] = (np.minimum(g["angle"] // CLASS_DEG, 180 // CLASS_DEG - 1) * CLASS_DEG).astype(int)
    return g.rename(columns={"Characteristic": "qc"})


def floors(g: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for qc, h in g.groupby("qc"):
        bm = group_centres(h.assign(batch=h["build"]), ["alternative", "batch"], ["y"])
        rows.append({"qc": qc, "floor": floor_from(bm, "y", ALPHA), "n_batches": len(bm),
                     "sd_within": float(h.groupby("alternative")["y"].std().median()),
                     "measurement_note": "mean of three CMM repetitions"})
    return pd.DataFrame(rows)


def alt_table(g: pd.DataFrame) -> pd.DataFrame:
    t = g.groupby(["qc", "alternative"]).agg(q95=("y", lambda v: float(np.quantile(v, 0.95))),
                                             centre=("y", lambda v: centre(v.to_numpy())),
                                             angle=("angle", "mean"), n=("y", "size")).reset_index()
    return t


def gp_interval(tq: pd.DataFrame, calib: list[int], target: int) -> tuple[float, float]:
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel

    X = (tq.loc[calib, "angle"].to_numpy() / 90.0)[:, None]
    gp = GaussianProcessRegressor(ConstantKernel(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-1, 1e2)) +
                                  WhiteKernel(1e-2, (1e-6, 1e1)), normalize_y=True,
                                  n_restarts_optimizer=GP_RESTARTS, random_state=0)
    gp.fit(X, tq.loc[calib, "q95"].to_numpy())
    mu, sd = gp.predict(np.array([[tq.loc[target, "angle"] / 90.0]]), return_std=True)
    z = norm.ppf(0.5 + CONF_LEVEL / 2)
    return float(mu[0] - z * sd[0]), float(mu[0] + z * sd[0])


def rule_intervals(tq: pd.DataFrame, calib: list[int], target: int) -> dict:
    q = tq.loc[calib, "q95"].to_numpy()
    med = float(np.median(q))
    marg = conformal_margin(np.abs(q - med), CONF_LEVEL)
    iv = {"M0": (0.0, 0.0), "M1": (med, med), "M2": (med - marg, med + marg)}
    if len(calib) >= 2:
        iv["M5"] = gp_interval(tq, calib, target)
    return iv


def verdict_rows(t: pd.DataFrame, fl: pd.Series, subsets: bool = False) -> list[dict]:
    rows = []
    for qc, tq in t.groupby("qc"):
        tq = tq.set_index("alternative")
        F = float(fl.loc[qc])
        for a in tq.index:
            others = [b for b in tq.index if b != a]
            cands = [others] if not subsets else [list(s) for k in range(1, len(others) + 1)
                                                  for s in itertools.combinations(others, k)]
            reqs = tq.loc[a, "q95"] + D_GRID * F
            for calib in cands:
                for m, (lo, hi) in rule_intervals(tq, calib, a).items():
                    for d, v in zip(D_GRID, verdicts(lo, hi, reqs)):
                        rows.append({"scope": "within", "method": m, "qc": qc, "alternative": a, "k": len(calib),
                                     "d": float(d), "verdict": v, "adequate": bool(d >= 0)})
    return rows


def main() -> None:
    warnings.filterwarnings("ignore")
    g = load()
    fl = floors(g)
    fl.to_csv(RESULTS / "case2_floor.csv", index=False)
    F = fl.set_index("qc")["floor"]
    t = alt_table(g)
    eff = []
    for qc, tq in t.groupby("qc"):
        c = tq.set_index("alternative")["centre"]
        for a, b in itertools.combinations(c.index, 2):
            eff.append({"qc": qc, "a": a, "b": b, "esr": abs(c[a] - c[b]) / F[qc]})
    eff = pd.DataFrame(eff)
    eff.to_csv(RESULTS / "case2_effects.csv", index=False)

    d = pd.DataFrame(verdict_rows(t, F))
    res = distance_table(d)
    res.to_csv(RESULTS / "case2_resolution.csv", index=False)
    db = pd.DataFrame(verdict_rows(t, F, subsets=True))
    bud = []
    for (k, m), h in db.groupby(["k", "method"]):
        h = h.assign(correct=((h["verdict"] == "meets") & h["adequate"]) | ((h["verdict"] == "fails") & ~h["adequate"]))
        h["not_wrong"] = h["correct"] | (h["verdict"] == "uncertain")
        at10 = h[h["d"].abs() == 10]
        bud.append({"k": k, "method": m, "resolution_floors": beyond(h.groupby(h["d"].abs())["correct"].mean()),
                    "safe_floors": beyond(h.groupby(h["d"].abs())["not_wrong"].mean()),
                    "wrong_at_10": float((~at10["not_wrong"]).mean()),
                    "uncertain_at_10": float((at10["verdict"] == "uncertain").mean())})
    bud = pd.DataFrame(bud)
    bud.to_csv(RESULTS / "case2_budget.csv", index=False)
    share = eff.assign(res=eff["esr"] >= 1).groupby("qc")["res"].agg(["sum", "size"])
    lines = ["# Second demonstration: build orientation in powder bed fusion of PA12", "",
             f"Specimens: {g['part_index'].groupby([g['build'], g['part_index']]).ngroups} "
             f"(anchors excluded); orientation classes of {CLASS_DEG} deg; characteristics: {len(QCS2)}.", "",
             "## Floor (batch = class within a build)", "", fl.round(4).to_markdown(index=False), "",
             "## Orientation-class pairs with ESR >= 1", "", share.to_markdown(), "",
             "## Decisive / safe distances (floors), held-out class, within", "",
             res[res["qc"] == "all"].to_markdown(index=False), "",
             res.pivot_table(index="qc", columns="method", values=["resolution_floors", "safe_floors"]).to_markdown(),
             "", "## Calibration budget", "", bud.round(3).to_markdown(index=False)]
    (RESULTS / "summary_case2.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
