"""Stream-convert the dataset zips: CSV runs -> compact float32 .npz.

Each run is stored as ``converted/<stem>.npz`` containing:
    x   float32 array (n_channels, n_samples) — all columns except time
    fs  sampling rate (Hz)

A ``metadata.csv`` row is written per run with the parsed labels.
CSVs are streamed one at a time straight from the zip (never written to disk),
so peak disk usage stays near the zip size plus the compact .npz output.
"""
from __future__ import annotations

import io
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

from .metadata import parse_filename

FS = 12_800.0

# Column meaning per the dataset paper (Table 4); first column is time.
CHANNEL_NAMES = [
    "keyphase", "torque",
    "vib_de_h", "vib_de_ax", "vib_de_v",
    "cur_a", "cur_b", "cur_c",
]


def _read_csv_bytes(raw: bytes) -> np.ndarray:
    """Read a run CSV, tolerating with/without header, return (N, k>=8)."""
    df = pd.read_csv(io.BytesIO(raw), header=None, low_memory=False)
    # Drop a header row if the first row isn't numeric
    first = pd.to_numeric(df.iloc[0], errors="coerce")
    if first.isna().any():
        df = df.iloc[1:]
    arr = df.apply(pd.to_numeric, errors="coerce").to_numpy(dtype=np.float64)
    # Drop all-NaN trailing columns (ragged CSV artifacts)
    keep = ~np.all(np.isnan(arr), axis=0)
    arr = arr[:, keep]
    # Drop rows with NaN
    arr = arr[~np.isnan(arr).any(axis=1)]
    return arr


def convert_zip(zip_path: Path, out_dir: Path) -> None:
    """Convert every CSV in a zip to a float32 .npz (idempotent, resumable)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if n.lower().endswith(".csv")]
        print(f"{zip_path.name}: {len(names)} csv files")
        for i, name in enumerate(names, 1):
            stem = Path(name).stem
            dest = out_dir / f"{stem}.npz"
            if dest.exists():
                print(f"  [{i}/{len(names)}] {stem}: cached", flush=True)
                continue
            arr = _read_csv_bytes(zf.read(name))
            # First column is the time axis -> drop; the rest are channels.
            x = np.ascontiguousarray(arr[:, 1:].T, dtype=np.float32)
            tmp = out_dir / f"{stem}.tmp.npz"
            # Write through a file handle so numpy uses the name verbatim
            # (passing a path, it would append a second ".npz").
            with open(tmp, "wb") as fh:
                np.savez_compressed(fh, x=x, fs=FS)
            tmp.replace(dest)  # atomic: a partial file never looks complete
            print(f"  [{i}/{len(names)}] {stem}: {x.shape}", flush=True)


def build_metadata(data_dir: Path) -> pd.DataFrame:
    """Scan converted/*.npz and (re)build metadata.csv from filenames."""
    out_dir = data_dir / "converted"
    rows: list[dict] = []
    for npz in sorted(out_dir.glob("*.npz")):
        stem = npz.stem
        with np.load(npz) as z:
            n_ch, n_smp = z["x"].shape
        try:
            row = parse_filename(stem).to_dict()
        except ValueError:
            row = {"file": stem, "fault_full": "UNPARSED", "components": "",
                   "is_compound": False, "profile": "", "torque_nm": 0.0,
                   "speed_rpm": 0, "condition": ""}
        row.update(n_channels=n_ch, n_samples=n_smp, npz=npz.name)
        rows.append(row)
    meta = pd.DataFrame(rows)
    meta_path = data_dir / "metadata.csv"
    meta.to_csv(meta_path, index=False)
    print(f"metadata: {len(meta)} runs -> {meta_path}")
    return meta


def convert_all(data_dir: Path, keep_csv: bool = False) -> pd.DataFrame:
    out_dir = data_dir / "converted"
    for zip_name in ("speed_circulation.zip", "torque_circulation.zip"):
        zp = data_dir / zip_name
        if zp.exists():
            convert_zip(zp, out_dir)
        else:
            print(f"warning: {zp} not found, skipping")
    return build_metadata(data_dir)
