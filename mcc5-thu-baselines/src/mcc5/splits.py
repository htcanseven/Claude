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


def leaky_random_split(idx: WindowIndex, test_frac: float = 0.3,
                       seed: int = 0):
    """Random window-level split — deliberately leaky, reported for contrast.

    Windows from the same recording land on both sides of the split, so
    neighbouring windows sharing an operating point and a machine state act as
    near-duplicates. This is a common protocol in the literature and it is what
    produces near-ceiling accuracies; including it lets the inflation over a
    guard-gap split be measured rather than assumed. Never use it as the
    headline result.
    """
    rng = np.random.default_rng(seed)
    n = len(idx.run)
    test = np.zeros(n, dtype=bool)
    test[rng.choice(n, size=int(n * test_frac), replace=False)] = True
    return ~test, test


def unknown_condition_split(idx: WindowIndex, held_out_condition: str):
    test_mask = idx.condition == held_out_condition
    train_mask = ~test_mask
    return train_mask, test_mask


def single_source_condition_split(idx: WindowIndex, source_condition: str):
    """Train on ONE operating condition, test on all the others.

    The complement of leave-one-condition-out, and the harder, more realistic
    direction: leaving one condition out still lets a model interpolate from
    the eleven it trained on (1000 and 3000 rpm bracket a held-out 2000 rpm),
    whereas commissioning a machine gives you data at one operating point and
    demands extrapolation to the rest.
    """
    train_mask = idx.condition == source_condition
    return train_mask, ~train_mask


def cross_profile_split(idx: WindowIndex, run_profile: np.ndarray,
                        train_profile: str = "torque_circulation"):
    """Train on one excitation profile, test on the other.

    ``torque_circulation`` holds speed constant while load varies and
    ``speed_circulation`` does the reverse, so this asks whether a model
    trained on load variation alone survives speed variation (or vice versa).
    ``run_profile`` is indexed by run id.
    """
    train_mask = run_profile[idx.run] == train_profile
    return train_mask, ~train_mask


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
