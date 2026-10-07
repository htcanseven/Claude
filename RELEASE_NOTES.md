# Release notes

Code, feature tables and result files of the paper *Evaluating design-stage manufacturability decisions against the
resolution of production* (H. T. Canseven; Research in Engineering Design, special collection "AI in Design for
Manufacturing").

## Version 4 (October 2026): final version of the paper

Version 4 holds exactly the code, feature tables and result files that produce the numbers of the final version of
the paper, which answers the third-round decision of 6 October 2026. It is the first deposited version: version 3 was
prepared for the second revision but not deposited.

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

**Changes since the version reviewed in the third round** (repository commit `18930d0`, 6 October 2026):

- `results/panel_guard_priors.csv` gained two columns, `trial_10_uncapped` and `trial_20_uncapped`. They hold the
  trial shares of step 6 when the guard band is not capped at 20 floors, which Section 3.6 of the paper cites. The
  other five columns are unchanged: without the two new columns the file is byte-identical to the third-round file,
  whose SHA-256 is `fa1d032f1e68d381147228f1a1f37ec1ba4afd060c3434efe279011cff8c1366`. To check, run in the root of
  the deposit (pandas 3.0.6, as in `requirements.txt`):

  ```
  python3 -c "import pandas as pd, hashlib; d = pd.read_csv('results/panel_guard_priors.csv').drop(columns=['trial_10_uncapped', 'trial_20_uncapped']); print(hashlib.sha256(d.to_csv(index=False).encode()).hexdigest())"
  ```

- `results/summary_panel.md` shows the two new columns.
- `scripts/panel.py` writes the two columns. `scripts/make_tables.py` writes the new rows of the paper's Tables 4
  and A2: intervals for M1 and the force trend M1sn, and the refit intervals of the safe distances. It also sets
  Tables A2–A4 on float pages, at 7 pt, with Tables A3 and A4 at the full text width.
- `scripts/write_checksums.sh` writes `SHA256SUMS`.
- Every other result file is byte-identical to the third-round version.

**Licence and attribution.** For the licence of the code, see `LICENSE`. The feature tables and the result files are
derived from two datasets by S. Baum and P. Heinzelmann, both licensed under CC BY 4.0
(<https://creativecommons.org/licenses/by/4.0/>):

- the Real Deep Drawing and Cutting dataset (RDDAC), version 2.0, doi:10.18419/DARUS-5589;
- the Deep Drawing and Cutting Simulations dataset (DDACS), version 3.0, doi:10.18419/DARUS-4801.

They were changed by extracting quality characteristics from the scans and the simulations and computing the
statistics the paper describes.
