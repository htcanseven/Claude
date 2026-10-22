# Release notes

Code, feature tables and result files of the paper *Evaluating AI-based manufacturability decisions against the
resolution of production* (H. T. Canseven).

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

**Licence and attribution.** For the licence of the code, see `LICENSE`. The feature tables and the result files are
derived from two datasets by S. Baum and P. Heinzelmann, both licensed under CC BY 4.0
(<https://creativecommons.org/licenses/by/4.0/>):

- the Real Deep Drawing and Cutting dataset (RDDAC), version 2.0, doi:10.18419/DARUS-5589;
- the Deep Drawing and Cutting Simulations dataset (DDACS), version 3.0, doi:10.18419/DARUS-4801.

They were changed by extracting quality characteristics from the scans and the simulations and computing the
statistics the paper describes.
