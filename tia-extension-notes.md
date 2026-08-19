# TIA Extension — the two-regime result

Triggered by Arumugam, Hamiti & Gerada, "Modeling of Different Winding Configurations
for Fault-Tolerant Permanent Magnet Machines to Restrain Interturn Short-Circuit
Current," IEEE Trans. Energy Convers., 27(2), pp. 351-361, June 2012.

## 1. The paper

Analytical slot-permeance model for Ls, Lh, Lm of shorted vs healthy turns in a
12s/14p FT-PMSM (65 turns/coil). Two arrangements: horizontal (turns stacked
radially) and a proposed vertical (turns side by side across the slot width).
Verified vs FEM, validated on a purpose-built stator section with an RLC meter.

Result: for horizontal and stranded windings the SC current after remedial action is
strongly position dependent, exceeding 4x rated for a single turn near the slot
opening. The vertical arrangement nearly removes that dependence.

Limitations: infinite-permeability analytical model (runs high vs FEM); straight
flux paths assumed (their Figs 7/9 show otherwise); prototype is SOLID low-carbon
steel, mu_r ~ 200, so measured magnitudes are not representative of a laminated
machine (they re-ran FEM at mu_r = 200 to match). AC/proximity loss of the vertical
arrangement is not addressed.

## 2. Apparent conflict with the EPEi paper

Both tooth-coil concentrated windings. EPEi paper: position changes Lf by +15/-8 %.
Arumugam: position changes SC current by >4x. Different quantities.

EPEi Lf = fault loop inductance with the healthy portion current-controlled.
Arumugam = SC current after the phase terminals are shorted. Their (21) in the
inductance-limited limit collapses to

    Is ~ e2 / (j w Lsc),     Lsc = Ls - Lm^2/Lh = Ls (1 - k^2)

The common tooth-flux term cancels identically in Lsc.

## 3. The exact result (the TIA spine)

Substituting the turn-ratio model Ls = s^2 Lcoil, Lh = (1-s)^2 Lcoil,
Lm = s(1-s) Lcoil:

    Ls*Lh - Lm^2 = s^2(1-s)^2 Lcoil^2 - s^2(1-s)^2 Lcoil^2 == 0

**The turn-count assumption is a perfect-coupling assumption: k == 1, Lsc == 0,
unbounded fault current.** Exact, general, no FEA required.

The EPEi paper measured the deviation: k = 0.963, so 1 - k^2 = 0.073. That 7 %
residual IS the fault-tolerant design quantity, and it is precisely what the
turn-count model discards. "Common term dominates Lf" and "coupling is near unity"
are the same statement, with opposite consequences in the two regimes.

## 4. What was NOT established (recorded honestly)

Initial expectation was that position dependence would blow up in the FT regime.
It does not, in a matrix calibrated to the published per-turn selfs (0.81 / 0.64 uH,
giving Lcoil = 434.7 uH vs the ~438 uH implied by the published Lf values):

    r    Lf/turn-count (bottom/opening)    Lsc [uH] (bottom/opening)   spread
    1        1.165 / 0.920                    0.0591 / 0.0551          1.1x
    3        1.150 / 0.926                    0.5265 / 0.4855          1.1x
    6        1.129 / 0.936                    2.1079 / 1.9165          1.1x
    10       1.102 / 0.949                    5.8762 / 5.2455          1.1x

Same direction as Arumugam (Lsc smallest at the opening -> largest current) but not
the magnitude. **Run `sc_inductance()` on the real 25x25 FE matrix before claiming
anything about magnitude.** Why Arumugam's machine is sensitive and this one may not
be (FT design at ~1 pu inductance, 65 turns, different slot aspect ratio) is an open
question -- and becomes contribution C3 rather than a loose end.

## 5. Proposed TIA paper

**"When Does the Turn-Count Severity Assumption Fail? Turn-Level Treatment of
Interturn Faults for Diagnosis and Fault-Tolerant Design"**

- **C1** Regime split, analytically: turn-count benign for Lf (the EPEi +15/-8 %
  bound), degenerate for Lsc (identically zero). General, exact.
- **C2** One turn matrix serves both regimes; arbitrary winding arrangements
  (horizontal, vertical, stranded, interleaved) are permutations of the connection
  matrix C, so Arumugam's comparison is reproduced and generalized from one solve.
- **C3** Design map: sweep slot aspect ratio, turns per coil, pu inductance,
  tooth-coil vs distributed -> which machines are position sensitive. Resolves the
  Arumugam-vs-benchmark gap.
- **C4** Experiment: purpose-wound coil with turn taps on an RLC meter (Arumugam's
  own route). No fault current, no drive, **no L_wire in the loop** -- this is what
  defeated the measurement in the EPEi paper (effect = 0.38 x Lwire). Achievable on
  a LUT stator section.
- **C5 (optional, possibly a separate paper)** AC/proximity loss penalty of the
  vertical winding -- their gap, and adjacent to the TEC 2024/2025 loss work.

Continuous with IECON 2021 (dual three-phase FT control). Stays non-adversarial to
the Brno group while engaging the Nottingham line directly.

## 6. Camera-ready action for the EPEi paper

Arumugam et al. 2012 is NOT cited. It is the closest prior work and Sec. VI discusses
the unsettled comparison with Wu [8] without it. Add, with:

> Arumugam et al. [x] report strong position dependence of the short-circuit current
> in a tooth-coil fault-tolerant PMSM. That is not in conflict with the present
> result: under terminal-short remedial action the current is governed by
> Ls - Lm^2/Lh, in which the common term cancels identically, so the leakage
> differential that is diluted in Lf is isolated there.

Also outstanding at camera-ready: ref [14] author list is corrupted (Pyrhonen twice);
the mandatory generative-AI disclosure section; n_p undefined in (6).
