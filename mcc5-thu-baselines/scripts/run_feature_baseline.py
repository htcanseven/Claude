#!/usr/bin/env python3
"""Feature-engineering baselines on all four protocols, using the window cache.

Protocols
  in_condition            temporal split within runs (guard gap)
  unknown_condition       leave-one-condition-out (all 12 folds)
  steady_to_transitional  train on quasi-stationary, test on ramps
  compositional           train on single faults, test zero-shot on compound
                          faults via multi-label component prediction

Writes results/feature_baseline.csv (+ confusion matrices).
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
from sklearn.linear_model import LogisticRegression             # noqa: E402
from sklearn.preprocessing import StandardScaler               # noqa: E402
from sklearn.pipeline import make_pipeline                     # noqa: E402
from sklearn.multiclass import OneVsRestClassifier             # noqa: E402
from sklearn.metrics import (accuracy_score, f1_score,         # noqa: E402
                             confusion_matrix)

from mcc5.cache import load_cache                              # noqa: E402
from mcc5.splits import WindowIndex, component_matrix           # noqa: E402
from mcc5 import splits as sp                                  # noqa: E402


def make_models(seed: int, which: list[str] | None = None):
    # dual=False solves the primal problem, which is the faster formulation
    # here because samples (~30k) greatly outnumber features (~108).
    all_models = {
        "rf": lambda: RandomForestClassifier(n_estimators=300, n_jobs=-1,
                                             random_state=seed),
        "svm": lambda: make_pipeline(
            StandardScaler(),
            LinearSVC(C=1.0, random_state=seed, dual=False, max_iter=2000)),
        "logreg": lambda: make_pipeline(
            StandardScaler(),
            LogisticRegression(max_iter=1000, n_jobs=-1)),
    }
    keys = which or ["rf", "svm"]
    return {k: all_models[k]() for k in keys if k in all_models}


def evaluate(name, Xtr, ytr, Xte, yte, classes, out_dir, rows, seeds,
             save_cm=True, tag="", models=None):
    for seed in seeds:
        for mname, model in make_models(seed, models).items():
            t0 = time.time()
            model.fit(Xtr, ytr)
            pred = model.predict(Xte)
            acc = accuracy_score(yte, pred)
            f1 = f1_score(yte, pred, average="macro")
            rows.append(dict(protocol=name, model=mname, seed=seed,
                             acc=acc, macro_f1=f1, n_train=len(ytr),
                             n_test=len(yte), fit_s=round(time.time() - t0, 1)))
            print(f"  {name:34s} {mname:4s} s{seed} "
                  f"acc={acc:.4f} macroF1={f1:.4f}", flush=True)
            if save_cm and seed == seeds[0]:
                cm = confusion_matrix(yte, pred,
                                      labels=np.arange(len(classes)))
                safe = name.replace("/", "_").replace("[", "_").replace("]", "")
                pd.DataFrame(cm, index=classes, columns=classes).to_csv(
                    out_dir / f"cm_{safe}_{mname}{tag}.csv")


def evaluate_multilabel(name, Xtr, Ytr, Xte, Yte, vocab, out_dir, rows, seeds,
                        tag="", models=None):
    """Zero-shot compound faults: predict independent fault components."""
    for seed in seeds:
        for mname, base in make_models(seed, models).items():
            t0 = time.time()
            clf = OneVsRestClassifier(base, n_jobs=1)
            clf.fit(Xtr, Ytr)
            P = clf.predict(Xte)
            exact = float((P == Yte).all(axis=1).mean())
            hamming = float((P == Yte).mean())
            micro = f1_score(Yte, P, average="micro", zero_division=0)
            macro = f1_score(Yte, P, average="macro", zero_division=0)
            rows.append(dict(protocol=name, model=mname, seed=seed,
                             acc=exact, macro_f1=macro, micro_f1=micro,
                             hamming=hamming, n_train=len(Ytr),
                             n_test=len(Yte),
                             fit_s=round(time.time() - t0, 1)))
            print(f"  {name:34s} {mname:4s} s{seed} exact={exact:.4f} "
                  f"microF1={micro:.4f} hamming={hamming:.4f}", flush=True)
            if seed == seeds[0]:
                per = pd.DataFrame({
                    "component": vocab,
                    "support_test": Yte.sum(axis=0),
                    "f1": f1_score(Yte, P, average=None, zero_division=0),
                })
                per.to_csv(out_dir / f"components_{mname}{tag}.csv",
                           index=False)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2, 3, 4])
    ap.add_argument("--n-held-out", type=int, default=12,
                    help="number of leave-one-condition-out folds")
    ap.add_argument("--protocols", nargs="+",
                    default=["leaky_random", "in_condition",
                             "unknown_condition", "steady_to_transitional",
                             "compositional"])
    ap.add_argument("--feature-set", default="plain",
                    choices=["plain", "order", "plain+order"],
                    help="plain = time/frequency features; order = "
                         "physics-guided envelope-order features")
    ap.add_argument("--models", nargs="+", default=["rf", "svm"],
                    choices=["rf", "svm", "logreg"])
    ap.add_argument("--tag", default="",
                    help="suffix for output filenames (e.g. _order)")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    cache = load_cache(args.data_dir / "cache", mmap_signals=False)
    blocks = {"plain": [cache["features"]],
              "order": [cache["order_features"]],
              "plain+order": [cache["features"], cache["order_features"]]}
    if args.feature_set != "plain" and "order_features" not in cache:
        print("error: cache has no order features; rebuild without "
              "--no-physics")
        return 1
    X = np.concatenate(blocks[args.feature_set], axis=1)
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    classes = cache["classes"]
    win = cache["win"]
    print(f"{X.shape[0]} windows x {X.shape[1]} features "
          f"[{args.feature_set}] | {len(classes)} classes")

    # Guard against non-finite features poisoning the linear model
    bad = ~np.isfinite(X).all(axis=1)
    if bad.any():
        print(f"warning: dropping {int(bad.sum())} windows with non-finite "
              f"features")
        X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

    rows: list[dict] = []

    if "leaky_random" in args.protocols:
        tr, te = sp.leaky_random_split(idx)
        evaluate("leaky_random", X[tr], idx.label[tr], X[te], idx.label[te],
                 classes, args.out, rows, args.seeds, save_cm=False,
                 tag=args.tag, models=args.models)

    if "in_condition" in args.protocols:
        tr, te = sp.in_condition_split(idx, cache["n_per_run"], win)
        evaluate("in_condition", X[tr], idx.label[tr], X[te], idx.label[te],
                 classes, args.out, rows, args.seeds,
                 tag=args.tag, models=args.models)

    if "unknown_condition" in args.protocols:
        conds = sorted(pd.unique(idx.condition))[: args.n_held_out]
        for cond in conds:
            tr, te = sp.unknown_condition_split(idx, cond)
            if te.sum() == 0:
                continue
            evaluate(f"unknown_condition[{cond}]", X[tr], idx.label[tr],
                     X[te], idx.label[te], classes, args.out, rows,
                     args.seeds, save_cm=False, tag=args.tag,
                     models=args.models)

    if "steady_to_transitional" in args.protocols:
        tr, te = sp.steady_to_transitional_split(idx)
        if tr.sum() and te.sum():
            evaluate("steady_to_transitional", X[tr], idx.label[tr],
                     X[te], idx.label[te], classes, args.out, rows,
                     args.seeds, tag=args.tag, models=args.models)

    if "compositional" in args.protocols:
        Yrun, vocab = component_matrix(meta)
        is_comp = meta["is_compound"].to_numpy().astype(bool)
        tr, te = sp.compositional_split(idx, is_comp)
        Yw = Yrun[idx.run]
        print(f"  components ({len(vocab)}): {vocab}")
        evaluate_multilabel("compositional_zeroshot", X[tr], Yw[tr],
                            X[te], Yw[te], vocab, args.out, rows,
                            args.seeds, tag=args.tag, models=args.models)

    df = pd.DataFrame(rows)
    df.insert(0, "feature_set", args.feature_set)
    path = args.out / f"feature_baseline{args.tag}.csv"
    df.to_csv(path, index=False)
    print(f"\nresults -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
