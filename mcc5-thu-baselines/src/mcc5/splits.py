"""Leakage-free evaluation protocols.

All splits operate on window *index tables* (run_id, start) so that the
split decision is made before any model sees samples.

Protocols
---------
in_condition
    Temporal split within each run: train on the first ``train_frac`` of the
    recording, test on the last ``test_frac``, with a guard gap in between so
    no window overlaps both. (A pure run-level split is impossible here: the
    dataset has one recording per fault x condition pair.)

unknown_condition
    Leave-one-condition-out: all runs of one operating-condition group form
    the test set, everything else trains.

steady_to_transitional
    Train on quasi-stationary windows, test on transitional windows
    (stationarity mask computed from torque + current channels).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class WindowIndex:
    """Flat table of candidate windows across runs."""
    run: np.ndarray      # run index into metadata frame
    start: np.ndarray    # sample offset within run
    label: np.ndarray    # encoded class id
    condition: np.ndarray  # condition group string per window
    stationary: np.ndarray | None = None


def in_condition_split(idx: WindowIndex, n_samples_per_run: dict[int, int],
                       win: int, train_frac: float = 0.6,
                       gap_frac: float = 0.1, seed: int = 0):
    train_mask = np.zeros(len(idx.run), dtype=bool)
    test_mask = np.zeros(len(idx.run), dtype=bool)
    for r in np.unique(idx.run):
        n = n_samples_per_run[int(r)]
        t_end = int(n * train_frac)
        g_end = int(n * (train_frac + gap_frac))
        sel = idx.run == r
        starts = idx.start
        train_mask |= sel & (starts + win <= t_end)
        test_mask |= sel & (starts >= g_end)
    return train_mask, test_mask


def unknown_condition_split(idx: WindowIndex, held_out_condition: str):
    test_mask = idx.condition == held_out_condition
    train_mask = ~test_mask
    return train_mask, test_mask


def steady_to_transitional_split(idx: WindowIndex):
    if idx.stationary is None:
        raise ValueError("stationarity mask not computed")
    train_mask = idx.stationary
    test_mask = ~idx.stationary
    return train_mask, test_mask


def compositional_split(idx: WindowIndex, is_compound_run: np.ndarray):
    """Train on single-fault runs, test on compound-fault runs (zero-shot).

    ``is_compound_run`` is indexed by run id. Compound faults are never seen
    during training, so a model can only succeed by composing the single-fault
    signatures it learned — the flagship generalization test for this dataset.
    """
    compound_win = is_compound_run[idx.run]
    return ~compound_win, compound_win


def component_matrix(meta, component_vocab: list[str] | None = None):
    """Multi-label component targets: (n_runs, n_components) 0/1 matrix."""
    comps = [str(c).split("+") if isinstance(c, str) and c else []
             for c in meta["components"]]
    if component_vocab is None:
        vocab = sorted({c for cs in comps for c in cs})
    else:
        vocab = component_vocab
    col = {c: i for i, c in enumerate(vocab)}
    Y = np.zeros((len(meta), len(vocab)), dtype=np.int8)
    for r, cs in enumerate(comps):
        for c in cs:
            if c in col:
                Y[r, col[c]] = 1
    return Y, vocab
