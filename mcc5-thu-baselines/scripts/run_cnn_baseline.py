#!/usr/bin/env python3
"""1D-CNN baseline (WDCNN-style) on cached raw windows, all four protocols.

For the compositional protocol the head is switched to multi-label
(sigmoid + BCE) over fault components, so unseen compound faults can be
predicted as the union of their single-fault components.
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sklearn.metrics import accuracy_score, f1_score           # noqa: E402

from mcc5.cache import load_cache                              # noqa: E402
from mcc5.models import CNN1D                                  # noqa: E402
from mcc5.splits import WindowIndex, component_matrix           # noqa: E402
from mcc5 import splits as sp                                  # noqa: E402


def standardize(train: np.ndarray, test: np.ndarray):
    mu = train.mean(axis=(0, 2), keepdims=True)
    sd = train.std(axis=(0, 2), keepdims=True) + 1e-8
    return (train - mu) / sd, (test - mu) / sd


def train_eval(name, Xtr, ytr, Xte, yte, n_out, rows, seeds,
               multilabel=False, vocab=None, out_dir=None,
               epochs=12, bs=64, lr=1e-3):
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    for seed in seeds:
        torch.manual_seed(seed)
        np.random.seed(seed)
        model = CNN1D(Xtr.shape[1], n_out).to(dev)
        opt = torch.optim.AdamW(model.parameters(), lr=lr)
        lossf = nn.BCEWithLogitsLoss() if multilabel else nn.CrossEntropyLoss()
        yt = torch.from_numpy(ytr.astype(
            np.float32 if multilabel else np.int64))
        dl = DataLoader(TensorDataset(torch.from_numpy(Xtr), yt),
                        batch_size=bs, shuffle=True, num_workers=0)
        t0 = time.time()
        for ep in range(epochs):
            model.train()
            tot = 0.0
            for xb, yb in dl:
                xb, yb = xb.to(dev), yb.to(dev)
                opt.zero_grad()
                loss = lossf(model(xb), yb)
                loss.backward()
                opt.step()
                tot += loss.item() * len(yb)
            if (ep + 1) % 4 == 0:
                print(f"    s{seed} ep{ep + 1}/{epochs} "
                      f"loss={tot / len(ytr):.4f}", flush=True)
        model.eval()
        outs = []
        with torch.no_grad():
            for i in range(0, len(Xte), 256):
                xb = torch.from_numpy(np.ascontiguousarray(Xte[i:i + 256]))
                outs.append(model(xb.to(dev)).cpu().numpy())
        logits = np.concatenate(outs)
        fit_s = round(time.time() - t0, 1)
        if multilabel:
            P = (logits > 0).astype(np.int8)
            exact = float((P == yte).all(axis=1).mean())
            micro = f1_score(yte, P, average="micro", zero_division=0)
            macro = f1_score(yte, P, average="macro", zero_division=0)
            rows.append(dict(protocol=name, model="cnn1d", seed=seed,
                             acc=exact, macro_f1=macro, micro_f1=micro,
                             hamming=float((P == yte).mean()),
                             n_train=len(ytr), n_test=len(yte), fit_s=fit_s))
            print(f"  {name:34s} cnn  s{seed} exact={exact:.4f} "
                  f"microF1={micro:.4f}", flush=True)
            if out_dir is not None and seed == seeds[0] and vocab:
                pd.DataFrame({
                    "component": vocab,
                    "support_test": yte.sum(axis=0),
                    "f1": f1_score(yte, P, average=None, zero_division=0),
                }).to_csv(out_dir / "components_cnn1d.csv", index=False)
        else:
            pred = logits.argmax(1)
            acc = accuracy_score(yte, pred)
            f1 = f1_score(yte, pred, average="macro")
            rows.append(dict(protocol=name, model="cnn1d", seed=seed,
                             acc=acc, macro_f1=f1, n_train=len(ytr),
                             n_test=len(yte), fit_s=fit_s))
            print(f"  {name:34s} cnn  s{seed} acc={acc:.4f} "
                  f"macroF1={f1:.4f}", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--epochs", type=int, default=12)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1])
    ap.add_argument("--n-held-out", type=int, default=3)
    ap.add_argument("--protocols", nargs="+",
                    default=["in_condition", "unknown_condition",
                             "steady_to_transitional", "compositional"])
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    cache = load_cache(args.data_dir / "cache", mmap_signals=True)
    if "signals" not in cache:
        print("error: no cached signals; rerun build_cache.py without "
              "--no-signals")
        return 1
    S = cache["signals"]
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    classes = cache["classes"]
    win = cache["win"]
    print(f"signals {S.shape} | {len(classes)} classes")

    rows: list[dict] = []

    def run(name, tr, te, multilabel=False, Y=None, vocab=None):
        Xtr = np.ascontiguousarray(S[tr])
        Xte = np.ascontiguousarray(S[te])
        Xtr, Xte = standardize(Xtr, Xte)
        if multilabel:
            train_eval(name, Xtr, Y[tr], Xte, Y[te], Y.shape[1], rows,
                       args.seeds, multilabel=True, vocab=vocab,
                       out_dir=args.out, epochs=args.epochs)
        else:
            train_eval(name, Xtr, idx.label[tr], Xte, idx.label[te],
                       len(classes), rows, args.seeds, epochs=args.epochs)
        del Xtr, Xte

    if "in_condition" in args.protocols:
        tr, te = sp.in_condition_split(idx, cache["n_per_run"], win)
        run("in_condition", tr, te)

    if "unknown_condition" in args.protocols:
        for cond in sorted(pd.unique(idx.condition))[: args.n_held_out]:
            tr, te = sp.unknown_condition_split(idx, cond)
            if te.sum():
                run(f"unknown_condition[{cond}]", tr, te)

    if "steady_to_transitional" in args.protocols:
        tr, te = sp.steady_to_transitional_split(idx)
        if tr.sum() and te.sum():
            run("steady_to_transitional", tr, te)

    if "compositional" in args.protocols:
        Yrun, vocab = component_matrix(meta)
        is_comp = meta["is_compound"].to_numpy().astype(bool)
        tr, te = sp.compositional_split(idx, is_comp)
        run("compositional_zeroshot", tr, te, multilabel=True,
            Y=Yrun[idx.run], vocab=vocab)

    pd.DataFrame(rows).to_csv(args.out / "cnn_baseline.csv", index=False)
    print(f"\nresults -> {args.out / 'cnn_baseline.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
