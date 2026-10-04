# Design-stage manufacturability decisions qualified with production evidence

Working repository for a paper aimed at the *Research in Engineering Design* special collection
**AI in Design for Manufacturing** (deadline 31 December 2026). The dataset survey that led here is in
[`dataset-survey-DFM.md`](dataset-survey-DFM.md).

## Data

| Dataset | Content | Licence |
|---|---|---|
| RDDAC, [doi:10.18419/DARUS-5589](https://doi.org/10.18419/DARUS-5589) (v2.0) | 9,000 deep-drawn and cut DP600 cups: 2 geometries × 3 blank-holder forces × 3 lubrication patterns, 500 consecutive parts each; press force, sheet and oil traverses, 3D scans after drawing and after cutting | CC BY 4.0 |
| DDACS, [doi:10.18419/DARUS-4801](https://doi.org/10.18419/DARUS-4801) (v3.0) | ≈32,000 FE simulations of the same process; 396 matched to the RDDAC conditions, the rest over design corners and process parameters | CC BY 4.0 |

Nothing is downloaded in bulk: the scripts read single files from the DaRUS archives through HTTP range
requests and keep only the extracted features. Raw data are never committed.

## Pipeline

| Script | Output |
|---|---|
| `scripts/features_rddac.py` | `results/features_rddac.csv`: one row per part (force features, traverses, scan characteristics) |
| `scripts/features_ddacs.py` | `results/features_ddacs_rddac.csv`, `results/features_ddacs_corners.csv`: the same characteristics from simulations |
| `scripts/qc.py` | the single definition of each quality characteristic |
| `scripts/alternatives.py` | production floor, effect-to-scatter ratios between alternatives, minimum resolvable change |
| `scripts/sensitivity.py` | the floor under other batch sizes, quantiles and batch centres; scatter versus drift |
| `scripts/decisions.py` | design-stage decisions (meets / fails / uncertain) from six rules (nominal simulation, bias correction, conformal envelope, simulation + ML, ML only, Gaussian-process calibration) scored against production, leave-one-alternative-out and across geometries |
| `scripts/budget.py` | the same decisions against the number of produced alternatives used for calibration |
| `scripts/design_space.py` | sensitivities over the DDACS design corners; surrogate accuracy against the production floor |
| `scripts/inline.py` | in-line verifiability of each characteristic from the force record |
| `scripts/figs.py` | `results/figures/`: the paper's figures (PDF and PNG) |

The results, with every number traced to its CSV, are summarised in [`results/findings.md`](results/findings.md).

`bash scripts/run_all.sh` reproduces every analysis from the cached feature tables in about 20 minutes on
four cores (and extracts them first if they are missing, which takes hours). Constants live in `scripts/common.py` and at the top of each script; seeds are fixed.

Requirements: Python 3.11 with the packages in `requirements.txt`.
