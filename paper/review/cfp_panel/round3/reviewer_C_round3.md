# Referee report, third round: Reviewer C

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal and collection:** Research in Engineering Design (Springer), Special Collection "AI in Design for Manufacturing"
**Round:** third (second revision; a short check of the points in my remit, at the editor's request)
**Reviewer focus:** process planning and tryout (sheet-metal forming among other processes), statistical process control, process capability and measurement systems analysis, DFM practice in companies

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The author has made the editor's required changes in my remit carefully and, with few exceptions, completely: the new family is scored in the produced family's floor, with intervals and no rule named the safest; the strata and the force split stand wherever the abstract, Sections 5.4 and 6.1, Table 5 and the conclusions quote the headline distances; Table 3 uses one consistent aggregate; the capability-anchored test is declared one-sided; and the guard bands have a table (Table A4), a stated prior and a conditional reading for the new family. Every number I re-derived from the released files reproduces. Three things still matter: the archive DOI, on which the editor made acceptance depend, is still "[DOI pending]"; the short-series analysis is still summarised beyond what it tests, in one surviving clause (Sect. 5.6) and one new clause (Sect. 6.5); and the abstract and the conclusions have dropped the performance index of 1.33, to which Section 5.8 now restricts the release-level statement. Two further one-clause corrections concern Section 6.4 and Table 5, and apart from the DOI every remaining item is a change of a clause or two.

## 2. Status of my second-round points

**What I re-derived.** All checks were read-only, on `results/*.csv`; I did not rerun the pipeline. All of the following reproduce.

- **Table 3, all 14 rows** (`panel_floor_protocol.csv`):
  - σw < σLT in every row;
  - √(σb² + σw²) matches σLT to within 2 %;
  - the normal model reproduces the floors to within 11.7 %;
  - the subgroup-of-five factor is 1.13–2.07, median 1.33.
- **The sibling strata:** 0.85, 2.45 and 4.85 floors; in the resolvable stratum, 4.45 for the force trend and 9.65 for M5.
- **The force split:**
  - the nearest setting needs 4.65 floors interpolated, 4.85 at 500 kN and 11.0 at 100 kN;
  - the force trend needs 8.85 at both extrapolated forces.
- **The decomposition in both floors:** 67/6 %, 69/6 %, 68/15 %, and 71/15 % with M1sn.
- **The new-family column of Table 4 in the produced family's floor:** the entries, their intervals, and the paired M3 − M2 differences (−16 to +7 and −3 to +8 floors; M3 has the smaller safe distance in 83 % and 25 % of resamples).
- **The capability-anchored test:**
  - positions of 1.03, 1.75, 2.46 and 3.14 floors;
  - right/false-reject/trial shares of 91/9/0, 65/35/0, 44/2/53, 32/16/52, 81/19/0 and 79/21/0;
  - at most 54 % right for a new family.
- **The guard bands:** Table A4 cell by cell (`panel_step6.csv`), and the bands under the four further priors (`panel_guard_priors.csv`).
- **The worked example:** the stored intervals, the margins of 6.2 and 8.4 floors, the widened intervals of M2, M5 and M5n, and the typicality claim (all 42 interpolated cases right at +8.5 floors), from `dec_intervals.csv`.
- **The short-series bounds:** 1.5 floors within a family and 4.0 for a new family (`rob_decisions.csv`).
- **The cost map:** the tie at zero cost with a sibling, and the force trend alone at zero cost for a new setting.
- **The regenerated physical-units file.**
- **The Section 5.1 figures** (`meas_floor.csv`, `panel_variogram.csv`, `rob_floor_between.csv`, `inline_drift.csv`).
- **The M1s − M1sn intervals,** paired and refitted.
- **The drawing-nominal baseline** (1.9 against 7.5 floors) **and M1n for the arm angle and the dome** (44 and 27 floors).

### Open points under the first-round comments

**C1. The production floor as a production construct: resolved.**

- **(i) Table 3.** See N4.
- **(ii) Positioning: resolved.**
  - The text now reads: "it is closer to a time-different intermediate-precision limit (ISO, 2023) of batch centres within a run; in the terms of ISO 22514-2 the runs follow a time-dependent model with varying location" (p. 6, ll. 253–256). This is exactly what I asked for.
  - *The editions.* My query was wrong. ISO 5725-2:2025 (third edition, December 2025) and ISO 22514-2:2026 (third edition, February 2026) are both in the ISO catalogue, as the response says. I withdraw the query.
- **(iii) Assumption A2: resolved.** It now reads "the variation within the runs from which it is estimated is like that within future runs" (p. 6, ll. 260–261).

**C2. Assumption A3 and the source of the drift: resolved.**

- The abstract now defines the floor by the "drift and scatter of production and measurement".
- The scan-order question was optional and has not yet been asked.
- *Optional:* the Introduction still defines the floor by "drift and scatter" alone (p. 2, ll. 71–73). Two words would align it with the abstract.

**C3. Decision situations and release decisions: resolved.**

- For the capability-anchored test, see N2.
- The trial's own error is stated: "being a run, also carries the variation between runs, so no decision is reliable closer to the requirement than the trial replacing it" (p. 9, ll. 377–380). Section 5.1 repeats it (p. 12, ll. 549–550).

**C4. The within-family headline in stratified terms: resolved, to the standard the editor set (S4).**

- The abstract gives "3.4 floors from the truth (0.85 for near-replicates, 4.9 for resolvable siblings)" and "4.7 floors interpolating, 4.9 extrapolating to 500 kN and 8.9 to 100 kN, with a stroke-speed change". Section 6.1 (p. 19, l. 872 – p. 20, l. 905), Table 5 and the conclusions (p. 23, ll. 1045–1050) do the same.
- Section 5.4:
  - gives all three strata;
  - offers my reading as an observation with the right caveat: "Taken together, the nearest setting decided at about 5 floors whenever the new design differed resolvably and force and speed did not change together, though each stratum has 34 to 58 cases …" (p. 15, ll. 674–677);
  - labels the gradient "Pooled over strata" (l. 685).
- Section 6.6 now says "The extrapolation to 100 kN is confounded with stroke speed" (p. 23, ll. 1030–1031).
- *The smaller point* is taken up: "this baseline is M1n, at 44 and 27 floors" (p. 16, ll. 707–708). I accept the editor's correction of my figure of 130 floors.
- One new pooled quotation has entered Section 6.4 (Section 4, item B).

**C5. How representative the simulation is: resolved.**

- (a) The envelope now varies "sheet thickness and friction but not material properties" (p. 7, ll. 292–293).
- (b) Section 6.3 now speaks of "The simulated force trend of the two draw-ins" (p. 21, l. 935).
- (c) The editor reversed the direction of my point (S1). The abstract and the conclusions now say "offset or rescaled", and I confirmed the M1s − M1sn intervals.

**C6. What a design or process-planning team would need: partly resolved, through (a) only.**

- **(a) Short runs: partly resolved.** See N1.
- **(b) Placement at production part approval: resolved.**
  - The text reads: "production part approval, whose initial process study covers the released setting, supplies the floor but not the variants". It also names the evidence relation that each source supports (p. 21, ll. 926–930).
  - *Optional precision.* An initial process study under PPAP typically measures subgroups (at least 100 readings in at least 25 subgroups) from a significant production run of at least 300 consecutive parts. The floor it supplies is therefore one of its own sampling protocol: the subgroup factor of Section 5.1 applies, and the longest lag is shorter. "Supplies a floor in its own sampling protocol (Section 5.1)" would make the sentence exact.
- **(c) Sampled measurement: resolved.** The figures (p. 12, ll. 537–538) reproduce from the corrected components.

**C7. Transfer to other processes: resolved.**

- Table 6 is marked "an untested proposal".
- For injection moulding the floor is taken "per cavity; cavity offsets as effects", and for machining "batch centres within an offset interval".
- The text says that distances in floors are comparable within a protocol, not across processes (p. 23, ll. 1013–1016).
- The two further columns were suggestions, so leaving them out is acceptable.

**C8. Contribution: resolved.** The sharper practical statement is adopted (p. 20, l. 919 – p. 21, l. 924).

### New issues of the second round

**N1. The short-series analysis truncated only the calibration side: partly resolved.**

- *What is fixed.*
  - "Calibrated" replaces "qualified".
  - Section 5.6 adds "here scored against the truths and floors of the full series" (p. 17, ll. 762–763), and the note to Table A2 says the same.
  - I confirmed in `robustness.py` (item 16) that the truths stay those of the 500-part series.
- *What survives.* The same sentence ends "and only the floor needs a run long enough to show the drift" (p. 17, l. 763).
- *What is new in this revision.* Section 6.5 now reads "here rules calibrated on about 50 parts per variant scored as well as with full series, and only the floor needed long runs" (p. 22, ll. 990–991). This replaces the second-round caveat "how many long runs a floor needs was not tested".
- *Why this is still a problem.*
  - Both clauses state, as a finding, that only the floor needs long runs. Yet every held-out truth in the variant came from the full series.
  - The clauses therefore go beyond the variant as the letter describes it: "the truths and the floors are those of the full series". Whether truths from short runs would do was never put to the test.
  - By the paper's own figure, the 95th percentiles of two batches of 100 parts differ by 0.92–1.49 floors (p. 12, ll. 546–548). That is more than the near-replicate distance (0.85 floors) and more than the nearest setting's guard band with a sibling (0.25 floors).
  - The Section 6.5 sentence sits in the list of prerequisites that a team will read before it plans its runs.
- *What would resolve it.* In both places write, for example: "the floor and the held-out truths came from the full 500-part series; whether truths from short runs suffice for qualification was not tested". No new analysis is needed.

**N2. The capability-anchored test scores only one side: resolved.**

- The text now reads: "The test is one-sided by construction: every alternative meets these limits, so a verdict can only be right, a false reject or a trial, and a rule biased towards meets scores well" (p. 18, l. 828 – p. 19, l. 830).
- The shares are given as rates, and they reproduce.
- "Decided at the design stage only with a produced sibling" is at p. 19, ll. 834–835.
- Section 3.1 now "locates such limits relative to the distances, without deciding them" (p. 6, l. 239).

**N3. The new family is qualified in one floor and decided in another: resolved.**

- The note to Table 4 says that a new family "is scored in the floor of the produced family (Section 3.2)". The table gives safe-distance intervals for M2, M3 and M5 and a decisive-distance interval for M2.
- Section 5.3 gives both floors and says that "two transfers do not resolve which rule is safest" (p. 14, ll. 629–636).
- The abstract, Table 5 and the conclusions name the unit.
- All entries reproduce from `panel_source_floor.csv` and `panel_source_floor_paired.csv`.

**N4. Table 3 combines different summaries: resolved.**

- The note now reads "classical statistics pooled over the series as root mean squares".
- σw < σLT in all 14 rows, and the three components are mutually consistent (see the checks above).
- One floor is now "0.7 to 1.7 long-term standard deviations" (p. 12, ll. 532–533).

**N5. Numbers that are no longer tabulated have no reference a reader can follow: partly resolved.**

- *Done.* Table A5 maps the quoted numbers, section by section, to scripts and result files. Every file it names exists. The Section 5.1 numbers I looked up are in the files it lists for that section.
- *Not done.* The archive is still cited as "Zenodo, version 3, [DOI pending]" (p. 28, ll. 1267–1268), and `.zenodo.json` holds no DOI. See S6.

**N6. The guard bands exist only in one sentence: resolved.**

- Table A4 gives g, the step-6 distances and T10/T20 by relation for nine rules.
- The prior is stated exactly (p. 9, ll. 406–412; caption of Fig. 4; Table A1), and its influence is shown (p. 17, l. 779 – p. 18, l. 803).
- The new-family statement is now conditional: "That every new-family design goes to trial thus follows from the reference prior and the 20-floor cap, as the practice of trying out every new die would have it" (p. 18, ll. 803–804).
- All of this reproduces.

**N7. The relation-specific cost comparison rests on the gross-failure scenario: resolved.**

- The coarseness of the scenario and the tie are stated (p. 19, ll. 835–843).
- *Optional:* the ranking for a new setting rests on three verdicts. The nearest setting makes three false rejects among the 108 decisions and the force trend none (`scen_scores.csv`). Saying so would match the paper's restraint about half-floor differences elsewhere.

**N8. The result file cited for distances in physical units is quantised: resolved.**

- `panel_physical_units.csv` is regenerated on a grid of 0.05 pooled floors, and its units are exactly floors × pooled floor.
- The flange waviness with a sibling is now 0.0032 mm.

### Remaining minor points

| Point | Status | Evidence |
|---|---|---|
| 1. "Within a family" in two senses | resolved | "with a produced sibling" for the sibling relation; each remaining "within a family" covers both within-family relations (e.g. p. 15, l. 684; p. 19, l. 852; p. 23, l. 1050) |
| 2. Note to Table A2 (floor between series) | resolved | "contains the lubrication effect and, for a new variant, the series that NN averages, which makes it close to circular there" (p. 26) |
| 3. Lag ranges | resolved | "(averages over the two geometries)" (p. 12, ll. 535–536) |
| 4. "The distances are exact" | resolved | "exact up to the 0.05-floor grid" (p. 9, l. 369) |
| 5. "Capability" for the 95th percentile | resolved | "predicted 95th percentile" (Table 5; p. 20, l. 916) |
| 6. "Measurement resolution" | resolved | defined in Table A1; one harmless leftover, "A3 holds for repeatability and resolution" (p. 12, ll. 540–541) |
| 7. Worked example | resolved | "chosen for illustration", "by which tryout sets the blank-holder force", and the typicality sentence (p. 18, ll. 808–821); reproduced |
| 8. `alt_mrc.csv` | resolved | the response is corrected; the file is unchanged; the paper's 21–67 kN rests on `rob_bhf_pairs.csv`, which agrees |
| 9. M6 | resolved | notes to Tables 2 and 4 |
| 10. Interval rules named in Sect. 5.3 | resolved | "(M2, M2n, M3, M3n, M5, M5n)" (p. 13, ll. 591–592) |
| 11. Two-sided wall angle | not done | optional per the letter; acceptable |
| 12. "Except a near-replicate's" | resolved | abstract, Table 5 and conclusions; but see Section 4, item A |

## 3. Required changes S1–S7 within my remit

| Item | Status | Evidence |
|---|---|---|
| S1 (supersedes my C5(c)) | met | M1sn is in Tables 2 and 4. Sect. 5.5 now reads "Rescaled, it does no better" (+0.65 to +3.0 and +5.3 to +13.8 floors; reproduced). The abstract says "offset or rescaled". |
| S2 (my N6) | met | Table A4; the prior stated exactly; four further priors; the new-family statement conditional; Fig. 4 split by relation |
| S3 (my N3) | met | see N3 |
| S4 (my C4, N2, m1, m12) | largely met | Every location the letter named carries the strata and the force split. Two residual inconsistencies remain (Section 4, items A and B). |
| S5 (my N4, N1 and C3) | partly met | Table 3 and the trial's own error are met. "Calibrated" is in, but the short-run claim survives in two clauses (N1). |
| S6 (my N5, N8, m8) | not met in its central condition | Table A5 and the corrected result files are in. The DOI is still pending, although the letter made acceptance depend on it. The availability statements (p. 24, ll. 1098–1104; p. 25, ll. 1130–1132) say in the present tense that the code, feature tables and results are archived on Zenodo; that cannot be checked until the deposit has a DOI. |
| S7 (my C7) | met | see C7 |

*For the deposit (not a condition of mine).* Neither `.zenodo.json` nor `CITATION.cff` names a licence, and the repository has no licence file. The editor may wish to check at deposit that the code carries a licence and that the derived feature tables carry CC BY 4.0, the licence of their source datasets.

## 4. New issues arising from this revision

**Major: none.**

**A. The abstract and the conclusions drop the index to which Section 5.8 restricts the release-level statement** (abstract; p. 23, ll. 1050–1052).

- *What changed.* The second-round abstract said "requirements at a performance index of 1.33". The revised abstract and conclusions write "Release-level requirements lay inside every decisive distance except a near-replicate's". But Section 5.8 restricts the statement: "up to an index of 1.33 they lie inside every decisive distance except a near-replicate sibling's" (p. 18, ll. 826–828).
- *Why the restriction is needed.* At indices of 1.67 and 2.0 the limits lie 2.46 and 3.14 floors above the 95th percentile. That is at, and then beyond, the 2.45 floors at which the nearest setting decides with one resolvable sibling (34 cases; `panel_sibling_strata.csv`).
- *Why it matters.*
  - Section 3.1 cites "a performance index of 1.33 or more" as the release criterion (p. 6, ll. 236–237).
  - Under AIAG PPAP (4th edn., §2.2.11.3), however, an initial process study meets the acceptance criteria outright only above 1.67. Between 1.33 and 1.67 it may be acceptable after review with the customer.
  - A quality engineer will therefore read "release-level" as including 1.67. At that index the abstract's statement no longer holds for the stratum with one resolvable sibling.
- *What would resolve it.*
  - Write "Requirements at a performance index of 1.33 lay inside …" in the abstract and the conclusions, as Table 5 already does.
  - Optionally, add the 1.67 criterion in Section 3.1, citing the AIAG reference already in the list.

**B. Section 6.4 quotes the pooled gradient without the strata** (p. 21, ll. 961–964).

- *The problem.* A new sentence reads: "The growth of the decisive distance from about 3 to 8 and over 30 floors says for which overlaps of development … preliminary manufacturability information can be released". It draws a design implication from the pooled 3.4 → 8.2 floors. S4 asked for the strata wherever the pooled figures are quoted.
- *Why it matters.* Within a family, the strata are what say when preliminary information is fit to release, not the pooled gradient:
  - about one floor for near-replicates;
  - about 5 floors for resolvable variants and for interpolated or same-speed settings;
  - 9–11 floors where force and speed changed together.
- *What would resolve it.* Insert "pooled over strata", or give the stratified figures.

**C. Table 5, row "New process setting", gives two rules' figures as if each held for both** (p. 20).

- *The problem.* The row reads "nearest setting or force trend right beyond 4.7 floors interpolated, 4.9 extrapolated to 500 kN and 8.9 to 100 kN". But:
  - the 4.9 floors are the nearest setting's; the force trend needs 8.9 at 500 kN;
  - the 8.9 floors are the force trend's; the nearest setting needs 11 at 100 kN (p. 15, ll. 672–674).
- *Why it matters.* This is the guidance table, and a planner who uses the nearest setting at 100 kN needs 11 floors, not 8.9.
- *What would resolve it.* Write "the better of the nearest setting and the force trend", or name the rule for each figure.

The new short-run clause in Section 6.5 is also introduced by this revision; I treat it under N1.

## 5. Accuracy of the response (my points)

1. **The DOI.** This is the one statement that the resubmission itself contradicts.
   - *The response says:* the DOI is minted "before resubmission" (Part 1, S6; Part 8), and "The manuscript will not be resubmitted without it" (Part 3).
   - *The manuscript has:* the resubmitted version still cites "[DOI pending]" (p. 28, ll. 1267–1268; `canseven2026archive` in `refs.bib`).
2. **The strata (S4 row of Part 1).**
   - *The response says:* "Wherever it is quoted as a headline, the nearest setting's strata are given."
   - *The manuscript has:* this holds everywhere except the new sentence in Section 6.4 (item B).
3. **The short series (A-m2 in Part 4; C-N1 in Part 6).**
   - *The response says:* it quotes the narrowed sentences.
   - *The manuscript has:* those sentences end with "and only the floor needs a run long enough to show the drift" and "and only the floor needed long runs". The response leaves these clauses out, and does not mention that the second-round caveat in Section 6.5 ("how many long runs a floor needs was not tested") was deleted.
4. **The worked example (C-m7).**
   - *The response says:* the measurement resolution (0.38 floors) is small against the example's margin (6.2 floors).
   - *The manuscript has:* no such sentence. This is immaterial.
5. **Where the response is right and I was wrong:** the editions of ISO 5725-2 and ISO 22514-2 (C1(ii)).

Everything else in Part 6, and in the provenance table of Part 7 as far as it concerns my points, matches the manuscript and the files. This includes:

- σw exceeding σLT in 5 of 126 series, by at most 0.27 %;
- the subgroup factor;
- the flange waviness at 0.0032 mm;
- the 1.5- and 4-floor short-series bounds;
- the guard bands of Table A4.

## 6. Recommendation

**Accept subject to the minor corrections listed below.**

The paper now meets the substance of every point in my remit, and all of it reproduces from the released files:

- the floor is positioned exactly, and its components are consistent;
- the new family is scored in the unit a team would have;
- the headline is stated in strata;
- the capability-anchored test is described as what it is;
- the guard bands are reported with their prior.

What remains is either administrative or a matter of a few clauses, and the editor can check it without another round:

1. **The DOI (S6).** Mint the archive DOI and cite it in the reference list and the availability statements. Make the deposit hold exactly the files that produce the numbers of this version.
2. **The short-run claim (N1).** Remove it from Section 5.6 (p. 17, l. 763) and Section 6.5 (p. 22, ll. 990–991), as proposed under N1.
3. **The index (item A).** Restore "at a performance index of 1.33" in the release-level sentence of the abstract and of the conclusions.
4. **Section 6.4 (item B).** Give the strata there, or write "pooled over strata" (p. 21, ll. 961–964).
5. **Table 5 (item C).** In the new-setting row, attribute each figure to its rule.

I do not need to see the manuscript again.

## 7. Confidential comments to the editor

The revision is careful and honest, and I found no computational error: Table 3, Table A4, the new-family column of Table 4, the capability shares, the worked example and the short-series bounds all reproduce. The only unmet condition is the one your letter made decisive: the DOI is still a placeholder, although the response says that the manuscript would not be resubmitted without it. I would not issue acceptance until the deposit exists and matches the result files. Beyond that, the short-series clause (N1) matters most to me. The revision removed the caveat in Section 6.5 on which I had relied, and put a stronger claim in its place, in the paragraph a team reads for prerequisites. The other items are one-clause fixes. My second-round doubt about the ISO editions was mistaken; the author was right, and I say so in the report.
