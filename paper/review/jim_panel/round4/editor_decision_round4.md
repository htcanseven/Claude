# Editorial decision, fourth round

**Manuscript:** "A production-referenced evaluation of design-stage decision rules in deep drawing: when can a prediction replace a physical trial?", by Hüseyin Tayyer Canseven (LUT University)

**Journal:** Journal of Intelligent Manufacturing (Springer)

**Version considered:** the restyled single-document version (`paper/review/jim_panel/round4/main_reviewed.pdf`, 33 pages, and its source), the version before the rewrite (`main_before_restyle.tex` and `.pdf`), and version 3 of the archive

**Reports considered:** Reviewer 1 (machine learning for manufacturing quality), Reviewer 2 (sheet-metal forming and quality engineering) and Reviewer 3 (industrial decision support), fourth-round reports dated 25 October 2026; all three recommend acceptance with minor corrections

**Date:** 25 October 2026

*Written by an AI agent in the persona of a fictional handling editor of a simulated review panel; it does not come from the journal or speak for any real person.*

---

## Decision

**Accept subject to corrections E1–E11 and the conditions.**

**What the version achieved.**
- The single document works. Every former citation of Online Resource 1 names a result file, every number the reviewers or I checked reproduces, and D1–D10 hold, except D3's wording in the abstract.
- The rewrite kept the substance. Against the earlier version, the source has the same numbers (one "500" is repeated from Fig. 4's caption), citations, named files and table values. Its definitions and its step-by-step example help readers.

**What it put at risk.**
- Meaning: six scopes, attributions or qualifiers moved (E1–E3, E5–E7).
- Support: the merge swapped two file pointers (E4) and dropped D5's reason for the missing intervals (E8).
- The deposit: the archive is now the only support, so the pending DOI bears on the paper itself.

**The must-fix items.** All six hold:

| Item | Reviewers | Correction |
|---|---|---|
| The abstract's "within 30 floors" | 1, 2, 3 | E1 |
| The Conclusion's scope and grammar | 1, 2, 3 | E3 |
| The scope of the learner finding in Section 6.1 | 1 | E2 |
| The number of simulated rounds | 1 | E10 |
| "Reproduced the production record" | 1 | E3 |
| The floor-component pointer | 2 | E4 |

**My checks of the archive** (all read-only). All 192 checksums and the 11 version-3 release-note hashes verify, and `opchar.py --selfcheck` reproduces every distance, the 40 guard bands and the example's cost band.

No correction needs new data or analysis, and none changes a finding. I will check E1–E11 myself; the paper does not go back to the reviewers. The corrected files are due by 8 November 2026, with one line per correction giving its location.

---

## Corrections required before acceptance

Pages and lines refer to `main_reviewed.pdf`.

**E1. Abstract** (Reviewers 1–3), p. 1, ll. 23 and 39–41.
- *Problem:* Mcd decides at exactly 30.00 floors (`learn_source_floor`; Table 5), so "none within 30 floors" is false.
- *Also new:* simulation is dated to "recent years" (compare p. 2, ll. 50–53), and "the baseline learned … checks" is a garden path.
- *Fix:*
  - "In recent years, simulation and machine learning have informed" → "Simulation and machine learning have informed";
  - "none within 30 floors" → "none closer than 30 floors" (D3's wording, as in Sections 6.1 and 7; Reviewer 3's "below" is also true);
  - "the baseline learned" → "the baseline that learned".
- *Length:* 250 → 249 words (the limit is 250).

**E2. Section 6.1** (Reviewer 1), p. 24, ll. 1098–1103.
- *Problem:* after the sentence split, "fitted to six to nine alternatives" qualifies the simulation. "What made the rules safe" also covers centres that the same borrowed interval leaves unsafe: false accepts reach 155.1 floors around M1s and 151.3 around M7 (`learn_resolution`).
- *Fix:*
  - "For this simulation dataset, and for GPs and boosting fitted to six to nine alternatives, the simulation" → "For this simulation dataset, the simulation";
  - "The learners added no decisiveness, and what made the rules safe" → "GPs and boosting fitted to six to nine alternatives added no decisiveness, and what made the production record safe" (as in the abstract).
- *Length:* three words shorter.

**E3. Conclusion** (Reviewers 1–3), p. 28, ll. 1275–1276 and 1279–1282.
- *Problem:* "it is suggested to index" is ungrammatical, and the recommendation has lost "within a family", though "these findings" include the new family, where only simulation-based rules decided.
- *Older:* "reproduced the production record" is false for boosting, which decides at best at 11.15 and 13.05 floors, against NN's 3.35 and 8.45 (`tune_decisions`, `dec_resolution`). I missed this in round 3.
- *Fix:*
  - "it is suggested to index production records by their relation … rather than to develop a more elaborate model. Within a design family, such a record" → "this study argues for indexing production records within a design family by their relation … rather than for a more elaborate model; such a record". Unlike "rather than developing", this is not advice against Section 6.3's candidates.
  - "reproduced" → "did not improve on".
- *Length:* two words more, which fit on the short l. 1278.

**E4. File pointers** (Reviewers 2 and 3), p. 7, l. 282; Table 4 note (p. 17, l. 750); p. 23, l. 1055.
- *Problem:* the merge replaced the citation of Table S4 (sources `meas_scan`, `panel_floor_protocol`, `sens_drift`) with `meas_floor`, whose σ_batch and σ_st give only 0.52–0.86 of the floors and which has no drift ratio.
- *Evidence:*
  - the per-geometry σb and σw of `panel_floor_protocol` reproduce every floor through Section 3.2's normal model to within 12 % (0.88–1.02);
  - the drift ratio is `drift_inflation` in `sens_drift` (2.08–4.49);
  - NN's 3.45, 4.45 and 5.75 floors at l. 1055 are in `qual_between_run`, not in `qual_between_run_trial`.
- *Fix:*
  - l. 282: "(`meas_floor`)" → "(`panel_floor_protocol`)";
  - l. 750: "σb, σw and the drift ratio in `meas_floor`" → "σb and σw in `panel_floor_protocol`, the drift ratio in `sens_drift`";
  - l. 1055: add `qual_between_run` to the pointer.
- *Length:* none; each change falls on a short line.

**E5. Section 5.2** (Reviewer 2; the wording was mine), p. 16, ll. 734–736, and p. 17, l. 770.
- *Problem:* only the force effect holds at every combination (ratio 2.83–7.44 in all 66). The concave arms bend downward in 89.4–100 % of the combinations and the dome is reversed in 76.3 % (`sim_grid_comparisons`). The enumeration makes my round-3 "hold across the grid" read as universal.
- *Fix (Reviewer 2's):* "This is shown at every friction and thickness of the grid by the three comparisons that … scanner. Firstly, the simulated" → "Three comparisons that … scanner show this (`sim_grid_comparisons`). Firstly, at every friction and thickness of the grid, the simulated".
- *Length:* the same; l. 792 has room.

**E6. Section 4.2** (Reviewers 2 and 3), p. 12, ll. 533–538.
- *Problem:* friction, a contact property, is attached to the blank's model, and depth, trimming and springback are stated as facts, not as documented, although p. 18, l. 797 tests a shorter depth.
- *Fix:* "and the blank is modeled by … with a scaled DP600 flow curve and constant Coulomb friction. The drawing depth is 30 mm, the trimming in OP20 is modeled without cutting tools, and springback is computed after" → "the blank is modeled by … with a scaled DP600 flow curve, and the contact uses constant Coulomb friction. It also gives a drawing depth of 30 mm, trimming in OP20 without modeled cutting tools, and springback after".
- *Length:* one word more, paid for by "It should be noted that" (l. 548, same paragraph).

**E7. Section 6.5** (Reviewers 2 and 3), p. 27, ll. 1232–1233.
- *Problem:* "the spread between teams of the share" misparses, and "within the safe distance" has been lost.
- *Fix:* "the spread between teams of the share of wrong verdicts accepted" → "the between-team spread of wrong acceptances within the safe distance", matching "right acceptances" just before.
- *Length:* five characters more, within l. 1233.

**E8. Intervals of the decision-time shares** (Reviewers 1 and 3), Table 7 note (p. 22, ll. 987–988); p. 25, l. 1141; `DATA_DICTIONARY.md`.
- *Problem:* D5's reason for the missing new-setting intervals left with S10. The dictionary promises an interval for every row, but `qual_guard_decision` has one only with a sibling (NN 0.936–0.971). "92 to 95 of the other 98" is 98 times that interval, and nothing in the paper now says so.
- *Fix:*
  - Table 7 note: "Shares per family, verdict counts" → "Shares per family, intervals, verdict counts";
  - l. 1141: "right." → "right (95 % interval).";
  - the `share_correct` row adds "with a sibling only; none for a new setting, where each family has one held-out cell interpolating and two extrapolating, whose alternatives share one fit".
- *Length:* four words more, on lines with room; "Moreover," at l. 1143 can go.

**E9. Older misstatements** (Reviewer 1; the second is mine). Each fix falls on a line with room.
- p. 19, l. 856: NN+RM needs 293 floors (Table 5; `learn_source_floor`). "(130–135 floors)" → "(130–135 floors; NN+RM 293)".
- p. 21, l. 937: the borrowed interval leaves M1s and M7 unsafe, but it makes M5 safe at 2.15 floors when extrapolating (`learn_resolution`). "around simulation-based centers" → "around the centers of M1s and M7".
- p. 23, l. 1046: the within-run trials of Table 5 decide at 1.35 and 0.90 floors, on which D8 rests. "every attainable distance" → "every design-stage distance".

**E10. Simulated rounds** (Reviewers 1 and 2), p. 14, l. 640; p. 15, l. 673; p. 29, l. 1314.
- *Fix:* "seven rounds" → "eight rounds" in both places; l. 673: "were added." → "were added; the eighth added no analysis."
- *Length:* five words more, on the short l. 678.

**E11. Archive** (Reviewers 1–3).
- `DATA_DICTIONARY.md`: the `meas_floor` row ("components of the floor: sigma_b, sigma_w"), the `panel_floor_protocol` and `sens_drift` rows as E4 requires, and the `share_correct` row as E8 requires.
- `findings.md`, l. 14, should give 33 pages, and `paper/submission/CHECKLIST.md`, l. 89, should end the main text on p. 28.
- Then regenerate `SHA256SUMS` and list these corrections in `RELEASE_NOTES.md`.

---

## Optional suggestions

The author's choice; one line of the response covers them.
- **File names.** Where a line has room, name files that only `findings.md` now maps, such as `sim_mc_friction` (p. 18, l. 783), `qual_trial_cost` (p. 23, l. 1040) and `qual_release_capability` (l. 1051).
- **Table notes** (Reviewer 2): in Table 9, "(Table 4, Section 5.1)", since the lag is in Section 5.1; in the Table 3 note, "per series in `meas_scan`".
- **Wording** (Reviewers 2 and 3): "M5 and M7n decide only at 6.8–7.2 floors but are safe below one floor" (p. 18, ll. 810–811); "41 of the sibling and 92 of the extrapolated verdicts" (p. 25, l. 1142).
- **Section 6.5** (Reviewer 3; optional in round 3 too). Base re-qualification on false accepts among accepted designs, and call the 150-verdict test one-sided.

## Items I reject

- **Rephrasing the connectives** (Reviewer 1; Reviewer 3's count of "However"). Each holds: "Therefore" (l. 232) follows from the requirement on a share p; ll. 720 and 996 mark real contrasts (within- against between-run variation; interpolating against extrapolating); "Thus" (l. 1046) follows from the 1.75 floors read against Table 5. Their number is style.
- **"The draw-ins" → "the mid-side draw-in"** (Reviewer 2). With M5 and M7, the simulation does help the corner draw-in when extrapolating: 5.7 against 14.6 floors and 9.4 against 12.3 (`qual_per_characteristic`).

---

## Length

- **Accepted.** 33 pages: the main text ends on p. 28 (l. 1286), the declarations on p. 29, and the references fill pp. 29–33. That is two pages more than in round 3, within the author's cap; JIM has no page limit, and the extra pages hold prose, not content.
- **The corrections add no line.** The paper must keep 33 pages, with the main text ending on p. 28.
- **The filler lines need not be cut.** They are the author's style, not errors, and the reserve if a compiled line overflows, in this order:
  - "It should be noted that" (p. 7, l. 287);
  - "It is important to note that" (p. 18, l. 815);
  - "According to the table," (p. 16, l. 699) and "As seen in the table," (p. 18, l. 805);
  - "The computational details are as follows." (p. 15, l. 679);
  - the restated floor definition in the Conclusion (p. 28, ll. 1260–1262).

## The number of simulated rounds

Section 4.5 and the declaration count rounds of simulated reviews, not rounds that added analyses. This round produced three reports and this letter, so it is the eighth, as D10 counted the seventh: both places say eight, and Section 4.5 says that the eighth added no analysis (E10), which keeps its list complete. My check of E1–E11 belongs to this round, not to a ninth.

## Conditions for acceptance

Actions for the author outside the manuscript, as in round 3.

- **Licence.** Still no `LICENSE` file, and no licence field in `.zenodo.json` or `CITATION.cff`. Add a code licence; the data-derived files keep CC BY 4.0, with the attribution in `README.md`.
- **DOI and deposit.** `paper/refs.bib` still reads "[DOI pending]"; the metadata carry the reordered title. Deposit version 3 from the corrected commit and cite the minted DOI in `refs.bib`, `CITATION.cff` and the cover letter. After E11, `sha256sum -c SHA256SUMS` must pass in the unpacked deposit, which I must be able to open.
- **Registration.** Met by its second branch, as in round 3.
- **Data dictionary.** The deposited dictionary must be corrected as E4, E8 and E11 require.

Yours sincerely,

Handling editor (a fictional persona in a simulated review panel), Journal of Intelligent Manufacturing
