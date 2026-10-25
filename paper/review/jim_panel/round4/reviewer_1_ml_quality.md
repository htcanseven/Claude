# Referee report, fourth round: Reviewer 1

**Manuscript:** A production-referenced evaluation of design-stage decision rules in deep drawing: when can a prediction replace a physical trial?
**Journal:** Journal of Intelligent Manufacturing
**Round:** Fourth round (verification of the single-document, restyled version)
**Reviewer focus:** Machine learning for manufacturing quality: predictive quality and virtual metrology, learned manufacturability assessment, uncertainty quantification and conformal prediction, small-data and transfer learning
**Date:** 25 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary

- **Single document:** it works. Every statement in my area that cited an Online Resource table (S5–S12, S14, S15) now names a result file, and the 60-odd numbers I recomputed reproduce.
- **Regressions:** my round-3 points and D1–D10 hold, except D3's wording in the abstract.
- **Rewrite:** Sections 3.3, 5.4 and 5.5, the core of my area, are faithful and often clearer. Three passages shifted meaning (abstract, Section 6.1, Conclusion), and the count of simulated rounds is out of date. I add one older misstatement I missed in round 3.
- Every fix is one line, adds no length and needs no new analysis.

## 2. Regressions

| Item | Status | Where (`main_reviewed.pdf`) |
|---|---|---|
| Major 1 / C1 (my round-3 table): safety credited to borrowed evidence | Holds; blurred in 6.1 (must-fix 2) | p. 1, ll. 37–39; p. 21, ll. 934–938; p. 28, ll. 1276–1278 |
| Major 2 / C2: no guarantee; coverage detail | Holds | Table 2 note; p. 8, ll. 341–347; p. 21, ll. 939–947 |
| Major 3 / C3: M7n's intervals and priors; M7 | Holds | p. 7, ll. 316–319; p. 21, ll. 921–927 |
| Major 4 / C4, C9: decision-time bands; cross-fits | Holds | Table 7; p. 24, ll. 1068–1072 |
| Minor points 1, 3–11; adopted options (nested validation, "not from learning") | Hold | p. 8, ll. 346–348; p. 21, ll. 934, 942–950; p. 25, l. 1141; Table 7 note |
| D1 ranges | Holds | p. 21, ll. 941–942 |
| D2 guarantee; reason per relation | Holds; `level` labels and dictionary aligned | Table 2 note; p. 8, ll. 341–342 |
| D3 "closer than 30 floors" | Holds in 6.1 and 7, not in the abstract (must-fix 1) | p. 24, l. 1096; p. 28, l. 1271; p. 1, l. 40 |
| D4 grid-wide comparisons | Holds | p. 16, l. 734 – p. 17, l. 774 |
| D5 pooled shares | Holds | p. 21, ll. 958–959; Table 7 note |
| D6 force cell left out | Holds; prior now explicit | p. 22, ll. 992–998 |
| D7 costs under step 5 | Holds (`qual_cost_cheapest`) | p. 22, l. 1005 – p. 23, l. 1036 |
| D8 "once runs differ by a floor" | Holds | Table 8; p. 25, ll. 1143–1145; p. 28, ll. 1271–1273 |
| D9 Fig. 1 | Holds | p. 9, caption |
| D10 archive; Table 3; rounds | Holds; count now out of date (must-fix 4) | p. 14, l. 640; p. 29, l. 1314 |

## 3. Support after the Online Resource was removed

Each former citation now names a file in the same sentence or paragraph. I recomputed:

- **S5 → `learn_gp_diagnostics`** (p. 19, l. 868): M5n 92.9/95.2 % and 0.28; M7n 0.33–0.36, length scales 192–195 kN, nugget 0.43–0.51 floors against sampling errors of 0.13–0.14.
- **S6 → `learn_m7n_priors`** (l. 926): coverage 52.4/56.0 %, variants 47.6–61.9 %, distances within 1.40.
- **S7 → `learn_resolution`** (l. 935): 17.55, 17.80, 20.10; 151.3, 155.1; 2.75; NN+RM 19.50/0.00; M7n 14.50/5.15.
- **S8–S9 → `qual_coverage`** (ll. 942, 944): 88.1/92.9 %; 76.2–100 and 66.7–100 %; GP intervals 82.5–85.7 % (0.72–0.94); M3 96.0 % (0.929–0.984); "guaranteed" only on sibling rows.
- **S10–S11 → `qual_guard_decision`:** NN per family 97/93 % interpolating and 92/100 % extrapolating; worst characteristics 88.8, 88.3, 85.3 %; release-like, 139 of 1,753 decided, 0.748 right.
- **S10 → `qual_guard_oos`:** 0.718 and 0.7345 (release-like); 0.875 and 0.867.
- **S12 → `qual_guard_prior_width`** (p. 22, l. 992): NN's in-sample sibling band 0.25 at ±20 floors, 2.0 at ±5.
- **S14, S15:** `qual_between_run` (2.875, 4.0, 8.875 at τ = 3); `qual_crossfit` (18.15, 11.45; 0.924–0.971; 0.733).
- **Also:** `learn_fewshot` (5.90–10.50), `tune_decisions` (11.15, 13.05), `qual_guard_nested` (0.956/2.7 %, 0.952/52.1 %).

Two gaps, neither an error:

- The text names no file for the nested, few-shot and tuning results; only `findings.md` maps them.
- Table 7 no longer gives or points to the intervals of its shares, as S10 did. `qual_guard_decision` has them for the sibling (NN 0.936–0.971); its empty new-setting rows lack S10's reason (one held-out cell per family interpolating, two extrapolating).

## 4. The rewrite

### Meaning changes and errors

1. **Abstract, p. 1, l. 40.**
   - Old: "none closer than 30 floors". New: "none within 30 floors".
   - Mcd decides at exactly 30.00 floors (`learn_source_floor`), so "within", read inclusively, is false; D3 settled this wording.
   - *Fix:* restore "closer than". Pay for it by deleting "In recent years," (l. 23), which dates finite-element simulation to recent years (cf. p. 2, l. 50).
2. **Section 6.1, p. 24, ll. 1098–1103.**
   - Old: the opening "For this simulation dataset and for Gaussian processes and boosting fitted to six to nine alternatives" covered, in the same sentence, "the learners added no decisiveness, and what made rules safe …".
   - New: the opening stays with the simulation clause; a new sentence reads "The learners added no decisiveness, and what made the rules safe …".
   - The learner finding has lost its scope. "The rules" now takes in simulation-based centres, which the same interval does not make safe (p. 21, ll. 937–938).
   - *Fix:* "For this simulation dataset, the simulation contributed little … directly. GPs and boosting fitted to six to nine alternatives added no decisiveness, and what made the production record safe for new settings was …".
3. **Conclusion, p. 28, ll. 1279–1282.**
   - Old: "… within a family, which argues for indexing such records … rather than for a more elaborate model".
   - New: "Based on these findings, it is suggested to index production records … rather than to develop a more elaborate model."
   - "Suggest" takes no to-infinitive. "These findings" now include the cross-family one, where only simulation-based rules decided, and the sentence reads as advice against developing models, at odds with Section 6.3's next candidates.
   - *Fix:* "Within a design family, these findings argue for indexing production records by their relation to the coming design rather than for a more elaborate model; such a record is the baseline that a learned manufacturability check has to beat."

Both fixes are no longer than the text they replace. Items 1 and 3 came in with the fixes that followed the earlier check (commit 0fa69de). I compared the whole text with the previous version, sentence by sentence in Sections 3.3–3.7, 5.3–5.7, 6.1–6.3 and 7, and found no other change of meaning. Two of that check's repairs are right: "Under the same prior" (p. 22, l. 994) ties 0.72/0.73 to the release-like prior, and "200 draws of this component" (p. 24, l. 1064) holds at every τ (`qual_between_run`).

### Clarity

The rewrite helps where it defines s0, d and P_FA/P_FR/P_T (p. 7, l. 299; p. 8, l. 367; p. 6, l. 249), splits the semicolon chains of Section 5.4, says which verdicts Section 6.2's 41, 92 and "6 of 8" count (p. 25, ll. 1142–1143), and gives descriptive titles and captions.

It is harder to follow or padded in two ways:

- Connectives claim links that are not there. "Therefore" introduces a definition (p. 6, l. 232). A second "However" (p. 16, l. 720) and "On the other hand" (p. 22, l. 996) contrast nothing. "Thus" (p. 23, l. 1046) follows from Table 5, not from the preceding sentence.
- Repetition and stock phrases, whose deletion saves about four lines: "Thus, the floor is the α-quantile …", which restates Eq. (3) (p. 6, l. 266); "It should be noted that" (p. 7, l. 287; p. 12, l. 548); "It is important to note that" (p. 18, l. 815); "According to the table," (p. 16, l. 699); "As seen in the table," (p. 18, l. 805); "The computational details are as follows." (p. 15, l. 679).

## 5. Items

### Must fix

1. Abstract, l. 40: "none closer than 30 floors"; delete "In recent years," (l. 23).
2. Section 6.1, ll. 1098–1103: restore the scope of the learner finding (fix in my Section 4).
3. Conclusion, ll. 1279–1282: restore the within-family scope and correct the grammar (fix in my Section 4).
4. Simulated rounds: with this round, eight. Update the declaration (p. 29, l. 1314) and, unless it counts only rounds that added analyses, Section 4.5 (p. 14, l. 640), as D10 did.
5. Conclusion, p. 28, ll. 1275–1276 (pre-existing; I missed it in round 3): "GPs and boosting … reproduced the production record". Boosting fell short of it, at 11.2 and 13.1 floors against 3.4 and 8.5 (`tune_decisions`, `dec_resolution`). *Fix:* "did not improve on".

### Should fix

1. Rephrase the connectives listed in my Section 4.
2. In the Table 7 note, write "Shares per family, intervals, verdict counts …" and name `qual_guard_nested`; the note's last line has room.

### Optional

1. p. 19, l. 856: NN+RM, a rule without the simulation, needs 293 floors (Table 5), outside "130–135"; add "NN+RM 293".
2. p. 23, l. 1046: "every attainable distance" overlooks the trials (1.4 and 0.90 floors, Table 5); write "every design-stage distance".
3. Archive: `findings.md` (l. 14) still says 31 pages; the dictionary should explain the empty new-setting intervals of `qual_guard_decision`.

## 6. Recommendation

**Accept with minor corrections.**

Once must-fix items 1–3 restore the previous scope and wording, the paper's claims on learned rules and their intervals stand as before; items 4 and 5 replace one word each. The editor can check every item without the reviewers.

**Confidence:** high for Sections 3.3, 5.3–5.5, 6.1 and 7 and the archive checks; moderate for the forming and decision-support passages, which I read for meaning only.
