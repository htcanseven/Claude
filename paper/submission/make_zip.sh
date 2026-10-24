#!/usr/bin/env bash
# Build the upload zip (Overleaf / editorial system) with the manuscript and its Online Resource 1 and prove that both
# compile in an empty directory.
# Usage: bash paper/submission/make_zip.sh   -> paper/submission/manuscript_source.zip
set -euo pipefail
cd "$(dirname "$0")/.."                       # paper/
TMP=$(mktemp -d)
cp main.tex online_resource_1.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst "$TMP"/
mkdir -p "$TMP/figures"
for f in $(grep -o '\\includegraphics\[[^]]*\]{[^}]*}' main.tex | sed 's/.*{\(.*\)}/\1/' | sort -u); do
  cp "figures/$f.pdf" "$TMP/figures/"
done
for doc in main online_resource_1; do
  ( cd "$TMP" && latexmk -pdf -interaction=nonstopmode -halt-on-error "$doc.tex" > "build_$doc.log" 2>&1 ) || {
    echo "clean-directory build of $doc.tex FAILED; see $TMP/build_$doc.log"; exit 1; }
  grep -q "undefined" "$TMP/$doc.log" && { echo "undefined references in the clean build of $doc.tex"; exit 1; } || true
done
PAGES=$(pdfinfo "$TMP/main.pdf" | awk '/Pages/ {print $2}')
OR_PAGES=$(pdfinfo "$TMP/online_resource_1.pdf" | awk '/Pages/ {print $2}')
( cd "$TMP" && rm -f build_*.log ./*.aux ./*.bbl ./*.blg ./*.fdb_latexmk ./*.fls ./*.log ./*.out ./*.pdf \
    && zip -qr manuscript_source.zip main.tex online_resource_1.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst figures )
mv "$TMP/manuscript_source.zip" submission/
echo "ok: submission/manuscript_source.zip ($(unzip -l submission/manuscript_source.zip | tail -1 | awk '{print $2}') files),"\
     "clean build: $PAGES pages, Online Resource 1: $OR_PAGES pages"
rm -rf "$TMP"
# the archive must be cited with its DOI before the final upload
if grep -q '\\pending{DOI}' refs.bib; then
  echo "WARNING: refs.bib still cites the archive DOI as pending (canseven2026archive); insert the DOI before uploading."
fi
