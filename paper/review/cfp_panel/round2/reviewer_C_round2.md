# Referee report, second round: Reviewer C

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal and collection:** Research in Engineering Design (Springer), Special Collection "AI in Design for Manufacturing"
**Round:** second (revised version)
**Reviewer focus:** process planning and tryout (sheet-metal forming among other processes), statistical process control, process capability and measurement systems analysis, DFM practice in companies

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

---

## 1. Summary of the revision

The revision is substantial and responds to my first-round report and to R1–R5 in good faith. The floor is now positioned against ISO 5725, labelled a within-run production-and-measurement floor and reported with its variance components, lag profile and ratio to the part scatter; the release-level consequence is stated in capability terms; and the confounds I raised (near-replicate siblings, force with stroke speed, run metadata, a production-informed new-family baseline, the in-line drift analysis) are reported and carried into the threats to validity. A guard-band version of step 6, a worked example, a process mapping and a reporting standard make the procedure usable, the paper is eight pages shorter, and every number I re-derived from the released files reproduces. What remains is mostly a matter of claims and summaries: the abstract and conclusions still carry the pooled within-family gradient that the paper's own strata and force split dissolve, three new analyses are summarised beyond what their design tests, and the archive DOI and the result-file references that should replace the removed supplement are missing. I recommend minor revision.

## 2. Assessment

- **Originality: adequate.** The novelty is now correctly placed in using a precision-type limit of batch centres as the unit of a design decision rule, and in the evaluation protocol around it, not in the limit itself.
- **Significance for design research: adequate.** Section 6.4 now argues strand by strand, and the practical message (release-level limits lie inside the decisive distances, so trials remain necessary) is stated, but the support is one dataset and no design team.
- **Significance for the collection (AI in DFM): adequate.** The paper now frames itself as an evaluation standard and adds a black-box formulation and a minimal reporting standard (Sect. 6.5), which fit the call, and the AI findings are now conditioned on the small-data regime.
- **Technical soundness: adequate.** The analysis is careful and reproducible: the new GP noise floor uses only calibration alternatives, and the refit bootstrap keeps the relation. But the floor's construct limits can only be stated, not removed, with these data, and three new analyses test less than the conclusions drawn from them (N1–N3).
- **Evidence supports the claims: weak → adequate.** The body now reports the strata, force levels, confounds and capability anchors that qualify the findings, but the abstract and conclusions have not caught up (C4).
- **Clarity, organisation and length: adequate.** The paper is much improved (30 instead of 38 pages, seven core rules, a notation table, a worked example). But Sections 5.3–5.9 still pack many numbers into single sentences, the guard bands exist only in prose, and "within a family" has two meanings.
- **Positioning and references: adequate.** The design-literature positioning is now broad (Sects. 2.2, 6.4), and ISO 5725, ISO 22514-2, PPAP and Tata and Thornton are cited, but the relation to the production-quality concepts is one sentence (p. 5, ll. 214–222).
- **Fit to RED: adequate.** This is a method with an evaluation and stated prerequisites; applicability beyond one process is argued through Table 6 rather than shown, which is acceptable for this paper.

**Verification.** I re-derived the following from the released result files, read-only:

- every cell of Table 4 that I compared (core rules, all relations, the pooled columns, the bootstrap intervals);
- the sibling strata and force levels (Sect. 5.4) and the paired differences (Sect. 5.5);
- the guard bands and step-6 figures, and the worked example (Sect. 5.7);
- the capability-anchored shares and the cost map (Sect. 5.8);
- the Table A2 rows for the temperature adjustment, the dropped warm-up, the floor between series and the short calibration series, and the refit intervals;
- the ratios in Table 3;
- the lag summary and the in-line drift figures (Sect. 5.1), and the surrogate statement (Sect. 5.5).

All of these reproduce. I also confirmed that the GP noise floor is computed from the calibration alternatives only, so the held-out truth does not leak into it. Where I disagree below, it is about what the numbers are taken to show, not about the numbers.

## 3. First-round major comments, point by point

### C1. The production floor as a production construct: **resolved** (minor points remain)

**Evidence.**

- The floor is positioned as a repeatability-type limit of batch centres under within-run conditions (p. 5, ll. 218–222; p. 6, ll. 271–274), with a reference protocol (p. 6, ll. 275–276).
- Table 3 gives F/σ_LT, σ_b/F and σ_w/F per geometry.
- Sect. 3.2 says that equal distances in floors do not mean equal nonconforming fractions (p. 7, ll. 281–284), and that the floor is a within-run lower bound of the variation of series production (ll. 289–290).
- The lag profile (p. 12, ll. 550–552) and the reproducibility of q95 (p. 13, ll. 574–577) are reported.
- A floor taken between series, and the unit of q95 reproducibility, are in Table A2 and p. 19, ll. 850–856; the rankings survive both.

This answers points (a)–(c) of my comment.

**What remains.**

- (i) Table 3's components cannot be combined with its own F/σ_LT column; see N4.
- (ii) The positioning is right in substance but imprecise in one respect.
  - A repeatability limit in ISO 5725-2 presupposes repeatability conditions over a short interval. The floor pools batch pairs up to 450 parts apart and, as Sect. 5.1 shows, is set by drift and grows with the lag. Formally it is closer to a time-different intermediate-precision limit (ISO 5725-3) of batch centres within a run.
  - In the terms of ISO 22514-2, the runs follow a time-dependent model with a varying location.
  - Two clauses (p. 5, l. 221; p. 6, l. 273) would make this exact.
  - Please also check the editions cited (ISO 5725-2:2025, ISO 22514-2:2026). The editions I know are ISO 5725-2:2019 and ISO 22514-2:2017.
- (iii) Assumption A2 ("the runs ... are like those of future production", p. 7, ll. 278–279) is still stated as an assumption, although ll. 289–290 and Sect. 6.6 concede that it does not hold for between-run variation. State what is actually assumed: that the within-run variation of these runs is like that of future runs.

### C2. Assumption A3 and the source of the drift: **resolved** (as far as the data allow)

**Evidence.**

- The paper states that the documentation gives neither the scanning order nor the dates (p. 11, ll. 477–479).
- It calls the unit a production-and-measurement floor (p. 7, ll. 287–289) and separates repeatability from stability (p. 13, ll. 567–569).
- It drops the punch-temperature claim and reports the in-line drift analysis (ll. 569–572).

I confirmed that `inline_drift.csv` has been regenerated with the current definitions (mid-side draw-in floor 0.051 mm) and matches the text (out-of-fold R² −0.23 to 0.20; floors change by −16 to +12 %).

**What remains (optional and cheap).**

- Ask the dataset's authors whether the parts were scanned in production order, and on which days.
  - If the parts were not scanned in production order, scanner drift could not appear as drift in production order, and the floor could be read as a production floor after all.
  - If they were, the present qualification stands.
- The abstract (p. 1, ll. 23–25) still defines the floor by the "drift and scatter" of production alone. Adding "of production and measurement" would carry the qualification to where most readers stop.

### C3. Decision situations and requirements compared with release decisions: **resolved** (subject to N2)

**Evidence.**

- The conformance level and its capability equivalent (Ppk ≈ 0.55) are stated in Sect. 3.1 (p. 6, ll. 255–260) and in the abstract.
- Sect. 5.8 places requirements at Ppk = 1.0–2.0, that is, 1.0, 1.7, 2.5 and 3.1 floors above q95 (I reproduced these).
- Sect. 6.2 draws the conclusion I had hoped for. Release-level requirements fall where only a near-replicate production record decides, "consistent with the practice of requiring a production trial run for a process change" (p. 20, ll. 913–916).
- The roles of the characteristics are labelled (p. 11, ll. 497–502), and two-sided tolerances are formulated (p. 6, ll. 239–242).
- The ISO 2768-1 scenario is no longer called realistic (p. 19, ll. 838–841).
- Trial costs are distinguished by relation (pp. 20–21, ll. 920–922), and the trial's own error is stated (p. 9, ll. 399–402).

**What remains.**

- The capability-anchored analysis is one-sided by construction, and two sentences around it overstate what it shows; see N2.
- The statement on the trial's error covers within-run reproducibility only. A trial is itself one run, so the between-run component (bounded at 1.2–9.8 floors, p. 13, ll. 572–574) applies to it as well. R4c asked for exactly this ("a separate run may differ by more"); one clause would do.

### C4. Confounds and structural features of the evidence relations: **partly resolved**

**Evidence.**

- The sibling relation is stratified by resolvability (p. 14, ll. 628–632).
- Extrapolation is split by force level, with the stroke-speed confound stated (ll. 632–636; Table 4; Sect. 6.6).
- Run metadata are reported (p. 11, ll. 474–479), and the k = 1 identity is explained (p. 17, ll. 762–765).
- A drawing-nominal baseline is added for a new family (p. 15, ll. 683–687).
- Table 5 gives the near-replicate figure and the split between interpolation and extrapolation.

All of these numbers reproduce.

**What remains: the headline.** R3b asked that the 3.4 floors be interpreted through the strata. R3c asked that interpolation and extrapolation be reported separately "wherever 8.5 floors is quoted".

The response to my minor comment 2 says that the split is reported "in the abstract-level statements (Sect. 5.3, Sect. 6.1, Table 5)". It is in Sect. 5.3 and Table 5. It is not in the abstract (p. 1, ll. 31–35), Sect. 5.4 (p. 15, ll. 671–673), Sect. 6.1 (ll. 872–874) or the Conclusions (p. 23, ll. 1032–1034), which still present the pooled 3.4 → 8.5 floors as the growth of the best distance with novelty.

The paper's own numbers show that within a family this gradient comes from the composition of the two relations, not from novelty:

| Case (nearest produced setting) | Cases | Decisive distance (floors) |
|---|---|---|
| sibling, neither sibling resolvable | 58 | 0.85 |
| sibling, one resolvable | 34 | 2.5 |
| sibling, both resolvable | 34 | 4.9 |
| new setting, interpolated (300 kN) | 42 | 4.7 |
| new setting, extrapolated to 500 kN (same stroke speed) | 42 | 4.9 |
| new setting, extrapolated to 100 kN (slower stroke) | 42 | 11 |

*Sources: Sect. 5.4 and Table 4; the 500 kN and 100 kN values are from `panel_force_levels.csv`.*

The table shows three things:

- Whenever the new design differs resolvably from the produced ones, and force and speed do not change together, the nearest produced setting decides at about 5 floors (about 0.25 mm of mid-side draw-in), in every relation within the family.
- Near-replicates are decided within a floor.
- Only the extrapolation in which the stroke speed also changed needs 11 floors.

For a process planner, that is a more accurate and more useful statement than "3.4 with a sibling, 8.5 for a new setting". It also qualifies the abstract's "requirements at a performance index of 1.33 lay inside every decisive distance" (ll. 35–36). A Ppk-1.33 limit (1.7 floors) lies outside the near-replicate distance, which is why the nearest setting correctly says "meets" in 91 % of such sibling cases (Sect. 5.8).

**What would resolve it.**

- Restate the within-family result in the stratified terms above in the abstract, Sect. 5.4, Sect. 6.1, the Conclusions and the Release-level row of Table 5. At a minimum:
  - give 4.7 and 9.5 floors, with the 100 kN caveat, wherever 8.5 appears;
  - give the near-replicate share wherever 3.4 appears.
- Keep the new-family step (two transfers) as the one real change of scale.
- In Sect. 6.6 (p. 23, ll. 1017–1019), "the extrapolation results describe a force and speed change together" should read "the extrapolation to 100 kN"; the extrapolation to 500 kN kept the speed.

**A smaller point.** The response says that no nominal-plus-offset baseline exists for the arm angles. It does exist. For characteristics whose nominal is the same in both families (the arm angle and the bottom dome, whose requirements are on absolute values about zero), "nominal plus the produced family's deviation" is identical to M1n, which fails at about 130 floors. That is the contrast the editor asked for, and it is already in Table 4. One sentence at p. 15, l. 687 would make it visible, and would explain why the drawing nominal helps only for the wall angle, whose design angle differs between the families.

### C5. How representative the simulation is, and the scope of RQ3: **resolved**

**Evidence.**

- The simulator's limitations are stated (p. 11, ll. 483–488).
- The cup-depth reference offset is separated: 108 → 65 floors (p. 13, ll. 589–593; reproduced from `panel_m0_split.csv`).
- RQ3 is conditioned on this simulator and this data regime (abstract; Sect. 6.3, ll. 935–938; Sect. 7).
- The headline distances are given in units (p. 14, ll. 623–624), and the guidance table no longer quotes 108 floors.
- The failure of friction calibration to repair the force trend is interpreted (p. 21, ll. 927–930), which is the right reading for a forming engineer.

**What remains (minor).**

- (a) The envelope's process window varies sheet thickness and friction only (p. 11, ll. 487–489). It does not vary material properties (coil-to-coil yield strength, hardening, r-value), which dominate springback scatter in series stamping. One clause where the envelope is introduced (p. 7, ll. 313–315) would explain why M0w, M2 and M5 do not represent production variation.
- (b) The force-effect ratio of 2.7–5.1 is computed for the two draw-ins only (`panel_force_effect.csv`). Sect. 5.2 says so (ll. 587–588); Sect. 6.3 (l. 927) does not.
- (c) "The simulation, as used, helped only across families" (abstract, ll. 36–38; similarly Sect. 7, ll. 1036–1038) contradicts M1s with a sibling, which decides 4.2 floors closer than M1n (p. 15, ll. 680–683). Write "as an offset", as Sect. 6.1 does (l. 904).

### C6. What a design or process-planning team would need: **partly resolved**

**Evidence.**

- The worked example (p. 18, ll. 817–827) takes one decision from the floor in millimetres to the verdict, the margin and what production showed. I reproduced its numbers from `dec_intervals.csv`.
- The procedure is placed in the development process (p. 21, ll. 922–924).
- A minimal evidence statement is given (p. 22, ll. 982–987).
- The lag profile shows how the floor scales with run length.

**What remains.**

- (a) **Short runs.** The central claim about evidence cost goes beyond what was tested: "the qualification needs short runs of several variants, and only the floor needs a run long enough to show the drift" (p. 17, ll. 777–779; repeated at p. 22, ll. 985–987). See N1.
- (b) **Placement at production part approval.** The paper says that "steps 1 to 5 fit the start of production or the production part approval of a family, when its series are measured anyway" (p. 21, ll. 922–924). This is optimistic.
  - At production part approval a company runs the released process setting and makes an initial process study on its special characteristics (under AIAG PPAP, typically at least 100 readings from at least 25 subgroups).
  - It does not run several blank-holder forces and lubrication patterns as long series with every part measured.
  - The produced variants that steps 1–5 need would come from process development and tryout (short runs; see N1), or from a product family's production history across part numbers.

  Please reword, and say which evidence relation each of these sources can support.
- (c) **Sampled measurement.** Series production measures subgroups, not every part. With the paper's own model (p. 6, ll. 272–273), the floor from subgroups of n parts is 1.96√2·√(σ_b² + σ_w²/n). From Table 3's components I obtain, for subgroups of five, roughly 1.1–2.1 times the reference floor (median 1.3), before the correction asked for in N4. One sentence would tell a team what sampled inspection does to the unit.

### C7. Transfer to the processes named in the call: **resolved** (suggestions only)

**Evidence.**

- Table 6 maps batch and run, dominant variation, relations and floor for injection moulding, machining, casting and additive manufacturing.
- Sect. 6.5 states the prerequisites, names attribute outcomes as outside the quantile requirement (ll. 988–990), and reports the PA12 attempt as a negative result with its remedy (ll. 1001–1005).
- "None is specific to forming" has been removed.

The editor did not require a second process, so this answers my comment.

**Suggestions (not conditions).**

- (a) **Injection moulding.** The cavities of a multi-cavity mould are stable, systematic offsets, which capability studies treat as separate streams. A floor "between cavities" would put them into the unit. Instead:
  - take the floor within a cavity;
  - treat cavity offsets as resolvable effects, as the geometry is treated here;
  - name set-up and material-lot changes as the excluded between-run component.
- (b) **Machining.** "Between offset intervals" reads as if the deliberate offset steps entered the floor; I assume batch centres within an offset interval are meant.
- (c) **Two further columns.** Two columns from my first-round request would show at a glance where the framework applies unchanged:
  - the predictor usually available (filling and warpage, solidification, CAM and deflection, or thermal-distortion simulation);
  - the form of the requirement (a dimensional quantile or an attribute rate).

### C8. Contribution to design research and to AI in DFM: **resolved**

**Evidence.**

- The evaluation protocol is presented as the contribution to the collection (p. 21, ll. 938–942).
- Sect. 6.4 is rewritten as an argument.
- The pooled scopes are reported and discussed (Table 4; p. 14, ll. 636–640).
- The machine-learning findings are framed as small-data findings.

**One suggestion.** The results support a sharper practical statement than the paper makes:

- The rules decide reliably in the relations where a physical trial is cheapest. A new force on an existing die is a short press run (p. 21, ll. 920–922).
- No rule is reliable near release-level limits in the relation where a trial is dearest: a new family, which may need a new tool.

Saying this in Sect. 6.2 or 6.4 would turn the operating characteristics into an argument about when design-stage prediction is worth having.

## 4. New issues arising from the revision

**Major: none.** The issues below are minor in effort, but N1–N3 change statements that a practitioner would act on.

**N1. The short-series analysis truncated only the calibration side** (Sect. 5.6, ll. 775–779; Sect. 6.5, ll. 985–987; Table A2).

- *What was done.* In the variant "Calibration series of n", only the calibration alternatives' q95 came from their first n parts. The held-out truths and the floors stayed those of the 500-part series (`robustness.py`, item 16, says so; the note to Table A2 does not).
- *Why it matters.* In step 5 every produced alternative is also a held-out truth. A team that has only short runs therefore qualifies its rules against truths that reproduce only to about one floor for 100 parts (p. 13, ll. 575–577), and worse for 50. The variant shows that rules can be *calibrated* on short runs; whether they can be *qualified* on them is untested.
- *Fix.* Either repeat the variant with truths from the same short series (the noise of the truth will matter most for the near-replicate stratum and the guard bands), or narrow the two sentences and the note to Table A2 accordingly. "Calibration runs of about 50 parts per variant qualified the rules" (l. 986) should then read "calibrated".

**N2. The capability-anchored test scores only one side** (Sect. 5.8, ll. 830–838; Sect. 3.1, ll. 258–260).

- *The problem.* Every alternative meets these limits by construction (`panel_capability.csv`: adequate in all cases). The shares therefore count only right verdicts, false rejects and trials, so a rule biased towards "meets" scores well. In the released file, M1s is right in 79 % of new-setting cases at Ppk 1.33, more than the nearest setting (65 %), although Table 4 shows M1s falsely accepting failing alternatives up to 164 floors from the limit.
- *Three corrections follow.*
  - (a) State the one-sidedness. Present the positions (1.0, 1.7, 2.5 and 3.1 floors) as the result, and the shares as false-reject and trial rates.
  - (b) "Release-level requirements are therefore decided at the design stage only within a family" (ll. 837–838) contradicts the 65 % for a new setting. The numbers show "only with a produced sibling", which is also what Sect. 6.2 says (ll. 914–915).
  - (c) "The framework reaches them through requirements anchored in capability" (p. 6, ll. 259–260) overstates. Section 5.8 still decides the 95th percentile and locates release-level limits relative to the distances; it does not decide whether Ppk ≥ 1.33.
- *If a two-sided capability decision is wanted,* the decided statistic could be the index itself or a parametric high quantile, with its own floor (its reproducibility between batches). The q95-reproducibility unit of Table A2 already does this for q95.

**N3. The new family is qualified in one floor and decided in another** (Sect. 3.2, ll. 290–292; Fig. 1, step 6; Table 4; Sect. 5.3, ll. 618–624; Sect. 5.9, ll. 856–857; abstract, ll. 33–35; Table 5).

- *The inconsistency.* Sect. 3.2 and step 6 use the produced family's floor. Table 4, Table 5 and the abstract report the new-family distances in the floor of the unproduced target family, and the note to Table 4 does not say so.
- *Why it matters.* The choice changes more than the numbers. In the produced family's floor (`panel_source_floor.csv`), M3 is the safest rule at 17 floors, and M2 is safe only at 26. Two statements therefore hold only in a unit that the team does not have:
  - "the envelope rule is the safest at 16 floors" (l. 621);
  - "the envelope rule [remains] the safest for a new family" (l. 857).
- *Fix.* Give the new-family columns of Table 4 and the corresponding row of Table 5 in the produced family's floor (or in both floors), and name the unit in the abstract.

**N4. Table 3 combines different summaries** (p. 13, Table 3; Sect. 3.2, ll. 284–287).

- *The problem.* σ_LT is the median of the per-alternative standard deviations, whereas σ_w and σ_b are pooled (root mean square) over alternatives (`panel.py`, `floor_protocol`).
  - As a result, σ_w exceeds σ_LT in 10 of the 14 cells. For the concave cup depth, for example, σ_w = 0.65 F and σ_LT = F/2.2, so σ_w ≈ 1.4 σ_LT, which cannot hold for the same parts.
  - For every alternative I recomputed, σ_w is below σ_LT.
  - The pooled σ_w is dominated by the 100 kN concave series, whose cup-depth scatter is two to four times that at 500 kN.
- *Why it matters.* Sect. 3.2 invites readers to recompute F for their own protocol from these components.
- *Fix.* Use one summary for all three quantities, and say whether the statistics are classical or trimmed (the floor uses 10 % trimmed means). Consider also noting that the part scatter differs by force level.

**N5. Numbers that are no longer tabulated have no reference a reader can follow** (Appendix A, ll. 1049–1052; Code availability, p. 25, ll. 1132–1135).

- *The problem.* With the supplement removed, many quoted numbers rest on the released files: the sibling strata, force levels, guard bands, capability shares, in-line drift analysis, lag profile, surrogate, cost map and paired differences. The manuscript names none of these files; the LaTeX source contains no file name. It refers only to results "archived with" the code, whose DOI is still "[DOI pending]".
- *Why it matters.* The editor required the DOI at resubmission.
- *Fix.* Supply the DOI, and add the response's table of numbers, scripts and result files (Part 5 of the response) as a short appendix table.

**N6. The guard bands, the procedure's main output, exist only in one sentence** (Sect. 5.7, ll. 802–816; Fig. 4).

- *What is missing.* "None for the interval rules within the family" refers to the sibling relation only; the guard bands of the interval rules for a new setting are not given. In `panel_step6.csv`, for an extrapolated setting:
  - M2 and M5 reach 95 % correct decided verdicts at no guard band up to 20 floors;
  - M5n, M3n and the nearest setting reach it at 6.5–7.0 floors.

  In other words, step 5 would not qualify the simulation-based interval rules for extrapolation. That is a practically important result which the reader cannot see.
- *Fix.* A small table (relation × core rule: g; decisive and safe distance with g; trial share at 10 floors) would replace much of the paragraph.
- *The prior.* "For a new family ... every design goes to trial" (ll. 812–813) follows from the requirement prior, which stops at ±20 floors (Sect. 3.6, l. 451). M2 alone is right in at least 95 % of verdicts beyond 51 floors (Table 4), so a wider prior would give it a finite guard band for gross margins. Sending every new-family design to trial agrees with forming practice, where a new die always goes through tryout. The paper should still say that this outcome is conditional on the prior.

**N7. The relation-specific cost comparison rests on the gross-failure scenario** (Sect. 5.8, ll. 838–845).

- *The problem.* The cheapest rule by trial cost is computed on the ISO 2768-1 scenario, which the paper itself describes as mostly testing gross failures: only 32 of its 108 decisions lie within 5 floors of the limit, and six of those concern failing alternatives. With a sibling, every decision is right and the cost is zero for M1s and the nearest setting alike. `scen_cost_map.csv` lists them as tied; the text names only the nearest setting.
- *Fix.* Either repeat the comparison on the requirement grid or on the capability-anchored requirements, or add a sentence that the cost ranking by relation inherits the scenario's coarseness.

**N8. The result file cited for distances in physical units is quantised** (`panel_physical_units.csv`; cited in the response to A9e, C5 and C-m23).

- *The problem.* The distances are evaluated on the 0.05-step grid of `decisions.FINE` with the floor set to 1, that is, in steps of 0.05 mm or 0.05°. That step is about 18 floors of flange waviness, 6–15 floors of bottom dome and 4–6 floors of cup depth. For the waviness, the nearest setting with a sibling is listed at 0.05 mm, about 20 times its value from the floor distances (0.85 floors, about 0.0025 mm).
- *Fix.* The paper itself quotes units only for the draw-in and the wall angle, and those values are correct. The file should be recomputed (for example by converting the per-characteristic floor distances) before anyone relies on it.

## 5. Remaining minor and editorial points

1. **"Within a family" has two meanings.**
   - In the decomposition it covers the sibling and new-setting relations together (p. 14, l. 644; p. 20, ll. 899–900).
   - At p. 15, l. 680; p. 18, l. 807; p. 19, l. 837; and p. 20, l. 905 it means the sibling relation alone.

   Use "with a produced sibling" for the latter.
2. **Note to Table A2, "Floor between series".** Say that this floor contains the lubrication effect, as `robustness.py` notes. For the sibling relation it is also computed from the very series that the nearest setting averages, so its 0.75 floors (p. 19, l. 853) are close to circular. For "Calibration series of n", see N1.
3. **Sect. 5.1, ll. 550–552.** The lag ranges of 0.51–0.80 and 1.1–1.5 floors are averages over the two geometries; per geometry they are 0.41–0.86 and 1.06–1.66 (`panel_variogram.csv`). Say so.
4. **Sect. 3.4, l. 361.** "The distances are exact": they are exact up to the 0.05-floor evaluation grid.
5. **"Capability" for the 95th percentile** (p. 20, ll. 910–914; Table 5, "expected margin to the capability"). In SPC usage, capability means the process spread or its index. Write "the predicted 95th percentile" to avoid a misreading by practitioners.
6. **"Resolution"** is still used in the gauge sense (p. 7, ll. 279–280; p. 13, ll. 566–567), next to "the resolution of production" (title) and "resolvable". Use "measurement resolution" for the gauge sense and add it to Table A1.
7. **Worked example (p. 18, ll. 817–827).**
   - Say how typical the case is, for example the share of the 42 interpolated cases in which step 6 with g = 2.0 gives the right verdict at a comparable requirement distance.
   - Say why the mid-side draw-in was chosen, since it is the one characteristic whose measurement resolution is coarse (0.38 floors).
8. **Response accuracy, `alt_mrc.csv`.** The response (C-m12) says that minimum resolvable changes beyond the 200 kN interval are now reported as ">200, beyond the interval". The file still gives numbers (for example 5,613 kN for the wall angle), and no script writes such a label. The paper's wording (p. 13, ll. 584–586) is correct and agrees with `rob_bhf_pairs.csv`. Please correct the file or the response.
9. **M6.** The notes to Tables 2 and 4 say that M6 "appears only in the robustness analysis", but it has a row in Table 4.
10. **Sect. 5.3, l. 612.** "The interval rules decide only at 13–31 floors" covers M2, M5, M5n, M3, M3n and M2n, but not M6 (56 floors). Name the set.
11. **Two-sided requirements** are formulated (Sect. 3.1, ll. 239–242) but not used in any result. One line of results for the wall angle, as an absolute deviation about its design angle, would show that the distances carry over (optional).
12. **Abstract and Table 5, release-level requirements.** "Inside every decisive distance" should become "inside every decisive distance except that of a near-replicate sibling" (see C4).

## 6. Recommendation

**Minor revision.**

The revision addresses my first-round concerns with the existing data, and does so honestly. The floor is positioned and bounded, the release-level consequence is stated in capability terms, the confounds are reported, the procedure is specified and worked through, and the paper is shorter. Everything I re-derived reproduces.

What remains needs no new data, and no new analysis apart from one optional rerun (N1):

- state the within-family result in the abstract, Sect. 5.4, Sect. 6.1 and the Conclusions in the stratified terms that the paper itself reports (C4);
- give the new-family figures in the unit used for deciding (N3);
- summarise the short-series and capability-anchored analyses within what they test (N1, N2);
- use consistent summaries in Table 3 (N4);
- supply the DOI and a table linking numbers to result files, to replace the removed supplement (N5).

I do not need to see the manuscript again if the editor can confirm these changes.

## 7. Confidential comments to the editor

The revision is a serious and largely successful response. I re-derived the main new numbers from the released files and found no computational errors. The new GP noise floor, which could have leaked the held-out truth, uses only calibration alternatives. My remaining concern is about framing. The abstract and conclusions still present the pooled 3.4 → 8.5-floor gradient, although R3b and R3c asked for it to be interpreted through the strata and the force split; the response suggests that this was done. The paper's own numbers show that, once near-replicates and the 100 kN speed change are separated, the nearest produced setting decides at about 5 floors in every relation within a family. Fixing this means rewriting a few sentences, not new work, but it is the statement readers will quote. The archive DOI required at resubmission is still pending. I see no need for another full round if you can check the headline rewrite, the new-family unit, the short-series claim and the DOI yourself.
