#!/usr/bin/env bash
# Build a self-contained folder (and archive) of code + results for sharing.
#
# Excludes the dataset (~13 GB) and the window cache (~2 GB): both are
# regenerable with the two commands printed in the package guide, and neither
# is ours to redistribute.
#
# Usage: scripts/make_package.sh [dest-dir]
set -eu
cd "$(dirname "$0")/.."
DEST="${1:-/home/user/Claude/mcc5-thu-share}"
NAME="mcc5-thu-benchmark"
PKG="$DEST/$NAME"

rm -rf "$PKG"
mkdir -p "$PKG"

# ---- code -----------------------------------------------------------------
cp -r src "$PKG/src"
cp -r scripts "$PKG/scripts"
cp requirements.txt README.md "$PKG/"
# the orientation document for a reader opening this cold
cp PACKAGE_GUIDE.md "$PKG/START_HERE.md"
find "$PKG" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
find "$PKG" -name '*.pyc' -delete 2>/dev/null || true

# ---- results --------------------------------------------------------------
mkdir -p "$PKG/results"
# aggregate metrics, per-component breakdowns, and the written findings
for pat in 'bench_*.csv' 'components_*.csv' 'compound_*.csv' \
           'feature_baseline*.csv' 'cnn_baseline*.csv' 'proposed*.csv' \
           'SUMMARY.md' 'FINDINGS.md'; do
  find results -maxdepth 1 -name "$pat" -exec cp {} "$PKG/results/" \; \
    2>/dev/null || true
done
# a few representative confusion matrices (the full set is ~100 files)
mkdir -p "$PKG/results/confusion_matrices"
for f in results/cm_in_condition_* results/cm_steady_to_transitional_* \
         results/cm_leaky_random_* results/cm_cross_profile_*; do
  [ -e "$f" ] && cp "$f" "$PKG/results/confusion_matrices/" || true
done

# ---- paper ----------------------------------------------------------------
mkdir -p "$PKG/paper"
cp -r paper/. "$PKG/paper/" 2>/dev/null || true

echo "package tree:"
find "$PKG" -maxdepth 2 -type d | sort | sed 's|^|  |'
echo
echo "file counts:"
printf '  code:    %s\n' "$(find "$PKG/src" "$PKG/scripts" -type f | wc -l)"
printf '  results: %s\n' "$(find "$PKG/results" -type f | wc -l)"
printf '  paper:   %s\n' "$(find "$PKG/paper" -type f | wc -l)"

# ---- archive --------------------------------------------------------------
cd "$DEST"
tar -czf "$NAME.tar.gz" "$NAME"
if command -v zip >/dev/null 2>&1; then
  zip -qr "$NAME.zip" "$NAME"
fi
echo
echo "archives:"
ls -lh "$DEST" | grep -E "$NAME\.(tar\.gz|zip)" | sed 's|^|  |'
echo
echo "folder: $PKG"
