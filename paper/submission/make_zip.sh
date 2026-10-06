#!/usr/bin/env bash
# Build the upload zip (Overleaf / editorial system) with the single-file manuscript and prove that it compiles in an
# empty directory.
# Usage: bash paper/submission/make_zip.sh   -> paper/submission/manuscript_source.zip
set -euo pipefail
cd "$(dirname "$0")/.."                       # paper/
TMP=$(mktemp -d)
cp main.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst "$TMP"/
mkdir -p "$TMP/figures"
for f in $(grep -o '\\includegraphics\[[^]]*\]{[^}]*}' main.tex | sed 's/.*{\(.*\)}/\1/' | sort -u); do
  cp "figures/$f.pdf" "$TMP/figures/"
done
( cd "$TMP" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex > build_main.log 2>&1 ) || {
  echo "clean-directory build of main.tex FAILED; see $TMP/build_main.log"; exit 1; }
grep -q "undefined" "$TMP/main.log" && { echo "undefined references in the clean build of main.tex"; exit 1; } || true
PAGES=$(pdfinfo "$TMP/main.pdf" | awk '/Pages/ {print $2}')
( cd "$TMP" && rm -f build_*.log ./*.aux ./*.bbl ./*.blg ./*.fdb_latexmk ./*.fls ./*.log ./*.out ./*.pdf \
    && zip -qr manuscript_source.zip main.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst figures )
mv "$TMP/manuscript_source.zip" submission/
echo "ok: submission/manuscript_source.zip ($(unzip -l submission/manuscript_source.zip | tail -1 | awk '{print $2}') files),"\
     "clean build: $PAGES pages"
rm -rf "$TMP"
