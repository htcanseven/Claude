"""Quality characteristics of the DDACS forming simulations.

Computes, from the final node positions of the blank, the same quantities that
``features_rddac.py`` measures on the scanned parts: flange extents across the
mid-lines and between the corner tips (draw-in), cup depth, flange waviness,
flange and arm inclinations along the mid-lines, wall position and angle, and
the dome of the cup bottom; plus simulation-only quantities (thinning,
plastic strain). The simulations model one quarter of the part; it is
mirrored into the full part.

Sets:
    rddac    the 396 simulations matched to the RDDAC experiments (rddac.zip)
    corners  the DDACS design corners near the RDDAC process window (streamed
             from the 18 DDACS packages; see --corners)

Usage:
    python scripts/features_ddacs.py --set rddac --workers 2
"""

from __future__ import annotations

import argparse
import sys
import time
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import (  # noqa: E402
    BLANK_MM,
    CACHE,
    DDACS_FILES,
    FLANGE_WALL_CLEARANCE_MM,
    PLATEAU_CORE_CLEARANCE_MM,
    RESULTS,
    atomic_append_rows,
    fetch_small,
    h5_from_bytes,
    read_member,
    remote_zip,
    robust_sd,
)
from features_rddac import ARM_BAND_HALF_MM, flat_segment, wall_measures  # noqa: E402

SIM_BIN_MM = 1.0            # node spacing is about 1 mm
SIM_DIRS = {"x": (1.0, 0.0), "y": (0.0, 1.0)}   # quarter model: the two mid-line arms


def mirror(p: np.ndarray) -> np.ndarray:
    x, y, z = p[:, 0], p[:, 1], p[:, 2]
    return np.column_stack([np.r_[x, -x, x, -x], np.r_[y, y, -y, -y], np.r_[z, z, z, z]])


def frame(p_full: np.ndarray) -> dict:
    """Cup-bottom datum: depth D of every node below the bottom plane (flange ~ +30).

    In DDACS the punch is fixed and the die moves down, so the cup bottom stays
    at the initial blank height and is the highest part of the blank, as it is
    in the scans; D and the dome are therefore defined exactly as there.
    """
    z = p_full[:, 2]
    bottom = z > z.max() - 0.5
    r = np.hypot(p_full[:, 0], p_full[:, 1])
    rb = np.percentile(r[bottom], 99)
    core = bottom & (r <= rb - PLATEAU_CORE_CLEARANCE_MM)
    A = np.column_stack([np.ones(core.sum()), p_full[core, 0], p_full[core, 1]])
    a, b, c = np.linalg.lstsq(A, z[core], rcond=None)[0]
    D = (a + b * p_full[:, 0] + c * p_full[:, 1]) - z
    xr, yr = p_full[core, 0], p_full[core, 1]
    k = np.linalg.lstsq(np.column_stack([np.ones(core.sum()), xr, yr, xr ** 2 + yr ** 2]), z[core], rcond=None)[0][3]
    return {"D": D, "core": core, "dome_mm": float(k * 40.0 ** 2)}


def op_features(p_quarter: np.ndarray, prefix: str, extents: bool) -> dict:
    out: dict = {}
    P = mirror(p_quarter)
    fr = frame(P)
    D = fr["D"]
    out[f"{prefix}_dome_mm"] = fr["dome_mm"]
    # flange nodes clear of the die radius
    cup = D < 20.0
    flange = ~cup & (D <= 40.0)
    if cup.any() and flange.any():
        dist = cKDTree(P[cup, :2]).query(P[flange, :2])[0]
        fl_idx = np.flatnonzero(flange)[dist >= FLANGE_WALL_CLEARANCE_MM]
    else:
        fl_idx = np.array([], int)
    out[f"{prefix}_depth_mm"] = float(np.median(D[fl_idx])) if fl_idx.size else np.nan
    thetas = []
    for name, (ux, uy) in SIM_DIRS.items():
        r = P[:, 0] * ux + P[:, 1] * uy
        lat = np.abs(-P[:, 0] * uy + P[:, 1] * ux)
        band = (lat <= ARM_BAND_HALF_MM) & (r > 0)
        out.update(wall_measures(r[band], D[band], f"{prefix}_{{}}_{name}", bin_mm=SIM_BIN_MM))
        flat = band & (D >= 20.0)
        seg = flat_segment(r[flat], D[flat], bin_mm=SIM_BIN_MM) if flat.sum() >= 10 else None
        keys = (f"{prefix}_theta_{name}_deg", f"{prefix}_rise_{name}_mm", f"{prefix}_seg_{name}_mm")
        if seg is None:
            out.update(dict.fromkeys(keys, np.nan))
            continue
        m = flat & (r >= seg[0]) & (r <= seg[1])
        p = np.polyfit(r[m], D[m], 1)
        th = float(np.degrees(np.arctan(p[0])))
        out[keys[0]], out[keys[1]], out[keys[2]] = th, float(p[0] * (seg[1] - seg[0])), float(seg[1] - seg[0])
        thetas.append(th)
    out[f"{prefix}_theta_mean_deg"] = float(np.mean(thetas)) if thetas else np.nan
    if extents:
        q = p_quarter
        Wx = 2.0 * q[q[:, 1] < 1.0, 0].max()
        Wy = 2.0 * q[q[:, 0] < 1.0, 1].max()
        proj = (q[:, 0] + q[:, 1]) / np.sqrt(2.0)
        tip = q[np.argmax(proj), :2]
        Ld = 2.0 * float(np.hypot(*tip))
        out.update({
            f"{prefix}_Wx_mm": float(Wx), f"{prefix}_Wy_mm": float(Wy), f"{prefix}_Ld_mm": Ld,
            f"{prefix}_drawin_mid_mm": (2 * BLANK_MM - Wx - Wy) / 4.0,
            f"{prefix}_drawin_corner_mm": (BLANK_MM * np.sqrt(2.0) - Ld) / 2.0,
        })
        if fl_idx.size > 50:
            X, Y, d = P[fl_idx, 0], P[fl_idx, 1], D[fl_idx]
            A = np.column_stack([np.ones_like(X), X, Y, X * X, X * Y, Y * Y])
            res = d - A @ np.linalg.lstsq(A, d, rcond=None)[0]
            out[f"{prefix}_wav_sd_mm"] = robust_sd(res)
        else:
            out[f"{prefix}_wav_sd_mm"] = np.nan
    return out


def sim_features(h5) -> dict:
    a = h5.attrs
    row = {k: (a[k].decode() if isinstance(a[k], bytes) else a[k].item() if hasattr(a[k], "item") else a[k])
           for k in a.keys()}
    p10 = h5["OP10/blank/node_displacement"][-1]
    p20 = h5["OP20/blank/node_displacement"][-1]
    row.update(op_features(np.asarray(p10, float), "op10", extents=True))
    row.update(op_features(np.asarray(p20, float), "op20", extents=False))
    t10 = h5["OP10/blank/element_shell_thickness"]
    t0 = float(np.median(t10[0]))
    row["sim_thin_min_ratio"] = float(np.min(t10[-1]) / t0)
    row["sim_thick_max_ratio"] = float(np.max(t10[-1]) / t0)
    eps = h5["OP10/blank/element_shell_effective_plastic_strain"][-1]
    row["sim_eps_max"] = float(np.max(eps))
    # OP20 springback: largest node movement during the final springback step
    d20 = h5["OP20/blank/node_displacement"]
    row["sim_op20_springback_max_mm"] = float(np.max(np.linalg.norm(d20[-1] - d20[0], axis=1)))
    return row


def _job(args: tuple) -> dict:
    file_id, member = args
    t0 = time.time()
    try:
        with h5_from_bytes(read_member(file_id, member)) as h:
            row = sim_features(h)
        row["status"] = "ok"
    except Exception as exc:
        row = {"member": member, "status": f"error: {type(exc).__name__}: {exc}"[:300]}
    row["member"] = member
    row["seconds"] = round(time.time() - t0, 2)
    return row


def run(jobs: list[tuple], out: Path, workers: int) -> None:
    done = set()
    if out.exists():
        prev = pd.read_csv(out, usecols=["member", "status"])
        done = set(prev.loc[prev["status"] == "ok", "member"])
    todo = [j for j in jobs if j[1] not in done]
    print(f"{len(done)} done, {len(todo)} to go -> {out}", flush=True)
    if not todo:
        return
    # fixed column order from one complete simulation
    columns = list(_job(todo[0]).keys())
    buf, t0 = [], time.time()
    with Pool(workers) as pool:
        for k, row in enumerate(pool.imap_unordered(_job, todo, chunksize=1), 1):
            buf.append(row)
            if len(buf) >= 10 or k == len(todo):
                atomic_append_rows(out, buf, columns)
                buf = []
            if k % 20 == 0 or k == len(todo):
                el = time.time() - t0
                print(f"{k}/{len(todo)}, {el / k:.1f} s/sim, eta {(len(todo) - k) * el / k / 60:.0f} min", flush=True)


CORNER_SELECTION = {          # DDACS design corners at the RDDAC process conditions
    "geometry": ["concave", "convex"],
    "material_scaling_factor": [1.0],
    "sheet_metal_thickness": [0.98, 0.99],
    "blankholder_force": [100000.0, 300000.0, 500000.0],
}


def ddacs_packages() -> list[tuple[int, int, int]]:
    """(first index, last index, DaRUS file id) of the DDACS simulation packages."""
    import json
    import urllib.request

    cache = CACHE / "ddacs_files.json"
    if not cache.exists():
        url = ("https://darus.uni-stuttgart.de/api/datasets/:persistentId/"
               "?persistentId=doi:10.18419/DARUS-4801")
        with urllib.request.urlopen(url, timeout=120) as r:
            files = json.load(r)["data"]["latestVersion"]["files"]
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps([{"name": f["dataFile"]["filename"], "id": f["dataFile"]["id"]} for f in files]))
    out = []
    for f in json.loads(cache.read_text()):
        stem = f["name"].removesuffix(".zip")
        if "_" in stem and all(p.isdigit() for p in stem.split("_")):
            a, b = map(int, stem.split("_"))
            out.append((a, b, int(f["id"])))
    return sorted(out)


def corner_jobs() -> list[tuple[int, str]]:
    p = pd.read_csv(fetch_small(DDACS_FILES["process_parameters"], CACHE / "ddacs_process_parameters.csv",
                                original=True))
    sel = p[~p["rddac"]]
    for col, vals in CORNER_SELECTION.items():
        sel = sel[sel[col].isin(vals)]
    packs = ddacs_packages()
    jobs = []
    for idx in sel["index"].astype(int):
        fid = next((f for a, b, f in packs if a <= idx <= b), None)
        if fid is not None:
            jobs.append((fid, f"{idx}.h5"))
    return jobs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", choices=["rddac", "corners", "sample"], default="rddac")
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    if args.set == "corners":
        jobs = corner_jobs()
        print(f"corners: {len(jobs)} simulations")
        run(jobs, RESULTS / "features_ddacs_corners.csv", args.workers)
        return
    if args.set == "sample":
        import zipfile

        src = fetch_small(DDACS_FILES["sample"], CACHE / "ddacs_258864.zip")
        with zipfile.ZipFile(src) as z, h5_from_bytes(z.read("258864.h5")) as h:
            row = sim_features(h)
        print(pd.Series(row).to_string())
        return
    zid = DDACS_FILES["rddac.zip"]
    members = sorted(i.filename for i in remote_zip(zid).infolist() if i.filename.endswith(".h5"))
    print(f"rddac.zip: {len(members)} simulations")
    run([(zid, m) for m in members], RESULTS / "features_ddacs_rddac.csv", args.workers)


if __name__ == "__main__":
    main()
