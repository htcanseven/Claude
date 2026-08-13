#!/usr/bin/env python3
"""Trivial constant-predictor baselines for the compound-fault metrics.

Every compound in this dataset pairs exactly one bearing constituent with one
other mechanism, and the inner- and outer-race constituents each appear in 60 of
the 108 compound runs. A predictor that ignores the input and always emits the
two bearing constituents therefore scores well on several standard multi-label
metrics -- exact match 0.111 and at-least-one-recovered 1.000 -- which is above
what several published-style pipelines achieve.

Reporting compound metrics without this reference makes an at-or-below-chance
result look like a positive one. Run this alongside any compound experiment.

Two label schemes are reported:
  9-constituent   severities merged (finner, fouter, fball, fbend, fbar, fdyn,
                  fstat, fvu, fwind) -- the scheme used in the collaborator draft
  15-component    severities kept separate -- the scheme used by this repository
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sklearn.metrics import f1_score                            # noqa: E402

from mcc5.cache import load_cache                               # noqa: E402
from mcc5.splits import (WindowIndex, component_matrix,          # noqa: E402
                         compositional_split, partial_credit)

NINE = ["fball", "finner", "fouter", "fbend", "fbar", "fdyn", "fstat", "fvu",
        "fwind"]


def to_nine(component: str) -> str | None:
    """Map a severity-split component onto the 9-constituent scheme."""
    c = component.strip()
    if c.startswith("bearing_inner"):
        return "finner"
    if c.startswith("bearing_outer"):
        return "fouter"
    if c.startswith("bearing_ball"):
        return "fball"
    if c.startswith("static_eccentricity"):
        return "fstat"
    if c.startswith("dynamic_eccentricity"):
        return "fdyn"
    if c.startswith("winding"):
        return "fwind"
    if c.startswith("voltage_unbalance"):
        return "fvu"
    if c == "broken_bar":
        return "fbar"
    if c == "bend":
        return "fbend"
    if c == "health":
        return None
    raise ValueError(f"unmapped component: {component!r}")


def score_constant(pred: set, truth_sets: list[set]) -> dict:
    """Set-level metrics for a constant predictor over run-level truth sets."""
    n = len(truth_sets)
    tp = fa = em = rany = rall = 0
    rc_num = rc_den = 0
    for t in truth_sets:
        inter = pred & t
        rc_num += len(inter)
        rc_den += len(t)
        fa += len(pred - t)
        em += pred == t
        rany += len(inter) > 0
        rall += inter == t
    return dict(EM=em / n, R_const=rc_num / rc_den, R_any=rany / n,
                R_all=rall / n, FA_per_run=fa / n)


def report_nine(meta: pd.DataFrame) -> None:
    comp = meta[meta.is_compound]
    truth = []
    for s in comp.components:
        cs = {to_nine(x) for x in str(s).split("+")}
        truth.append({c for c in cs if c})
    print(f"\n=== 9-constituent scheme, {len(truth)} compound runs ===")
    from collections import Counter
    freq = Counter(c for t in truth for c in t)
    print("constituent frequency: "
          + ", ".join(f"{k}={v}" for k, v in freq.most_common()))
    never = [c for c in NINE if c not in freq]
    print(f"never in any compound: {never}")
    cands = {
        "{finner, fouter}": {"finner", "fouter"},
        "{finner, fouter, fbar}": {"finner", "fouter", "fbar"},
        "{finner}": {"finner"},
        "all 9": set(NINE),
    }
    print(f"\n  {'predictor':26s} {'EM':>7s} {'R_const':>8s} {'R_any':>7s} "
          f"{'R_all':>7s} {'FA/run':>7s}")
    for name, p in cands.items():
        r = score_constant(p, truth)
        print(f"  {name:26s} {r['EM']:7.4f} {r['R_const']:8.4f} "
              f"{r['R_any']:7.4f} {r['R_all']:7.4f} {r['FA_per_run']:7.4f}")


def report_fifteen(data_dir: Path, meta: pd.DataFrame) -> None:
    cache = load_cache(data_dir / "cache", mmap_signals=False)
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    Yrun, vocab = component_matrix(meta)
    Yw = Yrun[idx.run]
    is_comp = meta["is_compound"].to_numpy().astype(bool)
    _, te = compositional_split(idx, is_comp)
    Yte = Yw[te]
    print(f"\n=== 15-component scheme, {Yte.shape[0]} compound test windows ===")
    cands = {
        "{bearing_inner_h, bearing_outer_h}": ["bearing_inner_h",
                                               "bearing_outer_h"],
        "{bearing_inner_h}": ["bearing_inner_h"],
        "all 15": list(vocab),
    }
    print(f"\n  {'predictor':36s} {'exact':>7s} {'microF1':>8s} {'anyFound':>9s}")
    for name, comps in cands.items():
        P = np.zeros_like(Yte)
        for c in comps:
            P[:, vocab.index(c)] = 1
        pc = partial_credit(P, Yte)
        print(f"  {name:36s} {float((P == Yte).all(1).mean()):7.4f} "
              f"{f1_score(Yte, P, average='micro', zero_division=0):8.4f} "
              f"{pc['any_component_found']:9.4f}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    args = ap.parse_args()
    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    report_nine(meta)
    if (args.data_dir / "cache" / "window_cache.npz").exists():
        report_fifteen(args.data_dir, meta)
    else:
        print("\n(skipping 15-component scheme: no window cache; "
              "run scripts/build_cache.py)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
