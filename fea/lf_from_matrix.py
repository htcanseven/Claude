"""
Fault-loop inductance from a turn-level inductance matrix.

Core idea: if each of the N turns of a coil is assigned as a separate winding and
Maxwell returns the N x N inductance matrix L_ij, then the fault-loop inductance of
any set S of shorted turns is the submatrix sum

    L_f(S) = sum_{i in S} sum_{j in S} L_ij

by superposition. Every severity and every position comes from ONE solve. Valid in
the linear (unsaturated) regime; saturation needs separate frozen-permeability runs.

Two entry points:
  * synthetic_slot_matrix() -- classical slot-leakage model, for method validation
    and for previewing the expected magnitude before any FEA exists.
  * load_maxwell_matrix()   -- read a matrix exported from Maxwell.
"""

import numpy as np


def synthetic_slot_matrix(n_turns=25, h_slot=1.0, mu0_L_over_w=1.0):
    """Classical rectangular-slot leakage model.

    Flux crossing the slot at height y is driven by the current below y and links the
    conductors below y. For conductors at heights x_i, x_j measured from the slot
    BOTTOM (x=0) toward the slot opening (x=h):

        M_ij = (mu0 * L_stk / w) * (h - max(x_i, x_j))

    Bottom conductors are linked by the whole cross-slot leakage flux and therefore
    carry the largest inductance; conductors at the opening carry almost none.

    Sanity check: with all N conductors carrying the same current this integrates to
    the textbook slot permeance N^2 * h / (3w).
    """
    x = (np.arange(n_turns) + 0.5) * h_slot / n_turns   # index 0 = slot bottom
    M = mu0_L_over_w * (h_slot - np.maximum.outer(x, x))
    return M


def load_maxwell_matrix(path):
    """Load an N x N inductance matrix exported from Maxwell (CSV, no header)."""
    L = np.loadtxt(path, delimiter=",")
    assert L.ndim == 2 and L.shape[0] == L.shape[1], "expected a square matrix"
    return 0.5 * (L + L.T)          # enforce symmetry, kill export round-off


def window_inductance(L, start, r):
    """L_f for r contiguous turns beginning at index `start` (0 = slot bottom)."""
    S = slice(start, start + r)
    return L[S, S].sum()


def sweep(L, severities=(3, 6, 10)):
    """L_f for every contiguous window, normalised by the whole-coil inductance,
    compared against the turn-ratio scaling (r/N)^2 that lumped models assume."""
    N = L.shape[0]
    L_coil = L.sum()
    rows = []
    for r in severities:
        ratio_model = (r / N) ** 2
        vals = np.array([window_inductance(L, s, r) / L_coil
                         for s in range(N - r + 1)])
        rows.append(dict(r=r, model=ratio_model,
                         lo=vals.min(), hi=vals.max(), mean=vals.mean(),
                         k_lo=vals.min() / ratio_model,
                         k_hi=vals.max() / ratio_model,
                         k_mean=vals.mean() / ratio_model,
                         profile=vals))
    return rows


if __name__ == "__main__":
    N = 25                                    # turns per coil segment (Brno machine)
    L = synthetic_slot_matrix(N)

    # verify against the textbook slot permeance N^2 h / 3w
    print(f"whole-coil sum      = {L.sum():.2f}   (textbook N^2h/3 = {N**2/3:.2f})\n")

    print(f"{'r':>3} {'(r/N)^2':>9} {'min':>9} {'max':>9} "
          f"{'k_min':>7} {'k_max':>7} {'spread':>7}")
    print("-" * 60)
    for row in sweep(L):
        print(f"{row['r']:>3} {row['model']:>9.4f} {row['lo']:>9.4f} {row['hi']:>9.4f} "
              f"{row['k_lo']:>7.2f} {row['k_hi']:>7.2f} "
              f"{row['k_hi']/row['k_lo']:>7.1f}x")

    print("\nk = L_f(FEA) / L_f(turn-ratio model). k=1 means the lumped model is exact.")
    print("Window index 0 = slot bottom (deepest turns), N-r = slot opening.\n")

    row = sweep(L, (3,))[0]
    print("r = 3, L_f/L_coil by window position (bottom -> opening):")
    print("  " + "  ".join(f"{v:.4f}" for v in row["profile"][::4]))


def random_wound_spread(L, r, n_draws=20000, seed=0):
    """Bound for a random-wound (mush-wound) coil.

    In an orderly coil, 'turns k..k+r' occupy contiguous slot positions. In a
    random-wound coil the winding sequence does not map to slot position, so the
    shorted turns land on an arbitrary subset. Reality sits between the two: the
    wire is laid continuously, so consecutive turns are correlated in position,
    but not perfectly ordered.

    Returns the L_f/L_coil distribution over random r-subsets.
    """
    rng = np.random.default_rng(seed)
    N = L.shape[0]
    L_coil = L.sum()
    out = np.empty(n_draws)
    for d in range(n_draws):
        S = rng.choice(N, size=r, replace=False)
        out[d] = L[np.ix_(S, S)].sum() / L_coil
    return out
