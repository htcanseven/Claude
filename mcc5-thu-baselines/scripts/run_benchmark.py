#!/usr/bin/env python3
"""Run one model family across every benchmark protocol.

All baselines enumerate splits through ``mcc5.protocols``, so numbers are
comparable across models by construction. One CSV per invocation:
``results/bench_<model>_<features><tag>.csv``.

Examples
    python scripts/run_benchmark.py --model rf  --seeds 0 1 2
    python scripts/run_benchmark.py --model svm --features plain+order
    python scripts/run_benchmark.py --model cnn --epochs 12 --noise-snr 20 10
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
from sklearn.linear_model import LogisticRegression            # noqa: E402
from sklearn.preprocessing import StandardScaler               # noqa: E402
from sklearn.pipeline import make_pipeline                     # noqa: E402
from sklearn.multiclass import OneVsRestClassifier             # noqa: E402
from sklearn.metrics import (accuracy_score, f1_score,         # noqa: E402
                             confusion_matrix)

from mcc5.cache import load_cache                              # noqa: E402
from mcc5.protocols import iter_protocols, ALL_PROTOCOLS        # noqa: E402
from mcc5.splits import (WindowIndex, component_matrix,         # noqa: E402
                         partial_credit, topk_metrics)

FEATURE_MODELS = ("rf", "svm", "logreg")


def make_estimator(name: str, seed: int):
    if name == "rf":
        return RandomForestClassifier(n_estimators=300, n_jobs=-1,
                                      random_state=seed)
    if name == "svm":
        # primal is the faster formulation when samples >> features
        return make_pipeline(StandardScaler(),
                            LinearSVC(C=1.0, random_state=seed, dual=False,
                                      max_iter=2000))
    if name == "logreg":
        return make_pipeline(StandardScaler(),
                             LogisticRegression(max_iter=1000, n_jobs=-1))
    raise ValueError(name)


def eval_multiclass(est, Xtr, ytr, Xte, yte, classes, out_dir, stem):
    est.fit(Xtr, ytr)
    pred = est.predict(Xte)
    cm = confusion_matrix(yte, pred, labels=np.arange(len(classes)))
    pd.DataFrame(cm, index=classes, columns=classes).to_csv(
        out_dir / f"cm_{stem}.csv")
    return dict(acc=accuracy_score(yte, pred),
                macro_f1=f1_score(yte, pred, average="macro",
                                  zero_division=0))


def eval_multilabel(est, Xtr, Ytr, Xte, Yte, vocab, out_dir, stem):
    clf = OneVsRestClassifier(est, n_jobs=1)
    clf.fit(Xtr, Ytr)
    P = clf.predict(Xte).astype(np.int8)
    scores = (clf.decision_function(Xte)
              if hasattr(clf, "decision_function") else P.astype(float))
    pd.DataFrame({"component": vocab,
                  "support_test": Yte.sum(axis=0),
                  "f1": f1_score(Yte, P, average=None, zero_division=0)}
                 ).to_csv(out_dir / f"components_{stem}.csv", index=False)
    out = dict(acc=float((P == Yte).all(axis=1).mean()),
               macro_f1=f1_score(Yte, P, average="macro", zero_division=0),
               micro_f1=f1_score(Yte, P, average="micro", zero_division=0),
               hamming=float((P == Yte).mean()))
    out.update(partial_credit(P, Yte))
    out.update(topk_metrics(np.asarray(scores), Yte))
    return out


def run_cnn(proto, S, Ylab, Ycomp, classes, vocab, args, seed, out_dir, stem):
    """Deep baseline: WDCNN-style 1D CNN on raw multichannel windows."""
    import torch
    import torch.nn as nn
    from mcc5.models import CNN1D

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    multilabel = proto.kind == "multilabel"

    Xtr = np.ascontiguousarray(S[proto.train])
    Xte = np.ascontiguousarray(S[proto.test])
    mu = Xtr.mean(axis=(0, 2), keepdims=True)
    sd = Xtr.std(axis=(0, 2), keepdims=True) + 1e-8
    Xtr, Xte = (Xtr - mu) / sd, (Xte - mu) / sd
    if multilabel:
        ytr, yte = Ycomp[proto.train], Ycomp[proto.test]
        n_out = Ycomp.shape[1]
    else:
        ytr, yte = Ylab[proto.train], Ylab[proto.test]
        n_out = len(classes)

    model = CNN1D(Xtr.shape[1], n_out).to(dev)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr)
    lossf = nn.BCEWithLogitsLoss() if multilabel else nn.CrossEntropyLoss()
    n = len(ytr)
    for ep in range(args.epochs):
        model.train()
        perm = rng.permutation(n)
        for s in range(0, n, args.bs):
            b = perm[s:s + args.bs]
            xb = torch.from_numpy(Xtr[b]).to(dev)
            yb = torch.from_numpy(
                ytr[b].astype(np.float32) if multilabel
                else ytr[b].astype(np.int64)).to(dev)
            opt.zero_grad()
            lossf(model(xb), yb).backward()
            opt.step()

    def predict(X):
        model.eval()
        outs = []
        with torch.no_grad():
            for i in range(0, len(X), 256):
                xb = torch.from_numpy(np.ascontiguousarray(X[i:i + 256]))
                outs.append(model(xb.to(dev)).cpu().numpy())
        return np.concatenate(outs)

    results = []
    for snr in [None] + list(args.noise_snr or []):
        Xev = Xte
        if snr is not None:
            # signals are standardized, so unit variance per channel: the noise
            # scale for a target SNR in dB is just 10^(-snr/20)
            noise = rng.normal(0.0, 10 ** (-snr / 20.0), Xte.shape)
            Xev = (Xte + noise).astype(np.float32)
        logits = predict(Xev)
        if multilabel:
            P = (logits > 0).astype(np.int8)
            row = dict(acc=float((P == yte).all(axis=1).mean()),
                       macro_f1=f1_score(yte, P, average="macro",
                                         zero_division=0),
                       micro_f1=f1_score(yte, P, average="micro",
                                         zero_division=0),
                       hamming=float((P == yte).mean()))
            row.update(partial_credit(P, yte))
            row.update(topk_metrics(logits, yte))
        else:
            pred = logits.argmax(1)
            row = dict(acc=accuracy_score(yte, pred),
                       macro_f1=f1_score(yte, pred, average="macro",
                                         zero_division=0))
            if snr is None:
                pd.DataFrame(confusion_matrix(yte, pred,
                                              labels=np.arange(len(classes))),
                             index=classes, columns=classes).to_csv(
                    out_dir / f"cm_{stem}.csv")
        row["noise_snr_db"] = snr
        results.append(row)
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--model", default="rf",
                    choices=["rf", "svm", "logreg", "cnn"])
    ap.add_argument("--features", default="plain",
                    choices=["plain", "order", "plain+order"])
    ap.add_argument("--protocols", nargs="+", default=ALL_PROTOCOLS)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0])
    ap.add_argument("--max-condition-folds", type=int, default=None,
                    help="cap the per-condition fold count (12 if unset)")
    ap.add_argument("--epochs", type=int, default=10)
    ap.add_argument("--bs", type=int, default=64)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--noise-snr", type=float, nargs="*", default=None,
                    help="extra test-time SNRs in dB (cnn only)")
    ap.add_argument("--tag", default="")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    cache = load_cache(args.data_dir / "cache",
                       mmap_signals=args.model == "cnn")
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    classes, win = cache["classes"], cache["win"]
    Yrun, vocab = component_matrix(meta)
    Ycomp = Yrun[idx.run]

    if args.model in FEATURE_MODELS:
        blocks = {"plain": [cache["features"]],
                  "order": [cache["order_features"]],
                  "plain+order": [cache["features"],
                                  cache["order_features"]]}[args.features]
        X = np.nan_to_num(np.concatenate(blocks, axis=1), nan=0.0,
                          posinf=0.0, neginf=0.0)
        S = None
        print(f"{X.shape[0]} windows x {X.shape[1]} features "
              f"[{args.features}] | model={args.model}")
    else:
        X, S = None, cache["signals"]
        print(f"signals {S.shape} | model=cnn")

    csv_path = (args.out / f"bench_{args.model}_"
                           f"{args.features.replace('+', '-')}{args.tag}.csv")
    if csv_path.exists():
        # Two invocations sharing a (model, features) pair land on the same
        # filename, and the second would otherwise silently discard the first
        # (how a whole multiclass sweep was once lost). Keep a copy.
        backup = csv_path.with_suffix(".prev.csv")
        backup.write_bytes(csv_path.read_bytes())
        print(f"note: {csv_path.name} exists; previous contents saved to "
              f"{backup.name}. Pass a distinct --tag to keep both.")

    rows = []
    for proto in iter_protocols(idx, meta, win, cache["n_per_run"],
                                which=args.protocols,
                                max_condition_folds=args.max_condition_folds):
        for seed in args.seeds:
            stem = (f"{proto.name}_{args.model}_{args.features}_s{seed}"
                    f"{args.tag}").replace("[", "_").replace("]", "")
            t0 = time.time()
            if args.model in FEATURE_MODELS:
                est = make_estimator(args.model, seed)
                if proto.kind == "multilabel":
                    m = eval_multilabel(est, X[proto.train],
                                        Ycomp[proto.train], X[proto.test],
                                        Ycomp[proto.test], vocab, args.out,
                                        stem)
                else:
                    m = eval_multiclass(est, X[proto.train],
                                        idx.label[proto.train], X[proto.test],
                                        idx.label[proto.test], classes,
                                        args.out, stem)
                metric_rows = [m]
            else:
                metric_rows = run_cnn(proto, S, idx.label, Ycomp, classes,
                                      vocab, args, seed, args.out, stem)
            for m in metric_rows:
                rows.append(dict(protocol=proto.name, kind=proto.kind,
                                 model=args.model, features=args.features,
                                 seed=seed,
                                 n_train=int(proto.train.sum()),
                                 n_test=int(proto.test.sum()),
                                 fit_s=round(time.time() - t0, 1), **m))
                snr = m.get("noise_snr_db")
                print(f"  {proto.name:44s} {args.model:4s} s{seed}"
                      + (f" snr={snr:g}dB" if snr is not None else "")
                      + f" acc={m['acc']:.4f} macroF1={m['macro_f1']:.4f}"
                      + (f" microF1={m['micro_f1']:.4f}"
                         if "micro_f1" in m else ""), flush=True)
            pd.DataFrame(rows).to_csv(csv_path, index=False)

    print(f"\n{len(rows)} rows -> {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
