#!/usr/bin/env bash
# Reproduce every table and figure of the paper from the feature caches (see features.py / features_wfsg.py
# for the extraction from the raw public data). Run from the repository root.
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH=scripts
export PAPER_FIGS=1          # figures without in-figure titles (the captions carry them)
for s in compare sensor_suites compare3 sensitivity revision figs_paper; do
  echo "== $s $(date -u +%H:%M:%S)"
  python3 "scripts/$s.py" > "results/run_$s.log" 2>&1
done
python3 scripts/make_tables.py > results/run_make_tables.log 2>&1 || echo "make_tables failed (see results/run_make_tables.log)"
cp results/figures/*.pdf paper/figures/
echo "== done $(date -u +%H:%M:%S)   (then: cd paper && latexmk -pdf main.tex && latexmk -pdf esm.tex)"
