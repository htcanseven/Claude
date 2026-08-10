"""Reconcile all result tables onto ONE protocol so baseline figures match.

Every table uses: fixed recording-level 6-fold partition, five seeds, RF(200)
(and KNN/SVM/LogReg where a table needs them), reported as mean +/- Type A
expanded uncertainty (k=2). This removes the cross-table baseline mismatch and
makes the reported dispersion the uncertainty of the measured mean throughout.
"""
from __future__ import annotations
import os, json
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.kernel_approximation import Nystroem
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

from dataio import list_recordings, CLASSES, CHANNELS, RAW_CHANNELS
from features import build_feature_matrix

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
SEEDS = [0, 1, 2, 3, 4]
NF = 6
RECS = list_recordings()


def make(name, seed):
    if name == "RF":
        return RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=seed)
    if name == "KNN":
        return make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5, n_jobs=-1))
    if name == "SVM":
        return make_pipeline(StandardScaler(),
                             Nystroem(kernel="rbf", n_components=400, random_state=seed),
                             LinearSVC(C=10.0, dual=False, max_iter=5000))
    if name == "LogReg":
        return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))


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


def group_perseed(X, y, g, name):
    out = []
    for s in SEEDS:
        fa = fold_assign(s); accs = []
        for f in range(NF):
            te = np.array([gr in fa[f] for gr in g]); tr = ~te
            m = make(name, s); m.fit(X[tr], y[tr])
            accs.append(accuracy_score(y[te], m.predict(X[te])))
        out.append(np.mean(accs))
    return np.array(out)


def random_perseed(X, y, name):
    out = []
    for s in SEEDS:
        skf = StratifiedKFold(5, shuffle=True, random_state=s); accs = []
        for tr, te in skf.split(X, y):
            m = make(name, s); m.fit(X[tr], y[tr])
            accs.append(accuracy_score(y[te], m.predict(X[te])))
        out.append(np.mean(accs))
    return np.array(out)


def leave_perseed(X, y, factor, values, name):
    out = []
    for s in SEEDS:
        accs = []
        for v in values:
            te = factor == v; tr = ~te
            m = make(name, s); m.fit(X[tr], y[tr])
            accs.append(accuracy_score(y[te], m.predict(X[te])))
        out.append(np.mean(accs))
    return np.array(out)


def ta(ps):
    n = len(ps); mean = 100*ps.mean(); s = 100*ps.std(ddof=1)
    U = stats.t.ppf(0.975, n-1) * s/np.sqrt(n)
    return dict(mean=mean, U95=U, s=s)


def fmt(d):
    return f"{d['mean']:.1f} $\\pm$ {d['U95']:.1f}"


def build(channels, fs, win):
    return build_feature_matrix(RECS, channels=channels, fs_target=fs, win_sec=win)


def main():
    rep = {}
    print("build C_base…")
    base = build(CHANNELS, 100, 2.0)
    Xb, yb, gb, sp, ld = base["X"], base["y"], base["groups"], base["speed"], base["load"]

    # ---- Table VI: optimism ----
    print("Table VI…")
    vi = {}
    for m in ["RF", "KNN", "SVM"]:
        vi[m] = dict(
            RANDOM=ta(random_perseed(Xb, yb, m)),
            GROUP=ta(group_perseed(Xb, yb, gb, m)),
            SPEED=ta(leave_perseed(Xb, yb, sp, [30, 40, 50], m)),
            LOAD=ta(leave_perseed(Xb, yb, ld, [0, 1], m)),
        )
        print(f"  {m}: RANDOM {fmt(vi[m]['RANDOM'])}, GROUP {fmt(vi[m]['GROUP'])}, "
              f"SPEED {fmt(vi[m]['SPEED'])}, LOAD {fmt(vi[m]['LOAD'])}")
    rep["VI"] = vi

    # ---- Table VII: sampling sweep (RF GROUP) ----
    print("Table VII…")
    vii = []
    for fs in [100, 50, 25, 20, 12.5, 10]:
        d = base if fs == 100 else build(CHANNELS, fs, 2.0)
        t = ta(group_perseed(d["X"], d["y"], d["groups"], "RF"))
        vii.append(dict(fs=fs, kbps=fs*6*2*8/1e3, **t))
        print(f"  {fs} Hz: {fmt(t)}")
    rep["VII"] = vii

    # ---- Table VIII: incremental recipe ----
    print("Table VIII…")
    recipe = [
        ("Baseline (100 Hz, 6 ch, 2 s)", CHANNELS, 100, 2.0),
        ("+ 25 Hz",                       CHANNELS, 25, 2.0),
        ("+ raw 3 ch",                    RAW_CHANNELS, 25, 2.0),
        ("+ 4 s window (optimal)",        RAW_CHANNELS, 25, 4.0),
    ]
    viii = []
    for label, ch, fs, win in recipe:
        d = base if (ch == CHANNELS and fs == 100 and win == 2.0) else build(ch, fs, win)
        row = {"label": label}
        for m in ["RF", "KNN", "LogReg"]:
            row[m] = ta(group_perseed(d["X"], d["y"], d["groups"], m))
        viii.append(row)
        print(f"  {label}: RF {fmt(row['RF'])}, KNN {fmt(row['KNN'])}, LogReg {fmt(row['LogReg'])}")
    rep["VIII"] = viii

    # ---- write ----
    def L(d):  # latex row helper
        return fmt(d)
    lines = ["# Reconciled tables (fixed recording partition, RF200, 5 seeds, mean +/- U95)", ""]
    lines.append("## Table VI optimism")
    lines.append("| Protocol | RF | KNN | SVM |")
    lines.append("|---|---|---|---|")
    for proto, key in [("RANDOM","RANDOM"),("GROUP","GROUP"),("CROSS-SPEED","SPEED"),("CROSS-LOAD","LOAD")]:
        lines.append(f"| {proto} | " + " | ".join(L(vi[m][key]) for m in ["RF","KNN","SVM"]) + " |")
    lines.append("\n## Table VII sampling (RF GROUP)")
    lines.append("| Rate (Hz) | kbps | Accuracy |")
    lines.append("|---|---|---|")
    for x in vii:
        lines.append(f"| {x['fs']:g} | {x['kbps']:.1f} | {x['mean']:.1f} $\\pm$ {x['U95']:.1f} |")
    lines.append("\n## Table VIII recipe")
    lines.append("| Configuration | RF | KNN | LogReg |")
    lines.append("|---|---|---|---|")
    for r in viii:
        lines.append(f"| {r['label']} | " + " | ".join(L(r[m]) for m in ["RF","KNN","LogReg"]) + " |")
    open(os.path.join(RES, "reconciled.md"), "w").write("\n".join(lines) + "\n")
    open(os.path.join(RES, "reconciled.json"), "w").write(json.dumps(rep, indent=2))
    print("\n".join(lines))
    print("wrote reconciled.md/json")


if __name__ == "__main__":
    main()
