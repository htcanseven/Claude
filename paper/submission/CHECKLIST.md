# Submission checklist

Research in Engineering Design, special collection *AI in Design for Manufacturing* (deadline 31 December 2026).

## Decisions only the author can take

- [ ] **Licence.** The code-availability statement says "released under an open licence", but the repository has no
      `LICENSE` file yet. Choose one (for example MIT or BSD-3-Clause for the code; CC BY 4.0 for the extracted
      feature tables, which derive from CC BY 4.0 data) and add it before archiving.
- [ ] **Zenodo DOI.** Connect the GitHub repository to Zenodo, create a release (tag), and put the DOI into the
      Code availability statement of `paper/main.tex` and into `CITATION.cff`.
- [ ] **ORCID and funding** in the editorial system; check the Funding declaration.
- [ ] **Outreach.** Send (or not) the drafts in this folder: `presubmission_enquiry.md` (guest editor) and
      `note_to_dataset_authors.md` (RDDAC/DDACS authors). Wait for their answers before the final revision if sent.
- [ ] **Blinded copy.** If the system asks for one, set `\anontrue` in `paper/main.tex`.

## Quality gates (run before every delivery; see METHODOLOGY.md on the earlier branch)

- [ ] `bash scripts/run_all.sh` then `python scripts/make_tables.py`; copy the figures from `results/figures/` to
      `paper/figures/`.
- [ ] `latexmk -pdf main.tex` in `paper/`: zero errors, no undefined references or citations, no overfull boxes;
      `pdffonts main.pdf` shows all fonts embedded.
- [ ] Abstract 150–250 words; 4–6 keywords; captions of at most two lines; no first person; British spelling.
- [ ] Every cited key in `refs.bib`; every reference verified against Crossref or DataCite.
- [ ] The Overleaf zip (main.tex, class and style files, refs.bib, figures, fig_procedure.tex) compiles in an empty
      directory.
- [ ] Cover letter (`cover_letter.md`) updated from the final abstract and contributions.
