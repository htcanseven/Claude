# When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing

Working repository for the paper, submitted to the *Journal of Intelligent Manufacturing*. The dataset survey
that led here is in [`dataset-survey-DFM.md`](dataset-survey-DFM.md).

## Data

| Dataset | Content | Licence |
|---|---|---|
| RDDAC, [doi:10.18419/DARUS-5589](https://doi.org/10.18419/DARUS-5589) (v2.0) | 9,000 deep-drawn and cut DP600 cups: 2 geometries × 3 blank-holder forces × 3 lubrication patterns, 500 consecutive parts each; press force, sheet and oil traverses, 3D scans after drawing and after cutting | CC BY 4.0 |
| DDACS, [doi:10.18419/DARUS-4801](https://doi.org/10.18419/DARUS-4801) (v3.0) | ≈32,000 FE simulations of the same process; 396 matched to the RDDAC conditions, the rest over design corners and process parameters | CC BY 4.0 |

Nothing is downloaded in bulk: the scripts read single files from the DaRUS archives through HTTP range
requests and keep only the extracted features. Raw data are never committed.

The extracted feature tables and the result files in `results/` are derived from RDDAC and DDACS (S. Baum and
P. Heinzelmann), both licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); they were changed by
extracting quality characteristics from the scans and the simulations and computing the statistics the paper
describes.

## Archive

The paper cites this repository on Zenodo (deposit metadata: `.zenodo.json`, `CITATION.cff`). Version 1 held the code,
feature tables and result files of the paper as first submitted; version 2 adds those of the revision (the scripts
`learners.py`, `qualify.py`, `simcheck.py` and `opchar.py` and their results); version 3 those of the second revision
(decision-time guard bands, the trial under between-run variation, release as a capability decision, the prior
sensitivity of M7n and a data dictionary). The licence of the code and the DOI are set by the
author when the deposit is published. [`RELEASE_NOTES.md`](RELEASE_NOTES.md) gives
the checksums of the main result files; `SHA256SUMS` holds the SHA-256 checksums of every script and result file
(`sha256sum -c SHA256SUMS` checks them; `bash scripts/write_checksums.sh` rewrites the file).

## Pipeline

| Script | Output |
|---|---|
| `scripts/features_rddac.py` | `results/features_rddac.csv`: one row per part (force features, traverses, scan characteristics) |
| `scripts/features_ddacs.py` | `results/features_ddacs_rddac.csv`, `results/features_ddacs_corners.csv`: the same characteristics from simulations |
| `scripts/qc.py` | the single definition of each quality characteristic (mid-side draw-in from the flange widths along the laser line, wall angle from the east and west walls) |
| `scripts/alternatives.py` | within-run floor (batch and cluster intervals), effect-to-scatter ratios, minimum resolvable change |
| `scripts/sensitivity.py` | the floor under other batch sizes, quantiles and batch centres; scatter versus drift |
| `scripts/measurement.py` | redundancy of the scans, components of the floor (short- and long-term variation, white-noise share, q95 floor, half series, between-series bound), extraction noise of the simulations |
| `scripts/decisions.py` | design-stage decisions (meets / fails / trial) of fourteen rules, each calibrated rule with and without the simulation (the force trend M1sn is the counterpart of the scaled simulation M1s), by evidence relation (new variant, new process setting with interpolation/extrapolation, new family, pooled); exact decisive and safe distances, one-sided distances, paired bootstrap with reference replicates, coverage, GP diagnostics |
| `scripts/guard.py` | family, range and novelty guards on new process settings and a new family, with conditional counts |
| `scripts/scenarios.py` | verdicts against general angular tolerances (ISO 2768-1), stratified by margin, with a cost comparison |
| `scripts/budget.py` | decisions against the number of produced alternatives, by the relation of the new design to them |
| `scripts/panel.py` | analyses added for the review panel: decomposition by relation and rule, sibling strata, force levels, source-family floor, physical units, failing-side weight, guard band of step 6 and its operating characteristics, guard bands under other requirement priors, a new family scored in the produced family's floor, capability-anchored requirements, M0 without the reference offset, drawing-nominal baseline, floor protocol and lag profile, measurement resolution, run metadata, force effect of the simulation, unit from the reproducibility of q95 |
| `scripts/robustness.py` | temperature, first 150 parts dropped, force–speed confound, constants, floor protocol, floor between series, short calibration series, adequacy share, smoothed simulation, GP specification, leave one pattern out, friction mapping, conformalised GP, relation-preserving refitting bootstrap with paired intervals |
| `scripts/tuning.py` | learners and settings of the part-level rules M3 and M4 (including quantile loss and inner selection) |
| `scripts/design_space.py`, `scripts/inline.py` | DDACS corner sensitivities (not in the paper) and the surrogate of the simulations; drift of the batch centres explained by the in-line signals, and part-level verifiability |
| `scripts/learners.py` | rules added in the revision: trend GP M7n (universal kriging, MAP under priors), autoregressive multi-fidelity M7, friction calibration with a GP discrepancy Mcd, predictors with relation-matched split-conformal intervals (P+RM), GP diagnostics, few-shot transfer to a new family (ICM GP) |
| `scripts/simcheck.py` | the simulation dataset against the measurement (validation, friction fits, depth offset, oil-film mapping, envelope over measured inputs) and the measurement (characteristics, single-run floors, a dimension fixed by the tooling) |
| `scripts/qualify.py` | qualification as a team would use it: decision-time sibling strata, guard bands per family, out of sample and per prior, costs and the trial as a rule, coverage with cluster intervals and interval scores, between-run sensitivity, cross-fitted selection, per-characteristic results, design-level verdicts, lower limits, short runs, capability statistic, M6 coverage, floors without the held-out series |
| `scripts/qualify.py` (second revision) | guard bands available when deciding (a family's own sibling cases; for a new setting the other family's band), the trial under between-run variation and the cost of its errors, release as a capability decision, the cheapest option per cost setting, the worked example |
| `scripts/opchar.py` | the scoring function on its own: distances, guard band, step 6 and expected cost for any table of intervals, truths and floors (`--selfcheck` reproduces `dec_resolution.csv` and the new-setting guard bands of `qual_guard_decision.csv`) |
| `scripts/data_dictionary.py` | `results/DATA_DICTIONARY.md`: columns, scopes and rule codes of every result file in the terms of the paper, and the floor each file uses |
| `scripts/case2_pa12.py` | exploratory, not in the paper and not run by `run_all.sh` (see its docstring) |
| `scripts/figs.py` | `results/figures/`: the paper's figures (PDF and PNG) |
| `scripts/make_tables.py` | writes the data tables from the CSVs into `paper/main.tex` |

The current results, with every number of the paper traced to its CSV, are summarised in
[`results/findings.md`](results/findings.md); the findings of earlier versions are in
[`results/findings_history.md`](results/findings_history.md), and
[`results/DATA_DICTIONARY.md`](results/DATA_DICTIONARY.md) explains the result files.

`bash scripts/run_all.sh` reproduces every analysis from the cached feature tables in about five hours on
four cores (and extracts them first if they are missing, which takes hours). Constants live in `scripts/common.py` and at the top of each script; seeds are fixed.

Requirements: Python 3.11 with the packages in `requirements.txt`.

## Manuscript

`paper/main.tex` (Springer `sn-jnl`; build with `latexmk -pdf main.tex` in `paper/`) is the manuscript: 31 pages of
main text, declarations and references, a single document without appendix or supplementary material; the
archived result files, which the text names in typewriter type, hold the tables behind its statements, and
`results/findings.md` maps every number to its script and result file. Tables between
`%% BEGIN GENERATED` markers are written by `scripts/make_tables.py`; figures are copied from `results/figures/`.
`paper/submission/` holds the cover letter, outreach drafts, the upload script and the submission checklist.

`paper/review/` holds the simulated reviews, all written by AI agents: the referee reports on the first version and
the response to them; a simulated call-for-papers panel in three rounds (`paper/review/cfp_panel/`, with responses and
marked-up comparisons); and a simulated first round at the *Journal of Intelligent Manufacturing*
(`paper/review/jim_panel/round1/`: three reports, the editor's decision, the response `response_round1.md` with
page and line numbers, and `main_diff.pdf` against the reviewed version), followed by a simulated second round on the
shortened 31-page version (`paper/review/jim_panel/round2/`: the frozen manuscript, three reports, the editor's
decision, all minor revision, the response `response_round2.md` and `main_diff.pdf` against the reviewed version),
and a simulated third round that verified the second revision (`paper/review/jim_panel/round3/`: three reports, the
editor's decision, accept subject to conditions, the response `response_round3.md` to its corrections D1–D10 and
`main_diff.pdf`). None of them is a review by a journal.
