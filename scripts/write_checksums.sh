#!/usr/bin/env bash
# Write SHA256SUMS in the repository root: the SHA-256 checksums of every tracked script and result file, so that a
# deposited release can be checked against the files the paper's numbers come from. Run it after the last change to
# scripts/ or results/ and commit the file with them.
# Usage: bash scripts/write_checksums.sh
# Check: sha256sum -c SHA256SUMS   (in the root of the repository or of the unpacked deposit)
set -euo pipefail
cd "$(dirname "$0")/.."
git ls-files scripts results requirements.txt | LC_ALL=C sort | xargs -d '\n' sha256sum > SHA256SUMS
echo "SHA256SUMS: $(wc -l < SHA256SUMS) files"
