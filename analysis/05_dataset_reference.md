# Verified facts about the source dataset (reference [11])

Everything below was checked against the published data report and the Mendeley record.
Several reviewer questions can be answered directly from these facts **with no new
experiments**. Items marked **[GAP]** are things the source does *not* provide, which
matters for the revision.

Source:
- Krüger, Nascimento, Antunes, Batistela, Sadowski, Freitas, "Stray magnetic field data of a
  synchronous generator with a faulty rotor winding – data report," *Frontiers in Energy
  Research*, 2026. <https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2026.1589769/full>
- Mendeley Data, DOI `10.17632/d75sb25f7m.1`, **CC BY 4.0**. <https://data.mendeley.com/datasets/d75sb25f7m/1>
- Measurements by GRUCAD at LABMAQ, Electrical Engineering Dept., UFSC, Florianópolis, Brazil.

---

## 1. Test bench: three machines, not two (answers R2-6)

| Item | Machine | Role |
|---|---|---|
| 1 | DC motor, 10 kW, 700–4000 rpm | Prime mover |
| 2 | **8-pole salient-pole SG, 10 kVA, 750/900 rpm** | **Machine under test — the only one used in this paper** |
| 3 | 2-pole cylindrical SG, 10 kVA, 3000/3600 rpm | Second machine on the shared bench; **not used in this study** |
| 4 | Electromagnetic clutch | Couples the DC motor to the generator line |

R2 asked "In Fig. 1 there are 2 generators. Why?" — the bench hosts two different SGs
(salient-pole and cylindrical) driven by a common prime mover through a clutch. Only the
8-pole salient-pole unit is used here. This needs one sentence in the caption and one in
the text. Consider also de-emphasising (greying/cropping) the unused machine in Fig. 1.

## 2. Rotor winding taps (answers R2-4, first half)

Field winding: **470 turns per pole, 8 poles → 3760 total rotor turns.**
Automatic switching between terminals on **one pole**, without shutting the generator down:

| Terminal | Turns short-circuited | Paper's label | Fraction of that pole | **Fraction of total rotor winding** |
|---|---|---|---|---|
| J  | 0   | Healthy | 0 %   | 0 %    |
| J1 | 94  | 20 %    | 20 %  | **2.5 %** |
| J2 | 235 | 50 %    | 50 %  | 6.25 % |
| J3 | 470 | 100 %   | 100 % | 12.5 % |

The data report describes direct short-circuit connections at the coil junctions; **no
fault resistance is specified**. The 2.5 % column is the honest way to answer R2-7 about
"incipient" faults — see `01_comment_triage.md`.

## 3. Sensors (answers R1-6 context, R2-4 second half)

Two identical induction search coils, CH1 and CH2, **90° apart mechanically** on the
generator casing, measuring the **tangential** component of the external field:

- 750 turns, AWG 39
- Cross-section 7.65 cm², height 1.13 cm
- Resistance ≈ 111 Ω, inductance ≈ 20.4 mH

The data report **contains a photograph of the sensor and its mounting** (its Figure 2,
showing the coil in its holder on the generator exterior, positioned relative to the
terminal box). Because the dataset is **CC BY 4.0**, this photograph can be reproduced
with attribution — this answers R2's request for sensor photos without needing new
hardware access. Contacting the authors (R2-5) is still worth doing, and is good practice.

## 4. Operating points (answers R3-4)

Seven operating points, **all at 7.0 kVA apparent power**:

| OP | Power factor | Excitation |
|---|---|---|
| P15 | 1.0 | Unity |
| P16 | 0.8 | Under-excited (leading) |
| P17 | 0.5 | Under-excited |
| P18 | 0.3 | Under-excited |
| P19 | 0.8 | Over-excited (lagging) |
| P20 | 0.5 | Over-excited |
| P21 | 0.3 | Over-excited |

**The published dataset contains only P15–P21.** The data report gives **no explanation for
why the numbering starts at 15**; P1–P14 are not described or released. So the correct
answer to R3-4 is: the labels are inherited verbatim from the source dataset to preserve
traceability, the released subset is P15–P21, and no other regimes are publicly available.
Do not invent a rationale. Confirm with the dataset authors when you contact them (R2-5).

Generator is **grid-connected**: "the generator was synchronized with the local 60 Hz
distribution network." Stator terminal voltage is therefore **imposed by the grid**, not
regulated to be perfectly balanced and sinusoidal — this is the direct answer to R2-8's
second half, and it should be stated plainly (grid background distortion and unbalance are
present, which is realistic but uncharacterised in the current manuscript).

## 5. **[GAP]** Field current per operating point — critical

The data report's machine-characteristics table lists **field voltage 220 V and field
current 3.5 A as *nameplate ratings*** of the salient-pole generator. The operating-point
table lists **only apparent power and power factor** for P15–P21. Likewise, armature
380 V / 15.2 A are **nameplate values** (10 kVA / (√3 × 380 V) = 15.19 A), not per-point
measurements; at 7.0 kVA the armature current would be ≈ 10.6 A.

**Consequence: there is no published per-operating-point excitation current.**

This is the single most damaging gap, because the paper's central physical argument —
Eq. (4), `V(kf_m) ≈ γ·K_k·I_f`, and the claim that P18 fails *because* `I_f` is low — is
built entirely on `I_f` varying across operating points. That variation is never measured,
reported, or verified anywhere in the manuscript. See `02_root_cause.md`, Problem 2.

## 6. File inventory (answers R1-7, and confirms the paper's n = 607)

Each file = 10 s of two-channel data at **125 kHz** (so 1.25 M samples per channel per
file), CSV with columns `Time, CH1, CH2`, named `VoltageVectorXX.csv` in folders P15–P21.
Full dataset ≈ 21.3 GB.

| OP | Files |
|---|---|
| P15 | 95 |
| P16 | 84 |
| P17 | 80 |
| P18 | 90 |
| P19 | 90 |
| P20 | 84 |
| P21 | 84 |
| **Total** | **607** |

This sums **exactly** to the 607 unique voltage-vector files used in the paper — good, it
confirms the whole released dataset is used and nothing was silently dropped. **Say this
explicitly in the revision**; it costs one sentence and removes a reproducibility doubt.

The data report's Table 5 maps voltage-vector numbers to fault condition per operating
point (e.g. **P15: vectors 1–20 healthy, 21–47 at 20 %, 48–77 at 50 %, 78–95 at 100 %**).
Reproduce the complete version of this as a per-OP × per-class count table in the
revision — a single table that answers a large part of R1-7 and the editor's
reproducibility objection.

Note the class imbalance this implies (for P15: 20/27/30/18). Combined with LOOPO, the
train/test split sizes are fully determined and should be tabulated — e.g. holding out P18
leaves 517 training files.

## 7. Related contemporary work worth citing (helps with R1-1, R2-1)

Rozhon, Bosson, Janous, Sevcik, Peroutka, "Severity Classification of Rotor Inter-Turn
Short Circuits Using Eddy-Current Vibration Signals," IEEE ISIE 2026
(arXiv:2607.03051) — rotor ITSC **severity** classification, but via eddy-current
*vibration* sensing, XGBoost on an 18-feature hybrid set, leave-one-out CV. Reports
**90.56 % accuracy, 87 % recall on mild faults**.

Two uses for this reference:
1. It is a genuinely different sensing modality on the same fault, so it supports rather
   than scoops your contribution — cite it to show awareness of current work.
2. Its **90.6 %** on a comparable severity task, versus your 99.5 %, is external evidence
   for the saturation argument in `02_root_cause.md`: when the task retains realistic
   difficulty, methods land near 90 %, not 99.5 %.
