# Evaluating design-stage manufacturability decisions against the resolution of production

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
| `scripts/qc.py` | the single definition of each quality characteristic (mid-side draw-in from the widths across the scan lines, wall angle from the east and west walls) |
| `scripts/alternatives.py` | production floor (batch and cluster intervals), effect-to-scatter ratios, minimum resolvable change |
| `scripts/sensitivity.py` | the floor under other batch sizes, quantiles and batch centres; scatter versus drift |
| `scripts/measurement.py` | redundancy of the scans, components of the floor (short- and long-term variation, white-noise share, q95 floor, half series, between-series bound), extraction noise of the simulations |
| `scripts/decisions.py` | design-stage decisions (meets / fails / trial) of twelve rules, each calibrated rule with and without the simulation, by evidence relation (new variant, new process setting with interpolation/extrapolation, new family, pooled); exact decisive and safe distances, one-sided distances, paired bootstrap with reference replicates, coverage, GP diagnostics |
| `scripts/guard.py` | family, range and novelty guards on new process settings and a new family, with conditional counts |
| `scripts/scenarios.py` | verdicts against general angular tolerances (ISO 2768-1), stratified by margin, with a cost comparison |
| `scripts/budget.py` | decisions against the number of produced alternatives, by the relation of the new design to them |
| `scripts/robustness.py` | temperature, force–speed confound, constants, floor protocol, adequacy share, smoothed simulation, GP specification, leave one pattern out, friction mapping, conformalised GP, refitting bootstrap |
| `scripts/tuning.py` | learners and settings of the part-level rules M3 and M4 (including quantile loss and inner selection) |
| `scripts/design_space.py`, `scripts/inline.py` | supplementary, not in the paper: DDACS corner sensitivities; in-line verifiability from the force record |
| `scripts/case2_pa12.py` | exploratory, not in the paper and not run by `run_all.sh` (see its docstring) |
| `scripts/figs.py` | `results/figures/`: the paper's figures (PDF and PNG) |
| `scripts/make_tables.py` | writes the manuscript's data tables from the CSVs into `paper/main.tex` |

The results, with every number traced to its CSV, are summarised in [`results/findings.md`](results/findings.md).

`bash scripts/run_all.sh` reproduces every analysis from the cached feature tables in about four hours on
four cores (and extracts them first if they are missing, which takes hours). Constants live in `scripts/common.py` and at the top of each script; seeds are fixed.

Requirements: Python 3.11 with the packages in `requirements.txt`.

## Manuscript

`paper/main.tex` (Springer `sn-jnl`, single file; build with `latexmk -pdf main.tex` in `paper/`). Tables between
`%% BEGIN GENERATED` markers are written by `scripts/make_tables.py`; figures are copied from `results/figures/`.
`paper/submission/` holds the cover letter, outreach drafts and the submission checklist; `paper/review/` the
simulated referee reports on the first version (`main_v1.pdf`) and the response to them.
