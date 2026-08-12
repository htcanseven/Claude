"""Assemble window index tables and materialize feature/signal matrices."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .features import window_features
from .windows import window_starts, stationarity_mask, CH_VIB, CH_CUR
from .splits import WindowIndex

FS = 12_800.0
DEFAULT_CHANNELS = CH_VIB + CH_CUR  # exclude keyphase & torque from inputs


def load_run(data_dir: Path, npz_name: str) -> np.ndarray:
    with np.load(data_dir / "converted" / npz_name) as z:
        return z["x"]


def build_index(data_dir: Path, meta: pd.DataFrame, win: int, hop: int,
                compute_stationarity: bool = True,
                label_col: str = "fault_full") -> tuple[WindowIndex, dict, list]:
    """Enumerate windows for every run; returns index + per-run sample counts."""
    runs, starts, labels, conds, stat = [], [], [], [], []
    classes = sorted(meta[label_col].unique())
    cls_to_id = {c: i for i, c in enumerate(classes)}
    n_per_run: dict[int, int] = {}
    for r, row in meta.iterrows():
        x = load_run(data_dir, row["npz"])
        n_per_run[r] = x.shape[1]
        st = window_starts(x.shape[1], win, hop)
        runs.append(np.full(len(st), r))
        starts.append(st)
        labels.append(np.full(len(st), cls_to_id[row[label_col]]))
        conds.append(np.full(len(st), row["condition"], dtype=object))
        if compute_stationarity:
            stat.append(stationarity_mask(x, win, st))
        del x
    idx = WindowIndex(
        run=np.concatenate(runs),
        start=np.concatenate(starts),
        label=np.concatenate(labels),
        condition=np.concatenate(conds),
        stationary=np.concatenate(stat) if compute_stationarity else None,
    )
    return idx, n_per_run, classes


def materialize_features(data_dir: Path, meta: pd.DataFrame, idx: WindowIndex,
                         mask: np.ndarray, win: int,
                         channels=DEFAULT_CHANNELS) -> np.ndarray:
    """Compute the feature matrix for the selected windows, run by run."""
    sel = np.where(mask)[0]
    out = None
    order = np.argsort(idx.run[sel], kind="stable")
    sel = sel[order]
    cur_run, x = -1, None
    for j, i in enumerate(sel):
        r = int(idx.run[i])
        if r != cur_run:
            x = load_run(data_dir, meta.loc[r, "npz"])
            cur_run = r
        f = window_features(x, int(idx.start[i]), win, channels)
        if out is None:
            out = np.empty((len(sel), len(f)), dtype=np.float32)
        out[j] = f
    # restore original order
    inv = np.empty(len(sel), dtype=int)
    inv[np.argsort(sel, kind="stable")] = np.arange(len(sel))
    return out


def materialize_signals(data_dir: Path, meta: pd.DataFrame, idx: WindowIndex,
                        mask: np.ndarray, win: int, decimate: int = 4,
                        channels=DEFAULT_CHANNELS) -> np.ndarray:
    """Raw signal windows (n, ch, win/decimate), simple stride decimation
    after low-pass via block mean."""
    sel = np.where(mask)[0]
    order = np.argsort(idx.run[sel], kind="stable")
    sel_sorted = sel[order]
    n_out = win // decimate
    out = np.empty((len(sel_sorted), len(channels), n_out), dtype=np.float32)
    cur_run, x = -1, None
    for j, i in enumerate(sel_sorted):
        r = int(idx.run[i])
        if r != cur_run:
            x = load_run(data_dir, meta.loc[r, "npz"])
            cur_run = r
        s = int(idx.start[i])
        w = x[list(channels), s:s + win]
        if decimate > 1:
            w = w[:, : n_out * decimate].reshape(len(channels), n_out, decimate).mean(axis=2)
        out[j] = w
    # map back to the order of `sel`
    inv = np.argsort(order, kind="stable")
    return out[inv]
