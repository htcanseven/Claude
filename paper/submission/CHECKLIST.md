# Submission checklist

*Journal of Intelligent Manufacturing* (Springer; JUFO level 2). Manuscript: *A production-referenced evaluation of
design-stage decision rules in deep drawing: when can a prediction replace a physical trial?* (first prepared as
*Evaluating AI-based manufacturability decisions against the resolution of production*).

**Status.** The manuscript was revised after a simulated first review round at JIM (three reviewers and an editor,
all AI agents; `paper/review/jim_panel/round1/`): new title and abstract (249 words), decision-time strata, a
small-data learner (M7n), multi-fidelity and discrepancy models, relation-matched intervals, guard bands per family
and out of sample, costs, a between-run sensitivity, results per characteristic and a measurement subsection. It was
then shortened to 31 pages without an appendix, and revised after a simulated second round
(`paper/review/jim_panel/round2/`, C1–C11): guard bands available when deciding, the release question as a capability
decision, the trial under between-run variation, consistent costs and a reworked worked example. At the author's request the paper is a single document without
supplementary material: the tables behind its statements are archived result files, `results/findings.md` maps
every number of the paper to its script and result file, and `results/DATA_DICTIONARY.md` explains the files.
A simulated third round (`paper/review/jim_panel/round3/`) accepted it subject to conditions, and its corrections
D1–D10 are made (`response_round3.md`). At the author's request, the prose was then rewritten in the style of the
author's earlier papers, with American spelling and the title reordered (`paper/notes/style_profile.md`); no number
changed, and the paper has 33 pages, within the two pages over 31 that the author allowed. A simulated fourth round
(`paper/review/jim_panel/round4/`) verified this version and accepted it subject to corrections E1–E11, which are
made (`response_round4.md`); none changes a number. The archive is version 3. Because the reviews were simulated, this version
goes to the journal as a first submission; the response letters and the marked-up versions are internal documents.

**Journal requirements** (submission guidelines): abstract 150–250 words; 4–6 keywords; author–year citations;
declarations (funding, competing interests, data availability) before the references; LaTeX with the Springer Nature
template accepted; no page limit. The corresponding author must give an ORCID in the submission system.

## Archive and DOI (the author's steps, in this order)

1. **Licence.** Choose one and add it:
   - a `LICENSE` file in the repository root, for example MIT or BSD-3-Clause for the code;
   - the same licence in `.zenodo.json`, as `"license": "<id>"` (Zenodo's identifier, for example `"mit"` or
     `"cc-by-4.0"`), and in `CITATION.cff`, as `license: <SPDX id>`, for example `MIT`.

   The feature tables and result files derive from RDDAC and DDACS, which are licensed under CC BY 4.0. The
   attribution that licence requires (the creators, the licence and the changes made) is already in `README.md` and
   `RELEASE_NOTES.md`. Commit.
2. **Checksums.** Rerun `bash scripts/write_checksums.sh` only if anything in `scripts/` or `results/` changed after
   this package. If it did, update the table in `RELEASE_NOTES.md` from `SHA256SUMS`. Commit and push.
3. **Deposit**, either way:
   - *GitHub release.* The Zenodo GitHub integration needs a public repository. Switch the repository on under
     Zenodo → Settings → GitHub. Create a GitHub release from the final commit, with tag `v3`, title "Version 3" and
     `RELEASE_NOTES.md` as its description. Zenodo reads `.zenodo.json` and mints the DOI. The deposited paper
     source then still shows the DOI as pending; the code and results are identical.
   - *Manual upload with a reserved DOI.* Start a new upload on Zenodo and reserve its DOI. Do steps 4 and 5 first,
     then upload `git archive --format=zip -o claude-v3.zip HEAD` from the final commit, fill in the metadata from
     `.zenodo.json` and publish.
4. **Insert the DOI** (`10.5281/zenodo.NNNNNNN`):
   - `paper/refs.bib`, entry `canseven2026archive`: replace `note = {\pending{DOI}}` by
     `doi = {10.5281/zenodo.NNNNNNN}`;
   - `CITATION.cff`: add `doi: 10.5281/zenodo.NNNNNNN`;
   - `paper/submission/cover_letter.md`: replace "[DOI to be inserted]".
5. **Rebuild** the paper (`latexmk -pdf main.tex` in `paper/`; 33 pages) and the upload zip
   (`bash paper/submission/make_zip.sh`, which builds it in a clean directory and warns while the DOI is still
   pending).
6. **Check** that the DOI resolves and that `sha256sum -c SHA256SUMS` passes in the unpacked deposit.

## Submission

- [ ] **Files.** Upload the LaTeX source (`manuscript_source.zip`) with the compiled PDF (`paper/main.pdf`); the
      journal requires the editable source files. There is no electronic supplementary material.
- [ ] **Registration.** The paper names a confirmatory test of the procedure, registered before the analysis, as an
      extension, and no longer calls the procedure frozen. To cite a registration, deposit
      `paper/notes/frozen_procedure.md` with a timestamp (for example on OSF Registries) before any confirmatory data
      are analysed.
- [ ] **Dataset providers.** Send the request in `note_to_dataset_authors.md` if you wish; the paper does not depend
      on the answer.
- [ ] **Cover letter.** `cover_letter.md`, written for JIM. Insert the DOI.
- [ ] **ORCID**, required for the corresponding author; check the Funding declaration ("No specific funding").
- [ ] **Affiliation.** Check the department line of the author block in `paper/main.tex`.
- [ ] **Suggested reviewers**, if the system asks. Possible candidates among the authors of cited work, after you
      have checked for conflicts of interest:
  - H. Tercan and T. Meisen (predictive quality in manufacturing);
  - Y. F. Zhao (reproducibility and reuse of ML-based process monitoring);
  - J.-Y. Dantan and A. Siadat (conformal prediction for quality assurance);
  - D. F. Benoit (manufacturability datasets for sheet metal).
- [ ] **Line numbers.** Keep the class option `lineno` for review; remove it for production after acceptance.
- [ ] **Internal review documents.** `paper/review/` holds simulated reviews, all written by AI agents: the review
      panel for the RED collection in `paper/review/cfp_panel/` and the simulated JIM rounds in
      `paper/review/jim_panel/`. They are internal working documents and not part of the submission. Section
      4.5 and the declaration on generative AI cover them.
- [ ] **ISO editions.** The paper cites ISO 5725-2:2025 and ISO 22514-2:2026, the current editions according to ISO's
      catalogue data. If you worked from the 2019 and 2017 texts, cite those instead (`iso2025repeatability`,
      `iso2026process` in `paper/refs.bib`).
- [ ] **Outreach drafts.** `presubmission_enquiry.md` was written for the RED guest editors and is obsolete;
      `note_to_dataset_authors.md` can still be sent to the RDDAC/DDACS authors.

## Quality gates (last run after the fourth-round corrections)

- [x] `paper/main.tex` compiles with zero errors, no undefined references or citations and no overfull boxes. The
      paper has 33 pages: the main text (abstract to conclusion) ends on page 28, the declarations follow on
      page 29, and the references fill pages 29–33, with DOIs as full links. Nine tables and six figures; no
      appendix and no supplementary material.
- [x] Abstract 249 words (247 when "95 %" counts as one word), within the journal's limit; six keywords; captions of
      at most two lines; no first person; American spelling, as in the author's earlier papers.
- [x] Every cited key is in `refs.bib`; the references were checked against the publisher, DBLP, Crossref or the ISO
      catalogue, those added for JIM (Friedman 2001 and Barber et al. 2021 in the second round) against Crossref.
- [x] Every number in the text checked against the result CSVs; tables are generated, not
      typed; `python3 scripts/opchar.py --selfcheck` reproduces the stored distances and the new-setting guard bands.
      The numbers that changed in the second-round revision are listed in `paper/review/jim_panel/round2/response_round2.md`.
- [x] The upload zip (`bash paper/submission/make_zip.sh`: main.tex, fig_procedure.tex, refs.bib, class and style
      files, figures) compiles in an empty directory to the same 33 pages.
