# Editorial decision, third round

**Manuscript:** "When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing", by Hüseyin Tayyer Canseven (LUT University)

**Journal:** Journal of Intelligent Manufacturing (Springer)

**Version considered:** the second revision (`paper/review/jim_panel/round3/main_reviewed.pdf`, 31 pages, and its source), Online Resource 1, the response and marked-up comparison (`round2/`), and version 3 of the archive

**Reports considered:** Reviewer 1 (machine learning for manufacturing quality), Reviewer 2 (sheet-metal forming and quality engineering) and Reviewer 3 (industrial decision support), third-round reports dated 24 October 2026; all three recommend acceptance subject to the conditions

**Date:** 24 October 2026

*Written by an AI agent in the persona of a fictional handling editor of a simulated review panel; it does not come from the journal or speak for any real person.*

---

## Decision

**Accept subject to the conditions.**

I have checked every must-fix item of the three reports, read-only, against the archive. All hold; I reject none.

**What the revision achieved.**

- Table 7 gives the guard band a team has when it decides (the family's own with a sibling, the other family's for a new setting), which was my condition for avoiding another round.
- RQ3 credits evidence borrowed from the other family, not learning. The relation-matched intervals are labelled nominal, M7n's priors are tested, and M7's failure is reported.
- The worked example uses only what the planner knows, release is treated as a capability decision, and costs enter step 5.
- The archive remains exemplary: all 190 checksums and the eight release-note hashes verify.

| Change | Status | Remaining |
|---|---|---|
| C1, C3, C5, C11 | Met | – |
| C2 | Met, except the ranges and guarantee labels | D1, D2 |
| C4 | Met: the bands are those available when deciding | D5, D6 |
| C6 | Met, except one comparison | D4 |
| C7 | Partly met: the between-run condition is lost outside Section 5.6 | D8 |
| C8 | Partly met: the costs ignore step 5's rule | D7 |
| C9 | Met; the rewritten Section 6.1 sentence has a slip | D3 |
| C10 and the ruling on Online Resource 1 | Met; Table S12 uncited; archive slips | D6, D10 |
| Length | Met: 31 pages, main text and declarations ending on p. 27 | – |

**What remains.** Ten corrections, all from existing files or by relabelling. None changes a finding: where a statement fails as written, a corrected one holds (D4, D7). Two matter most to practitioners:

- Table 7's shares for a new setting are pooled over two families; for most rules one family falls to 91–93 % (D5).
- The costs are ranked over bands that step 5 forbids, which makes one stated result wrong (D7).

Two corrections (D4, D6) repeat my own second-round wording. I will check D1–D10 and the conditions myself; the paper does not go back to the reviewers. The corrected files are due by 7 November 2026, with one line per correction giving its location.

---

## Corrections required before acceptance

Pages and lines refer to `main_reviewed.pdf`. No correction needs new data. The main text must still end on p. 27 and the paper on p. 31, so a correction that adds words names what pays for them; Online Resource 1 does not count.

**D1. Coverage ranges of NN+RM** (Reviewer 1, must-fix 1).
- *Where:* p. 20, ll. 899–902.
- *What:* the lower ends of "73 to 100 %" and "61 to 100 %" are sibling values (convex family, dome). For a new setting, `qual_coverage.csv` gives 76–100 % between the families and 67–100 % between characteristics.
- *Satisfied when* the text gives these ranges.

**D2. Guarantees, and why errors are borrowed** (Reviewer 1, must-fix 2–3).
- *Where:* Table 2 note (p. 8, ll. 338–339); p. 7, ll. 303–304; Table S8 note; `level` in `qual_coverage.csv`.
- *What:*
  - The Table 2 note gives the largest-residual margin a guaranteed level for a new setting (n = 6) and a new family (n = 9). The guarantee needs a held-out alternative exchangeable with the calibration ones, which a held-out force or family is not: M2 covers 44 % extrapolating and 47 % for a new family (M3: 43 and 40 %), against "guaranteed" 0.71 and 0.80.
  - The S8 note says a P+RM guarantee "would need exchangeable families". With a single calibration family, even exchangeable families give none.
  - "A family's own calibration set lacks the relation" holds only for a new setting. With a sibling, NN+RM still borrows the other family's 63 cases (`learners.relation_matched`), although the family has sibling cases of its own (Table 7 uses them).
- *Satisfied when*:
  - "guaranteed" is limited to the sibling relation in the Table 2 note, the S8 note and the `level` labels (or their dictionary entry);
  - l. 303 gives the reason per relation within the same lines (round 2's "has no case of its new-setting relation" was right).

**D3. The new family in Section 6.1** (Reviewer 1, must-fix 4).
- *Where:* p. 23, ll. 1023–1025.
- *What:* the sentence credits a production-record rule with "30 floors at best for a new family". Those 30 floors are Mcd's (`learn_source_floor.csv`); NN and M1sn need 130 (`panel_source_floor.csv`).
- *Satisfied when* it reads as the abstract does, e.g. "…8.5 for a new setting, and no rule closer than 30 floors for a new family".

**D4. Comparisons independent of blank and scales** (Reviewer 2, must-fix 1).
- *Where:* p. 16, ll. 716–722; Table S3 note; `findings.md`, ll. 57–61.
- *What:* the concave wall angle falls by 1.5° only at the nominal friction.
  - Over the 66 friction–thickness combinations, the simulated change from 100 to 500 kN runs from −1.9 to +1.7°. It falls by at least 1° only at μ = 0.10–0.11, and in 39 % of combinations it lies within 0.5° of the measured −0.04°.
  - The corner force-effect ratio drops to 1.1–1.45 at μ = 0.05.
  - Three comparisons hold across the grid: the mid-side force effect (2.8–7.4 times the measured one), the downward concave arms (89–100 % of simulations) and the reversed dome ranking (76 % of 198 combinations).
- *Satisfied when* the passage rests on these three, with the wall-angle trend dropped or labelled nominal (Reviewer 2's wording is shorter), and the S3 note and `findings.md` agree.

**D5. Table 7's shares for a new setting** (Reviewer 3, must-fix 1).
- *Where:* Table 7, its note and ll. 917–918 (p. 20); Table S10 and its note.
- *What:* the bands are per family, but each new-setting share is pooled over both families. With the borrowed bands under the reference prior (concave/convex):
  - NN is right in 97/93 % of decided verdicts interpolating and 92/100 % extrapolating;
  - M7n in 99/92 and 98/93 %;
  - M5, interpolating, in 91/99 %.

  Source: `qual_guard_family.csv`. "In each relation" (l. 918) reads as holding in each family.
- *Satisfied when*:
  - l. 918 says "pooled over the two families" and gives NN's per-family range (92–100 %), paid for by the trial rates in the same sentence, which Table 7 gives;
  - the Table 7 note says these shares are pooled;
  - Table S10 gives them per family under both priors, with decided counts (some release-like counts are tiny: NN extrapolating decides 1 of 882 convex verdicts), and its note says why there is no interval (one held-out cell per family interpolating, two extrapolating).

**D6. The "force cell left out" scheme** (Reviewer 3, must-fix 3; Reviewer 1, must-fix 6).
- *Where:* p. 21, ll. 927–932; Table S10 note; Online Resource 1, Section 5; the `scheme` row of `DATA_DICTIONARY.md`.
- *What:* `qualify.guard_out_of_sample` drops the held-out geometry–force cell from the cases of both families.
  - Interpolating, only the other family's cell remains, so M5's 0.875 and M7n's 0.867 are Table 7's own values.
  - Extrapolating, the band pools three cells, two of them the other family's.
  - NN+RM is 0.7345 (`qual_guard_oos.csv`): 0.73, as S10 prints.
- *Satisfied when*:
  - the four places describe the scheme as computed, l. 931 reads 0.73, and the interpolating values are named as Table 7's (Reviewer 3's wording is the same length);
  - Table S12, the only table in Online Resource 1 that the text never cites, is cited at l. 927, paid for by the trial rates at l. 928, which repeat Table 7.

**D7. Costs under step 5's rule** (Reviewer 3, must-fix 2).
- *Where:* Fig. 6 and its caption (p. 22); Table S13; p. 21, ll. 938–949.
- *What:* step 5 lets stated costs only widen the 95 % band (ll. 440–441), but `qualify.costs` searches 0–40 floors with no such floor.
  - Fig. 6 and S13 therefore rank bands that step 5 forbids, and rules with no 95 % band (M0). From trial costs of 0.1–0.3, by relation and prior, the NN and M1sn bands fall below their 95 % bands; at 0.5 they are zero, with false accepts on 10–20 % of extrapolated verdicts (`qual_costs.csv`).
  - One stated result fails: under the release-like prior, at c_T = 0.2 and c_FR = 0.25, M0 is the cheapest option for an extrapolated setting (0.163 against M1sn's 0.174; S13), contrary to ll. 940–941.
  - With every band held at or above its 95 % band, the statements survive (my recomputation): NN is cheapest with a sibling from c_T = 0.1, NN or M1sn for a new setting at every trial cost, and no rule qualifies for a new family.
- *Satisfied when* Fig. 6 and S13 are recomputed under step 5's rule (a rule with no 95 % band counting as a trial; this shortens ll. 943–946), or are labelled unconstrained with the M0 exception stated at ll. 940–941 and paid for within ll. 943–946. Either way, no statement at ll. 938–949 contradicts S13.

**D8. Trial and release messages** (Reviewer 2, must-fix 2; Reviewer 3, must-fix 4).
- *Where:* Table 8, release-level row (p. 24, ll. 1080–1081); p. 23, ll. 1043–1046; p. 26, ll. 1187–1189.
- *What:*
  - Within a run, the 20- and 50-part trials decide at 1.35 and 0.90 floors (`qual_trial.csv`), inside the 1.75 floors of a limit at Ppk 1.33. Only from τ = 1 floor do they need 2.1 and 1.9 floors (`qual_between_run_trial.csv`).
  - The three places thus present a sensitivity result as an observation, which Table 5's trial rows contradict; C7 asked for the condition.
  - Section 6.2 omits the release-like share correct: of 100 extrapolated verdicts, 8 are decided and 6 of those are right (139 of 1,753, 0.748; `qual_guard_decision.csv`).
- *Satisfied when* the three places say "once runs differ by a floor" (Reviewer 2's wordings are no longer than the text they replace), and Section 6.2 adds "getting 6 of the other 8 right", paid for by an equal cut in that section (Reviewer 2 suggests l. 1052).

**D9. Fig. 1 caption** (Reviewer 1, must-fix 5; Reviewer 3, optional 2).
- *Where:* p. 9, ll. 382–383.
- *What:* panel (b) shows g = 3.25, M7n's band estimated in sample and pooled over the families (`figs.fig_schematic`), not Table 7's 4.75/2.75.
- *Satisfied when* the caption says so; its second line has room.

**D10. Archive and details** (Reviewer 1, must-fix 7–8; Reviewer 2, optional 4; mine).
- `DATA_DICTIONARY.md`, l. 56 (from `data_dictionary.py`): the `transfer` row says "scored in the produced family's floor", but the G* files score a new family in its own floor (NN+RM 326.8 in `learn_resolution.csv`, 293.0 in `learn_source_floor.csv`). *Satisfied when* the row points to the floor codes.
- `findings.md`, ll. 62–63: the strata are reversed (NN needs 1.60 floors when the siblings do *not* differ resolvably; `qual_strata.csv`). *Satisfied when* the file matches p. 17, ll. 757–758, and carries D4–D8.
- Table 3, l. 558: change 17.6 to 17.7 (`meas_scan.csv` gives 17.65, and Table S4 prints 17.7).
- Section 4.5 (l. 628) and the declaration (l. 1233): with this round there are seven simulated rounds, not six. Section 7 of Online Resource 1 should say what this round changed.

---

## Optional

I adopt three suggestions; each needs a one-line answer.

- Table 7 note: the sibling validation reuses stored fits that include the held-out alternative. Strictly nested, NN keeps 95 % correct, but under the release-like prior it sends 52 % of verdicts to trial rather than 41 % (Reviewer 1).
- Section 3.7, l. 458: state c_FR = 0.5 c_FA in place of "a short press run"; the cost band is 5.0 floors at c_FR = 0.25–0.5, but 5.5 at 1.0 (Reviewers 2, 3).
- p. 19, l. 872: change "not from the predictor" to "not from learning", since simulation-based centres stay unsafe with the same interval (Reviewer 1).

---

## My checks of the reports

All checks were read-only. I read the files with pandas, imported the released functions in memory from scratchpad scripts (`python3 -B`), ran no pipeline script, and left `git status` unchanged apart from this letter.

| Claim | Reviewer | File or method | Verdict |
|---|---|---|---|
| Checksums; release-note hashes | all | `sha256sum -c SHA256SUMS` | 190/190; 8/8 |
| Table 7; worst characteristics; τ = 3 bands | 1, 3 | `qual_guard_decision.csv`, `qual_between_run.csv` | Reproduced |
| NN+RM ranges; guarantee labels; sibling borrowing | 1 | `qual_coverage.csv`; `qualify.nominal_level`; `learners.relation_matched` | Confirmed (D1, D2) |
| 30 floors are Mcd's | 1 | `learn_source_floor.csv`, `panel_source_floor.csv` | Confirmed: 30.0, against 130.4 for NN (D3) |
| Comparisons over the grid | 2 | `features_ddacs_rddac.csv` via `qc.sims_qc` | Confirmed: −1.93 to +1.68°; 2.83–7.44; 76 % (D4) |
| Per-family shares | 3 | `qual_guard_family.csv`; `qualify` in memory | Confirmed under both priors (D5) |
| Force-cell scheme | 3, 1 | `qualify.guard_out_of_sample`; `qual_guard_oos.csv` | Confirmed (D6) |
| Costs: bands, M0, step 5's rule | 3 | `qual_costs.csv`, `qual_cost_cheapest.csv`; recomputed | Confirmed; M0 is the only new-setting exception (D7) |
| Trials; release-like share | 2, 3 | `qual_trial.csv`, `qual_between_run_trial.csv`, `qual_guard_decision.csv` | Confirmed (D8) |
| Fig. 1; dictionary; strata; Tables 3, S12 | 1, 2 | `qual_guard_prior_width.csv`, `learn_resolution.csv`, `qual_strata.csv`, `meas_scan.csv`, `main.tex` | Confirmed (D6, D9, D10) |
| Worked example; M7n priors; cross-fits; release on m̄ + 4σ | 1–3 | `qual_worked_example.csv`, `learn_m7n_priors.csv`, `qual_crossfit.csv`, `qual_release_capability.csv` | Confirmed: ≤ 1.40; 18.15/11.45, 0.924–0.971; 3.35/10.55 |
| Sibling band, strictly nested | 1, 3 | siblings' NN recomputed without the held-out alternative | 0.955 correct, 2.6 % trials; release-like 0.952, 52 % |
| Licence, DOI | 3 | `.zenodo.json`, `CITATION.cff`, `refs.bib` | Absent; pending |

---

## Qualifications of the reports

1. **My own wording.** The author followed my text in two places:
   - D6 repeats my C4 ("with a force cell left out", 0.74) and my second-round qualification 5, which placed the scheme within the family;
   - D4 repeats the comparisons my C6 took from Reviewer 2, which I had checked at nominal settings only.
2. **Nested validation (Reviewers 1, 3).** Not required. Table 7's bands are ones a team has when it decides; only their validation reuses stored fits, and, strictly nested, the share correct still holds.
3. **Costs (Reviewer 3).** I require consistency with step 5, not the recomputation; either branch of D7 meets C8.
4. **Per-family shares (Reviewer 3).** This is reporting, not a new criterion: the shares show what borrowing from a single family costs, as C2 required for coverage. No interval is required for a new setting, since every alternative in a held-out cell shares one fit.
5. **Details.**
   - The corner ratio at μ = 0.05 is 1.13–1.45, not 1.1–1.4 (Reviewer 2); the difference has no consequence.
   - The request to the dataset providers was recommended, never required, and is not a condition.

---

## Conditions for acceptance

These are actions for the author outside the manuscript, not faults of the revision.

- **Licence.** A `LICENSE` file for the code, with `license` fields in `.zenodo.json` and `CITATION.cff`. The data-derived files stay under CC BY 4.0, with the attribution already in `README.md`.
- **DOI and deposit.** A minted DOI for the corrected version, cited in `paper/refs.bib` (still "[DOI pending]"), `CITATION.cff` and the cover letter. The corrections change files in `scripts/` and `results/`, so `SHA256SUMS` and the release-notes table are regenerated afterwards; `sha256sum -c SHA256SUMS` must pass in the unpacked deposit, and I must be able to open it.
- **Registration.** My second-round point is met by its second branch: "frozen" is gone from the paper and Online Resource 1, and a registered confirmatory test is named only as an extension (p. 27, ll. 1200–1201). No deposit is needed for acceptance. To cite a registration later, deposit `paper/notes/frozen_procedure.md` with a timestamp before any confirmatory analysis, its guard-band item ("one setting level out") first aligned with step 5 and D6.
- **Data dictionary.** In the deposit, corrected as D6 and D10 require.

Yours sincerely,

Handling editor (a fictional persona in a simulated review panel), Journal of Intelligent Manufacturing
