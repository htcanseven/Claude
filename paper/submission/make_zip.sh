#!/usr/bin/env bash
# Build the upload zip (Overleaf / editorial system) with the manuscript and its Electronic Supplementary Material, and
# prove that both compile in an empty directory. The ESM reads the paper's labels from main.aux, so main.tex is built first.
# Usage: bash paper/submission/make_zip.sh   -> paper/submission/manuscript_source.zip, paper/submission/esm.pdf
set -euo pipefail
cd "$(dirname "$0")/.."                       # paper/
TMP=$(mktemp -d)
cp main.tex esm.tex esm_labels.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst "$TMP"/
mkdir -p "$TMP/figures"
for f in $(cat main.tex esm.tex | grep -o '\\includegraphics\[[^]]*\]{[^}]*}' | sed 's/.*{\(.*\)}/\1/' | sort -u); do
  cp "figures/$f.pdf" "$TMP/figures/"
done
for doc in main esm; do
  ( cd "$TMP" && latexmk -pdf -interaction=nonstopmode -halt-on-error "$doc.tex" > "build_$doc.log" 2>&1 ) || {
    echo "clean-directory build of $doc.tex FAILED; see $TMP/build_$doc.log"; exit 1; }
  grep -q "undefined" "$TMP/$doc.log" && { echo "undefined references in the clean build of $doc.tex"; exit 1; } || true
done
cp "$TMP/esm.pdf" submission/esm.pdf
( cd "$TMP" && rm -f build_*.log ./*.aux ./*.bbl ./*.blg ./*.fdb_latexmk ./*.fls ./*.log ./*.out \
    && zip -qr manuscript_source.zip main.tex esm.tex esm_labels.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst figures )
mv "$TMP/manuscript_source.zip" submission/
echo "ok: submission/manuscript_source.zip ($(unzip -l submission/manuscript_source.zip | tail -1 | awk '{print $2}') files),"\
     "clean build: main $(pdfinfo "$TMP/main.pdf" | awk '/Pages/ {print $2}') pages, ESM $(pdfinfo "$TMP/esm.pdf" | awk '/Pages/ {print $2}') pages"
rm -rf "$TMP"
