"""Physics-grounded signal processing driven by the key-phase tachometer.

The key-phase channel is a 1 pulse-per-revolution tachometer (verified against
the constant-speed runs: recovered 991/1989/2999 rpm for the 1000/2000/3000 rpm
labels). That gives exact instantaneous shaft angle, which enables computed
order tracking: resampling a signal at constant angular increments turns
speed-dependent fault frequencies into speed-invariant *orders*.

Bearing fault orders for the SKF 6205 (dataset paper, Table 7) are constants in
the order domain regardless of shaft speed — which is what makes order-domain
features robust under the variable-speed profiles.
"""
from __future__ import annotations

import numpy as np

FS = 12_800.0

# Multiples of shaft rotational frequency (dataset paper, Table 7)
BEARING_ORDERS = {"BPFO": 3.585, "BPFI": 5.415, "BSF": 2.357}


MAX_RPM = 6000.0            # well above the rig's 3000 rpm ceiling
MIN_PULSE_AMPLITUDE = 0.5   # volts; pulses reach ~4 V, noise floor is ~0.01 V


def keyphase_edges(keyphase: np.ndarray, fs: float = FS,
                   min_gap: int | None = None) -> np.ndarray:
    """Rising-edge sample indices of the 1-per-rev tachometer pulse train.

    Two guards matter on real runs. A window recorded before the shaft turns
    contains only noise, and thresholding noise yields a burst of spurious
    edges a few samples apart, which would read as an absurd speed; so edges
    closer than one revolution at ``MAX_RPM`` are suppressed (debounce), and a
    channel with no genuine pulse amplitude yields no edges at all.

    Prefer calling this on a whole run rather than per window: the threshold is
    then set from the run's real pulse amplitude instead of a window's noise.
    """
    if min_gap is None:
        min_gap = max(int(fs * 60.0 / MAX_RPM), 1)
    p1, p99 = np.percentile(keyphase, [1, 99])
    if (p99 - p1) < MIN_PULSE_AMPLITUDE:
        return np.empty(0, dtype=int)  # shaft not turning / no pulse train
    thr = p1 + 0.5 * (p99 - p1)
    raw = np.flatnonzero((keyphase[:-1] < thr) & (keyphase[1:] >= thr))
    if len(raw) == 0:
        return raw
    kept = [raw[0]]
    for e in raw[1:]:
        if e - kept[-1] >= min_gap:
            kept.append(e)
    return np.asarray(kept, dtype=int)


def instantaneous_speed(keyphase: np.ndarray, fs: float = FS):
    """Shaft speed at each revolution boundary.

    Returns ``(edge_idx, rpm)`` where ``rpm[i]`` is the mean speed over the
    revolution ending at sample ``edge_idx[i]``.
    """
    edges = keyphase_edges(keyphase)
    if len(edges) < 2:
        return np.empty(0, dtype=int), np.empty(0)
    dt = np.diff(edges) / fs
    with np.errstate(divide="ignore", invalid="ignore"):
        rpm = 60.0 / dt
    ok = np.isfinite(rpm)
    return edges[1:][ok], rpm[ok]


def speed_series(keyphase: np.ndarray, fs: float = FS) -> np.ndarray:
    """Per-sample shaft speed (rpm), interpolated between revolutions."""
    idx, rpm = instantaneous_speed(keyphase, fs)
    n = len(keyphase)
    if len(idx) == 0:
        return np.zeros(n)
    return np.interp(np.arange(n), idx, rpm, left=rpm[0], right=rpm[-1])


def shaft_angle(keyphase: np.ndarray) -> np.ndarray:
    """Cumulative shaft angle in revolutions, from tachometer edges.

    Within a revolution the angle is linear in time; across revolutions it
    increments by exactly 1, so the mapping is exact at every pulse.
    """
    edges = keyphase_edges(keyphase)
    n = len(keyphase)
    if len(edges) < 2:
        return np.zeros(n)
    revs = np.arange(len(edges), dtype=float)
    return np.interp(np.arange(n), edges, revs,
                     left=revs[0], right=revs[-1])


def order_resample(sig: np.ndarray, angle: np.ndarray,
                   samples_per_rev: int = 64):
    """Computed order tracking: resample ``sig`` at constant angular steps.

    ``angle`` is cumulative shaft angle in revolutions, aligned sample-for-
    sample with ``sig`` (see :func:`shaft_angle`). Returns
    ``(resampled, n_revs)``. A spectrum of the result has axis units of
    *orders* (multiples of shaft rate), so fault peaks sit at the fixed
    BEARING_ORDERS values no matter how the speed varies.
    """
    if len(angle) == 0 or len(sig) == 0:
        return np.empty(0), 0
    a0, a1 = float(angle[0]), float(angle[-1])
    n_revs = int(np.floor(a1 - a0))
    if n_revs < 1:
        return np.empty(0), 0
    grid = a0 + np.arange(n_revs * samples_per_rev) / samples_per_rev
    # angle is monotonically non-decreasing -> np.interp is a valid inverse map
    return np.interp(grid, angle, sig), n_revs


def order_spectrum(sig: np.ndarray, angle: np.ndarray,
                   samples_per_rev: int = 64):
    """Amplitude spectrum in the order domain. Returns ``(orders, amp)``."""
    res, n_revs = order_resample(sig, angle, samples_per_rev)
    if len(res) == 0:
        return np.empty(0), np.empty(0)
    res = res - res.mean()
    amp = np.abs(np.fft.rfft(res)) / len(res)
    orders = np.fft.rfftfreq(len(res), d=1.0 / samples_per_rev)
    return orders, amp


def envelope(sig: np.ndarray, fs: float = FS,
             band: tuple[float, float] = (1000.0, 5000.0)) -> np.ndarray:
    """Squared-envelope of a resonance band (classical demodulation).

    A localized bearing defect excites a structural resonance once per
    impact, so the defect frequency appears as the *modulation* rate of a
    high-frequency carrier — it is largely absent from the raw spectrum.
    Band-pass around the resonance, then take the analytic-signal magnitude
    to recover that modulation.
    """
    from scipy.signal import butter, sosfiltfilt, hilbert

    nyq = fs / 2.0
    lo, hi = band[0] / nyq, min(band[1] / nyq, 0.99)
    sos = butter(4, [lo, hi], btype="bandpass", output="sos")
    band_sig = sosfiltfilt(sos, sig)
    env = np.abs(hilbert(band_sig))
    return env - env.mean()


def envelope_order_spectrum(sig: np.ndarray, angle: np.ndarray,
                            fs: float = FS,
                            band: tuple[float, float] = (1000.0, 5000.0),
                            samples_per_rev: int = 64):
    """Envelope order spectrum: the standard way to expose bearing orders.

    Demodulate first (so the informative signal is low-frequency), then order-
    track. Both steps matter: order tracking alone leaves the fault smeared
    across speed, and demodulation alone leaves it smeared across orders.
    """
    env = envelope(sig, fs=fs, band=band)
    return order_spectrum(env, angle, samples_per_rev=samples_per_rev)


def order_band_energy(orders: np.ndarray, amp: np.ndarray, center: float,
                      rel_width: float = 0.06) -> float:
    """Energy in a narrow band around a fault order (and its 2nd harmonic)."""
    if len(orders) == 0:
        return 0.0
    tot = 0.0
    for k in (1, 2):
        c = center * k
        lo, hi = c * (1 - rel_width), c * (1 + rel_width)
        sel = (orders >= lo) & (orders <= hi)
        if sel.any():
            tot += float((amp[sel] ** 2).sum())
    return tot
