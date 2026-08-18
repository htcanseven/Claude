# TIA Paper Structure

**Route:** EPEi 2026 conference paper → invited extension to IEEE Transactions on
Industry Applications. Structure the journal paper first; the conference paper is a
carve-out (Section 10).

**Data:** Brno CEITEC pair — Zenodo [10.5281/zenodo.15233529](https://zenodo.org/records/15233529)
(modeling, 144.6 MB) and [10.5281/zenodo.21717722](https://zenodo.org/records/21717722)
(mitigation, 601 MB). Both verified open access with files present (checked 18 Aug 2026).
Companion papers: Zezula et al., IEEE TIE 71(11) 2024 (diagnostics) and TIE 73(1) 2026
(discrete-time modeling).

---

## 1. Working title

> **Finite-Element Assessment of Lumped-Parameter Interturn Short-Circuit Models in
> Interior PMSMs: Effective Fault Severity, Saturation, and Series-Parallel Windings**

Alternatives:
- *Electromagnetic Limits of Lumped Interturn Short-Circuit Models for PMSM
  Diagnostics: An FEA and Open-Benchmark Study*
- *Bridging Machine Design and Model-Based Diagnostics: FE Validation of Interturn
  Short-Circuit Models for Concentrated-Winding PMSMs*

Title must signal: (a) machine-side physics, not another ML classifier; (b) validated
on experimental data; (c) actionable for diagnostics people.

## 2. One-paragraph pitch (the cover-letter claim)

Model-based ISC diagnostics — the state of the art for embedded, transient-capable
fault-indicator estimation — rest on lumped-parameter fault models whose key
constants are taken as winding-topology facts: fault severity equals the shorted-turn
ratio, inductances are the healthy machine's, and windings are series-connected. None
of these holds exactly in a real machine, and no one has quantified the error. We
build a turn-level finite-element model of the open-benchmark IPMSM of Zezula et al.,
quantify each assumption's error across the published severity × short-circuit-resistance
× operating-condition grid, show how the errors bias state-of-the-art severity
estimators, provide a design-derived correction with zero runtime cost, and extend the
model to the series-parallel winding case the benchmark authors explicitly left open.

## 3. Contributions (C1–C5)

| # | Contribution | Novelty claim |
|---|---|---|
| **C1** | Turn-level FE model of the 253 W concentrated-winding IPMSM (21 pole pairs, 6 segments × 25 turns/phase), calibrated to the published parameter set (Rs 727 mΩ, Rc 362 mΩ, Ld 3.29 mH, Lq 3.12 mH, L0 2.74 mH, λpm,1 18.4 mWb, λpm,3 200 µWb) and verified against measured back-EMF harmonics and terminal behavior | First independent electromagnetic replication of an open ISC benchmark machine |
| **C2** | **Effective fault severity.** Test the x_f = r/N assumption at turn level: flux linked by shorted turns depends on radial slot position through leakage; derive an effective-severity map x_f,eff(r, position, load) and the resulting fault-current prediction error | The assumption is used by essentially every lumped ISC model; its error has not been quantified against experiment |
| **C3** | **Saturation under fault.** Incremental Ld, Lq, Lf vs load (1–3 Nm) and severity; local saturation around the shorted coil is invisible to lumped models. Propagate through the TIE-2024 severity estimator → bias map over the 3-severity × 4-Rsc grid | Explains (or bounds) residual estimation errors the incumbents observe but do not attribute |
| **C4** | **Series-parallel extension (np > 1).** Generalized fault model including segment-linking resistance — the case the TIE-2026 paper states violates its model — with FEA analysis of inter-branch circulating currents under ISC | The benchmark authors' own acknowledged open gap; parallel-branch windings are standard in traction and MW machines, which is the industrial-relevance hook |
| **C5** | **Open-benchmark validation.** Every claim tested against the published measurements: 3 severities × 4 R_sc × {steady, velocity-transient 10⁴ rad/s², load-transient 50 Nm/s} from 15233529; mitigation on/off from 21717722 (does mitigation reshape the signature as the corrected model predicts?) | Fully reproducible — no closed data anywhere in the paper |

**Methodological identity:** machine-design/FEA paper that serves diagnostics, not a
diagnostics-algorithm paper. We never compete with Zezula's estimator; we calibrate it.

## 4. Section skeleton (journal, ~10 pp double column)

**I. Introduction** (~1 p)
ISC risk chain (insulation → fault current → thermal runaway). Model-based diagnostics
as SOA for embedded/transient operation. The gap: lumped fault models embed
design-level assumptions never checked against the electromagnetic design. Contributions
C1–C5. Cite own prior work (IECON 2021 dual three-phase ITSC FTC; TIA 2022/2024) and
the Brno line (TIE 2024, TIE 2026).

**II. Lumped ISC Models and Their Embedded Assumptions** (~1 p)
Recap the α–β / dq fault model (healthy + fault-current subsystem, Φ matrix, R*f, Lf).
Enumerate the assumptions as testable hypotheses:
- **A1:** x_f = r/N (severity = turn ratio, position-independent)
- **A2:** Ld, Lq, λpm of the faulted machine = healthy identified values (no local saturation)
- **A3:** series connection, np = 1; segment-linking resistance negligible
- **A4:** fault resistance lumped, wiring inductance negligible (note: the benchmark's
  own FIU adds L_wire = 3.81 µH — use this as a worked example of A4's violation)

**III. Turn-Level Finite-Element Model** (~1.5 pp)
Geometry reconstruction from the published internal-structure figure and parameter
table; calibration protocol (match Rs, Ld/Lq via locked-rotor-equivalent simulation,
λpm harmonics via back-EMF); verification table (measured vs FE, target < a few %).
**State openly:** exact laminations unpublished → representative calibrated model;
sensitivity of conclusions to geometric uncertainty quantified in an appendix-style
subsection (vary tooth-tip/slot-opening dims, show conclusions hold).

**IV. Effective Fault Severity (tests A1)** (~1.5 pp)
Turn-resolved winding in FE; short each turn subset at each slot position; compute
linked flux and fault-loop inductance vs position. Deliver: x_f,eff map; error in
predicted i_f vs the r/N model across severities 3/25–10/25 and 4 R_sc levels.

**V. Saturation Under Fault (tests A2)** (~1.5 pp)
Co-simulate fault current at operating points spanning 1–3 Nm, 1200–1900 rad/s.
Incremental inductance fields around shorted coil; equivalent Ld,Lq,Lf shifts; severity
bias when the estimator uses healthy parameters. Deliver: bias map over the published
grid; identify where the lumped model is safe (low load / high Rsc) vs unsafe.

**VI. Series-Parallel Windings (closes A3)** (~1.5 pp)
Extended state-space model with np > 1 and segment-linking resistance Rc; circulating
current between parallel branches under ISC (FEA); observability consequence: does the
terminal-signature severity indicator under- or over-read for parallel windings?
Scaling argument to traction/MW machines (ties to LUT high-specific-power line).

**VII. Benchmark Validation** (~1.5 pp)
Experiment matrix (Section 6). Metrics: fault-current amplitude/phase error, severity
estimate bias, transient trajectory error vs both DTM variants (forward Euler,
matrix-exponential). Mitigation on/off comparison from 21717722.

**VIII. Implications for Diagnostics** (~0.5 p)
Corrected severity indicator = published estimator × design-derived correction (lookup,
zero runtime cost — keeps the 3 ms / embedded story intact). When is correction
worth it; practitioner guidance table.

**IX. Conclusion** (~0.25 p)

## 5. Figure and table plan

Figures (~10): (1) fault circuit + assumption schematic; (2) FE model + flux plot
healthy/faulted; (3) calibration: measured vs FE back-EMF spectrum; (4) x_f,eff vs turn
position, per severity; (5) i_f prediction error vs r/N model; (6) saturation maps
around shorted coil; (7) severity-bias surface over severity × Rsc grid; (8) np>1
circulating currents; (9) measured vs corrected-model transients (velocity + load);
(10) mitigation on/off signature comparison.

Tables (4): (I) machine + published parameters; (II) FE calibration verification;
(III) validation matrix results (error metrics per condition); (IV) assumption
scorecard — A1–A4, error magnitude, when it matters, correction available.

Table IV is the paper's memorable artifact — reviewers and readers cite scorecards.

## 6. Experiment matrix

| Axis | Values | Source |
|---|---|---|
| Severity r/25 | 3, 6, 10 (15233529); 3, 6, 9 (21717722) | data |
| R_FIU | 442, 47.0, 5.62, 1.74 mΩ (+14.4 mΩ wire) | data |
| Speed | 1200–1900 rad/s elec. | data |
| Load | 1–3 Nm (0.5–1.5 Nm in 21717722) | data |
| Regime | steady / velocity transient / load transient | data |
| Mitigation | off / on | 21717722 |
| FE sweeps | turn position × severity × load; np ∈ {1, 2, 3, 6} × Rc | FEA (new) |

## 7. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Lamination geometry unpublished | Representative calibrated model + geometric sensitivity study (Sec. III); frame claims as mechanism + bound, not exact replication |
| FE effects turn out negligible (A1/A2 errors < measurement noise) | Still publishable: "lumped models validated from the design side" is a useful negative result, and C4 (np>1) is independent of it |
| Brno group as reviewers | Paper calibrates and extends their model, cites both TIE papers and both datasets — adversarial only to assumptions, not to authors |
| 21717722 companion (mitigation) paper not yet indexed — unknown claims | Read the PDF reports inside the dataset zip before writing Sec. VII; keep 21717722 to validation role only |
| Under-review TIA paper overlap | Different dataset, different machine, different question (model validation vs whatever it covers) — confirm no method overlap once topic is final |

## 8. Verification checklist (before writing)

1. ~~Download 15233529; inspect contents.~~ **Done 18 Aug 2026:**
   - Models (MATLAB R2024b, all native blocks, no S-functions, no protection):
     `models_comparison.slx` (continuous + derived DTM + forward Euler side by side,
     fault subsystems cleanly isolated: Fault inductances Lf1/Lf2, Fault resistance,
     Fault PM flux, ISC in phase a, mechanics on/off; 2 359 blocks / 110 subsystems);
     `codegen_mod_new.slx` and `codegen_mod_eul.slx` (single-precision, for codegen).
   - Data: 7 recordings (~24 MB each). `Data_diverse_FI/`: Rsc sweeps
     {442, 47.0, 5.62, 1.74} mΩ at 1900 rad/s for {3,6} turns × {1,3} Nm.
     `Data_diverse_OC/`: steady state (1400 rad/s, 1 Nm), velocity transient
     (1200→1600 rad/s), load transient (1→3 Nm), all at 10/25 turns.
   - **Key finding:** every .mat contains measured signals AND both DTM predictions
     time-aligned (idq/if/Te × meas/new/eul + udq, we, SinCos, Rsc, sgm). Residuals
     i_f,meas − i_f,new are computable immediately — the conference paper's evidence
     base exists before any FEA runs. Conference logic: (1) quantify residuals over the
     2×2×4 grid; (2) explain with FEA (effective severity); (3) inject corrected
     parameters into their own model and show the residual shrink.
   - Caveats: MATLAB ≥ R2024b to open models; .mat are MATLAB timeseries objects
     (MCOS) — one ~10-line MATLAB export script to plain arrays enables all further
     processing in Python; FI sweeps are single-speed (1900 rad/s) — speed dependence
     only via the three OC files at 10/25 turns, so no broad speed-robustness claims
     in the conference paper.
   - Still to do: download and inspect 21717722 (601 MB, mitigation datasets).
2. Read the PDF reports in 21717722; establish the mitigation paper's claims.
3. Confirm FE tooling and license at LUT (2-D transient with external circuit coupling
   is sufficient; turn-level winding needs circuit-coupled conductors).
4. Email EPEi chairs: late submission + TIA invitation process (still the gating item).

## 9. Timeline against EPEi dates

| When | What |
|---|---|
| Now → +1 wk | Chairs' answer; data download + inspection; FE model geometry + calibration started |
| +1 → +3 wk | Calibrated FE model; first x_f,eff results (conference core) |
| By 31 Aug | EPEi paper submitted (if chairs accept late) |
| Sep–Oct | Journal-only work: saturation study, np>1 model, full validation matrix |
| 22–24 Oct | Present at EPEi (early registration by 7 Oct) |
| Nov (if invited) | Assemble journal manuscript — most content exists by then; ~4 wk window |

## 10. EPEi conference carve-out (4–6 pp)

**Working title:** *Effective Fault Severity in Lumped Interturn Short-Circuit Models
of PMSMs: A Finite-Element Assessment on an Open Benchmark*

Contains: C1 + C2 + steady-state slice of C5.
- I. Introduction (compressed)
- II. Lumped ISC model and assumption A1
- III. FE model and calibration (verification table)
- IV. Effective severity results (Figs. 4–5 equivalents)
- V. Steady-state validation vs 15233529 (3 severities × 4 Rsc, one speed/load pair)
- VI. Conclusion + outlook naming the journal axes (saturation, transients, np>1)

Held back for the journal (≥60% new): saturation study (C3), np>1 extension (C4),
all transients, mitigation dataset, bias-correction framework, sensitivity analysis.
The outlook paragraph deliberately plants the extension so the invitation reads natural.

Mandatory: IEEE conference template; generative-AI disclosure statement; cite both
Zenodo DOIs and both TIE papers.
