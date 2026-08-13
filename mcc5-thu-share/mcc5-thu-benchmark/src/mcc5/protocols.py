"""Single source of truth for the benchmark's evaluation protocols.

Every baseline enumerates splits through :func:`iter_protocols`, so a number
reported for one model is comparable to a number reported for another by
construction rather than by convention. Adding a protocol here makes it
available to all baselines at once.

Each protocol yields a :class:`Protocol` with boolean train/test window masks
and a ``kind``:

``multiclass``
    24-way fault classification.
``multilabel``
    15-way fault-component prediction; a compound fault is the union of its
    components, so unseen combinations stay expressible.

Ordered from the most optimistic protocol to the hardest, which is the order the
paper reports them in.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

import numpy as np
import pandas as pd

from . import splits as sp
from .splits import WindowIndex

# Presentation order, from optimistic to hardest.
PROTOCOL_ORDER = [
    "leaky_random",
    "in_condition",
    "unknown_condition",
    "cross_profile",
    "single_source",
    "steady_to_transitional",
    "compositional_control",
    "leave_combination_out",
    "compositional_zeroshot",
]

ALL_PROTOCOLS = list(PROTOCOL_ORDER)


@dataclass
class Protocol:
    name: str
    train: np.ndarray
    test: np.ndarray
    kind: str  # "multiclass" | "multilabel"


def _folds_of_three(combos: list[str]) -> list[list[str]]:
    """Split the compound combinations into three disjoint held-out groups."""
    return [combos[i::3] for i in range(3)]


def iter_protocols(idx: WindowIndex, meta: pd.DataFrame, win: int,
                   n_per_run: dict[int, int], which: list[str] | None = None,
                   max_condition_folds: int | None = None
                   ) -> Iterator[Protocol]:
    wanted = set(which or ALL_PROTOCOLS)
    conditions = sorted(pd.unique(idx.condition))
    if max_condition_folds is not None:
        conditions = conditions[:max_condition_folds]
    is_comp = meta["is_compound"].to_numpy().astype(bool)
    run_fault = meta["fault_full"].to_numpy()
    run_profile = meta["profile"].to_numpy()

    if "leaky_random" in wanted:
        tr, te = sp.leaky_random_split(idx)
        yield Protocol("leaky_random", tr, te, "multiclass")

    if "in_condition" in wanted:
        tr, te = sp.in_condition_split(idx, n_per_run, win)
        yield Protocol("in_condition", tr, te, "multiclass")

    if "unknown_condition" in wanted:
        for c in conditions:
            tr, te = sp.unknown_condition_split(idx, c)
            if tr.any() and te.any():
                yield Protocol(f"unknown_condition[{c}]", tr, te, "multiclass")

    if "cross_profile" in wanted:
        for train_prof in ("torque_circulation", "speed_circulation"):
            tr, te = sp.cross_profile_split(idx, run_profile, train_prof)
            if tr.any() and te.any():
                yield Protocol(f"cross_profile[train={train_prof}]", tr, te,
                               "multiclass")

    if "single_source" in wanted:
        for c in conditions:
            tr, te = sp.single_source_condition_split(idx, c)
            if tr.any() and te.any():
                yield Protocol(f"single_source[{c}]", tr, te, "multiclass")

    if "steady_to_transitional" in wanted:
        tr, te = sp.steady_to_transitional_split(idx)
        if tr.any() and te.any():
            yield Protocol("steady_to_transitional", tr, te, "multiclass")

    if "compositional_control" in wanted:
        tr, te = sp.compositional_control_split(idx, is_comp, n_per_run, win)
        if tr.any() and te.any():
            yield Protocol("compositional_control", tr, te, "multilabel")

    if "leave_combination_out" in wanted:
        for fi, held in enumerate(_folds_of_three(
                sp.compound_combinations(meta))):
            tr, te = sp.leave_combination_out_split(idx, run_fault, held)
            if tr.any() and te.any():
                yield Protocol(f"leave_combination_out[fold{fi}]", tr, te,
                               "multilabel")

    if "compositional_zeroshot" in wanted:
        tr, te = sp.compositional_split(idx, is_comp)
        if tr.any() and te.any():
            yield Protocol("compositional_zeroshot", tr, te, "multilabel")


def group_name(protocol_name: str) -> str:
    """Strip the fold suffix: ``unknown_condition[...]`` -> ``unknown_condition``."""
    return protocol_name.split("[")[0]
