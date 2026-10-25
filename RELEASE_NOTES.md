# Release notes

Code, feature tables and result files of the paper *A production-referenced evaluation of design-stage decision rules
in deep drawing: when can a prediction replace a physical trial?* (H. T. Canseven), first submitted as *Evaluating
AI-based manufacturability decisions against the resolution of production*.

## Version 3 (October 2026)

Version 3 holds the code, feature tables and result files that produce the numbers of the paper's second revision,
a single document without supplementary material: the tables behind its statements are the result files, which the
text names in typewriter type. The
result files of version 2 are unchanged (their checksums still hold) except those listed under *Changed*.

**Added.**

- `scripts/qualify.py`, new jobs: guard bands available when deciding, validated by the matching scheme
  (`qual_guard_decision.csv`); the trial of the first 20 or 50 parts under the between-run component
  (`qual_between_run_trial.csv`) and the expected cost of its own errors (`qual_trial_cost.csv`); release scored on
  the mean plus four standard deviations (`qual_release_capability.csv`); the cheapest option per relation, trial
  cost, prior and cost ratio (`qual_cost_cheapest.csv`); every number of the worked example
  (`qual_worked_example.csv`).
- `scripts/learners.py --prior-sensitivity`: the trend GP M7n with each of its four prior medians halved or doubled
  (`learn_m7n_priors.csv`; the reference variant reproduces the stored fits exactly).
- `scripts/data_dictionary.py` and `results/DATA_DICTIONARY.md`: the columns, scopes and rule codes of every result
  file in the terms of the paper (`within` = sibling, `transfer` = new family, M4 = M3n, `resolution_floors` = decisive
  distance), and the floor each file uses.
- `scripts/opchar.py --selfcheck` also reproduces the new-setting guard bands of `qual_guard_decision.csv`, their
  share correct and trial rate (40 of 40), with the stand-alone scoring function.
- `results/findings_history.md`: the findings of earlier versions, moved out of `findings.md`, which now holds only
  the current numbers and the map of the paper. (An Online Resource drafted for this version was withdrawn before
  the deposit at the author's request; its tables are the result files named in the paper.)

**Changed.**

- `results/qual_coverage.csv`: coverage values unchanged; columns `rm_n`, `rm_quantile_floors` (the borrowed cases
  and quantile behind each relation-matched interval) and `ci_note` added; cluster intervals are given only with a
  sibling, where every alternative has its own calibration set (for a new setting the alternatives of a held-out cell
  share one fit, and the intervals of version 2 were degenerate or too narrow), and are drawn from a new bootstrap
  stream (bounds move by at most one alternative in 18); interval scores added for the decision-time strata.
- `results/figures/`: `F_schematic`, `F_batches`, `F_costs` and `F3_decisions_main` redrawn at smaller heights, and
  `F_batches` with the warm-up shaded; the data are unchanged.
- `make_tables.py` writes guard bands of half a floor above 10 floors with their decimal (14.5, not 14).
- `results/findings.md` and `results/summary_qualify.md` rewritten.

**Corrected before the deposit, after a third simulated review round** (`paper/review/jim_panel/round3/`).

- `qualify.costs`: the cost-minimising band follows step 5, searched from the rule's 95 % band up to 20 floors, and a
  rule without a 95 % band sends every design to trial (version 3 as first prepared searched 0–40 floors without that
  floor). `qual_costs.csv`, `qual_cost_cheapest.csv` and `F_costs` are recomputed; the paper's statements on costs
  hold under the rule, and the nominal simulation is no longer the cheapest option anywhere.
- `qualify.guard_decision_time` adds the shares correct, trial rates and verdict counts per family
  (`qual_guard_decision.csv`); `qualify.guard_nested_sibling` validates the nearest setting's sibling band with
  strictly nested fits (`qual_guard_nested.csv`).
- `qualify.nominal_level`: the largest-residual and jackknife+ levels are labelled guaranteed only with a sibling
  (`level` in `qual_coverage.csv`; coverage values unchanged).
- `simcheck.grid_comparisons` (`python3 simcheck.py --grid`): the comparisons independent of blank and scales over
  the whole friction-thickness grid (`sim_grid_comparisons.csv`).
- `make_tables.py`: Table 3 rounds 17.65 to 17.7; the notes of Tables 4–7 point to the result files behind them. `data_dictionary.py`: the `transfer`, `scheme` and `level` entries.

**Wording, at the author's request.** The paper's prose was rewritten in the style of the author's earlier papers,
with American spelling, and its title reordered. `make_tables.py` writes the new table captions (and "center lines"
in Table 3), and `figs.py` labels the lower row of `F_costs` "cost-minimizing band"; no number changes.

**Corrected after a fourth simulated review round** (`paper/review/jim_panel/round4/`), without a change of number.

- `make_tables.py`: the Table 4 note points to `panel_floor_protocol` for sigma_b and sigma_w (they reproduce each
  floor to within 12 %) and to `sens_drift` for the drift ratio, not to `meas_floor`; the Table 7 note names the
  intervals and `qual_guard_nested`; the Table 3 note names `meas_scan`.
- `data_dictionary.py` and `results/DATA_DICTIONARY.md`: the `meas_floor`, `panel_floor_protocol` and `sens_drift`
  rows say which file holds the floor components and the drift ratio; the `share_correct` row of
  `qual_guard_decision` says that its interval exists with a sibling only, and why there is none for a new setting.
- `results/findings.md`: the paper has 33 pages.

Main result files added or changed in version 3:

| File | SHA-256 |
|---|---|
| `results/qual_guard_decision.csv` | `3c4f6dc98b23442a0534af6f977874a09cada29545ea45d409ac1a8504e5af9d` |
| `results/qual_guard_nested.csv` | `1a2266a7cc06a3c29b1ab483d75cfc4e56d683c01516981ad24079fb664a82ae` |
| `results/qual_costs.csv` | `660dfb16fb3329abc73cf29120e05fe1f5b02a562d6cc052f47f70c7fe96de9f` |
| `results/qual_cost_cheapest.csv` | `63a5ea50bf49d773d3b53895286d22fdcfde614dfc7be1f56ba91cb58641f2bb` |
| `results/qual_between_run_trial.csv` | `f32c802cec3e108856942a8f45ef6fd01118ed74d0cf84c3703a6105d14ec85f` |
| `results/qual_trial_cost.csv` | `6425ab2c15705082837b367e5428990f3db85d1edf6f1a27eab514ff3d60d414` |
| `results/qual_release_capability.csv` | `cf6f7decf9d6b5deda7819c0366f20fa87bfc9546d53e5dc498cb077c63b4727` |
| `results/qual_worked_example.csv` | `d968d40c6c9daeb3bea684001051ba435392b60b473c711f35008cff02391a50` |
| `results/learn_m7n_priors.csv` | `5b5ba404a4b34774d06bed73d91c08e0c4e78ba44dbbe1c802b65b168b2715f1` |
| `results/qual_coverage.csv` | `652c96c9cd07380ca042f954968549f404410a949cf44b697f9e5c61252e4585` |
| `results/sim_grid_comparisons.csv` | `01dddfdcdd67124155f32eb7bac70e2739130ae3891c28e8166eb3ef10c4fc30` |

**Open before the deposit is published (the author's actions).** A licence file for the code and the licence fields
of `.zenodo.json` and `CITATION.cff`; the DOI, then cited in the paper and in `CITATION.cff`; and a timestamped
deposit of `paper/notes/frozen_procedure.md` if the procedure is to be cited as registered. The paper no longer
calls the procedure frozen; it names a confirmatory test of the procedure, registered before the analysis, as an
extension.

## Version 2 (October 2026)

Version 2 holds the code, feature tables and result files that produce the numbers of the revised paper, which has
no appendix and no supplementary material. Every result file of version 1 is unchanged (the checksums under version 1 still hold), except
the figure `F5_reliability`, which now shows the rules of the main text; `figs.py`, `make_tables.py` and `run_all.sh`
were extended, and the revision adds:

- `scripts/learners.py`: the trend GP M7n, the autoregressive multi-fidelity model M7, the friction calibration with
  a discrepancy term Mcd, predictors with relation-matched intervals (P+RM), GP diagnostics and the few-shot transfer
  to a new family (`results/learn_*.csv`).
- `scripts/qualify.py`: decision-time sibling strata, guard bands per family, out of sample and under other priors,
  costs and the trial as a rule, coverage with cluster intervals and interval scores, the between-run sensitivity,
  cross-fitted selection, results per characteristic, design-level verdicts, lower limits, short runs, a capability
  statistic, M6 coverage and floors without the held-out series (`results/qual_*.csv`).
- `scripts/simcheck.py`: the simulation dataset against the measurement and the measurement behind the floor
  (`results/sim_*.csv`, `results/meas_characteristics.csv`, `meas_cut_walls.csv`, `meas_run_floors.csv`,
  `meas_tooling_reference.csv`).
- `scripts/opchar.py`: the scoring function on its own, for any table of intervals, truths and floors;
  `python opchar.py --selfcheck` reproduces `results/dec_resolution.csv`.
- `results/findings.md` maps every number of the revised paper to its script and result file; the results that the
  paper does not tabulate are in the result files.
- `requirements.txt` now pins every package, including `tabulate`, which `DataFrame.to_markdown` needs.

Main result files added in version 2:

| File | SHA-256 |
|---|---|
| `results/learn_intervals.csv` | `9abfbe52fa20e0e0a29b63721ff8364d101b1c2d937e92543155e4c17acd0b3c` |
| `results/learn_resolution.csv` | `3241c641ffd6b60e84800cbb1928d2c8350f5aa401085775e3b9bfb3ee0a9b60` |
| `results/qual_strata.csv` | `9ef41a47ec1f943d967fb4f1756f30cf57c3eb54870267164a8e5aa916323010` |
| `results/qual_guard_oos.csv` | `8d39ffb9ed6b6552614d7eee2487ed03839791d6ed2888cee782acc80ac34008` |
| `results/qual_coverage.csv` | `269c1d8d6107e670a1ef823a806b7352e0492a571b93b2e8279cd7373ff66836` |
| `results/qual_costs.csv` | `0c31c81c0242c477498fe955c5c2b590938a41a98c5bfaf2aa956a677346a8a2` |
| `results/sim_validation.csv` | `97f51438d6e3cf9cba24953330833374f6cde1d2fd70cbc1695a1122019ebc28` |

**Constants and development record.** No timestamped snapshot of the constants was deposited before the first
results; the paper therefore no longer states that the repository history records when they were set. The order in
which rules and analyses were added, and which of them followed reviews simulated with a language model, is stated in
Section 4.5 and in the declarations of the paper.

**Licence.** The code carries no licence yet: the author adds a `LICENSE` file and the licence field of the deposit
metadata before the deposit is published. The data-derived files keep the CC BY 4.0 terms below.

## Version 1 (October 2026)

Version 1 holds exactly the code, feature tables and result files that produce the numbers of the paper as submitted
for publication. It is the first deposited version.

**Contents.**

- `scripts/`: the analysis pipeline (`bash scripts/run_all.sh`; Python 3.11 with the packages in `requirements.txt`).
- `results/`: the extracted feature tables (`features_*.csv`) and every result file. Table A5 of the paper maps each
  number quoted in the text to its script and result file.
- `paper/`: the LaTeX source of the paper.

The raw datasets are not included; the scripts read single files from DaRUS.

**Checking the files.** `SHA256SUMS` holds the SHA-256 checksums of every script and result file. In the root of the
unpacked deposit, `sha256sum -c SHA256SUMS` checks them all. The main result files:

| File | SHA-256 |
|---|---|
| `results/dec_intervals.csv` | `afebd27b3e14976b3e54daf17699f7e953a82bc895e30aa36580062277962092` |
| `results/dec_q95_reps.npy` | `bcd5fbfbf7ab100db3cf00460d840994966b8a4eff5da8a6e7cc71e58bb3f956` |
| `results/dec_resolution.csv` | `58f1970c5e6ee45e97ae58061230a862cedccad45957f38bfa74b4d0605fea49` |
| `results/panel_source_floor.csv` | `9b9d40ea51eb0654c23462e740d1d6df7022e7a2135397e5db6651e9cc3c20de` |
| `results/panel_guard_priors.csv` | `a4366a9ec1abad9acc714068e04ceebc131159e904cf89d96822606fa34a849c` |
| `results/panel_step6.csv` | `733329987119679ee1cfa8a2bf6c31d553abe9edb76432b53e215e6ad3ac6fef` |
| `results/rob_refit.csv` | `d244fb64230e75f18806e5716270e7355282e9108bc3d7573c8db195be3e6c18` |

**Licence and attribution.** For the licence of the code, see version 2. The feature tables and the result files are
derived from two datasets by S. Baum and P. Heinzelmann, both licensed under CC BY 4.0
(<https://creativecommons.org/licenses/by/4.0/>):

- the Real Deep Drawing and Cutting dataset (RDDAC), version 2.0, doi:10.18419/DARUS-5589;
- the Deep Drawing and Cutting Simulations dataset (DDACS), version 3.0, doi:10.18419/DARUS-4801.

They were changed by extracting quality characteristics from the scans and the simulations and computing the
statistics the paper describes.
