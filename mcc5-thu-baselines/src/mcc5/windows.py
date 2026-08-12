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
                      rel_thresh: float = 0.15) -> np.ndarray:
    """True where a window is quasi-stationary.

    A window counts as stationary when both the torque channel and the
    speed proxy (RMS of one current phase, tracking the electrical
    fundamental amplitude/frequency changes) vary by less than
    ``rel_thresh`` relative to their run-median absolute level.
    """
    flags = np.zeros(len(starts), dtype=bool)
    torque = x[CH_TORQUE]
    cur = x[CH_CUR[0]]
    t_scale = np.median(np.abs(torque)) + 1e-9

    def _win_rms(sig, s):
        seg = sig[s:s + win]
        k = max(win // 8, 1)
        blocks = seg[: (len(seg) // k) * k].reshape(-1, k)
        return np.sqrt((blocks ** 2).mean(axis=1))

    c_scale = np.sqrt((cur ** 2).mean()) + 1e-9
    for i, s in enumerate(starts):
        t_seg = torque[s:s + win]
        t_var = (t_seg.max() - t_seg.min()) / t_scale
        c_rms = _win_rms(cur, s)
        c_var = (c_rms.max() - c_rms.min()) / c_scale
        flags[i] = (t_var < rel_thresh) and (c_var < rel_thresh)
    return flags
