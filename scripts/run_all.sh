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
python3 decisions.py         # design-stage decisions scored against production
python3 design_space.py      # DDACS corners: sensitivities, surrogate accuracy
python3 inline.py            # in-line verifiability from the force record
python3 figs.py              # figures in the paper's style (results/figures)
