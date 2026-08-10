"""Data I/O for the smartphone-MEMS induction-motor vibration dataset.

Dataset: Ertargin et al., Data in Brief 67 (2026) 112916.
Mendeley Data DOI 10.17632/rs4vz8n3t5.1 (version 1).

Files: data/raw/<CLASS>/<CLASS>_<LOAD>_<SPEED>Hz.csv  (36 recordings)
CSV: ';'-delimited, header  gX;gY;gZ;gUserX;gUserY;gUserZ  ; fs = 100 Hz ; 15 min.
"""
from __future__ import annotations

import os
import glob
import re
from dataclasses import dataclass

import numpy as np
import pandas as pd

# --- Dataset constants -------------------------------------------------------
FS = 100.0  # Hz, fixed sampling rate of the smartphone app
RAW_CHANNELS = ["gX", "gY", "gZ"]                 # raw tri-axial acceleration
USER_CHANNELS = ["gUserX", "gUserY", "gUserZ"]    # gravity-compensated linear accel.
CHANNELS = RAW_CHANNELS + USER_CHANNELS

# 6 health states. Order fixed for reproducible label indexing.
CLASSES = ["H", "B1", "B2", "B3", "V", "R"]
CLASS_NAME = {
    "H":  "Healthy",
    "B1": "Insufficient lubrication",
    "B2": "Severe insufficient lubrication",
    "B3": "Cracked outer ring",
    "V":  "Voltage imbalance",
    "R":  "Broken rotor bar",
}
CLASS_TO_IDX = {c: i for i, c in enumerate(CLASSES)}
SPEEDS = [30, 40, 50]
LOADS = [0, 1]  # 0 = unloaded, 1 = loaded

DEFAULT_RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")

_FNAME_RE = re.compile(r"^(?P<cls>H|B1|B2|B3|V|R)_(?P<load>[01])_(?P<speed>30|40|50)Hz$")


@dataclass(frozen=True)
class Recording:
    """Metadata + path for one 15-minute recording (one operating condition)."""
    path: str
    cls: str          # health class code
    load: int         # 0/1
    speed: int        # 30/40/50 Hz
    label: int        # class index

    @property
    def name(self) -> str:
        return f"{self.cls}_{self.load}_{self.speed}Hz"

    @property
    def group_id(self) -> str:
        """Unique recording id used for group-aware (leakage-free) splitting."""
        return self.name


def parse_filename(path: str) -> Recording | None:
    stem = os.path.splitext(os.path.basename(path))[0]
    m = _FNAME_RE.match(stem)
    if not m:
        return None
    cls = m.group("cls")
    return Recording(
        path=path,
        cls=cls,
        load=int(m.group("load")),
        speed=int(m.group("speed")),
        label=CLASS_TO_IDX[cls],
    )


def list_recordings(raw_dir: str = DEFAULT_RAW_DIR, ext: str = "csv") -> list[Recording]:
    """Return all recordings, sorted deterministically by (class, load, speed)."""
    paths = glob.glob(os.path.join(raw_dir, "**", f"*.{ext}"), recursive=True)
    recs = [r for r in (parse_filename(p) for p in paths) if r is not None]
    recs.sort(key=lambda r: (CLASS_TO_IDX[r.cls], r.load, r.speed))
    return recs


def load_signal(rec: Recording, channels: list[str] | None = None) -> np.ndarray:
    """Load one recording as an (N, C) float32 array in canonical channel order."""
    channels = channels or CHANNELS
    df = pd.read_csv(rec.path, sep=";", usecols=channels, dtype=np.float32)
    # enforce column order
    return df[channels].to_numpy(dtype=np.float32)
