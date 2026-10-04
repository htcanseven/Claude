"""Per-experiment features of the RDDAC deep-drawing experiments.

For every one of the 9,000 parts this script reads the raw HDF5 file straight
from the DaRUS archive (HTTP range requests; nothing is stored) and reduces it
to one row of scalar quantities:

* incoming material and lubrication: sheet thickness and oil film (traverses);
* the press-force record: force at fixed forming depths, drawing work before
  the bottoming spike, load-cell imbalance, forming speed, punch temperature;
* quality characteristics from the 3D scans after drawing (OP10) and after
  cutting (OP20): flange extents along the mid-lines and diagonals (draw-in),
  cup depth, flange waviness, flange and arm angles about the cup bottom, and
  the dome of the cup bottom.

All geometry is expressed about the plane of the cup bottom, which is the
part's own datum; the scanner placement drops out. The same characteristics
are computed for the simulations by ``features_ddacs.py``.

Usage:
    python scripts/features_rddac.py --sample          # 18 sample files (local zip)
    python scripts/features_rddac.py --workers 4       # all 9,000, resumable
"""

from __future__ import annotations

import argparse
import sys
import time
import zipfile
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    ARM_BAND_HALF_MM,
    BAND_HALF_MM,
    BLANK_MM,
    CACHE,
    FLANGE_WALL_CLEARANCE_MM,
    FORCE_WINDOW_S,
    OIL_MAX_POS_MM,
    PLATEAU_CORE_CLEARANCE_MM,
    RDDAC_FILES,
    RESULTS,
    SHEET_LAST_N,
    X_MM_PER_PX,
    Y_MM_PER_PX,
    Z_MM_PER_UNIT,
    atomic_append_rows,
    fetch_small,
    h5_from_bytes,
    lumi_valid_mask,
    oil_to_friction,
    read_member,
    robust_plane,
    robust_sd,
)

# Block size of the robust grid used for the region measures (lines x columns):
# 2 x 4 pixels = 0.316 mm x 0.308 mm.
BLK_Y, BLK_X = 2, 4
DY, DX = BLK_Y * Y_MM_PER_PX, BLK_X * X_MM_PER_PX
FORMING_DEPTH_MM = 30.0     # nominal drawing depth; contact at bottom dead centre minus this
DRAW_WORK_END_MM = 28.0     # drawing work is integrated up to here (before the bottoming spike)
ARM_DIRS = {"E": (1.0, 0.0), "W": (-1.0, 0.0), "S": (0.0, 1.0), "N": (0.0, -1.0)}
PROFILE_BIN_MM = 0.5        # radial bins of the arm/flange profiles
MIN_BIN_COUNT = 3           # cells (or nodes) needed for a bin median
FLAT_SLOPE_DEG = 15.0       # steeper profile parts are wall, die radius or edge roll-off
ARM_SEG_MARGIN_MM = 1.0     # trimmed from both ends of the flat run
ARM_MIN_SEGMENT_MM = 4.0
WALL_LEVELS_MM = (8.0, 15.0, 22.0)  # depths for the wall angle (lower, mid, upper)
EDGE_CLEARANCE_MM = 3.0     # flange cells this close to the outer edge are excluded
TIP_WINDOW_MM = 0.3         # outline points within this of the extreme form a corner tip


# ── traverses and force ──────────────────────────────────────────────────────
def sheet_features(data: np.ndarray) -> dict:
    t = data[-SHEET_LAST_N:, 1].astype(float)
    t[t < 0] = np.nan                       # sensor error codes
    v = t[np.isfinite(t)]
    return {
        "sheet_um": float(np.median(v)) if v.size else np.nan,
        "sheet_sd_um": robust_sd(v),
        "sheet_n": int(v.size),
    }


def oil_features(data: np.ndarray) -> dict:
    pos, val = data[:, 0].astype(float), data[:, 1].astype(float)
    v = val[(pos < OIL_MAX_POS_MM) & np.isfinite(val)]
    if v.size == 0:
        return {"oil_gm2": np.nan, "oil_sd_gm2": np.nan, "oil_n": 0, "fc_equiv": np.nan}
    med, sd = np.median(v), max(robust_sd(v), 0.01)
    keep = np.abs(v - med) <= 3.0 * sd       # spikes and dropouts
    m = float(np.mean(v[keep]))
    return {"oil_gm2": m, "oil_sd_gm2": float(np.std(v[keep])), "oil_n": int(keep.sum()),
            "fc_equiv": oil_to_friction(m)}


def force_features(data: np.ndarray, columns: list[str]) -> dict:
    d = {c: data[:, i].astype(float) for i, c in enumerate(columns)}
    t, pos, tot = d["time"], d["punch_pos"], d["total_force"]
    cells = np.column_stack([d[f"load_cell_{k}"] for k in range(1, 5)])
    w = (t > FORCE_WINDOW_S[0]) & (t <= FORCE_WINDOW_S[1])
    i_bdc = int(np.argmax(pos))
    pos_bdc = pos[i_bdc]
    load = np.arange(i_bdc + 1)
    # rest level: loading branch well before contact
    rest = load[pos[load] < pos_bdc - FORMING_DEPTH_MM - 15.0]
    base = float(np.median(tot[rest])) if rest.size else 0.0
    cbase = np.median(cells[rest], axis=0) if rest.size else np.zeros(4)
    s = pos[load] - (pos_bdc - FORMING_DEPTH_MM)          # forming depth, mm
    f = tot[load] - base
    order = np.argsort(s, kind="stable")
    s_o, f_o, t_o = s[order], f[order], t[load][order]
    F10, F20, F25 = np.interp([10.0, 20.0, 25.0], s_o, f_o)
    m = (s_o >= 0) & (s_o <= DRAW_WORK_END_MM)
    work = float(np.trapezoid(f_o[m], s_o[m])) if m.sum() > 2 else np.nan   # kN*mm = J
    c20 = np.array([np.interp(20.0, s_o, (cells[load, k] - cbase[k])[order]) for k in range(4)])
    t10, t25 = np.interp([10.0, 25.0], s_o, t_o)
    return {
        "F10_kN": float(F10), "F20_kN": float(F20), "F25_kN": float(F25),
        "W_draw_J": work,
        "F_peak_kN": float(np.max(f)),
        "F_rest_kN": base,
        "imbalance20": float((c20.max() - c20.min()) / np.mean(c20)) if np.mean(c20) > 0 else np.nan,
        "v_form_mm_s": float(15.0 / (t25 - t10)) if t25 > t10 else np.nan,
        "punch_temp_C": float(np.median(d["punch_temp"][w])) if w.any() else float(np.median(d["punch_temp"])),
        "pos_bdc_mm": float(pos_bdc),
        "cycle_s": float(t[-1] - t[0]),
    }


# ── scans ────────────────────────────────────────────────────────────────────
def load_scan(h5, op: str):
    g = h5[f"pointcloud/{op}"]
    shape = (int(g.attrs["y_shape"]), int(g.attrs["x_shape"]))
    z = g["z"][:].reshape(shape).astype(np.float64)
    lumi = g["luminescence"][:].reshape(shape)
    valid = lumi_valid_mask(lumi) & (z > 0)
    return np.where(valid, z * Z_MM_PER_UNIT, np.nan), valid


def block_median(Z: np.ndarray) -> np.ndarray:
    ny, nx = Z.shape[0] // BLK_Y, Z.shape[1] // BLK_X
    b = Z[: ny * BLK_Y, : nx * BLK_X].reshape(ny, BLK_Y, nx, BLK_X).transpose(0, 2, 1, 3).reshape(ny, nx, -1)
    with np.errstate(all="ignore"):
        import warnings

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            return np.nanmedian(b, axis=2)


def largest_component(mask: np.ndarray) -> np.ndarray:
    lab, n = ndimage.label(mask)
    if n <= 1:
        return mask
    sizes = ndimage.sum(mask, lab, index=np.arange(1, n + 1))
    return lab == (int(np.argmax(sizes)) + 1)


def part_frame(Zd: np.ndarray) -> dict:
    """Cup-bottom datum on the block grid: plane, centre, depth map, core mask."""
    ny, nx = Zd.shape
    Xg = (np.arange(nx) * BLK_X + (BLK_X - 1) / 2) * X_MM_PER_PX
    Yg = (np.arange(ny) * BLK_Y + (BLK_Y - 1) / 2) * Y_MM_PER_PX
    X, Y = np.meshgrid(Xg, Yg)
    fin = np.isfinite(Zd)
    z_top = np.nanpercentile(Zd, 99.0)
    plateau = largest_component(fin & (Zd > z_top - 3.0))
    inner = ndimage.distance_transform_edt(plateau, sampling=(DY, DX))
    core = plateau & (inner >= PLATEAU_CORE_CLEARANCE_MM)
    a, b, c = robust_plane(X[core], Y[core], Zd[core])
    D = (a + b * X + c * Y) - Zd                 # depth below the cup-bottom plane (mm)
    xc, yc = float(X[plateau].mean()), float(Y[plateau].mean())
    # dome of the bottom: z = a + b x + c y + k r^2 about the centre; sag at r = 40 mm
    xr, yr = X[core] - xc, Y[core] - yc
    A = np.column_stack([np.ones(core.sum()), xr, yr, xr ** 2 + yr ** 2])
    k = np.linalg.lstsq(A, Zd[core], rcond=None)[0][3]
    tilt = float(np.degrees(np.arctan(np.hypot(b, c))))
    return {"X": X, "Y": Y, "D": D, "fin": fin, "plateau": plateau, "core": core, "xc": xc, "yc": yc,
            "dome_mm": float(k * 40.0 ** 2), "plane_tilt_deg": tilt, "n_core": int(core.sum())}


def flange_points(fr: dict, d_lo: float = 20.0, d_hi: float = 40.0) -> np.ndarray:
    """Flange/arm cells clear of the cup (die radius) and of the outer edge roll-off."""
    D, fin = fr["D"], fr["fin"]
    cup = fin & (D < d_lo)
    clear = ndimage.distance_transform_edt(~cup, sampling=(DY, DX)) >= FLANGE_WALL_CLEARANCE_MM
    inside = ndimage.distance_transform_edt(fin, sampling=(DY, DX)) >= EDGE_CLEARANCE_MM
    return fin & (D >= d_lo) & (D <= d_hi) & clear & inside


def flat_segment(r: np.ndarray, d: np.ndarray, bin_mm: float = None):
    """Longest run of a radial profile whose slope stays below FLAT_SLOPE_DEG.

    The profile is the median depth in 0.5 mm bins of r. The wall, the die
    radius and the edge roll-off are steep and fall outside the run; the run
    is shortened by ARM_SEG_MARGIN_MM at both ends. Returns (r_start, r_end)
    or None when no run of ARM_MIN_SEGMENT_MM exists.
    """
    bin_mm = bin_mm or PROFILE_BIN_MM
    edges = np.arange(np.floor(r.min()), np.ceil(r.max()) + bin_mm, bin_mm)
    idx = np.digitize(r, edges) - 1
    cnt = np.bincount(idx, minlength=len(edges))[: len(edges) - 1]
    med = np.full(len(edges) - 1, np.nan)
    for i in np.flatnonzero(cnt >= MIN_BIN_COUNT):
        med[i] = np.median(d[idx == i])
    centres = edges[:-1] + bin_mm / 2
    ok = np.isfinite(med)
    if ok.sum() < 4:
        return None
    c, m = centres[ok], med[ok]
    slope = np.gradient(m, c)
    flat = np.abs(slope) < np.tan(np.radians(FLAT_SLOPE_DEG))
    contiguous = np.diff(c) <= bin_mm * 2.5                  # gaps break runs
    best, start = (0.0, -1, -1), None
    for i in range(len(c)):
        if not flat[i]:
            start = None
            continue
        if start is None or not contiguous[i - 1]:
            start = i
        if c[i] - c[start] > best[0]:
            best = (c[i] - c[start], start, i)
    _, i0, i1 = best
    if i0 < 0:
        return None
    r0, r1 = c[i0] + ARM_SEG_MARGIN_MM, c[i1] - ARM_SEG_MARGIN_MM
    return (r0, r1) if r1 - r0 >= ARM_MIN_SEGMENT_MM else None


def wall_measures(r: np.ndarray, d: np.ndarray, key: str, bin_mm: float = None) -> dict:
    """Wall position at mid-depth and apparent wall angle from a radial profile.

    The binned median profile is walked outward from the cup bottom; the radii
    where it first reaches WALL_LEVELS_MM are interpolated. Wall angle is from
    vertical: atan(dr / dD) between the lower and upper level.
    """
    lo, mid, hi = WALL_LEVELS_MM
    out = {key.format("wall_r15") + "_mm": np.nan, key.format("wall_angle") + "_deg": np.nan}
    if r.size < 30:
        return out
    bin_mm = bin_mm or PROFILE_BIN_MM
    edges = np.arange(np.floor(r.min()), np.ceil(r.max()) + bin_mm, bin_mm)
    idx = np.digitize(r, edges) - 1
    cnt = np.bincount(idx, minlength=len(edges))[: len(edges) - 1]
    good = np.flatnonzero(cnt >= MIN_BIN_COUNT)
    if good.size < 4:
        return out
    c = edges[good] + bin_mm / 2
    m = np.array([np.median(d[idx == i]) for i in good])

    def first_crossing(level: float) -> float:
        above = np.flatnonzero(m >= level)
        if above.size == 0 or above[0] == 0:
            return np.nan
        i = above[0]
        if c[i] - c[i - 1] > max(3.0, 3 * bin_mm):   # no interpolation across scan holes
            return np.nan
        return float(np.interp(level, [m[i - 1], m[i]], [c[i - 1], c[i]]))

    r_lo, r_mid, r_hi = (first_crossing(v) for v in (lo, mid, hi))
    out[key.format("wall_r15") + "_mm"] = r_mid
    if np.isfinite(r_lo) and np.isfinite(r_hi):
        out[key.format("wall_angle") + "_deg"] = float(np.degrees(np.arctan2(r_hi - r_lo, hi - lo)))
    return out


def arm_angles(fr: dict, prefix: str) -> dict:
    """Inclination of the flange (OP10) or arm (OP20) along the four mid-lines.

    In each 10 mm wide band the usable segment runs from where the wall reaches
    the flange level (plus ARM_ROOT_MARGIN_MM, which excludes the die radius)
    to the outer edge (minus ARM_EDGE_MARGIN_MM, which excludes the edge
    roll-off). The slope of the depth below the cup-bottom plane along the
    segment gives the angle; positive means the edge lies farther from the cup
    bottom than the root.
    """
    out, thetas = {}, []
    X, Y, D, fin = fr["X"], fr["Y"], fr["D"], fr["fin"]
    dx, dy = X - fr["xc"], Y - fr["yc"]
    for name, (ux, uy) in ARM_DIRS.items():
        r = dx * ux + dy * uy
        lat = np.abs(-dx * uy + dy * ux)
        band = fin & (lat <= ARM_BAND_HALF_MM) & (r > 0)
        keys = (f"{prefix}_theta_{name}_deg", f"{prefix}_rise_{name}_mm", f"{prefix}_seg_{name}_mm")
        out.update(wall_measures(r[band], D[band], f"{prefix}_{{}}_{name}"))
        flat = band & (D >= 20.0)
        seg = flat_segment(r[flat], D[flat]) if flat.sum() >= 30 else None
        if seg is None:
            out.update(dict.fromkeys(keys, np.nan))
            continue
        r_root, r_edge = seg
        m = flat & (r >= r_root) & (r <= r_edge)
        if m.sum() < 30:
            out.update(dict.fromkeys(keys, np.nan))
            continue
        rr, dd = r[m], D[m]
        keep = np.ones(rr.size, bool)
        for _ in range(3):
            p = np.polyfit(rr[keep], dd[keep], 1)
            res = dd - np.polyval(p, rr)
            keep = np.abs(res) <= 3.0 * max(robust_sd(res[keep]), 1e-3)
        th = float(np.degrees(np.arctan(p[0])))
        out[keys[0]] = th
        out[keys[1]] = float(p[0] * (r_edge - r_root))
        out[keys[2]] = float(r_edge - r_root)
        thetas.append(th)
    out[f"{prefix}_theta_mean_deg"] = float(np.mean(thetas)) if thetas else np.nan
    out[f"{prefix}_theta_range_deg"] = float(np.ptp(thetas)) if len(thetas) > 1 else np.nan
    return out


def extents(valid: np.ndarray, xc: float, yc: float) -> dict:
    """Flange extents on the full-resolution mask after drawing.

    Mid-line widths are edge-to-edge distances across bands through the cup
    centre; at the mid-sides the outline is at an extremum, so the band
    position matters little. Corner tips are the outline points farthest out
    along each diagonal; tip-to-tip distances do not depend on the centre.
    """
    V = largest_component(valid)
    ny, nx = V.shape
    cx, cy = xc / X_MM_PER_PX, yc / Y_MM_PER_PX
    rows = np.arange(int(np.floor(cy - BAND_HALF_MM / Y_MM_PER_PX)), int(np.ceil(cy + BAND_HALF_MM / Y_MM_PER_PX)) + 1)
    cols = np.arange(int(np.floor(cx - BAND_HALF_MM / X_MM_PER_PX)), int(np.ceil(cx + BAND_HALF_MM / X_MM_PER_PX)) + 1)
    lo_x, hi_x, lo_y, hi_y = [], [], [], []
    for r in rows[(rows >= 0) & (rows < ny)]:
        c = np.flatnonzero(V[r])
        if c.size:
            lo_x.append(c.min() * X_MM_PER_PX)
            hi_x.append(c.max() * X_MM_PER_PX)
    for c in cols[(cols >= 0) & (cols < nx)]:
        r = np.flatnonzero(V[:, c])
        if r.size:
            lo_y.append(r.min() * Y_MM_PER_PX)
            hi_y.append(r.max() * Y_MM_PER_PX)
    lo_x, hi_x, lo_y, hi_y = map(np.asarray, (lo_x, hi_x, lo_y, hi_y))
    Wx = float(np.median(hi_x - lo_x)) if lo_x.size else np.nan
    Wy = float(np.median(hi_y - lo_y)) if lo_y.size else np.nan
    # corner tips from the outline
    edge = V & ~ndimage.binary_erosion(V)
    ey, ex = np.nonzero(edge)
    px, py = ex * X_MM_PER_PX, ey * Y_MM_PER_PX
    tips = {}
    for key, (sx, sy) in {"pp": (1, 1), "mm": (-1, -1), "pm": (1, -1), "mp": (-1, 1)}.items():
        proj = (sx * px + sy * py) / np.sqrt(2.0)
        sel = proj >= proj.max() - TIP_WINDOW_MM
        tips[key] = np.array([px[sel].mean(), py[sel].mean()])
    Ld1 = float(np.hypot(*(tips["pp"] - tips["mm"])))
    Ld2 = float(np.hypot(*(tips["pm"] - tips["mp"])))
    return {
        "op10_Wx_mm": Wx, "op10_Wy_mm": Wy,
        "op10_Ld1_mm": Ld1, "op10_Ld2_mm": Ld2,
        "op10_drawin_mid_mm": (2 * BLANK_MM - Wx - Wy) / 4.0,
        "op10_drawin_corner_mm": (2 * BLANK_MM * np.sqrt(2.0) - Ld1 - Ld2) / 4.0,
        # side-wise extents from the cup centre (blank placement shows up here)
        "op10_ext_E_mm": float(np.median(hi_x) - xc) if hi_x.size else np.nan,
        "op10_ext_W_mm": float(xc - np.median(lo_x)) if lo_x.size else np.nan,
        "op10_ext_S_mm": float(np.median(hi_y) - yc) if hi_y.size else np.nan,
        "op10_ext_N_mm": float(yc - np.median(lo_y)) if lo_y.size else np.nan,
        "op10_band_rows": int(lo_x.size), "op10_band_cols": int(lo_y.size),
    }


def flange_waviness(fr: dict, fl: np.ndarray) -> dict:
    X, Y, D = fr["X"][fl] - fr["xc"], fr["Y"][fl] - fr["yc"], fr["D"][fl]
    if D.size < 100:
        return {"op10_wav_sd_mm": np.nan, "op10_wav_p99_mm": np.nan}
    A = np.column_stack([np.ones_like(X), X, Y, X * X, X * Y, Y * Y])
    keep = np.ones(D.size, bool)
    for _ in range(3):
        coef = np.linalg.lstsq(A[keep], D[keep], rcond=None)[0]
        res = D - A @ coef
        keep = np.abs(res) <= 4.0 * max(robust_sd(res), 1e-3)
    return {"op10_wav_sd_mm": robust_sd(res), "op10_wav_p99_mm": float(np.percentile(np.abs(res - np.median(res)), 99))}


def scan_features(h5) -> dict:
    out: dict = {}
    for op in ("op10", "op20"):
        Z, valid = load_scan(h5, op)
        Zd = block_median(Z)
        fr = part_frame(Zd)
        fl = flange_points(fr)
        out[f"{op}_dome_mm"] = fr["dome_mm"]
        out[f"{op}_bottom_tilt_deg"] = fr["plane_tilt_deg"]
        out[f"{op}_n_valid"] = int(valid.sum())
        out[f"{op}_n_flange"] = int(fl.sum())
        out[f"{op}_depth_mm"] = float(np.median(fr["D"][fl])) if fl.any() else np.nan
        out.update(arm_angles(fr, op))
        if op == "op10":
            out.update(extents(valid, fr["xc"], fr["yc"]))
            out.update(flange_waviness(fr, fl))
    return out


# ── driver ───────────────────────────────────────────────────────────────────
def experiment_features(h5) -> dict:
    a = h5.attrs
    row = {
        "index": int(a["id"]), "experiment_id": int(a["experiment_id"]), "category": int(a["category"]),
        "geometry": str(a["geometry"]), "bhf_kN": int(a["blankholder_force"]), "oil_type": str(a["oil_type"]),
        "mean_punch_temp_attr": float(a["mean_punch_temp"]),
    }
    cols = [c.decode() if isinstance(c, bytes) else str(c) for c in h5["force"].attrs["columns"]]
    row.update(force_features(h5["force/data"][:], cols))
    row.update(sheet_features(h5["sheet_thickness/data"][:]))
    if "oil_thickness" in h5:
        row.update(oil_features(h5["oil_thickness/data"][:]))
    if "pointcloud" in h5 and bool(a.get("has_pointcloud", True)):
        row.update(scan_features(h5))
    return row


# The one-per-category sample files live only in sample.zip, not in the two main archives.
SAMPLE_IDS = {0, 500, 1002, 1500, 2000, 2500, 3000, 3500, 4000,
              4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500}


def _member_name(index: int) -> tuple[int, str]:
    if index in SAMPLE_IDS:
        return RDDAC_FILES["sample.zip"], f"{index:04d}.h5"
    zip_id = RDDAC_FILES["concave.zip"] if index < 4500 else RDDAC_FILES["convex.zip"]
    return zip_id, f"{index:04d}.h5"


def _job_remote(index: int) -> dict:
    t0 = time.time()
    try:
        zip_id, name = _member_name(index)
        data = read_member(zip_id, name)
        with h5_from_bytes(data) as h:
            row = experiment_features(h)
        row["status"] = "ok"
    except Exception as exc:  # keep the run going; the row records the failure
        row = {"index": index, "status": f"error: {type(exc).__name__}: {exc}"[:300]}
    row["seconds"] = round(time.time() - t0, 2)
    return row


def run_sample(out: Path) -> pd.DataFrame:
    src = fetch_small(RDDAC_FILES["sample.zip"], CACHE / "rddac_sample.zip")
    rows = []
    with zipfile.ZipFile(src) as z:
        for name in sorted(n for n in z.namelist() if n.endswith(".h5")):
            with h5_from_bytes(z.read(name)) as h:
                r = experiment_features(h)
            r["status"] = "ok"
            rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(out, index=False)
    return df


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sample", action="store_true", help="process the 18 sample files only")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--ids", type=str, default=None, help="e.g. 0-99 or 5,17,4500")
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    if args.sample:
        out = Path(args.out) if args.out else RESULTS / "features_rddac_sample.csv"
        df = run_sample(out)
        print(f"wrote {out} ({len(df)} rows, {df.shape[1]} columns)")
        return

    out = Path(args.out) if args.out else RESULTS / "features_rddac.csv"
    if args.ids:
        sel = set()
        for tok in args.ids.split(","):
            a, _, b = tok.partition("-")
            sel.update(range(int(a), int(b or a) + 1))
        ids = sorted(sel)
    else:
        ids = list(range(9000))
    sample_csv = RESULTS / "features_rddac_sample.csv"
    if not sample_csv.exists():
        run_sample(sample_csv)
    # fixed column order, taken from the complete sample rows
    columns = list(pd.read_csv(sample_csv, nrows=0).columns) + ["seconds"]
    done = set()
    if out.exists():
        prev = pd.read_csv(out, usecols=["index", "status"])
        done = set(prev.loc[prev["status"] == "ok", "index"].astype(int))
    # interleave the 18 cells (500 consecutive ids each) so that partial results stay balanced;
    # within a cell the parts are processed in production order
    todo = sorted((i for i in ids if i not in done), key=lambda i: (i % 500, i))
    print(f"{len(done)} already done, {len(todo)} to go -> {out}", flush=True)
    buf: list[dict] = []
    t0 = time.time()
    with Pool(args.workers) as pool:
        for k, row in enumerate(pool.imap_unordered(_job_remote, todo, chunksize=1), 1):
            buf.append(row)
            if len(buf) >= 20 or k == len(todo):
                atomic_append_rows(out, buf, columns)
                buf = []
            if k % 50 == 0 or k == len(todo):
                el = time.time() - t0
                print(f"{k}/{len(todo)} done, {el / k:.2f} s/part, eta {(len(todo) - k) * el / k / 3600:.2f} h", flush=True)
    if buf:
        atomic_append_rows(out, buf, columns)


if __name__ == "__main__":
    main()
