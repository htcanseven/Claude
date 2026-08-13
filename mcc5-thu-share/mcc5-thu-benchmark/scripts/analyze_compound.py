#!/usr/bin/env python3
"""Per-combination analysis of the zero-shot compound-fault failure.

Tests the cross-modal masking hypothesis. Published zero-shot compound-fault
methods report 75-87 % on *bearing-only* compounds, where both components are
mechanical and both are visible in vibration. Eight of this dataset's nine
compounds instead pair a mechanical bearing defect with an electrical or magnetic
fault, so the two components are observable in *different* modalities. One
compound — ``bearing_outer_h_and_inner_h`` — is mechanical-only, which makes it
the internal control: if cross-modal masking is what breaks the model, that
combination should be recognised markedly better than the other eight.

Also reports, per combination, whether the mechanical or the electrical component
is the one that survives, and repeats the whole analysis using vibration-only and
current-only features to locate where each fault's evidence lives.
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
from mcc5.splits import (WindowIndex, component_matrix,         # noqa: E402
                         compositional_split, partial_credit,
                         topk_metrics, multilabel_scores)

# Which modality carries each fault's primary evidence.
ELECTRICAL = {"winding_h", "winding_l", "broken_bar", "voltage_unbalance_l",
              "static_eccentricity_h", "static_eccentricity_l",
              "dynamic_eccentricity"}

# Feature-block layout from build_cache: 18 features per channel, vibration
# channels first, then the three currents.
FEATS_PER_CHANNEL = 18
N_VIB_CH, N_CUR_CH = 3, 3


def feature_view(F: np.ndarray, which: str) -> np.ndarray:
    v = N_VIB_CH * FEATS_PER_CHANNEL
    if which == "vibration":
        return F[:, :v]
    if which == "current":
        return F[:, v:v + N_CUR_CH * FEATS_PER_CHANNEL]
    return F


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("./data"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--views", nargs="+",
                    default=["both", "vibration", "current"])
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
    is_comp = meta["is_compound"].to_numpy().astype(bool)
    tr, te = compositional_split(idx, is_comp)
    win_fault = meta["fault_full"].to_numpy()[idx.run]

    rows, comp_rows = [], []
    for view in args.views:
        X = feature_view(F, view)
        clf = OneVsRestClassifier(
            RandomForestClassifier(n_estimators=300, n_jobs=-1,
                                   random_state=args.seed), n_jobs=1)
        clf.fit(X[tr], Yw[tr])
        P = clf.predict(X[te]).astype(np.int8)
        scores = multilabel_scores(clf, X[te])
        Yte = Yw[te]
        faults_te = win_fault[te]

        overall = dict(view=view, combination="ALL",
                       n_windows=int(te.sum()),
                       exact=float((P == Yte).all(axis=1).mean()),
                       micro_f1=f1_score(Yte, P, average="micro",
                                         zero_division=0),
                       **partial_credit(P, Yte),
                       **topk_metrics(np.asarray(scores), Yte))
        rows.append(overall)
        print(f"[{view}] ALL: exact={overall['exact']:.4f} "
              f"microF1={overall['micro_f1']:.4f} "
              f"topkRecall={overall['topk_recall']:.4f}", flush=True)

        for combo in sorted(set(faults_te)):
            m = faults_te == combo
            parts = combo.split("_and_")
            # the modality label follows from which components are electrical
            kinds = {"electrical" if p in ELECTRICAL else "mechanical"
                     for p in [c for c in vocab if Yte[m][0][vocab.index(c)]]}
            kind = ("mechanical-only" if kinds == {"mechanical"}
                    else "cross-modal")
            r = dict(view=view, combination=combo, kind=kind,
                     n_windows=int(m.sum()),
                     exact=float((P[m] == Yte[m]).all(axis=1).mean()),
                     micro_f1=f1_score(Yte[m], P[m], average="micro",
                                       zero_division=0),
                     **partial_credit(P[m], Yte[m]),
                     **topk_metrics(np.asarray(scores)[m], Yte[m]))
            rows.append(r)
            print(f"  [{view}] {combo:44s} {kind:16s} "
                  f"exact={r['exact']:.4f} microF1={r['micro_f1']:.4f} "
                  f"topkRecall={r['topk_recall']:.4f}", flush=True)

            # which of the two components survived?
            for ci, c in enumerate(vocab):
                if not Yte[m][0][ci]:
                    continue
                comp_rows.append(dict(
                    view=view, combination=combo, component=c,
                    modality="electrical" if c in ELECTRICAL else "mechanical",
                    detection_rate=float(P[m][:, ci].mean())))

    pd.DataFrame(rows).to_csv(args.out / "compound_per_combination.csv",
                              index=False)
    pd.DataFrame(comp_rows).to_csv(args.out / "compound_per_component.csv",
                                   index=False)
    print(f"\n-> {args.out / 'compound_per_combination.csv'}")
    print(f"-> {args.out / 'compound_per_component.csv'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
