# Draft point-by-point responses

Use these when you resubmit — either as the response document for a new IEEE TEC submission
(declaring the prior submission), or adapted for another venue's cover letter.

**Conventions used below**
- `«...»` marks text that depends on work not yet done — fill in after WP3/WP4, do not ship
  with placeholders.
- Responses are written to *concede where the reviewer is right*, which is both honest and
  the fastest route through a second round. Two places where a reviewer is factually
  mistaken (R1-9, R3-2b) are handled by fixing the underlying cause without disputing the
  reviewer.

---

## To the Editor

> Novelty and added value not sufficiently demonstrated; validation not comprehensive;
> methodological details insufficient for reproducibility.

We thank the Editor for a diagnosis we accept in full. On re-examination we concluded that
the original manuscript's framing — a comparative benchmark of classical and deep models —
could not support a novelty claim, for a reason internal to the experiment: with all
evaluated models between 0.963 and 0.995 macro-F1, and with only 28 physically distinct
conditions (7 operating points × 4 severity levels) underlying the 607 recordings, the
benchmark had insufficient resolving power to separate any two methods. Our own paired test
(p = 1.000 on a single discordant file) demonstrated this.

The revised manuscript is therefore restructured around a different and, we believe,
genuinely new contribution: **a first-order physical model of the confounding between
shorted-turn fraction γ and excitation current I_f in stray-field amplitude, validated
against measurement, and used to predict a priori which operating points cross-operating-point
diagnosis will fail at.** The benchmark is retained as supporting evidence rather than as
the headline result.

Concretely, since the original submission we have:
1. Obtained «per-operating-point field current» and verified the first-order scaling
   `A(k·f_m) ∝ γ·I_f` across all 28 measured conditions «R² = ...» (Section «...»).
2. Quantified the effect of fundamental normalisation as a between-operating-point variance
   reduction of «...×» at fixed severity, replacing the previously qualitative argument.
3. Introduced an excitation–severity confounding index computed from measured operating
   quantities alone, which ranks operating-point difficulty «before» any classifier is
   trained and correctly identifies P18 as the boundary case.
4. Replaced the fixed six-source-operating-point protocol with a sweep over the number of
   source operating points (k = 1…6), which restores resolving power: methods that are
   indistinguishable at k = 6 differ by «...» macro-F1 at k = 2.
5. Added record-length, sampling-rate and sensor-perturbation sweeps, and computational-cost
   measurements.
6. Released the complete analysis code and a full specification of preprocessing,
   architectures and hyperparameters, so that every table and figure can be regenerated
   from the public CC BY 4.0 dataset with one command.

---

## To Reviewer 1

### R1-1 — Results show no significant novelty over prior publications

Accepted; see our response to the Editor. The comparative benchmark has been demoted from
the paper's contribution to supporting evidence, and the contribution is now the validated
physical model of γ–I_f confounding and the resulting predictive difficulty criterion,
which to our knowledge has not been reported for stray-field diagnosis of salient-pole
synchronous generators.

### R1-2 — The measurement and signal-processing methodology deserves fuller treatment

We agree, and we have acted on the suggestion in two ways. Within this manuscript,
Section «...» now gives, for each descriptor family, the defining expression, its
attribution to the literature «refs», a fully worked numeric example computed from a named
file in the public dataset, and its measured variation across all seven operating points
(Fig. «...»). We have additionally followed the Reviewer's suggestion that this material
could support a separate publication «— a companion paper devoted to the measurement chain
and descriptor construction is in preparation / has been submitted to ... ».

### R1-3 — More detail on each method: input type, preprocessing, representation

Added as Table «...», which specifies for every model the input representation (file-level
feature vector vs. raw two-channel window), its dimension, the scaling applied, the
hyperparameter grid, and the selection criterion. The CNN is now fully specified — window
length and overlap, per-channel normalisation, layer-by-layer architecture, optimiser,
learning-rate schedule, batch size, epoch budget, the severity-loss weight β of Eq. (11),
early-stopping rule, and the three random seeds.

### R1-4 — The paper does not permit independent reproduction

We accept this as stated. The complete analysis pipeline — feature extraction, training,
LOOPO evaluation, statistical tests and figure generation — is now publicly available at
«repository URL», with a pinned environment and fixed seeds. Since the underlying dataset
is openly available under CC BY 4.0 (DOI 10.17632/d75sb25f7m.1), every reported number can
be regenerated from public sources.

### R1-5 — How LOOPO is applied to the two-sensor signals

Clarified in Section «...». Descriptors are computed independently for CH1 and CH2 and
concatenated into a single file-level vector, so both channels of a recording always remain
in the same fold; no recording is split across folds. In each outer fold the entire
held-out operating point — both channels, all severity levels — is excluded from feature
scaling, hyperparameter search, model selection and threshold calibration. For the CNN
branch, train/validation separation is performed at file level within the source operating
points so that windows from one recording cannot appear on both sides. Table «...» now
gives the exact composition of all seven folds.

### R1-6 — Rationale for 90° rather than the 180° of [15]

The 90° spacing is a property of the public measurement campaign we analyse, not a design
choice of this study; we have made that explicit. The configuration is nonetheless
well-suited to the fault considered, and Section II now states the reason directly: in an
8-pole machine a 90° mechanical separation corresponds to 360° electrical, so the p-periodic
healthy field produces nominally identical signatures at the two sensors, while a defect on
a single pole is not p-periodic and therefore breaks that equivalence. The inter-channel
descriptors of Eq. (8) exploit exactly this asymmetry. Reference [15] addresses *stator*
inter-turn faults on a different machine, where a 180° arrangement targets a different
spatial symmetry; we now discuss this distinction explicitly.

### R1-7 — Insufficient detail on the signals used for training

Section «...» and Table «...» now report: 607 two-channel recordings in total, each 10 s
sampled at 125 kHz; the number of recordings per operating point (P15: 95, P16: 84, P17: 80,
P18: 90, P19: 90, P20: 84, P21: 84) and per severity level within each operating point; the
resulting window counts after segmentation; and the class imbalance this produces. The
threshold-selection procedure is now given in full: t01 = 0.10 and t12 = 0.35 are fixed at
the physical midpoints of the severity levels {0.0, 0.2, 0.5, 1.0}, while t23 is selected
per outer fold over the candidate grid «...» using only source operating points, yielding
t23 = 0.675 in all seven folds, with the sensitivity analysis over t23 ∈ [0.55, 0.80]
reported in Fig. «...».

### R1-8 — More thorough discussion of the tables

Expanded throughout. In particular, the large gap in Table II between raw harmonic
amplitudes (0.803 macro-F1) and normalised spectral profiles (0.946) is now interpreted
through Eq. (5): absolute amplitudes carry the excitation-dependent factor I_f, which
changes between operating points and is therefore an unreliable cue under LOOPO, whereas
the fundamental-normalised ratios cancel that factor to first order. This is the
quantitative confirmation of the physical argument of Section II, and it was previously
left implicit.

### R1-9 — Figure 6: error counts inconsistent with macro-F1

We thank the Reviewer for this observation, which identified a genuine defect in our
presentation. The underlying values were correct but the table and figure mixed two
different denominators: results for the classical models were reported over the 607
recordings, whereas CNN results were pooled over three random seeds (n = 1821 = 607 × 3).
On a common basis, 48/1821 = 2.64 % is a *lower* error rate than 22/607 = 3.62 %, which is
why the CNN attains the higher macro-F1; and 12/1821 and 4/607 are both exactly 0.659 %,
which is why those two models share macro-F1 = 0.9935.

We have removed the ambiguity rather than merely explaining it. Table «...» and Fig. «...»
now report **error rate** as the primary quantity, with all CNN results expressed on the
607-recording basis as a mean ± standard deviation over the three seeds. Fig. «...» (the
P18 confusion matrices) is likewise reported per seed rather than pooled. We regret the
confusion the original presentation caused.

---

## To Reviewer 2

### R2-1 — Novelty unclear; the features are known and not new

We accept this. The descriptor families are indeed established, and we no longer claim them
as a contribution; Section «...» now attributes each to prior work. The contribution has
been moved to the physical level — see our response to the Editor.

### R2-2 — Report computational demand and time to diagnosis

Added as Table «...»: feature-extraction time per 10 s recording, training time, inference
time per recording, parameter count and peak memory, all on stated hardware. Following the
Reviewer's point that time-to-diagnosis matters operationally, we went further and swept the
*observation length* required to reach a target accuracy: «...» — diagnosis at «...»
macro-F1 requires «...» of signal rather than the full 10 s record. We are grateful for this
suggestion, which produced one of the more practically useful results in the revision.

### R2-3 — "Physics-informed beats raw data" is already known

Agreed, and the claim has been removed from the abstract and conclusions. We now treat the
comparison as a control rather than a finding.

### R2-4 — Show the tap connections and photographs of the mounted sensors

Added. Fig. «...» now shows the field-winding tap arrangement explicitly: terminals J
(healthy), J1, J2 and J3 on a single pole, short-circuiting 0, 94, 235 and 470 of that
pole's 470 turns respectively, together with the automatic switching element that allows the
condition to be changed without shutting the generator down. Fig. «...» shows the induction
sensor and its mounting on the generator casing, reproduced from the data report [11] under
its CC BY 4.0 licence with attribution «and with the authors' agreement».

### R2-5 — Contact the authors of [11]

We have done so. «Summarise the outcome: data provided, figures authorised, collaboration
or acknowledgement established.» Their assistance is acknowledged in «...», and the
per-operating-point excitation data they provided underpins the validation of Eq. (4) in
Section «...».

### R2-6 — Why are there two generators in Fig. 1?

The workbench carries two synchronous machines driven by a common 10 kW DC prime mover
through an electromagnetic clutch: an 8-pole salient-pole generator (10 kVA, 750/900 rpm),
which is the machine under test throughout this study, and a 2-pole cylindrical generator
(10 kVA, 3000/3600 rpm), which is used for other investigations on the same bench and takes
no part in the measurements analysed here. The caption and Section III now state this, and
the machine not under test is de-emphasised in the figure.

### R2-7 — Sensitivity to incipient faults; 20 % of one coil is not incipient

The Reviewer is right and we have corrected the terminology throughout: the mildest
available condition is no longer described as incipient. We have also restated it in the
more meaningful terms the Reviewer's comment implies — 20 % of one pole is 94 of the
machine's 3760 rotor turns, i.e. **2.5 % of the total field winding**, and by Eq. (4) it
perturbs the electrical fundamental by only γ/2p ≈ 1.25 %. Section «...» now reports the
detection margin at this severity in normalised-ratio units, so that sensitivity to milder
faults can be extrapolated rather than assumed.

We note frankly that the finest tap in the public dataset is 20 % of one pole, so genuinely
incipient severities cannot be studied from these measurements. «We have therefore extended
the analysis with a finite-element model of the same machine, validated against the 28
measured conditions, and used it to examine 5 % and 10 % severities (Section ...).» / «We
identify this as the principal limitation of the present study and the subject of ongoing
measurements with the group of [11].»

### R2-8 — All conditions share the same stator MMF; clarify the grid connection

On the second point: the generator is synchronised to the local 60 Hz distribution network
throughout, so the terminal voltage is imposed by the grid and is not regulated to be
perfectly balanced or sinusoidal. Section III now states this explicitly and reports the
measured background unbalance and distortion «...», which the original manuscript left
uncharacterised.

On the first point, the Reviewer is correct and we now state it as an explicit limitation:
all seven released operating points are at 7.0 kVA, so the campaign explores the reactive
axis while holding the armature MMF essentially fixed, and no claim about behaviour under
varying load can be supported by these data alone. «We have addressed this by ... » /
«We have narrowed the claims of the paper accordingly and identify load variation as the
primary direction for further work.»

---

## To Reviewer 3

We thank the Reviewer for the recommendation and for a precise list of corrections, all of
which have been made.

**1. Abbreviations before definition.** CH1 and CH2 are now introduced at first occurrence
in Section II rather than in Section III, and "mean absolute error (MAE)" is expanded at its
first appearance, which now precedes both Table II and Section IV-D.

**2. Figure and table ordering.**
(a) Figs. 1, 2 and 3 are now cited in the text, in order, at the points where the bench,
the tap arrangement and the sensor placement are first discussed.
(b) The discussion of Table III has been substantially expanded in Section «...», and the
table has been repositioned adjacent to that discussion; the forward reference from
Section II has been reworded so that the table is introduced where it is interpreted.
(c) Long explanatory footnotes have been moved into the body text, and every column is now
defined in the header or caption: `#` is the number of features in the family, ρ is the
Spearman rank correlation with ordinal severity, `Bal.` is balanced accuracy, `n` is the
number of evaluated predictions, and `Err.` is the number of misclassified recordings.

**3. "Magnitude of the external magnetic field."** Replaced with the specific quantity
throughout — the RMS amplitude of the sensor-induced voltage, which by Eq. (1) is
proportional to the time derivative of the tangential component of the stray-field flux
density. Other loose uses of "magnitude" and "field" have been made specific.

**4. The P15–P21 notation.** These labels are inherited verbatim from the public dataset
[11] so that every recording remains traceable to its source file. The released dataset
contains only these seven operating points; the numbering originates in the measurement
campaign of [11] and earlier points are not part of the public release. Section III now
explains this and states the consequence the Reviewer's question implies — that all seven
operating points share an apparent power of 7.0 kVA, so the released data spans the
excitation axis but not the loading axis.

**5. A developed worked example.** Added. Section «...» follows a single named recording
from the public dataset end to end: segmentation into windows, per-channel normalisation,
computation of each descriptor family with numeric values, window-level CNN outputs,
majority voting, severity averaging, threshold comparison and the final decision. Rather
than a code fragment in the paper, the complete implementation is released at «repository
URL» so that the entire pipeline can be inspected and re-run.
