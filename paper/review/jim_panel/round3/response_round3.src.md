# Response to the editor, third round

**Manuscript:** "When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing", by Hüseyin Tayyer Canseven
**Journal:** Journal of Intelligent Manufacturing
**Answers:** the decision of 24 October 2026 (accept subject to the conditions: corrections D1–D10, three optional suggestions, conditions for acceptance) and the third-round reports of Reviewers 1, 2 and 3
**Revision of:** the version considered in the third round (frozen as `paper/review/jim_panel/round3/main_reviewed.tex`)

> **Note on this document.** The decision letter and the three reports it answers were written by AI agents acting as a simulated review panel; they do not come from the journal, its editors or its reviewers. The response is written as it would be to a real editor. Items that only the author can complete are marked **[author]**: the licence and the DOI of the archive.

**Locations.** Page and line numbers refer to the corrected manuscript, `paper/main.pdf`, compiled with line numbers; tables, captions and figures carry no line numbers and are named. Tables S1–S15 are those of `paper/online_resource_1.pdf`. The version marked up against the one you considered is `paper/review/jim_panel/round3/main_diff.pdf`.

**Length.** The paper still has {{totalpages}} pages, its main text ending on page {{mainpages}}; every addition is paid for in the same paragraph, as listed below.

**Archive.** The corrections change files in `scripts/` and `results/`. `SHA256SUMS` and the checksum table of `RELEASE_NOTES.md` (version 3, not yet deposited) are regenerated, and the release notes list the corrections. `python3 scripts/opchar.py --selfcheck` still reproduces every stored distance, the 40 new-setting guard bands and the worked example's cost band.

Dear Editor,

Thank you for checking every item yourself and for saying where the wording was yours. All ten corrections are made as specified, with no new data. Two needed computations from the stored results, both under rules the paper already states: the costs under step 5's rule (D7), and the shares per family of the decision-time bands (D5). A third comes from the optional suggestions: the sibling validation with strictly nested fits. No finding changes. Where a statement failed as written, the corrected one holds: the simulation finding now rests on comparisons that hold across the whole grid (D4), and the cost statements hold under step 5's rule (D7).

---

## Corrections D1–D10

**D1. Coverage ranges of NN+RM.** For a new setting the text now gives 76–100 % between the families and 67–100 % between characteristics {{loc:it ranges from 76 to 100}} (`qual_coverage.csv`).

**D2. Guarantees, and why errors are borrowed.**
- The Table 2 note now reads "guaranteed only with a sibling (largest residual, n = 8 calibration alternatives), whose held-out alternative is exchangeable with them; otherwise nominal".
- The S8 note says the levels for a new setting or family are nominal, and that with a single calibration family P+RM has no guarantee even if the families were exchangeable.
- `qualify.nominal_level` labels the levels the same way (`level` in `qual_coverage.csv`), and the data dictionary describes them.
- The reason for borrowing is given per relation, within the same lines: "a family's own calibration set has no case of its new-setting relation (with a sibling, for one construction)" {{loc:has no case of its new-setting relation}}. The added words are paid for by "Finally" and "in floors" in the sentence before.

**D3. The new family in Section 6.1.** The sentence now reads "decided at 3.4 floors with a sibling and 8.5 for a new setting, no rule closer than 30 floors for a new family" {{loc:no rule closer than 30 floors for a new family}}.

**D4. Comparisons independent of blank and scales.** Section 5.2 now rests on the three comparisons that hold "at every friction and thickness of the grid" {{loc:show it at every friction and thickness of the grid}}:
- the simulated force effect on the mid-side draw-in is 2.8–7.4 times the measured one;
- the concave arms bend downwards in 89–100 % of the simulations;
- the dome ranks the geometries in reverse in 76 % of the simulations {{loc:in reverse in 76}}.

The concave wall-angle trend is dropped. A new function, `simcheck.grid_comparisons` (`python3 simcheck.py --grid`; `sim_grid_comparisons.csv`), computes all of them. It reproduces your figures: 2.83–7.44, −1.93 to +1.68° for the wall angle (39 % within 0.5° of the measured change), and the signed dome reversed in 151 of 198 combinations. The S3 note and `findings.md` agree. The passage is shorter than before.

**D5. Table 7's shares for a new setting.**
- Section 5.5 now says the shares are "pooled over the two families (92–100 % per family)" {{loc:pooled over the two families (92--100 % per family)}}, paid for by the trial rates, which Table 7 gives.
- The Table 7 note says the shares are pooled.
- Table S10 gives every share per family under both priors, with the decided verdicts per family and the verdict totals. Its note says why there is no interval for a new setting: each family has one held-out cell interpolating and two extrapolating, whose alternatives share one fit.
- The per-family columns are new outputs of `qualify.guard_decision_time`. NN is right in 97/93 % interpolating and 92/100 % extrapolating (reference prior); under the release-like prior NN extrapolating decides 1 of 882 convex verdicts, as you noted.

**D6. The "force cell left out" scheme.**
- Section 5.5 now describes it as computed: "with a band estimated from both families' cases except the held-out force cell, the nearest setting and NN+RM reach 0.72 and 0.73 extrapolating, while interpolating, where only the other family's cell remains, M5 and M7n keep Table 7's 0.88 and 0.87" {{loc:with a band estimated from both families' cases except the held-out force cell}}.
- The Table S10 note, Section 5 of Online Resource 1 and the `scheme` entry of the data dictionary say the same.
- Table S12 is now cited at the start of the paragraph {{loc:The bands belong to the prior as much as to the rules}}, paid for by the trial rates there, which Table 7 gives.

**D7. Costs under step 5's rule.** Recomputed, the first of your two branches.
- **The recomputation.** `qualify.costs` searches each rule's cost-minimising band from its 95 % band up to 20 floors, and a rule without a 95 % band sends every design to trial. Fig. 6, Table S13, `qual_costs.csv` and `qual_cost_cheapest.csv` are recomputed.
- **Section 5.6** states the rule {{loc:each rule's band chosen as step 5 prescribes}}. Every statement holds under both priors and all three cost ratios:
  - the nearest setting or the force trend is cheapest for a new setting at every trial cost;
  - with a sibling the nearest setting is cheapest from a trial cost of a tenth of a false accept, and below that the cheapest rules differ by at most 0.003;
  - for a new family no rule qualifies, so every design goes to trial {{loc:For a new family no rule qualifies, so every design goes to trial}}.
- **The bands** keep the 95 % bands when trials are expensive and widen as trials get cheaper, the nearest setting's to 5–15 floors at a hundredth of a false accept {{loc:keep the 95 % bands when trials are expensive}}.
- **What changed.** The M0 exception and the sentence on minimising without the 95 % target are gone, which shortens the paragraph. Fig. 6's caption now says "bands of step 5".
- **Unchanged.** NN's whole cost with a sibling at c_T = 0.05 remains 0.018, and the worked example's band (2.5 widened to 5.0) was already computed under the rule.

**D8. Trial and release messages.**
- **Table 8's release-level row** now reads "once runs differ by a floor, confirming the index needs replicated runs, not a prediction or a short trial".
- **Section 6.2:**
  - "near release-level limits, once runs differed by a floor, neither a prediction nor a short trial confirmed capability" {{loc:once runs differed by a floor, neither a prediction nor a short trial}};
  - "under the release-like prior 41 and 92, getting 6 of the other 8 right" {{loc:getting 6 of the other 8 right}}.
  - Both are paid for in the same section, by removing "which needed replicated runs" and "pointing to the produced alternatives it averages".
- **Conclusions:** "once runs differed by a floor, confirming a performance index of 1.33 needed replicated runs" {{loc:once runs differed by a floor, confirming a performance index of 1.33}}. Paid for by removing "(the pre-specified M5 at 35)", which Section 5.3 and Table 5 keep.

**D9. Fig. 1 caption.** The caption now names "the in-sample pooled g" and stays within two lines.

**D10. Archive and details.**
- **Data dictionary:** the `transfer` row points to the floor codes (G*: the new family's own floor; G: the produced family's).
- **`findings.md`:** the strata read "1.60 when the produced siblings do not differ resolvably and 4.40 when they do", and the file carries D4–D8.
- **Table 3:** 17.7 (the generator now rounds 17.65 up, as Table S4 does).
- **Seven simulated rounds** in Section 4.5 {{loc:in seven rounds}} and in the declaration {{loc:manuscript in seven rounds}}. Section 7 of Online Resource 1 says what this round led to.

## Optional suggestions (adopted)

- **Nested sibling validation:** adopted in the Table 7 note. Refitting the band's cases without the held-out alternative, NN keeps 96 and 95 % correct and sends 3 and 52 % of the verdicts to trial under the two priors (`qualify.guard_nested_sibling`; `qual_guard_nested.csv`). This agrees with your 0.955/2.6 % and 0.952/52 % to within 0.1 percentage point.
- **c_FR in the worked example:** "a trial costs a twentieth and a false reject half of a false accept" {{loc:a trial costs a twentieth and a false reject half of a false accept}}.
- **"Not from learning":** adopted {{loc:not from learning}}.

## Conditions for acceptance

- **Licence: [author].** A `LICENSE` file for the code, and the licence fields of `.zenodo.json` and `CITATION.cff`. The data-derived files keep CC BY 4.0.
- **DOI and deposit: [author].** Deposit version 3 from the corrected commit (tag `v3`), then put the DOI in `paper/refs.bib`, `CITATION.cff` and the cover letter. `sha256sum -c SHA256SUMS` passes on this commit and will pass in the unpacked deposit.
- **Registration:** met by its second branch, as you ruled. The guard-band item of `paper/notes/frozen_procedure.md` is now aligned with step 5 and the decision-time scheme, in case it is deposited later.
- **Data dictionary:** in the deposit, corrected as D6 and D10 require.

## Numbers that changed

- **Section 5.4:** NN+RM's coverage ranges for a new setting, 76–100 % and 67–100 % (73–100 and 61–100 % before, from the sibling relation).
- **Section 5.2:** the force-effect ratio over the grid is 2.8–7.4 (2.7–5.1 before, at the nominal friction and over both draw-ins), and the dome is reversed in 76 % of the simulations; the wall-angle trend is removed.
- **Section 5.5:** NN+RM with the force cell left out, 0.73 (0.74 before).
- **Section 5.6, Fig. 6 and Table S13:**
  - with a sibling, NN is cheapest from a trial cost of a tenth of a false accept (a fifth before);
  - for a new family, a trial of every design at every trial cost (before, the cheapest rule changed with the prior);
  - the bands start at the 95 % band.
- **Table 3:** 17.7 (17.6 before).
- **New numbers:**
  - the per-family shares in Section 5.5 and Table S10;
  - the nested validation in the Table 7 note;
  - "6 of the other 8" in Section 6.2.
- **No distance, floor, coverage value or Table 7 band changed.**

With thanks to you and the three reviewers,

Hüseyin Tayyer Canseven
