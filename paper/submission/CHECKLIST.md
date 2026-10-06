# Submission checklist

Research in Engineering Design, special collection *AI in Design for Manufacturing* (deadline 31 December 2026).
Manuscript: *Evaluating design-stage manufacturability decisions against the resolution of production*.

## Decisions only the author can take

- [ ] **Licence.** The code-availability statement says "released under an open licence", but the repository has no
      `LICENSE` file yet. Choose one (for example MIT or BSD-3-Clause for the code; CC BY 4.0 for the extracted
      feature tables, which derive from CC BY 4.0 data) and add it before archiving or submitting.
- [ ] **Zenodo DOI (needed before submission).** Connect the repository to Zenodo, create a release and insert the
      DOI where the manuscript says "[DOI pending]" (Code availability) and in the cover letter. Optionally rename
      the repository to a descriptive name and update the URL in the Code availability statement.
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
      marked-up comparison (`main_diff.pdf`). They are internal working documents and not part of the submission.

## Quality gates (last run on the final manuscript)

- [x] Pipeline results regenerated (`bash scripts/run_all.sh` or the individual scripts), tables written by
      `python scripts/make_tables.py`, figures copied from `results/figures/` to `paper/figures/`.
- [x] Single file, no supplementary material: `paper/main.tex` compiles with zero errors, no undefined references
      or citations and no overfull boxes; 30 pages in all, the main text (abstract to conclusions) ending on page
      23; six tables and four figures in the main text, two tables in the appendix; references from page 25.
- [x] Abstract 250 words; six keywords; captions of at most two lines; no first person; British spelling.
- [x] Every cited key (69) is in `refs.bib`; the references added in the revision were checked against the
      publisher, DBLP, Crossref or the ISO catalogue, and ISO standards are cited in their current editions.
- [x] Every number in the text checked against the result CSVs; tables are generated, not typed.
- [x] The upload zip (`bash paper/submission/make_zip.sh`: main.tex, fig_procedure.tex, refs.bib, class and style
      files, figures) compiles in an empty directory to the same 30 pages.
- [x] Cover letter (`cover_letter.md`) and outreach drafts updated from the final abstract and results.
