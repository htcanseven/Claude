"""Windowing and stationarity segmentation.

Windows are cut per run; every window carries its run index so splits can be
made at run level (or with a temporal guard gap) before model training —
never window-shuffled across the split boundary.
"""
from __future__ import annotations

import numpy as np

FS = 12_800.0

# Channels indices in the converted arrays (see convert.CHANNEL_NAMES)
CH_KEYPHASE = 0
CH_TORQUE = 1
CH_VIB = (2, 3, 4)
CH_CUR = (5, 6, 7)


def window_starts(n_samples: int, win: int, hop: int) -> np.ndarray:
    if n_samples < win:
        return np.empty(0, dtype=int)
    return np.arange(0, n_samples - win + 1, hop)


def stationarity_mask(x: np.ndarray, win: int, starts: np.ndarray,
                      rpm: np.ndarray | None = None,
                      speed_thresh: float = 0.05,
                      torque_thresh: float = 0.15,
                      fs: float = FS) -> np.ndarray:
    """True where a window is quasi-stationary in BOTH speed and load.

    Speed comes from the key-phase tachometer (1 pulse/rev), not from a current
    proxy: current amplitude tracks load, so under a constant-torque speed ramp
    a current-based proxy stays flat and would wrongly mark ramp windows as
    steady. A window is stationary when the shaft speed varies by less than
    ``speed_thresh`` and the torque by less than ``torque_thresh``, both
    relative to their own level within the window.
    """
    from .physics import speed_series

    flags = np.zeros(len(starts), dtype=bool)
    torque = x[CH_TORQUE]
    if rpm is None:
        rpm = speed_series(x[CH_KEYPHASE], fs)
    t_scale = np.median(np.abs(torque)) + 1e-9

    for i, s in enumerate(starts):
        t_seg = torque[s:s + win]
        t_var = (t_seg.max() - t_seg.min()) / t_scale
        r_seg = rpm[s:s + win]
        r_mean = r_seg.mean()
        r_var = (r_seg.max() - r_seg.min()) / (abs(r_mean) + 1e-9)
        flags[i] = (t_var < torque_thresh) and (r_var < speed_thresh)
    return flags
