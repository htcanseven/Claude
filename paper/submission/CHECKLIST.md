# Submission checklist

Research in Engineering Design, special collection *AI in Design for Manufacturing* (deadline 31 December 2026).
Manuscript: *Evaluating design-stage manufacturability decisions against the resolution of production*.

## Decisions only the author can take

- [ ] **Licence.** The code-availability statement says "released under an open licence", but the repository has no
      `LICENSE` file yet. Choose one (for example MIT or BSD-3-Clause for the code; CC BY 4.0 for the extracted
      feature tables, which derive from CC BY 4.0 data) and add it before archiving or submitting.
- [ ] **Repository name and Zenodo DOI.** Optionally rename the repository to a descriptive name (the manuscript cites
      `https://github.com/htcanseven/Claude`; update the URL in the Code availability statement if renamed). Connect
      the repository to Zenodo and create a release; the manuscript promises the DOI at acceptance.
- [ ] **ORCID and funding** in the editorial system; check the Funding declaration ("No specific funding").
- [ ] **Affiliation.** Check the department line of the author block in `paper/main.tex`.
- [ ] **Outreach.** Send (or not) the drafts in this folder: `presubmission_enquiry.md` (guest editor) and
      `note_to_dataset_authors.md` (RDDAC/DDACS authors). If sent, wait for the answers before submitting; the
      dataset authors' answers on tolerances, repeat scans and run dates could change Sections 4.3, 5.8 and 6.6.
- [ ] **Blinded copy.** If the system asks for one, set `\anontrue` in `paper/main.tex`.
- [ ] **Internal review documents.** `paper/review/` holds a simulated three-referee review of the first version and
      the response to it. They are internal working documents and are not part of the submission.

## Quality gates (last run on the final manuscript)

- [x] Pipeline results regenerated (`bash scripts/run_all.sh`, about four hours on four cores), tables written by
      `python scripts/make_tables.py`, figures copied from `results/figures/` to `paper/figures/`.
- [x] `paper/main.tex` compiles: zero errors, no undefined references or citations, no overfull boxes, 38 pages;
      `pdffonts main.pdf` shows every font embedded.
- [x] Abstract 250 words; six keywords; captions of at most two lines; no first person; British spelling.
- [x] Every cited key (92) is in `refs.bib`; references were checked against Crossref, DataCite or the publisher.
- [x] Every number in the results text checked against the result CSVs; tables are generated, not typed.
- [x] The upload zip (`bash paper/submission/make_zip.sh`: main.tex, class and style files, refs.bib, figures,
      fig_procedure.tex) compiles in an empty directory.
- [x] Cover letter (`cover_letter.md`) and outreach drafts updated from the final abstract and results.
