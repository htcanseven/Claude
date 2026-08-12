#!/usr/bin/env python3
"""Train the proposed CompositionalNet and its ablations on all protocols.

Losses
  component  BCE over fault components (multi-label; compound = union)
  condition  cross-entropy behind a gradient-reversal layer, weight ramped
             from 0 so the trunk first learns to discriminate faults and only
             then is pushed to forget the operating condition

Training also superposes pairs of same-condition single-fault windows to
manufacture compound examples (see ``make_mixer``), which is the only way to
show the model a two-fault label when no compound data may be seen.

Ablations (--variant)
  full          fusion + adversarial + physics features + superposition
  no_mix        drop the fault-superposition augmentation
  no_adv        drop the adversarial condition objective
  no_physics    drop the order-domain features
  no_fusion     single encoder over all six channels (no cross-modal gate)

Reported metrics separate a representation failure from a threshold failure:
``exact``/``microF1`` threshold the logits at zero, while ``topkExact``/
``topkRecall`` only rank them.
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

from sklearn.metrics import f1_score, accuracy_score               # noqa: E402

from mcc5.cache import load_cache                                  # noqa: E402
from mcc5.models import CompositionalNet, CNN1D                    # noqa: E402
from mcc5.splits import (WindowIndex, component_matrix,             # noqa: E402
                         partial_credit, topk_metrics)
from mcc5 import splits as sp                                      # noqa: E402

N_VIB = 3  # first three cached channels are the triaxial vibration
N_CUR = 3  # last three are the phase currents


def standardize(tr, te):
    mu = tr.mean(axis=(0, 2), keepdims=True)
    sd = tr.std(axis=(0, 2), keepdims=True) + 1e-8
    return (tr - mu) / sd, (te - mu) / sd


def std_2d(tr, te):
    mu, sd = tr.mean(0, keepdims=True), tr.std(0, keepdims=True) + 1e-8
    return (tr - mu) / sd, (te - mu) / sd


def make_mixer(Y: np.ndarray, cond: np.ndarray, rng):
    """Sample partners for fault-superposition augmentation.

    A linear structure excited by two independent faults responds, to first
    order, with the sum of the two responses, so adding two single-fault windows
    recorded at the same operating point approximates a compound-fault window
    and its label is the union of the two component sets. That manufactures
    compound training examples from single-fault data only, which is what the
    zero-shot setting forbids obtaining any other way.

    Partners are drawn from the same operating condition (mixing 1000 rpm with
    3000 rpm would fabricate a machine running at two speeds at once) and are
    required to carry a different component.
    """
    by_cond: dict[int, np.ndarray] = {}
    for c in np.unique(cond):
        by_cond[int(c)] = np.flatnonzero(cond == c)

    def sample(i: int) -> int | None:
        pool = by_cond.get(int(cond[i]))
        if pool is None or len(pool) < 2:
            return None
        for _ in range(8):  # rejection-sample a partner with a different fault
            j = int(pool[rng.integers(len(pool))])
            if not np.array_equal(Y[j], Y[i]):
                return j
        return None

    return sample


def make_batch(idxs, X, E, Y, sample, rng, mix_prob: float):
    """Assemble one batch, superposing a fraction with same-condition partners."""
    xb, eb, yb = X[idxs].copy(), E[idxs].copy(), Y[idxs].copy()
    if mix_prob > 0:
        for b, i in enumerate(idxs):
            if rng.random() >= mix_prob:
                continue
            j = sample(int(i))
            if j is None:
                continue
            # /sqrt(2) keeps the summed signal near the unit variance the
            # encoder saw during standardization
            xb[b] = (X[i] + X[j]) / np.sqrt(2.0)
            if eb.shape[1]:
                # band energies of a mixture carry both faults' indicators;
                # take the stronger of each rather than summing standardized
                # values, whose offsets would not add meaningfully
                eb[b] = np.maximum(E[i], E[j])
            yb[b] = np.maximum(Y[i], Y[j])
    return xb, eb, yb


def build_model(variant, n_comp, n_cond, n_extra):
    return CompositionalNet(N_VIB, N_CUR, n_comp, n_cond, n_extra=n_extra,
                            fusion=variant != "no_fusion")


def forward_batch(model, variant, xb, eb, lambd):
    # split channels into the two modalities; the no_fusion variant
    # concatenates them internally instead of gating
    return model(xb[:, :N_VIB], xb[:, N_VIB:], eb, lambd)


def run_protocol(name, S, E, Ycomp, ycond, tr, te, variant, args, rows):
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    Xtr, Xte = standardize(np.ascontiguousarray(S[tr]),
                           np.ascontiguousarray(S[te]))
    use_phys = variant != "no_physics" and E is not None
    if use_phys:
        Etr, Ete = std_2d(E[tr], E[te])
    else:
        Etr = np.zeros((tr.sum(), 0), np.float32)
        Ete = np.zeros((te.sum(), 0), np.float32)
    Ytr, Yte = Ycomp[tr], Ycomp[te]
    ctr = ycond[tr]

    mix_prob = 0.0 if variant == "no_mix" else args.mix_prob

    for seed in args.seeds:
        torch.manual_seed(seed)
        rng = np.random.default_rng(seed)
        model = build_model(variant, Ycomp.shape[1], int(ycond.max()) + 1,
                            Etr.shape[1]).to(dev)
        opt = torch.optim.AdamW(model.parameters(), lr=args.lr)
        bce, ce = nn.BCEWithLogitsLoss(), nn.CrossEntropyLoss()
        sample = make_mixer(Ytr, ctr, rng)
        n = len(Ytr)
        t0 = time.time()
        for ep in range(args.epochs):
            model.train()
            # ramp the adversarial weight: discriminate first, then forget
            lambd = (0.0 if variant == "no_adv"
                     else args.adv_weight * min(1.0, ep / max(args.epochs / 2, 1)))
            perm = rng.permutation(n)
            tot = 0.0
            for s in range(0, n, args.bs):
                idxs = perm[s:s + args.bs]
                xb_np, eb_np, yb_np = make_batch(idxs, Xtr, Etr, Ytr, sample,
                                                 rng, mix_prob)
                xb = torch.from_numpy(xb_np).to(dev)
                eb = torch.from_numpy(eb_np).to(dev)
                yb = torch.from_numpy(yb_np.astype(np.float32)).to(dev)
                cb = torch.from_numpy(ctr[idxs].astype(np.int64)).to(dev)
                opt.zero_grad()
                cl, dlog, _, _ = forward_batch(model, variant, xb, eb, lambd)
                loss = bce(cl, yb)
                if lambd > 0:
                    loss = loss + ce(dlog, cb)
                loss.backward()
                opt.step()
                tot += loss.item() * len(idxs)
            if (ep + 1) % 4 == 0:
                print(f"    s{seed} ep{ep + 1}/{args.epochs} "
                      f"loss={tot / n:.4f} lambda={lambd:.2f} "
                      f"mix={mix_prob:.2f}", flush=True)
        model.eval()
        outs = []
        with torch.no_grad():
            for i in range(0, len(Xte), 256):
                xb = torch.from_numpy(Xte[i:i + 256]).to(dev)
                eb = torch.from_numpy(Ete[i:i + 256]).to(dev)
                cl, _, _, _ = forward_batch(model, variant, xb, eb, 0.0)
                outs.append(cl.cpu().numpy())
        scores = np.concatenate(outs)
        P = (scores > 0).astype(np.int8)
        exact = float((P == Yte).all(axis=1).mean())
        pc = partial_credit(P, Yte)
        tk = topk_metrics(scores, Yte)
        rows.append(dict(protocol=name, model=f"proposed[{variant}]", seed=seed,
                         acc=exact,
                         macro_f1=f1_score(Yte, P, average="macro",
                                           zero_division=0),
                         micro_f1=f1_score(Yte, P, average="micro",
                                           zero_division=0),
                         hamming=float((P == Yte).mean()),
                         **pc, **tk,
                         n_train=int(tr.sum()), n_test=int(te.sum()),
                         fit_s=round(time.time() - t0, 1)))
        print(f"  {name:30s} {variant:11s} s{seed} exact={exact:.4f} "
              f"microF1={rows[-1]['micro_f1']:.4f} "
              f"topkExact={tk['topk_exact']:.4f} "
              f"topkRecall={tk['topk_recall']:.4f}", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--epochs", type=int, default=12)
    ap.add_argument("--bs", type=int, default=64)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--adv-weight", type=float, default=0.3)
    ap.add_argument("--mix-prob", type=float, default=0.5,
                    help="fraction of each batch replaced by a superposed "
                         "same-condition fault pair (0 disables)")
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    ap.add_argument("--variants", nargs="+",
                    default=["full", "no_mix", "no_adv", "no_physics",
                             "no_fusion"])
    ap.add_argument("--protocols", nargs="+",
                    default=["compositional", "unknown_condition",
                             "steady_to_transitional"])
    ap.add_argument("--n-held-out", type=int, default=2)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    cache = load_cache(args.data_dir / "cache", mmap_signals=True)
    S = cache["signals"]
    E = cache.get("order_features")
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    Yrun, vocab = component_matrix(meta)
    Ycomp = Yrun[idx.run]
    conds = sorted(pd.unique(idx.condition))
    cond_id = {c: i for i, c in enumerate(conds)}
    ycond = np.array([cond_id[c] for c in idx.condition])
    print(f"signals {S.shape} | components {len(vocab)} | conditions "
          f"{len(conds)}")

    rows: list[dict] = []
    for variant in args.variants:
        if "compositional" in args.protocols:
            is_comp = meta["is_compound"].to_numpy().astype(bool)
            tr, te = sp.compositional_split(idx, is_comp)
            run_protocol("compositional_zeroshot", S, E, Ycomp, ycond, tr, te,
                         variant, args, rows)
        if "unknown_condition" in args.protocols:
            for c in conds[: args.n_held_out]:
                tr, te = sp.unknown_condition_split(idx, c)
                run_protocol(f"unknown_condition[{c}]", S, E, Ycomp, ycond,
                             tr, te, variant, args, rows)
        if "steady_to_transitional" in args.protocols:
            tr, te = sp.steady_to_transitional_split(idx)
            run_protocol("steady_to_transitional", S, E, Ycomp, ycond, tr, te,
                         variant, args, rows)

    pd.DataFrame(rows).to_csv(args.out / "proposed.csv", index=False)
    print(f"\nresults -> {args.out / 'proposed.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
