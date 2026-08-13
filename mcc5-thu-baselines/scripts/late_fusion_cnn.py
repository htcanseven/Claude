#!/usr/bin/env python3
"""Combine the two interventions that address different halves of the failure.

The compound-fault analysis found two independent causes:

1. *No two-positive training signal.* Trained only on single faults, every window
   carries exactly one positive of fifteen, so the head learns to push one logit
   up and the rest far down and can never assert two faults at once.
   Superposition augmentation supplies the missing signal by adding two
   single-fault windows recorded at the same operating point.
2. *Feature-space dominance.* Vibration and current features detect disjoint
   fault families, but sharing one representation destroys the weaker: winding
   faults are detected on 39 % of windows from current alone and 0.2 % once
   vibration is concatenated. Late fusion keeps one model per modality and unions
   their positives, so each competes only within its own channels.

Neither addresses the other's cause, so this trains per-modality CNNs *with*
superposition and unions them. Reports every arm, not only the combination, so
the contribution of each half is visible.
"""
import argparse
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sklearn.metrics import f1_score                            # noqa: E402

from mcc5.cache import load_cache                               # noqa: E402
from mcc5.models import CNN1D                                   # noqa: E402
from mcc5.protocols import iter_protocols                        # noqa: E402
from mcc5.splits import (WindowIndex, component_matrix,          # noqa: E402
                         partial_credit, topk_metrics)

VIB = [0, 1, 2]
CUR = [3, 4, 5]


def make_mixer(Y, cond, rng):
    """Same-condition partner sampler for fault superposition."""
    by_cond = {int(c): np.flatnonzero(cond == c) for c in np.unique(cond)}

    def sample(i):
        pool = by_cond.get(int(cond[i]))
        if pool is None or len(pool) < 2:
            return None
        for _ in range(8):
            j = int(pool[rng.integers(len(pool))])
            if not np.array_equal(Y[j], Y[i]):
                return j
        return None
    return sample


def train_one(X, Y, cond, n_out, seed, epochs, bs, lr, mix_prob, log_prefix):
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    torch.manual_seed(seed)
    rng = np.random.default_rng(seed)
    model = CNN1D(X.shape[1], n_out).to(dev)
    opt = torch.optim.AdamW(model.parameters(), lr=lr)
    lossf = nn.BCEWithLogitsLoss()
    sample = make_mixer(Y, cond, rng)
    n = len(Y)
    for ep in range(epochs):
        model.train()
        perm = rng.permutation(n)
        tot = 0.0
        for s in range(0, n, bs):
            idxs = perm[s:s + bs]
            xb_np, yb_np = X[idxs].copy(), Y[idxs].copy()
            if mix_prob > 0:
                for b, i in enumerate(idxs):
                    if rng.random() >= mix_prob:
                        continue
                    j = sample(int(i))
                    if j is None:
                        continue
                    # /sqrt(2) keeps the sum near the unit variance the encoder
                    # was standardized for
                    xb_np[b] = (X[i] + X[j]) / np.sqrt(2.0)
                    yb_np[b] = np.maximum(Y[i], Y[j])
            xb = torch.from_numpy(xb_np).to(dev)
            yb = torch.from_numpy(yb_np.astype(np.float32)).to(dev)
            opt.zero_grad()
            loss = lossf(model(xb), yb)
            loss.backward()
            opt.step()
            tot += loss.item() * len(idxs)
        if (ep + 1) % 5 == 0:
            print(f"    {log_prefix} ep{ep + 1}/{epochs} loss={tot / n:.4f}",
                  flush=True)
    return model


def predict(model, X, bs=256):
    dev = next(model.parameters()).device
    model.eval()
    outs = []
    with torch.no_grad():
        for i in range(0, len(X), bs):
            xb = torch.from_numpy(np.ascontiguousarray(X[i:i + bs])).to(dev)
            outs.append(model(xb).cpu().numpy())
    return np.concatenate(outs)


def standardize(tr, te):
    mu = tr.mean(axis=(0, 2), keepdims=True)
    sd = tr.std(axis=(0, 2), keepdims=True) + 1e-8
    return ((tr - mu) / sd).astype(np.float32), ((te - mu) / sd).astype(np.float32)


def score(name, logits, Yte, rows, extra):
    P = (logits > 0).astype(np.int8)
    row = dict(arm=name,
               exact=float((P == Yte).all(axis=1).mean()),
               micro_f1=f1_score(Yte, P, average="micro", zero_division=0),
               macro_f1=f1_score(Yte, P, average="macro", zero_division=0),
               **partial_credit(P, Yte), **topk_metrics(logits, Yte), **extra)
    rows.append(row)
    print(f"  {name:34s} exact={row['exact']:.4f} "
          f"microF1={row['micro_f1']:.4f} "
          f"anyFound={row['any_component_found']:.3f} "
          f"allZero={row['all_zero_prediction_rate']:.3f}", flush=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--seeds", type=int, nargs="+", default=[0])
    ap.add_argument("--epochs", type=int, default=15)
    ap.add_argument("--bs", type=int, default=64)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--mix-prob", type=float, default=0.5)
    ap.add_argument("--protocols", nargs="+",
                    default=["compositional_zeroshot", "leave_combination_out"])
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    csv_path = args.out / "late_fusion_cnn.csv"

    rows = []
    done = set()
    if args.resume and csv_path.exists():
        prev = pd.read_csv(csv_path)
        rows = prev.to_dict("records")
        done = {(str(r["protocol"]), int(r["seed"])) for _, r in prev.iterrows()}
        print(f"resuming: {len(done)} (protocol, seed) pairs already done")

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    cache = load_cache(args.data_dir / "cache", mmap_signals=True)
    S = cache["signals"]
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    Yrun, vocab = component_matrix(meta)
    Yw = Yrun[idx.run]
    conds = sorted(pd.unique(idx.condition))
    cond_id = {c: i for i, c in enumerate(conds)}
    ycond = np.array([cond_id[c] for c in idx.condition])

    for proto in iter_protocols(idx, meta, cache["win"], cache["n_per_run"],
                                which=args.protocols):
        print(f"\n{proto.name}  train={proto.train.sum()} "
              f"test={proto.test.sum()}")
        Ytr, Yte = Yw[proto.train], Yw[proto.test]
        ctr = ycond[proto.train]
        for seed in args.seeds:
            if (proto.name, seed) in done:
                print(f"  seed {seed}: cached")
                continue
            t0 = time.time()
            extra = dict(protocol=proto.name, seed=seed,
                         n_train=int(proto.train.sum()),
                         n_test=int(proto.test.sum()))
            arms = {}
            for tag, chans in (("vib", VIB), ("cur", CUR)):
                Xtr, Xte = standardize(
                    np.ascontiguousarray(S[proto.train][:, chans]),
                    np.ascontiguousarray(S[proto.test][:, chans]))
                for mixp, mixname in ((0.0, "nomix"), (args.mix_prob, "mix")):
                    m = train_one(Xtr, Ytr, ctr, Yte.shape[1], seed,
                                  args.epochs, args.bs, args.lr, mixp,
                                  f"s{seed}/{tag}/{mixname}")
                    arms[(tag, mixname)] = predict(m, Xte)
                    del m
                del Xtr, Xte
            # shared-feature-space reference: both modalities, one model
            Xtr, Xte = standardize(
                np.ascontiguousarray(S[proto.train]),
                np.ascontiguousarray(S[proto.test]))
            for mixp, mixname in ((0.0, "nomix"), (args.mix_prob, "mix")):
                m = train_one(Xtr, Ytr, ctr, Yte.shape[1], seed, args.epochs,
                              args.bs, args.lr, mixp,
                              f"s{seed}/both/{mixname}")
                arms[("both", mixname)] = predict(m, Xte)
                del m
            del Xtr, Xte

            for mixname in ("nomix", "mix"):
                score(f"shared[{mixname}]", arms[("both", mixname)], Yte,
                      rows, extra)
                score(f"vibration[{mixname}]", arms[("vib", mixname)], Yte,
                      rows, extra)
                score(f"current[{mixname}]", arms[("cur", mixname)], Yte,
                      rows, extra)
                score(f"late_fusion[{mixname}]",
                      np.maximum(arms[("vib", mixname)],
                                 arms[("cur", mixname)]), Yte, rows, extra)
            print(f"  (seed {seed} took {time.time() - t0:.0f}s)")
            pd.DataFrame(rows).to_csv(csv_path, index=False)

    pd.DataFrame(rows).to_csv(csv_path, index=False)
    print(f"\n-> {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
