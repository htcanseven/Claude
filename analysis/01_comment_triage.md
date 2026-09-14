# Comment-by-comment triage

All 25 distinct comments, each with a verdict, the concrete fix, and effort.

**Verdict key:** ✅ valid — accept and fix · ⚠️ partly valid — underlying concern is fair
even where the literal claim is off · ❌ factually incorrect — but handle diplomatically ·
🔴 fatal — cannot be fixed by editing, needs new work

**Effort key:** S = hours · M = days · L = weeks · XL = months / new experiments

---

## Editor

| # | Comment | Verdict | Fix | Effort |
|---|---|---|---|---|
| E1 | Novelty and added value not demonstrated vs. existing fault-diagnosis methods | 🔴 valid | Reframe around the physical confounding result; see `02_root_cause.md` Problems 1–3 | XL |
| E2 | Experimental validation not comprehensive enough to support claimed performance and general applicability | 🔴 valid | Harder LOOPO protocol (vary #source OPs, record length, perturbations); cover other loading levels via FEM or new measurements | XL |
| E3 | Methodological details for reproducibility insufficiently documented | ✅ valid | Full preprocessing/architecture/hyperparameter tables + released code; see R1-4, R1-7, R3-5 | M |

E2's "general applicability" is the one that cannot be satisfied from the public data
alone: all seven operating points sit at **7.0 kVA**, so a single loading level. See R2-8.

---

## Reviewer 1

| # | Comment | Verdict | Assessment and fix | Effort |
|---|---|---|---|---|
| R1-1 | Comparative results show no significant novelty vs. previously reported results | 🔴 valid | Same as E1. The benchmark is saturated (all methods 0.96–0.995), so it cannot demonstrate anything new. Reframe. | XL |
| R1-2 | The measurement + signal-processing methodology deserves a full treatment — worked examples of every parameter, variation with operating point, literature references for the formulas | ⚠️ valid, and an opportunity | The paper defines Eqs. (6)–(8) but never shows a worked numeric example, never cites sources for the formulations, and never shows how each descriptor moves with operating point. **R1 is offering you a second paper** — take this seriously as a strategic option (see `03_revision_plan.md`, Option C). Minimum: add references for each descriptor family, one fully worked example per family, and a per-OP sensitivity figure. | M–L |
| R1-3 | ML comparison needs per-method detail: input signal type, preprocessing, representation, and fuller explanation of results | ✅ valid | Add a table: per model — input (file-level feature vector vs. raw window), dimension, scaling, hyperparameter grid, selection criterion. For the CNN: window length, overlap, per-channel normalisation, layer-by-layer architecture, optimiser, LR schedule, batch size, epochs, β in Eq. (11), early stopping, seeds. | M |
| R1-4 | Paper does not contain the information needed to reproduce and independently verify the results | ✅ valid — and decisive | This alone justifies rejection at a Transactions. **Release the code and a fixed feature manifest.** The dataset is CC BY 4.0 and already public, so a public repo with extraction + training + evaluation scripts, plus environment pinning and seeds, is achievable and removes the objection outright. | M |
| R1-5 | Describe how LOOPO is applied to the two-sensor signals | ✅ valid | Currently only stated at a high level. Specify: features are computed per channel then concatenated (CH1 and CH2 stay in the same file-level vector); files never split across folds; the whole held-out OP — both channels, all severities — is excluded from feature scaling, hyperparameter search and threshold selection. Add a fold-composition table (train/test file counts per fold; see `05_dataset_reference.md` §6). | S |
| R1-6 | Justify 90° sensor placement rather than 180° as in [15] | ✅ valid, easy | You did not choose it — the geometry is fixed by the source dataset. Say so. Then give the physics you already have: in an 8-pole machine, 90° mechanical = 360° electrical, so the p-symmetric healthy field is nominally *in phase* at the two sensors, and a single-pole defect breaks that equivalence — which is exactly what motivates the cross-channel descriptors. [15] uses 180° on a different machine for a different fault (stator ITSC). Section II already contains this argument; it just needs to be stated as an explicit answer. | S |
| R1-7 | Insufficient information on training signals: number, type, preprocessing, threshold selection | ✅ valid | Fully answerable from the source (see `05_dataset_reference.md` §6): 607 files, 10 s at 125 kHz, two channels, CSV; per-OP × per-severity counts; window count after segmentation; class imbalance; and the t01 = 0.10 / t12 = 0.35 / t23 = 0.675 threshold selection procedure with the candidate grid and the selection criterion made explicit. | S–M |
| R1-8 | More thorough discussion of the results in the tables | ✅ valid | Tables II–V are presented with little interpretation. In particular explain *why* raw harmonic amplitudes collapse to 0.80 while normalised profiles reach 0.95 — that is Eq. (5) in action and it is your own argument going unused. | S |
| R1-9 | Fig. 6: how can 48 errors give a higher macro-F1 than 22 errors, while 12 and 4 errors give the same macro-F1? | ⚠️ **your numbers are right, your presentation is wrong** | Denominator switch: classical rows n = 607, CNN rows n = 1821 = 607 × 3 seeds. 48/1821 = 2.64 % < 22/607 = 3.62 %; and 12/1821 = 4/607 = 0.659 % exactly. Fix by reporting **error rate** and putting CNN results on the 607-file basis as mean ± std over seeds. See `02_root_cause.md` Problem 4 and `tools/error_rate_check.py`. | S |

---

## Reviewer 2

| # | Comment | Verdict | Assessment and fix | Effort |
|---|---|---|---|---|
| R2-1 | Novelty unclear; the features are known and not new | 🔴 valid | Correct — harmonic ratios, band-energy ratios and cross-channel differences are all established. Novelty must move to the physical result (validated Eq. (4), confounding index), not the feature list. | XL |
| R2-2 | Add computational demand and time-to-diagnosis metrics | ✅ valid, easy, and useful | Report on stated hardware: feature-extraction time per 10 s file, training time, inference time per file, model size/parameter count, peak memory. Then go further — sweep the **record length** required to reach target accuracy. That converts a reviewer request into a new result and simultaneously serves `02_root_cause.md` Problem 1, fix 2. | S–M |
| R2-3 | "Physics-informed beats raw data" is already known | ✅ valid | Agreed; stop presenting it as the finding. See `02_root_cause.md` Problem 3. | — |
| R2-4 | Fig. 1 must show how the taps are connected to produce the controlled fault, and photos of the flux sensors mounted on the generator | ✅ valid, fully answerable | Tap terminals are **J (healthy), J1 (94 turns, 20 %), J2 (235, 50 %), J3 (470, 100 %)** on one pole, switched automatically without shutdown. Redraw Fig. 2 with the terminal labels and the switching element. The data report contains a **photograph of the sensor and its mounting**, and the dataset is **CC BY 4.0**, so it can be reproduced with attribution. | S |
| R2-5 | Since the data is from a public dataset, contact the authors of [11] | ✅ valid, and strategically important | Do this. It gets you: (a) the **per-operating-point field current** you need for `02_root_cause.md` Problem 2 — the single highest-value missing item; (b) permission/figures for the bench and sensors; (c) the reason for the P15 numbering (R3-4); (d) possibly new measurements at other loading levels and finer taps, which is the only realistic route to E2 and R2-7/R2-8. A co-authorship or acknowledged collaboration also removes the "someone else's data" undertone in R2's comment. | S to initiate |
| R2-6 | Why are there 2 generators in Fig. 1? | ✅ valid, easy | The bench carries an 8-pole salient-pole SG (the machine under test) **and** a 2-pole cylindrical SG (10 kVA, 3000/3600 rpm) not used in this study, both driven by the 10 kW DC motor through an electromagnetic clutch. One sentence; consider greying out the unused machine in the figure. | S |
| R2-7 | Demonstrate sensitivity to incipient faults — 20 % of the turns of one coil is not incipient | ⚠️ valid, and the terminology is genuinely wrong | Two honest moves. (1) **Reframe the number**: 20 % of one pole = 94 of **3760** total rotor turns = **2.5 % of the field winding**, and it perturbs the fundamental by only ≈ γ/2p = 1.25 %. Say that; it is a much more defensible statement than "20 %." (2) **Stop calling it incipient.** The finest tap in the public dataset is 20 % of one pole; sub-20 % cases need new hardware. Report the *detection margin* at 20 % in normalised-ratio units so a reader can extrapolate, and either commit to finer taps as future work or generate sub-20 % cases by FEM. | M (reframe) / XL (new data) |
| R2-8 | All conditions have the same stator MMF; test other conditions. Clarify whether the stator is grid-connected or voltage-controlled | ✅ valid — and half of it is free | **Grid connection:** confirmed — the generator is synchronised to the local 60 Hz distribution network, so terminal voltage is imposed by the grid and is *not* regulated to be perfectly balanced and sinusoidal. State this, and characterise the background unbalance/THD from the data you have. **Same stator MMF:** correct and unavoidable — all seven OPs are at **7.0 kVA**, so only the reactive axis is explored, never the loading axis. This is a genuine limitation on "general applicability" (= editor's E2). Address by FEM extension, new measurements via the R2-5 collaboration, or an explicitly narrowed claim. | S (clarify) / XL (new conditions) |

---

## Reviewer 3 — recommends publication with minor edits

Worth noting: **one of three reviewers recommended acceptance.** All of R3's points are
editorial and cost roughly a day in total.

| # | Comment | Verdict | Fix | Effort |
|---|---|---|---|---|
| R3-1a | CH1/CH2 used before being defined | ✅ **verified correct** | CH1/CH2 first appear in Section II ("induces nominally matched signatures in CH1 and CH2") before the Section III definition. Define at first use or forward-reference. | S |
| R3-1b | MAE used before "severity mean absolute error (MAE)" is expanded | ✅ **verified correct** | MAE appears in the Table II header and in Section IV-D ("minimized severity MAE") before it is expanded in Section IV-E. Move the expansion to first use. | S |
| R3-2a | Figs. 1, 2, 3 are never referenced in the text | ✅ **verified correct** | Confirmed: Figs. 1–3 appear only as captions; Figs. 4–7 are cited. Add in-text citations, and cite them in order. | S |
| R3-2b | Table III has no description or reference in the text | ❌ **factually incorrect** | Table III *is* cited twice (Section II: "confirmed in Table III"; Section V-A: "Table III reports representative high-correlation indicators"). **Do not argue the point.** The underlying concern is fair: the Section II citation is a forward reference from six pages earlier and the Section V-A discussion is one line. Expand the discussion and move the table next to it — that satisfies the reviewer without a dispute. | S |
| R3-2c | Footnote-style captions hard to read; undefined columns (# in Table II, ρ) | ✅ valid | Define every column in the header or caption: `#` = number of features; `ρ` = Spearman rank correlation with ordinal severity (Table III); `Bal.` = balanced accuracy; `n` = number of evaluated predictions; `Err.` = misclassified files. Move long footnotes into the body text. (R3 wrote "ρ in Table IV"; ρ is in Table III — a minor slip, ignore it and fix both tables.) | S |
| R3-3 | "magnitude of the external magnetic field" is ambiguous | ✅ valid | Replace with the precise quantity — e.g. "the RMS amplitude of the sensor-induced voltage, which is proportional to the time derivative of the tangential stray-field flux density." Sweep the manuscript for other loose uses of "magnitude"/"field." | S |
| R3-4 | Explain the P15–P21 notation; can there be other regimes outside this range? | ✅ valid, easy | The labels are inherited verbatim from the source dataset for traceability. The published dataset contains **only** P15–P21; P1–P14 are neither described nor released, and the data report gives no reason for the numbering. Say exactly that — **do not invent a rationale** — and confirm with the dataset authors when you contact them (R2-5). Note this also exposes R2-8: the released regimes are all at 7.0 kVA. | S |
| R3-5 | Include a developed worked example, perhaps a code listing, at least for the 1D-CNN | ✅ valid — converges with R1-4 | The best response is not a code fragment in the paper but a **public repository** plus an architecture/hyperparameter table and one fully worked numeric example (one file → windows → features → prediction). This answers R3-5, R1-3, R1-4 and E3 at once. | M |

---

## Distribution of effort

- **Editorial / presentation (S):** R1-5, R1-6, R1-8, R1-9, R2-4, R2-6, all of R3 — about
  1–2 days total, and they remove roughly half the comment list.
- **Documentation and code release (M):** E3, R1-3, R1-4, R1-7, R2-2, R3-5 — about 1–2 weeks.
- **New experimental work on existing data (L):** `02_root_cause.md` Problems 1 and 3 — the
  harder LOOPO protocol, calibration generalised to classical models.
- **Blocked on external input (XL):** Problem 2 needs field current per operating point;
  R2-7 and R2-8/E2 need finer taps and other loading levels — new measurements or FEM.

**The short items are not the problem.** Doing only those produces a tidier manuscript that
fails on the same three grounds.
