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

Share of fault recordings in which each signal group carries the strongest signature (each group
represented by its best reliable feature: `I2_I1` for stator current; `V2_V1` (PMSG) / `PId_2fe` (SCIG) for
dq / control; `Vdc_std` (PMSG) / `Spd_std` (SCIG) for mechanical):

| | stator current | dq / control | mechanical |
|---|---|---|---|
| PMSG, inter-turn | 16 % | **75 %** | 9 % |
| PMSG, inter-winding | 7 % | **90 %** | 3 % |
| SCIG, inter-turn | 33 % | **62 %** | 5 % |
| SCIG, inter-winding | 33 % | **67 %** | 0 % |

- **PMSG**: the current controller suppresses the current asymmetry; the fault shows up as **negative-sequence
  terminal voltage** (`V2_V1`, median SDR 3.0 inter-turn / 62 inter-winding), 2fe ripple in the q-axis voltage
  and PI action. Stator-current negative sequence is weak for inter-turn faults (SDR 1.5).
- **SCIG**: the fault shows up as **2fe ripple on the d-axis (magnetising) current and its PI action**
  (`Id_2fe`, `PId_2fe`: SDR 6.7 / 74) and much more strongly in `I2_I1` (4.5 / 56) — the current side is
  informative, not just the voltage side.
- The two topologies weight the features almost orthogonally: cosine similarity of the two logistic
  detectors' weight vectors = **0.04**; `PIq_2fe` even has opposite signs.

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
| raw physical units (GBDT) | 0.88 | 0.84 | 0.71 | 0.60 |
| z-scored on target's healthy recordings (GBDT) | 0.88 | 0.84 | 0.84 | 0.78 |
| \|z\| against each recording's own pre-fault segment (GBDT) | 0.97 | 0.99 | 0.99 | 0.95 |

- Absolute-feature detectors do not transfer (AUC collapses to 0.60–0.71).
- Calibrating the feature scale on the *target* machine's healthy data — a few healthy recordings, no fault
  data — recovers most of it (0.78–0.84).
- Expressing every feature as a deviation from the recording's own reference makes the detector essentially
  topology-agnostic (0.95–0.99; TPR at 1 % FPR 0.76–0.92).

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

## 7. Monitoring architecture: what each sensor suite buys, per topology

`scripts/sensor_suites.py`, table `results/tables/F_sensor_suites.csv`, figure `F_sensor_suites.png`,
all numbers in `results/summary_suites.md`. Five suites ordered by added hardware / integration; each
feature is assigned to the cheapest suite whose measurements can compute it (dq-frame quantities need the
drive's angle, so they count as drive access; `Vd/Vq` come from *measured* terminal voltages, `Vd_conv/Vq_conv`
are the converter's own commands). One fixed feature per suite (best median SDR); the per-recording best
feature is the upper bound in brackets.

Minimum detectable extent (winding fraction between taps; smallest tested level is 2.3 % inter-winding,
2.7 % inter-turn) and share of fault recordings detectable:

| suite | PMSG inter-turn | SCIG inter-turn | PMSG inter-winding | SCIG inter-winding |
|---|---|---|---|---|
| drive-internal (no added sensors) | 7.4 % · 64 % [87 %] `D2_D1` | 2.7 % · 78 % [96 %] `PId_2fe` | 2.3 % · 90 % [100 %] `D2_D1` | 2.3 % · 100 % `PId_2fe` |
| 3 CT | 7.4 % · 57 % [78 %] `I2_I1` | 2.8 % · 75 % [84 %] `I2_I1` | 9.7 % · 82 % [94 %] `I2_I1` | 2.3 % · 100 % `I2_I1` |
| 3 CT + 3 VT | **2.8 % · 76 % [88 %]** `V2_V1` | 2.8 % · 75 % [88 %] `I2_I1` | **2.3 % · 94 % [97 %]** `V2_V1` | 2.3 % · 100 % |
| 3 CT + 3 VT + drive | 2.8 % · 76 % [95 %] | 2.7 % · 78 % [99 %] `PId_2fe` | 2.3 % · 94 % [100 %] | 2.3 % · 100 % |
| + torque transducer | no change | no change | no change | no change |

What this says about the design decision:

- **PMSG: the terminal-voltage transducers are the decisive hardware.** Current-only monitoring (classic
  MCSA) resolves inter-turn faults only from 7.4 % and inter-winding from 9.7 %; adding three voltage
  transducers takes both to the floor of the test matrix. The drive's own commanded voltage is *not* a
  substitute — the duty-cycle negative sequence detects inter-turn faults only from 7.4 %, and the commanded
  q-axis 2fe component (`Vqconv_2fe`) is excluded for firing on healthy recordings — so the signature sits in
  the measured terminal voltage, i.e. in the difference between what the converter commands and what the
  machine produces.
- **SCIG: the cheapest architecture already suffices.** Three current transducers, or the drive's own
  d-axis PI action with no added sensor, reach the smallest tested extent for both fault types; extra
  hardware buys robustness (share detectable 75–78 % → 99 % upper bound), not reach.
- **A torque transducer adds nothing for winding faults in either topology** (shaft-torque SDR 0.03–0.3):
  the mechanical route does not see stator winding faults at these extents.
- **Transferability by suite** (GBDT, cross-topology AUC on the monitored machine): with features referenced
  to each recording's own pre-fault segment every suite transfers (0.93–0.99, currents-only included); with
  features merely scaled on the target's healthy recordings, currents-only transfers worst (0.68–0.71) and
  voltage transducers or drive access lift it to 0.72–0.85.

Design-method reading: the same monitoring specification ("three CTs, current-signature analysis") yields a
2.8 % minimum detectable inter-turn extent on one topology and 7.4 % on the other; the sensor suite has to
be chosen *with* the topology, and the choice is driven by where the control loop pushes the asymmetry
(voltage side for the PMSG, magnetising-axis current for the SCIG). Same caveat as before: one machine per
topology; the SCIG's narrower drift band is partly a sensing-chain effect.

## Next steps

1. ~~Sensor-suite question~~ — done (Section 7).
2. Onset detection: the relay pickup delay (≈ 85–90 ms) and the 1 s pre-fault give a clean onset benchmark;
   the onset-aware approach from the cobot paper applies directly.
3. Tier 2: harmonise the variable-speed wound-field SG (bench C) to 977 Hz / 260 ms and re-run the SDR
   pipeline — it has fault impedance and repetition IDs the 3-phase sets lack.
4. FEA populations: simulate the 24 tap pairs on PMSG and SCIG models under parameter variation to get the
   distribution behind each diamond in figure C.
