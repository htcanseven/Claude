# Release notes

Code, feature tables and result files of the paper *When can a prediction replace a physical trial? A
production-referenced evaluation of design-stage decision rules in deep drawing* (H. T. Canseven), first submitted
as *Evaluating AI-based manufacturability decisions against the resolution of production*.

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
