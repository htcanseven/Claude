#!/usr/bin/env python3
"""1D-CNN baseline (WDCNN-style) on raw multichannel windows, all protocols."""
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

from mcc5.dataset import build_index, materialize_signals      # noqa: E402
from mcc5.models import CNN1D                                  # noqa: E402
from mcc5 import splits as sp                                  # noqa: E402

WIN = 8192
HOP = 8192
DECIMATE = 4  # -> 2048 samples per window at 3.2 kHz


def standardize(train: np.ndarray, *others):
    mu = train.mean(axis=(0, 2), keepdims=True)
    sd = train.std(axis=(0, 2), keepdims=True) + 1e-8
    return tuple((a - mu) / sd for a in (train, *others))


def train_eval(name, Xtr, ytr, Xte, yte, n_classes, rows, out_dir,
               epochs=15, bs=64, lr=1e-3, seed=0):
    torch.manual_seed(seed)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    model = CNN1D(Xtr.shape[1], n_classes).to(dev)
    opt = torch.optim.AdamW(model.parameters(), lr=lr)
    lossf = nn.CrossEntropyLoss()
    dl = DataLoader(
        TensorDataset(torch.from_numpy(Xtr), torch.from_numpy(ytr)),
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
        print(f"  ep{ep + 1}: loss={tot / len(ytr):.4f}", flush=True)
    model.eval()
    preds = []
    with torch.no_grad():
        for i in range(0, len(Xte), 256):
            xb = torch.from_numpy(Xte[i:i + 256]).to(dev)
            preds.append(model(xb).argmax(1).cpu().numpy())
    pred = np.concatenate(preds)
    acc = accuracy_score(yte, pred)
    f1 = f1_score(yte, pred, average="macro")
    rows.append(dict(protocol=name, model="cnn1d", acc=acc, macro_f1=f1,
                     n_train=len(ytr), n_test=len(yte),
                     fit_s=round(time.time() - t0, 1)))
    print(f"{name:28s} cnn  acc={acc:.4f} macroF1={f1:.4f}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--epochs", type=int, default=15)
    ap.add_argument("--n-held-out", type=int, default=1)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    idx, n_per_run, classes = build_index(args.data_dir, meta, WIN, HOP)
    rows: list[dict] = []

    def run(name, tr, te):
        Xtr = materialize_signals(args.data_dir, meta, idx, tr, WIN, DECIMATE)
        Xte = materialize_signals(args.data_dir, meta, idx, te, WIN, DECIMATE)
        Xtr, Xte = standardize(Xtr, Xte)
        train_eval(name, Xtr, idx.label[tr], Xte, idx.label[te],
                   len(classes), rows, args.out, epochs=args.epochs)

    tr, te = sp.in_condition_split(idx, n_per_run, WIN)
    run("in_condition", tr, te)

    for cond in sorted(meta.condition.unique())[: args.n_held_out]:
        tr, te = sp.unknown_condition_split(idx, cond)
        if te.sum():
            run(f"unknown_condition[{cond}]", tr, te)

    tr, te = sp.steady_to_transitional_split(idx)
    if tr.sum() and te.sum():
        run("steady_to_transitional", tr, te)

    pd.DataFrame(rows).to_csv(args.out / "cnn_baseline.csv", index=False)
    print(f"results -> {args.out / 'cnn_baseline.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
