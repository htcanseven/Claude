# Start here

A benchmark study of the **MCC5-THU motor fault diagnosis dataset**
(Chen et al., *Data in Brief* 65 (2026) 112583; data DOI
[10.17632/6s3dggj9mw.1](https://doi.org/10.17632/6s3dggj9mw.1), CC BY 4.0).

The dataset is published without baselines. This package contains the code and
results for the first benchmark on it: nine evaluation protocols, three model
families under identical splits, and an analysis of where they fail.

**The dataset itself is not included** (≈13 GB) and neither is the derived
feature cache (≈2 GB). Both are reproducible from the code — see
*Reproducing* below.

---

## The one-paragraph summary

On this dataset, the evaluation protocol moves reported accuracy further than
any modelling choice does. With one feature set and one model, accuracy runs from
**0.975** under a random window split to **0.333** when training is confined to a
single operating condition, and to **0.000** when compound faults must be
recognised from single-fault training alone. Three model families reproduce the
same ladder. The compound-fault failure is the sharpest result: a model that
identifies held-out single faults at 0.900 exact match scores 0.000 on unseen
*combinations* of those same faults, and reports no fault at all on 76 % of
doubly-faulted windows.

---

## What to read, in order

| # | File | Why |
|---|---|---|
| 1 | `results/FINDINGS.md` | every measured result with the reasoning; the best single document |
| 2 | `paper/tables.md` | the generated tables (T1–T5) |
| 3 | `paper/figures/` | four figures; `fig4_order_spectra.png` is the physics validation |
| 4 | `paper/PAPER_DRAFT.md` | the manuscript draft, including its own honest limitations |
| 5 | `paper/stats.md` | significance tests for the headline contrasts |
| 6 | `README.md` | the repository's own overview, aimed at a benchmark user |

## Where the code lives

```
src/mcc5/
  protocols.py   THE IMPORTANT ONE: every evaluation protocol, defined once
  splits.py      the split functions and the multi-label metrics
  physics.py     tachometer, order tracking, envelope demodulation
  features.py    108 time/frequency features + 36 order-domain features
  cache.py       precompute windows/features once; all protocols reuse them
  convert.py     dataset CSV -> float32 .npz + parsed metadata
  metadata.py    filename -> fault/severity/condition labels
  models.py      the CNN baseline and the compositional network
  windows.py     windowing and stationary/transitional labelling

scripts/
  download_dataset.py  fetch the two dataset archives (resumable)
  convert_dataset.py   convert to .npz + build metadata
  build_cache.py       precompute all windows and features
  run_benchmark.py     ONE model across every protocol  <- main entry point
  run_full_campaign.sh all models, ablations, noise curves
  analyze_compound.py  the cross-modal masking experiment
  make_tables.py       regenerate paper/tables.md from the result CSVs
  make_stats.py        significance tests
  make_figures.py      regenerate the figures
```

`src/mcc5/protocols.py` is where to look first. Every baseline enumerates splits
through it, so any two numbers in the results are comparable by construction
rather than by convention, and a new method can be dropped in without
reimplementing the splits.

## Where the results live

```
results/
  bench_<model>_<features>_<stage>.csv   one row per protocol x seed
  components_*.csv                       per-fault-component F1
  compound_per_combination.csv           per compound type (cross-modal test)
  compound_per_component.csv             which constituent survived
  FINDINGS.md                            the written analysis
  confusion_matrices/                    a representative subset
paper/
  tables.md, table_T*.csv                generated tables
  stats.md, table_T7.csv                 significance tests
  figures/*.png                          generated figures
  PAPER_DRAFT.md, references.bib         manuscript
```

---

## The results in brief

### Protocol sets the score (T1)

| Protocol | What is held out | RF | SVM | CNN |
|---|---|---|---|---|
| `leaky_random` | nothing — random windows | 0.975 | 0.964 | 0.939 |
| `in_condition` | last 30 % of each recording | 0.965 | 0.955 | 0.913 |
| `unknown_condition` | 1 of 12 conditions (12 folds) | 0.939 | 0.947 | 0.883 |
| `cross_profile` | the other excitation profile | 0.839 | 0.874 | 0.810 |
| `steady_to_transitional` | speed/load ramps | 0.767 | 0.885 | — |
| `single_source` | 11 conditions, training on 1 | **0.333** | 0.365 | 0.363 |
| `compositional_zeroshot` | all compound faults | **0.000** | — | — |

### Two findings that change how robustness should be measured

1. **Leave-one-condition-out is nearly free** (−2.6 points). Training on eleven
   of twelve conditions brackets the held-out one, so the model interpolates.
   Reversed — train on one condition, test on the other eleven — costs over 60
   points. The near-universal robustness test in this literature is the easy
   direction.
2. **Cross-profile transfer is asymmetric** at equal training size: training
   where speed varies transfers to load variation (0.943), while the reverse
   loses 21 points (0.735). Training-time excitation diversity matters more than
   training-set size.

### Compound faults fail categorically, and it is controlled

| Test set | Exact match | micro-F1 | ≥1 component found | all-zero predictions |
|---|---|---|---|---|
| held-out **single** faults | **0.900** | 0.936 | 0.901 | 0.075 |
| unseen **compound** faults | **0.000** | 0.072 | 0.080 | 0.760 |

Same features, same model, same training data. The components are individually
learnable, so this is a failure to *compose*. Per-component F1 shows the shape of
it: bearing components survive weakly (0.09–0.17) while every non-bearing
constituent is annihilated — `broken_bar`, `static_eccentricity`, and
`dynamic_eccentricity` all score exactly **0.000**.

Why this matters: published zero-shot compound-fault methods report **75–87 %**,
but on compounds whose constituents are *both mechanical and both visible in
vibration*. Eight of this dataset's nine compounds pair a mechanical bearing
defect with an *electrical or magnetic* fault, so the constituents live in
different modalities. `analyze_compound.py` tests that explanation against the
dataset's one mechanical-only compound.

### Physics features help exactly where expected

Order-domain features (speed-invariant by construction) barely change
in-distribution accuracy (+0.004) but roughly **double micro-F1 on the compound
protocols** (0.222 → 0.446 and 0.062 → 0.228).

`fig4_order_spectra.png` validates the signal processing: the outer-race defect
peaks on BPFO, the inner-race defect on BPFI, and the ball defect raises nothing
at BSF. Envelope demodulation must precede order tracking — on the raw order
spectrum the healthy recording scores *higher* at BPFO than the faulty one.

---

## What this work does **not** claim

Worth stating plainly, since it shaped the framing:

- Leakage-aware evaluation, the multi-label formulation of compound faults, and
  the superposition principle are all **established prior work**, cited in
  `paper/references.bib`. None is claimed as novel.
- **No method here solves the compound-fault problem.** Superposition
  augmentation lifts zero-shot exact match from 0.000 to 0.029 — a 72×
  improvement and still unusable. It is offered as a baseline to beat.
- Architectural ideas that did **not** work are reported rather than dropped:
  cross-modal gated fusion, adversarial condition-invariance, and appended order
  features all failed, and the complete architecture was the *weakest* variant
  (micro-F1 0.197 vs 0.399 for a single-encoder ablation). Model capacity was not
  the binding constraint; the absence of any multi-label training signal was.
- One rig, one motor rating, no cross-dataset validation. The synthetic noise
  study is additive Gaussian and is not a substitute for field data.

## Four things to know about the data release

Each would silently bias results if unhandled:

1. **288 recordings, not the documented 282** (144 per profile).
2. **One inconsistent cell**: `bearing_outer_h` has two recordings at
   `speed_circulation / 20 N·m / 3000 rpm` while `bearing_inner_h` has none, and
   the surplus file is stamped six weeks after its siblings. Reported, not
   relabelled.
3. **Abbreviated compound labels**: in `bearing_outer_H_and_inner_H` the second
   constituent omits its family prefix. Parsed literally it becomes a sixteenth
   component with no training support, making zero-shot exact match unachievable
   for those recordings by construction.
4. **Channels are raw voltages.** Applying the published 100 mV/N·m to the torque
   channel yields ≈2.4 N·m for recordings labelled 20 N·m, so the label is a
   commanded set-point, not a measurement.

---

## Reproducing

```bash
pip install -r requirements.txt

python scripts/download_dataset.py --data-dir ./data   # ~13 GB, resumable
python scripts/convert_dataset.py  --data-dir ./data   # ~10 min
python scripts/build_cache.py      --data-dir ./data   # ~6 min, 4 workers

# one model across all protocols
python scripts/run_benchmark.py --data-dir ./data --model rf --seeds 0 1 2

# everything (several hours on 4 CPU cores)
bash scripts/run_full_campaign.sh ./data results

python scripts/make_tables.py  --out results --paper paper
python scripts/make_stats.py   --out results --paper paper
python scripts/make_figures.py --out results --data-dir ./data
```

CPU-only throughout; no GPU was used. Seeds are fixed and reported in every
results row.
