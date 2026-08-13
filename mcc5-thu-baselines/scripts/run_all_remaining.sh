#!/usr/bin/env bash
# Everything still outstanding, in one idempotent chain.
#
# Every stage either resumes or is cheap to repeat, so after a container restart
# this script can simply be re-run: completed work is skipped, not redone.
#
# Usage: scripts/run_all_remaining.sh <data-dir> [out-dir]
set -u
DATA="${1:?usage: run_all_remaining.sh <data-dir> [out-dir]}"
OUT="${2:-results}"
cd "$(dirname "$0")/.."
mkdir -p "$OUT" logs

say() { echo "=== $* $(date -u +%H:%M:%S) ==="; }

# 1. Benchmark campaign (each stage resumes).
say "campaign start"
bash scripts/run_full_campaign.sh "$DATA" "$OUT"
say "campaign done"

# 2. Late fusion, feature-space models, both compound protocols, 3 seeds.
say "late_fusion(rf) start"
python3 scripts/late_fusion.py --data-dir "$DATA" --out "$OUT" --seeds 0 1 2 \
  --resume --protocols compositional_zeroshot leave_combination_out \
  2>&1 | tee logs/late_fusion_rf.log
say "late_fusion(rf) done"

# 3. The combination experiment: per-modality CNNs with superposition.
say "late_fusion(cnn) start"
python3 scripts/late_fusion_cnn.py --data-dir "$DATA" --out "$OUT" \
  --seeds 0 1 --epochs 15 --resume \
  --protocols compositional_zeroshot leave_combination_out \
  2>&1 | tee -a logs/late_fusion_cnn.log
say "late_fusion(cnn) done"

# 4. Regenerate every derived artifact from the CSVs.
say "artifacts start"
python3 scripts/make_tables.py  --out "$OUT" --paper paper
python3 scripts/make_stats.py   --out "$OUT" --paper paper
python3 scripts/make_figures.py --out "$OUT" --data-dir "$DATA" \
  --figs paper/figures
say "artifacts done"

# 5. Shareable package.
say "package start"
bash scripts/make_package.sh /home/user/Claude/mcc5-thu-share
say "package done"

echo "ALL REMAINING WORK COMPLETE $(date -u +%H:%M:%S)"
