#!/usr/bin/env bash
# Build the upload zip (Overleaf / editorial system) and prove it compiles in an empty directory.
# Usage: bash paper/submission/make_zip.sh   -> paper/submission/manuscript_source.zip
set -euo pipefail
cd "$(dirname "$0")/.."                       # paper/
TMP=$(mktemp -d)
cp main.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst "$TMP"/
mkdir -p "$TMP/figures"
for f in $(grep -o '\\includegraphics\[[^]]*\]{[^}]*}' main.tex | sed 's/.*{\(.*\)}/\1/'); do
  cp "figures/$f.pdf" "$TMP/figures/"
done
( cd "$TMP" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex > build.log 2>&1 ) || {
  echo "clean-directory build FAILED; see $TMP/build.log"; exit 1; }
grep -q "undefined" "$TMP/main.log" && { echo "undefined references in the clean build"; exit 1; } || true
( cd "$TMP" && rm -f build.log main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out \
    && zip -qr manuscript_source.zip main.tex fig_procedure.tex refs.bib sn-jnl.cls sn-basic.bst figures )
mv "$TMP/manuscript_source.zip" submission/
echo "ok: submission/manuscript_source.zip ($(unzip -l submission/manuscript_source.zip | tail -1 | awk '{print $2}') files),"\
     "clean build $(pdfinfo "$TMP/main.pdf" | awk '/Pages/ {print $2}') pages"
rm -rf "$TMP"
