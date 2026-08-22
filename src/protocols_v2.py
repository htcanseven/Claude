"""Shared machinery for the Measurement (Elsevier) revision experiments.

Adds three capabilities the original pipeline lacked:

1. `build_custom` — a feature-matrix builder that accepts an arbitrary
   resampling function, so the anti-alias study can separate band-limiting from
   decimation (the stock `features.build_feature_matrix` always routes through
   `resample_poly`, which applies an anti-alias filter unconditionally).
2. Partitionings that decompose leakage: random over overlapping windows,
   random over non-overlapping windows, temporally blocked within recording,
   recording-wise, cross-speed and cross-load.
3. Per-held-out-recording scoring, so performance can be summarised with
   recording-clustered intervals and compared with a paired permutation test
   rather than treating seed re-runs as independent measurements.
"""
from __future__ import annotations

import numpy as np
from scipy.signal import butter, filtfilt, resample_poly
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

from dataio import list_recordings, load_signal, CLASSES, CHANNELS, FS
from features import make_windows, extract

NF = 6                       # recording-wise folds: 6 recordings per class
RECS = list_recordings()


# --------------------------------------------------------------------------
# resamplers (all take a (n, C) float array at 100 Hz, return (m, C))
# --------------------------------------------------------------------------
def rs_identity(sig):
    return sig


def rs_polyphase(down):
    """Standard decimation: polyphase FIR with its anti-alias filter."""
    def f(sig):
        return resample_poly(sig, up=1, down=int(down), axis=0).astype(np.float32)
    return f


def rs_lowpass_only(cutoff_hz, order=8):
    """Band-limit at `cutoff_hz` but keep the 100 Hz sample rate."""
    b, a = butter(order, cutoff_hz, btype="low", fs=FS)
    def f(sig):
        return filtfilt(b, a, sig, axis=0).astype(np.float32)
    return f


def rs_naive_decimate(down):
    """Decimate by simple subsampling, with NO anti-alias filter (aliasing)."""
    def f(sig):
        return np.ascontiguousarray(sig[::int(down)]).astype(np.float32)
    return f


# --------------------------------------------------------------------------
def build_custom(recs=None, channels=CHANNELS, resampler=rs_identity,
                 fs_out=FS, win_sec=2.0, overlap=0.5):
    """Mirror of features.build_feature_matrix with a pluggable resampler."""
    recs = RECS if recs is None else recs
    win = int(round(win_sec * fs_out))
    hop = max(1, int(round(win * (1.0 - overlap))))
    Xs, ys, gs, sp, ld, tt = [], [], [], [], [], []
    cols = None
    for r in recs:
        sig = resampler(load_signal(r, list(channels)))
        w = make_windows(np.ascontiguousarray(sig), win, hop)
        if w.shape[0] == 0:
            continue
        X, cols = extract(w, feature_set="full", channels=channels)
        n = X.shape[0]
        Xs.append(X)
        ys.append(np.full(n, r.label, dtype=np.int64))
        gs.append(np.array([r.name] * n))
        sp.append(np.full(n, r.speed, dtype=np.int64))
        ld.append(np.full(n, r.load, dtype=np.int64))
        tt.append(np.arange(n) / max(n - 1, 1))      # normalised position in recording
    return {"X": np.concatenate(Xs), "y": np.concatenate(ys),
            "groups": np.concatenate(gs), "speed": np.concatenate(sp),
            "load": np.concatenate(ld), "tpos": np.concatenate(tt),
            "columns": cols, "fs": fs_out, "win": win, "hop": hop}


def rf(seed, n_estimators=200):
    return RandomForestClassifier(n_estimators=n_estimators, n_jobs=-1,
                                  random_state=seed)


def fold_assign(seed, nf=NF):
    """One recording per class per fold, reshuffled by seed."""
    rng = np.random.default_rng(seed)
    by = {c: [] for c in CLASSES}
    for r in RECS:
        by[r.cls].append(r.name)
    a = {f: set() for f in range(nf)}
    for c, names in by.items():
        names = sorted(names)
        perm = rng.permutation(len(names))
        for i, nm in enumerate(names):
            a[int(perm[i]) % nf].add(nm)
    return a


# --------------------------------------------------------------------------
# evaluation: every protocol returns (overall_acc, macro_f1, per_recording dict)
# --------------------------------------------------------------------------
def _fit_score(d, tr, te, seed, n_estimators=200):
    m = rf(seed, n_estimators)
    m.fit(d["X"][tr], d["y"][tr])
    pred = m.predict(d["X"][te])
    yt = d["y"][te]
    per = {}
    for g in np.unique(d["groups"][te]):
        sel = d["groups"][te] == g
        per[str(g)] = float(accuracy_score(yt[sel], pred[sel]))
    return (float(accuracy_score(yt, pred)),
            float(f1_score(yt, pred, average="macro")), per)


def eval_group(d, seed, nf=NF, n_estimators=200):
    fa = fold_assign(seed, nf)
    accs, f1s, per = [], [], {}
    for f in range(nf):
        te = np.array([g in fa[f] for g in d["groups"]])
        a, fm, p = _fit_score(d, ~te, te, seed, n_estimators)
        accs.append(a); f1s.append(fm); per.update(p)
    return float(np.mean(accs)), float(np.mean(f1s)), per


def eval_random(d, seed, test_frac=1.0 / NF):
    """Stratified random split over windows (the leaky reference)."""
    rng = np.random.default_rng(seed)
    te = np.zeros(len(d["y"]), bool)
    for c in np.unique(d["y"]):
        idx = np.where(d["y"] == c)[0]
        pick = rng.choice(idx, size=int(round(test_frac * len(idx))), replace=False)
        te[pick] = True
    return _fit_score(d, ~te, te, seed)


def eval_blocked(d, seed, nf=NF):
    """Contiguous temporal block held out within every recording.

    Removes window-overlap leakage and near-duplicate temporal proximity, but
    keeps recording identity in the training set.
    """
    rng = np.random.default_rng(seed)
    accs, f1s, per = [], [], {}
    for f in range(nf):
        lo = f / nf
        hi = (f + 1) / nf
        te = (d["tpos"] >= lo) & (d["tpos"] < hi)
        a, fm, p = _fit_score(d, ~te, te, seed)
        accs.append(a); f1s.append(fm)
        for k, v in p.items():
            per.setdefault(k, []).append(v)
    per = {k: float(np.mean(v)) for k, v in per.items()}
    return float(np.mean(accs)), float(np.mean(f1s)), per


def eval_leave_one(d, seed, key):
    """Leave-one-operating-condition-out (key = 'speed' or 'load')."""
    accs, f1s, per = [], [], {}
    for v in np.unique(d[key]):
        te = d[key] == v
        a, fm, p = _fit_score(d, ~te, te, seed)
        accs.append(a); f1s.append(fm); per.update(p)
    return float(np.mean(accs)), float(np.mean(f1s)), per


# --------------------------------------------------------------------------
# statistics on recording-level scores
# --------------------------------------------------------------------------
def clustered_ci(per_rec_by_seed, alpha=0.05):
    """95% interval for the mean, clustering on recording (the sampling unit).

    Each recording's score is first averaged over seeds, so the n is the number
    of independent recordings rather than the number of seed re-runs.
    """
    recs = sorted(set().union(*[set(p) for p in per_rec_by_seed]))
    means = np.array([np.mean([p[r] for p in per_rec_by_seed if r in p]) for r in recs])
    n = len(means)
    from scipy import stats
    se = means.std(ddof=1) / np.sqrt(n)
    h = stats.t.ppf(1 - alpha / 2, n - 1) * se
    return float(100 * means.mean()), float(100 * h), n, {r: float(m) for r, m in zip(recs, means)}


def paired_permutation(a_by_rec, b_by_rec, n_perm=20000, seed=0):
    """Two-sided paired permutation test on per-recording differences."""
    recs = sorted(set(a_by_rec) & set(b_by_rec))
    d = np.array([b_by_rec[r] - a_by_rec[r] for r in recs])
    obs = d.mean()
    rng = np.random.default_rng(seed)
    signs = rng.choice([-1.0, 1.0], size=(n_perm, len(d)))
    null = (signs * d).mean(axis=1)
    p = (np.sum(np.abs(null) >= abs(obs) - 1e-15) + 1) / (n_perm + 1)
    return float(100 * obs), float(p), len(d)
