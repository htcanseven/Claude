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


# --- physics-guided order-domain features -------------------------------

ORDER_TARGETS = ["BPFO", "BPFI", "BSF", "shaft1", "shaft2", "shaft3"]


def order_features(x: np.ndarray, start: int, win: int,
                   channels: tuple[int, ...], angle: np.ndarray,
                   fs: float = FS) -> np.ndarray:
    """Envelope-order band energies at the bearing and shaft orders.

    Speed-invariant by construction: the window is resampled onto the shaft
    angle, so a fault sits at the same order at 1000 and 3000 rpm. ``angle`` is
    the run-level cumulative shaft angle (revolutions), sliced here.
    """
    from .physics import (envelope_order_spectrum, order_band_energy,
                          BEARING_ORDERS)

    ang = angle[start:start + win]
    feats = []
    for c in channels:
        w = x[c, start:start + win].astype(np.float64)
        orders, amp = envelope_order_spectrum(w, ang, fs=fs)
        if len(orders) == 0:
            feats.append(np.zeros(len(ORDER_TARGETS)))
            continue
        tot = float((amp ** 2).sum()) + 1e-12
        vals = [order_band_energy(orders, amp, BEARING_ORDERS[k]) / tot
                for k in ("BPFO", "BPFI", "BSF")]
        vals += [order_band_energy(orders, amp, float(k)) / tot
                 for k in (1, 2, 3)]
        feats.append(np.asarray(vals))
    return np.concatenate(feats)


def order_feature_names(channels: tuple[int, ...],
                        ch_names: list[str]) -> list[str]:
    return [f"{ch_names[c]}_ord_{t}" for c in channels for t in ORDER_TARGETS]


def condition_features(x: np.ndarray, start: int, win: int,
                       rpm: np.ndarray, torque_ch: int = 1) -> np.ndarray:
    """Operating-condition descriptors: mean/range of speed and torque.

    Kept separate from the fault features on purpose — these are the auxiliary
    target for condition-disentanglement, not inputs to the fault classifier.
    ``rpm`` is the run-level per-sample speed series, sliced here.
    """
    r = rpm[start:start + win]
    tq = x[torque_ch, start:start + win].astype(np.float64)
    return np.array([r.mean(), r.max() - r.min(),
                     tq.mean(), tq.max() - tq.min()])


CONDITION_FEATURES = ["rpm_mean", "rpm_range", "torque_mean", "torque_range"]
