#!/usr/bin/env bash
# Reproduce every analysis from the cached feature tables.
#
# Step 0 (feature extraction) streams the raw data from DaRUS and takes hours;
# it is skipped when the feature tables exist. Delete a table to re-extract it.
#   results/features_rddac.csv          9,000 parts       (features_rddac.py)
#   results/features_ddacs_rddac.csv    396 simulations   (features_ddacs.py --set rddac)
#   results/features_ddacs_corners.csv  264 simulations   (features_ddacs.py --set corners)
set -euo pipefail
cd "$(dirname "$0")"

[ -f ../results/features_rddac.csv ] || python3 features_rddac.py --workers 4
[ -f ../results/features_ddacs_rddac.csv ] || python3 features_ddacs.py --set rddac --workers 2
[ -f ../results/features_ddacs_corners.csv ] || python3 features_ddacs.py --set corners --workers 2

python3 alternatives.py      # production floor, effect-to-scatter, minimum resolvable change
python3 sensitivity.py       # floor under other batch sizes, quantiles and batch centres; drift share
python3 measurement.py       # scan redundancy, components of the floor, extraction noise of the simulations
python3 decisions.py         # design-stage decisions scored against production (all scopes and rules)
python3 guard.py             # applicability guards on new process settings and a new family
python3 scenarios.py         # verdicts against general angular tolerances (ISO 2768-1)
python3 budget.py            # decisions against the number and choice of calibration alternatives
python3 robustness.py        # data weaknesses, constants, GP specification, refitting bootstrap
python3 tuning.py            # learner and settings of the part-level rules M3 and M4
python3 design_space.py      # supplementary: DDACS corners, sensitivities, surrogate accuracy (not in the paper)
python3 inline.py            # supplementary: in-line verifiability from the force record (not in the paper)
python3 figs.py              # figures in the paper's style (results/figures)
python3 make_tables.py       # tables of paper/main.tex from the CSVs
