# Revision and resubmission plan

## First: do not appeal

IEEE PES journals accept appeals, but they succeed essentially only when a reviewer made a
demonstrable factual error that drove the decision. Here:

- R3's claim that Table III is uncited **is** factually wrong — but R3 recommended
  acceptance, so it did not drive the rejection.
- R1's Fig. 6 question looks like a reviewer error, but it is not: the table genuinely
  switches denominators mid-column (`02_root_cause.md`, Problem 4). That is on the
  manuscript.
- The editor's three grounds (novelty, validation breadth, reproducibility) are each
  independently defensible.

An appeal would cost two months and almost certainly fail. Revise and resubmit.

## Second: the binding constraint

You do not have physical access to the test bench. The machine is at UFSC/LABMAQ in
Brazil; you worked from the CC BY 4.0 public dataset. The editor asked for "substantial
additional experimental work," and the two reviewer requests that most directly drive E2 —
sub-20 % faults (R2-7) and other loading levels (R2-8) — **cannot be satisfied from the
released data at all**, because the release contains only P15–P21, all at 7.0 kVA, with a
finest tap of 20 % of one pole.

So there are exactly three ways forward, and the choice determines everything else.

---

## Option A — Collaborate with the dataset authors *(recommended)*

Contact the UFSC/GRUCAD group (Krüger, Nascimento, Antunes, Batistela, Sadowski, Freitas).
R2 explicitly recommended this, so it also discharges R2-5.

**What it unlocks:**
- **Per-operating-point field current** — the single highest-value missing quantity, and
  the thing that converts your physics from asserted to measured (`02_root_cause.md`,
  Problem 2).
- Bench and sensor photographs, tap-switching schematic, and the reason for the P15
  numbering (R2-4, R2-6, R3-4).
- Possibly new measurements: finer taps and other loading levels (R2-7, R2-8, E2).

**Cost:** an email now; weeks to months if new measurements follow. **Risk:** they may
decline or be slow, and new measurements are on their schedule, not yours.
**Do this today regardless of which option you ultimately take** — the field-current data
alone is worth the email, and it is the long-pole item.

## Option B — Extend by finite-element modelling

Build a 2D FEM model of the 8-pole salient-pole machine, validate it against the 28
measured conditions, then use it to generate what the measurements cannot: sub-20 % faults
(5 %, 10 %), other loading levels, and other fault locations.

**Strengths:** entirely under your control; standard and well-received practice in TEC/TIE
(your own reference [4] does exactly this); directly answers R2-7, R2-8 and E2; lets you
test Eq. (4) across a continuous (γ, `I_f`) grid rather than four discrete severities.
**Cost:** 2–4 months including validation. **Risk:** reviewers discount simulation-only
severity claims unless the FEM is convincingly validated against the measured data — so
the validation step is mandatory, not optional.

**Option A + B together is the strongest combination**, and is what I would pursue.

## Option C — Split into two papers, as Reviewer 1 suggested

R1 wrote that the measurement and signal-processing methodology "could, in itself,
constitute a separate publication." That is a real offer, not a brush-off.

- **Paper 1 — measurement and physics-informed feature extraction.** The descriptor
  families with full derivations, literature attribution, worked numeric examples, and
  per-operating-point sensitivity. Natural home: *IEEE Trans. Instrumentation and
  Measurement*, or *IEEE Sensors Journal*.
- **Paper 2 — cross-operating-point generalisation.** The hardened benchmark, the
  validated Eq. (4), the confounding index, the severity calibration. Natural home:
  *IEEE TEC* (new submission), *IEEE TIE*, or *IEEE TIA*.

**Strength:** each paper gets enough room to be complete, which is the core of R1's
reproducibility objection. **Risk:** Paper 1 on its own may read as incremental unless the
physical validation (Problem 2) goes into it. **Cost:** low extra work, mostly
reorganisation — but two review cycles.

---

## Venue

If you rework substantially, **IEEE TEC as a new submission** is legitimate (declare the
prior submission and summarise the changes in the cover letter) — but only if Problems 1–3
are genuinely resolved; the editor has already seen this work.

Alternatives, all of which publish stray-flux diagnosis routinely and appear in your own
reference list:

| Venue | Fit |
|---|---|
| IEEE Trans. Industrial Electronics | Strong — refs [4], [12], [13] are TIE; welcomes diagnosis + ML |
| IEEE Trans. Industry Applications | Strong — ref [6], [14]; tolerant of applied benchmark work |
| IEEE Trans. Instrumentation and Measurement | Best fit for the Option C Paper 1 (ref [17] is TIM) |
| IET Electric Power Applications | Reasonable fallback, faster |
| IEEE Sensors Journal | Fits a sensing/feature-extraction framing |

Do **not** downgrade to a low-bar venue before fixing Problem 1 — the saturation objection
will follow the paper anywhere it is reviewed competently.

---

## Work packages

Ordered by dependency, not by size.

### WP0 — Send the email (day 1, blocks WP3)
Request from the UFSC group: field current and terminal quantities per operating point;
permission and source files for bench/sensor figures; tap-switching schematic; the P15
numbering rationale; and whether finer taps or other loading levels exist or could be
measured. Offer co-authorship or a formal collaboration.

### WP1 — Presentation fixes (1–2 days, independent)
All of R3; plus R1-5, R1-6, R1-8, R1-9, R2-4, R2-6. Specifically:
- Rebuild Table IV and Fig. 6 on a single denominator, reporting error rate and per-seed
  mean ± std (`tools/error_rate_check.py`).
- Rebuild Fig. 7 on a per-seed basis (36 seed-level P18 errors = 12 per seed).
- Cite Figs. 1–3 in text, in order; define `#`, `ρ`, `Bal.`, `n`, `Err.`; expand CH1/CH2
  and MAE at first use; fix "magnitude of the external magnetic field."
- Add the fold-composition table and the per-OP × per-severity file-count table.

### WP2 — Reproducibility package (1–2 weeks, independent)
Answers E3, R1-3, R1-4, R1-7, R3-5 — and R1-4 alone is sufficient grounds for rejection at
a Transactions, so this is not optional.
- Public repository: feature extraction → training → LOOPO evaluation → figures, with
  pinned environment, fixed seeds, and a one-command reproduction of every table.
- Full CNN architecture and hyperparameter table; window length, overlap, per-channel
  normalisation, optimiser, schedule, batch size, epochs, β, early stopping.
- One fully worked numeric example: one file → windows → features → prediction.
- Computational cost table (R2-2): extraction, training, inference, model size, memory.

### WP3 — Physical validation *(the core contribution; needs WP0)*
Per `02_root_cause.md`, Problem 2:
- Obtain or estimate `I_f` per operating point.
- Fit measured `A(k·f_m)` against `γ·I_f` over all 28 cells; report R².
- Quantify the normalisation as a between-OP variance-reduction factor at fixed γ.
- Derive the **excitation–severity confounding index**, compute it per operating point
  *before* classification, and show it predicts the measured difficulty ranking.

### WP4 — Hardened benchmark (2–4 weeks, independent)
Per `02_root_cause.md`, Problem 1:
- Source-operating-point sweep, *k* = 1…6, as the new headline experiment.
- Record-length and sampling-rate sweep (doubles as R2-2's time-to-diagnosis).
- Sensor gain/misplacement/noise perturbation tests.
- Per-cell results for all 28 conditions; confidence intervals by resampling **conditions**.
- New headline metric: minimum number of source operating points for 95 % macro-F1.

### WP5 — Generalise the severity calibration (1 week, after WP4)
Apply ordinal severity calibration to RF, ExtraTrees, LR and SVM as well as the CNN. Report
the result honestly either way — general method, or a patch for the CNN that should be
demoted.

### WP6 — Extend the condition space (months; Option A and/or B)
Sub-20 % severities and non-7.0 kVA loading, by new measurements or validated FEM.
This is what E2's "general applicability" ultimately requires.

### WP7 — Rewrite and resubmit
Reframe the abstract and contributions around WP3; demote the benchmark to supporting
evidence; drop "does not support a simple deep-learning-superiority conclusion"; narrow
every claim to the conditions actually tested.

---

## Sequencing

| Phase | Work | Elapsed |
|---|---|---|
| 1 | WP0 (email) + WP1 (presentation) | Week 1 |
| 2 | WP2 (reproducibility) + WP4 (hardened benchmark), in parallel | Weeks 2–6 |
| 3 | WP3 (physical validation), once WP0 returns | Weeks 4–8 |
| 4 | WP5 (calibration generalisation) | Weeks 8–9 |
| 5 | WP6 (FEM and/or new measurements) | Months 3–6 |
| 6 | WP7 (rewrite, resubmit) | Months 6–7 |

**Realistic horizon: 4 months for a strong TIE/TIA submission without new measurements
(WP0–WP5, WP7); 6–8 months for a TEC-grade resubmission including WP6.**

## Go/no-go checkpoints

1. **After WP4.** If methods still tie at *k* = 1–2 source operating points, the dataset
   genuinely has no resolving power and the benchmark framing must be abandoned entirely —
   go all-in on the physical result (WP3) and Option C, Paper 1.
2. **After WP3.** If Eq. (4) does *not* fit the measured `A(k·f_m)` vs. `γ·I_f`, that is
   itself a publishable negative finding — but the title must stop claiming
   "physics-informed," and the first-order model needs revisiting (saturation,
   armature reaction, AVR dynamics are the obvious candidates, all currently neglected).
3. **After WP0.** If the UFSC group cannot supply field currents and you cannot estimate
   them credibly, Problem 2 is unresolvable on measured data and Option B (FEM) becomes
   mandatory rather than optional.
