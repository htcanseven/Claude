# Referee report, fourth round: Reviewer 3

**Manuscript:** A production-referenced evaluation of design-stage decision rules in deep drawing: when can a prediction replace a physical trial?
**Journal:** Journal of Intelligent Manufacturing
**Round:** Fourth round (verification of the single-document, restyled version)
**Reviewer focus:** Industrial decision support: decisions under uncertainty, cost-aware decisions, human–AI collaboration and trust, and the deployment of AI tools in factories
**Date:** 25 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary

The rewrite keeps the substance of my area. Steps 5 and 6, the worked example, Table 7, the costs under step 5's rule, the trial and release conditions, Table 8 and Section 6.5 say what they said before. Every number I checked reproduces.

The archive verifies: 192 of 192 checksums, and `opchar.py --selfcheck` reproduces the distances, the 40 new-setting bands and the example's cost band. Compared as multisets, the old and new texts contain the same numbers.

Two slips need fixing:

- the abstract now says no new-family rule decides "within 30 floors", but Mcd decides at exactly 30;
- the Conclusion's recommendation has lost its within-family scope, and its grammar is wrong.

Removing the Online Resource left a few statements without a named file or without their explanation. `findings.md` covers all of them.

## 2. Regressions

| Item | Status | Where |
|---|---|---|
| Step 5 (own band, one alternative left out, borrow or trial, costs only widen) | Holds; "such as interpolation" now fits Table 7 better | p. 10, L422–441 |
| Step 6, pseudocode | Holds | p. 10, L442–450 |
| Worked example (C5) | Holds; reproduces from `qual_worked_example` | pp. 10–11, L453–495 |
| D5 shares per family | Holds; S10's interval rationale lost (Section 3) | p. 21, L958–959; p. 22, L983–988 |
| D6 force cell out | Holds; the added "Under the same prior" is correct | p. 22, L994–998 |
| D7 costs under step 5 | Holds; all statements reproduce | pp. 22–23, L1005–1036 |
| D8 trial and release | Holds in all three places | p. 25, L1126–1127, L1142–1145; p. 28, L1271–1273 |
| D9 Fig. 1 | Holds | p. 9, L382–383 |
| D3 new family | Holds in Sections 6.1 and 7; **regressed in the abstract** | p. 1, L039–040 |
| D1, D2, D10; my round-3 minors | Hold | e.g. L338–342, L939–942, L1264, L1070–1072 |
| My round-3 optional 4 | Not adopted | p. 27, L1220–1224 |
| Length (editor: text to p. 27, 31 pages) | p. 28 and 33 pages, the author's cap; for the editor to confirm | – |

## 3. Support after the Online Resource was removed

Each citation of an S-table became one file name. All checks were read-only.

**S10 and S11, now `qual_guard_decision`** (Table 7 note; L965). The file holds the per-family shares, the decided counts and the characteristics. Confirmed:
- NN per family 0.924–0.998, and 0.954 (0.936–0.971) with a sibling;
- release-like, extrapolated: 139 of 1,753 decided, 0.748 correct (convex: 1 of 882);
- worst characteristics 0.888, 0.883 and 0.853.

Two things left with S10:
- **Why the new-setting shares have no interval**, which D5 required: one held-out cell per family when interpolating and two when extrapolating, with every alternative of a cell sharing one fit. The dictionary's `share_correct_lo, share_correct_hi` row promises a cluster interval, yet the file has none outside the sibling relation.
- **The label of the interval at L1141.** "92 to 95 of the other 98" is 98 × 0.936–0.971. A reader who sees "95" in Table 7 cannot reconstruct it.

**Other files:**
- `qual_guard_oos` (L998): 0.718 and 0.7345 extrapolated, 0.875 and 0.867 interpolated, all release-like. Confirmed.
- `qual_guard_prior_width` (L992): from a prior of ±3 to one of ±50 floors, NN's band falls from 8.0 to 0 with a sibling and from 14.75 to 5.75 extrapolated. This supports L992.
- `qual_cost_cheapest` (L1008): all 168 rows agree with L1008–1013.
  - Since S13's note was removed, the bands at L1034–1035 (5.0–14.75 floors) and NN's 0.018 sit in `qual_costs`, which the text does not name.
  - The trial's 0.0171/0.0374 and the 47 % (0.474) likewise sit in the unnamed `qual_trial_cost`.
- `qual_between_run_trial` (L1055): 2.1/3.6/5.1 confirmed, but NN's 3.45/4.45/5.75 are in `qual_between_run`.
- Release (L1049–1051): the numbers reproduce from `qual_release_capability`, which the text has not named since round 3.

Nothing is unsupported. The archive is now the only support, though, so the pending DOI also bears on the paper.

## 4. The rewrite

### 4.1 Meaning changes and errors

**a. Abstract, the new family** (p. 1, L039–040).
- Old: "none closer than 30 floors". New: "none within 30 floors".
- Problem: Mcd decides at 30.00 floors (Table 5; `learn_source_floor`), which is within 30. The new wording contradicts L1096–1097 and Table 8, which D3 aligned.
- Fix: "none below 30 floors" (same length).

**b. Conclusion, the recommendation** (p. 28, L1279–1281).
- Old: "carried the decision within a family, which argues for indexing such records … rather than for a more elaborate model".
- New: "Based on these findings, it is suggested to index production records … rather than to develop a more elaborate model."
- Problem: the scope is lost. "These findings" include the new family, where only simulation-based rules decided. "Suggest to index" is ungrammatical.
- Fix (shorter): "These findings suggest indexing production records within a design family by their relation to the coming design rather than developing a more elaborate model; such a record is the baseline …".

**c. Section 6.5, the last sentence** (p. 27, L1232–1233).
- Old: "narrows the spread of that share between teams". New: "narrows the spread between teams of the share of wrong verdicts accepted".
- Problem: it misparses ("teams of the share"), and "within the safe distance" is dropped.
- Fix: "narrows the differences between teams in the share of wrong verdicts accepted within the safe distance" (fits in L1233).

**d. Section 4.2** (p. 12, L533–538).
- Old: "Its documentation gives … a drawing depth of 30 mm, …". New: "The drawing depth is 30 mm, …".
- Problem: the attribution now ends after the first sentence, while L797 tests a shorter depth (Reviewer 2's area).
- Fix: "It also gives a drawing depth of 30 mm, trimming in OP20 without modeled cutting tools, and springback after both operations".

**e. Abstract, the last sentence** (p. 1, L040–041).
- Old: "the baseline a learned manufacturability check has to beat". New: "the baseline learned manufacturability checks must beat".
- Problem: a garden path ("baseline learned").
- Fix: "the baseline that learned … must beat". The abstract has 250 words (`CHECKLIST.md`), so delete "Then," at L028.

Checked and acceptable:
- "Under the same prior" (L994) resolves the old semicolon correctly. Under the reference prior the scheme gives NN 0.93.
- "6 of the other 8 extrapolated verdicts" (L1143) is more explicit.
- "should be reported/treated/tested" (L1185–1188) is prescriptive, but it sits inside a proposal labelled untested.
- "future work will focus on" (L1283) keeps the registered test as an extension.
- The Conclusion no longer claims that decisions "can be evaluated against production". This is weaker, not wrong; Section 6.1 keeps the answer to RQ1.

### 4.2 Clarity

What helps a process planner:
- the worked example now runs step by step in the order of Fig. 2 (L456–490);
- Eq. (2) defines P_FA, P_FR and P_T (L249);
- the floor is now "of production and measurement together, not of production alone" (L285–286);
- the split trial and release sentences of Sections 5.6 and 6.2.

What hinders:
- "respectively" at L1142 points back across two sentences. Write "41 of the sibling and 92 of the extrapolated verdicts".
- "However" occurs 26 times, against once before. At L721 it marks a change of topic, not a contrast.

These phrases carry no content and can pay for additions:
- "It is important to note that" (L815);
- "It should be noted that" (L287, L548);
- "According to the table" (L700) and "As seen in the table" (L805);
- "The computational details are as follows" (L679);
- the third verbatim definition of the floor (L1260–1262).

## 5. Items

**Must fix**
1. Abstract, L039–040: "none within 30 floors" becomes "none below 30 floors" (4.1a).
2. Conclusion, L1279–1281: restore the within-family scope and correct the grammar (4.1b).

**Should fix**

3. The abstract's garden path (4.1e), Section 6.5 (4.1c) and Section 4.2 (4.1d).
4. L1141: "gets 92 to 95 of the other 98 right (95 % interval)", paid for by "Moreover," at L1143.
5. Name the files:
   - add "(`qual_trial_cost`)" at L1040, paid for by "which is" there;
   - add `qual_between_run` at L1055.
6. Restore D5's interval rationale at no page cost, under `share_correct_lo, share_correct_hi` in `DATA_DICTIONARY.md`, or in the Table 7 note, paid for by L815's "It is important to note that".

**Optional**

7. Name `qual_release_capability` at L1051.
8. Carried over from round 3: the chart at L1220–1224 sees only false accepts, so it cannot track "share of wrong decided verdicts". The 150 is one-sided (185 two-sided).
9. Archive: `findings.md` (l. 14) says 31 pages, and `CHECKLIST.md` (l. 89) puts the end of the main text on p. 29, but the text ends on p. 28.

## 6. Recommendation

**Accept with minor corrections.** The rewrite caused no regression in the procedure, guard bands, costs, trial and release conditions, guidance table or deployment section. The two must-fix items are wording errors; the editor can check them, and items 3–6, without another round. The conditions outside the manuscript remain open: no `LICENSE`, and `refs.bib` still reads "DOI pending".

**Confidence:** high. Every number in my area that I checked reproduced, and the versions differ in wording only.
