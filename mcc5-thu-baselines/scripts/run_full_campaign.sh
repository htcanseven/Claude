#!/usr/bin/env bash
# Full benchmark campaign, run sequentially so each stage gets all cores.
#
# Usage: scripts/run_full_campaign.sh <data-dir> [out-dir]
set -u
DATA="${1:?usage: run_full_campaign.sh <data-dir> [out-dir]}"
OUT="${2:-results}"
cd "$(dirname "$0")/.."
mkdir -p "$OUT" logs

stage() {
  local name="$1"; shift
  echo "=== STAGE $name  $(date -u +%H:%M:%S) ==="
  python3 scripts/run_benchmark.py --data-dir "$DATA" --out "$OUT" "$@" \
    2>&1 | tee "logs/$name.log"
  echo "=== STAGE $name done  $(date -u +%H:%M:%S) ==="
}

# Multi-seed multiclass sweep: the headline protocol table.
stage rf_multiclass --model rf --features plain --seeds 0 1 2 \
  --protocols leaky_random in_condition unknown_condition cross_profile \
              single_source steady_to_transitional

# Multi-label protocols are ~10x costlier (15 one-vs-rest fits), so fewer seeds.
stage rf_multilabel --model rf --features plain --seeds 0 1 \
  --protocols compositional_control leave_combination_out \
              compositional_zeroshot

# A second, differently-biased feature-space model for cross-model agreement.
stage svm --model svm --features plain --seeds 0 \
  --protocols leaky_random in_condition unknown_condition cross_profile \
              single_source steady_to_transitional

# Physics-feature ablation: do speed-invariant order features help where
# condition shift bites hardest?
stage rf_order --model rf --features plain+order --seeds 0 1 2 \
  --protocols in_condition unknown_condition cross_profile single_source \
              steady_to_transitional
stage rf_order_ml --model rf --features plain+order --seeds 0 \
  --protocols compositional_control leave_combination_out \
              compositional_zeroshot

# Deep baseline, plus test-time noise robustness at several SNRs.
stage cnn --model cnn --seeds 0 --epochs 10 --max-condition-folds 3 \
  --noise-snr 20 10 0 \
  --protocols leaky_random in_condition unknown_condition cross_profile \
              single_source steady_to_transitional
stage cnn_ml --model cnn --seeds 0 --epochs 10 \
  --protocols compositional_control leave_combination_out \
              compositional_zeroshot

echo "ALL STAGES COMPLETE $(date -u +%H:%M:%S)"
