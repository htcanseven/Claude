# Referee report, third round: Reviewer 1

**Manuscript:** When can a prediction replace a physical trial? A production-referenced evaluation of design-stage decision rules in deep drawing
**Journal:** Journal of Intelligent Manufacturing
**Round:** Third round (second revision)
**Reviewer focus:** Machine learning for manufacturing quality: predictive quality and virtual metrology, learned manufacturability assessment, uncertainty quantification and conformal prediction, small-data and transfer learning
**Date:** 24 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

## 1. Summary of the revision

The author has answered every point of my second report:

- the safety at new settings is credited to the other family's errors on the same relation (Section 5.4, Table S7);
- the relation-matched intervals are labelled nominal;
- M7n's undercoverage is explained and its priors are tested, and M7's failure is reported;
- Table 7 holds the bands available when deciding, and both cross-fits are reported;
- Online Resource 1 and a data dictionary are in place, with the main text still ending on page 27.

Everything I recomputed reproduces. Eight one-line corrections remain, and none changes a conclusion.

## 2. My second-round points

| Point | Status | Where (revised PDF) |
|---|---|---|
| Major 1: credit for safety; crossing | Resolved | p. 1, ll. 37–38; p. 19, ll. 868–873; p. 20, ll. 897–899; p. 23, ll. 1030–1031; p. 26, ll. 1195–1196; Table S7 |
| Major 2: guarantee; coverage detail | Partly resolved | p. 7, ll. 303–309; Table 2; p. 20, ll. 899–902; Tables S8–S9; must-fix 1–3 |
| Major 3: M7n's intervals and priors; M7 | Resolved | p. 7, ll. 297–299; p. 17, ll. 771–773; p. 19, ll. 854–866; Table S6 |
| Major 4: selection and validation | Resolved | p. 1, l. 34; p. 14, l. 631; Table 7 (p. 20); p. 21, ll. 921–932; p. 22, ll. 999–1002; must-fix 6 |
| Major 5: where the tables went | Resolved | p. 27, ll. 1205–1206, 1223–1224; Online Resource 1; `DATA_DICTIONARY.md`; `findings_history.md`; must-fix 7–8 |
| Minor 1: finite-sample sentence; Barber et al. (2021); Friedman (2001) | Resolved | p. 7, ll. 307–309, 316–317 |
| Minor 2: conformal risk control, learn then test | Not resolved (declined; reason accepted) | response, Part 2 |
| Minor 3: interval-score sentence | Resolved | p. 20, ll. 902–904 (optional 5) |
| Minor 4: cluster intervals | Resolved | p. 20, ll. 905–906 (M3 recomputed: 0.929–0.984) |
| Minor 5: degenerate intervals | Resolved | `qual_coverage.csv`, `ci_note` (26 flagged) |
| Minor 6: M0 without its own series | Resolved | p. 22, l. 1012 |
| Minor 7: M7 counted | Resolved | p. 7, l. 310 |
| Minor 8: few-shot floor | Resolved | p. 20, ll. 908–910 |
| Minor 9: 92–95 of 98 | Resolved | p. 23, ll. 1041–1043 |
| Minor 10: per-family bands | Resolved | Table 7 (p. 20) |
| Minor 11: dense paragraph | Resolved | pp. 19–20, ll. 868–910 |

## 3. The editor's required changes in my area

- **C1: met.**
  - The claim names the borrowed evidence.
  - Section 5.4 states the three results with the right numbers.
  - Table S7 holds the crossing and the pooled trend GP.
  - The interval-score sentence is limited to production-record and trend centres.
- **C2: met in substance.**
  - In place: no guarantee; "nominal 0.9" in Table 2; the 21, 42 or 63 cases; the two family swaps; Tables S8–S9; Barber et al. (2021).
  - Wrong: the ranges given in the text, and the Table S8 note (must-fix 1–2).
- **C3: met.**
  - The mechanism is explained (p. 19, ll. 855–862).
  - Table S6 and its sentence are in place: distances move by at most 1.40 floors, and coverage stays at 47.6–61.9 %.
  - M7 is described as a force slope, its 118 floors are reported, and it is counted.
- **C4 (validation): met.**
  - Bands are given per family, borrowed from the other family for a new setting.
  - Table S10 adds the intervals, the counts and the force-cell-out shares.
  - Step 5 (p. 10, ll. 436–440) agrees with Tables 8–9.
  - Section 5.5 gives the requested figures, with one rounding slip (must-fix 6).
- **C9: met.** The wording is changed, and both cross-fits reproduce `qual_crossfit.csv`:
  - 18.15 and 11.45 floors;
  - 0.924–0.971, four of six below 0.95;
  - 0.733 for a new family.
- **C10: met.**
  - Online Resource 1 follows the ruling, though Table S12 is uncited (optional 3).
  - The length holds, and `findings.md` is separated from its history.
  - Two slips remain in the archive (must-fix 7–8).
- **C11 (my items): met.**

## 4. New issues

### Must fix

Each fix replaces at most a line, and I checked each item against the file named.

1. **Coverage ranges (p. 20, ll. 899–902).**
   - The text attaches "73 to 100 %" and "61 to 100 %" to the coverage for a new setting.
   - Both lower bounds come from the sibling relation (convex family 73 %, dome 61 %).
   - For a new setting, `qual_coverage.csv` gives 76–100 % between the families and 67–100 % between characteristics.
2. **Guarantee wording (Table 2 note, p. 8, ll. 338–339; Online Resource 1, Table S8 note).**
   - The S8 note says the P+RM guarantee "would need exchangeable families". Section 3.3 rightly says that cases from one family's few shared fits give no guarantee.
   - The Table 2 note gives M2 a guaranteed level for a new setting and a new family. M2 covers 44 % extrapolating and 47 % for a new family (M3: 43 % and 40 %), against "guaranteed" levels of 0.71 and 0.80 (`qual_coverage.csv`).
   - Fix: restrict "guaranteed" to the sibling relation, as the S8 note itself does, and align the `level` labels in `qual_coverage.csv`.
3. **Why the errors are borrowed (p. 7, ll. 303–304).**
   - "A family's own calibration set lacks the relation" holds only for a new setting.
   - With a sibling, Table 7 takes the band from the family's own sibling cases (`qualify.py`, l. 261), yet NN+RM borrows the other family's 63 cases (`learners.py`, ll. 355–363).
   - Round 2's wording, "has no case of its new-setting relation", was correct.
4. **Section 6.1 (p. 23, ll. 1023–1025).**
   - The sentence gives the production-record rule "30 floors at best for a new family".
   - The 30 floors are Mcd's (`learn_source_floor.csv`); the production record decides at 130 floors (`panel_source_floor.csv`).
   - The slip predates this revision, but the C9 edit rewrote this sentence. Suggested: "…, 8.5 for a new setting, and no rule closer than 30 floors for a new family".
5. **Fig. 1 (p. 9, caption, ll. 382–383).**
   - Panel (b) shows g = 3.25, M7n's in-sample band pooled over the families (`figs.py`, `fig_schematic`; `qual_guard_prior_width.csv`). It is the value that round-2 Table 7 printed.
   - The revised Table 7 gives 4.75/2.75. Add "in sample, pooled over the families" to the caption.
6. **p. 21, l. 931.** NN+RM with the force cell left out is 0.7345 (`qual_guard_oos.csv`): "0.73", as Table S10 prints it.
7. **`results/DATA_DICTIONARY.md`, l. 56 (written by `scripts/data_dictionary.py`, l. 56).**
   - The scope table says `transfer` rows are "scored in the produced family's floor".
   - In the `dec_*` and `learn_*` files they are in the new family's own floor, as the dictionary's own code G* says: `learn_resolution.csv` gives NN+RM 326.8, against 293.0 in `learn_source_floor.csv`.
   - This is the very trap C10 was meant to remove; correct the row.
8. **`results/findings.md`, ll. 62–63.** The strata are reversed: the nearest setting needs 1.60 floors when the siblings do *not* differ resolvably (`qual_strata.csv`). The paper, at p. 17, ll. 757–758, has it right.

### Optional

1. Table S10's new-family rows, and the P+RM intervals for a new family, borrow from the reverse transfer, which needs the new family's own production (`qualify.py`, l. 264). Label them a validation, not bands available when deciding.
2. With a sibling, the validating band comes from stored fits that include the held-out alternative. Fully nested, NN keeps 0.956 correct, but its trial rate rises from 2 to 3 %, and under the release-like prior from 41 to 52 %. One clause in the Table 7 note would say so.
3. Cite Table S12 at p. 21, l. 927; it is the only table of Online Resource 1 that the text never cites.
4. p. 19, l. 872: "not from the predictor" → "not from learning", since simulation-based centres stay unsafe with the same interval.
5. p. 20, ll. 902–904: when extrapolating, the best scores belong to the trend centres (19.1–19.4); the trend GP on both families (20.9) beats NN+RM's 24.3.

## 5. Checks I ran against the archive

All checks were read-only:

- Python ran as `python3 -B`, with released functions imported in memory.
- I ran no pipeline script.
- `git status` was unchanged afterwards.

| Claim | File or method | Verdict |
|---|---|---|
| Archive integrity; changes since version 2 | `sha256sum -c SHA256SUMS`; version-2 list via `git show` | 190/190 verify; changes and the eight release-note checksums match |
| Scoring function | `opchar.py --selfcheck` | Distances, 40 guard bands and the worked example's cost band reproduced |
| Table 5 (with Mcd), Table S1 | `dec_resolution`, `learn_resolution`, `panel_source_floor`, `learn_source_floor` | Confirmed |
| Table 6; Table S2 (M7 204/118 on the depth) | `qual_per_characteristic` | Confirmed |
| Three like-for-like results; Table S7 | `learn_resolution`, `qual_coverage` | Confirmed (17.55, 17.80, 20.10; 151.3, 155.1; 2.75) |
| NN+RM coverage and its ranges | `qual_coverage` | 88/93 % confirmed; ranges misattributed (must-fix 1) |
| GP 83–86 % (0.72–0.94), M3 0.93–0.98, flags | `qual_coverage` | Confirmed; 26 degenerate rows flagged |
| M7n diagnostics; Table S5 | `learn_gp_diagnostics` | Confirmed (nugget 0.43–0.51 floors) |
| Prior sensitivity; Table S6 | `learn_m7n_priors` | Confirmed (≤ 1.40; ≤ 0.41 floor from M1sn; reference reproduces to 4e-15) |
| Table 7, Tables S10–S11 | `qual_guard_decision`, `qual_guard_oos` | Confirmed except 0.74 (must-fix 6) |
| Sibling band, nested | `opchar` functions on `dec_intervals` | Stored 0.954/2 % reproduced; nested 0.956/3 % and 0.952/52 % |
| Cross-fits | `qual_crossfit` | Confirmed |
| Few-shot, tuning, M0, design level | `learn_fewshot`, `tune_decisions`, `qual_floor_loao`, `qual_design_level` | Confirmed (5.9–10.5; 11.15/13.05; 3.75; ≤ 1.75 against 15.85) |
| Fig. 1 band | `figs.fig_schematic`; `qual_guard_prior_width` | In sample and pooled, 3.25 (must-fix 5) |
| Dictionary and `findings.md` | `learn_resolution` against `learn_source_floor`; `qual_strata` | Two slips (must-fix 7–8) |

## 6. Recommendation

**Accept subject to the conditions.** The revision meets C1–C4, C9, C10 and my C11 items as specified. The paper now:

- credits borrowed evidence, not learning, for the safety at new settings;
- states that the relation-matched intervals carry no guarantee and reports their coverage in detail;
- shows that M7n's undercoverage holds under every prior variant tested;
- validates the guard bands with information a team has.

The eight must-fix items are one-line corrections, each checkable against the file named. The other conditions are the author's actions outside the manuscript:

- a licence for the code;
- a minted DOI whose deposit matches the checksums;
- a timestamped registration, if a registered confirmatory test is cited.

## 7. Confidential comments to the editor

The author did what you asked, and the archive remains exemplary: every number I tested reproduces. I see no reason for another round.

Must-fix items 1 and 2 matter most, because they carry the paper's message on uncertainty quantification. The rest is housekeeping.

Two points need no action before acceptance:

- The sibling validation of Table 7 is not strictly nested. Nested, NN stays at 95 % correct, but its release-like trial rate rises from 41 to 52 %.
- The new-family rows of Table S10 use the new family's own production. No conclusion rests on them.

I need not see the paper again.
