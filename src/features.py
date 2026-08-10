"""Windowing and time-domain feature extraction.

Design goals:
- vectorised over windows (n_win, W, C) for speed;
- a rich feature set plus the 6-feature "paper" subset for ablation;
- a single entry point `build_feature_matrix` that also handles optional
  resampling (decimation) and an arbitrary per-recording signal transform
  (used later for quantisation / packet-loss / coupling-augmentation studies).
"""
from __future__ import annotations

from typing import Callable, Sequence
import numpy as np
from scipy.signal import resample_poly

from dataio import Recording, load_signal, CHANNELS, FS

EPS = 1e-12

# Feature names in the fixed order produced by `_features`.
FEATURE_NAMES = [
    "mean", "std", "rms", "var", "p2p", "max_abs",
    "skew", "kurt", "crest", "shape", "impulse", "clearance", "zcr", "entropy",
]
# 6-feature subset used by the dataset article's baseline (for D4 ablation).
PAPER_FEATURES = ["rms", "std", "p2p", "kurt", "skew", "crest"]


def make_windows(sig: np.ndarray, win: int, hop: int) -> np.ndarray:
    """(N, C) -> (n_win, win, C) using a strided view (no copy)."""
    n = (len(sig) - win) // hop + 1
    if n <= 0:
        return np.empty((0, win, sig.shape[1]), dtype=sig.dtype)
    s0, s1 = sig.strides
    from numpy.lib.stride_tricks import as_strided
    return as_strided(sig, shape=(n, win, sig.shape[1]), strides=(hop * s0, s0, s1))


def _features(w: np.ndarray) -> np.ndarray:
    """(n_win, W, C) -> (n_win, C, n_feat). Vectorised time-domain features."""
    x = w.astype(np.float64)
    mean = x.mean(axis=1)
    std = x.std(axis=1)
    var = std ** 2
    rms = np.sqrt((x ** 2).mean(axis=1))
    xmin = x.min(axis=1)
    xmax = x.max(axis=1)
    p2p = xmax - xmin
    absx = np.abs(x)
    max_abs = absx.max(axis=1)
    mean_abs = absx.mean(axis=1)
    # higher-order moments
    xc = x - mean[:, None, :]
    m2 = (xc ** 2).mean(axis=1)
    m3 = (xc ** 3).mean(axis=1)
    m4 = (xc ** 4).mean(axis=1)
    skew = m3 / (m2 ** 1.5 + EPS)
    kurt = m4 / (m2 ** 2 + EPS) - 3.0
    # shape/impulse factors
    crest = max_abs / (rms + EPS)
    shape = rms / (mean_abs + EPS)
    impulse = max_abs / (mean_abs + EPS)
    sqrt_mean = (np.sqrt(absx).mean(axis=1)) ** 2
    clearance = max_abs / (sqrt_mean + EPS)
    # zero-crossing rate (about the mean)
    sign = np.sign(xc)
    zcr = (np.abs(np.diff(sign, axis=1)) > 0).mean(axis=1)
    # amplitude Shannon entropy (per channel, 32-bin normalised histogram)
    entropy = _amp_entropy(x)
    feats = np.stack(
        [mean, std, rms, var, p2p, max_abs, skew, kurt,
         crest, shape, impulse, clearance, zcr, entropy], axis=-1
    )  # (n_win, C, n_feat)
    return feats


def _amp_entropy(x: np.ndarray, bins: int = 32) -> np.ndarray:
    n_win, W, C = x.shape
    out = np.empty((n_win, C))
    xmin = x.min(axis=1, keepdims=True)
    xmax = x.max(axis=1, keepdims=True)
    rng = np.maximum(xmax - xmin, EPS)
    xn = (x - xmin) / rng  # -> [0,1]
    idx = np.minimum((xn * bins).astype(np.int64), bins - 1)  # (n_win,W,C)
    for c in range(C):
        # histogram per window via bincount trick
        offset = idx[:, :, c] + (np.arange(n_win)[:, None] * bins)
        counts = np.bincount(offset.ravel(), minlength=n_win * bins).reshape(n_win, bins)
        p = counts / W
        with np.errstate(divide="ignore", invalid="ignore"):
            h = -np.where(p > 0, p * np.log2(p), 0.0).sum(axis=1)
        out[:, c] = h
    return out


def feature_columns(channels: Sequence[str], feature_names: Sequence[str]) -> list[str]:
    return [f"{ch}:{fn}" for ch in channels for fn in feature_names]


def extract(windows: np.ndarray, feature_set: str = "full",
            channels: Sequence[str] = CHANNELS) -> tuple[np.ndarray, list[str]]:
    feats = _features(windows)                       # (n_win, C, n_feat)
    if feature_set == "paper":
        keep = [FEATURE_NAMES.index(f) for f in PAPER_FEATURES]
        feats = feats[:, :, keep]
        names = PAPER_FEATURES
    else:
        names = FEATURE_NAMES
    n_win = feats.shape[0]
    X = feats.reshape(n_win, -1)                     # (n_win, C*n_feat)
    return X.astype(np.float32), feature_columns(channels, names)


def resample_signal(sig: np.ndarray, fs_from: float, fs_to: float) -> np.ndarray:
    """Anti-aliased decimation/resampling; fs_to must divide fs_from's factor."""
    if abs(fs_to - fs_from) < 1e-9:
        return sig
    factor = fs_from / fs_to
    if abs(factor - round(factor)) < 1e-9:
        return resample_poly(sig, up=1, down=int(round(factor)), axis=0).astype(np.float32)
    # general rational case
    from fractions import Fraction
    fr = Fraction(fs_to / fs_from).limit_denominator(1000)
    return resample_poly(sig, up=fr.numerator, down=fr.denominator, axis=0).astype(np.float32)


def build_feature_matrix(
    recs: Sequence[Recording],
    channels: Sequence[str] = CHANNELS,
    fs_target: float = FS,
    win_sec: float = 2.0,
    overlap: float = 0.5,
    feature_set: str = "full",
    signal_transform: Callable[[np.ndarray, Recording], np.ndarray] | None = None,
) -> dict:
    """Return dict with X, y, groups, speed, load, columns.

    `signal_transform(sig, rec) -> sig` runs after resampling, before windowing
    (used by later studies: quantisation, packet loss, coupling augmentation).
    """
    win = int(round(win_sec * fs_target))
    hop = max(1, int(round(win * (1.0 - overlap))))
    Xs, ys, gs, sp, ld = [], [], [], [], []
    cols = None
    for r in recs:
        sig = load_signal(r, list(channels))
        if abs(fs_target - FS) > 1e-9:
            sig = resample_signal(sig, FS, fs_target)
        if signal_transform is not None:
            sig = signal_transform(sig, r)
        w = make_windows(np.ascontiguousarray(sig), win, hop)
        if w.shape[0] == 0:
            continue
        X, cols = extract(w, feature_set=feature_set, channels=channels)
        Xs.append(X)
        ys.append(np.full(X.shape[0], r.label, dtype=np.int64))
        gs.append(np.array([r.group_id] * X.shape[0]))
        sp.append(np.full(X.shape[0], r.speed, dtype=np.int64))
        ld.append(np.full(X.shape[0], r.load, dtype=np.int64))
    return {
        "X": np.concatenate(Xs), "y": np.concatenate(ys),
        "groups": np.concatenate(gs), "speed": np.concatenate(sp),
        "load": np.concatenate(ld), "columns": cols,
        "win": win, "hop": hop, "fs": fs_target,
    }
