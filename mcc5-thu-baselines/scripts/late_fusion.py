#!/usr/bin/env python3
"""Late fusion by label union: the prescription implied by the masking analysis.

``analyze_compound.py`` shows a clean dissociation. Vibration-only features detect
the mechanical constituent of a compound fault and never the electrical one;
current-only features do the reverse. Concatenating both modalities does not
combine those abilities, it destroys one of them: ``winding_h`` is detected on
39 % of windows from current alone and on 0.2 % once vibration features are
appended. The electrical evidence is present and learnable, but in a shared
feature space the mechanical features dominate the split criterion.

So do not share the feature space. Train one multi-label model per modality and
take the union of their positive predictions. Each model then competes only
against faults visible in its own channels, which is exactly the structure the
dissociation implies -- and unlike a gated fusion embedding, nothing forces the
two families through one representation.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sklearn.ensemble import RandomForestClassifier            # noqa: E402
from sklearn.multiclass import OneVsRestClassifier             # noqa: E402
from sklearn.metrics import f1_score                           # noqa: E402

from mcc5.cache import load_cache                              # noqa: E402
from mcc5.protocols import iter_protocols                       # noqa: E402
from mcc5.splits import (WindowIndex, component_matrix,         # noqa: E402
                         partial_credit, topk_metrics,
                         multilabel_scores)

FEATS_PER_CHANNEL = 18
N_VIB_CH, N_CUR_CH = 3, 3
VIB = slice(0, N_VIB_CH * FEATS_PER_CHANNEL)
CUR = slice(N_VIB_CH * FEATS_PER_CHANNEL,
            (N_VIB_CH + N_CUR_CH) * FEATS_PER_CHANNEL)


def fit_predict(X, Ytr, tr, te, seed):
    clf = OneVsRestClassifier(
        RandomForestClassifier(n_estimators=300, n_jobs=-1,
                               random_state=seed), n_jobs=1)
    clf.fit(X[tr], Ytr)
    return (clf.predict(X[te]).astype(np.int8),
            multilabel_scores(clf, X[te]))


def metrics(name, P, scores, Yte, extra=None):
    row = dict(model=name,
               exact=float((P == Yte).all(axis=1).mean()),
               micro_f1=f1_score(Yte, P, average="micro", zero_division=0),
               macro_f1=f1_score(Yte, P, average="macro", zero_division=0),
               **partial_credit(P, Yte),
               **topk_metrics(np.asarray(scores), Yte))
    row.update(extra or {})
    print(f"  {name:22s} exact={row['exact']:.4f} "
          f"microF1={row['micro_f1']:.4f} "
          f"anyFound={row['any_component_found']:.3f} "
          f"allZero={row['all_zero_prediction_rate']:.3f}", flush=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--seeds", type=int, nargs="+", default=[0])
    ap.add_argument("--protocols", nargs="+",
                    default=["compositional_zeroshot", "leave_combination_out"])
    ap.add_argument("--resume", action="store_true",
                    help="skip (protocol, seed) pairs already in the CSV")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    meta = pd.read_csv(args.data_dir / "metadata.csv")
    meta = meta[meta.fault_full != "UNPARSED"].reset_index(drop=True)
    cache = load_cache(args.data_dir / "cache", mmap_signals=False)
    idx = WindowIndex(run=cache["run"], start=cache["start"],
                      label=cache["label"], condition=cache["condition"],
                      stationary=cache["stationary"])
    F = np.nan_to_num(cache["features"], nan=0.0, posinf=0.0, neginf=0.0)
    Yrun, vocab = component_matrix(meta)
    Yw = Yrun[idx.run]

    out = args.out / "late_fusion.csv"
    rows, done = [], set()
    if args.resume and out.exists():
        prev = pd.read_csv(out)
        rows = prev.to_dict("records")
        done = {(str(r["protocol"]), int(r["seed"])) for _, r in prev.iterrows()}
        print(f"resuming: {len(done)} (protocol, seed) pairs already done")

    for proto in iter_protocols(idx, meta, cache["win"], cache["n_per_run"],
                                which=args.protocols):
        print(f"{proto.name}  (train={proto.train.sum()} "
              f"test={proto.test.sum()})")
        Yte = Yw[proto.test]
        for seed in args.seeds:
            if (proto.name, seed) in done:
                print(f"  seed {seed}: cached")
                continue
            Pb, Sb = fit_predict(F, Yw[proto.train], proto.train, proto.test,
                                 seed)
            rows.append(metrics("shared (both)", Pb, Sb, Yte,
                                dict(protocol=proto.name, seed=seed)))

            Pv, Sv = fit_predict(F[:, VIB], Yw[proto.train], proto.train,
                                 proto.test, seed)
            rows.append(metrics("vibration only", Pv, Sv, Yte,
                                dict(protocol=proto.name, seed=seed)))

            Pc, Sc = fit_predict(F[:, CUR], Yw[proto.train], proto.train,
                                 proto.test, seed)
            rows.append(metrics("current only", Pc, Sc, Yte,
                                dict(protocol=proto.name, seed=seed)))

            # the prescription: union of positives, max of scores
            Pu = np.maximum(Pv, Pc)
            Su = np.maximum(np.asarray(Sv), np.asarray(Sc))
            rows.append(metrics("late fusion (union)", Pu, Su, Yte,
                                dict(protocol=proto.name, seed=seed)))
            pd.DataFrame(rows).to_csv(out, index=False)

    pd.DataFrame(rows).to_csv(out, index=False)
    print(f"\n-> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
