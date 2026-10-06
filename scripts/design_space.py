"""Design space from the DDACS corners: sensitivities and minimum resolvable change.

DDACS varies the geometry of each base shape between two corners in which
curvature radius, bottom radius and wall angle move together; the RDDAC tool
is a third point (the concave tool lies midway between its corners; the
convex tool differs from its upper corner only in wall angle). Process
parameters are varied fully. At matched process conditions (material scaling
1.0, sheet thickness 0.98-0.99 mm, blank-holder force 100/300/500 kN, all
friction values) this script estimates, per quality characteristic (QC):

* the simulated sensitivity to each design factor (geometric steps, blank-
  holder force, friction, sheet thickness) from paired differences at equal
  process conditions;
* the real sensitivity where the experiments vary the factor (blank-holder
  force between cells; sheet thickness within a series);
* the minimum resolvable change: production floor (alternatives.py) divided
  by the sensitivity. With the simulation as the only evidence, the
  simulation's own uncertainty (the calibrated margin of decisions.py) is
  added to the floor;
* the accuracy of a Gaussian-process surrogate of the simulations
  (leave-one-out over process conditions) relative to the production floor;
* the surrogate scored as a decision rule: its leave-one-out prediction at the
  nominal sheet thickness and friction of every alternative replaces the
  nominal simulation in M0 and, with a produced sibling, in M1 (decisions.py).

Outputs: results/ds_sensitivity.csv, ds_surrogate.csv, ds_surrogate_rule.csv, summary_design_space.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from alternatives import within_slope  # noqa: E402
from common import OIL_MAX_GM2, OIL_MIN_GM2, RESULTS, group_centres, oil_to_friction  # noqa: E402
from qc import SHARED, parts_qc, sims_qc  # noqa: E402

THICKNESS = [0.98, 0.99]
GEOM_POINTS = {   # geometry -> {label: (curvature radius, bottom radius, wall angle)}
    "concave": {"low": (50.0, 5.0, 10.0), "tool": (100.0, 7.5, 20.0), "high": (150.0, 10.0, 30.0)},
    "convex": {"low": (100.0, 5.0, 10.0), "tool": (150.0, 10.0, 10.0), "high": (150.0, 10.0, 30.0)},
}
GP_SEED = 0


def load_sims() -> pd.DataFrame:
    s = [sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))]
    if (RESULTS / "features_ddacs_corners.csv").exists():
        s.append(sims_qc(pd.read_csv(RESULTS / "features_ddacs_corners.csv")))
    s = pd.concat(s, ignore_index=True)
    s = s[(s["material_scaling_factor"] == 1.0) & s["sheet_metal_thickness"].isin(THICKNESS)]
    s["point"] = None
    for geo, pts in GEOM_POINTS.items():
        for lab, (cr, br, wa) in pts.items():
            m = (s["geometry"] == geo) & (s["curvature_radius"] == cr) & (s["bottom_radius"] == br) & \
                (s["wall_angle"] == wa)
            s.loc[m, "point"] = lab
    return s.dropna(subset=["point"])


def paired_step(s: pd.DataFrame, geo: str, a: str, b: str, qc: str) -> pd.Series:
    """QC(b) - QC(a) for equal process conditions (force, friction, thickness)."""
    key = ["bhf_kN", "friction_coefficient", "sheet_metal_thickness"]
    A = s[(s["geometry"] == geo) & (s["point"] == a)].set_index(key)[qc]
    B = s[(s["geometry"] == geo) & (s["point"] == b)].set_index(key)[qc]
    return (B - A).dropna()


def process_slope(s: pd.DataFrame, geo: str, qc: str, x: str) -> float:
    """Slope of a QC on a process factor at the tool geometry, pooled over the other factors."""
    g = s[(s["geometry"] == geo) & (s["point"] == "tool")]
    others = [c for c in ["bhf_kN", "friction_coefficient", "sheet_metal_thickness"] if c != x]
    num = den = 0.0
    for _, h in g.groupby(others):
        h = h[[x, qc]].dropna()
        if len(h) >= 2:
            xc = h[x] - h[x].mean()
            num += float((xc * (h[qc] - h[qc].mean())).sum())
            den += float((xc ** 2).sum())
    return num / den if den else np.nan


def surrogate_loo(s: pd.DataFrame, geo: str, qc: str) -> tuple[dict, dict]:
    """Leave-one-out RMSE of a GP surrogate of the simulations over force, friction and sheet thickness at the
    tool geometry, and its leave-one-out predictions at the nominal thickness and friction of each force."""
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel

    from decisions import NOMINAL_FRICTION, NOMINAL_THICKNESS

    g = s[(s["geometry"] == geo) & (s["point"] == "tool")].dropna(subset=[qc])
    X = g[["bhf_kN", "friction_coefficient", "sheet_metal_thickness"]].to_numpy(float)
    X = (X - X.mean(0)) / X.std(0)
    y = g[qc].to_numpy(float)
    if len(y) < 10:
        return {"rmse_loo": np.nan, "n": len(y)}, {}
    nominal = np.isclose(g["sheet_metal_thickness"], NOMINAL_THICKNESS) & \
        np.isclose(g["friction_coefficient"], NOMINAL_FRICTION)
    kern = ConstantKernel(1.0) * RBF([1.0, 1.0, 1.0]) + WhiteKernel(1e-3)
    err, at_nominal = [], {}
    for i in range(len(y)):
        m = np.ones(len(y), bool)
        m[i] = False
        gp = GaussianProcessRegressor(kern, normalize_y=True, random_state=GP_SEED).fit(X[m], y[m])
        pred = gp.predict(X[i:i + 1])[0]
        err.append(pred - y[i])
        if nominal[i]:
            at_nominal[int(g["bhf_kN"].iloc[i])] = float(pred)
    return {"rmse_loo": float(np.sqrt(np.mean(np.square(err)))), "n": len(y)}, at_nominal


def surrogate_rule(pred: dict) -> pd.DataFrame:
    """The surrogate in place of the nominal simulation: M0 (no production evidence) and M1 with a produced
    sibling (median offset of the other alternatives of the geometry), scored with the exact distances of
    decisions.py against the same truths and floors as the simulation."""
    import decisions as D
    from qc import QCS

    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    floors = D.load_floors()
    t["surrogate"] = [abs(pred[(g, int(b), q)]) if QCS[q][2] == "abs" else pred[(g, int(b), q)]
                      for g, b, q in zip(t["geometry"], t["bhf_kN"], t["qc"])]
    t["floor"] = [floors[(q, g)] for q, g in zip(t["qc"], t["geometry"])]
    rows = []
    for col, label in (("sim_nominal", "simulation"), ("surrogate", "surrogate")):
        rows.append({"rule": "M0", "source": label, **D.distance_pair(*D.exclusion(t.assign(lo=t[col], hi=t[col])))})
        m1 = []
        for (geo, qc), g in t.groupby(["geometry", "qc"]):
            for a in g["alternative"]:
                c = g[g["alternative"] != a]
                v = float(g.loc[g["alternative"] == a, col].iloc[0] + np.median(c["real_q95"] - c[col]))
                m1.append({**g[g["alternative"] == a].iloc[0].to_dict(), "lo": v, "hi": v})
        rows.append({"rule": "M1 (sibling produced)", "source": label,
                     **D.distance_pair(*D.exclusion(pd.DataFrame(m1)))})
    return pd.DataFrame(rows)


def main() -> None:
    s = load_sims()
    floor = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    margin = None
    if (RESULTS / "dec_margins.csv").exists():
        margin = pd.read_csv(RESULTS / "dec_margins.csv").set_index("qc")["margin"]
    parts = parts_qc(pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False))
    rows, surr, nominal_pred = [], [], {}
    for geo in GEOM_POINTS:
        pg = parts[parts["geometry"] == geo]
        cell = group_centres(pg, ["bhf_kN", "oil_type"], SHARED).reset_index()
        for qc in SHARED:
            F = float(floor.loc[qc, f"floor_{geo}"]) if f"floor_{geo}" in floor.columns else float(floor.loc[qc, "floor"])
            E = float(margin.loc[qc]) if margin is not None and qc in margin.index else np.nan
            for a, b, unit in (("low", "tool", "step"), ("tool", "high", "step")):
                d = paired_step(s, geo, a, b, qc)
                if d.empty:
                    continue
                rows.append({"geometry": geo, "qc": qc, "factor": f"geometry {a}->{b}", "unit": unit,
                             "sim_sensitivity": float(d.median()), "sim_sens_sd": float(d.std()),
                             "real_sensitivity": np.nan, "floor": F,
                             "resolvable_steps_real": abs(float(d.median())) / F, "n_pairs": len(d)})
            for x, unit, scale in (("bhf_kN", "per 100 kN", 100.0), ("friction_coefficient", "per 0.01", 0.01),
                                   ("sheet_metal_thickness", "per 10 um", 0.01)):
                ss = process_slope(s, geo, qc, x) * scale
                rs = np.nan
                if x == "bhf_kN":
                    sl = [np.polyfit(h["bhf_kN"].astype(float), h[qc], 1)[0] for _, h in cell.groupby("oil_type")
                          if h[qc].notna().sum() >= 2]
                    rs = float(np.mean(sl)) * scale if sl else np.nan
                elif x == "sheet_metal_thickness":
                    rs = within_slope(pg, qc, "sheet_um") * 10.0          # per 10 um
                elif x == "friction_coefficient":
                    # friction equivalent of the measured oil film (rddac mapping), within each series;
                    # only parts inside the unclamped oil range carry information
                    h = pg[(pg["oil_gm2"] > OIL_MIN_GM2) & (pg["oil_gm2"] < OIL_MAX_GM2)].copy()
                    h["fc_equiv"] = [oil_to_friction(o) for o in h["oil_gm2"]]
                    rs = within_slope(h, qc, "fc_equiv") * scale
                rows.append({"geometry": geo, "qc": qc, "factor": x, "unit": unit, "sim_sensitivity": ss,
                             "sim_sens_sd": np.nan, "real_sensitivity": rs, "floor": F,
                             "mrc_real_floor": F / abs(rs) if rs and np.isfinite(rs) else np.nan,
                             "mrc_sim_floor": F / abs(ss) if ss else np.nan,
                             "mrc_sim_floor_plus_margin": (F + E) / abs(ss) if ss and np.isfinite(E) else np.nan})
            res, at_nominal = surrogate_loo(s, geo, qc)
            surr.append({"geometry": geo, "qc": qc, **res, "floor": F, "rmse_over_floor": res["rmse_loo"] / F})
            nominal_pred.update({(geo, bhf, qc): v for bhf, v in at_nominal.items()})
    sens = pd.DataFrame(rows)
    sens.to_csv(RESULTS / "ds_sensitivity.csv", index=False)
    sg = pd.DataFrame(surr)
    sg.to_csv(RESULTS / "ds_surrogate.csv", index=False)
    rule = surrogate_rule(nominal_pred)
    rule.to_csv(RESULTS / "ds_surrogate_rule.csv", index=False)
    lines = ["# Design space from the DDACS corners", "",
             f"Simulations used: {len(s)} (material scaling 1.0; thickness {THICKNESS}).", "",
             "## Sensitivities and minimum resolvable change", "", sens.round(4).to_markdown(index=False), "",
             "## Gaussian-process surrogate, leave-one-out error over process conditions", "",
             sg.round(4).to_markdown(index=False), "",
             "## The surrogate as a decision rule (in place of the nominal simulation; floors)", "",
             rule.round(2).to_markdown(index=False)]
    (RESULTS / "summary_design_space.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
