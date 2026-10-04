"""Quality characteristics (QCs): one definition used by every analysis.

The feature tables carry raw measurements per side (E, W, S, N for the
scans; x, y for the quarter-model simulations). This module turns them into
the characteristics used in the study, so that a characteristic is defined
once, identically for parts and simulations.

The south side of the scans is excluded from the wall measures: the scanner
leaves a gap at the south wall (laser shadow), visible as missing data in
both operations. The wall angle after cutting is not used: on the cut convex
parts the north and, in some parts, the west wall read 5-7 degrees steeper
than the east wall although all three agree after drawing (scan artefacts on
walls facing the camera); the per-side values remain in the feature table.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

#: name -> (label, unit, direction of a requirement: 'max' = smaller is better,
#: 'abs' = closer to zero is better)
QCS = {
    "drawin_mid": ("Draw-in at mid-sides", "mm", "max"),
    "drawin_corner": ("Draw-in at corners", "mm", "max"),
    "waviness": ("Flange waviness", "mm", "max"),
    "wall_op10": ("Wall angle after drawing", "deg", "max"),
    "arm_op20": ("Arm angle after cutting", "deg", "abs"),
    "depth_op10": ("Cup depth", "mm", "max"),
    "dome_op20": ("Bottom dome after cutting", "mm", "abs"),
}
#: Characteristics measured identically on parts and simulations.
SHARED = ["drawin_mid", "drawin_corner", "waviness", "wall_op10", "arm_op20", "depth_op10", "dome_op20"]
#: Process signals and incoming conditions of a part (not quality outcomes).
SIGNALS = ["F10_kN", "F20_kN", "F25_kN", "W_draw_J", "F_peak_kN", "imbalance20", "v_form_mm_s",
           "punch_temp_C", "sheet_um", "oil_gm2"]


def _nanmean(df: pd.DataFrame, cols: list[str]) -> pd.Series:
    present = [c for c in cols if c in df.columns]
    return df[present].mean(axis=1, skipna=True) if present else pd.Series(np.nan, index=df.index)


def parts_qc(f: pd.DataFrame) -> pd.DataFrame:
    """QCs of the scanned parts from the rows of results/features_rddac.csv."""
    f = f[f["status"] == "ok"].copy()
    q = pd.DataFrame(index=f.index)
    q["drawin_mid"] = f["op10_drawin_mid_mm"]
    q["drawin_corner"] = f["op10_drawin_corner_mm"]
    q["waviness"] = f["op10_wav_sd_mm"]
    q["wall_op10"] = _nanmean(f, [f"op10_wall_angle_{s}_deg" for s in "EWN"])
    q["arm_op20"] = _nanmean(f, [f"op20_theta_{s}_deg" for s in "EWSN"])
    q["depth_op10"] = f["op10_depth_mm"]
    q["dome_op20"] = f["op20_dome_mm"]
    meta = ["index", "experiment_id", "category", "geometry", "bhf_kN", "oil_type"]
    out = pd.concat([f[meta], q, f[[c for c in SIGNALS if c in f.columns]]], axis=1)
    out["alternative"] = out["geometry"] + "/" + out["bhf_kN"].astype(str) + "/" + out["oil_type"]
    return out.sort_values(["category", "experiment_id"]).reset_index(drop=True)


def sims_qc(s: pd.DataFrame) -> pd.DataFrame:
    """QCs of the simulations from the rows of results/features_ddacs_*.csv."""
    s = s[s["status"] == "ok"].copy()
    q = pd.DataFrame(index=s.index)
    q["drawin_mid"] = s["op10_drawin_mid_mm"]
    q["drawin_corner"] = s["op10_drawin_corner_mm"]
    q["waviness"] = s["op10_wav_sd_mm"]
    q["wall_op10"] = _nanmean(s, ["op10_wall_angle_x_deg", "op10_wall_angle_y_deg"])
    q["arm_op20"] = _nanmean(s, ["op20_theta_x_deg", "op20_theta_y_deg"])
    q["depth_op10"] = s["op10_depth_mm"]
    q["dome_op20"] = s["op20_dome_mm"]
    meta = ["index", "geometry", "curvature_radius", "bottom_radius", "wall_angle", "material_scaling_factor",
            "sheet_metal_thickness", "friction_coefficient", "blankholder_force"]
    extra = [c for c in ["sim_thin_min_ratio", "sim_thick_max_ratio", "sim_eps_max"] if c in s.columns]
    out = pd.concat([s[meta], q, s[extra]], axis=1)
    out["bhf_kN"] = (out["blankholder_force"] / 1000.0).round().astype(int)
    return out.reset_index(drop=True)
