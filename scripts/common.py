"""Shared constants and helpers for the RDDAC / DDACS pipeline.

Every number that is fixed once for the whole study lives here, so that no
script types it again. Raw data are read from DaRUS (University of Stuttgart)
file by file through HTTP range requests, so the 87 GB experimental archive
and the 647 GB simulation archive never have to be stored locally.

Data:
    RDDAC  doi:10.18419/DARUS-5589 (CC BY 4.0), version 2.0
    DDACS  doi:10.18419/DARUS-4801 (CC BY 4.0), version 3.0
"""

from __future__ import annotations

import io
import os
import threading
import time
from pathlib import Path

import numpy as np
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CACHE = RESULTS / "cache"          # git-ignored downloads of small index files
FIGURES = RESULTS / "figures"

# ── DaRUS file ids (stable within the dataset versions above) ────────────────
DARUS = "https://darus.uni-stuttgart.de/api/access/datafile/{}"
RDDAC_FILES = {
    "concave.zip": 659883,          # 45.2 GB, experiments 0000-4499
    "convex.zip": 659884,           # 41.6 GB, experiments 4500-8999
    "sample.zip": 659885,           # one experiment per category
    "process_parameters": 659888,   # index (tab; '?format=original' gives the csv)
}
DDACS_FILES = {
    "rddac.zip": 566636,            # the 396 simulations matched to RDDAC
    "process_parameters": 566626,
    "sample": 565787,               # 258864.zip
}

# ── Scanner calibration (rddac 2.0.0, calibration.json) ──────────────────────
X_MM_PER_PX = 0.07692307692307693   # along the 3200 columns
Y_MM_PER_PX = 0.1581                # along the 2000 lines
Z_MM_PER_UNIT = 0.007754506005746317
LUMI_MIN_PATCH = 20040              # px; connected-component filter (rddac default)

# ── Nominal process geometry ─────────────────────────────────────────────────
BLANK_MM = 210.0                    # square blank edge (DDACS initial mesh: quarter of 105 mm)
FORCE_WINDOW_S = (0.25, 2.25)       # forming window of the 300 Hz force record (rddac default)
SHEET_LAST_N = 200                  # stable part of the thickness traverse (rddac default)
OIL_MAX_POS_MM = 200                # oil traverse beyond this is edge artefact (rddac default)
# Oil film -> friction coefficient used to match a simulation (rddac 2.0.0):
OIL_MIN_GM2, OIL_MAX_GM2 = 0.8, 1.6
FC_MAX, FC_MIN = 0.15, 0.05

# ── Quality-characteristic extraction (this study) ───────────────────────────
BAND_HALF_MM = 2.0                  # half-width of the bands used for flange extents
ARM_BAND_HALF_MM = 5.0              # half-width of the arm centre-line bands (OP20)
PLATEAU_MIN_DEPTH_MM = 25.0         # a pixel belongs to the cup bottom beyond this depth
FLANGE_MAX_DEPTH_MM = 3.0           # a pixel belongs to the flange within this depth
FLANGE_WALL_CLEARANCE_MM = 8.0      # flange pixels this close to the cup are excluded
PLATEAU_CORE_CLEARANCE_MM = 10.0    # plateau pixels this close to its edge are excluded


def oil_to_friction(oil_gm2: float) -> float:
    """Friction coefficient for an oil-film density (linear, clamped), as in rddac."""
    oil = float(np.clip(oil_gm2, OIL_MIN_GM2, OIL_MAX_GM2))
    return FC_MAX - (oil - OIL_MIN_GM2) * (FC_MAX - FC_MIN) / (OIL_MAX_GM2 - OIL_MIN_GM2)


# ── Remote archive access ────────────────────────────────────────────────────
_LOCAL = threading.local()


def remote_zip(file_id: int):
    """A per-thread/process RemoteZip over a DaRUS file (range requests)."""
    from remotezip import RemoteZip

    cache = getattr(_LOCAL, "zips", None)
    if cache is None:
        cache = _LOCAL.zips = {}
    if file_id not in cache:
        cache[file_id] = RemoteZip(DARUS.format(file_id))
    return cache[file_id]


def read_member(file_id: int, name: str, retries: int = 5) -> bytes:
    """Read one archive member, retrying with back-off on network errors."""
    for attempt in range(retries):
        try:
            return remote_zip(file_id).read(name)
        except Exception:
            if attempt == retries - 1:
                raise
            getattr(_LOCAL, "zips", {}).pop(file_id, None)   # reopen on the next try
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def fetch_small(file_id: int, dest: Path, original: bool = False) -> Path:
    """Download a small DaRUS file once into the cache directory."""
    import urllib.request

    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        url = DARUS.format(file_id) + ("?format=original" if original else "")
        with urllib.request.urlopen(url, timeout=300) as r, open(dest, "wb") as f:
            f.write(r.read())
    return dest


def h5_from_bytes(data: bytes):
    import h5py

    return h5py.File(io.BytesIO(data), "r")


# ── Image helpers ────────────────────────────────────────────────────────────
def lumi_valid_mask(lumi: np.ndarray, min_patch: int = LUMI_MIN_PATCH) -> np.ndarray:
    """Pixels on a large connected luminescence patch (rddac's surface mask)."""
    fg = lumi > 0
    lab, n = ndimage.label(fg)
    if n == 0:
        return np.zeros_like(fg)
    sizes = ndimage.sum(fg, lab, index=np.arange(1, n + 1))
    keep = np.flatnonzero(sizes >= min_patch) + 1
    return np.isin(lab, keep)


def robust_plane(x: np.ndarray, y: np.ndarray, z: np.ndarray, n_iter: int = 4, k: float = 3.0):
    """Least-squares plane z = a + b x + c y with iterative MAD trimming."""
    keep = np.ones(len(z), dtype=bool)
    coef = np.zeros(3)
    for _ in range(n_iter):
        A = np.column_stack([np.ones(keep.sum()), x[keep], y[keep]])
        coef, *_ = np.linalg.lstsq(A, z[keep], rcond=None)
        res = z - (coef[0] + coef[1] * x + coef[2] * y)
        mad = 1.4826 * np.median(np.abs(res[keep] - np.median(res[keep])))
        if mad == 0:
            break
        keep = np.abs(res) <= k * mad
    return coef


def robust_sd(v: np.ndarray) -> float:
    v = v[np.isfinite(v)]
    if v.size == 0:
        return float("nan")
    return float(1.4826 * np.median(np.abs(v - np.median(v))))


def atomic_append_rows(path: Path, rows: list[dict], columns: list[str]) -> None:
    """Append rows to a CSV, writing the header when the file is new."""
    import csv

    new = not path.exists()
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        if new:
            w.writeheader()
        for r in rows:
            w.writerow(r)
        f.flush()
        os.fsync(f.fileno())
