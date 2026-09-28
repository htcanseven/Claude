# Pre-submission review — IET Electric Power Applications version

Review of the 12-page IET EPA template version, compared against the IEEE TEC submission and
the TEC reviewer comments.

## Verdict

**Substantially better than the TEC version, a good scope fit for IET EPA, and — after about
half a day of fixes — in reasonable shape to submit.** I'd expect a *revise* decision rather than
a reject, with a realistic path to acceptance.

IET EPA is a machines journal (its scope names "design and analysis of motors and generators of
all sizes"), so the system-relevance problem EPSR had does not arise here. The journal has
published exactly this line of work, and the manuscript now cites six IET EPA papers, including
both overviews it builds on (Mazaheri-Tehrani & Faiz on stray-flux monitoring; Mostafaei & Faiz
on SG fault detection). IET EPA also runs normal revision rounds, so fixable gaps can be fixed.

Two things need attention before submitting:

1. The move to the IET template introduced **regressions** — the funding acknowledgment
   disappeared, two tables collide on page 9, the reference list is visibly broken, and three
   figures reproduced from the source dataset are not attributed.
2. **Figure 5(c) contradicts Eq. (5) on the under-excited side**, and a machines reviewer is
   well placed to notice. There is a clean physical explanation, and adding it turns the weakest
   point in the physics into its strongest. About an hour, no new experiments.

---

## What improved

Real work went into this revision. Addressed from the TEC comments:

| Comment | How it was addressed |
|---|---|
| R2-1 novelty / known features | Explicit statement that the contribution is *not* new descriptors — good positioning |
| R2-6 two generators | Fig. 1 caption now explains the 2-pole machine is unused |
| R2-4 taps and sensors | J/J1/J2/J3 in text; Fig. 3 now includes a sensor photograph |
| R1-6 90° spacing | Honestly attributed to the dataset, not presented as a design choice |
| R3-4 P15–P21 | Labels explained as inherited from the source dataset |
| R2-8 constant stator MMF | Fixed 7.0 kVA stated as a scope limit |
| R2-7 "incipient" | No longer claimed for this work |
| R1-9 denominators | Explained in the Section 5.2 text |
| R3-1, R3-2, R3-3 | CH1/CH2, MAE, ρ defined at first use; Figs. 1–3 cited; "magnitude" wording fixed |
| — | Eq. (1) and Eq. (3) assumptions stated; conclusion bounded to one machine and one dataset; McNemar interpretation tightened; Data Availability and COI statements added |

---

## A. Fix before submitting (~2–3 hours total)

### A1. Funding acknowledgment was dropped — restore it *(5 min, compliance)*

The TEC version acknowledged: *"This work was supported by the Academy of Finland under the Centre
of Excellence Programme for the project High-Speed Electromechanical Energy Conversion Systems."*
**The IET version has no Acknowledgments section and no funding statement at all.**

This matters beyond courtesy: the funder (now the Research Council of Finland) expects its
support to be acknowledged, and **IET EPA's author guidelines ask for all funding sources to be
listed in the Acknowledgments section.** Restore it, and check the current grant number and
funder name.

Also: **all IET journals require ORCID** for submission.

### A2. Figures 1–3 are reproduced from the dataset paper without full attribution *(5 min)*

Figs. 1, 2 and 3 appear to come from the data report [14] — Fig. 3's black coil in a cream holder
with the terminal-box cross-section matches the data report's own Figure 2. **Only Fig. 1's
caption cites [14]; Figs. 2 and 3 cite nothing.**

CC BY 4.0 permits reuse but *requires* attribution, and Wiley asks about permissions for
previously published figures. Add to all three captions:

> Reproduced from [14] under the CC BY 4.0 licence.

While there: Fig. 3's caption still says "Schematic overview" but it now contains a photograph —
change to "(left) Photograph of the search coil; (right) schematic of the 90° placement of CH1
and CH2." Fig. 1 has callouts 4, 5, 6 that the new caption no longer defines (the TEC caption
did: clutch, flange systems, position transducers) — restore that legend.

### A3. Tables 3 and 4 collide on page 9 *(15 min)*

Table 3's *Interpretation* column runs straight into Table 4's *Model* column — "Mech. harmonic
increases" and "SC-CNN" touch with no gutter — and Table 4 is squeezed into very small type.
Place them one above the other, or make Table 4 full width (`table*`).

### A4. Reference list is visibly broken *(30 min)*

Almost certainly a BibTeX/template issue, but it looks careless on the last page:

- **19 double commas** in author lists ("Xuanjie Fan,, and Peng Qi")
- Missing spaces: "Frontiers in Energy Research14", "Measurement70", "IEEE Access10"
- **[2]** lost its year, volume and pages (the TEC version had 2025)
- **[10]** is broken ("…electrical machines." , .) — it is a PhD thesis, Newcastle University, 2018
- **[13]** ends with ", ."
- Inconsistent capitalisation: "IET electric power applications", "IEEE transactions on…"

### A5. Fig. 6 still shows the numbers R1 questioned *(15–30 min)*

The Section 5.2 text now explains the denominators — good. But **Fig. 6 still labels its bars
"48 err." and "22 err."**, with the 48-error bar standing taller than the 22-error one. That is the
exact image that made R1 doubt the results, and figures get read on their own. Relabel with error
rates:

| Bar | Label now | Label instead |
|---|---|---|
| ExtraTrees | 3 err. | 0.49 % |
| SVM-RBF | 4 err. | 0.66 % |
| LogReg-L2 | 4 err. | 0.66 % |
| SC-CNN | 12 err. | 0.66 % |
| Raw-CNN | 48 err. | 2.64 % |
| RF | 22 err. | 3.62 % |

Add an error-rate column to Table 4 as well. And **Fig. 7**: P18 has 90 files in total (30 + 20 +
20 + 20), but the matrices show 90 *healthy* files and 60 per fault class, because they are pooled
over three seeds. The caption should say so: "Counts are pooled over three seeds; per-seed counts
are one third of those shown."

### A6. The abstract was not updated *(10 min)*

The body improved; the abstract is word-for-word the TEC version. It still leads with "the
benchmark does not support a simple deep-learning-superiority conclusion" and "recovered all 36
raw CNN errors" (a pooled count). The editor reads the abstract first. A drop-in revision is in
`07_minimal_revision_package.md`.

---

## B. Worth an hour: Fig. 5(c) and the physics model

This is the most substantive issue, and fixing it strengthens the paper rather than just
patching it.

### What the figure shows

Read from Fig. 5(c) at γ = 1, the fundamental-normalised ratio A(45 Hz)/A(60 Hz):

| Operating point | Excitation | A(45)/A(60) at γ = 1 |
|---|---|---|
| P18 | 0.3 PF under-excited | ≈ 0.29 |
| P17 | 0.5 PF under-excited | ≈ 0.36 |
| P16 | 0.8 PF under-excited | ≈ 0.48 |
| P15 | unity | ≈ 0.60 |
| P19, P20, P21 | over-excited | ≈ 0.73, nearly coincident |

The pooled linear fit shown in the figure has **R² = 0.811** — a number the text never mentions.

### Why it matters

Eq. (5) says the normalised ratio is approximately independent of I_f. The figure shows that
holds on the **over-excited** side — P19, P20 and P21 collapse almost exactly — but not on the
**under-excited** side, where the curves fan out *monotonically with decreasing excitation* to a
≈ 2.5× spread. The text calls this "residual spread", which undersells a systematic effect.

A machines reviewer will see a pattern that tracks excitation this cleanly and ask what the model
is missing.

### The explanation

Eq. (4) assumes |V(f_e)| ∝ I_f. That holds when the rotor field alone sets the fundamental. But
this generator is **grid-connected at constant apparent power**, so its terminal voltage and
armature-current magnitude are imposed externally, and part of the 60 Hz stray field is set by
the operating condition rather than by I_f. The sub-synchronous fault harmonics have no such
component: they come only from the rotor MMF defect, so they still scale as γ·I_f.

Writing |V(f_e)| ≈ K_a + K_e·I_f:

```
R ≈ γ·K_k·I_f / (K_a + K_e·I_f)
```

- **High excitation** (K_e·I_f ≫ K_a): R → (K_k/K_e)·γ, independent of I_f. **Over-excited curves collapse.** ✓
- **Low excitation**: the fixed term K_a is no longer negligible, so R falls with I_f. **Under-excited curves fan out in excitation order.** ✓

That reproduces the qualitative shape of Fig. 5(c) — and it explains *why P18 is the boundary
case* more precisely than the current text does. The current text says low I_f weakens the fault
harmonics, which normalisation should fix. The fuller answer is that normalisation *stops
working* in exactly the under-excited regime.

Worth a sanity check with a phasor diagram if you have the machine's reactances. And note the
public dataset does not report I_f per operating point, so the excitation ordering is inferred
from standard phasor relations, not measured — say so in one sentence.

### Drop-in text

**Section 2**, replacing the sentence beginning "The model assumes linear magnetics…":

> The model assumes linear magnetics and a fixed defect location, and neglects local saturation,
> AVR dynamics, and the contribution of the grid-imposed terminal voltage and armature current to
> the fundamental. The first two perturb the constants $K_k$; the third does not, and in
> under-excited operation it limits the cancellation of $I_\mathrm{f}$ in (5), as shown in
> Section 5.1. Since the public dataset does not report field current per operating point, the
> excitation ordering used here follows from standard phasor relations for a grid-connected
> synchronous generator at constant apparent power rather than from direct measurement.

**Section 5.1**, after "visible residual spread remains between under-excited and over-excited
conditions":

> The structure of this residual is informative. The three over-excited operating points
> (P19–P21) collapse almost onto a single curve, whereas the under-excited points fan out
> monotonically with decreasing excitation from P15 to P18, reaching a spread of roughly 2.5× at
> $\gamma = 1$ (pooled linear fit $R^2 = 0.811$). This follows if the fundamental contains a
> component that does not scale with field current, which (4) omits. Because the generator is
> grid-connected at constant apparent power, its terminal voltage and armature-current magnitude
> are imposed externally, so part of the 60 Hz stray field is fixed by the operating condition
> rather than by $I_\mathrm{f}$. Writing $|V(f_\mathrm{e})| \approx K_a + K_\mathrm{e} I_\mathrm{f}$
> gives $R \approx \gamma K_k I_\mathrm{f} / (K_a + K_\mathrm{e} I_\mathrm{f})$: at high excitation
> the rotor term dominates and $R$ tends to the excitation-independent value
> $(K_k/K_\mathrm{e})\gamma$ predicted by (5), while at low excitation $R$ falls with
> $I_\mathrm{f}$. Normalization therefore removes excitation dependence in over-excited operation
> but only partially in under-excited operation — precisely the regime of the boundary failure
> analysed in Section 5.4.

---

## C. Quick logic fix: the threshold-sensitivity argument *(15 min)*

Section 5.4 argues the P18 correction is not fragile threshold tuning because "the P18
sensitivity analysis showed perfect performance for t₂₃ values between 0.55 and 0.80."

**That tests the wrong threshold.** The P18 errors are 20 % → healthy confusions. Correcting them
requires ŷ_sev = 1, i.e. 0.10 ≤ ŝ_file < 0.35 — governed by **t₀₁ = 0.10** (and t₁₂), not by
t₂₃ = 0.675, which only separates 50 % from 100 %. A sweep of t₂₃ says nothing about the 20 % →
healthy correction.

The good news is that the correct argument is *stronger*: **t₀₁ and t₁₂ were fixed a priori at the
physical midpoints and never tuned**, so the P18 correction cannot be a product of threshold
tuning. Replace the two sentences:

> The P18 correction depends on $t_{01}$ and $t_{12}$, which were fixed a priori at the physical
> midpoints between severity levels and never tuned, so it cannot be attributed to threshold
> selection. The tuned threshold $t_{23}$ affects only the 50 %/100 % boundary; it was stable at
> 0.675 across all seven outer folds, and P18 performance remained perfect for
> $t_{23} \in [0.55, 0.80]$.

If easy, add the range of ŝ_file for the P18 20 %-severity files to show the margin above 0.10.

---

## D. Likely to come back in review — can wait for the revision round

Given the low-effort goal, these are reasonable to defer, since IET EPA will return a revision
request rather than reject for them. But D1 is the most common request in machine-learning-for-
machines reviews, and an hour now saves a round.

**D1. Implementation details.** Still absent: CNN architecture (layers, kernels), window length
and overlap, optimiser, learning rate, batch size, epochs, the value of β in Eq. (11),
hyperparameter grids for SVM and LR, FFT settings, the t₂₃ candidate grid, and a code link. This
was the TEC editor's explicit reproducibility ground. One compact table would pre-empt it.

**D2. Per-operating-point file counts.** P15 95, P16 84, P17 80, P18 90, P19 90, P20 84, P21 84 —
sum 607. One small table; see `05_dataset_reference.md`.

**D3. Figure legibility.** Fig. 5 squeezes three panels into one column, leaving legends and axis
labels at roughly 5 pt — make it full width. Fig. 2's tap labels are nearly unreadable; enlarge
them and add J/J1/J2/J3.

---

## Practical: check APC funding before submitting

IET EPA is fully open access at **$2,800**. LUT's FinELib Wiley agreement had exhausted its
full-OA quota by September 2026, with an optional 2027 continuation — and given IET EPA review
times, acceptance will almost certainly fall in 2027. Confirm with the LUT library whether IET
titles are covered and whether the 2027 year applies; otherwise the APC is paid directly.

---

## Checklist

- [ ] A1 Acknowledgments section with Research Council of Finland funding restored; ORCID ready
- [ ] A2 "Reproduced from [14] under CC BY 4.0" on Figs. 1–3; Fig. 3 caption updated; Fig. 1 callouts 4–6 defined
- [ ] A3 Tables 3 and 4 separated
- [ ] A4 Reference list cleaned (double commas, spaces, [2], [10], [13], capitalisation)
- [ ] A5 Fig. 6 relabelled with error rates; error-rate column in Table 4; Fig. 7 caption notes pooling
- [ ] A6 Abstract revised
- [ ] B Fig. 5(c) explanation added to Sections 2 and 5.1; R² = 0.811 stated; I_f caveat added
- [ ] C Threshold-sensitivity argument rewritten around t₀₁
- [ ] D1–D3 optional now, likely requested in review
- [ ] APC funding confirmed with LUT library
