"""Precompute window features (and optionally decimated raw windows) once.

Every protocol then reuses the same cache by boolean masking, so the
expensive FFT/feature work happens exactly once per dataset instead of once
per protocol/fold.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd

from .features import (window_features, feature_names, order_features,
                       order_feature_names, condition_features,
                       CONDITION_FEATURES)
from .convert import CHANNEL_NAMES
from .physics import speed_series, shaft_angle
from .windows import (window_starts, stationarity_mask, CH_VIB, CH_CUR,
                      CH_KEYPHASE)

DEFAULT_CHANNELS = CH_VIB + CH_CUR


def _process_run(args):
    """Worker: features + stationarity + raw windows for one run."""
    (data_dir, npz_name, run_id, win, hop, channels, decimate,
     want_signals, want_physics) = args
    with np.load(Path(data_dir) / "converted" / npz_name) as z:
        x = z["x"]
    starts = window_starts(x.shape[1], win, hop)
    feats = np.stack([window_features(x, int(s), win, channels)
                      for s in starts]).astype(np.float32)
    # Speed and shaft angle are derived once for the whole run: the tachometer
    # threshold is then set from the run's real pulse amplitude, not from the
    # noise inside a window recorded before the shaft starts turning.
    rpm = speed_series(x[CH_KEYPHASE])
    stat = stationarity_mask(x, win, starts, rpm=rpm)
    ofeats = cfeats = None
    if want_physics:
        angle = shaft_angle(x[CH_KEYPHASE])
        ofeats = np.stack([order_features(x, int(s), win, channels, angle)
                           for s in starts]).astype(np.float32)
        cfeats = np.stack([condition_features(x, int(s), win, rpm)
                           for s in starts]).astype(np.float32)
    sig = None
    if want_signals:
        n_out = win // decimate
        sig = np.empty((len(starts), len(channels), n_out), dtype=np.float32)
        for i, s in enumerate(starts):
            w = x[list(channels), int(s):int(s) + win]
            if decimate > 1:
                w = (w[:, : n_out * decimate]
                     .reshape(len(channels), n_out, decimate).mean(axis=2))
            sig[i] = w
    return run_id, starts, feats, stat, sig, x.shape[1], ofeats, cfeats


def build_cache(data_dir: Path, meta: pd.DataFrame, win: int, hop: int,
                channels=DEFAULT_CHANNELS, decimate: int = 4,
                want_signals: bool = True, want_physics: bool = True,
                workers: int = 4, label_col: str = "fault_full") -> dict:
    classes = sorted(meta[label_col].unique())
    cls_to_id = {c: i for i, c in enumerate(classes)}

    tasks = [(str(data_dir), row["npz"], r, win, hop, channels, decimate,
              want_signals, want_physics) for r, row in meta.iterrows()]

    runs, starts, feats, stats, sigs = [], [], [], [], []
    ofeats_all, cfeats_all = [], []
    labels, conds = [], []
    n_per_run: dict[int, int] = {}

    with ProcessPoolExecutor(max_workers=workers) as ex:
        for k, out in enumerate(ex.map(_process_run, tasks), 1):
            run_id, st, f, stat, sig, n_smp, ofe, cfe = out
            n_per_run[int(run_id)] = int(n_smp)
            runs.append(np.full(len(st), run_id))
            starts.append(st)
            feats.append(f)
            stats.append(stat)
            if want_signals:
                sigs.append(sig)
            if want_physics:
                ofeats_all.append(ofe)
                cfeats_all.append(cfe)
            row = meta.loc[run_id]
            labels.append(np.full(len(st), cls_to_id[row[label_col]]))
            conds.append(np.full(len(st), row["condition"], dtype=object))
            print(f"  cached [{k}/{len(tasks)}] run {run_id}: {len(st)} windows",
                  flush=True)

    cache = dict(
        run=np.concatenate(runs),
        start=np.concatenate(starts),
        label=np.concatenate(labels),
        condition=np.concatenate(conds),
        stationary=np.concatenate(stats),
        features=np.concatenate(feats, axis=0),
        feature_names=feature_names(channels, CHANNEL_NAMES),
        classes=classes,
        n_per_run=n_per_run,
        win=win, hop=hop, decimate=decimate,
        channels=list(channels),
    )
    if want_signals:
        cache["signals"] = np.concatenate(sigs, axis=0)
    if want_physics:
        cache["order_features"] = np.concatenate(ofeats_all, axis=0)
        cache["order_feature_names"] = order_feature_names(channels,
                                                           CHANNEL_NAMES)
        cache["cond_features"] = np.concatenate(cfeats_all, axis=0)
        cache["cond_feature_names"] = CONDITION_FEATURES
    return cache


def save_cache(cache: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    sig = cache.pop("signals", None)
    np.savez(out_dir / "window_cache.npz",
             **{k: v for k, v in cache.items() if k != "n_per_run"},
             n_per_run_keys=np.array(list(cache["n_per_run"].keys())),
             n_per_run_vals=np.array(list(cache["n_per_run"].values())))
    if sig is not None:
        # plain .npy so it can be memory-mapped when training
        np.save(out_dir / "window_signals.npy", sig)
        cache["signals"] = sig
    print(f"cache -> {out_dir / 'window_cache.npz'}"
          + (f" + window_signals.npy {sig.shape}" if sig is not None else ""))


def load_cache(out_dir: Path, mmap_signals: bool = True) -> dict:
    with np.load(out_dir / "window_cache.npz", allow_pickle=True) as z:
        cache = {k: z[k] for k in z.files}
    cache["n_per_run"] = dict(zip(cache.pop("n_per_run_keys").tolist(),
                                  cache.pop("n_per_run_vals").tolist()))
    cache["classes"] = [str(c) for c in cache["classes"]]
    cache["win"] = int(cache["win"])
    sig_path = out_dir / "window_signals.npy"
    if sig_path.exists():
        cache["signals"] = np.load(sig_path,
                                   mmap_mode="r" if mmap_signals else None)
    return cache
