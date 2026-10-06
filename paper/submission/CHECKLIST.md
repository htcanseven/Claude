# Submission checklist

Research in Engineering Design, special collection *AI in Design for Manufacturing* (deadline 31 December 2026).
Manuscript: *Evaluating design-stage manufacturability decisions against the resolution of production*.

## Decisions only the author can take

- [ ] **Licence.** The code-availability statement says "released under an open licence", but the repository has no
      `LICENSE` file yet. Choose one (for example MIT or BSD-3-Clause for the code; CC BY 4.0 for the extracted
      feature tables, which derive from CC BY 4.0 data) and add it before archiving or submitting.
- [ ] **Zenodo DOI (a condition of acceptance; needed before resubmission).** The guest editor will check the
      revision against the archive, so the release must hold exactly the code and result files of this version.
      1. Add the `LICENSE` file (above) and commit.
      2. Connect the GitHub repository to Zenodo (Zenodo → Settings → GitHub → switch the repository on).
         `.zenodo.json` in the repository root supplies the title, version 3, description, keywords and the two
         source datasets; add your ORCID there if you want it in the record.
      3. Create a GitHub release from the final commit, tag `v3`, title "Version 3: revision for the second-round
         decision". Zenodo then mints the DOI.
      4. In `paper/refs.bib`, entry `canseven2026archive`, replace `note = {\pending{DOI}}` by `doi = {10.5281/…}`;
         rebuild the paper (`latexmk -pdf main.tex` in `paper/`) and the upload zip (`bash
         paper/submission/make_zip.sh`).
      5. Replace "[DOI to be inserted after deposit]" in
         `paper/review/cfp_panel/round2/response_round2.src.md` (then run `python
         paper/review/cfp_panel/round2/resolve_locations.py`) and "[DOI to be inserted]" in `cover_letter.md`.
      Because the DOI changes `refs.bib` after the release, either cut the release after step 4 (a second release
      is then version 3.1 with the final PDF) or accept that the archived PDF shows the DOI as pending; the code and
      results are identical either way.
- [ ] **ORCID and funding** in the editorial system; check the Funding declaration ("No specific funding").
- [ ] **Affiliation.** Check the department line of the author block in `paper/main.tex`.
- [ ] **Outreach.** Send (or not) the drafts in this folder: `presubmission_enquiry.md` (guest editor) and
      `note_to_dataset_authors.md` (RDDAC/DDACS authors). If sent, wait for the answers before submitting; the
      dataset authors' answers on tolerances, repeat scans, scanning order and run dates could change Sections 4.1,
      4.3, 5.8 and 6.6.
- [ ] **Blinded copy.** If the system asks for one, set `\anontrue` in `paper/main.tex`.
- [ ] **Line numbers.** The review copy is compiled with line numbers (class option `lineno`); remove the option for
      the final version.
- [ ] **Internal review documents.** `paper/review/` holds two simulated reviews, both written by AI agents: a
      three-referee review of the first version and, in `paper/review/cfp_panel/`, a review panel for the
      collection (three reviewers and a guest editor) with the response to it (`response_to_panel.md`) and a
      marked-up comparison (`main_diff.pdf`). Its second round is in `paper/review/cfp_panel/round2/`: the reports,
      the decision (minor revision), the response with page and line numbers (`response_round2.md`, generated from
      `response_round2.src.md`) and the comparison with the second-round version (`main_diff.pdf`). They are
      internal working documents and not part of the submission.
- [ ] **ISO editions.** The paper cites ISO 5725-2:2025 and ISO 22514-2:2026, the current editions according to
      ISO's catalogue data. The panel asked to cite the editions consulted; if you worked from the 2019 and 2017
      texts, cite those instead (`iso2025repeatability`, `iso2026process` in `paper/refs.bib`).

## Quality gates (last run on the final manuscript)

- [x] Pipeline results regenerated (`bash scripts/run_all.sh` or the individual scripts), tables written by
      `python scripts/make_tables.py`, figures copied from `results/figures/` to `paper/figures/`.
- [x] Single file, no supplementary material: `paper/main.tex` compiles with zero errors, no undefined references
      or citations and no overfull boxes; 30 pages in all, the main text (abstract to conclusions) ending on page
      23; six tables and four figures in the main text, five tables in the appendix (notation, robustness, interval
      rules, step 6, mapping of numbers to result files); references from page 28.
- [x] Abstract 249 words; six keywords; captions of at most two lines; no first person; British spelling.
- [x] Every cited key (63) is in `refs.bib`; the references added in the revision were checked against the
      publisher, DBLP, Crossref or the ISO catalogue, and ISO standards are cited in their current editions.
- [x] Every number in the text checked against the result CSVs; tables are generated, not typed.
- [x] The upload zip (`bash paper/submission/make_zip.sh`: main.tex, fig_procedure.tex, refs.bib, class and style
      files, figures) compiles in an empty directory to the same 30 pages.
- [x] Cover letter (`cover_letter.md`) and outreach drafts updated from the final abstract and results.
