# Review report: Reviewer C (manufacturing engineering perspective)

**Manuscript:** "Evaluating design-stage manufacturability decisions against the resolution of production"
**Journal:** Research in Engineering Design, Special Collection "AI in Design for Manufacturing"
**Reviewer focus:** process planning and tryout, statistical process control, process capability, measurement systems analysis, DFM practice in companies

---

## 1. Summary of the submission

The manuscript proposes a framework for judging whether a design-stage prediction is fit to decide a manufacturability question, using production data as the reference. Its unit, the "production floor", is the 95 % limit of the difference between the centres of two 50-part batches of one design within a run. A decision rule that returns *meets*, *fails* or *trial* is characterised by a "decisive" and a "safe" distance (in floors) between the requirement and the true 95th percentile, evaluated separately for three relations of the new design to the produced evidence: a sibling variant, a new process setting, and a new family. The framework is demonstrated on an open dataset of 18 deep-drawing alternatives (two cup geometries × three blank-holder forces × three lubrication patterns, 500 scanned parts each) with matched finite-element simulations. Twelve rules are compared, from the nominal simulation to Gaussian-process and gradient-boosting models, each calibrated rule also without the simulation. The paper concludes that the evidence relation matters more than the predictor, that the nearest produced setting is as decisive as any learned model within a family, and that the simulation helps only for the transfer to the other geometry, where no rule is safe closer than 16 floors.

## 2. Assessment

- **Originality: adequate.** Scoring design-stage manufacturability rules against production by evidence relation, with a production-record baseline and explicit abstention, is new for DFM. However, the floor is in substance a precision limit of the ISO 5725 type for batch means, and the two distances are operating characteristics and guard bands as known from conformity assessment, so the novelty lies in the combination and its use.
- **Significance for design research: adequate.** It gives design margins, test planning and front-loading a measurable, production-referenced quantity. But the implications for design research (Section 6.4) are thin, and no design team was involved.
- **Significance for the collection (AI in DFM): adequate.** The evaluation protocol (production-record baseline, calibrated abstention, evidence relation) is what AI-based DFM support needs. The learned models, however, are fitted to 6–8 alternatives, so the AI-specific conclusions are largely fixed in advance by that data regime.
- **Technical soundness: adequate.** The statistics are careful: grouped cross-validation, an exact estimator, paired bootstrap including the uncertainty of the reference, and an open development record. But the construct validity of the floor (assumptions A2 and A3) and several confounds in the evidence relations are not resolved.
- **Evidence supports the claims: weak.** The numbers for this case are well supported and reproducible. The general answers to RQ2 and RQ3, however, rest partly on features of the design (near-replicate siblings, a new-family baseline that fails by construction), on a confound between force and stroke speed, and on a single simulation that matches production poorly.
- **Clarity, organisation and length: adequate.** The paper is logically organised and precise. It is also very dense (twelve coded rules, often four to six numbers per sentence) and has no worked example; the main text could lose about a fifth of its length.
- **Positioning and references: adequate.** Coverage of V&V, conformal prediction, conformity assessment and design margins is broad. Missing are the ISO 5725 precision limits, time-dependent capability models (ISO 22514-2), industrial capability acceptance criteria, and the literature on process-capability data in design.
- **Fit to RED: adequate.** This is a method with an evaluation, not a case study of one design effort. But the evidence base is one small dataset from one process, so broad applicability is argued rather than shown.

**Strengths that I want to acknowledge.**
- The question is important and rarely asked in DFM research. It is not how accurate a predictor is, but how close to a requirement it can be trusted, and what that costs in production evidence.
- The production evidence (8,990 scanned parts with matched simulations) is unusually rich, and it is handled with care. The use of scan redundancy to choose measurement directions (Section 4.3, Table A8) is good practice that many machine-learning papers in manufacturing skip.
- The nearest-produced-setting baseline and the ablations with and without the simulation are exactly the comparisons that the AI-in-DFM literature tends to omit. The result that a simple production-record rule matches the learned models within a family is useful and credible.
- The reporting is honest: the development record (Section 4.5), the selection optimism, the coverage failures of the Gaussian-process intervals, and the threats to validity are all stated.
- I checked Table 8, the contrast counts of Table 6, and the floors and drift factors of Table 4 against the released result files. I also recomputed the new-setting distances from the stored intervals with the paper's own estimator. All agree.

## 3. Major comments

### 1. The production floor as a production construct: its relation to established precision and capability concepts, and what it measures here

**Problem.** Eq. (2) defines the floor F as the 95 % quantile of the difference between batch centres within one run. Under the stationary model on p. 8, F = 1.96√2·√(σ_b² + σ_w²/B). This is formally the repeatability or intermediate-precision limit of ISO 5725 (the 95 % limit for the difference of two results, 2.8σ), applied to 50-part batch means under within-run conditions.

Section 2.5 relates the floor to capability indices and MSA in two sentences. It does not engage with ISO 5725, nor with ISO 22514-2, whose time-dependent process models describe exactly the location drift that sets the floor here (drift factors 2.1–4.5, Table 4). Three consequences bear on the claims.

- **(a) Comparability.** The paper claims that the floor makes decision fitness "comparable across characteristics and predictors" (pp. 5–6 and 25). It does so only for the resolution of centres, not for conformance. From the released files (`dec_alternatives.csv`, `alt_floor.csv`), one floor equals a median 1.4 standard deviations of the parts over a run. Per characteristic and geometry it ranges from 0.66σ (wall angle, convex) to 2.2σ (cup depth, concave), and over alternatives from 0.48σ to 3.0σ. Because the ratio of drift to part scatter differs between characteristics, the same distance in floors means very different nonconforming fractions.
- **(b) Dependence on the protocol.** F grows with series length (the first half of each series gives 0.49–0.95 of the full value, Table 5) and shrinks with B. Taking α = 0.90 or 0.99 instead of 0.95 rescales all distances by factors of 0.54–1.46 (Section 5.9, Table 12). The paper says so on p. 8, but Table 13 then treats the floor as a portable unit. Without a reference protocol, distances from two studies or two plants cannot be compared.
- **(c) Run-to-run variation.** F excludes variation between runs. The paper bounds that variation at 1.2–9.8 floors (Table 5), so it may be several times F. In series sheet-metal production, coil-to-coil material variation, the thermal state of the die and the lubrication condition between runs usually dominate. A single 500-part run per alternative cannot represent them. Assumption A2 ("the runs ... are like those of future production", p. 7) is therefore not met. Likewise, the reference q₉₅ is the q₉₅ of one run: its bootstrap standard error (about 0.1 floor) covers only sampling within the run.

**Why it matters.** Every result is expressed in floors. One floor means 0.7σ for one characteristic and 2.2σ for another, its size depends on run length, and it leaves out the dominant variance component of series production. The distances are therefore neither comparable across characteristics in the sense practitioners will assume, nor transferable to series production.

**What would resolve it.**
- Relate F explicitly to the ISO 5725 precision limits, to σ_ST/σ_LT and to the ISO 22514-2 models, and state what is new.
- Report F/σ_ST and F/σ_LT for each characteristic and geometry (Table 4 is the natural place).
- Justify why centre resolution, rather than the reproducibility of the decided quantile (the "q₉₅ floor" of Table 5) or σ_LT, is the right unit for a decision on q_p. Alternatively, show that the main conclusions hold under one alternative normalisation.
- Add to Table 12 a variant whose floor includes the between-series component (as an upper bound), and propagate run-to-run uncertainty into the reference q₉₅.
- Define a reference protocol (series length, B, α, number of runs) for reporting floors.

### 2. Assumption A3 and the source of the drift that sets the floor

**Problem.** A3 ("the measurement adds little") is said to be "checked in Section 5.1" (p. 7). That check (white share 15–33 %, Table 5) bounds only measurement noise that is independent from part to part. The floor, however, is set by drift (Table 4), and the paper concedes that scanner drift cannot be separated from process drift (pp. 14 and 28). The sentence that the floor "is dominated by variation between batches, which a repeatable measurement cannot create" (p. 14) conflates repeatability with stability, which MSA treats as separate properties (AIAG 2010).

The available evidence does not identify the process as the source of the drift:
- Correcting every characteristic for punch temperature changes the floors by only −14 to +4 % (p. 24), although p. 14 names the temperature rise as "one of the sources of this drift".
- The in-line analysis released with the code but not reported (Appendix A.2; `scripts/inline.py`, `results/inline_drift.csv`) finds that batch centres of press force, punch temperature, sheet thickness and oil film do not predict the batch drift of any characteristic out of fold (R² from −0.23 to 0.11). Removing the predicted drift lowers the floors by at most 16 % and raises some by up to 11 %.
- A simple check I made on the released feature table points the same way. The size of each run's warm-up (punch-temperature rise over the first three batches, about 0.5–3.7 K) does not predict the spread of batch centres within the run for six of the seven characteristics (Spearman |ρ| ≤ 0.29; cup depth 0.47).

**Why it matters.** If part of the floor is scanner drift, the unit is partly a property of the measuring system. That undermines its reading as "the resolution of production", its use for minimum resolvable changes (Table 6), and the transfer of floors between plants with different gauges.

**What would resolve it.**
- State whether the parts were scanned in production order, and when (same session? same day?).
- Report and discuss the in-line drift analysis.
- Use any available evidence on scanner stability: repeated scans of retained parts in a different order, a master part, or ambient-temperature logs from the dataset authors.
- Either show that A3 holds for drift, or reframe the floor as a "production-and-measurement floor" and state the consequences.

### 3. Decision situations and requirements compared with how release decisions are made

**(a) What the distances mean in capability terms.** Adequacy means q₉₅ ≤ R, i.e. at most 5 % nonconforming parts. For a normal characteristic that is a Ppk of about 0.55 (median 0.53 in these data). Release criteria in series production are typically Ppk ≥ 1.33, and ≥ 1.67 for initial process studies (AIAG PPAP).

I translated the headline distances using the released data, with R = q₉₅ + dF and a Ppk equivalent of (R − centre)/(3σ), taking medians over the 126 alternative–characteristic cases:

| Requirement position | Meaning |
|---|---|
| 1 floor above q₉₅ | Ppk ≈ 1.0 |
| 3.4 floors above | Ppk ≈ 2.1 |
| 8.5 floors above | Ppk ≈ 4.5 |
| 16 floors above | Ppk ≈ 8 |
| 1 floor below q₉₅ | about 44 % of parts nonconforming (empirically) |
| 3.4 floors below | about 99.8 % of parts nonconforming |

It follows that:
- With a produced sibling, the nearest produced setting is ≥ 95 % correct only for alternatives with Ppk ≳ 2, or with almost no conforming parts.
- For a new process setting, that holds only for Ppk ≳ 4.5; for a new family, only for Ppk ≳ 8.
- The decisions that matter for process release (Ppk ≈ 1–2, nonconforming fractions from ppm to a few per cent) lie inside every decisive distance reported. Interval rules can be safe there only by sending a large share of designs to trial.

This is the core practical message behind "when a physical trial is unavoidable" (abstract), and the paper never states it. The paper also notes (p. 28) that conformance levels as used in industry would need a parametric tail. The abstract should therefore say that the demonstration covers a 95 % conformance level.

**(b) Characteristics and form of the requirement.** Draw-in and flange waviness are measured on a flange that is cut away in OP20. In tryout they are process indicators (material flow, tendency to wrinkle) rather than drawing requirements. Cup depth and wall angle would normally carry two-sided tolerances about a nominal, not one-sided upper limits. The central design-stage manufacturability questions in deep drawing (splits, wrinkles, thinning, and springback against profile tolerances) lie outside a framework that handles continuous dimensional characteristics with one-sided limits on a quantile.

**(c) The ISO 2768-1 scenario (Section 5.8, Table 11).** According to `results/scen_truth.csv`:
- the convex arm angle fails every tolerance class by 15–43 floors (q₉₅ ≈ 4.8° against limits of 1–3°);
- the wall angle fails classes f/m and c by 6–17 floors, because the parts' wall angles lie well above the tool's design angle (q₉₅ about 1.5–1.8° above 20° and 10°; Fig. 2 shows the whole 5–95 % range above it; the design angles are not stated in the paper);
- only 32 of the 108 decisions lie within 5 floors.

In tryout, such systematic deviations are removed by die compensation before any release decision. This scenario therefore mostly tests whether rules recognise gross failures; it is not "requirements with realistic margins". In addition, the "shorter leg" of the convex arm (about 9 mm, including two 1 mm margins added by the analyst) moves it into a coarser ISO 2768-1 row.

**(d) The cost and the error of a trial depend on the evidence relation.**
- For a new blank-holder force or lubricant on an existing die, a trial is a short press run. In automotive supply, a process change normally requires a production trial run with a capability study anyway.
- For a new family, a trial means a new or reworked die and weeks of lead time.
- Section 5.8 nevertheless applies one cost structure to all relations (c_FR = 0.5 c_FA; c_T = 0.02–0.5 c_FA).
- Section 3.4 treats trials as error-free, although a short trial run resolves q₉₅ only to about 1–1.5 floors (q₉₅ floor, Table 5). That is precisely the zone in which trials are triggered.

**Why it matters.** These choices decide whether the framework answers the question in its title for real design and process-planning decisions. As reported, a reader cannot see that the trustworthy region corresponds to very large capability margins.

**What would resolve it.**
- Report the operating characteristics also at requirement positions anchored in capability, e.g. limits at which each produced alternative has Ppk = 1.0, 1.33, 1.67 and 2.0. The existing d-grid supports this. Add a capability-equivalent axis to Fig. 3 or a column to Table 8.
- Give the headline distances also in units of the characteristic.
- Restrict requirements to characteristics a drawing would carry, with two-sided limits where appropriate.
- Replace or complement the ISO 2768 scenario with requirements anchored after die compensation.
- Make the cost and the error of a trial specific to the evidence relation.
- State in the abstract and in Section 3.1 that the framework addresses dimensional conformance at a modest conformance level.

### 4. Confounds and structural features of the evidence relations that carry RQ2 and RQ3

**(a) The new variant is a near-replicate.**
- The variant differs from its siblings only in lubrication. Production does not resolve lubrication in 75 of 126 contrasts (Table 6; median ESR 0.7), and the oil amounts of the patterns overlap (Section 4.1).
- The nominal simulation and the envelope depend only on geometry and force; I confirmed in `dec_alternatives.csv` that they are identical across siblings. M0, M0w, M1, M2 and M5 therefore receive no simulation information that distinguishes the variant from its siblings. Only Mc and M3 see lubrication, through the oil-film mapping.
- The 3.4 floors of the nearest produced setting are therefore mainly an estimate of how reproducible q₉₅ is between near-replicate runs (compare the between-series bound of 1.2–9.8 floors in Table 5).
- The statement that "within a family [the simulation] adds nothing" is partly built into this relation. The paper itself notes (p. 24) that leaving out a whole lubrication pattern "behaves like a new variant ... because the siblings at the same force remain".
- In Table 9, the k = 1 sibling results of M1, M2 and NN are algebraically one rule, not three rules that agree: the simulation terms cancel, and with a single calibration alternative the margin of M2 is zero.

**(b) Extrapolation in force is confounded with stroke speed.** The 100 kN alternatives ran at a slower stroke (pp. 15 and 28; about 47 against 79 mm/s in the feature table). I split the 84 extrapolation cases of the new-setting scope by force level, using the paper's own estimator on `dec_intervals.csv`:

| Rule | 100 kN | 500 kN | Interpolation (300 kN) |
|---|---|---|---|
| NN, decisive distance | 11.0 | 4.85 | 4.65 |
| M2n, safe distance | 9.9 | 3.6 | – |
| M5n, safe distance | 10.1 | 2.25 | – |
| M4, safe distance | 9.85 | 3.2 | – |
| M2, safe distance | 8.1 | 9.95 | 2.7 |
| M5, safe distance | 8.1 | 9.65 | 2.85 |

Only the simulation-based rules M2 and M5 are unsafe at both ends. The production-only rules lose almost only at 100 kN. The statement that "extrapolating in force doubles the decisive distance of the nearest produced setting" (p. 25) therefore rests on the cases in which force and speed changed together.

**(c) Run order and thermal state are not reported.**
- In the released feature table, runs start at punch temperatures between about 21 and 30 °C, and the rise occurs mostly within the first ~150 parts.
- In several geometry–force cells the start temperature increases in the order coarse, medium, fine. This suggests that the lubrication pattern is partly confounded with run order and with the thermal state of the die.
- Median sheet thickness also differs between runs (about 0.986–0.993 mm), which suggests different positions on the coil, or different coils.

**(d) The new-family baseline fails by construction.**
- With one family in the calibration set, the geometry descriptor is constant and is dropped (Appendix A.1). M1n, M2n, M4, M5n and NN can therefore only return the other family's values. Their failure (131–133 floors, Table 8) is a property of the evaluation design, and the "about 93 floors" contributed by the simulation (p. 19) is measured against a baseline no practitioner would use.
- Without a simulation, a designer would start from the drawing nominal and add the deviation observed on the produced family. For the wall angle, q₉₅ − nominal is about 1.64° in both families. A rule "nominal plus the other family's median deviation" predicts the new family's q₉₅ within a median 0.3 floors (90 % quantile 1.8 floors). The bias-corrected simulation M1 reaches a median 5.3 and a 90 % quantile 15.9 floors, and the paper's production-only rules about 126 floors (my computation from `dec_alternatives.csv` and `dec_intervals.csv`).
- For other characteristics such a baseline would fail; for example, the arms deviate from flat by about 0.6° on the concave and 4.8° on the convex cups. That contrast is exactly the comparison that would show where the simulation is needed.

**Why it matters.** These four features carry the headline answers to RQ2 and RQ3 (abstract, Sections 6.1 and 7).

**What would resolve it.**
- Describe the variant relation as prediction of a near-replicate run, or stop treating a lubrication change as a design change.
- Report the extrapolation results by force level and discuss stroke speed.
- Report run order, start temperatures, coils and dates, and add these confounds and their consequences to Section 6.6.
- For the new family, add a "drawing nominal plus offset" baseline for the characteristics that have a nominal.
- Moderate the statements made for RQ2 and RQ3 accordingly.

### 5. How representative the simulation is, and the scope of the RQ3 conclusion

**Problem.** The simulation (Sections 4.2 and 5.3) has several weaknesses that a tryout engineer would see at once:
- It is a quarter model with nodes about 1 mm apart.
- It uses a constant Coulomb friction coefficient, mapped linearly from the oil film, and its yield criterion and unloading model are not documented.
- Its blank-holder-force effect is 2.6–5.1 times the measured one, it is about 3 mm off in corner draw-in, and it gives the wrong sign for the concave arm angle.
- Its extraction noise reaches about 10 floors (Table A9).
- Its process window varies sheet thickness and friction but not material properties, which in practice dominate springback scatter. The envelope used by M0w, M2 and M5 therefore does not represent production variation.
- Part of the 108 floors of M0 is a matter of definition: the nearly constant cup-depth offset of −0.90 to −0.95 mm comes from the reference surface (p. 16).

No tryout team would take draw-in or springback decisions with an uncalibrated model of this kind. Industrial practice calibrates material cards and friction and compensates springback. Nevertheless:
- the abstract and the conclusions state without qualification that "the simulation contributed only to the new family";
- Table 13 lists the nominal simulation as "reliable beyond about 108 floors";
- Section 6.3 generalises to "the evaluation of AI-based DFM support".

**Why it matters.** Readers of an AI-in-DFM collection will read RQ3 as a statement about simulation and machine learning in DFM in general.

**What would resolve it.**
- Limit the RQ3 conclusions to this simulation and this data regime in the abstract and in Sections 6.1, 6.3 and 7.
- Remove known definitional offsets (reference surface, sheet thickness) before scoring M0.
- State the headline distances also in units of the characteristic: 16 floors is about 0.8 mm of mid-side draw-in and about 1.3° of wall angle. Forming readers can compare these with the known accuracy of springback simulation.
- If feasible, include one better-calibrated predictor, for example Mc with a pressure-dependent friction law.

### 6. What a design or process-planning team would need: applicability and cost in production evidence

**Problem.** Steps 2–5 of the procedure (Fig. 1) need, per family:
- several produced variants, each with a long run of consecutive parts;
- every part measured with definitions identical to those of the simulation (here 8,990 scans);
- a simulation of every variant.

That is evidence at the scale of series production or PPAP, not of the design stage; a tryout loop yields tens of parts. Because the floor grows with run length, a team that qualifies rules on short tryout runs obtains a smaller floor, and hence larger distances in floors. Qualifications are therefore not portable between protocols (see comment 1b). The paper does not say who in a company runs steps 1–5, at which milestone or at what cost, nor what step 6 looks like for a single decision. Section 6.5 lists the four prerequisites but not how much of each is needed.

**Why it matters.** RED and this collection look for methods that teams can apply. Whether the framework is usable depends on its cost in production evidence.

**What would resolve it.**
- Add a worked example of step 6 for one alternative and one characteristic, from the floor to the verdict and its margin.
- Derive a minimal evidence protocol (number of variants, parts per run, B, number of runs, measurement) from material already in the paper (B = 25/100, first half, k = 1–8 in Table 9), and state how sensitive it is.
- Place the procedure in the development process, e.g. qualifying rules at start of production or PPAP for later decisions on variants and process changes.
- Discuss cheaper sources of evidence (sampled measurement, in-line force signals) and what the floor becomes with them.

### 7. Transfer to the processes named in the call

**Problem.** Section 6.5 states that "None is specific to forming" (p. 27). Yet the paper's only attempt at transfer, powder bed fusion of PA12, found the first prerequisite unmet (no batches of one design; eight anchor specimens per build). The floor presupposes long runs of identical parts in a known sequence. That fits stamping and, largely, injection moulding. Elsewhere it does not:
- In additive manufacturing the build is the unit of variation, with position effects and few replicates.
- In small-lot machining, drift from tool wear is compensated by offsets, and inspection is sampled.
- Multi-cavity moulds and multi-impression casting add nested structures (cavity within shot within run) that Eq. (2) does not handle.
- Many manufacturability outcomes in these processes are attributes (porosity, short shots, sink marks, cracks), which a quantile requirement on a continuous characteristic does not cover.

**Why it matters.** The collection names additive manufacturing, injection moulding, machining and casting explicitly, and RED asks for broad applicability.

**What would resolve it.**
- Add a short mapping table with one row per process: what a batch and a run are, the dominant variance components, the evidence relations, the predictors available, and the type of requirement. Include a proposed floor for each (e.g. a nested floor for multi-cavity tools, or a between-build floor from replicated anchor specimens for additive manufacturing).
- Report the PA12 attempt as a negative result, with its lessons.
- Ideally, add a second demonstration on an open dataset from another process.

### 8. Contribution to design research and to AI in DFM

**Problem.**
- The implications for design research (Section 6.4) occupy one paragraph. The links to margins (Eckert et al. 2019; Brahma and Wynn 2020), test planning (Thomke and Bell 2001) and front-loading are asserted rather than developed, and the decision situations are not grounded in any evidence of how teams decide.
- The AI part consists of Gaussian processes and boosting fitted on 6–8 alternatives with three descriptors, one of which production rarely resolves. In the Gaussian-process fits the noise level sits at its lower bound in up to 45 % and a length scale at a bound in up to 62 % of cases (Table A7). The finding that learned models "add calibrated abstention rather than accuracy" is therefore largely predetermined.
- The pooled scopes test the common AI-in-DFM practice of pooling another family's production record. They are defined (Section 4.4) but not reported in Table 8. The released `dec_resolution.csv` indicates that pooling makes several rules worse for a new variant: M5 6.7 → 11.3 floors, M1n 9.1 → 130, M2n 19 → 325.

**Why it matters.** RED expects a contribution to design theory, and the collection seeks understanding of how AI changes decision-making in DFM.

**What would resolve it.**
- Present the evaluation protocol as the main contribution.
- Develop Section 6.4: for example, how the decisive and safe distances put a number on the value of a margin and on when to test, and how trust in AI-based DFM support should be calibrated for each evidence relation.
- Report the pooled scopes.
- Frame the machine-learning findings as small-data findings.
- If possible, show the protocol in a regime where learning could help, e.g. geometric descriptors across the simulation design space mentioned in Appendix A.2.

## 4. Minor comments

1. **Abstract; Section 3.4, p. 10.** Both signs are weighted equally at ±δ. A rule that always decides therefore reaches "at least 95 % correct" when 90 % of its absolute errors lie within δ, and for a biased rule the one-sided error rate at the decisive distance can approach 10 %. Say this in the abstract, or base headline claims on the one-sided distances (Table A2).
2. **Abstract; Section 6.1, p. 25; Table 13.** "No rule decided closer than 8.5 floors" pools interpolation (NN 4.7) and extrapolation (NN 9.5) in the 1:2 ratio fixed by three force levels. A team knows which case it faces, so report both.
3. **Eq. (2), p. 7.** Pooling all 45 batch pairs per run (lags 1–9) means that, under monotone drift, F is close to the range of batch centres over a run. The median within-run range is about 0.6–1.0 floors per characteristic. Reporting the batch difference as a function of lag (a variogram) would show directly how the floor scales with run length.
4. **Eq. (3), p. 8.** ESR ≥ 1 compares centres of 500-part runs with a floor of 50-part batches, so it is a practical, not a statistical, threshold; say so. The counts in Table 6 use point estimates. With a bootstrap probability of resolvability ≥ 0.95 (column `p_resolvable` in `alt_effects.csv`), 42 rather than 51 of the 126 lubrication contrasts are resolved; report this.
5. **Table 2 / Section 3.3.** State explicitly that the nominal simulation and the envelope do not depend on the lubrication pattern; this is essential for reading Sections 5.4–5.6.
6. **Section 3.4, p. 10 (decision-theoretic paragraph).** "Trials error-free" is optimistic near the requirement. Include the trial's own operating characteristic, e.g. the q₉₅ floor of Table 5 for a trial run of 100 parts.
7. **Section 4.1.** Describe the press (type and drive), the stroke rate, and the run order and dates of the 18 series. Give the coil or material batch with its certificate values (yield strength, r-value), say whether warm-up parts were discarded, and describe the scanning set-up, order and timing. Also clarify whether the two geometries are separate tools or inserts in one tool set; this matters for what "new family" means physically.
8. **Section 4.2.** The linear mapping from oil film to friction coefficient (0.8–1.6 g/m² → 0.15–0.05) is an assumption of the dataset authors. It governs M3, Mc and all matched simulations, so give its basis or discuss its validity.
9. **Section 4.3 and Table 3.** Give the engineering role of each characteristic (product requirement or process indicator), and the form a requirement on it would take on a drawing.
10. **Section 5.1, p. 14.** "Which a repeatable measurement cannot create": a measuring system can be repeatable and still drift. Rephrase in terms of stability (see major comment 2).
11. **Section 5.1, p. 14 against Section 5.9, p. 24.** The punch temperature is called "one of the sources of this drift", yet the temperature correction changes the floors by only −14 to +4 %. Either quantify the contribution or soften the statement.
12. **Table 6, p. 16.** Several minimum resolvable changes exceed the 200 kN interval over which the local slope was estimated (wall angle 366–420 kN, dome 543–731 kN, arm angle 1083 kN between 300 and 500 kN). They are extrapolations; report them as "beyond the interval" rather than as numbers.
13. **Section 5.3, p. 16; Table 13.** Separate definitional offsets (shell mid-surface against scanned surface, drawing depth) from physical simulation error before scoring M0. Otherwise "reliable beyond about 108 floors" overstates the simulation's error.
14. **Section 5.4, p. 18.** "Every calibrated rule improves by an order of magnitude": Mc improves from 108 to 27 floors, a factor of four. M1 is essentially removal of the bias.
15. **Section 5.5, p. 19.** "Within a family it adds nothing": the paired differences M2 − M2n (+3.9) and M1 − M1n (+6.2) show that the simulation degrades these rules. Say so.
16. **Section 5.5, p. 19.** "Exactly the n/(n+1) = 8/9": with an offset estimated from the same residuals, the guarantee under exchangeability is only (n−1)/(n+1) = 7/9 (as Section 3.3 itself states), and the cases are not exchangeable. The agreement with 8/9 is coincidental.
17. **Section 5.6, Table 9.** Note that M1, M2 and NN coincide algebraically for a single sibling (see major comment 4a).
18. **Section 5.7, Table 10.** For a new setting, the range guard refuses exactly the extrapolated cases by construction, so it restates the interpolation/extrapolation split. The novelty guard is the informative one; the text can be shortened.
19. **Section 5.8.** State the design angles used (20° and 10°). Note that a general tolerance applies to every feature of every part, i.e. 100 % conformance, not to the q₉₅ of a mean over sides. The 12 truths that change with the worst side indicate how sensitive the scenario is to this choice; consider the worst side as the primary truth.
20. **Section 5.8.** The cost ratios (c_FR = 0.5 c_FA; c_T = 0.02–0.5 c_FA) need an industrial rationale, or a sensitivity map over c_FR/c_FA and c_T/c_FA.
21. **Table 12.** Add a variant whose floor includes the between-series component, and one that excludes the first ~150 parts of each run (the thermal transient).
22. **Section 4.4.** The pooled scopes are defined but appear only in Table A7. Report them in Table 8, or remove the definition (see major comment 8).
23. **Fig. 3, p. 20.** The curves pool seven characteristics with very different F/σ. Per-characteristic panels in the appendix and a secondary axis in Ppk equivalent or nonconforming fraction would help practitioners.
24. **Table 4, p. 15.** Add F/σ_LT. Label the "Drift" column as the drift factor (floor over the floor of permuted series), and state whether "Part SD" is σ_LT.
25. **Section 2.5 and references.** Add:
    - ISO 5725 (Parts 1, 2, 3 and 6: repeatability, intermediate precision, critical differences);
    - ISO 22514-2:2017 (time-dependent process models);
    - AIAG PPAP (4th edn) acceptance criteria for initial process studies;
    - the literature on using process-capability data in design (e.g. Tata and Thornton 1999);
    - on the forming side, work on coil-to-coil and run-to-run variation in series stamping beyond Havinga et al. (2020) and Purr et al. (2015).
26. **Terminology.** "Calibration" is used in three senses: V&V calibration of a simulator parameter, the "calibration alternatives", and, implicitly, metrological calibration. "Resolution" also has a fixed meaning in MSA (gauge resolution). A short glossary would avoid misreadings by practitioners.
27. **Clarity and length.** Twelve rule codes (M0, M0w, M1, Mc, M2, M3, M5, M1n, NN, M2n, M4, M5n), plus M6, which appears only in Section 5.9, are hard to follow. Keep in the main text the rules that carry conclusions and move the others to the appendix. The sentences carrying four to six numbers each in Sections 5.4, 5.6 and 5.9 would read better as tables.
28. **Reproducibility package.** `results/` contains files produced with a superseded characteristic definition: `inline_drift.csv` reports a mid-side draw-in floor of 0.085 mm, the older definition quoted on p. 14. It also contains a file that no current script writes (`budget_curve.csv`). Neither is used in the paper, but both should be regenerated or removed. Please also deposit code and feature tables with a DOI for the review rather than only at acceptance.
29. **Section 6.6.** The threats are listed but their consequences are not. For example, "the blank-holder force of 100 kN ran at a slower stroke" should be followed by what this does to the extrapolation results (major comment 4b), and the same holds for run order and thermal state.

## 5. Recommendation

**Major revision.**

The paper asks a question that DFM and AI-in-DFM research should ask more often, uses a rare production dataset with care, and is exemplary in transparency and reproducibility. Its procedural idea would be a useful contribution to RED and to this collection: qualify a predictor for the evidence relation of the coming designs, against a production-record baseline, with explicit abstention. As submitted, however, three problems stand in the way:
- The unit on which every result rests is not yet established as a production construct. Its relation to established precision and capability concepts, its dependence on the protocol, and the unresolved source of the drift that sets it all need attention.
- The decision situations and requirements are not anchored in how release decisions are made. Read in capability terms, the reported trustworthy region begins at about Ppk 2 with a produced sibling and about Ppk 4.5 for a new process setting.
- Several headline answers to RQ2 and RQ3 are partly built into the evaluation design or confounded: near-replicate siblings, force extrapolation coinciding with a speed change, and a new-family baseline that fails by construction.

Most of this can be addressed with the existing data and code: capability-anchored requirements, the split by force level, a nominal-plus-offset baseline, the pooled scopes, the in-line drift analysis, and the run-order information. Together with reframing and narrower claims, that would make the paper's contribution clear and its conclusions defensible. A demonstration on a second process would substantially strengthen the fit to the collection, but I would not make it a condition. I would be glad to review a revised version.

## 6. Confidential comments to the editor

The manuscript is technically careful and unusually transparent. I checked several tables against the released result files and found them consistent. The released code also contains analyses not reported in the paper that bear on its conclusions; I draw on one of them in major comment 2. My concerns are about construct validity, confounding and practical relevance rather than computational errors, and I consider them addressable within one revision. The AI content is modest for an "AI in DFM" collection: the work is best read as an evaluation protocol for simulation- and AI-based DFM support. Its fit therefore depends on the author developing that angle and the implications for design research. Rejection would be too harsh given the quality of the analysis. Acceptance without major comments 1–4 being addressed would, however, invite readers to over-read the practical reach of the results.
