# Reviewer 1 (design theory and methodology) — *Research in Engineering Design*

Manuscript: "Alternative-dependent diagnosability: a design-stage method for co-selecting system architecture and monitoring suite ..." (frozen v1, 32 pp.)

## Recommendation: Major revision

The paper has a genuine design-methodological kernel: it moves detectability into architecture selection, proposes a drift-calibrated, unit-free statistic that makes alternatives comparable, and adds a family-level transfer test; it is well written, candid and reproducible. It is not yet a RED paper for four fixable reasons: the "design-stage" claim is never instantiated, and the statistic's denominator is exactly what a design-stage model cannot supply; the selection step that carries the "so what" is never executed; the positioning omits the design community's own failure-reasoning line and overclaims novelty against model-based diagnosability; and three headline claims (control structure, transfer rule, robustness) outrun the evidence, with one internal table inconsistency. All of this is addressable by rewriting and re-running the released pipeline on the same data.

## Summary of the contribution

The author proposes that diagnosability be treated as a property of (architecture, control structure, observation suite) and evaluated during architecture selection. The instrument is the signal-to-drift ratio (SDR): the relative change of a feature between a healthy reference interval and a faulted interval, divided by the α-quantile of the relative change the healthy system shows between adjacent reference intervals, pooled per alternative. From it the paper derives a minimum detectable extent (MDE), a detectable share (DS) and a "signature location", embedded in a six-step procedure (frame, generate trials, compute, map, select, assess transfer). The procedure is instantiated on public bench data of a PMSG, an SCIG and a WFSG with identical tapped winding faults. Findings: equal design-level extent is not equal physical severity; the fault surfaces in different measurement groups per machine; the cheapest adequate suite is drive-internal for the SCIG but needs voltage transducers for the PMSG; and a learned detector transfers only when features are referenced per trial to their own healthy interval.

## Major comments

**M1. Positioning and novelty.** §1 para 1 claims that "for electromechanical systems there is no equivalent method" to testability analysis; the paper's own §2.2 contradicts this, since structural diagnosability and cost-aware sensor placement (Krysander & Frisk; Blanke et al.; Zhang & Rizzoni 2015, on an EV drive) answer "which faults are detectable with which sensor set" from a model structure at the design stage. More seriously for RED, the design community's own line is absent: function–failure mapping (Tumer & Stone, RED 2003; Stone, Tumer & Van Wie, JMD 2005), functional-failure reasoning for evaluating conceptual architectures (Kurtoglu & Tumer, JMD 2008; Kurtoglu, Tumer & Jensen, RED 2010), and PHM feature-quality metrics (Coble & Hines 2009), the SDR's closest relatives. What is new is (i) an empirical, drift-calibrated magnitude of detectability that structural analysis cannot give, (ii) the co-selection framing, (iii) the family transfer test. Say exactly that, delete the overclaim, and add a comparison table (inputs, outputs, cost handling, stage). One useful paragraph, via the uncited Suh (2001): controller and monitor share the DP "current asymmetry", a coupling that explains why signatures relocate.
Addressable: text

**M2. The "design-stage" claim is not credible as framed.** Title, abstract and §3.1 promise a design-stage method; the demonstration is entirely test-stage on built machines, and §6 concedes the design-stage instantiation is future work. The deeper problem is unaddressed: the SDR numerator is simulable by FE/circuit models, but the denominator (sensor noise, thermal drift, controller activity, operating-point wander) is a property of hardware and environment that a simulation will not reproduce, so a simulated SDR is optimistic by an unknown factor. Reframe as a co-selection method whose test-stage instantiation is demonstrated; add a subsection on what a design-stage instantiation must supply (a null from prior hardware of the same class, or noise models) and how bench data would validate it; take "design-stage" out of the title.
Addressable: text

**M3. A metric more than a method: steps 1, 2, 5, 6 are not reusable.** §3.4 calls these "design decisions the method structures but does not take", yet gives no structure: how to elicit e_req and α (link them to fault growth rate and consequence); how many operating points, extents and healthy trials step 2 needs (the ≥ 2× fault-duration rule appears only in §5.3); what c(s) is (never more than ordinal); how to aggregate over several failure-mode classes; and how to decide when bootstrap intervals straddle the requirement (SCIG I2/I1 MDE 2.8 [2.7, 7.4]). Give each a default rule.
Addressable: text

**M4. Step 5 is never executed, so the "so what for the designer" is not shown.** No requirement, no cost and no selected (architecture, suite) pair appear in §4 or §5. Here every alternative reaches the smallest tested extent with some suite, so diagnosability would not have changed the architecture choice, only the monitoring specification (three VTs, negligible at MW scale). Say so plainly and add a decision table: for e_req ∈ {3, 5, 8} % and α ∈ {0.90, 0.95, 0.99}, the cheapest suite per alternative classified meets/uncertain/fails from the bootstrap intervals, with ordinal cost. That table is the design result; then state when the method would change an architecture decision (no affordable suite meets the requirement for one alternative).
Addressable: re-analysis of existing data

**M5. The derived quantities are not requirement-writable as defined.** DS (§3.3) pools extents from 2.3 % to 40 %, so it reflects the benchmark's test matrix, not the alternative; define it conditional on e ≥ e_req or per extent cluster. MDE as min{e : median SDR ≥ 1} is not monotone-safe; define it as the smallest extent above which all tested extents are detectable. The fixed feature is chosen on the same 108 trials it is then evaluated on (§3.2), an in-sample selection over 31 candidates; nest the selection or acknowledge the bias.
Addressable: re-analysis of existing data

**M6. "The control structure decides where the fault becomes visible" is an interpretation, not a result.** Both PMSG and SCIG run FOC on the same bench; the paper separates neither machine physics (magnetising current, back-EMF) from controller action nor the SDR numerator from its denominator. Table `tab:null` shows the SCIG null for I2/I1 is 5× and for I_d 2f_e 35× lower than the PMSG's, so the SCIG/PMSG ratios 3.1 and 12.6 (§4.3) may be largely denominator. Report δ and q_α separately; give controller bandwidths relative to 2f_e if the controller claim stays, else soften to "the machine–drive combination". Also, Table `tab:groups` and Fig. `fig:features` file V2/V1 under "dq/controller" although it is a terminal measurement and §3.3 promises a separate terminal-voltage group, so the tabulated signature location cannot support the mechanism it is cited for.
Addressable: re-analysis of existing data

**M7. The transfer implication conflates two referencing rules.** Table `tab:transfer` shows that z-scoring on the target's healthy trials (a commissioning baseline) transfers poorly (logistic S→P AUC 0.39), while referencing each window to its own trial's immediately preceding interval transfers well. §5.1–5.2 then prescribe "deviations from the unit's own reference behaviour ... established at commissioning", i.e. the rule that failed. The rule that worked presupposes an abrupt onset with a healthy interval seconds earlier, a short-horizon change detector, not monitoring of a slowly developing fault. Further, reference windows normalised on their own mean/std serve as negatives, so the classifier partly learns "is this window inside the normalising interval"; report AUC/TPR on the healthy trials' fault-time windows only. Rewrite the implication.
Addressable: re-analysis of existing data

**M8. Scope understated, generality overstated.** §5.3 says nothing in §3 is specific to electrical machines and that run-to-failure gearbox or battery-cycling trials would serve. As defined, the method needs abrupt seeded faults at a stationary operating point with a healthy interval immediately before the fault, features with non-zero healthy value (δ divides by |φ̄_R|), and an extent scale realisable in every alternative; run-to-failure data meet none of the first set. Add a scope box to §3.5 and make the physical-severity axis of §4.1 part of step 1.
Addressable: text

**M9. Inconsistency in the three-alternative suite table; fragility of the headline.** Appendix Table `tab:suites3` assigns I2/I1 (7.4 %/57 %) or D2/D1 to the PMSG's voltage-including suites although Tables `tab:topfeat` and `tab:sens` give V2/V1 as the strongest PMSG feature at 3 cycles (median SDR 2.5; 2.8 %/73 %); likewise V_d^cmd is chosen for the SCIG where I_d 2f_e is stronger. State the selection rule and fix. At 3 cycles the SCIG's 3 CT MDE is 7.4 %, equal to the PMSG's, so the abstract's "superfluous for the SCIG" holds at 5 and 8 cycles only; say that orderings are robust while MDEs move by one extent cluster.
Addressable: re-analysis of existing data

**M10. Length and structure.** 32 pages, twelve tables and nine figures for two failure-mode classes; the four findings are restated five times (abstract, §1, §4 headings, §5.1, §6); §4.2 is a wall of numbers; the method section (1,200 words) is a quarter of the results. Cut 20–25 %, merge `tab:mde` and `tab:boot`, shorten the 40-word title; this also reduces the desk-reject risk of reading as a condition-monitoring study.
Addressable: text

## Minor comments

m1. Contribution 1 claims "a formal definition of alternative-dependent diagnosability"; none is given. Define it, e.g. the map (a, s, f) ↦ (MDE, DS, location), alternative-dependent when the cheapest adequate suite differs across A beyond bootstrap uncertainty. Addressable: text
m2. Table `tab:alternatives`: PMSG "2.5 kVA" vs SCIG "2.5 kW". Addressable: text
m3. Table `tab:null` gives N = 618 WFSG records for the null; §4.4 says 198. `tab:topfeat` and Fig. `fig:features` pool all WFSG impedances while `tab:suites3` uses the matching one; state one rule. Addressable: re-analysis of existing data
m4. The WFSG has no healthy trials, so the §3.2 screen cannot be applied; define the fallback ("pre-fault null alone", §5.3) in §3 and say on which machines the nine failing features failed. Addressable: text
m5. §3.2 contains demonstration numbers (nine healthy trials, τ = 0.2); move to §4. Addressable: text
m6. "It upper-bounds what a threshold detector on that feature can do" (§3.2) contradicts §3.5; it characterises one specific threshold detector. Addressable: text
m7. False-alarm units differ: per trial in the requirement (§3.3), per window in the transfer experiment (1 % FPR); and the fault interval includes the 85–90 ms relay pick-up transient while the null does not, so only the τ-screen guards the "≈ 1 − α" reading. Addressable: text
m8. Terminology drifts: observation/sensor/monitoring suite; trials/records/recordings; alternative/architecture/topology/machine; extent/severity. Fix one term each in §3.1. Addressable: text
m9. Figures use code identifiers (I2_I1, PId_2fe, Vdconv_2fe, Spd_std) against the text's I_2/I_1, PI_d 2f_e, V_d^cmd; in-figure titles duplicate captions; Fig. `fig:suites` labels collide with markers; Fig. `fig:boot` legend overlaps data. Addressable: text
m10. Fig. `fig:severity` (the design-level axis on which requirements are written) sits in the appendix although §5.1 says the method "carries two severity axes"; bring it forward. Addressable: text
m11. refs.bib holds uncited entries (Suh 2001; Blessing & Chakrabarti 2009, which would let you call the demonstration a support evaluation; Rocha et al. 2023, which describes the bench and should be cited; Jung 2023; Hanley & McNeil 1982); `year = {2026a}` will misbehave under sn-chicago; self-citations Canseven 2024/2025 are tangential where cited. Addressable: text
m12. Placeholders remain (funding, repository URL); the code repository must be live at submission, and Table `tab:transfer3` should footnote the WFSG rows acknowledged as inflated. Addressable: text

## Claims not supported by the presented evidence

- "No equivalent method for electromechanical systems" (§1) — see M1.
- "The control structure decides where the fault becomes visible" (abstract, §5.1) — see M6.
- "The findings are robust to the method's tuning" (abstract) — orderings are; MDEs move by one extent cluster (M9).
- "Transfers only when referenced to the unit's own healthy behaviour" and the commissioning prescription (§5.1–5.2) — the baseline variant did not transfer (M7).
- "A formal definition of alternative-dependent diagnosability" (contribution 1) — not given.
- "The cheapest suite meeting a requirement is architecture-specific" — no requirement or cost is stated (M4).
- "Nothing in Section 3 is specific to electrical machines" (§5.3) — as defined, false for gradual faults (M8).
