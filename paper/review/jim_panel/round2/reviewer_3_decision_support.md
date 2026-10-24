# Referee report, second round: Reviewer 3

**Manuscript:** When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing
**Journal:** Journal of Intelligent Manufacturing
**Round:** Second round (first revision)
**Reviewer focus:** Industrial decision support: decisions under uncertainty, cost-aware decisions, human–AI collaboration and trust, and the deployment of AI tools in factories
**Date:** 24 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The revision is thorough and responsive. The paper is retitled and framed as an exploratory, production-referenced evaluation of design-stage decision rules on one deep-drawing process; the abstract defines its terms, carries five numbers and ends with a finding; reuse for classifiers and language-model checks is labelled an untested proposal; the sibling strata use decision-time information; and the learners get a fairer test (a small-data trend GP M7n, a multi-fidelity model M7, a calibration with discrepancy Mcd, relation-matched intervals). In my area, guard bands are now estimated per family, validated out of sample and reported under a release-like prior and per characteristic (Table 7, Section 5.5); a loss (Eq. 2), a decision-curve-style cost figure (Fig. 6), safe distances on the false-accept and false-reject sides, trial reference rows and a design-level verdict are added; and a schematic (Fig. 1), a worked example (Section 3.7), a reporting checklist (Table 9), a scoring function (`scripts/opchar.py`) and a deployment section (6.5) answer my presentation and reuse comments. To stay at 31 pages, the revision has no appendix and no supplement; the tables the decision asked to go there are result files in version 2 of the archive.

## 2. Assessment of the response to my first-round comments

**Major 1 (message hard to reach): Resolved.** The main message is now easy to find. The abstract (L022–040), Fig. 1 (p. 9), the 90th-percentile reading (L352–355), the worked example (L454–471), eight rules with descriptive names (Table 2) and Section 6.2 all carry it. Some Results paragraphs are still dense (minor 9).

**Major 2 (guard band): Partly resolved.** Every analysis I asked for exists: per family (L914–918), out of sample (L918–921), under a release-like prior (L924–927), per characteristic (L921–923) and in the main text (Table 7). But Table 7 reports bands pooled over the families, not the per-family bands the procedure prescribes, and for new settings a per-family band is not available when the decision is made (major 1).

**Major 3 (costs, trial rates, part-level verdicts): Partly resolved.** The following were added: Eq. (2) (L234–239), Fig. 6, trial rates (Table 7), safe distances on both sides (Table 5), trial rows, a design-level verdict (L995–998) and a message per 100 verdicts (L1061–1064). But the costs are computed in-sample, pooled over families, under one prior and with a trial assumed error-free, and they do not enter step 5 (major 2).

**Major 4 (claims and scope): Resolved.** This is answered by the title, the abstract (L031–040), the exploratory status (L088–089, L631–633, L1188–1189), Section 6.4 "a proposal" (L1094, L1101) and the decision-time strata. One ambiguous phrase remains (minor 1).

**Major 5 (unit): Resolved.** The revision adds physical units and performance indices (Table 6, L767–768) and F/σLT (Table 4). It also gives the requirement grid in units (L437–438), calls the floor a lower bound (L272–273) and adds a between-run sensitivity analysis (L960–964).

**Major 6 (reuse and checklist): Resolved.** This is answered by Table 9, the limitation for classifiers (L1101–1104, L1125), the expanded language-model protocol (L1126–1130) and `opchar.py`, which I ran (Section 5). Remaining points are minor 7 and 8.

**Major 7 (positioning): Resolved.** Section 2 now covers virtual metrology with reliance indices (L108–111; Table 1), JCGM 106 (L147–148, L158–160), transfer learning (L111–113), reliance on automation (L155–158) and cost-sensitive evaluation (L154–155), and says what is adopted and what is new (L179–183, L212–213).

**Major 8 (human–AI collaboration and deployment): Partly resolved, which is sufficient given the editor's qualification.** Section 6.5 (L1144–1160) sketches the interface, monitoring with triggers for re-qualification, the cost of the evidence and a user study. Two practical gaps remain (minor 6).

| Minor | Status | Note |
|---|---|---|
| 1–3 | Resolved | "learned 90 % intervals" gone; keywords added (six-keyword limit accepted); sentence rewritten |
| 4–7 | Resolved | levels in Table 2; FA/FR sides (L363–367); verdicts behind distances (L360–361); pseudocode (L447–450) |
| 8–11 | Resolved | Fig. 2 input boxes; replication units (L550–551); development record (L622–631); Fig. 5 |
| 12 | Resolved | Sections 5.3 and 6.1; abstract number limit accepted |
| 13–15 | Resolved | decomposition limited to pre-specified rules; noise bound (L859–861); tuning study (L871–873) |
| 16 | Partly | states what was used and what sufficed for NN (L1098–1101), not what step 5 needs |
| 17–23 | Resolved | Sections 5.5–5.6; Fig. 1b; Table 8; explainability (L1071–1073); L1009 deleted; PA12 needs (L1138–1140); threats (L1175–1177) |
| 24 | Partly | ISO editions accepted; DOI pending |
| 25 | Partly | versions pinned and release notes corrected; licence pending |

## 3. The editor's required changes that concern my expertise

- **R1 (claims): met.** Remaining point: minor 1.
- **R2 (decision-time strata): met.** I verified the numbers. The release-level comparison is reported as marginal (L950–957).
- **R7 (guard band): partly met.** The main table shows pooled bands. The out-of-sample intervals, the scheme that leaves out a force cell, and the band as a function of the prior's width are only in the archive (major 1).
- **R8 (pre-specified versus post hoc rules): met.** The exception is that the cross-fitted step-6 shares are not reported (minor 5).
- **R9 (per characteristic, physical units): met in substance (Table 6).** The full table with safe distances exists only as a CSV file (major 3).
- **R10 (costs, trials, decision set): met as specified** (Eq. 2; Fig. 6; false-accept side; trial rows; decision set at L078–082). What remains is in major 2.
- **R11 (presentation and positioning): met, with one exception.** It asked that the main text not grow and that material move to supplementary material. Instead the main text grew by about four pages, to p. 27, and there is no supplement (major 3).
- **R12 (archive and declarations): partly met.** The licence and the DOI are still pending; both are needed before acceptance.

## 4. New or remaining issues

### Major

**1. The guard band in Table 7 and in the worked example is not the band that step 5 prescribes, and for new settings it uses information not available when the decision is made** (Table 7, p. 20; L408–413, L442–443, L463–466, L910–927; Table 9).

- *Pooled instead of per family.* Step 5, Fig. 2 and Table 9 call for a band per family, but Table 7's g and g5 are pooled over both families: `opchar.guard_band` reproduces them exactly (NN: 0.25, 2.0, 7.0). The per-family bands of NN are 0 and 0.5 with a sibling, 1.5 and 2.5 interpolating, 9.5 and 5.75 extrapolating. The worked example uses the per-family 1.5 floors; Table 7 gives only the pooled 2.0.
- *Decision time.* In the worked example the 300 kN setting has not been produced, yet its band "on this family" is estimated from the three concave 300 kN alternatives, including the one being decided, the family's only interpolated cell. This is the decision-time problem that R2 removed from the strata. The paper makes the right argument for the relation-matched intervals (L305–307: a family's own data contain no case of its new-setting relation); it applies equally to the band.
- *Validation scheme.* For new settings, Table 7's out-of-sample (OOS) column leaves one alternative out within its family, so the band rests mainly on that alternative's lubrication siblings in the same held-out cell, which share its calibration set and, for NN, its prediction; for interpolation it rests on nothing else. That is close to in-sample. The scheme that matches the relation leaves the force cell out (for interpolation: the other family's band).
- *What the main text leaves out.* Under the release-like prior, leaving the force cell out gives shares correct well below 95 %: NN 0.72 (cluster interval 0.68–0.78) and NN+RM 0.74 extrapolating, M5 0.88 and M7n 0.87 interpolating; only the first is mentioned (L927). With the pooled band, the worst characteristics are not the sibling dome quoted at L922 (89 %) but NN on the cup depth (86 %) and M7n on the waviness (83 %) extrapolating, and M5 on the dome interpolating (83 %). And since each truth is a single run, a band for future runs needs a between-run allowance: with τ = 3 floors the band of NN grows from 0.25 to 2.9, 2.0 to 4.0 and 7.0 to 8.9 floors; only the first is reported (L964).

*Requests.* (a) Report in Table 7 the band a team could have when deciding: per family with a sibling; for new settings borrowed from the other family (or estimated from the family's other produced settings) and validated by leaving the force cell out. Say so in step 5 and Table 8, or justify pooling explicitly, as R7 allows. (b) Redo the worked example with such a band (the convex family's 2.5 floors; the margin of 6.2 floors still releases). (c) Give the OOS shares and trial rates with their cluster intervals, under both priors and both schemes, and the number of decided verdicts behind each band. (d) Name the worst characteristic per relation, and add a between-run column (e.g. τ = 1.5 and 3 floors) or state that the bands are within-run lower bounds. (e) Show band and trial rate against the width of the prior, as R7 required; the archive has it, and it supports the release-level conclusion: within ±3 floors NN with a sibling needs 8 floors and sends 99 % of verdicts to trial.

**2. The costs sit beside the procedure rather than inside it, and they are estimated in-sample** (Section 5.6, L937–949; Fig. 6; L447–450; L460–461).

- *Costs are not part of step 5.* Step 1 and Fig. 2 list costs as inputs and Table 8 chooses rules "by expected cost", but the pseudocode (L447–450) fixes g by the 95 % target alone, and the worked example states a trial cost of a twentieth of a false accept (L460–461) without using it. The paper's own remark that "cost-optimal bands would be wider" (L945–946) is left unconnected: at c_T = 0.05 c_FA the cost-minimising band of NN interpolating is 4.5 floors (pooled), sending 40 % of verdicts to trial instead of 18 %. (The example would still release.)
- *Unconstrained minimisation can be unsafe.* With c_FR = 0.25 and c_T = 0.5 (both relative to c_FA), the cheapest option for a new family is the nominal simulation without a band, with a false-accept probability of 0.14 per verdict.
- *In-sample and pooled.* `qualify.costs` chooses the cost-minimising band on the same cases on which it scores the cost, pooled over families: the estimation that R7 removed from the 95 % band. The new-family statement (M2 and then M5 cheapest beyond c_T ≈ 0.1, L941–943) rests on in-sample bands over two transfers and changes with c_FR (with c_FR = 0.25: M3 at c_T = 0.1, M0 at 0.2 and 0.5).
- *One prior, one c_FR, no uncertainty.* Under the release-like prior the cheapest rule with a sibling at c_T = 0.05–0.1 is M7n, not NN, by a few thousandths of c_FA (M7n 0.035, M5 0.037, NN 0.038 at 0.05), differences this design almost certainly cannot resolve. L939–940 thus holds under the reference prior only.
- *Error-free trial; prevalence.* In Fig. 6 "trial every design" costs exactly c_T. Scored with `opchar.step6`, the 20-part trial of Table 5 has an expected error cost of 0.017 c_FA per verdict under the reference prior and 0.037 under the release-like prior, as large as NN's entire expected cost with a sibling at c_T = 0.05 (0.018). Both priors also place 47 % of verdicts on failing designs, far more than a team proposing settings on a qualified die would expect.

*Requests.* (a) Define how costs set g in step 5, add it to the pseudocode and carry it through the worked example; for instance, minimise Eq. (2) at the team's ratios subject to a cap on the false-accept rate, with the 95 % band as the default when costs are unknown. (b) Estimate the cost-minimising band out of sample with the schemes of major 1, or cross-fit it between geometries, and qualify the new-family statement. (c) Report both priors and all three values of c_FR (the archive has them), with cluster intervals for cost differences or a statement of which differences are resolved. (d) Add the trial's own error (its within-run lower bound) to the cost of a trial verdict. (e) State the implied share of failing designs and show how the band changes when they are rarer (e.g. 10–20 %).

**3. The evidence for the part a factory would deploy should be visible to the reader** (response letter, "Length, and where the tables went"; Table 7 footnote; L634–635).

On the merits, the CSV files with `results/findings.md` are complete, checksummed and more reusable than typeset tables, and the main text keeps the most important tables (Tables 3 and 6 and a compact Table 7). But the reason given, keeping the paper at 31 pages, does not apply to an Online Resource, which does not count towards the article's length. For a JIM reader the CSV files are no substitute: they use internal names (`within`, `setting/extrapolation`, `transfer`, M4 for M3n, `+RM`), have no captions and often no units; the deposit has no DOI and the code no licence, so the results behind statements such as "bands per family, out of sample and under other priors are in the archived results" cannot yet be cited or reused; and `findings.md` is a layered history in which superseded first-version tables (its Sections 1–5) sit beside current ones. *Request:* restore a compact Online Resource with the tables named in R3a, R4, R5 and R9 (with safe distances) and, for my area, per-family and borrowed bands, OOS shares by scheme and prior with intervals, bands against the prior's width, bands per characteristic, and costs by prior and c_FR. Keep the CSV files as the machine-readable complement, and give `findings.md` an index of current numbers with its history in a separate file.

### Minor

1. **"Committed to in advance"** (L034–035, L1042, L1191). NN was added after the first results (Table 2, L626), so a reader may take this phrase to mean pre-specified. Write instead "one rule applied to every relation".
2. **Mcd's 30 floors** are quoted in the abstract (L039) and Table 8, but Mcd is not in Table 5. Add its row, or at least its value for a new family.
3. **L1062–1064.** "Gets at least 93 of the other 98 right" is an in-sample figure averaged over characteristics. Write "about 93 (95 % out of sample; 89 % on the dome)".
4. **L1186–1188.** "A guard band validated for the requirements a team expects" overstates the result: here the band was validated for an assumed prior.
5. **L965–992.** Report the cross-fitted step-6 shares correct from `qual_crossfit.csv`: 0.92–0.97, below 0.95 in four of the six within-family cases. They are the out-of-sample test of the whole selection in step 5, rule and band together.
6. **Section 6.5.** Monitoring sees one side only: false accepts on accepted designs become visible after production, false rejects never, and trial verdicts are produced anyway. Detecting a rise of the wrong-verdict share from 5 % to 10 % needs about 150 decided verdicts (one-sided, 80 % power), possibly years in one family, so the floor-based trigger is the practical one; say so. The study's participants should be process planners and quality engineers (L078–082), not "designers" (L1157–1158), and overrides of trial verdicts should be an outcome.
7. **Table 9.** Its guard-band row cites Table 7 for bands "per family, out of sample", which Table 7 does not show. Consider items for the intended decision, the held-out unit per relation, the uncertainty of the distances (intervals, smallest resolvable difference) and code and data availability with licence.
8. **`opchar.py`.** The self-check covers the distances only; add checks of `guard_band` and `step6` against Table 7 (they reproduce it), a grouped out-of-sample function (the procedure requires validation), a cost-minimising band, weights for a team's prior and an example input file.
9. **Density.** The paragraph at L889–906 carries some thirty numbers, Section 5.7 (L960–1005) as many; move half to the Online Resource.
10. **Figures.** Fig. 1b: add the decided share against g on a second axis, the trade-off a planner faces. Fig. 6: differences between rules are invisible in panels a–c at low trial costs; plot cost relative to "trial every design" or to NN (net benefit), state the reference prior in the text, and note that its band search reaches 40 floors (M2 and M5 at 24.5 in panel g) while step 5 caps at 20.
11. **Section 3.7** uses cups, forces and draw-in before Section 4 introduces them; add a forward reference.
12. **L946.** "More than a new force on an existing tool costs" needs a source or an order-of-magnitude example, or should be stated as an assumption.
13. **L1176.** If Table 7 stays pooled, write "pooled over characteristics and families".

## 5. Checks I ran against the archive

All checks were read-only, and I ran no pipeline script. My own short scripts lived outside the repository and imported the released functions without writing bytecode; the checks left the repository unchanged.

| What | File(s) | Result |
|---|---|---|
| Checksums | `SHA256SUMS` (180 entries); the hashes listed in `RELEASE_NOTES.md` | All verify; the main version-1 result files are unchanged. Confirmed |
| Scoring function | `scripts/opchar.py --selfcheck` (I read the code first; it only reads and prints) | "all distances reproduced". Confirmed |
| Table 7: g, g5, T | `opchar.guard_band` and `step6` on `dec_intervals.csv` + `learn_intervals.csv` | Reproduced exactly; g is pooled over families (per-family bands in `qual_guard_family.csv`). NN under the release-like prior decides 63/32/2 % of verdicts. Confirmed |
| OOS shares, Section 5.5 | `qual_guard_oos.csv` | 0.94–0.99; 0.93–0.95; 0.83/0.81; 0.72 confirmed. The release-like failures when a force cell is left out are not reported beyond NN |
| Per characteristic | `qual_guard_characteristic.csv` | 0.892/0.985/0.917 confirmed; worse cases under extrapolation are not reported |
| Prior width | `qual_guard_prior_width.csv` | Within ±3 floors, NN with a sibling: band 8, trial rate 99 %. Not in the paper |
| Costs, Section 5.6 | `qual_costs.csv`; code of `qualify.costs` | NN band 5→0 and 14.75→0, the cheapest rules, and "a tenth to a quarter" confirmed. The band is chosen in-sample and pooled; the results under the release-like prior and other c_FR differ and are not reported |
| Trial rows; trial error cost | `features_rddac.csv` via `qc.parts_qc`; `opchar` | 1.35/0.90 floors confirmed; error cost 0.017/0.037 c_FA |
| Worked example | stored intervals, concave/300/medium, mid-side draw-in | Floor 0.0497 mm, NN 14.994 mm, margin 6.16 floors, M7n 4.46, M0 15.663 mm, truth 8.36 floors below the limit: confirmed. The 1.5-floor band comes from the concave 300 kN cell |
| Table 5 | `dec_resolution.csv`, `learn_resolution.csv`, `panel_source_floor.csv`, `learn_source_floor.csv` | NN, M1sn, M2, M5, M7n, NN+RM in every relation, including FA/FR, intervals and trial rows. Confirmed |
| Strata; release-level limits | `qual_strata.csv`, `panel_capability.csv` | 1.60/4.40 (75/51 cases), 3.05/4.20, 6.15/8.90; 1.03/1.75/2.46/3.14 floors. Confirmed |
| Table 6 (NN; performance index) | `qual_per_characteristic.csv` | Confirmed |
| Between-run, cross-fitting, design level, guards, few-shot transfer | `qual_between_run`, `qual_crossfit`, `qual_design_level`, `dec_guard`, `learn_fewshot` | Confirmed as quoted; the cross-fitted step-6 shares (0.92–0.97) are not reported |
| Implied share of failing designs | `opchar` evaluation grid on the sibling cases | 47 % under both priors |
| Licence, DOI | repository, `CITATION.cff`, reference list | Both absent (pending) |

## 6. Recommendation

**Minor revision.** The revision answers nearly everything I asked for, the archive verifies (every number I checked reproduces, and the released scoring function reproduces the distances and Table 7), the claims now match the evidence and the paper reads as a JIM paper. What remains concerns the element a factory would deploy: the guard band in Table 7 and the worked example is neither the band step 5 prescribes nor one a team could have when deciding, and the costs are computed in-sample, beside the procedure rather than inside it. Both can be fixed from the stored intervals with the released code, without new data; neither is likely to change the findings, but both change what a practitioner would take from Table 7 and Section 5.6. With majors 1–3 addressed, the licence and DOI in place and the minor points answered, I would support acceptance. I would like to see the revised Table 7, Section 3.7 and Section 5.6, but do not need a full further round.

## 7. Confidential comments to the editor

The revision is honest and the archive is in good order: all 180 checksums verify, and every number I spot-checked reproduces, Table 7 included, with the released function. My remaining concerns are about the internal consistency of the procedure that would be deployed: pooled versus per-family bands, a worked-example band that draws on the production of the very setting being decided, and costs estimated in-sample. They need no new data and leave the findings intact, which is why I recommend minor rather than major revision; if the author declines to make the bands in Table 7 available at decision time, I would consider another round warranted. On the tables moved to the archive, I suggest asking for a compact Online Resource: it does not count towards the length, and until the deposit has a DOI and a licence, readers can neither cite nor reuse the results that several statements rest on. Licence and DOI are prerequisites for acceptance. The AI-use statement is now explicit, including that most post hoc analyses followed simulated reviews; whether that extent of use is acceptable is a policy question for the journal.
