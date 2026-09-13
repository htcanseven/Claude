# PMSG vs SCIG under identical winding short-circuits — findings of the first pass

Data: InnovaPower `PMSG-3phase-Dataset` and `SCIG-3phase-Dataset` (Tominaga et al., *Data in Brief* 2025),
225 recordings each, identical test matrix (24 tap-pair short-circuits + healthy, × 3 speeds × 3 torques),
20 kHz, 3 s, contactor closed at 1.000 s for ≈ 0.40 s. Pipeline: `scripts/features.py` →
`scripts/compare.py`; all tables and figures in `results/`; `results/summary.md` has every number.

Detectability statistic used throughout: **signal-to-drift ratio (SDR)** — |relative change of a feature
from the 0.36 s before the relay to the fault interval| divided by the 95th percentile of the |relative
change| between two adjacent no-fault intervals of the same length, pooled over all 225 recordings of that
machine. SDR ≥ 1 ⇒ the change exceeds ordinary within-recording drift at ≈ 5 % per-recording false alarm.
Features that nevertheless fired on > 1 of the 9 healthy recordings (`D2_D1`, `Ia_h3`, `Ia_h7`, `Id_1fe`,
`Iq_2fe`, `PId_std`, `Spd_std`, `Vdc_std`) are excluded from the "best feature" choices.

## 1. The same tap pair is not the same physical fault

Fault current for the same tap pair is 4–22 % lower in the SCIG (median ratio 0.91), but relative to what
the stator sensors see it is far smaller: fault current / pre-fault stator current = **1.86 (PMSG) vs 0.80
(SCIG)**, because the SCIG draws ≈ 6.3 A of magnetising current. In per-unit of rated current: 1.05 vs 0.78.
A "12 % inter-turn fault" is therefore a different diagnostic problem in the two topologies, even before any
algorithm is involved — the tap-pair label is a *design* description, not a physical severity.

## 2. The signature moves to a different place in the drive

Share of fault recordings in which each signal group carries the strongest signature:

| | stator current | dq / control | mechanical |
|---|---|---|---|
| PMSG, inter-turn | 10 % | **83 %** | 7 % |
| PMSG, inter-winding | 6 % | **94 %** | 0 % |
| SCIG, inter-turn | 28 % | **68 %** | 5 % |
| SCIG, inter-winding | 33 % | **67 %** | 0 % |

- **PMSG**: the current controller suppresses the current asymmetry; the fault shows up as **negative-sequence
  terminal voltage** (`V2_V1`, median SDR 3.0 inter-turn / 62 inter-winding), 2fe ripple in the q-axis voltage
  and PI action. Stator-current negative sequence is weak for inter-turn faults (SDR 1.5).
- **SCIG**: the fault shows up as **2fe ripple on the d-axis (magnetising) current and its PI action**
  (`Id_2fe`, `PId_2fe`: SDR 6.7 / 74) and much more strongly in `I2_I1` (4.5 / 56) — the current side is
  informative, not just the voltage side.
- The two topologies weight the features almost orthogonally: cosine similarity of the two logistic
  detectors' weight vectors = **0.06**; `PIq_2fe` even has opposite signs.

Design reading: *which measurement carries the fault is a property of topology + control structure*, so a
monitoring design fixed at the "current signature analysis" stage is topology-specific.

## 3. Minimum detectable fault extent

Smallest tap-pair severity (winding fraction between taps) at which the median SDR ≥ 1:

| feature | PMSG inter-turn | SCIG inter-turn | PMSG inter-winding | SCIG inter-winding |
|---|---|---|---|---|
| `V2_V1` | 2.8 % | 2.7 % | 2.3 % | 2.3 % |
| `Vq_2fe` | 7.4 % | 7.4 % | 2.3 % | 2.3 % |
| `I2_I1` | 7.4 % | 2.8 % | 9.7 % | 2.3 % |
| `PId_2fe` | 11.6 % | 2.7 % | 10.6 % | 2.3 % |

SDR rises monotonically with fault extent (Spearman 0.69–0.95). On this bench the SCIG is detectable at the
smallest tested extent on three of the four features; the PMSG only through the voltage negative sequence.

## 4. Operating point

Speed dominates: PMSG median best-SDR 8 → 13 → 18 from 1200 to 1800 rpm (share detectable 79–83 % at
1200 rpm vs 92–96 % above); SCIG 16 → 24 → 47 (92–100 %). Torque changes little. Consistent with the fault
EMF scaling with speed — and with the point that a "minimum speed for monitoring" is a design parameter.

## 5. Cross-topology transfer of a learned detector

Window-level detector, 5-fold GroupKFold over unseen tap pairs within a machine; cross rows train on all of
one machine and test on all of the other.

| feature calibration | within PMSG | within SCIG | PMSG → SCIG | SCIG → PMSG |
|---|---|---|---|---|
| raw physical units (GBDT) | 0.88 | 0.84 | 0.71 | 0.58 |
| z-scored on target's healthy recordings (GBDT) | 0.88 | 0.84 | 0.83 | 0.78 |
| \|z\| against each recording's own pre-fault segment (GBDT) | 0.97 | 0.99 | 0.99 | 0.94 |

- Absolute-feature detectors do not transfer (AUC collapses to 0.58–0.72).
- Calibrating the feature scale on the *target* machine's healthy data — a few healthy recordings, no fault
  data — recovers most of it (0.78–0.83).
- Expressing every feature as a deviation from the recording's own reference makes the detector essentially
  topology-agnostic (0.94–0.99; TPR at 1 % FPR 0.72–0.92).

Caveat specific to the last row: the negatives are dominated by pre-fault windows, which are ≈ 0 by
construction under self-referencing; the only hard negatives are the fault-time windows of healthy recordings
(≈ 120 per machine). The row therefore answers "does a change detector trained on one topology flag the
other's fault onsets" — yes — not "does it reject other transients", which this dataset cannot test.

## 6. What this does and does not support

Supported (as a demonstration of the method): the same design-level fault produces a different physical
severity, a different observable signature and a different minimum detectable extent in the two generator
topologies, and the transferability of a monitoring design depends on how its features are referenced.

Not supported: any general statement "SCIG faults are easier to detect than PMSG faults". One machine per
topology, no repeated tests, and the SCIG's narrower drift band (its relative no-fault variation is 3–5×
smaller, plausibly because its 2.5× larger stator current gives a better relative SNR on the same current
sensors) is a sensing-chain effect that is confounded with topology. Separating the two requires the
FEA-generated topology populations planned for the paper, with the two measured machines as validation points.

## Next steps

1. Sensor-suite question: repeat B–C with feature subsets a real installation would have (phase currents
   only; currents + voltages; controller internals) → cost vs minimum detectable extent per topology.
2. Onset detection: the relay pickup delay (≈ 85–90 ms) and the 1 s pre-fault give a clean onset benchmark;
   the onset-aware approach from the cobot paper applies directly.
3. Tier 2: harmonise the variable-speed wound-field SG (bench C) to 977 Hz / 260 ms and re-run the SDR
   pipeline — it has fault impedance and repetition IDs the 3-phase sets lack.
4. FEA populations: simulate the 24 tap pairs on PMSG and SCIG models under parameter variation to get the
   distribution behind each diamond in figure C.
