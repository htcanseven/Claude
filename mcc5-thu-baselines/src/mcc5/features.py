"""Classic time- and frequency-domain features per window and channel."""
from __future__ import annotations

import numpy as np
from scipy import stats
from scipy.fft import rfft, rfftfreq

FS = 12_800.0

TIME_FEATURES = ["rms", "std", "kurtosis", "skew", "crest", "p2p",
                 "shape", "impulse"]
FREQ_FEATURES = ["centroid", "bandwidth"] + [f"band{i}" for i in range(8)]


def time_features(w: np.ndarray) -> np.ndarray:
    rms = np.sqrt((w ** 2).mean()) + 1e-12
    mean_abs = np.abs(w).mean() + 1e-12
    peak = np.abs(w).max()
    return np.array([
        rms,
        w.std(),
        stats.kurtosis(w),
        stats.skew(w),
        peak / rms,               # crest factor
        w.max() - w.min(),        # peak-to-peak
        rms / mean_abs,           # shape factor
        peak / mean_abs,          # impulse factor
    ])


def freq_features(w: np.ndarray, fs: float = FS, n_bands: int = 8) -> np.ndarray:
    spec = np.abs(rfft(w - w.mean()))
    freqs = rfftfreq(len(w), 1.0 / fs)
    p = spec ** 2
    ptot = p.sum() + 1e-12
    centroid = (freqs * p).sum() / ptot
    bandwidth = np.sqrt(((freqs - centroid) ** 2 * p).sum() / ptot)
    # log energy in n_bands equal bands
    edges = np.linspace(0, len(p), n_bands + 1, dtype=int)
    bands = np.array([np.log(p[a:b].sum() + 1e-12)
                      for a, b in zip(edges[:-1], edges[1:])])
    return np.concatenate([[centroid, bandwidth], bands])


def window_features(x: np.ndarray, start: int, win: int,
                    channels: tuple[int, ...]) -> np.ndarray:
    """Feature vector for one window: per-channel time+freq features."""
    feats = []
    for c in channels:
        w = x[c, start:start + win].astype(np.float64)
        feats.append(time_features(w))
        feats.append(freq_features(w))
    return np.concatenate(feats)


def feature_names(channels: tuple[int, ...], ch_names: list[str]) -> list[str]:
    names = []
    for c in channels:
        names += [f"{ch_names[c]}_{f}" for f in TIME_FEATURES]
        names += [f"{ch_names[c]}_{f}" for f in FREQ_FEATURES]
    return names
