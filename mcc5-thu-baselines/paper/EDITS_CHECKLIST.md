# Final edits checklist — merged manuscript

Companion to `remaining_sections.tex`, which supplies the Abstract, Index
Terms, Introduction, Conclusion, Appendix A, and Data/Code Availability.
The items below are line-level fixes still open in the current version
(the one whose Section IV ends with the classifier-family analysis).

## Blocking (visible errors)

1. **Reference [20] duplicates [18].** Both currently resolve to Liu, Li, He,
   "Evidential ensemble preference-guided learning…," TII 20(4):5495–5504.
   [20] should be:
   > L. Wang, Y. Gao, X. Li, and L. Gao, "Self-supervised-enabled open-set
   > cross-domain fault diagnosis method for rotating machinery," IEEE
   > Transactions on Industrial Informatics, vol. 20, no. 8,
   > pp. 10314–10324, 2024.
   As it stands, "other groups applied condition-robust architectures to the
   companion gearbox release [20], [21]" cites the dataset authors' own paper
   as "other groups."

2. **Section II, lost phrase.** "constituents are homogeneous: bearing gear
   combinations" should read "constituents are homogeneous:
   bearing--bearing or bearing--gear combinations". The bearing–bearing case
   matters: the dataset's one mechanical-only compound is bearing–bearing.

3. **Section II opening.** "Four research threads intersect…" precedes six
   topical paragraph groups now that subsections are removed. Suggested:
   "Several research threads intersect in this study: compound-fault
   decoupling, zero-shot recognition of unseen fault combinations, the
   reliability of evaluation protocols, generalization across operating
   conditions, multimodal motor diagnosis, and the benchmark datasets that
   underpin them."

4. **Section II forward reference now resolvable.** The sentence "Our
   companion benchmark experiments on this dataset show that protocol to be
   nearly saturated…" should now cite Appendix A:
   "(Appendix~\ref{app:condition})" — the appendix in
   `remaining_sections.tex` supplies the experiments and table backing the
   ~3-point vs >60-point claim.

## Reference-list corrections

5. [1] "Ieee Access" → "IEEE Access"; year should be 2019 (vol. 7 issue year;
   2018 was online-first).
6. [14] Vieira et al. is missing its journal name (renders as "p. 114640,
   2026"); confirm the journal field (Mechanical Systems and Signal
   Processing, art. 114640) is present in the .bib.
7. [16] Zhao et al. is missing its journal (ISA Transactions, vol. 107,
   pp. 224–255, 2020).
8. [18] (and corrected [20]) year: vol. 20 is 2024, not 2023.
9. [33] add volume 65 to the Data in Brief entry; protect "{Data in Brief}"
   capitalization in [32].
10. Add the dataset DOI entry (Mendeley Data, 10.17632/6s3dggj9mw.1, CC BY
    4.0) — it is cited by the new Data Availability statement
    (`\cite{mcc5motor_data}`); the entry exists in `references.bib` in this
    directory.

## Consistency checks after inserting the new sections

11. Label names: the new sections reference `\label{sec:related}` (II),
    `\label{sec:methods}` (III), `\label{sec:results}` (IV),
    `\label{sec:conclusion}` (V), `\label{app:condition}` (Appendix A).
    Ensure those labels exist on the corresponding sections (add them if the
    template currently has none).
12. The Introduction's contribution list cites Sections III–IV and
    Appendix A only through those labels — no numbers are hard-coded.
13. Appendix A introduces one table (`tab:condref`). If the editor prefers
    appendix tables numbered separately (A.1), IEEEtran handles this
    automatically under `\appendices`.
14. The new Data Availability statement replaces the currently empty DATA
    AVAILABILITY heading; the Code Availability text keeps the
    "upon reasonable request" policy but a commented alternative recommends
    a Zenodo DOI — worth deciding before submission, since the paper's
    subject is evaluation reliability.
15. Abstract length is ~250 words (IEEE Access guidance ≤250) — if the
    editor trims, cut the sentence on threshold/classifier analyses last.

## Numbers used in the new sections (all verified against the current body)

| Claim | Source in body |
|---|---|
| closed-set 0.913, CI [0.885, 0.938] | Table 2 |
| EM 0.083–0.157; micro-F1 0.631–0.686; recall 0.630–0.694 | Table 3 |
| floors: micro-F1 0.556, EM 0.111, R_any 1.000, R_all 0.111 | Table 4 |
| interaction +0.040 [0.009, 0.073]; recall +0.051; R_all +0.083 | IV-C |
| ≥1 constituent recovered in >92% of runs | Table 3 (R_any) |
| F0.5 thresholds: EM 0.157–0.287, FA/run 0.222–0.389 | IV-D |
| classifier families: FA/run ~0.68 → ~0.26; recall 0.659–0.669 | Table 5 |
| reversal Holm p = 0.0136 / 0.0108 | IV-G |
| recording control AUC 0.998; same-date AUCs 0.972–1.000 | IV-G |
| Appendix A table and statistics | released benchmark CSVs (multi-seed) |
