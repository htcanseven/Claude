# Response to the guest editor and the reviewers

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design, special collection "AI in Design for Manufacturing"
**Revision of:** the version reviewed on 5 October 2026 (frozen as `paper/review/cfp_panel/main_reviewed.tex`)

> **Note on this document.** The decision letter and the three reports it answers (`editor_decision.md`, `reviewer_A_design_theory.md`, `reviewer_B_ai_dfm.md`, `reviewer_C_manufacturing.md`) were written by AI agents acting as a simulated review panel. They do not come from the journal or its reviewers. The response is written as it would be to a real panel, so that it can serve as a template when real reports arrive.

Page and line numbers refer to the revised manuscript `paper/main.pdf`, which is compiled with line numbers. "ESM Table S*n*" refers to the Electronic Supplementary Material `paper/esm.pdf`. A marked-up version is `paper/review/cfp_panel/main_diff.pdf`. Every new number is produced by the released code; the last section lists the script and result file for each.

Dear Guest Editor, dear Reviewers,

Thank you for three careful reports and a decision letter that checked the reviewers' figures against the released files. The revision follows the letter wherever it qualifies a report. In summary:

- **Claims.** Every general claim is now quantified and conditioned on the evidence. The headline about the evidence relation is replaced by the best attainable distance per relation and a decomposition, and every RQ3 statement names the simulator and the data regime (R1).
- **Unit and distances.** The floor is positioned as a repeatability-type limit of batch centres (ISO 5725), with a reference protocol, variance components, a lag profile and its ratio to the part scatter. New-family results are given in the floor of the produced family, the weighting is stated exactly, and one-sided distances are in the main table (R2).
- **Fair and complete evaluation.** All scopes are reported, including the pooled ones and M6. The sibling relation is split by resolvability and extrapolation by force level. The Gaussian processes have a between-run noise floor, M3 and M3n a jackknife+ interval, and a scaled simulation rule M1s is added. For a new family there is a drawing-nominal baseline, and the refit bootstrap now preserves the evidence relation (R3).
- **The procedure.** Step 6 is specified as a guard band on the observable margin and evaluated for every relation, and one decision is worked through (R4).
- **Readability and length.** A design-theory positioning, a reuse section with a black-box formulation and a process mapping, a notation table and physical and capability anchors are added. Seven core rules carry the main text. The main text is shorter, from about 29 pages (abstract to conclusions) to 24, with five tables and four figures. The whole paper has 32 pages, against 38 before. Thirty tables and one figure move to the ESM (R5).

The reviewed version's conclusions survive the fairer specifications, with one exception: the simulation does add information within a family when it is rescaled (M1s) rather than added as an offset. The statement "within a family it adds nothing" now refers to the additive use only.

---

## Part 1. Map of the required revisions (R1–R5)

| Item | What was done | Where |
|---|---|---|
| **R1** Bring general claims into line with the evidence | Headline replaced by the best attainable distance per relation (3.4, 8.5 and no rule safe closer than 16 floors) and by a decomposition. The relation explains 69 % of the variation of the log decisive distance over all relations but 15 % within a family, where the rule explains 68 %. RQ3 is conditioned on this simulator (no lubrication or stroke-speed dependence; force effect 2.7–5.1 times too large; partly sign-inconsistent) and on six to nine produced settings per fit. Behaviour is explained by inductive biases. The new family is presented as two transfers. Scope, conformance level, physical anchor and capability anchor are in the abstract and introduction. Wording: "reliable", no "calibrated abstention". The validity claim is restricted to structural validity. Guidance table with its basis. Confirmatory and exploratory findings separated. | Abstract; p. 1, l. 30; p. 3, l. 98; Sect. 5.4 p. 16, l. 712; Sect. 5.5; Sect. 6.1 p. 20, l. 905; Sect. 6.3 p. 22, l. 988; Sect. 6.4 p. 23, l. 1018; Table 5; Sect. 7 |
| **R2a** Positioning of the floor | Repeatability limit of ISO 5725-2/-6 applied to batch centres under within-run conditions; relation to time-dependent process models (ISO 22514-2:2026). What is new is its use as a decision unit (Sect. 2.5). | p. 7, l. 301; p. 5, l. 221 |
| **R2b** Protocol and comparability | Reference protocol stated (B = 50, ten batches, all pairs, α = 0.95, per-geometry floors). σ_b, σ_w, model floor, F/σ_LT and F/σ_ST per characteristic and geometry (ESM Table S3), floor by lag (ESM Table S4), F/σ_LT in Table 3. RQ1 and Conclusions say "common production-referenced scale" and that equal distances do not mean equal nonconforming fractions. | Sect. 3.2 p. 7, l. 304; p. 7, l. 310; Table 3; ESM Tables S3, S4 |
| **R2c** Between-run variation and measurement | Floor labelled a within-run, production-and-measurement floor. A robustness variant uses a floor between series (an upper bound). The documentation does not state scan order or dates (said explicitly). The in-line drift analysis is regenerated and reported. Measurement resolution per characteristic is given (Table 3, ESM Table S9). | p. 7, l. 318; p. 14, l. 614; p. 12, l. 512; ESM Tables S9, S29, S30 |
| **R2d** The new family | Distances in the floor of the produced family (M5 35/31, M2 41/26 floors) and in physical units (ESM Tables S18, S19); new-family branch in Fig. 1 and step 6. | p. 15, l. 671; Fig. 1 |
| **R2e** Weighting and sides | Weighting described exactly; the failing side carries half the weight up to a few floors and a third at about 100 floors (ESM Table S11). FA-side distances are in Table 4 next to the pooled ones; all one-sided distances in ESM Table S14. | p. 10, l. 415; Table 4 |
| **R3a** Pooled scopes and M6 | Reported and discussed. Pooling makes most rules less decisive (M5 7.2 → 11, M2 23 → 53, M2n 19 → 325 floors) but raises M5's coverage from 86 to 90 % and makes its centre the most accurate point predictor (2.9 floors). M6 for all relations (ESM Table S12). The development record is corrected. | p. 15, l. 685; ESM Tables S12, S21 |
| **R3b** Sibling strata | Split by resolvability. Neither sibling resolvable (58 cases): NN 0.85 floors. Both resolvable (34 cases): NN 4.9 and M5 9.7 floors. | p. 15, l. 678; ESM Table S21 |
| **R3c** Force levels and stroke speed | Split by force level (NN 11 / 4.9 / 4.7 floors at 100 / 500 / 300 kN). The stroke-speed confound is stated wherever extrapolation is quoted. Interpolation and extrapolation are reported separately in Table 4, Sect. 5.3 and Table 5. | p. 15, l. 682; Table 4 |
| **R3d** Fair small-data baselines | GP noise bounded below by the variance between the series of one geometry and force; jackknife+ for M3/M3n; scaled simulation M1s (4.9 / 19 / 122 floors). The GP coverage within the family rises from 71–72 % to 85–86 %. | Sect. 3.3 p. 8, l. 348; p. 8, l. 342; Sect. 5.5 |
| **R3e** Production-informed new-family baseline | Drawing nominal plus the produced family's deviation for the wall angle: 2.0 floors against 7.3 for M5 (ESM Table S19). No such baseline exists for the arm angles. | p. 16, l. 733 |
| **R3f** Relation-preserving uncertainty | The refit bootstrap resamples whole lubrication patterns within a geometry (all forces kept; a target's copies never calibrate it), so every case keeps its relation. Paired refit intervals for NN–M5, NN–M5n, M5–M5n, M2–M2n, M1s–NN and M1–M1n (ESM Table S15). Differences of a few floors are not interpreted. | Sect. 4.4 p. 13, l. 568; Sect. 5.9; ESM Tables S15, S29 |
| **R4a** Specify and evaluate step 6 | Step 6 now compares the observable margin with a guard band g fixed in step 5 from the reliability-by-margin analysis. The requirement prior is stated (grid within ±20 floors). The operating characteristics and trial rates of the procedure's decision rule are reported for every relation (Fig. 4; ESM Table S24). For a new family no guard band up to 20 floors reaches 95 %, so the procedure sends every design to trial. | Sect. 3.6 p. 11, l. 483; Sect. 5.7 p. 19, l. 830; Fig. 4 |
| **R4b** Worked example | A tryout engineer releasing the concave cup at 300 kN, medium lubrication. It gives the floor in mm, the requirement, the relation and the guard, four rules' intervals and verdicts, the margin and guard band, the reliability at that margin and what production showed. | p. 19, l. 847 |
| **R4c** The trial's own error | A trial of 100 parts reproduces q95 to 0.92–1.49 floors, so no decision is reliable closer than the trial that would replace it; between-run variation is stated. | p. 10, l. 433; p. 14, l. 620 |
| **R5a** Design-theory positioning | New Sect. 2.2 (design types and product families, process-capability data, preliminary information, set-based design, prototyping, V&V domains and ASME V&V 40). Sect. 6.4 is rewritten as a strand-by-strand argument, distinguishing the predictive-uncertainty part of a margin from change absorption. | Sect. 2.2 p. 4, l. 140; Sect. 6.4 p. 22, l. 1000 |
| **R5b** Reuse for other AI-based DFM tools | New Sect. 6.5: prerequisites, a black-box formulation (classifier at its threshold, LLM check with the requirement in the prompt), continuous relations, a minimal reporting standard, the PA12 attempt as a negative result. Process mapping in Table A2; "machine learning" in the keywords; held-out-accuracy studies cited in Sect. 2.1. | Sect. 6.5 p. 23, l. 1025; Table A2 |
| **R5c** Density and length | Notation table (Table A1). Seven core rules in the main text. Thirty tables and one figure in the ESM. Tables carry the numbers and the text the interpretation. Main text 24 pages, against about 29. | Appendix A; ESM |

### Recommended revisions (Section 4 of the letter)

1. **Prerequisites.** Distances with the calibration alternatives truncated to their first 50, 100 and 250 parts (p. 18, l. 825; ESM Table S29). A minimal evidence protocol is stated in Sect. 6.5 (p. 23, l. 1025), and a between-build floor from replicated anchors is named as the remedy when no consecutive series exist.
2. **Capability-anchored operating characteristics.** Requirements at Ppk = 1.0, 1.33, 1.67 and 2.0 lie a median 1.0, 1.7, 2.5 and 3.1 floors above q95, inside every decisive distance. The shares of right and trial verdicts are reported (p. 19, l. 861; ESM Table S26), and Sect. 3.1 discusses high conformance levels early (p. 7, l. 285).
3. **The designer's view.** Fig. 4 shows the reliability by observed margin, with the prior stated. Sect. 6.3 discusses expert versus trial for an abstention (p. 22, l. 996) and Sect. 6.2 the transparency of NN against a GP interval (p. 21, l. 964). Hypotheses for a designer study are given (Sect. 6.3).
4. **Surrogate contrast.** `ds_surrogate.csv` is recomputed with the current definitions. The surrogate reproduces the simulation within 1.8 floors for 12 of 14 characteristic–geometry pairs, yet its decision fitness is that of the simulation (p. 16, l. 735; ESM Table S7).
5. **Borrowing strength across families.** We explain why a multi-task model cannot help a family with no produced alternative. The pooled GP with a geometry input is the form the data allow; it improves coverage but not decisiveness (p. 22, l. 984).
6. **Run and measurement metadata.** Start temperatures, warm-up, sheet thickness and stroke speed are reported for every series (ESM Table S10). The documentation states neither run order and dates nor the scanning order. The in-line drift analysis is regenerated and reported (ESM Table S30). A robustness variant drops the first 150 parts.
7. **Roles and requirement forms.** Roles are labelled (process indicator / drawing; ESM Table S1 and Sect. 4.3). Design angles are stated, and a two-sided tolerance is illustrated as a limit on the absolute deviation (p. 6, l. 268). The ISO 2768-1 scenario is no longer described as "realistic margins"; it "mostly tests whether a rule recognises gross failures".
8. **Per-characteristic distances and costs.** Per-characteristic distances in floors and in units (ESM Tables S17, S18). Trial costs differ by relation (Sect. 6.2). A cost sensitivity map is given over c_FR/c_FA and c_T/c_FA (ESM Table S28).
9. **Definitional offsets.** M0 is kept raw. Removing the cup-depth reference offset alone brings its decisive distance from 108 to 65 floors (p. 14, l. 639), and the guidance table no longer quotes "reliable beyond about 108 floors".
10. **Calibration design and guard.** "Calibration design" is removed; the construct is the calibration budget by relation. The applicability guard is shortened and related to valid input domains (Malak and Paredis 2010).

### Optional extensions (Section 5 of the letter)

- **A second process:** not attempted. As the letter allows, the PA12 attempt is reported as a negative result with its remedy, and the prerequisites are stated (Sect. 6.5).
- **Forward evaluation:** not done. Instead, step 6 is evaluated (R4a) and the selection optimism is stated in Sects. 4.5, 5.7 and 6.6.
- **Value of simulation fidelity; full Kennedy–O'Hagan; pressure-dependent friction:** not done. M1s is the linear multi-fidelity correction (Kennedy and O'Hagan 2000).
- **Error-rate methods:** conformal risk control and covariate-shift conformal prediction are positioned in Sect. 2.3. The 1/(n+1) bound on certifiable miss rates is stated with its consequence for the calibration budget (p. 8, l. 364).
- **Renaming the floor:** kept, but defined prominently as "a floor in the sense of a noise floor rather than of the shop floor" (p. 2, l. 80).
- **References:** NeurIPS entries completed (volume, pages, publisher) and the AIAG place of publication added.

### Editor's minor and editorial points (Section 7 of the letter)

- "every calibrated rule improves by an order of magnitude" → "every calibrated rule improves on the nominal simulation" (p. 15, l. 651).
- "exactly the n/(n+1) = 8/9" → the guarantee of at least (n−1)/(n+1) = 7/9 under exchangeability, which these cases lack (p. 17, l. 776). The rules table no longer says "at most".
- Section 4.5 corrected: "every variant tried is reported in the paper or the ESM", and the pooled scopes are now reported.
- "at 95 % confidence" → "in 95 % of batch pairs" (p. 13, l. 589).
- Liu et al. (2026) removed. In the Whitney sentence, the link to production variation is ours, supported by Thornton et al. (2000) (p. 2, l. 62).
- Rule names M3/M3n; the nominal simulation and the envelope do not depend on lubrication (p. 8, l. 355).
- Minimum resolvable changes beyond the interval are reported as ">200" with the note "beyond the interval" (ESM Table S5).
- Bootstrap intervals for the headline rules in Table 4.
- Fig. 2 (formerly Fig. 3): palette checked for colour-vision deficiency with a palette validator; δ_d (solid) and δ_s (dashed) on each panel.
- Sect. 6.3 states the question directly.
- References completed (see above).

---

## Part 2. Reviewer A (design theory and methodology)

### Major comments

**A1. Broad applicability is claimed but not yet shown.**
*Changed.* (a) A second application was not possible (see the letter, Section 6). The PA12 attempt is reported as a negative result with its remedy (p. 23, l. 1040). (b) Claims are narrowed throughout. The evidence-relation findings are labelled "observations on this dataset and hypotheses for confirmation" (p. 20, l. 911), and "None is specific to forming" is removed. (c) The prerequisites are stated in Sect. 6.5 and Table A2. The distances with calibration series of 50, 100 and 250 parts are reported (p. 18, l. 825). A between-build floor from replicated anchors replaces the floor when no consecutive series exist. (d) The abstract and introduction state that two of the three relations concern process settings on one tool (p. 1, l. 30; p. 3, l. 96).

**A2. The production floor: positioning, protocol dependence and the new-family case.**
*Changed.* The floor is positioned as the repeatability limit of ISO 5725-2/-6 applied to batch centres under within-run conditions (p. 7, l. 301). A reference protocol is fixed, and σ_b, σ_w and the floor at every lag are reported (ESM Tables S3, S4). For a new family the distances are given in the source family's floor and in units (p. 15, l. 671; ESM Tables S18, S19), and Fig. 1 has the new-family branch. RQ1 and the Conclusions now say "common production-referenced scale". The between-run component is discussed in Sects. 3.2, 5.1 and 6.6, with a robustness variant whose floor is taken between series.

**A3. The population behind the distances changes with the distance.**
*Changed.* The weighting is described exactly (p. 10, l. 415). The number of feasible failing-side requirements at each reported distance is in ESM Table S11 (124, 98, 84 and 63 of 126 at 3.4, 16, 35 and 108 floors). The FA-side distances are in Table 4 next to the pooled ones, and all one-sided distances are in ESM Table S14. Per-characteristic distances are in ESM Tables S17 and S18. How a team would obtain per-characteristic distances is discussed in Sect. 6.5 (the minimal report and data requirements). Restricting to the always-feasible range would discard the large distances that matter for a new family, so we report the weights instead.

**A4. The sibling relation mixes replicates with variants; pooled scopes not reported.**
*Changed.* The new-variant cases are split by the effect-to-scatter ratio of the siblings. Neither sibling resolvable (58 cases): NN 0.85 floors; one resolvable (34): 2.5; both resolvable (34): NN 4.9 and M5 9.7 (p. 15, l. 678; ESM Table S21). The pooled scopes are reported and discussed (p. 15, l. 685; ESM Tables S12, S16, S21). For continuous design spaces the relation becomes a distance in descriptor space or the position relative to the hull of produced designs, or is graded by the predicted ESR to the nearest produced alternative (p. 10, l. 444; p. 23, l. 1034).

**A5. The headline claim that the relation "governed decision fitness more than the model did".**
*Changed.* The decomposition is reported. The relation explains 69 % and the rule 6 % of the variation of the log decisive distance over all three relations; within a family the rule explains 68 % and the relation 15 % (p. 16, l. 713). The headline now reads: the best attainable distance grows with the novelty of the design, and within a family the choice of rule matters at least as much. The new family is presented as two transfers with one simulation. A production-informed transfer rule (drawing nominal plus offset) is added for the wall angle (p. 16, l. 733).

**A6. What simulation and learning contribute concern this simulation and design.**
*Changed.* Sect. 3.3 states that the nominal simulation and the envelope do not depend on lubrication, so in the sibling relation they cannot distinguish the new design (p. 8, l. 355). RQ3 is conditioned throughout (abstract; Sects. 5.5, 6.1, 6.3, 7). The scaled rule M1s shows that the simulation does carry information within a family when rescaled (p. 16, l. 728). The surrogate contrast is recomputed and reported (p. 16, l. 735). A controlled fidelity analysis was not done (optional in the letter).

**A7. The procedure and the guidance are not evaluated as such.**
*Changed.* (a) Step 6 now compares the observable margin with a guard band derived from the reliability-by-margin analysis; its operating characteristics and trial rates are reported for every relation (p. 19, l. 835; Fig. 4; ESM Table S24). (b) A nested evaluation was not done (encouraged, not required); the selection optimism is stated in Sects. 4.5, 5.7 and 6.6. Current-practice baselines are included in the cost analysis: M0, the process-window worst case M0w, and a new baseline, a trial for every design. For a new family the latter is the cheapest while a trial costs at most a tenth of a false accept (p. 20, l. 893; ESM Table S28). (c) Table 5 separates guidance from the definitions and observations on this dataset, each with its basis. The dataset-specific row on the new family is moved to the observed block. (d) Sect. 6.4 now claims structural validity in the sense of the validation square and a support evaluation in the terms of the design research methodology, not performance validity (p. 23, l. 1018). (e) The trial's own error is stated (p. 10, l. 433).

**A8. Positioning in the design literature.**
*Changed.* New Sect. 2.2 covers design types and product families (Pahl et al. 2007; Simpson et al. 2006; Jiao et al. 2007) and process-capability data (Tata and Thornton 1999; Thornton 2004; Thornton 1999; Chase and Parkinson 1991). It also covers preliminary information (Krishnan et al. 1997; Terwiesch et al. 2002), set-based concurrent engineering (Sobek et al. 1999), prototyping (Camburn et al. 2017), V&V domains and ASME V&V 40, and margins (Eckert and Isaksson 2017). Sect. 6.4 is an argument strand by strand (p. 22, l. 1000).

**A9. Readability, density and length.**
*Changed.* (a) Worked example (p. 19, l. 847). (b) Notation table (Table A1). (c) Seven core rules in the main text; six further rules in the ESM. (d) The tables named and much of Sects. 4.3, 5.1 and 5.3 moved to the ESM. (e) Physical units: 16 floors are about 0.8 mm of draw-in or 1.3° of wall angle (p. 15, l. 672); per-characteristic distances in units in ESM Table S18. (f) The text interprets and the tables carry the numbers. (g) The abstract is rewritten around the design question with a physical anchor.

### Minor comments

1. *Changed.* "increasingly rest" kept. The last sentence of the abstract now states what the framework gives evaluations of AI-based support.
2. *Changed.* "Calibrated abstention" removed. The coverage of each interval rule is named (p. 17, l. 775).
3. *Changed.* The Whitney sentence is rephrased; the link to production variation is ours (p. 2, l. 62).
4. *Changed.* "In 95 % of batch pairs".
5. *Changed.* Sect. 3.1 discusses the conformance level early (p. 7, l. 285); capability-anchored requirements are in Sect. 5.8.
6. *Changed.* Actor, milestone and evidence are given in Sect. 3.1 (p. 7, l. 283), Sect. 6.2 (p. 22, l. 970) and the worked example.
7. *Changed.* Step 3 in Fig. 1 now reads "below F: not confirmable in production", consistent with the caveat on tails.
8. *Changed.* M3/M3n, with the note that M3n is M4 in the code; the lubrication independence is stated in Sect. 3.3.
9. *Changed.* Points on operating characteristics, Bechhofer's indifference zone and the AQL/RQL analogy (p. 10, l. 426).
10. *Changed.* The interval level is described as a decision variable (Chow 1970), with 0.8 and 0.95 in the robustness analysis (p. 8, l. 368).
11. *Changed.* "Calibration design" is removed; only the calibration budget by relation remains.
12. *Changed.* The guard is shortened and related to valid input domains (Malak and Paredis 2010) (p. 19, l. 843).
13. *Changed.* "Design–process alternatives" is used for the alternatives.
14. *Changed.* Sect. 6.1 separates the two findings that follow from the definitions from the three that are observations and hypotheses.
15. *Changed* (see the editor's points).
16. *Changed.* The k = 1 coincidence of M1, M2 and NN is presented as an identity (p. 18, l. 816).
17. *Changed.* Design angles are stated (Sect. 4.3; ESM Table S1). The structure of the scenario is described (32 of 108 decisions within 5 floors). The cost ratio is varied in a sensitivity map (ESM Table S28).
18. *Changed.* Rankings within a few floors are treated as point estimates, with paired refit intervals and the share of resamples in which one rule is the more decisive ((location not found); ESM Table S15).
19. *Changed.* The third to fifth findings are labelled as observations on this dataset and hypotheses.
20. *Changed.* The PA12 attempt is reported briefly as a negative result with its remedy; "None is specific to forming" is removed.
21. *Changed.* Sect. 2.1 cites learned manufacturability models that were evaluated by held-out accuracy only (p. 3, l. 129).
22. *Changed.* Table 1 now reads "coverage; per decision possible" (conformal prediction) and "can require tests" (V&V).
23. *Changed.* Table 4 gives bootstrap intervals for M1s, M5, M5n and NN; all rules in ESM Table S13.
24. *Changed.* Fig. 1 has the new-family branch and the guard band; Fig. 2 marks δ_d and δ_s.
25. *Changed.* The extensions now include a confirmatory evaluation of the frozen procedure on another dataset or process (p. 24, l. 1087).

---

## Part 3. Reviewer B (AI in design for manufacturing)

### Major comments

**B1. The conclusions about learning depend on a small factorial data regime.**
*Changed.* (a) The data regime is stated in the abstract ("six to nine produced settings per fit") and next to each RQ3 statement (p. 22, l. 990). (b) Following the letter, the new-variant relation is stratified rather than relabelled: near-replicate siblings give NN 0.85 floors, the reproducibility of q95 (p. 15, l. 680). (c) The headline is replaced by the best distance per relation and the decomposition. (d) Behaviour is explained by inductive biases: trees do not extrapolate, two force levels identify at most a linear trend, and the GP force length scale sits at its lower bound (p. 17, l. 779). The interval centres decide at 3.3 (M5), 3.1 (M5n) and 3.7 floors (M3n), as close as NN.

**B2. One low-fidelity simulator used only additively; two transfers.**
*Changed.* The scaled rule M1s (q95 = a + b·s0) is added (p. 8, l. 342). It decides at 4.9 floors within the family, at 19 for a new setting (falsely accepting up to 164 floors from the limit) and at 122 for a new family. "Within a family it adds nothing" now refers to the additive use (p. 16, l. 724). The simulator's limitations are stated: no lubrication or stroke-speed dependence; force effect 2.7–5.1 times too large (recomputed with the current definitions in `panel_force_effect.csv`); wrong arm sign. They appear in Sects. 4.2, 5.2 and 6.3 and in the Conclusions (p. 24, l. 1082). The new family is two illustrative transfers. That any surrogate inherits the simulator's distance is stated (p. 22, l. 990). The full Kennedy–O'Hagan formulation was not implemented (recommended, not required).

**B3. The learned models lack a fair small-data specification.**
*Changed.* (a) The GP noise variance is bounded below by the pooled variance between the series of one geometry and force, the quasi-replicate lubrication series (p. 8, l. 348). Coverage within the family rises to 85–86 %; the sampling-only bound is kept as a robustness variant. (b) Jackknife+ for M3 and M3n; coverage of M3 96 % within the family. (c) A multi-task model cannot be estimated for a family with no produced alternative; the pooled GP is the borrowing the data allow (p. 22, l. 984). (d) Conformal risk control and weighted conformal prediction are positioned in Sect. 2.3. The 1/(n+1) bound and its consequence for the calibration budget (19 alternatives for a 5 % miss rate, nine for 10 %) are stated in Sect. 3.3 (p. 8, l. 364).

**B4. Unreported results; confirmatory versus exploratory.**
*Changed.* Pooled scopes reported and discussed (p. 15, l. 685; ESM Tables S12, S16, S21); M6 for all relations (ESM Table S12). Sect. 6.1 separates findings from the definitions from observations; Sect. 4.5 says which elements were added after first results. A confirmation on held-back data was not possible: the analysis has used all 18 alternatives and all seven characteristics since the first round.

**B5. Precision overstated; the refit bootstrap mixes relations.**
*Changed.* The refit bootstrap resamples whole lubrication patterns within each geometry, with all forces kept and a target's copies never calibrating it, so every case keeps its relation (p. 13, l. 568). Paired refit intervals and the share of resamples in which one rule is the more decisive are reported ((location not found); ESM Table S15). Rankings within a few floors are not interpreted.

**B6. Trust treated only statistically.**
*Changed.* (a) Fig. 4 shows the share of correct verdicts by observed margin, for each relation and rule, with the requirement prior stated in the caption and Sect. 5.7. (b) The worked example shows what the designer receives (p. 19, l. 847). (c) Sects. 6.2 and 6.3 discuss the transparency of NN against a GP interval, expert versus trial, and appropriate reliance (Lee and See 2004; Madras et al. 2018; Zhang et al. 2021). (d) "Reliable" replaces "trusted". Concrete hypotheses for a designer study are given (p. 22, l. 995).

**B7. How developers of AI-based DFM tools could use the framework.**
*Changed.* New Sect. 6.5 with a black-box formulation (classifiers at their threshold, LLM checks with the requirement in the prompt), relations for continuous novelty, a minimal reporting standard and data requirements (p. 23, l. 1031). The protocol dependence is handled by a reference protocol and reported variance components (R2b). Positioning adds Regenwetter et al. (2022) and learned-manufacturability studies; the keywords include machine learning.

### Minor comments

1. *Partly changed.* The term is kept but defined prominently as "a floor in the sense of a noise floor rather than of the shop floor". "At 95 % confidence" is replaced.
2. *Changed.* Physical size (0.05 mm), data structure and conformance level are in the abstract. "Calibrated abstention" removed; "thirteen rules" includes M1s, and M6 appears in the robustness analysis.
3. *Changed.* "Machine learning" is a keyword.
4. *Changed.* Liu et al. (2026) removed.
5. *Changed.* The introduction states that early product design is covered only by the new-family relation (p. 2, l. 88).
6. *Changed.* σ_b, σ_w, the lag profile and the reference protocol are reported (R2b).
7. *Changed.* "At least" with the one-line argument (p. 8, l. 361).
8. *Not changed.* The oil amounts of the three patterns overlap between series (Sect. 4.1), so a continuous descriptor would order the series rather than the patterns. The rank (the order of the oil amount) is kept, and a one-hot coding is reported as a robustness variant (ESM Table S29).
9. *Partly changed.* The relation to selective classification and risk–coverage curves is stated in Sect. 2.4. Fig. 2 shows the verdict shares, which contain the risk–coverage information at each requirement distance. Coverage, half-width and centre accuracy of the interval rules are in ESM Table S16. Separate risk–coverage curves are not added for space.
10. *Not changed.* Following the letter, the guard is shortened rather than extended. A multivariate applicability measure is named as the natural extension in Sect. 6.5 (distance in descriptor space or hull).
11. *Changed.* The resolution of each characteristic relative to its floor is reported: the mid-side draw-in step is 0.38 floors; the others are effectively continuous (Table 3; ESM Table S9). The GP noise bound no longer depends on the zero standard errors, because it is set by the between-run variance. Per-characteristic distances allow a reading without the mid-side draw-in (ESM Table S17).
12. *Changed.* Source-family floor (R2d).
13. *Changed* (see the editor's points).
14. *Not changed.* Table 4 with intervals is kept; Fig. 2 and Fig. 3 show the distances graphically for the core rules.
15. *Changed.* CVD-checked palette (blue, grey, orange, violet). The number of feasible verdicts per distance is in ESM Table S11.
16. *Changed.* The M5 fits from k = 2 are kept and flagged in the note to ESM Table S20. The odd–even pattern of M1 is explained ((location not found)).
17. *Changed.* Nominal angles stated (20°, 10° and 0° for the arms), and the scenario's structure described. Linear general tolerances on depth and flange width were not added: the depth is referred to the cup bottom, and the flange is cut away.
18. *Changed.* The question is stated directly. The GP centres are described as at least as accurate as NN.
19. *Changed.* Table 5 asks for decisive and safe distance jointly or the expected cost.
20. *Changed.* Minimum data requirements in Sect. 6.5 and Table A2.
21. *Pending, the author's action.* A versioned archive with a DOI will be deposited on Zenodo at resubmission and cited in the availability statements (the placeholder is marked in the manuscript).
22. *Changed.* NeurIPS and AIAG entries completed. Kennedy and O'Hagan (2000), Angelopoulos et al. (2024), Lee and See (2004), Madras et al. (2018), Zhang et al. (2021) and Regenwetter et al. (2022) added. Mozannar and Sontag (2020) was dropped for length; Madras et al. (2018) covers learning to defer.

---

## Part 4. Reviewer C (manufacturing)

### Major comments

**C1. The floor as a production construct.**
*Changed.* (a) The floor is positioned against ISO 5725 and ISO 22514-2 (p. 7, l. 301; Sect. 2.5). F/σ_LT is in Table 3 and F/σ_ST in ESM Table S3. Equal distances in floors do not mean equal nonconforming fractions (p. 7, l. 311). (b) A reference protocol is fixed (R2b). (c) The floor is labelled within-run, a lower bound of series variation. A robustness variant takes the floor between series ((location not found)). The reproducibility of the decided quantile is reported beside the floor (0.92–1.49 floors for 100-part batches). Centre resolution is kept as the unit because it is what production resolves between alternatives; the q95-based normalisation is reported as a robustness variant.

**C2. Assumption A3 and the source of the drift.**
*Changed.* The documentation states neither the scanning order nor its timing; we say so (p. 12, l. 512). The in-line drift analysis is regenerated with the current definitions and reported (p. 14, l. 614; ESM Table S30). Process signals predict the batch drift with an out-of-fold R² of −0.23 to 0.20, and removing it changes the floors by −16 to +12 %. Evidence on scanner stability (master part, rescans) is not in the dataset, so the unit is called a production-and-measurement floor and its consequences are stated in Sects. 3.2 and 6.6. "Which a repeatable measurement cannot create" is removed.

**C3. Decision situations and requirements versus release decisions.**
*Changed.* (a) Capability-anchored requirements (recommended item 2): release-level requirements lie inside every decisive distance, and only the production record decides them within a family (p. 19, l. 868). (b) Roles are labelled. Two-sided limits are illustrated as limits on the absolute deviation. Draw-in and waviness are kept as tryout quantities, as the letter decides. Splits, wrinkles and thinning are outside the framework's continuous dimensional characteristics, as Sect. 6.5 notes for attribute outcomes. (c) The ISO 2768-1 scenario is described as a test of gross failures. (d) Trial costs differ by relation (Sect. 6.2); a cost sensitivity map is given (ESM Table S28); the trial's error is stated (Sect. 3.4). The abstract and Sect. 3.1 give the conformance level.

**C4. Confounds and structural features of the relations.**
*Changed.* (a) Sibling strata (R3b), and the k = 1 identity (Sect. 5.6). (b) Split by force level, with the stroke-speed confound stated (p. 15, l. 682; Sect. 6.6). (c) Run metadata are reported (ESM Table S10). The documentation gives no run order or dates. As the letter notes, start temperature rises in the order coarse, medium, fine strictly in only two of the six cells, so run order is not an established confound. (d) The drawing-nominal baseline is added for the wall angle (R3e).

**C5. How representative the simulation is.**
*Changed.* RQ3 is limited to this simulation and data regime. The cup-depth reference offset is separated (65 against 108 floors). The headline distances are given in units (p. 15, l. 672). The guidance table no longer quotes "reliable beyond about 108 floors". A pressure-dependent friction law was not implemented (optional).

**C6. Applicability and cost in production evidence.**
*Changed.* The worked example shows step 6 for one decision (p. 19, l. 847). A minimal evidence protocol is derived from the distances with short calibration series and the budget (p. 18, l. 825; p. 23, l. 1025). The procedure is placed at start of production or PPAP for later decisions (p. 22, l. 970). Cheaper evidence: the in-line signals do not explain the drift (C2). Where no consecutive series exist, a floor from replicated specimens or between offsets takes its place (Table A2).

**C7. Transfer to the processes named in the call.**
*Changed.* Mapping table with batch and run, dominant variation, relations and floor per process (Table A2). The PA12 attempt is reported as a negative result. Attribute outcomes are named as outside the quantile requirement (Sect. 6.5). A second demonstration was not possible (the letter, Section 6).

**C8. Contribution to design research and AI in DFM.**
*Changed.* The evaluation protocol is presented as the main contribution for the collection (p. 22, l. 991). Sect. 6.4 is developed (R5a). The pooled scopes are reported, and the machine-learning findings are framed as small-data findings. The geometric corners of the simulation dataset have no production counterpart and so cannot be scored against production (ESM Section S6).

### Minor comments

1. *Changed.* FA-side distances in Table 4. For a rule that always decides, δ_d is close to the 90 % quantile of its absolute error (p. 10, l. 422).
2. *Changed.* Interpolation and extrapolation are reported separately in the abstract-level statements (Sect. 5.3, Sect. 6.1, Table 5).
3. *Changed.* Floor by lag (ESM Table S4).
4. *Changed.* ESR is called a practical threshold. 42 of 126 lubrication contrasts have a bootstrap probability of resolvability of at least 0.95 (p. 14, l. 629).
5. *Changed* (Sect. 3.3).
6. *Changed* (Sect. 3.4).
7. *Partly changed.* Stroke speed, start temperature, warm-up and sheet thickness per series are reported (ESM Table S10). The documentation gives no press type, run order, dates, coil certificates or scanning timing; we say so. The tool set has two geometries (p. 11, l. 500).
8. *Changed.* The oil-film–friction mapping is identified as an assumption of the dataset's authors on which Mc, M3 and the matched simulations depend (p. 12, l. 527).
9. *Changed.* Roles in ESM Table S1 and Sect. 4.3.
10. *Changed.* Stability is distinguished from repeatability (p. 14, l. 613).
11. *Changed.* The temperature statement is removed. The temperature-adjusted variant is in the robustness analysis ((location not found)).
12. *Changed.* ">200" with "beyond the interval" (ESM Table S5); "beyond either force interval" in Sect. 5.2.
13. *Changed* (C5).
14. *Changed* (see the editor's points).
15. *Changed.* "Degrades two rules" (p. 16, l. 725).
16. *Changed* (see the editor's points).
17. *Changed* (Sect. 5.6).
18. *Changed.* Shortened. The range guard is described as refusing exactly the extrapolated forces.
19. *Partly changed.* Design angles are stated. The worst side as truth is not adopted. The requirements in this paper are on side-averaged characteristics throughout, and changing the truth for one scenario would mix definitions. The sensitivity (12 truths change) is noted in the response but not in the paper, for length.
20. *Changed.* Cost sensitivity map (ESM Table S28).
21. *Changed.* Variants with a floor between series and with the first 150 parts dropped ((location not found); ESM Table S29).
22. *Changed.* Pooled scopes reported.
23. *Partly changed.* Per-characteristic distances (ESM Tables S17, S18) and capability-anchored verdicts (ESM Table S26) are given. A Ppk axis on Fig. 2 would be misleading, because the translation differs between characteristics.
24. *Changed.* F/σ_LT added to Table 3; the drift column is labelled as the ratio to the permuted-series floor.
25. *Changed.* ISO 5725-2:2025 and 5725-6:1994, ISO 22514-2:2026, AIAG PPAP and Tata and Thornton (1999) added. Further coil-to-coil literature was not added, for length.
26. *Changed.* Notation table (Table A1); "calibration alternatives" is defined there.
27. *Changed.* Core rules in the main text, others in the ESM.
28. *Changed.* `inline_drift.csv` and `ds_surrogate.csv` are regenerated with the current definitions, and `budget_curve.csv` is removed. The DOI archive is the author's action (see B-m21).
29. *Changed.* Sect. 6.6 states the consequences of each threat, for example the extrapolation results describing a force and speed change together (p. 24, l. 1060).

---

## Part 5. New numbers and where they come from

| Number(s) in the paper | Script | Result file |
|---|---|---|
| Decisive/safe distances of all rules and scopes, intervals, one-sided values, coverage, paired differences, GP diagnostics, guard performance | `scripts/decisions.py` | `results/dec_resolution.csv`, `dec_coverage.csv`, `dec_paired.csv`, `dec_gp.csv`, `dec_guard.csv`, `dec_intervals.csv` |
| Scaled simulation M1s, jackknife+ M3/M3n, between-run GP noise floor | `scripts/decisions.py` | `results/dec_intervals.csv`, `dec_resolution.csv` |
| Decomposition (69/6 %, 15/68 %) | `scripts/panel.py` | `results/panel_decomposition.csv` |
| Sibling strata, force levels, source-family floor, physical units, failing-side weight | `scripts/panel.py` | `results/panel_sibling_strata.csv`, `panel_force_levels.csv`, `panel_source_floor.csv`, `panel_physical_units.csv`, `panel_failing_weight.csv` |
| Guard bands and step-6 operating characteristics; reliability by margin (Fig. 4) | `scripts/panel.py`, `scripts/figs.py` | `results/panel_step6.csv`, `panel_step6_curves.csv` |
| Capability-anchored requirements | `scripts/panel.py` | `results/panel_capability.csv` |
| M0 without the cup-depth reference offset (65 floors) | `scripts/panel.py` | `results/panel_m0_split.csv` |
| Drawing nominal plus offset (wall angle) | `scripts/panel.py` | `results/panel_nominal_offset.csv` |
| Floor protocol: σ_b, σ_w, model floor, F/σ; lag profile | `scripts/panel.py` | `results/panel_floor_protocol.csv`, `panel_variogram.csv` |
| Measurement resolution; run metadata | `scripts/panel.py` | `results/panel_resolution_steps.csv`, `panel_runs.csv` |
| Force effect of the simulation (2.7–5.1 times) | `scripts/panel.py` | `results/panel_force_effect.csv` |
| In-line drift analysis | `scripts/inline.py` | `results/inline_drift.csv` |
| Surrogate of the simulations | `scripts/design_space.py` | `results/ds_surrogate.csv` |
| Calibration budget by relation | `scripts/budget.py` | `results/budget_design.csv` |
| Robustness variants (first 150 parts dropped, floor between series, short calibration series, GP variants, M6) and the relation-preserving refit bootstrap with paired intervals | `scripts/robustness.py` | `results/rob_decisions.csv`, `rob_floor_between.csv`, `rob_refit.csv`, `rob_refit_paired.csv` |
| Part-level learners (jackknife+) | `scripts/tuning.py` | `results/tune_decisions.csv` |
| Cost sensitivity map | `scripts/scenarios.py` | `results/scen_cost_map.csv` |

All tables of the paper and the ESM are written from these files by `scripts/make_tables.py`, and the figures by `scripts/figs.py`.

With kind regards,

The author
