"""The simulation against the produced process, and the measurement behind the floor.

Simulation (DDACS, 396 simulations of the RDDAC tools at 0.95-1.00 mm and friction 0.05-0.15):
 1. Validation: measured centre per characteristic, geometry and force (signed, physical units) against the
    simulation at the nominal thickness (0.99 mm) and friction (0.10), the range over the friction grid, and the
    grid friction closest to the measurement; with the extraction noise of the simulated characteristic.
 2. Friction fits of Mc: the friction coefficient calibrated per lubrication pattern for every calibration set of
    decisions.py, and how many end at an edge of the grid.
 3. Cup-depth offset: measured and simulated depth with the flange inclination and rise (an upper bound of what a
    different flange inclination adds to the median flange depth) and the wall position at 15 mm depth.
 4. Oil film to friction: the change of draw-in per g/m2 of oil that the dataset's mapping implies through the
    simulated friction sensitivity, against the within-run slope (pooled within each series) and the slopes
    between the lubrication patterns of one setting.
 5. Envelope over the measured incoming variation: M0w, M2 and M5 with the envelope taken over the grid values
    covering the 5th-95th percentiles of the parts' sheet thickness and mapped friction (per pattern).
Measurement (single-sided range imager, 0.077 mm x 0.158 mm pixels, 7.75 um height steps):
 6. Characteristics: operation, region, directions, measurement resolution and the systematic, direction-
    dependent differences that the redundancy of the four sides exposes.
 7. Floors of single runs against the pooled floor of their geometry, the cluster interval, and the floor without
    the warm-up of the first 150 parts.
 8. A dimension fixed by the tooling: the cup width at 15 mm depth (punch and die), whose batch centres within a
    run bound a lateral drift of the scanner, and their correlation with those of the flange width.

Outputs: results/sim_validation.csv, sim_mc_friction.csv, sim_depth_offset.csv, sim_oil_mapping.csv,
sim_envelope_variant.csv, meas_characteristics.csv, meas_run_floors.csv, meas_tooling_reference.csv,
summary_simcheck.md
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decisions as D  # noqa: E402
import panel as P  # noqa: E402
from alternatives import BATCH, batch_centres, batches, floor_from  # noqa: E402
from common import FC_MAX, FC_MIN, OIL_MAX_GM2, OIL_MIN_GM2, RESULTS, centre, oil_to_friction  # noqa: E402
from qc import QCS, SHARED, parts_qc, sims_qc  # noqa: E402

WARM_UP = 150
THICK_GRID = [0.95, 0.96, 0.97, 0.98, 0.99, 1.00]


def sims_signed() -> pd.DataFrame:
    raw = pd.read_csv(RESULTS / "features_ddacs_rddac.csv")
    s = sims_qc(raw)
    s["geometry"] = raw.loc[s.index, "geometry"].to_numpy() if "geometry" not in s else s["geometry"]
    s["mu"] = s["friction_coefficient"].round(3)
    s["thick"] = s["sheet_metal_thickness"].round(3)
    return s


# 1 ─────────────────────────────────────────────────────────────────────────────
def validation(t: pd.DataFrame, s: pd.DataFrame, floors: dict) -> pd.DataFrame:
    noise = pd.read_csv(RESULTS / "meas_sim.csv").set_index(["qc", "geometry"])
    nom = s[np.isclose(s["thick"], D.NOMINAL_THICKNESS)]
    rows = []
    for (geo, bhf), g in t.groupby(["geometry", "bhf_kN"]):
        for qc in SHARED:
            meas = g[g["qc"] == qc]["real_centre_signed"].to_numpy(float)
            cell = nom[(nom["geometry"] == geo) & (nom["bhf_kN"] == bhf)].sort_values("mu")
            sim = cell[qc].to_numpy(float)
            mus = cell["mu"].to_numpy(float)
            m = float(np.mean(meas))
            j = int(np.argmin(np.abs(sim - m)))
            s010 = float(sim[np.isclose(mus, D.NOMINAL_FRICTION)][0])
            F = floors[(qc, geo)]
            nz = noise.loc[(qc, geo)]
            rows.append({"qc": qc, "unit": QCS[qc][1], "geometry": geo, "bhf_kN": int(bhf),
                         "measured_centre": m, "measured_min_series": float(meas.min()),
                         "measured_max_series": float(meas.max()), "sim_nominal": s010,
                         "sim_minus_measured": s010 - m, "sim_minus_measured_floors": (s010 - m) / F,
                         "sim_min_over_friction": float(sim.min()), "sim_max_over_friction": float(sim.max()),
                         "measured_inside_friction_range": bool(sim.min() <= m <= sim.max()),
                         "closest_mu": float(mus[j]), "sim_at_closest_mu": float(sim[j]),
                         "residual_at_closest_floors": (float(sim[j]) - m) / F,
                         "sim_xy_sd_floors": float(nz["xy_sd_floors"]) if np.isfinite(nz["xy_sd_floors"]) else np.nan,
                         "sim_roughness_sd_floors": float(nz["roughness_sd_floors"])})
    return pd.DataFrame(rows)


# 2 ─────────────────────────────────────────────────────────────────────────────
def mc_friction(t: pd.DataFrame) -> pd.DataFrame:
    alts = sorted(t["alternative"].unique())
    rows = []
    jobs = []
    for a in alts:
        jobs.append(("within", a, [b for b in alts if b != a and b.split("/")[0] == a.split("/")[0]]))
    for geo in ("concave", "convex"):
        for bhf in (100, 300, 500):
            jobs.append(("setting", f"{geo}/{bhf}", [b for b in alts if b.startswith(geo) and D.bhf_of(b) != bhf]))
    for scope, target, calib in jobs:
        for lub in ("coarse", "medium", "fine"):
            mu = D.friction_fit(tuple(sorted(calib)), lub)
            rows.append({"scope": scope, "target": target, "lubrication": lub, "mu": mu,
                         "at_upper_edge": bool(np.isclose(mu, FC_MAX)), "at_lower_edge": bool(np.isclose(mu, FC_MIN))})
    return pd.DataFrame(rows)


# 3 ─────────────────────────────────────────────────────────────────────────────
def depth_offset(f: pd.DataFrame, s: pd.DataFrame) -> pd.DataFrame:
    nom = s[np.isclose(s["thick"], D.NOMINAL_THICKNESS) & np.isclose(s["mu"], D.NOMINAL_FRICTION)]
    raw = pd.read_csv(RESULTS / "features_ddacs_rddac.csv").set_index("index")
    rows = []
    for (geo, bhf), g in f.groupby(["geometry", "bhf_kN"]):
        sim = raw.loc[nom[(nom["geometry"] == geo) & (nom["bhf_kN"] == bhf)]["index"].to_numpy()]
        theta_m = float(np.nanmedian(g[["op10_theta_E_deg", "op10_theta_W_deg"]].mean(axis=1)))
        theta_s = float(np.nanmedian(sim[["op10_theta_x_deg", "op10_theta_y_deg"]].mean(axis=1)))
        rise_m = float(np.nanmedian(g[["op10_rise_E_mm", "op10_rise_W_mm"]].mean(axis=1)))
        rise_s = float(np.nanmedian(sim[["op10_rise_x_mm", "op10_rise_y_mm"]].mean(axis=1)))
        r15_m = float(np.nanmedian(g[["op10_wall_r15_E_mm", "op10_wall_r15_W_mm"]].mean(axis=1)))
        r15_s = float(np.nanmedian(sim[["op10_wall_r15_x_mm", "op10_wall_r15_y_mm"]].mean(axis=1)))
        dm, ds = float(np.nanmedian(g["op10_depth_mm"])), float(np.nanmedian(sim["op10_depth_mm"]))
        rows.append({"geometry": geo, "bhf_kN": int(bhf), "depth_measured": dm, "depth_sim": ds,
                     "depth_sim_minus_measured": ds - dm, "flange_angle_measured_deg": theta_m,
                     "flange_angle_sim_deg": theta_s, "flange_rise_measured": rise_m, "flange_rise_sim": rise_s,
                     "rise_difference": rise_s - rise_m,
                     "wall_r15_measured": r15_m, "wall_r15_sim": r15_s, "wall_r15_measured_minus_sim": r15_m - r15_s,
                     "press_bdc_median_mm": float(np.nanmedian(g["pos_bdc_mm"])),
                     "press_bdc_sd_mm": float(np.nanstd(g["pos_bdc_mm"]))})
    return pd.DataFrame(rows)


# 4 ─────────────────────────────────────────────────────────────────────────────
def oil_mapping(q: pd.DataFrame, s: pd.DataFrame, f: pd.DataFrame) -> pd.DataFrame:
    nom = s[np.isclose(s["thick"], D.NOMINAL_THICKNESS)]
    dmu_doil = -(FC_MAX - FC_MIN) / (OIL_MAX_GM2 - OIL_MIN_GM2)
    rows = []
    for (geo, bhf), g in q.groupby(["geometry", "bhf_kN"]):
        cell = nom[(nom["geometry"] == geo) & (nom["bhf_kN"] == bhf)].sort_values("mu")
        for qc in ("drawin_mid", "drawin_corner"):
            sens = float(np.polyfit(cell["mu"], cell[qc], 1)[0])         # mm per unit friction
            h = g.dropna(subset=[qc, "oil_gm2"])
            dev_y = h[qc] - h.groupby("alternative")[qc].transform("mean")
            dev_o = h["oil_gm2"] - h.groupby("alternative")["oil_gm2"].transform("mean")
            within = float(np.sum(dev_y * dev_o) / np.sum(dev_o ** 2))
            cen = h.groupby("oil_type").agg(y=(qc, centre), oil=("oil_gm2", "median"))
            between = [(cen.loc[b, "y"] - cen.loc[a, "y"]) / (cen.loc[b, "oil"] - cen.loc[a, "oil"])
                       for a, b in (("coarse", "medium"), ("coarse", "fine"), ("medium", "fine"))]
            rows.append({"geometry": geo, "bhf_kN": int(bhf), "qc": qc, "sim_mm_per_mu": sens,
                         "implied_mm_per_gm2": sens * dmu_doil, "within_run_mm_per_gm2": within,
                         "between_patterns_min": float(np.min(between)), "between_patterns_max": float(np.max(between)),
                         "between_patterns_median": float(np.median(between)),
                         "oil_traverse_sd_median": float(np.nanmedian(f.loc[(f["geometry"] == geo) & (f["bhf_kN"] == bhf), "oil_sd_gm2"])),
                         "oil_between_parts_sd": float(np.nanmedian(h.groupby("alternative")["oil_gm2"].std()))})
    return pd.DataFrame(rows)


# 5 ─────────────────────────────────────────────────────────────────────────────
def envelope_variant(t: pd.DataFrame, f: pd.DataFrame, s: pd.DataFrame, floors: dict) -> pd.DataFrame:
    from robustness import fast_intervals

    tv = t.copy()
    mu_grid = np.sort(s["mu"].unique())
    for alt, g in f.groupby("alternative"):
        th = g["sheet_um"].dropna().to_numpy() / 1000
        mu = np.array([oil_to_friction(o) for o in g["oil_gm2"].dropna()])
        tlo, thi = np.percentile(th, [5, 95])
        mlo, mhi = np.percentile(mu, [5, 95])
        tg = [x for x in THICK_GRID if x >= np.floor(tlo * 100) / 100 - 1e-9 and x <= np.ceil(thi * 100) / 100 + 1e-9]
        mg = [x for x in mu_grid if x >= np.floor(mlo * 100) / 100 - 1e-9 and x <= np.ceil(mhi * 100) / 100 + 1e-9]
        geo, bhf = alt.split("/")[0], D.bhf_of(alt)
        cell = s[(s["geometry"] == geo) & (s["bhf_kN"] == bhf) & s["thick"].isin(np.round(tg, 3)) & s["mu"].isin(np.round(mg, 3))]
        for qc in SHARED:
            v = D.transform(qc, cell[qc].dropna().to_numpy())
            sel = (tv["alternative"] == alt) & (tv["qc"] == qc)
            tv.loc[sel, "sim_env_lo"], tv.loc[sel, "sim_env_hi"] = float(v.min()), float(v.max())
            tv.loc[sel, "env_thickness"] = f"{min(tg):.2f}-{max(tg):.2f}"
            tv.loc[sel, "env_friction"] = f"{min(mg):.2f}-{max(mg):.2f}"
    rows = []
    for label, table in (("DDACS grid (reference)", t), ("measured incoming variation", tv)):
        D._CTX.update(t=table, floors=floors)
        iv = D.with_relation_scopes(fast_intervals(table, floors, rules=["M0w", "M2", "M5"]))
        iv = P.in_produced_floor(iv, floors)
        for (scope, m), g in iv[iv["scope"].isin(["within", "setting/interpolation", "setting/extrapolation",
                                                     "transfer"])].groupby(["scope", "method"]):
            rows.append({"envelope": label, "scope": scope, "method": m, **P.dist(g, sides=False),
                         "median_width_floors": float(np.median((g["hi"] - g["lo"]) / g["floor"]))})
    return pd.DataFrame(rows), tv[["alternative", "env_thickness", "env_friction"]].drop_duplicates()


# 6 ─────────────────────────────────────────────────────────────────────────────
def characteristics(f: pd.DataFrame) -> pd.DataFrame:
    scan = pd.read_csv(RESULTS / "meas_scan.csv")
    steps = pd.read_csv(RESULTS / "panel_resolution_steps.csv").set_index("qc")
    g = f.groupby("alternative")
    south = g.apply(lambda h: np.nanmedian(h["op10_wall_angle_S_deg"] - h[["op10_wall_angle_E_deg", "op10_wall_angle_W_deg"]].mean(axis=1)),
                    include_groups=False)
    cut_n = g.apply(lambda h: np.nanmedian(h["op20_wall_angle_N_deg"] - h["op20_wall_angle_E_deg"]), include_groups=False)
    cut_w = g.apply(lambda h: np.nanmedian(h["op20_wall_angle_W_deg"] - h["op20_wall_angle_E_deg"]), include_groups=False)
    convex = [a for a in south.index if a.startswith("convex")]
    rng = lambda v: f"{np.min(v):.2f} to {np.max(v):.2f}"  # noqa: E731
    north = scan.groupby("geometry")["N_minus_EW"].agg(["min", "max"])
    defs = {
        "drawin_mid": ("OP10", "flange, mid-sides", "x widths only, (210 - Wx)/2",
                       f"Wy - Wx {rng(scan['wy_minus_wx'])} mm; sd(Wy)/sd(Wx) {rng(scan['sd_wy'] / scan['sd_wx'])}"),
        "drawin_corner": ("OP10", "flange, corner tips", "mean of the two diagonals",
                          f"diagonals differ by {rng(scan['diag_difference'])} mm"),
        "waviness": ("OP10", "flange", "residual sd about a quadratic surface", "-"),
        "wall_op10": ("OP10", "side walls at mid-depth", "mean of east and west walls",
                      f"north wall {north.loc['convex', 'min']:.2f} to {north.loc['convex', 'max']:.2f} deg against E/W on the convex cups "
                      f"({north.loc['concave', 'min']:.2f} to {north.loc['concave', 'max']:.2f} concave); south wall shadowed, "
                      f"{rng(np.abs(south.to_numpy()))} deg off"),
        "arm_op20": ("OP20", "cut arms, centre lines", "mean of the four arms", "-"),
        "depth_op10": ("OP10", "flange against the bottom plane", "median over the flange",
                       "the flange plane is cut away at OP20"),
        "dome_op20": ("OP20", "cup bottom, sag at r = 40 mm", "paraboloid fit", "-"),
    }
    rows = []
    for qc in SHARED:
        op, region, dirs, bias = defs[qc]
        st = steps.loc[qc]
        rows.append({"qc": qc, "unit": QCS[qc][1], "operation": op, "region": region, "directions": dirs,
                     "resolution_step": float(st["median_step"]), "step_over_floor": float(st["step_over_floor"]),
                     "distinct_per_series": f"{int(st['distinct_per_series_min'])}-{int(st['distinct_per_series_max'])}",
                     "zero_se_alternatives": int(st["alternatives_with_zero_q95_se"]), "known_biases": bias})
    extra = pd.DataFrame({"cut_wall_north_minus_east_convex": [rng(cut_n[convex].to_numpy())],
                          "cut_wall_west_minus_east_convex": [rng(cut_w[convex].to_numpy())]})
    return pd.DataFrame(rows), extra


# 7 ─────────────────────────────────────────────────────────────────────────────
def run_floors(q: pd.DataFrame, floors: dict) -> pd.DataFrame:
    qb = batches(q)
    bc = batch_centres(qb, list(SHARED))
    rows = []
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    qw = q[q.groupby("alternative").cumcount() >= WARM_UP]
    bcw = batch_centres(batches(qw), list(SHARED))
    for qc in SHARED:
        ratios = []
        for alt, h in bc[qc].groupby(level=0):
            v = h.dropna().to_numpy()
            d = [abs(a - b) for i, a in enumerate(v) for b in v[i + 1:]]
            ratios.append(float(np.quantile(d, 0.95)) / floors[(qc, alt.split("/")[0])])
        rows.append({"qc": qc, "floor": float(fl.loc[qc, "floor"]), "batch_interval": f"{fl.loc[qc, 'floor_lo']:.4g}-{fl.loc[qc, 'floor_hi']:.4g}",
                     "cluster_interval": f"{fl.loc[qc, 'floor_lo_alt']:.4g}-{fl.loc[qc, 'floor_hi_alt']:.4g}",
                     "run_floor_min": float(np.min(ratios)), "run_floor_median": float(np.median(ratios)),
                     "run_floor_max": float(np.max(ratios)), "floor_without_warm_up": floor_from(bcw, qc),
                     "warm_up_ratio": floor_from(bcw, qc) / float(fl.loc[qc, "floor"])})
    return pd.DataFrame(rows)


# 8 ─────────────────────────────────────────────────────────────────────────────
def tooling_reference(f: pd.DataFrame) -> pd.DataFrame:
    f = f.copy()
    f["alternative"] = f["geometry"] + "/" + f["bhf_kN"].astype(str) + "/" + f["oil_type"]
    f["cup_width_15"] = f["op10_wall_r15_E_mm"] + f["op10_wall_r15_W_mm"]
    f["wx"] = f["op10_Wx_mm"]
    f["pos"] = f.sort_values(["category", "experiment_id"]).groupby("alternative").cumcount()
    f["batch"] = f["pos"] // BATCH
    cols = ["cup_width_15", "wx", "op10_depth_mm"]
    bc = f.groupby(["alternative", "batch"])[cols].agg(centre)
    dev = bc - bc.groupby(level=0).transform("mean")
    rows = []
    for geo in ("concave", "convex"):
        sub = dev[[a.startswith(geo) for a in dev.index.get_level_values(0)]]
        fl = {}
        for c in cols:
            dd = []
            for _, h in bc[c][[a.startswith(geo) for a in bc.index.get_level_values(0)]].groupby(level=0):
                v = h.dropna().to_numpy()
                dd += [abs(a - b) for i, a in enumerate(v) for b in v[i + 1:]]
            fl[c] = float(np.quantile(dd, 0.95))
        rows.append({"geometry": geo, "r_wx_cupwidth": float(sub["wx"].corr(sub["cup_width_15"])),
                     "floor_cup_width_mm": fl["cup_width_15"], "floor_wx_mm": fl["wx"], "floor_depth_mm": fl["op10_depth_mm"],
                     "cup_width_mm": float(np.nanmedian(f.loc[f["geometry"] == geo, "cup_width_15"])),
                     "wx_mm": float(np.nanmedian(f.loc[f["geometry"] == geo, "wx"])),
                     "lateral_scale_drift_bound": fl["cup_width_15"] / float(np.nanmedian(f.loc[f["geometry"] == geo, "cup_width_15"]))})
    return pd.DataFrame(rows)


def main() -> None:
    import warnings

    warnings.simplefilter("ignore")
    t = pd.read_csv(RESULTS / "dec_alternatives.csv")
    floors = D.load_floors()
    s = sims_signed()
    sims = sims_qc(pd.read_csv(RESULTS / "features_ddacs_rddac.csv"))
    D.setup(t, sims, floors)
    f = pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False)
    f = f[f["status"] == "ok"].copy()
    f["alternative"] = f["geometry"] + "/" + f["bhf_kN"].astype(str) + "/" + f["oil_type"]
    q = parts_qc(f)
    out = {"sim_validation": validation(t, s, floors), "sim_mc_friction": mc_friction(t),
           "sim_depth_offset": depth_offset(f, s), "sim_oil_mapping": oil_mapping(q, s, f)}
    out["sim_envelope_variant"], env = envelope_variant(t, f, s, floors)
    out["sim_envelope_ranges"] = env
    out["meas_characteristics"], extra = characteristics(f)
    out["meas_cut_walls"] = extra
    out["meas_run_floors"] = run_floors(q, floors)
    out["meas_tooling_reference"] = tooling_reference(f)
    for name, frame in out.items():
        frame.to_csv(RESULTS / f"{name}.csv", index=False)
    mc = out["sim_mc_friction"]
    lines = ["# The simulation against the produced process, and the measurement", "",
             f"Mc friction fits at the upper edge of the grid (0.15): within the family {int(mc['at_upper_edge'].sum())} "
             f"of {len(mc)}.", ""]
    for name, frame in out.items():
        lines += [f"## {name}", "", frame.round(4).to_markdown(index=False), ""]
    (RESULTS / "summary_simcheck.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:120]))


if __name__ == "__main__":
    main()
