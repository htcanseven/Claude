# Measured baselines on MCC5-THU Motor, and what they imply for the paper

Dataset: MCC5-THU multi-mode motor fault diagnosis
(Chen et al., *Data in Brief* 65 (2026) 112583; DOI 10.17632/6s3dggj9mw.1;
CC BY 4.0). Baseline: random forest (300 trees) on 108 handcrafted time- and
frequency-domain features, 0.64 s windows (8192 samples at 12.8 kHz),
non-overlapping, three vibration and three current channels.
40,320 windows over 288 runs. Single seed unless noted.

## 1. Protocol choice dominates the headline number

| Protocol | What is held out | Accuracy |
|---|---|---|
| `leaky_random` | nothing (random windows) | **0.975** |
| `in_condition` | last 30 % of each run, guard gap | 0.965 |
| `unknown_condition` | one of 12 operating conditions (12 folds) | 0.939 ± 0.024 |
| `cross_profile` | the other excitation profile (2 folds) | 0.839 ± 0.147 |
| `steady_to_transitional` | speed/load ramps | 0.767 |
| `single_source` | 11 conditions, training on 1 (12 folds) | **0.333 ± 0.106** |
| `compositional_zeroshot` | all compound faults (exact match) | **0.000** |

The same features and model span 0.975 to 0.000 across protocols. Any claim
about this dataset is therefore a claim about its protocol, which is the first
thing the paper should establish.

## 2. "Unseen operating condition" is nearly free — as usually benchmarked

Leave-one-condition-out costs only ~2.6 points (0.965 → 0.939). Training on 11
of 12 conditions brackets the held-out one (1000 and 3000 rpm surround a
held-out 2000 rpm), so the model interpolates.

Reversing it changes everything: training on **one** condition and testing on
the other eleven drops to **0.333**, a 63-point collapse. That is the
industrially realistic direction — commissioning yields data at one operating
point — and it is where condition-invariance work should be measured. Framing a
paper's contribution on leave-one-condition-out would be arguing against a
straw man.

## 3. Training-time excitation diversity matters more than quantity

`cross_profile` is strongly asymmetric, on equal training-set sizes (144 runs
each):

| Train | Test | Accuracy |
|---|---|---|
| `speed_circulation` (constant load, varying speed) | `torque_circulation` | **0.943** |
| `torque_circulation` (constant speed, varying load) | `speed_circulation` | **0.735** |

A model trained where speed varies transfers to load variation; the reverse
loses 21 points. Speed variation appears to be the harder invariance, and it
must be present in training to be learned — a concrete, actionable finding for
practitioners, and an argument for order-domain (speed-invariant) features.

## 4. Compound faults: a real failure, but the metrics needed a floor

> **Correction (added after the first pass).** The compound results in this
> section were originally reported without a trivial-baseline reference, and that
> omission changed their meaning. On the zero-shot compound test set a constant
> predictor that ignores the input and always emits the two bearing constituents
> scores **exact 0.111, micro-F1 0.556, at-least-one-found 1.000**, which beats
> every model trained here — by 3.6× on micro-F1 and 14× on exact match:
>
> | Model | exact | micro-F1 | ≥1 found |
> |---|---|---|---|
> | **constant `{bearing_inner_h, bearing_outer_h}`** | **0.111** | **0.556** | **1.000** |
> | constant `{bearing_inner_h}` | 0.000 | 0.370 | 0.556 |
> | shared vibration + current features | 0.000 | 0.061 | 0.068 |
> | vibration only | 0.000 | 0.093 | 0.117 |
> | current only | 0.000 | 0.086 | 0.095 |
> | late fusion by union | 0.008 | 0.156 | 0.203 |
>
> The cause is structural: every compound in this dataset pairs one bearing
> constituent with one other mechanism, and inner- and outer-race each appear in
> 60 of the 108 compound runs, so the constant predictor gets that prior for free
> while a model trained on single-fault windows (exactly one positive of fifteen)
> emits at most one positive.
>
> What this means for the claims below. The *measurements* stand — the control
> contrast, the per-component pattern, the modality dissociation — but two
> framings do not. "Categorical failure" described something real while
> attributing it to composition alone, when miscalibration against the label prior
> is a large part of it. And late fusion is **not** a solution: it improves a
> badly calibrated model toward, but still far below, trivial. Reproduce with
> `scripts/trivial_baselines.py`.



Trained on the 180 single-fault runs, tested zero-shot on the 108 compound-fault
runs, predicting fault *components* (multi-label, 15 components):

- exact match **0.000**
- micro-F1 0.072
- at least one of the two true components found on only **8.0 %** of windows
- **76.0 % of windows receive an all-zero prediction** — the model declares the
  machine healthy on a doubly-faulted motor
- Hamming accuracy 0.861 — which is why Hamming must not be reported alone:
  most components are absent, so all-zeros already scores high

Per-component F1 on the compound test set shows *which* faults are lost:

| Component | Test support | F1 |
|---|---|---|
| `bearing_inner_h` | 8400 | 0.168 |
| `bearing_outer_h` | 8400 | 0.091 |
| `winding_h` | 3360 | 0.002 |
| `broken_bar` | 3360 | **0.000** |
| `dynamic_eccentricity` | 3360 | **0.000** |
| `static_eccentricity_h` | 3360 | **0.000** |

When a bearing defect co-occurs with an electrical or eccentricity fault, the
non-bearing fault is lost entirely. This is the paper's strongest motivating
result: it is not a small accuracy gap, it is a categorical failure of a
standard pipeline on the exact case the dataset was built to expose.

### The mechanism: feature-space dominance, not absent signal

Three predictions were tested (`scripts/analyze_compound.py`). One failed; the
other two identify the cause.

**Failed — masking is not specific to cross-modal pairs.** We expected the one
mechanical-only compound (`bearing_outer_h_and_inner_h`) to fare better than the
eight mechanical–electrical ones. It did not: its micro-F1 of 0.018 is among the
lowest, and within it one bearing fault still suppresses the other (inner-race
detected on 2.7 % of windows, outer-race on 0.0 %). Masking is general to the
weaker constituent rather than a property of crossing modalities. Only one such
compound exists, so this is weak evidence either way, but it does not support the
hypothesis.

**Confirmed — the electrical constituent is the one that dies.** Across the eight
cross-modal compounds, mean detection rate is 0.0002 for the electrical
constituent (max 0.0018) against 0.072 for the mechanical one (max 0.239).

**Confirmed, and decisive — each modality sees only its own family, and sharing a
feature space destroys one of them.**

| Feature view | electrical constituent | mechanical constituent |
|---|---|---|
| vibration only | **0.000** | 0.100 (max 0.356) |
| current only | **0.108** (max 0.393) | 0.000 |
| both concatenated | **0.0002** | 0.072 |

The dissociation is perfect: vibration features never detect an electrical fault,
current features never detect a mechanical one. The third row is the finding —
`winding_h` is detected on **39.3 %** of windows from current features alone and
on **0.2 %** once vibration features are concatenated, a roughly 200-fold
collapse. The electrical evidence is present and learnable; the mechanical
features win the split criterion and it is discarded.

The failure is therefore **feature-space dominance**, not a missing signature.
That also explains why gated fusion failed (§8): a learned gate still funnels both
families through one embedding, which is the problem rather than the fix.

### The prescription, and that it works

If sharing the feature space is what destroys the weaker family, do not share it:
train one multi-label model per modality and union their positive predictions, so
each competes only against faults visible in its own channels
(`scripts/late_fusion.py`, zero-shot compound protocol):

| Model | Exact match | micro-F1 | ≥1 found | all-zero |
|---|---|---|---|---|
| shared (both) | 0.0000 | 0.072 | 0.080 | 0.760 |
| vibration only | 0.0000 | 0.090 | 0.111 | 0.559 |
| current only | 0.0000 | 0.087 | 0.096 | 0.794 |
| **late fusion (union)** | **0.0078** | **0.155** | **0.200** | **0.415** |

Exact match moves off zero, micro-F1 doubles, and the all-zero rate nearly halves —
consistently, across three seeds, and derived from the diagnosis rather than found
by search, unlike the architecture sweep in §8.

**But it clears none of the bars that matter.** At micro-F1 0.155 it remains 3.6×
below the constant predictor's 0.556 (see the correction at the head of this
section), and far below the 0.63 that a properly constructed constituent-level
pipeline reaches on comparable protocols. Late fusion is therefore a diagnostic
result — evidence that a shared feature space is actively harmful — and not a
method. The right conclusion is that the remedy has to be built in from the start,
by giving each mechanism its own feature family and calibrating its own threshold,
rather than repaired afterwards by unioning two miscalibrated models.

Superposition augmentation (§8) and late fusion address different halves of the
problem: the first teaches the model to emit two positives at all, the second
stops one modality from suppressing the other. Neither addresses the label-prior
miscalibration that the trivial baseline exposes, which is why both remain below
it.

### The control settles the interpretation

A low zero-shot score could simply mean the multi-label setup never learned
anything. It did learn. Same features, same model, same 180 single-fault runs
for training — tested on held-out *single*-fault windows instead of compound
ones:

| Test set | Exact match | micro-F1 | ≥1 component found | all-zero predictions |
|---|---|---|---|---|
| held-out single faults (`compositional_control`) | **0.900** | 0.936 | 0.901 | 0.075 |
| unseen compound faults (`compositional_zeroshot`) | **0.000** | 0.072 | 0.080 | 0.760 |

A 90-point gap between recognizing a fault and recognizing that same fault in
combination with another. The component detectors are individually competent and
collectively unable to compose, which is precisely the gap a compositional
method should close.

## 5. The physics layer is validated, and the tachometer makes it possible

The key-phase channel is a 1 pulse-per-revolution tachometer: recovered speeds
of 991 / 1989 / 2999 rpm against the 1000 / 2000 / 3000 rpm labels (<1 % error),
giving exact shaft angle for computed order tracking.

Envelope demodulation before order tracking is necessary, not cosmetic. On the
raw order spectrum, bearing band energies do not separate fault from healthy
(healthy BPFO 0.0143 vs outer-race 0.0119 — the wrong way round). After
band-pass demodulation of the 1–5 kHz resonance:

| Run (constant 3000 rpm) | BPFO | BPFI | BSF |
|---|---|---|---|
| healthy | 0.039 | 0.027 | 0.017 |
| outer-race defect | **0.094** | 0.016 | 0.067 |
| inner-race defect | 0.102 | **0.065** | 0.026 |
| ball defect | 0.020 | 0.046 | 0.015 |

Outer- and inner-race defects each raise their own characteristic order ~2.4×
over healthy. Ball defects do not raise BSF — consistent with rolling-element
defects being the hardest class to detect, and reported rather than hidden.

## 6. Dataset observations worth reporting

- **288 runs, not 282.** The Hugging Face release holds 144 runs per profile;
  the paper documents 282. The extra runs include later re-acquisitions.
- **One inconsistent cell.** `bearing_outer_h` has two runs at
  `speed_circulation_20Nm_3000rpm` while `bearing_inner_h` has none. The extra
  outer-race file is stamped 2025-08-21, six weeks after its siblings
  (2025-07-04 to 07-07), and sits exactly in the missing inner-race slot. Which
  label is correct cannot be settled from the data, so it is reported, not
  silently relabelled; it does skew that leave-one-condition-out fold.
- **Compound component naming is abbreviated.** In
  `bearing_outer_H_and_inner_H` the second part omits its family, and parsing it
  literally invents a component with no single-fault training support, which
  would make zero-shot exact match unachievable for those 12 runs.
- **Channel units are raw voltages** requiring the published sensitivities.
  Applying the stated 100 mV/Nm to the torque channel yields ~2.4 Nm for runs
  labelled 20 Nm, so the torque channel's scaling does not reconcile with the
  set-point labels; the label should be read as a commanded set-point.
  Per-channel standardization sidesteps this for learning, but anyone reporting
  physical torque should be aware.

## What this means for the paper

The contribution should target the two collapses, since they are large,
reproducible, and industrially meaningful:

1. **Zero-shot compound-fault recognition** (0.000 exact match) — via
   multi-label composition over single-fault components, with vibration/current
   fusion so an electrical fault is not masked by a co-occurring bearing defect.
2. **Single-source condition extrapolation** (0.333) — via speed-invariant
   order-domain features and adversarial condition-invariance.

Both are measured here, so the paper's introduction can state the gap it closes
in numbers rather than in adjectives. The `leaky_random` row also lets the paper
quantify how much the common protocol inflates results (+1.0 point over a
guard-gap split, and far more against the honest generalization protocols),
which is a contribution in itself.
