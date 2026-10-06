# Referee report, third round: Reviewer B

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal and collection:** Research in Engineering Design (Springer), special collection "AI in Design for Manufacturing"
**Round:** third (second revision)
**Focus:** AI for design for manufacturing: data-driven manufacturability prediction, machine learning for process design and design for additive manufacturing, uncertainty quantification and trustworthy AI in engineering design

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The second revision takes up every point of my second-round report and every required change in my remit. The guard band of step 6 now has an exactly stated reference prior, and its dependence on that prior is shown under four further priors. The procedure's operating characteristics are tabulated by relation (Table A4), next to the coverage, width and centre of the interval rules (Table A3). The rescaled simulation is paired with a force trend, the jackknife+, the refit bootstrap, the noise floor of the Gaussian processes and the surrogate are described accurately, and Section 6.5 now shows how fixed-threshold classifiers, language-model checks and continuous relations would be scored, with a numbered minimal report. Every number I re-derived reproduces; what remains is that the archive still has no DOI, that step 6 is specified with applicability guards that its evaluation leaves out, and two small gaps against the paper's own minimal report.

## 2. Status of my second-round points

*How I checked.* All checks were read-only, on `results/*.csv` and the functions in `scripts/`. Python ran with bytecode writing disabled, and no pipeline script was rerun. The following reproduce to the precision printed:

- every cell of Table A4 (`panel_step6.csv`);
- the guard bands under all five priors (`panel_guard_priors.csv`);
- Table A3, whose new-family column I recomputed in the produced family's floor from `dec_intervals.csv` with the paper's estimator;
- the worked example;
- the new-family rows of Table 4 in both floors, and the M1sn row;
- the fixed-fit and refit paired differences of M1s and M1sn;
- the decomposition, the sibling strata and the force levels;
- the capability shares and the surrogate figures;
- the shares of GP fits at the noise bound;
- the order statistics used in `jackknife_plus`.

### New issues N1–N10

**N1. The guard band's prior and cap: resolved** (but see new issue A).

- **The prior.** It is stated exactly in Sect. 3.6, p. 9, l. 407–412: "weights the 47 distances of the evaluation grid within ±20 floors equally (0, ±0.5 to ±10 in steps of 0.5, ±12, ±15 and ±20; 87 % of the weight within ±10), drops infeasible requirements and searches g in steps of 0.25 floors up to 20". It is repeated in the caption of Fig. 4 (p. 18, l. 798–800) and in Table A1 (p. 25, l. 1117–1121).
- **Its status.** "g depends on the distribution of requirement distances that the team expects, not on rule and relation alone" (p. 9, l. 406–407; also Table 5, "Deciding a single design").
- **Its influence.** It is shown in Sect. 5.7, p. 17–18, l. 779–804, under the grid within ±5 floors and uniform priors within ±20 and ±50 floors, and in the worked example under the grid within ±3. Every band reproduces.
- **The rest of my request.**
  - The rules that never qualify are named (l. 776–778; note to Table A4).
  - The new-family outcome is conditioned (l. 803–804).
  - Fig. 4 shows the interpolated and extrapolated relations separately, with the bands marked.
- **The 20-floor cap** is still not justified in the paper; the editor made this optional. The response's reason holds: the uncapped bands of 23–42 floors would send 97–100 % of the verdicts at 10 floors to trial (my recomputation). That reason would fit in one clause at l. 411.
- **A prior-free g** is declined, with a fair argument (it answers a different question). I accept that.

**N2. Evidence behind RQ3 and the paper's own minimal report: partly resolved.**

*Now in the paper:*

- **Table A3:** coverage, median half-width and the decisive distance of the interval centre by relation; its note gives the GP fits at the noise bound.
- **Table A4:** g, the step-6 distances and the trial shares at 10 and 20 floors.
- **Guard performance:** one sentence (p. 18, l. 805–807).
- **The refit pair** of M1s and M1sn (p. 19, l. 857).
- **Table A5** (p. 27), which maps every other number to its script and result file.

This is what I asked for.

*Still open:*

- The archive: the reference reads "Zenodo, version 3, [DOI pending]" (p. 28, l. 1267–1268); see S6 and Section 5.
- Two small gaps against the paper's own checklist (new issues B and C).

**N3. Overreach in the headline statements: resolved.**

- **(a) The simulation.** The editor settled this point in the opposite direction (S1). The abstract's "the simulation as used, offset or rescaled, helped only across families" now agrees with Sect. 5.5 (p. 16, l. 697–702) and Sect. 6.1 (p. 20, l. 908–910).
- **(b) The force split.** It is given wherever the new-setting figure is quoted: the abstract; p. 20, l. 904; p. 23, l. 1047–1049. I checked that the best rule at each force is the one stated (`panel_force_levels.csv`):
  - at 100 kN, M1sn at 8.85 floors;
  - at 500 kN, NN at 4.85;
  - at 300 kN, NN and M1sn at 4.65.
- **(c) Coverage of the learned intervals.** The abstract and the conclusions (p. 23, l. 1053–1055) now say "85–96 % ... with a produced sibling, under 50 % extrapolating or for a new family", which is correct against Table A3. *Optional:* the interpolated case is left out, where coverage runs from 36 % (M3n) to 93 % (M2n, M5n); a parenthesis in the conclusions would complete it.
- **(d) Release-level requirements.** "Except a near-replicate's" appears in the abstract, Table 5 and the conclusions, and p. 18, l. 826–828 restricts the statement to indices up to 1.33. Table 5 no longer contradicts itself.
- **(e) The new family.** "16–17 floors in either family's floor" holds. The smallest safe distance is 15.8 floors (M2) in the new family's floor and 17.1 floors (M3) in the produced family's floor (`panel_source_floor.csv`).

**N4. Refit bootstrap: resolved.**

- **The design is described.** Sect. 4.4, p. 12, l. 508–513: "Its 200 resamples contain 48 of the 49 distinct configurations; in three of four draws a pattern is duplicated ... Its intervals thus show the effect of losing a pattern, not the sampling uncertainty of the reported values."
- **The edge-of-interval estimates** are named (p. 19, l. 857–859).
- **The noise floor.** The appendix says that it is not restricted to distinct series (p. 24, l. 1083–1085).
- **The paired interval.** The refit pair of M1s and M1sn reproduces from `rob_refit_paired.csv`: +1.35 to +3.6 floors with a sibling, +8.8 to +12 for a new setting, and M1s is never the more decisive. As the letter decided, it replaces the M1s–M1n pair I asked for.

**N5. Jackknife+ guarantee: resolved.**

- Sect. 3.3, p. 7, l. 313–316: the bounds "fall at or beyond the extreme leave-one-out values, which are used instead; under exchangeability these guarantee a coverage of 1−2/(n+1), 0.71 to 0.80 ..., approximately because the residuals are centred on their median".
- The appendix (p. 24, l. 1080–1083) describes the median centring and the extreme order statistics.
- The empirical coverage is compared with 7/9 (p. 16, l. 718–720).
- This matches `jackknife_plus`, whose upper index is min(⌈0.9(n+1)⌉, n).

**N6. Noise floor of the Gaussian processes: resolved.**

- **Its source and purpose:** "the calibration alternatives' series" (p. 7, l. 293–298).
- **How often it binds, and what follows** (p. 16, l. 714–718): "so this coverage comes from the quasi-replicate series rather than from the learner".
- **The fitting details:** maximum-marginal-likelihood estimates without hyperpriors, and the bound on the normalised scale (p. 24, l. 1069–1074).
- **The minimal report** now asks for it (item 3).
- **The shares reproduce:** 96.8 % (M5) and 99.2 % (M5n) of the fits with a sibling, and 100 % for a new setting and for a new family.

**N7. Labels in Sect. 6.1: resolved.**

- **(a)** p. 19, l. 869–870: "its distribution-free intervals are guaranteed their level only where the calibration alternatives are exchangeable".
- **(b)** p. 20, l. 910 adds "with a produced sibling".
- *Optional nit:* M3's centre decides at 9.9 floors with a sibling (Table A3). "Learned models predicted as well as the nearest produced setting" therefore still has one exception; "M5, M5n and M3n" would make the sentence exact.

**N8. Two senses of terms: resolved.**

- "Within a family" now always means both within-family relations (e.g. p. 15, l. 683; p. 17, l. 761; p. 19, l. 852; p. 20, l. 905).
- "Six to nine produced alternatives at two or three force levels" (p. 20, l. 908; p. 21, l. 942–943).

**N9. Transparency: resolved.** p. 21, l. 924–925: "arguably also the most transparent: the nearest produced setting points to the produced alternatives whose record it averages".

**N10. Surrogate: resolved.**

- **The method** takes one clause, and the surrogate is scored as a rule (p. 16, l. 707–711).
- **The figures reproduce:**
  - 12 of the 14 leave-one-out RMSEs lie below 2 floors (`ds_surrogate.csv`);
  - as M0, the surrogate decides at 108.65 floors against 108.35 for the simulation (`ds_surrogate_rule.csv`);
  - as M1 with a sibling, at 15.05 against 15.2.

### Remaining points 1–10

1. **Black-box formulation: resolved (S7).** Sect. 6.5, p. 22, l. 993–1004 covers:
   - fixed-threshold classifiers: binning by the true margin, or the requirement as an input; two thresholds to return a trial;
   - language-model checks: a requirement grid, repeated queries and the share of non-monotone sequences;
   - continuous relations: how strata are formed and how large they must be;
   - generative tools.
2. **Minimal report as a checklist: resolved.** p. 22, l. 1004–1010 gives six numbered items, including the source of the noise variance and the prompt and query protocol.
3. **AI-for-DFM references: resolved** (p. 3, l. 108–110). Both records check out in Crossref: Harvard Data Science Review, Special Issue 5 (2024), and Artificial Intelligence Review 58(9):288 (2025).
4. **Designer-study hypotheses: resolved.** p. 21, l. 947–952 gives two testable hypotheses with their measures, and Zhang et al. (2021) is used where it bears on them.
5. **Multi-task statement: resolved.** p. 21, l. 938–941: "a restricted intrinsic coregionalisation model (equal variances, one positive correlation between the families, shared length scales)".
6. **M5 at two alternatives: resolved.** Fig. 3 starts M5 at k = 3 in every panel, and p. 16, l. 731–733 says why.
7. **Abstract wording: resolved:** "was right for requirements over 3.4 floors from the truth".
8. **Number of rules: resolved.** The fourteen are the thirteen of the last version plus M1sn (Table 2), and M6 is "a robustness variant" in the notes to Tables 2 and 4.
9. **Cost sentence: resolved.** p. 19, l. 835–843 is now a list that names the ties and the coarseness of the scenario.
10. **Interval version of M1s (optional): not done.** The reason given is acceptable: the force trend dominates the scaled simulation as a point rule, and M2n is the interval rule without the simulation.

## 3. Required changes S1–S7 within my remit

**S1, the rescaled simulation: met.**

- **The rule.** M1sn is in Table 2 and in Table 4, with paired intervals.
  - With the fits fixed (`dec_paired.csv`), M1s minus M1sn is +1.35 floors [0.65, 2.95] with a sibling and +11.0 [5.3, 13.8] for a new setting.
  - With refitting, see N4.
- **The text.** Sections 5.5, 6.1 and 6.3, the abstract and the conclusions are rewritten.
- **The comparison with NN.** The force trend's 8.2 floors against NN's 8.5 are reported without interpretation.
- **The decomposition.** Its treatment of M1sn is stated (p. 15, l. 683–684), and it reproduces from `panel_decomposition.csv`.

**S2, the guard band: met,** subject to new issues A and B.

- **(a)** The prior is stated exactly. The "why" (l. 410–412) describes the prior rather than arguing for it. But (c) now makes the team's own distribution the governing one, which is the substantive point.
- **(b)** g is reported under four further priors.
- **(c)** Its conditional status is stated in Sect. 3.6, Table 5 and Table A1.
- **(d)** Tables A3 and A4 cover the requested rows and columns, and every cell of Table A4 reproduces. The rules that never qualify are named, and guard performance has a sentence.
- **(e)** The new-family outcome is attributed to the prior and the cap.
- **(f)** Fig. 4 has four panels, marks the bands and states the "at least the given margin" convention.
- **(g)** The worked example says that the requirement was chosen for illustration and that g was estimated on data that include the case. I reproduced it from `dec_intervals.csv`:
  - NN predicts 14.99 mm, a margin of 6.2 floors;
  - the truth lies 8.4 floors below the limit;
  - the widened intervals of M2, M5 and M5n are as printed;
  - no guard fires for this case.

**S3, the new family in the produced family's floor: met** for my point N3(e).

- All fifteen new-family rows of Table 4 and their intervals reproduce from `panel_source_floor.csv`.
- No safest rule is named.
- The new-family column of Table A3 reproduces in the produced family's floor.

**S4: met within my remit.** This covers the statements on learning, the labels and the terms (N3(b)–(d), N7 and N8 above).

**S5, the jackknife+, the refit bootstrap and the surrogate: met** (N4, N5 and N10 above).

**S6, traceability and the archive: partly met.**

*Met:*

- The numbers that carry claims are in the paper: Tables A3 and A4, and the new family in both floors.
- Table A5 traces the rest. The few numbers it does not list, such as 0.17 mm, 0.8 mm and 1.3°, are products of Tables 3 and 4.

*Not met:*

- **The DOI.** The archive has none: the reference list reads "[DOI pending]" (p. 28, l. 1267–1268), and `paper/refs.bib` still holds the placeholder.
- **The availability statements.** They now say that the files "are archived with the code" and that the pipeline "is archived ... on Zenodo" (p. 24, l. 1100–1101 and l. 1103–1104; p. 25, l. 1130). These statements are not true until the deposit exists.
- **A practical route.** Zenodo can reserve a DOI before a deposit is published, so the manuscript can carry the DOI now.

**S7, reuse for other AI-based DFM tools: met.**

- Sect. 6.5 (p. 22, l. 987–1010; p. 23, l. 1013–1016) covers the cases of my remaining point 1.
- Table 6 is marked as an untested proposal.
- Floors are said to be comparable within a protocol, not across processes.
- Injection moulding has a floor per cavity.
- The section takes about two-thirds of a page, in line with the letter.

**Does the paper meet its own minimal report (p. 22, l. 1005–1010)? Nearly.**

| Item | Status | Where |
|---|---|---|
| 1. The floor, its protocol, variance components and lag dependence | met | Table 3, Sect. 5.1 |
| 2. Decisive and safe distances by relation, with refit intervals and one-sided values | largely met: the refit intervals cover decisive distances only (new issue C) | Table 4, including the false-accept column; Table A2 |
| 3. Coverage and half-width of interval rules, and the source of the noise variance | met | Table A3, Sect. 3.3, appendix |
| 4. The nearest-produced-setting and no-simulation baselines | met | Table 4 |
| 5. Guard bands with their prior, trial rates and guard performance | largely met: the guard-performance sentence lacks its requirement distance, and the role of the guards in step 6 is unspecified (new issues A and B) | Sect. 5.7, Table A4 |
| 6. Prompt and query protocol for language-model tools | not applicable | – |

## 4. New issues arising from this revision

### A. Step 6 is specified with the applicability guards but evaluated without them (minor; requires correction)

*Location:* Sect. 3.6, p. 10, l. 434–437; Fig. 1, step-6 box (p. 10, l. 426–430); Table 5, "Deciding a single design" (p. 20, l. 885–888); Sect. 5.7, p. 17–18, l. 772–807; Table A4 and its note (p. 27).

*The problem.*

- **The specification.** Step 6 "applies the rule qualified for it and the guards ... or a trial when a guard fires". Table 5 has the same rule: "a margin inside it, or a fired guard, means a trial".
- **The evaluation.** `step6` in `panel.py` widens each interval by g and applies no guard. Table A4, Fig. 4 and Sect. 5.7 therefore describe step 6 without the guards.
- **Where the guards fire.** In this design they coincide with relations (`dec_guard.csv`):
  - the range guard fires for all 84 extrapolated cases and all 126 new-family cases;
  - the family guard fires for all 126 new-family cases;
  - the novelty guard fires for 18 of the 42 interpolated cases and 66 of the 84 extrapolated ones.
- **The consequence.** Under the procedure as written, every extrapolated and every new-family design goes to trial, whatever g and whatever the prior. With the novelty guard, 35 of the 80 interpolated verdicts of the nearest setting (44 %) would also go to trial. All 35 are verdicts that step 6 decides correctly at 10 floors, and Table A4 shows 0 % trial for them.
- **The statements affected.** All of the following describe a procedure that the paper does not specify:
  - "for an extrapolated setting it needs 7.0 floors and sends a quarter to trial" (l. 776);
  - the extrapolated columns of Table A4;
  - the new-family bands under a uniform prior within ±50 floors (l. 801–803).
- **Why it is now harder to see.** The second-round text said that "the range guard refuses exactly the extrapolated forces". This revision removed that sentence (`main_diff.pdf`).

*Why it matters.* Step 6 is the paper's procedure for single decisions, and Table A4 gives its operating characteristics. A reader who implements Sect. 3.6 as written will not obtain Table A4.

*What would fix it.* State which guards step 6 applies; no new analysis is needed.

- **Preferred route.** It fits the results and keeps the letter's S2(e) framing intact:
  - the relation-specific guard band takes the place of the range and family guards, which here coincide with the extrapolated and new-family relations;
  - the novelty guard is reported as a diagnostic, not applied, since most of its refusals would have been right (96 % for the nearest setting, 73 % for M5, for a new setting).

  Say this in Sect. 3.6, in Fig. 1 and in Table 5, and add "no applicability guard is applied" to the note of Table A4.
- **Alternative route.** Keep the guards in step 6. Table A4 and l. 776 and 801–804 must then report that every extrapolated and new-family design goes to trial, and the interpolated trial shares must include the refusals of the novelty guard.

### B. The guard-performance sentence lacks its condition (minor)

*Location:* Sect. 5.7, p. 18, l. 805–807.

*The problem.* The sentence reads: "96 % of the range guard's refusals for a new setting would have been right for the nearest setting and 72 % for M5 (novelty guard 96 and 73 %)". The figures reproduce, but they are evaluated at requirements 10 floors from the truth (`D_CHECK` in `guard.py`), and the sentence does not say so. Without a requirement distance, "would have been right" is not defined.

*Fix.* Add "at requirements 10 floors from the truth", and say that the range guard refuses exactly the extrapolated designs (84 of the 126 new-setting cases). This also serves issue A.

### C. Item 2 of the minimal report: refit intervals of the safe distances (minor; continues N2)

*Location:* Sect. 6.5, p. 22, l. 1006; Table A2, last row (p. 26, l. 1169); Sect. 5.9, p. 19, l. 857–859.

*The problem.* Item 2 asks for distances "with refit intervals". Sect. 5.9, newly, cites "the safe distances of M2 and M5" as lying at the edge of their refit intervals. Those intervals are not in the paper, because Table A2 gives refit intervals for decisive distances only. They are in `rob_refit.csv`: with a sibling, M2 has 0.15 floors [0.15, 1.35] and M5 0.75 [0.75, 2.96].

*Fix.* Give the refit row of Table A2 as δd/δs, like the other rows of that table. No computation is needed.

## 5. Accuracy of the response

- **The DOI.** This is the one statement about my points that does not match the manuscript, and the editor made it a condition of acceptance.
  - *The response says:*
    - "the author mints the DOI before resubmission and inserts it in the reference list" (Part 1, S6);
    - "The manuscript will not be resubmitted without it" (Part 3);
    - the DOI "will replace the placeholder ... before resubmission" (Part 8).
  - *The manuscript and files show:* the resubmitted manuscript still reads "[DOI pending]" (p. 28, l. 1267–1268), and `.zenodo.json` holds prepared metadata but no DOI.
- **Trial rates under the uncapped bands (immaterial).** The response says that the uncapped bands send "94–100 % of the verdicts at requirements 10 floors from the truth to trial and 82–100 % of those at 20 floors". For the five bands it names, I obtain 97–100 % and 82–99 %. The conclusion is unaffected.
- **Everything else in Parts 1, 2 and 5 that concerns my points matches** the manuscript and the files. This includes:
  - the uncapped bands themselves (23.25, 23.0, 41.75, 42.25 and 42.25 floors);
  - the noise bound binding in 84–93 % of the pooled fits;
  - the fixed-fit and refit pairs of M1s and M1sn;
  - the scores of the surrogate;
  - the Crossref records;
  - the page and line locations I followed.

## 6. Recommendation

**Accept subject to the minor corrections listed below.**

The paper now does what this collection needs from it: it offers a production-referenced standard for evaluating design-stage manufacturability decisions, AI-based or not. It reports, by evidence relation, how close to a requirement a rule decides and how close it can be relied on. It gives a procedure for single decisions whose dependence on the requirement prior is explicit. And it gives a conditioned, honest answer about what classical small-data learning and a low-fidelity simulator add. Every number I re-derived reproduces, and the required changes in my remit are met, except the archive. The new issue A concerns how the procedure is specified, not its numbers; a sentence or two and a table note fix it. None of the corrections needs new data or modelling, and the editor can check all of them without another review round.

*Corrections:*

1. Deposit the archive with the code, the feature tables and the result files named in Table A5, and cite its DOI in the reference list and in the availability statements. Until then, those statements must not say that the files "are archived" (S6).
2. State which applicability guards step 6 applies, and make Sect. 3.6, Fig. 1, Table 5, Sect. 5.7 and the note to Table A4 consistent with that choice (issue A).
3. Give the requirement distance (10 floors) in the guard-performance sentence, and say that the range guard refuses exactly the extrapolated designs (issue B).
4. Add the refit intervals of the safe distances to Table A2 (issue C).

*Optional:*

- one clause justifying the 20-floor cap (N1);
- the interpolated coverage in the conclusions (N3(c));
- "M5, M5n and M3n" in place of "learned models" in the RQ3 sentence (N7(b)).

## 7. Confidential comments to the editor

The revision is careful, and apart from the DOI the response is exact where it concerns my points. I re-derived Tables A3 and A4 in full, the guard bands under all five priors, the worked example, the new-family columns in both floors, the M1sn comparisons, the strata, the decomposition, the capability shares and the surrogate figures; all reproduce. The DOI is the point on which to hold firm: the response says three times that the DOI would be in place before resubmission, and it is not. I would make final acceptance conditional on a resolving DOI whose deposit holds the files listed in Table A5. Issue A is the only substantive point I found. It changes no number, only what Table A4 describes, and you can check the fix yourself. I do not need to see the manuscript again.
