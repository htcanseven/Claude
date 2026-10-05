"""Measurement and the production floor: what the floor contains and what it leaves out.

1. Redundancy of the scans. The four sides of a part measure the same
   physical quantity twice (x and y flange widths, east and west walls, two
   flange diagonals), so their differences expose measurement noise and bias
   without a gauge study. Per series: standard deviations, correlations,
   lag-1 autocorrelations and mean differences (meas_scan.csv). These led to
   the definitions in qc.py (mid-side draw-in from the x widths, wall angle
   from the east and west walls).
2. Components of the floor per characteristic (meas_floor.csv), in the terms
   of statistical process control:
   - sigma_st, the short-term standard deviation within rational subgroups of
     SUBGROUP consecutive parts, and sigma_lt, the standard deviation of the
     whole series (medians over series), and sigma_batch, the standard
     deviation of the batch centres beyond what the parts' scatter explains
     (one-way analysis of variance within a series);
   - the white floor: what part-to-part noise alone would produce between two
     batch centres, 1.96 * sqrt(2 / B) * sigma_ss, with sigma_ss from the mean
     square successive difference. Measurement noise that is independent from
     part to part is part of it, so white floor / floor bounds the share of the
     floor that a scanner's repeatability can explain;
   - the floor from the first half of every series (series length);
   - the floor of the decided statistic itself: the 95th percentile of batches
     of 100 parts (q95 floor), and of the two halves of each series;
   - the between-series floor: the three lubrication series of one geometry
     and force were produced separately and production does not separate most
     of them, so the differences between their centres bound the variation
     between runs of one design from above (lubrication effects included).
3. Extraction noise of the simulated characteristics (meas_sim.csv): the
   quarter model is symmetric about its diagonal, so its x and y values
   estimate the same quantity and their difference is extraction noise; the
   roughness of the simulated values along the friction grid (second
   differences) gives the same from another angle. The upper end of the
   simulation envelope (used by M2 and M5) is compared with the upper end of a
   quadratic response surface over sheet thickness and friction in each cell.
All values are also given in floors of the characteristic's geometry.

Outputs: results/meas_scan.csv, meas_floor.csv, meas_sim.csv, summary_measurement.md
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from alternatives import ALPHA, BATCH, batch_centres, batches, floor_from  # noqa: E402
from common import RESULTS, centre  # noqa: E402
from decisions import transform  # noqa: E402
from qc import QCS, SHARED, parts_qc, sims_qc  # noqa: E402

SUBGROUP = 5        # consecutive parts of a rational subgroup (short-term variation)
Q95_BATCH = 100     # parts per batch of the q95 floor
Z = 1.959964


def scan_redundancy(f: pd.DataFrame) -> pd.DataFrame:
    f = f[f["status"] == "ok"].sort_values(["category", "experiment_id"])
    f = f.assign(alternative=f["geometry"] + "/" + f["bhf_kN"].astype(str) + "/" + f["oil_type"])
    rows = []
    for a, g in f.groupby("alternative"):
        E, W, N = (g[f"op10_wall_angle_{s}_deg"] for s in "EWN")
        wx, wy = g["op10_Wx_mm"], g["op10_Wy_mm"]
        rows.append({"alternative": a, "geometry": a.split("/")[0],
                     "sd_wx": wx.std(), "sd_wy": wy.std(), "r_wx_wy": wx.corr(wy),
                     "lag1_wx": wx.dropna().autocorr(1), "lag1_wy": wy.dropna().autocorr(1),
                     "wy_minus_wx": (wy - wx).mean(), "diag_difference": (g["op10_Ld1_mm"] - g["op10_Ld2_mm"]).mean(),
                     "sd_E": E.std(), "sd_W": W.std(), "sd_N": N.std(), "r_E_W": E.corr(W), "r_E_N": E.corr(N),
                     "lag1_N": N.dropna().autocorr(1), "N_minus_EW": (N - (E + W) / 2).mean(),
                     "sd_EW_mean": ((E + W) / 2).std(), "sd_EWN_mean": ((E + W + N) / 3).std(),
                     "noise_bound_EW_mean": (E - W).std() / 2})
    return pd.DataFrame(rows)


def series_stats(y: np.ndarray) -> dict:
    y = y[np.isfinite(y)]
    n = len(y) // SUBGROUP * SUBGROUP
    sub = y[:n].reshape(-1, SUBGROUP)
    st = float(np.sqrt(np.mean(np.var(sub, axis=1, ddof=1))))
    ss = float(np.sqrt(np.mean(np.diff(y) ** 2) / 2))
    nb = len(y) // BATCH
    b = y[:nb * BATCH].reshape(nb, BATCH)
    msb = BATCH * np.var(b.mean(axis=1), ddof=1)
    msw = np.mean(np.var(b, axis=1, ddof=1))
    return {"sigma_st": st, "sigma_lt": float(np.std(y, ddof=1)), "sigma_ss": ss,
            "sigma_batch": float(np.sqrt(max(msb - msw, 0.0) / BATCH))}


def q95_floor(q: pd.DataFrame, qc: str, size: int) -> float:
    diffs = []
    for _, g in q.groupby("alternative"):
        y = transform(qc, g[qc].to_numpy())
        y = y[np.isfinite(y)]
        k = len(y) // size
        v = np.array([np.quantile(y[i * size:(i + 1) * size], 0.95) for i in range(k)])
        if v.size >= 2:
            i, j = np.triu_indices(v.size, 1)
            diffs.append(np.abs(v[i] - v[j]))
    return float(np.quantile(np.concatenate(diffs), ALPHA)) if diffs else np.nan


def floor_components(q: pd.DataFrame, fl: pd.DataFrame) -> pd.DataFrame:
    qb = batches(q)
    bm = batch_centres(qb, list(QCS))
    half = qb[qb["batch"] < qb.groupby("alternative")["batch"].transform("max") / 2 + 0.5]
    bm_half = batch_centres(half, list(QCS))
    cent = q.groupby("alternative")[list(QCS)].agg(lambda s: centre(s.dropna().to_numpy()))
    rows = []
    for c in QCS:
        st = pd.DataFrame([series_stats(g[c].to_numpy(float)) for _, g in q.groupby("alternative")]).median()
        F = float(fl.loc[c, "floor"])
        # between-series: the three lubrication series of each geometry and force
        between = []
        for (geo, bhf), g in q.groupby(["geometry", "bhf_kN"]):
            v = cent.loc[g["alternative"].unique(), c].to_numpy()
            between += [abs(x - y) for x, y in itertools.combinations(v, 2)]
        halves = []
        for _, g in q.groupby("alternative"):
            y = transform(c, g[c].to_numpy())
            y = y[np.isfinite(y)]
            halves.append(abs(np.quantile(y[:len(y) // 2], 0.95) - np.quantile(y[len(y) // 2:], 0.95)))
        white = Z * np.sqrt(2.0 / BATCH) * st["sigma_ss"]
        rows.append({"qc": c, "unit": QCS[c][1], "floor": F, "sigma_st": st["sigma_st"], "sigma_lt": st["sigma_lt"],
                     "sigma_ss": st["sigma_ss"], "sigma_batch": st["sigma_batch"],
                     "lt_over_st": st["sigma_lt"] / st["sigma_st"],
                     "white_floor": white, "white_share": white / F,
                     "floor_first_half": floor_from(bm_half, c),
                     "q95_floor_b100": q95_floor(q, c, Q95_BATCH), "q95_halves_max": float(np.max(halves)),
                     "q95_halves_median": float(np.median(halves)),
                     "between_series_q95": float(np.quantile(between, ALPHA)),
                     "between_series_median": float(np.median(between))})
    out = pd.DataFrame(rows)
    for col in ["white_floor", "floor_first_half", "q95_floor_b100", "q95_halves_max", "q95_halves_median",
                "between_series_q95", "between_series_median"]:
        out[f"{col}_floors"] = out[col] / out["floor"]
    return out


def sim_noise(s: pd.DataFrame, fl: pd.DataFrame) -> pd.DataFrame:
    """Extraction noise of the simulated characteristics, in floors of each geometry."""
    pairs = {"wall_op10": ("op10_wall_angle_x_deg", "op10_wall_angle_y_deg", 1.0),
             "arm_op20": ("op20_theta_x_deg", "op20_theta_y_deg", 1.0),
             "drawin_mid": ("op10_Wx_mm", "op10_Wy_mm", 0.5)}
    q = sims_qc(s)
    rows = []
    for c in SHARED:
        for geo, g in q.groupby("geometry"):
            F = float(fl.loc[c, f"floor_{geo}"])
            r = {"qc": c, "geometry": geo, "floor": F}
            if c in pairs:
                x, y, scale = pairs[c]
                raw = s[(s["status"] == "ok") & (s["geometry"] == geo)]
                dxy = scale * (raw[x] - raw[y]).to_numpy()
                dxy = dxy[np.isfinite(dxy)]
                r.update({"xy_sd_floors": float(np.std(dxy) / F), "xy_max_floors": float(np.max(np.abs(dxy)) / F),
                          "xy_share_over_1_floor": float(np.mean(np.abs(dxy) > F))})
            # roughness along the friction grid at fixed geometry, force and thickness
            rough = []
            for _, h in g.groupby(["bhf_kN", "sheet_metal_thickness"]):
                v = transform(c, h.sort_values("friction_coefficient")[c].to_numpy())
                if v.size >= 3:
                    rough.append(v[1:-1] - (v[:-2] + v[2:]) / 2)
            rough = np.concatenate(rough)
            rough = rough[np.isfinite(rough)]
            r.update({"roughness_sd_floors": float(np.std(rough) / np.sqrt(1.5) / F),
                      "roughness_max_floors": float(np.max(np.abs(rough)) / F)})
            # upper end of the envelope: raw maximum against a quadratic response surface
            gaps = []
            for _, h in g.groupby("bhf_kN"):
                h = h.dropna(subset=[c])
                t, m = h["sheet_metal_thickness"].to_numpy(), h["friction_coefficient"].to_numpy()
                yv = transform(c, h[c].to_numpy())
                A = np.column_stack([np.ones_like(t), t, m, t * t, m * m, t * m])
                coef, *_ = np.linalg.lstsq(A, yv, rcond=None)
                gaps.append((yv.max() - (A @ coef).max()) / F)
            r.update({"env_hi_minus_smooth_floors_median": float(np.median(gaps)),
                      "env_hi_minus_smooth_floors_max": float(np.max(np.abs(gaps)))})
            rows.append(r)
    return pd.DataFrame(rows)


def main() -> None:
    f = pd.read_csv(RESULTS / "features_rddac.csv", low_memory=False)
    s = pd.read_csv(RESULTS / "features_ddacs_rddac.csv")
    fl = pd.read_csv(RESULTS / "alt_floor.csv").set_index("qc")
    scan = scan_redundancy(f)
    scan.to_csv(RESULTS / "meas_scan.csv", index=False)
    comp = floor_components(parts_qc(f), fl)
    comp.to_csv(RESULTS / "meas_floor.csv", index=False)
    sim = sim_noise(s, fl)
    sim.to_csv(RESULTS / "meas_sim.csv", index=False)
    lines = ["# Measurement and the production floor", "",
             "## Redundancy of the scans per series (x/y flange widths, walls)", "",
             scan.round(3).to_markdown(index=False), "",
             "## Components of the floor (medians over series; *_floors in floors)", "",
             comp.round(4).to_markdown(index=False), "",
             "## Extraction noise of the simulated characteristics (floors)", "",
             sim.round(3).to_markdown(index=False)]
    (RESULTS / "summary_measurement.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
