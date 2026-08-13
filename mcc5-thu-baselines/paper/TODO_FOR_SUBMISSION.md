# Remaining human tasks before submission

The manuscript is complete and compiles cleanly (16 pages, zero errors, zero
undefined citations): `paper/manuscript/main.pdf`, source in
`paper/manuscript/`. Everything below needs a human decision or an account
login, which is why it is still open.

## Must do (blocking submission)

1. **Move the source into the official IEEE Access template.** The
   reconstruction compiles with the IEEEtran journal class as a stand-in.
   Download the IEEE Access LaTeX template from the author portal, copy
   `sections/`, `refs.bib`, and `figures/` across, and transplant the
   `\author`/`\thanks` block into the template's front-matter macros. The
   section files are template-agnostic; this is ~30 minutes of mechanical
   work.
2. **Replace the extracted figures with the originals.** `figures/fig1..fig5`
   were extracted from the PDF at their embedded resolution (all ≥550 dpi, so
   they are print-quality, but the originals are cleaner). Evin has the
   source files. The two biography photos likewise.
3. **Verify the six reference entries whose author lists I reconstructed**
   from the draft's rendered reference list rather than from publisher
   records: `ltssbow2024`, `decoupling_attn2020`, `hemtan2024`, `kbs2025`,
   `neuro2025`, `appac2025`, plus the full-name expansions in `wang2024`,
   `drmnn2020`, `plos2025`, `multilevel2019` (initials were expanded to
   likely full names; IEEE style prints initials, so errors here are latent
   but worth 15 minutes against the DOIs).
4. **Both authors read the Abstract, Introduction, and Conclusion.** They
   are new text written tonight in Evin's register, quoting only numbers
   from her tables — but the claims are made in your names.
5. **ORCID iDs and final author metadata** in the submission portal.

## Should do (strongly recommended)

6. **Decide code availability.** The manuscript currently says "available on
   reasonable request", with a commented Zenodo alternative. For a paper
   whose subject is evaluation reliability, a public repository + Zenodo DOI
   is materially stronger and reviewers increasingly expect it. The complete
   suite is ready in this repository.
7. **Professional language pass.** The body is consistent but has two
   authorial voices; a single native-speaker pass smooths it.
8. **Graphical abstract** (IEEE Access requires one at submission): Figure 1
   (the regime graph) or Figure 4 (within-pair vs transfer) cropped works
   well; needs a one-sentence caption.
9. **Run a plagiarism/similarity self-check** — Sections III–IV share
   phrasing with the earlier standalone draft, which is fine (same
   manuscript lineage), but check nothing overlaps the Data in Brief
   descriptor's phrasing.

## Nice to have

10. Cover letter (offer: I can draft one on request — two paragraphs:
    cross-modal compound regime + prior-aware evaluation).
11. Suggested reviewers list (people publishing on zero-shot compound
    diagnosis and leakage-aware evaluation are natural picks; avoid the
    dataset authors — conflict).
12. Consider citing the arXiv/preprint of `gama2025` explicitly if the MSSP
    article number (114640) has not yet been assigned an issue.

## Already done tonight (no action needed)

- All placeholder sections written (Abstract, Index Terms, Introduction,
  Conclusion, Data/Code Availability).
- Appendix A added: the operating-condition reference experiments that back
  Section II's saturation claim, with verified multi-seed numbers.
- Reference [20] duplicate replaced with Wang et al.; [1] year/caps fixed;
  [14] journal added (MSSP); [16] journal added (ISA Transactions); [18]
  issue year corrected to 2024; [33] volume 65 added; dataset DOI added as
  [34] and cited from Data Availability.
- Section II fixes applied: "Several research threads", "bearing–bearing or
  bearing–gear", Appendix cross-reference replacing the dangling
  "companion benchmark experiments" claim.
- Figures and biography photos extracted and placed; compile verified page
  by page.
