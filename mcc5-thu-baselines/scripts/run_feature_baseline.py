#!/usr/bin/env python3
"""Feature-engineering baseline (RandomForest + linear SVM) on all protocols.

Outputs per-protocol accuracy / macro-F1 to results/feature_baseline.csv and
confusion matrices to results/cm_<protocol>.csv.
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sklearn.ensemble import RandomForestClassifier            # noqa: E402
from sklearn.svm import LinearSVC                              # noqa: E402
from sklearn.preprocessing import StandardScaler               # noqa: E402
from sklearn.pipeline import make_pipeline                     # noqa: E402
from sklearn.metrics import (accuracy_score, f1_score,         # noqa: E402
                             confusion_matrix)

from mcc5.dataset import build_index, materialize_features     # noqa: E402
from mcc5 import splits as sp                                  # noqa: E402

WIN = 8192   # 0.64 s
HOP = 8192   # non-overlapping to keep the first pass light


def evaluate(name, Xtr, ytr, Xte, yte, classes, out_dir, rows, seed=0):
    models = {
        "rf": RandomForestClassifier(n_estimators=300, n_jobs=-1,
                                     random_state=seed),
        "svm": make_pipeline(StandardScaler(),
                             LinearSVC(C=1.0, random_state=seed)),
    }
    for mname, model in models.items():
        t0 = time.time()
        model.fit(Xtr, ytr)
        pred = model.predict(Xte)
        acc = accuracy_score(yte, pred)
        f1 = f1_score(yte, pred, average="macro")
        rows.append(dict(protocol=name, model=mname, acc=acc, macro_f1=f1,
                         n_train=len(ytr), n_test=len(yte),
                         fit_s=round(time.time() - t0, 1)))
        print(f"{name:28s} {mname:4s} acc={acc:.4f} macroF1={f1:.4f}")
        cm = confusion_matrix(yte, pred, labels=np.arange(len(classes)))
        pd.DataFrame(cm, index=classes, columns=classes).to_csv(
            out_dir / f"cm_{name}_{mname}.csv")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--n-held-out", type=int, default=3,
                    help="number of leave-one-condition-out folds to run")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    print(f"{len(meta)} runs, {meta.fault_full.nunique()} classes, "
          f"{meta.condition.nunique()} conditions")

    idx, n_per_run, classes = build_index(args.data_dir, meta, WIN, HOP)
    print(f"{len(idx.run)} windows")

    rows: list[dict] = []

    # Protocol 1: in-condition (temporal split with guard gap)
    tr, te = sp.in_condition_split(idx, n_per_run, WIN)
    Xtr = materialize_features(args.data_dir, meta, idx, tr, WIN)
    Xte = materialize_features(args.data_dir, meta, idx, te, WIN)
    evaluate("in_condition", Xtr, idx.label[tr], Xte, idx.label[te],
             classes, args.out, rows)

    # Protocol 2: leave-one-condition-out (first n folds)
    conditions = sorted(meta.condition.unique())
    for cond in conditions[: args.n_held_out]:
        tr, te = sp.unknown_condition_split(idx, cond)
        if te.sum() == 0:
            continue
        Xtr = materialize_features(args.data_dir, meta, idx, tr, WIN)
        Xte = materialize_features(args.data_dir, meta, idx, te, WIN)
        evaluate(f"unknown_condition[{cond}]", Xtr, idx.label[tr],
                 Xte, idx.label[te], classes, args.out, rows)

    # Protocol 3: steady -> transitional
    tr, te = sp.steady_to_transitional_split(idx)
    if te.sum() and tr.sum():
        Xtr = materialize_features(args.data_dir, meta, idx, tr, WIN)
        Xte = materialize_features(args.data_dir, meta, idx, te, WIN)
        evaluate("steady_to_transitional", Xtr, idx.label[tr],
                 Xte, idx.label[te], classes, args.out, rows)

    pd.DataFrame(rows).to_csv(args.out / "feature_baseline.csv", index=False)
    print(f"results -> {args.out / 'feature_baseline.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
