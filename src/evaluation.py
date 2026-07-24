"""Model zoo + evaluation protocols.

The point of this module is the *protocol* axis:
- RANDOM  : stratified split over overlapping windows  (leaky baseline)
- GROUP   : whole-recording holdout                     (leakage-free)
- SPEED   : leave-one-speed-out                          (cross-speed generalisation)
- LOAD    : leave-one-load-out                           (cross-load generalisation)

All protocols return per-fold accuracy + macro-F1 and (optionally) pooled
out-of-fold predictions for confusion matrices.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.kernel_approximation import Nystroem
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold
from sklearn.metrics import accuracy_score, f1_score


def make_models(seed: int = 0) -> dict:
    """Three baselines. SVM uses an RBF-Nystroem + linear SVC (scalable RBF-SVM)."""
    return {
        "RF": RandomForestClassifier(
            n_estimators=300, n_jobs=-1, random_state=seed),
        "KNN": make_pipeline(
            StandardScaler(), KNeighborsClassifier(n_neighbors=5, n_jobs=-1)),
        "SVM": make_pipeline(
            StandardScaler(),
            Nystroem(kernel="rbf", n_components=400, random_state=seed),
            LinearSVC(C=10.0, dual=False, max_iter=5000)),
    }


@dataclass
class ProtocolResult:
    name: str
    per_model: dict = field(default_factory=dict)   # model -> dict(acc=[...], f1=[...])
    oof: dict = field(default_factory=dict)          # model -> (y_true, y_pred) pooled

    def summary(self) -> dict:
        out = {}
        for m, d in self.per_model.items():
            acc = np.array(d["acc"]); f1 = np.array(d["f1"])
            out[m] = dict(
                acc_mean=float(acc.mean()), acc_std=float(acc.std()),
                f1_mean=float(f1.mean()), f1_std=float(f1.std()),
                acc_ci=float(1.96 * acc.std() / max(1, np.sqrt(len(acc)))),
                n_folds=len(acc),
            )
        return out


def _fit_eval(model, Xtr, ytr, Xte, yte):
    model.fit(Xtr, ytr)
    yp = model.predict(Xte)
    return accuracy_score(yte, yp), f1_score(yte, yp, average="macro"), yp


def _run_folds(X, y, folds, seed, collect_oof=True) -> ProtocolResult:
    res = ProtocolResult(name="", per_model={}, oof={})
    for mname in ["RF", "KNN", "SVM"]:
        accs, f1s, yt_all, yp_all = [], [], [], []
        for (tr, te) in folds:
            model = make_models(seed)[mname]
            acc, f1, yp = _fit_eval(model, X[tr], y[tr], X[te], y[te])
            accs.append(acc); f1s.append(f1)
            if collect_oof:
                yt_all.append(y[te]); yp_all.append(yp)
        res.per_model[mname] = dict(acc=accs, f1=f1s)
        if collect_oof:
            res.oof[mname] = (np.concatenate(yt_all), np.concatenate(yp_all))
    return res


def protocol_random(X, y, n_splits=5, seed=0) -> ProtocolResult:
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    folds = list(skf.split(X, y))
    r = _run_folds(X, y, folds, seed); r.name = "RANDOM (leaky)"
    return r


def protocol_group(X, y, groups, n_splits=6, seed=0) -> ProtocolResult:
    sgkf = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    folds = list(sgkf.split(X, y, groups))
    r = _run_folds(X, y, folds, seed); r.name = "GROUP (recording-holdout)"
    return r


def protocol_leave_value_out(X, y, factor, values, seed=0, name="") -> ProtocolResult:
    """Leave-one-value-out on an operating factor (speed or load)."""
    folds = []
    for v in values:
        te = np.where(factor == v)[0]
        tr = np.where(factor != v)[0]
        folds.append((tr, te))
    r = _run_folds(X, y, folds, seed); r.name = name
    return r
