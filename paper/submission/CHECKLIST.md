# Submission checklist

Research in Engineering Design, special collection *AI in Design for Manufacturing* (deadline 31 December 2026).
Manuscript: *Evaluating design-stage manufacturability decisions against the resolution of production*.

**Status.** The simulated review panel (AI agents, `paper/review/cfp_panel/round3/`) accepted the paper in principle,
subject to C1–C7. C2–C7 and the editorial corrections are in the manuscript. C1, the archive and its DOI, is the
author's step below. Abstract: 250 words by a strict count (`0.05 mm` and `500 kN` as two words each), the journal's
limit.

## C1: licence, archive and DOI (the author's steps, in this order)

1. **Licence.** Choose one and add it:
   - a `LICENSE` file in the repository root, for example MIT or BSD-3-Clause for the code;
   - the same licence in `.zenodo.json`, as `"license": "<id>"` (Zenodo's identifier, for example `"mit"` or
     `"cc-by-4.0"`), and in `CITATION.cff`, as `license: <SPDX id>`, for example `MIT`.

   The feature tables and result files derive from RDDAC and DDACS, which are licensed under CC BY 4.0. The
   attribution that licence requires (the creators, the licence and the changes made) is already in `README.md` and
   `RELEASE_NOTES.md`. Then replace "[licence to be named by the author]" in
   `paper/review/cfp_panel/round3/response_round3.src.md`. Commit.
2. **Checksums.** Rerun `bash scripts/write_checksums.sh` only if anything in `scripts/` or `results/` changed after
   this package. If it did, update the table in `RELEASE_NOTES.md` from `SHA256SUMS`. Commit and push.
3. **Deposit**, either way:
   - *GitHub release.* The Zenodo GitHub integration needs a public repository. Switch the repository on under
     Zenodo → Settings → GitHub. Create a GitHub release from the final commit, with tag `v4`, title "Version 4:
     final version of the paper" and `RELEASE_NOTES.md` as its description. Zenodo reads `.zenodo.json` and mints
     the DOI. The deposited paper source then still shows the DOI as pending; the code and results are identical.
   - *Manual upload with a reserved DOI.* Start a new upload on Zenodo and reserve its DOI. Do steps 4 and 5 first,
     then upload `git archive --format=zip -o claude-v4.zip HEAD` from the final commit, fill in the metadata from
     `.zenodo.json` and publish.
4. **Insert the DOI** (`10.5281/zenodo.NNNNNNN`):
   - `paper/refs.bib`, entry `canseven2026archive`: replace `note = {\pending{DOI}}` by
     `doi = {10.5281/zenodo.NNNNNNN}`;
   - `CITATION.cff`: add `doi: 10.5281/zenodo.NNNNNNN`;
   - `paper/review/cfp_panel/round3/response_round3.src.md` and `cover_letter_final.md`: replace
     "[DOI to be inserted after deposit]";
   - `paper/submission/cover_letter.md`: replace "[DOI to be inserted after deposit]".
5. **Rebuild.**
   - The paper: `latexmk -pdf main.tex` in `paper/`. Check that it still has 30 pages and that the main text ends at
     the top of page 24.
   - The response: `python paper/review/cfp_panel/round3/resolve_locations.py`.
   - The upload zip: `bash paper/submission/make_zip.sh`. It warns while the DOI is still pending.
6. **Check** that the DOI resolves and that `sha256sum -c SHA256SUMS` passes in the unpacked deposit.

## Final version for the (simulated) guest editor

Per the decision letter, the final version is due by 20 October 2026. It consists of:

- the clean manuscript, `paper/main.pdf`, with line numbers kept for the editor's check, and its source zip;
- the marked-up version, `paper/review/cfp_panel/round3/main_diff.pdf`, against the third-round manuscript;
- the short response, `paper/review/cfp_panel/round3/response_round3.md`, generated from `response_round3.src.md`;
- the transmittal letter, `paper/review/cfp_panel/round3/cover_letter_final.md`.

## Submission to the journal

- [ ] **Cover letter.** `cover_letter.md` is written for the submission to RED. Insert the DOI.
- [ ] **ORCID and funding** in the editorial system; check the Funding declaration ("No specific funding").
- [ ] **Affiliation.** Check the department line of the author block in `paper/main.tex`.
- [ ] **Outreach.** Send (or not) the drafts in this folder: `presubmission_enquiry.md` (guest editor) and
      `note_to_dataset_authors.md` (RDDAC/DDACS authors). If sent, wait for the answers before submitting. The dataset
      authors' answers on tolerances, repeat scans, scanning order and run dates could change Sections 4.1, 4.3, 5.8
      and 6.6.
- [ ] **Blinded copy.** If the system asks for one, set `\anontrue` in `paper/main.tex`.
- [ ] **Line numbers.** Keep the class option `lineno` for review; remove it for production after acceptance.
- [ ] **Internal review documents.** `paper/review/` holds simulated reviews, all written by AI agents:
  - a three-referee review of the first version;
  - in `paper/review/cfp_panel/`, a review panel for the collection (three reviewers and a guest editor) over three
    rounds, with the responses and marked-up comparisons;
  - in `round3/`, the decision to accept in principle and the final response.

  They are internal working documents and not part of the submission. The manuscript's declaration on generative
  AI covers them.
- [ ] **ISO editions.** The paper cites ISO 5725-2:2025 and ISO 22514-2:2026, the current editions according to ISO's
      catalogue data. If you worked from the 2019 and 2017 texts, cite those instead (`iso2025repeatability`,
      `iso2026process` in `paper/refs.bib`).

## Quality gates (last run on the final manuscript)

- [x] Pipeline results regenerated, tables written by `python scripts/make_tables.py`, and figures copied from
      `results/figures/` to `paper/figures/`. Since the third round only `panel_guard_priors.csv` changed: two columns
      were added (`RELEASE_NOTES.md`).
- [x] Single file with no supplementary material. `paper/main.tex` compiles with zero errors, no undefined references
      or citations and no overfull boxes. The paper has 30 pages, and the main text (abstract to conclusions) ends at
      the top of page 24, after the conclusions were extended by eight lines. The main text has six tables and four
      figures; the appendix has five tables. Tables A1 and A2 share page 25, a float page (placement `[p]`, set at
      7.5 pt by `\tabsizesmall`; Table A2's placement and size are written by `make_tables.py`). References start on
      page 27.
- [x] Abstract within 250 words; six keywords; captions of at most two lines; no first person; British spelling.
- [x] Every cited key is in `refs.bib`. The references were checked against the publisher, DBLP, Crossref or the ISO
      catalogue.
- [x] Every number in the text checked against the result CSVs; tables are generated, not typed.
- [x] The upload zip (`bash paper/submission/make_zip.sh`: main.tex, fig_procedure.tex, refs.bib, class and style
      files, figures) compiles in an empty directory to the same 30 pages.
- [x] Response to the third-round decision with page and line numbers resolved from the compiled PDF; marked-up
      version against the third-round manuscript (abstract marked; tables, captions and Fig. 1 shown in their new
      form).
