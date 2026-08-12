# MCC5-THU Motor — Benchmark Suite

A leakage-aware benchmark for the **MCC5-THU multi-mode motor fault diagnosis
dataset** (Chen et al., *Data in Brief* 65 (2026) 112583; dataset DOI
[10.17632/6s3dggj9mw.1](https://doi.org/10.17632/6s3dggj9mw.1), CC BY 4.0).

The dataset ships without baselines. This repository supplies **nine evaluation
protocols, reference baselines across three model families, and the analysis
code**, so a new method can be compared against published numbers without
reimplementing the splits.

## The headline: the protocol sets the score

One dataset, one feature set, one model (random forest on 108 handcrafted
features). Only the protocol changes:

| Protocol | What is held out | Accuracy |
|---|---|---|
| `leaky_random` | nothing — random windows | **0.975** |
| `in_condition` | last 30 % of each recording, guard gap | 0.965 |
| `unknown_condition` | one of 12 operating conditions (12 folds) | 0.939 ± 0.024 |
| `cross_profile` | the other excitation profile (2 folds) | 0.839 ± 0.147 |
| `steady_to_transitional` | speed/load ramps | 0.767 |
| `single_source` | 11 conditions, training on 1 (12 folds) | **0.333 ± 0.106** |
| `compositional_zeroshot` | all compound faults (exact match) | **0.000** |

Three results worth knowing before designing an experiment on this dataset:

1. **Leave-one-condition-out is nearly free** (−2.6 points). Training on eleven
   of twelve conditions brackets the held-out one, so the model interpolates.
   Reverse it — train on one condition, test on the rest — and accuracy falls by
   over 60 points. Robustness claims should be measured in that direction.
2. **Cross-profile transfer is asymmetric** at equal training size: training
   where speed varies transfers to load variation (0.943), while the reverse
   loses 21 points (0.735). Excitation diversity beats data volume.
3. **Compound faults fail categorically, not gradually.** A multi-label model
   that identifies held-out single faults at 0.900 exact match scores 0.000 on
   unseen combinations of those same faults, and predicts *no fault at all* on
   76 % of doubly-faulted windows. Whenever a bearing defect co-occurs, the
   second fault is annihilated (F1 = 0.000 for broken bars, static and dynamic
   eccentricity).

## Quick start

Requires Python 3.10+ and ~30 GB free disk.

```bash
pip install -r requirements.txt

python scripts/download_dataset.py --data-dir ./data   # ~13 GB, resumable
python scripts/convert_dataset.py  --data-dir ./data   # CSV -> float32 .npz + metadata
python scripts/build_cache.py      --data-dir ./data   # windows, features, order features

# one model across every protocol
python scripts/run_benchmark.py --data-dir ./data --model rf --seeds 0 1 2

# or the full campaign (all models, ablations, noise curves)
bash scripts/run_full_campaign.sh ./data results

python scripts/make_tables.py   --out results --paper paper
python scripts/make_figures.py  --out results --data-dir ./data
```

## Protocols

Defined once in [`src/mcc5/protocols.py`](src/mcc5/protocols.py), which every
baseline enumerates, so cross-model comparability is structural rather than
conventional. Windows are 8192 samples (0.64 s), non-overlapping; the three
vibration and three current channels are inputs, while key-phase and torque are
reserved for deriving shaft speed and condition descriptors and are never given
to the classifier.

| Protocol | Question it asks |
|---|---|
| `leaky_random` | how much does a random window split inflate results? |
| `in_condition` | conventional in-distribution accuracy |
| `unknown_condition` | the standard robustness test (12 folds) |
| `cross_profile` | does load-variation training transfer to speed variation? |
| `single_source` | commissioning-realistic extrapolation from one condition |
| `steady_to_transitional` | robustness to non-stationary operation |
| `compositional_control` | control: same model, held-out single faults |
| `leave_combination_out` | generalising to unlogged fault combinations (3 folds) |
| `compositional_zeroshot` | strict composition: singles → all compounds |

`compositional_*` protocols use a multi-label formulation over 15 fault
components, so a compound fault is the union of its parts and unseen
combinations stay expressible.

### Why `in_condition` is a temporal split

The dataset holds exactly one recording per (fault, condition) pair, so a
run-level split necessarily also changes the operating condition — that is
`unknown_condition`, not an in-distribution test. `in_condition` therefore splits
each recording temporally with a 10 % guard gap, and `leaky_random` is reported
alongside it to bound the residual optimism.

## Physics utilities

The key-phase channel is a **1 pulse-per-revolution tachometer**, verified
against the constant-speed recordings (991 / 1989 / 2999 rpm recovered for the
1000 / 2000 / 3000 rpm labels). [`src/mcc5/physics.py`](src/mcc5/physics.py)
provides instantaneous speed, shaft angle, computed order tracking, envelope
demodulation, and bearing-order band energies.

Demodulation must precede order tracking. On the raw order spectrum the bearing
bands do not separate fault from healthy (healthy BPFO 0.0143 vs outer-race
0.0119 — the wrong way round), because a localised defect modulates a structural
resonance rather than appearing at the defect frequency. After band-pass
demodulating 1–5 kHz, each raceway defect raises its own order ≈2.4× over
healthy. Ball defects do not raise BSF, consistent with rolling-element defects
being the hardest to detect.

## Notes on the data release

Surfaced automatically by the coverage audit in `build_metadata`:

- **288 recordings, not the documented 282** (144 per profile); the surplus
  includes later re-acquisitions.
- **One inconsistent cell**: `bearing_outer_h` has two recordings at
  `speed_circulation / 20 N·m / 3000 rpm` while `bearing_inner_h` has none, and
  the surplus outer-race file is stamped six weeks after its siblings. Reported,
  not relabelled — but it does unbalance one `unknown_condition` fold.
- **Abbreviated compound labels**: in `bearing_outer_H_and_inner_H` the second
  component omits its family prefix. Parsed literally it becomes a sixteenth
  component with no single-fault support, which silently makes zero-shot exact
  match unachievable for those recordings.
- **Channels are raw voltages**; applying the published 100 mV/N·m to the torque
  channel gives ≈2.4 N·m for recordings labelled 20 N·m, so treat the label as a
  commanded set-point.

## Baseline for compound faults: fault superposition

Independent excitations of a linear structure superpose to first order, so adding
two single-fault windows **from the same operating condition** approximates a
machine carrying both faults, labelled with the union of their components. This
manufactures two-positive training examples without observing compound data, so
the zero-shot protocol stays honest.

| Configuration | Exact match | micro-F1 |
|---|---|---|
| random forest, thresholded | 0.000 | 0.072 |
| CNN, no augmentation | 0.0004 | 0.287 |
| CNN + superposition, 8 epochs | 0.0138 | 0.335 |
| CNN + superposition, 24 epochs | **0.0290** | 0.343 |

A 72× improvement, and still far from usable: **recognising an electromagnetic
fault masked by a co-occurring bearing defect, from single-fault training alone,
is an open problem on this dataset.** Cross-modal gated fusion, adversarial
condition-invariance, and appended order features did *not* help; the absence of
any multi-label training signal, not model capacity, was the binding constraint.

## Layout

```
scripts/    download, convert, cache, benchmark runner, campaign, tables, figures
src/mcc5/   metadata, conversion, windows, features, physics, splits, protocols, models
results/    metrics CSVs, confusion matrices, per-component F1, FINDINGS.md
paper/      manuscript draft, generated tables and figures
```

## Citing

Cite the dataset article and the dataset DOI separately:

- S. Chen, Z. Liu, C. Li, D. Zou, X. He, D. Zhou, "Multi-mode fault diagnosis
  datasets of three-phase asynchronous motor under variable working conditions,"
  *Data in Brief*, vol. 65, 112583, 2026.
- Dataset: <https://doi.org/10.17632/6s3dggj9mw.1> (CC BY 4.0).
