# MCC5-THU Motor — Baseline Pipeline

Reproducible first-baseline pipeline for the **MCC5-THU multi-mode motor fault
diagnosis dataset** (Chen et al., *Data in Brief* 65 (2026) 112583,
dataset DOI [10.17632/6s3dggj9mw.1](https://doi.org/10.17632/6s3dggj9mw.1),
CC BY 4.0), intended as groundwork for an IEEE Access submission.

The dataset: 282 runs × 90 s from a 2.2 kW three-phase asynchronous motor,
8 synchronized channels (key-phase, torque, triaxial vibration, three-phase
currents) at 12.8 kHz, 24 fault conditions (incl. 9 mechanical–electrical
compound faults) under 12 speed/load profiles (steady + transitional).

## Quick start (on your own computer)

Requires Python 3.10+ and ~30 GB free disk.

```bash
cd mcc5-thu-baselines
pip install -r requirements.txt

# 1. Create the data folder and download both zips (~13 GB) from Hugging Face
python scripts/download_dataset.py --data-dir ./data

# 2. Convert CSVs to compact float32 .npz and build metadata.csv
#    (streams each CSV straight from the zip; no CSVs written to disk)
python scripts/convert_dataset.py --data-dir ./data

# 3. Run the feature-engineering baseline (RF / SVM, all three protocols)
python scripts/run_feature_baseline.py --data-dir ./data --out results/

# 4. Run the 1D-CNN baseline
python scripts/run_cnn_baseline.py --data-dir ./data --out results/
```

## Evaluation protocols

Follows the leakage-free guidance in the dataset paper (split at the
recording-run level *before* windowing):

| Protocol | Train | Test |
|---|---|---|
| `in_condition` | early portion of each run (temporal split, gap between train/test) | late portion of the same runs |
| `unknown_condition` | 11 of 12 operating-condition groups | held-out condition group (leave-one-condition-out) |
| `steady_to_transitional` | quasi-stationary segments (low speed/torque derivative) | transitional segments (ramps) |

Note: the dataset has one recording per (fault, condition) pair, so a pure
run-level in-condition split is not possible; the temporal-split variant with
a guard gap is used instead and labeled as such in results.

## Labels

Parsed from filenames (see `src/mcc5/metadata.py`):

- `fault_full` — the full 24-class condition label (e.g. `bearing_inner_H`,
  `winding_H_and_bearing_outer_H`)
- `components` — multi-label decomposition for compound-fault experiments
  (e.g. `winding_H` + `bearing_outer_H`)
- `profile` — `speed_circulation` (constant torque, varying speed) or
  `torque_circulation` (constant speed, varying torque)
- `torque_nm`, `speed_rpm` — nominal set-points; together with `profile`
  they define the 12 operating-condition groups.

## Layout

```
scripts/            entry points (download, convert, baselines)
src/mcc5/           library code (metadata, conversion, windows, features,
                    splits, models)
results/            metrics tables + confusion matrices land here
```
