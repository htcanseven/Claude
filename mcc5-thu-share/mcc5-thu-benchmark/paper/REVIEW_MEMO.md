# Review memo — "Beyond Closed-Set Accuracy: Constituent-Level Generalization in Compound Motor Fault Diagnosis"

**To:** Evin Şahin Sadık, Hüseyin Tayyer Canseven
**Re:** technical review of the results section, and a symmetric correction to the
independent benchmark work on the same dataset
**Dataset:** MCC5-THU motor (Chen et al., *Data in Brief* 65 (2026) 112583;
DOI 10.17632/6s3dggj9mw.1, CC BY 4.0), 288 runs, 108 of them compound

Every number below was computed directly from the released data. Reproduction
commands are in the last section.

---

## 1. Summary

The draft's central claim is correct and well supported: the dominant failure in
compound diagnosis is **incomplete decomposition, not loss of diagnostic
information**. The crossed 3 × 2 protocol (recombination / one-sided /
two-sided compound-context zero-shot × seen / unseen condition), the graph
formulation of context withholding, the run-clustered bootstrap, and the Holm
correction are all stronger than the corresponding parts of the independent
benchmark work described in §6.

Two issues need addressing before submission. One is mandatory (§2): the
constituent metrics need a trivial-baseline reference, without which several
reported values are at or below what a constant predictor achieves. The other is
significant (§3): the oracle detectability analysis is confounded by acquisition
session, and its headline AUC = 0.000 result may be a session artefact.

Both issues apply symmetrically to the independent benchmark work, whose compound
results turn out to be *worse* than trivial (§6). That is offered as evidence
that this check is worth running on any compound-fault result in this literature,
not as a criticism aimed in one direction.

---

## 2. Mandatory: trivial-baseline reference for Table 2

### The structural reason

In this dataset every compound pairs exactly one bearing constituent with one
other mechanism. Constituent frequencies across the 108 compound runs:

| Constituent | Runs |
|---|---|
| `fouter` | 60 |
| `finner` | 60 |
| `fbar` | 24 |
| `fdyn` | 24 |
| `fstat` | 24 |
| `fwind` | 24 |
| `fball`, `fbend`, `fvu` | **0** |

Consequently a predictor that ignores the input entirely and always emits
`{finner, fouter}` is a strong competitor on several of the reported metrics.

### The numbers

| Predictor | EM | R_const | R_any | R_all | FA/run |
|---|---|---|---|---|---|
| constant `{finner, fouter}` | **0.1111** | 0.5556 | **1.0000** | 0.1111 | 0.8889 |
| constant `{finner, fouter, fbar}` | 0.0000 | 0.6667 | 1.0000 | **0.3333** | 1.6667 |
| constant `{finner}` | 0.0000 | 0.2778 | 0.5556 | 0.0000 | 0.4444 |
| **Table 2, range over six regimes** | 0.0833–0.1574 | 0.6296–0.6944 | 0.9259–0.9444 | 0.3241–0.4444 | 0.6389–0.7315 |

### What follows

1. **EM does not reliably exceed trivial.** Reported values straddle 0.1111:
   two-sided/seen ties it exactly (0.1111), two-sided/unseen falls below it
   (0.0833), and only the recombination regimes clearly exceed it (0.1389,
   0.1574).
2. **R_any is below trivial in all six regimes** (0.9259–0.9444 against 1.0000).
   The sentence "at least one correct constituent was recovered in more than 92 %
   of compound runs" currently reads as a positive result, but a constant output
   achieves 100 %.
3. **R_all for the four weaker regimes sits at the three-constituent constant
   baseline** (0.3241–0.3796 against 0.3333).
4. **The genuine evidence of learning is R_const and recombination R_all.**
   R_const 0.6296–0.6944 against 0.5556, and R_all 0.4167/0.4444 against 0.1111
   — the latter a four-fold margin. These should carry the argument.

**Recommendation.** Add the constant-predictor rows to Table 2 (or a companion
table) and re-anchor the narrative on R_const and R_all. The argument barely
changes and the section becomes much harder to attack: any reviewer who computes
this independently and finds it absent will discount the whole results section.

Consider also demoting R_any, which is saturated and beaten by a constant output.
It supports "partial recovery is easy" but cannot support a claim of diagnostic
skill.

---

## 3. Significant: the oracle analysis is confounded by acquisition session

### Evidence

Filenames carry a `YYMMDDHHMMSS` acquisition stamp. Every compound run was
recorded on a **different day** from the single-fault run it is compared against
in the `A + B` vs `B` oracle analysis — unavoidably, since creating a compound
fault requires disassembling and reassembling the machine:

| Table 3 comparison | Compound recorded | Single-`B` recorded |
|---|---|---|
| bearing outer + static ecc. | 2025-07-05 | 2025-07-07 and 2025-08-21 |
| bearing inner + broken bar | 2025-07-05 | 2025-07-04 |
| bearing inner + bearing outer | 2025-07-02 | 2025-07-04 |

Session identity is almost perfectly recoverable from the features. Taking the
one fault label that was recorded twice on different days at the same operating
condition (`bearing_outer_h`, `speed_circulation / 20 N·m / 3000 rpm`, recorded
2025-07-07 and 2025-08-21) and classifying **acquisition day** from the same
feature family:

```
AUC(day) = 0.999      (same fault, same operating condition, n_test = 112 windows)
```

*Caveat, stated so it is not discovered later:* only one run exists per day for
that fault and condition, so "day" and "run" coincide here and the control
strictly demonstrates **run-level** separability. That is precisely the structure
of the oracle comparison, which also contrasts a small number of distinct runs —
so the inference holds, but the claim should be phrased as "distinct recordings of
the same state are near-perfectly separable" rather than as an isolated
session-effect estimate. A cleaner version of this control would need two
same-fault runs recorded on the same day, which the release does not provide.

### Why this matters

Two recordings of the *same* fault under the *same* condition are separable at
AUC ≈ 1.0. So separability between two recordings that *additionally* differ in
fault is not evidence that the fault caused it. This affects:

- **Within-pair AUC 0.9167–1.0000, median 1.0000.** Cannot be attributed to
  constituent `A` rather than to session.
- **The AUC_dir = 0.000 polarity reversal.** If a constituent score partly tracks
  session nuisance (assembly torque, sensor remounting, thermal state), a
  detector trained in partner `C`'s session can invert in partner `B`'s session
  without any physical polarity inversion. The Holm-corrected permutation test
  (p = 0.0136) establishes that the ordering is not chance, but not that it is
  caused by the fault.

### Recommendation

Keep the analysis; change the interpretation.

1. Weaken "measurable information associated with the missing constituent
   remained present" to *"not attributable to signature disappearance alone"*.
2. Present AUC_dir = 0.000 as a candidate session artefact as well as a candidate
   physical reorientation, and say which cannot be distinguished in this dataset.
3. Report the number of runs per directed comparison. With roughly six versus six
   runs, AUC = 1.000 is reachable from a modest effect.
4. Where possible use **same-session** references: `static_ecc + outer` and
   `bar + outer` were both recorded 2025-07-05.
5. Add the session confound to the limitations, alongside the release
   inconsistencies in §5.

---

## 4. Smaller but worthwhile

### 4a. An ordering anomaly with a likely cause

Under **seen** conditions the more restrictive two-sided regime *outperforms*
one-sided: micro-F1 0.6620 > 0.6581, R_any 0.9444 > 0.9259. This contradicts the
paper's own difficulty hierarchy.

The methods section supplies the likely explanation: the one-sided regime yields
**216 prediction rows from 108 physical runs** (both directions), while
recombination and two-sided yield 108 each. The three regimes are therefore
averaged over different units, and runs whose one direction is hard receive
double weight.

*Fix:* report the two directions separately, or aggregate each run's two
directional predictions into one row so all three regimes have 108 units. This
may restore the expected ordering.

### 4b. Run the context × condition interaction test

The draft states the pattern "does not by themselves constitute a formal test of
a context-by-condition interaction." It is one bootstrap away: compute
Δ(recombination − two-sided) separately under seen and unseen conditions, then
bootstrap the **difference of those differences**, clustered by run. If the
interval excludes zero, the interaction can be claimed directly. This is the most
interesting result in the paper and currently the least committed.

### 4c. Precision, not recall, limits exact decomposition

R_all 0.44 against EM 0.157 means false additions destroy roughly two-thirds of
otherwise-correct decompositions; FA/run 0.64–0.73 is the binding constraint.
Thresholds were tuned for constituent-level F1, which favours recall. A sweep over
threshold criteria (F1 / precision-weighted / balanced accuracy) plotting the
R_all ↔ EM trade-off would convert an incidental observation into a contribution,
and is cheap to run.

### 4d. Miscellaneous

- **Closed-set 0.9132 needs a confidence interval.** With 288 runs over 24 classes,
  five-fold run-level CV gives roughly 2.4 test runs per class per fold. The
  interval is wide, and this number carries argumentative weight as the reference
  for "the dataset is not intrinsically hard".
- **Three of the nine constituents never appear in any compound** (`fball`,
  `fbend`, `fvu`). Compositional claims therefore cover six constituents; state
  this explicitly.
- **Severity merging deserves a one-line ablation.** Compounds contain only `_H`
  severities, so admitting `bearing_inner_L` as a positive for `finner` may help
  (more support) or hurt (label noise). Currently untested.
- **Curated feature-count asymmetry** (2 descriptors for voltage unbalance, 56 for
  eccentricity) invites a "why" question; one sentence of justification suffices.
- **Position against the zero-shot compound literature.** Published methods report
  roughly 75–87 % on *bearing-only* compounds, where both constituents are
  mechanical and both visible in vibration. Eight of the nine compounds here pair
  a mechanical bearing defect with an electrical or magnetic fault, so the
  constituents are observable in different modalities. Lower numbers are
  defensible on exactly those grounds, but the comparison must be explicit or
  reviewers will assume unfamiliarity with the field.

---

## 5. Release inconsistencies worth reporting (independent of the above)

Found while building the benchmark; each biases results silently if unhandled.

1. **288 runs, not the documented 282** (144 per profile). The surplus includes
   later re-acquisitions.
2. **One inconsistent cell.** `bearing_outer_h` has two runs at
   `speed_circulation / 20 N·m / 3000 rpm` while `bearing_inner_h` has none, and
   the surplus outer-race file is stamped 2025-08-21, six weeks after its siblings
   (2025-07-04 to 07-07), in exactly the vacant inner-race slot. Which label is
   correct is not determinable from the data.
3. **Abbreviated compound labels.** In `bearing_outer_H_and_inner_H` the second
   constituent omits its family prefix. Parsed literally it becomes an extra
   constituent with no single-fault support, which makes exact-match unachievable
   for those runs by construction.
4. **Channels are raw voltages.** Applying the published 100 mV/N·m to the torque
   channel yields ≈ 2.4 N·m for runs labelled 20 N·m, so the label is a commanded
   set-point rather than a measurement.

---

## 6. The same correction applied to the independent benchmark work

The trivial-baseline check in §2 was applied to the independent benchmark's own
compound results. They fail it more badly.

That work used a 15-component vocabulary (severities kept separate), window-level
prediction, and a fixed decision threshold. On its strict zero-shot compound
protocol (train on all 180 single-fault runs, test on all 108 compound runs,
15 120 test windows):

| Model | Exact | micro-F1 | ≥1 found |
|---|---|---|---|
| **constant `{bearing_inner_h, bearing_outer_h}`** | **0.1111** | **0.5556** | **1.0000** |
| constant `{bearing_inner_h}` | 0.0000 | 0.3704 | 0.5556 |
| shared vibration + current features | 0.0000 | 0.0614 | 0.068 |
| vibration only | 0.0000 | 0.0929 | 0.117 |
| current only | 0.0000 | 0.0858 | 0.095 |
| late fusion by union of modalities | 0.0080 | 0.1560 | 0.203 |

The constant predictor beats every trained model by 3.6× on micro-F1 and 14× on
exact match. The cause is now clear: models trained on single-fault windows see
exactly one positive of fifteen and therefore emit at most one positive at test
time, whereas every compound requires two. The constant predictor encodes that
prior for free.

**Consequences.** The benchmark's "categorical failure at 0.000 exact match" was
measuring something real but describing it wrongly, and its late-fusion result is
not a solution — it improves a badly calibrated model *towards*, but still far
below, trivial. Those claims are being rewritten rather than quietly dropped.

**Why this supports the draft's approach.** The constituent-level design in this
draft clears the trivial baseline on R_const and R_all precisely because it
supplies what the benchmark models lacked: per-mechanism curated feature
selectors, per-constituent thresholds calibrated on inner cross-validation,
severity merging that roughly doubles per-constituent support, and run-level
median aggregation. Three diagnostics from the benchmark work explain *why* each
choice matters, and are offered for the merged paper's methods discussion:

- **Feature-space dominance.** With a shared feature space, `winding_h` is
  detected on **39.3 %** of windows from current features alone and **0.2 %** once
  vibration features are concatenated — a roughly 200-fold collapse. Per-mechanism
  selectors are structurally immune to this, since the winding detector never sees
  vibration descriptors.
- **Threshold miscalibration.** A fixed threshold on single-fault-trained scores
  produced all-zero predictions on **76 %** of compound windows. Per-constituent
  calibration is the correct remedy.
- **Modality dissociation.** Vibration features never detect an electrical
  constituent (0.000) and current features never detect a mechanical one (0.000),
  which is the empirical justification for mechanism-specific feature families.

---

## 7. Suggested division for a merged paper

Submitting two overlapping papers on this dataset from overlapping authorship
risks a salami-slicing rejection. A single paper is stronger:

**Core (this draft):** constituent-level formulation, crossed
composition–context–condition protocol, physics-guided multimodal features,
cross-partner transfer analysis, statistics.

**Added from the benchmark work:**

- the protocol ladder quantifying leakage: identical features and model span
  0.975 under a random window split, 0.965 in-condition, 0.939 leave-one-
  condition-out, 0.839 cross-profile, 0.767 steady→transitional, 0.333
  single-source
- **direction dominates in condition generalization**: leave-one-condition-out
  costs 2.6 points while single-source training costs over 60
  (Δ = 0.606, paired over 12 folds, p = 7.7 × 10⁻¹⁰) — this sharpens the draft's
  seen/unseen condition axis
- **cross-profile asymmetry** at equal training size: training under speed
  variation transfers to load variation (0.943) while the reverse loses 21 points
  (0.735), p = 3.3 × 10⁻⁵
- **order-domain features help only under condition shift**: +0.047 on
  single-source (p = 8.4 × 10⁻⁴) against +0.001 in-condition (p = 0.84)
- test-time noise robustness curves (20 / 10 / 0 dB)
- cross-model baselines (random forest, linear SVM, 1D CNN) under identical splits
- the release inconsistencies (§5) and the session confound (§3)
- the three diagnostics in §6

---

## 8. Reproducing the numbers in this memo

```bash
# trivial baselines, 9-constituent (draft) scheme and 15-component scheme
python scripts/trivial_baselines.py --data-dir ./data

# session-confound control: classify acquisition day, same fault + condition
python scripts/session_confound.py --data-dir ./data

# per-combination and per-modality compound analysis
python scripts/analyze_compound.py --data-dir ./data --out results

# late fusion by union
python scripts/late_fusion.py --data-dir ./data --out results --seeds 0 1 2
```

Constituent frequencies, acquisition dates, and the release inconsistencies come
from `results/../data/metadata.csv`, built by
`scripts/convert_dataset.py`.
