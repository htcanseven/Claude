# Low-effort route: EPSR first, IEEE Access as fallback — with drop-in text

## The decision

**Primary: Electric Power Systems Research (Elsevier).** *Revised recommendation — see below.*
IF 5.56, Q1, CiteScore 6.6. Hybrid, so publishing costs nothing (subscription route free; OA
covered by the FinELib Elsevier agreement through Dec 2026). Typically **~1.7 revision rounds**,
~2.7 review reports, ~3.4 months total handling.

**Fallback: IEEE Access.** APC $2,160 (2026), **funded for LUT via FinELib**. First decision in
~30 days. Reviewers assess technical soundness and clarity — articles are *not* expected to show
high novelty, only to be distinct from prior work and technically sound. That is exactly the
objection that sank you at TEC, and Access does not apply it the same way.

**Second fallback: e-Prime (Elsevier).** APC $1,400 and **currently waived**. Scope is a
near-perfect match (power generation, signal processing, AI, sensors). Rapid review. No impact
factor yet, so it counts for less on a CV, but it costs nothing.

**Avoid Heliyon.** It retracted roughly **392 papers in 2025** (up from 26 in 2024) amid
paper-mill cleanup. Not somewhere a post-doc wants a publication on record.

---

## Why EPSR before IEEE Access

The deciding factor is not impact factor — it is the **decision model**, and it interacts
directly with this paper's specific weaknesses.

| | EPSR | IEEE Access |
|---|---|---|
| Impact factor | **5.56** (Q1) | ~3.4 |
| Revision rounds | **~1.7 typical** | **Binary: accept or reject** |
| Cost to you | **Free** (hybrid, or FinELib OA) | $2,160, FinELib-funded |
| Time to decision | ~2.7 months first round | ~30 days |
| Novelty assessed | Yes, normally | Not heavily |
| Scope risk | **Real — needs reframing** | Low |

This paper's known problems — the Table IV denominators, thin reproducibility documentation —
are **fixable**. A journal with revision rounds is strictly better for fixable problems. IEEE
Access's binary model is built for manuscripts that are already clean; if a reviewer there hits
either issue, it is a reject with no recovery, and the venue is spent.

At EPSR the same issues produce a major revision, you fix them, and the paper lands in a journal
with a meaningfully better impact factor for no money.

**Sequencing matters and only works one way.** If EPSR rejects, IEEE Access is still open — and
you would arrive there with EPSR's reviewer comments already addressed, making it a stronger
submission. The reverse does not work: an Access rejection wastes the better option, and you
cannot fall upward.

You also have something no aggregator can give: **you have reviewed for EPSR and seen a similar
paper go through.** That is better calibration of the real bar than anything in this document.

---

## ⚠️ The one genuine risk at EPSR: scope

EPSR's official scope statement is unusually explicit, and it cuts close:

> "The scope of Electric Power Systems Research is broad, yet the submission contents should be
> directly related to **the influence on power system operation rather than presenting the issues
> of particular network elements only**. Furthermore, submissions focusing primarily on
> electricity prices, market economics, or **isolated components without demonstrating a
> technical impact on the broader power system fall outside the journal's scope**."

As currently framed — diagnosing a fault in a 10 kVA laboratory machine — the paper reads as
exactly the "isolated component" case. And the 9-day median to first decision indicates an active
desk-screening step, which is where a scope mismatch gets caught.

**The fix costs nothing and is honest, not spin.** Your paper is genuinely about power system
operation, and the current framing hides it:

1. **Reactive power dispatch is set by the grid, not the machine.** The reason the operating
   point varies across P15–P21 at all is that system voltage-support requirements and grid codes
   dictate the generator's reactive set point. Cross-operating-point robustness is therefore a
   *power system operation* requirement, not a laboratory curiosity. This is the single strongest
   scope argument available and it is already implicit in Section III — make it explicit in the
   Introduction.
2. **Rotor ITSC drives unplanned generator outages**, which affect system adequacy, reserve
   margins and reliability. Early severity-aware detection lets operators schedule maintenance
   rather than trip unexpectedly.
3. **Frame the boundary-condition finding in operational terms**: the under-excited,
   low-power-factor condition is a normal grid-dictated operating state (absorbing reactive power
   for voltage control), and it is precisely where naive diagnosis fails. That is an operationally
   relevant result, not a lab artifact.

Rewrite the first two Introduction paragraphs around points 1–3, add one sentence to the abstract
about generation availability, and the scope objection disappears. Roughly an hour's work.

### Also worth knowing

EPSR reviewers *do* assess novelty, unlike Access. The novelty objection that sank you at TEC is
still live there. The difference is that at EPSR you get a revision round to argue it, and the
reframing above (diagnosis under grid-dictated reactive dispatch) is a more defensible position
than "a benchmark of known features." Present it as an operational-robustness study, not a
method comparison.

---

## ⚠️ The one thing that changes the work estimate

**IEEE Access uses a binary decision model.** Reviewers recommend *Accept* (minor edits only) or
*Reject*. There is **no major-revision round**. You get one shot.

Overall acceptance is around 27 %, and the most common rejection reasons are **weak validation
or reproducibility** and technical incorrectness — not novelty.

This matters directly: R1 already wrote that the paper *"does not provide all the information
necessary to reproduce and independently verify the reported results,"* and already found
Table IV self-contradictory. If an Access reviewer hits either of those, it is a reject with no
second chance. So the minimal fix list below is not optional polish — it is the difference
between accept and reject.

**Realistic effort: about one week.** Almost all of it mechanical.

---

## Mandatory minimal fix list

### 1. Fix the Table IV / Fig. 6 denominators *(1 hour — highest priority)*

Non-negotiable. Replace Table IV with a single-denominator version:

```latex
\begin{table}[t]
\caption{Strong classical and raw deep benchmark under LOOPO. All results are
expressed per 607 voltage-vector files; CNN rows are means over three seeds.}
\label{tab:benchmark}
\centering
\begin{tabular}{llcccc}
\hline
Model & Representation & Err. & Err. rate & Macro-F1 & MAE \\
\hline
ET      & All numeric            & 3    & 0.49\% & 0.9951 & 0.0010 \\
SVM     & Norm. spectral profile & 4    & 0.66\% & 0.9935 & 0.0015 \\
LR-L2   & Band-energy ratios     & 4    & 0.66\% & 0.9935 & 0.0013 \\
SC-CNN  & Raw + severity calib.  & 4.0  & 0.66\% & 0.9935 & 0.0013 \\
Raw-CNN & Raw majority voting    & 16.0 & 2.64\% & 0.9737 & 0.0053 \\
RF      & Cross-channel ratios   & 22   & 3.62\% & 0.9632 & 0.0157 \\
\hline
\end{tabular}
\end{table}
```

Notes:
- `Err.` for CNN rows = pooled seed errors ÷ 3 (48 → 16.0, 12 → 4.0). Add `± std` from your own
  per-seed results if you have them; if not, the mean alone is fine as long as the caption says so.
- Define every column: `Err.` = misclassified files, `MAE` = severity mean absolute error.
- **Regenerate Fig. 6 with error *rates* on the bars, not raw counts.**
- **Fig. 7 (P18 confusion matrices): report per seed, not pooled** — 36 seed-level errors is
  12 per seed. Say so in the caption.
- Everywhere in the text, "48 seed-level file errors" → "an error rate of 2.64 % (16 of 607
  files per seed, pooled over three seeds)".

Verify with `python3 tools/error_rate_check.py`.

### 2. Add the reproducibility material *(2–3 days)*

Access rejects for weak reproducibility. Add a subsection or appendix containing:

**(a) Dataset composition table** — this is free, the numbers are in `05_dataset_reference.md`:

```latex
\begin{table}[t]
\caption{Composition of the evaluated dataset. All 607 released voltage-vector
files of [11] are used; each file contains 10 s of two-channel data at 125 kHz.}
\centering
\begin{tabular}{lccccc}
\hline
OP & Power factor & Excitation & Files \\
\hline
P15 & 1.0 & Unity          & 95 \\
P16 & 0.8 & Under-excited  & 84 \\
P17 & 0.5 & Under-excited  & 80 \\
P18 & 0.3 & Under-excited  & 90 \\
P19 & 0.8 & Over-excited   & 90 \\
P20 & 0.5 & Over-excited   & 84 \\
P21 & 0.3 & Over-excited   & 84 \\
\hline
\multicolumn{3}{l}{Total} & 607 \\
\hline
\end{tabular}
\end{table}
```

Add a per-severity breakdown column if you can extract it (the source data report's Table 5 maps
vector numbers to fault condition — e.g. P15: 1–20 healthy, 21–47 at 20 %, 48–77 at 50 %,
78–95 at 100 %).

**(b) CNN specification table** — window length, overlap, per-channel normalisation, the
layer-by-layer architecture, optimiser, learning-rate schedule, batch size, epochs, the severity
weight β of Eq. (11), early-stopping rule, and the three seed values.

**(c) Classical model table** — per model: input representation, dimension, scaling,
hyperparameter grid, selection criterion.

**(d) LOOPO fold composition** — train/test file counts per fold (e.g. holding out P18 leaves
517 training files), and one explicit sentence that both channels of a file always stay in the
same fold and that the held-out operating point is excluded from scaling, hyperparameter search
and threshold selection.

**(e) A code repository link.** This single item does more than anything else to neutralise the
reproducibility objection, and the dataset is already public under CC BY 4.0. Even a tidy
GitHub repo with the extraction and evaluation scripts is enough.

### 3. Editorial fixes *(1 day — all of Reviewer 3)*

- Define CH1/CH2 and MAE at first use, not later.
- Cite Figs. 1, 2, 3 in the text, in order.
- Define every table column: `#` = number of features, `ρ` = Spearman rank correlation with
  ordinal severity, `Bal.` = balanced accuracy, `n` = evaluated predictions, `Err.` = misclassified files.
- Replace "magnitude of the external magnetic field" with "RMS amplitude of the sensor-induced
  voltage, proportional by (1) to the time derivative of the tangential stray-field flux density."
- Move long footnotes into the body text.

### 4. Drop-in answers to the easy comments *(half a day)*

All facts verified — see `05_dataset_reference.md`. Paste these into Section III:

> The workbench carries two synchronous machines driven by a common 10 kW DC prime mover through
> an electromagnetic clutch: an 8-pole salient-pole generator (10 kVA, 750/900 rpm), which is the
> machine under test throughout this study, and a 2-pole cylindrical generator (10 kVA,
> 3000/3600 rpm), which is used for other investigations on the same bench and takes no part in
> the measurements analysed here.

> Controlled faults are imposed through terminals on a single pole of the field winding, which
> has 470 turns per pole and 3760 turns in total. Terminal J corresponds to the healthy winding,
> while J1, J2 and J3 short-circuit 94, 235 and 470 turns of that pole, corresponding to 20 %,
> 50 % and 100 % of the pole and to 2.5 %, 6.25 % and 12.5 % of the complete field winding. An
> automatic switching system changes between these states without shutting the generator down.

> The generator is synchronised to the local 60 Hz distribution network throughout, so the
> terminal voltage is imposed by the grid rather than regulated to be perfectly balanced and
> sinusoidal.

> The operating-point labels P15–P21 are adopted verbatim from the public dataset [11] so that
> every recording remains traceable to its source file; these seven points constitute the
> complete public release. All of them share an apparent power of 7.0 kVA, so the dataset spans
> the excitation and power-factor axis while holding the armature loading fixed.

And for the 90° question, in Section II or III:

> The 90° sensor spacing is a property of the public measurement campaign analysed here rather
> than a design choice of this study. It is nonetheless well matched to the fault considered: in
> an 8-pole machine, 90 mechanical degrees correspond to 360 electrical degrees, so the
> p-periodic healthy field produces nominally identical signatures at the two sensors, whereas a
> defect confined to a single pole is not p-periodic and breaks that equivalence. The
> cross-channel descriptors of (8) exploit this asymmetry directly. The 180° arrangement of [15]
> targets a different spatial symmetry for stator inter-turn faults on a different machine.

### 5. Soften the claims *(1 hour — costs nothing, removes risk)*

The current abstract advertises a null result and invites pushback. Rewrite the middle:

- **Delete**: *"Importantly, the benchmark does not support a simple deep-learning-superiority
  conclusion"* → replace with a factual statement of what was measured.
- **Delete** any wording implying general applicability. Add one explicit limitations paragraph:
  all seven operating points are at 7.0 kVA, the mildest available severity is 20 % of one pole
  (2.5 % of the field winding), and results are from a single 10 kVA laboratory machine.
- **Stop using "incipient"** for the 20 % condition.

A modest, carefully bounded paper passes Access. An over-claiming one gives a reviewer a reason
to reject, and there is no revision round to recover in.

---

## What you are explicitly skipping

Fine to skip on this route — just don't claim otherwise in the paper:

- WP3 physics validation (measured `I_f`, Eq. (4) verification, confounding index)
- WP4 hardened benchmark (source-OP sweep, record-length sweep, perturbations)
- WP5 severity calibration on classical models
- WP6 FEM / new measurements

**One consequence to accept knowingly:** with the physics unvalidated, "Physics-Informed" in the
title is doing work the paper does not support. Access reviewers are unlikely to press it, but
consider retitling to something defensible such as *"Physics-Motivated Feature Representations
for Cross-Operating-Point Diagnosis of Rotor Winding Inter-Turn Short Circuits in Synchronous
Generators."* One word, no extra work, and it removes the most obvious line of attack.

---

## Submission checklist

- [ ] Table IV and Fig. 6 on a single denominator; Fig. 7 per seed
- [ ] Dataset composition table (607 files, per-OP counts)
- [ ] CNN and classical model specification tables
- [ ] LOOPO fold composition stated explicitly
- [ ] Code repository published and linked
- [ ] All of Reviewer 3's editorial fixes
- [ ] Drop-in paragraphs for bench, taps, grid connection, P15–P21, 90° spacing
- [ ] Limitations paragraph added; "incipient" removed; abstract claim softened
- [ ] Title reconsidered
- [ ] **For EPSR: Introduction reframed around power system operation** (grid-dictated reactive
      dispatch, unplanned outage avoidance, generation availability)
- [ ] Confirm FinELib APC funding with the LUT library *before* submitting
- [ ] Cover letter stating scope fit and what the paper contributes

---

## Drop-in: revised abstract

Rewritten to state results factually, put the CNN numbers on a consistent basis, and drop the
null-result framing. Same length as the original.

> Reliable diagnosis of rotor winding inter-turn short circuits (ITSCs) in synchronous generators
> is challenging under operating-point variation, because changes in excitation and reactive
> power strongly affect stray magnetic field measurements. This paper presents a leakage-safe
> cross-operating-point evaluation of rotor winding short-circuit severity diagnosis using
> two-channel stray magnetic field signals from a 10 kVA salient-pole synchronous generator
> operated at seven excitation and power-factor conditions. Physics-motivated feature
> representations — normalized harmonic ratios, spectral profiles, band-energy ratios and
> cross-channel descriptors — are evaluated alongside classical learners and raw-signal 1D-CNN
> models under a leave-one-operating-point-out (LOOPO) protocol. Absolute magnitude-dependent
> features prove vulnerable to operating-point shift, reaching 0.803 macro-F1, whereas normalized
> representations reach 0.946 under the same classifier, consistent with the first-order
> cancellation of excitation-dependent amplitude scaling predicted by the underlying
> magnetomotive-force model. Across the full benchmark, ExtraTrees with all numeric descriptors
> attains 0.9951 macro-F1 (0.49 % file-level error rate), while SVM-RBF, ℓ2 logistic regression
> and a nested severity-calibrated 1D-CNN each attain 0.9935 (0.66 %), and raw 1D-CNN majority
> voting attains 0.9737 (2.64 %). A paired file-level McNemar test between the best classical
> model and the calibrated CNN detects no statistically significant difference at this error
> level. Under the under-excited low-power-factor P18 condition, where stray-field attenuation
> shifts low-severity decision boundaries, nested ordinal severity calibration recovers all raw
> CNN errors without degrading previously correct predictions. The results indicate that
> cross-operating-point robustness in stray-field rotor winding diagnosis is governed at least as
> much by feature normalization and leakage-safe evaluation as by model capacity, within the
> operating range examined.

Also update the index terms: replace "physics-informed features" with "physics-motivated
features" if you retitle.

---

## Drop-in: EPSR cover letter

The job of this letter is to clear the scope screen. Lead with power system relevance, not with
the method.

> Dear Editor,
>
> Please consider the enclosed manuscript, "«final title»," for publication in Electric Power
> Systems Research.
>
> Synchronous generators are the primary electromechanical conversion units in conventional
> generation, and rotor winding inter-turn short circuits are among the faults most likely to
> force an unplanned outage. Because such outages reduce generation availability and erode system
> reserve margins, reliable early detection of rotor winding degradation is a power system
> operation concern as much as a machine design one.
>
> The manuscript addresses a problem that arises specifically from system operation. A
> grid-connected generator's excitation and reactive power set point are dictated by system
> voltage-support requirements and grid code obligations, not by the machine itself, and the
> external stray magnetic field used for non-invasive diagnosis varies strongly with that set
> point. A diagnostic model validated at one reactive dispatch condition can therefore fail at
> another. We show that this is not hypothetical: under deeply under-excited operation — a normal
> state when a unit absorbs reactive power for voltage control — stray-field attenuation shifts
> classification boundaries so that mild rotor faults are misread as healthy.
>
> The paper contributes: (i) a leave-one-operating-point-out evaluation protocol that measures
> generalization to unseen excitation and power-factor conditions rather than to random splits;
> (ii) a comparison of stray-field feature representations under that protocol, quantifying how
> far fundamental-normalized descriptors reduce reactive-dispatch sensitivity; and (iii) an
> analysis of the under-excited boundary condition together with an ordinal severity-calibration
> stage that recovers the resulting failures.
>
> Results are obtained from an openly available measurement dataset (CC BY 4.0,
> DOI 10.17632/d75sb25f7m.1) covering seven excitation and power-factor conditions of a
> salient-pole synchronous generator synchronized to a 60 Hz distribution network. The complete
> analysis pipeline is released at «repository URL» so that all reported results can be
> independently reproduced. Limitations — a single 10 kVA machine at fixed apparent power — are
> stated explicitly.
>
> The manuscript is original, is not under consideration elsewhere, and all authors have approved
> the submission.
>
> Yours sincerely,
> Hüseyin Tayyer Canseven, Evin Şahin Sadık

---

## Drop-in: IEEE Access cover letter

Access editors use the cover letter to judge fit before reading the manuscript, so scope fit and
a clear statement of what the paper offers matter more than selling novelty.

> Dear Editor,
>
> Please consider the enclosed manuscript, "«final title»," for publication in IEEE Access.
>
> The manuscript addresses non-invasive diagnosis of rotor winding inter-turn short-circuit
> faults in salient-pole synchronous generators using external stray magnetic field measurements.
> Rotor winding faults are a leading cause of unplanned outages in power generation, and stray
> flux sensing is attractive because it requires no machine dismantling. The practical obstacle
> is that the measured stray field depends strongly on excitation state and reactive power, so
> diagnostic models validated on mixed operating points can substantially overstate field
> performance.
>
> The paper contributes: (i) a leakage-safe leave-one-operating-point-out evaluation protocol
> that tests generalization to unseen excitation and power-factor conditions rather than to
> random splits; (ii) a systematic comparison of eleven stray-field feature families under that
> protocol, quantifying how far fundamental-normalized descriptors reduce operating-point
> sensitivity relative to absolute-amplitude descriptors; (iii) a benchmark of four classical
> learners against raw-signal 1D-CNN models under identical conditions with paired statistical
> testing; and (iv) an analysis of the under-excited low-power-factor boundary condition, where
> an ordinal severity-calibration stage recovers the observed classification failures.
>
> All results are obtained from an openly available measurement dataset (CC BY 4.0,
> DOI 10.17632/d75sb25f7m.1), and the complete analysis pipeline is released at «repository URL»,
> so every reported table and figure can be independently regenerated from public sources.
>
> The work is bounded to a single 10 kVA laboratory machine at a fixed apparent power of 7.0 kVA,
> and these limitations are stated explicitly in the manuscript.
>
> The manuscript is original, is not under consideration elsewhere, and all authors have approved
> the submission.
>
> Yours sincerely,
> Hüseyin Tayyer Canseven, Evin Şahin Sadık
