"""Reconcile the edge-footprint table (referee minor concern #3).

Recomputes the GROUP-protocol accuracy of the four footprint models under the
SAME five-partition protocol used for the other reconciled tables (baseline
config: 100 Hz, six channels, 2 s), so that RF-200 and logistic regression agree
with the reconciled baseline (52.8 / 59.6). Serialised sizes are architecture-
determined and are taken from the existing analysis; only accuracies are
recomputed here. Reports mean +/- Type A expanded uncertainty (k = t_0.975,4).
"""
from __future__ import annotations
import os, json
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

from dataio import list_recordings, CLASSES
from features import build_feature_matrix

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]
NF = 6
RECS = list_recordings()


def fold_assign(seed):
    rng = np.random.default_rng(seed)
    by = {c: [] for c in CLASSES}
    for r in RECS:
        by[r.cls].append(r.name)
    a = {f: set() for f in range(NF)}
    for c, names in by.items():
        names = sorted(names); perm = rng.permutation(len(names))
        for i, nm in enumerate(names):
            a[int(perm[i]) % NF].add(nm)
    return a


def per_seed(make_model, X, y, g):
    out = []
    for s in SEEDS:
        fa = fold_assign(s); accs = []
        for f in range(NF):
            te = np.array([gr in fa[f] for gr in g]); tr = ~te
            m = make_model(s)
            m.fit(X[tr], y[tr]); accs.append(accuracy_score(y[te], m.predict(X[te])))
        out.append(np.mean(accs))
    return np.array(out)


def ta(a):
    a = np.asarray(a, float); n = len(a)
    m = a.mean(); s = a.std(ddof=1)
    k = stats.t.ppf(0.975, n - 1)
    return 100 * m, 100 * k * s / np.sqrt(n)


def main():
    d = build_feature_matrix(RECS)  # baseline: 100 Hz, 6 ch, 2 s
    X, y, g = d["X"], d["y"], d["groups"]
    models = {
        "RF (200 trees)":       lambda s: RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=s),
        "RF (50, depth 8)":     lambda s: RandomForestClassifier(n_estimators=50, max_depth=8, n_jobs=-1, random_state=s),
        "Decision tree (d=8)":  lambda s: DecisionTreeClassifier(max_depth=8, random_state=s),
        "Logistic regression":  lambda s: make_pipeline(StandardScaler(),
                                                        LogisticRegression(max_iter=2000, random_state=s)),
    }
    res = {}
    for name, mk in models.items():
        a = per_seed(mk, X, y, g); m, u = ta(a)
        res[name] = dict(mean=m, u95=u)
        print(f"{name:22s}: {m:5.1f} +/- {u:4.1f}")
    json.dump(res, open(os.path.join(RES, "footprint_reconcile.json"), "w"), indent=2)
    L = ["# Footprint table reconcile (baseline config, 5-partition GROUP, mean +/- U95)"]
    for name, v in res.items():
        L.append(f"- {name}: {v['mean']:.1f} +/- {v['u95']:.1f}")
    open(os.path.join(RES, "footprint_reconcile.md"), "w").write("\n".join(L) + "\n")
    print("wrote footprint_reconcile.md/json")


if __name__ == "__main__":
    main()
