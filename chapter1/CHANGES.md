# Chapter 1 — Record of Changes

Three versions were produced from the 6 110-word draft:

| | Prose words | Figures | Est. pages* | Scope |
|---|---|---|---|---|
| Original draft | 6 110 | 4 placeholders | ~13 | — |
| **CONSERVATIVE** | 8 577 | 9 (all supplied) | **~20** | original prose verbatim; corrections added alongside it |
| **MINIMAL** | 5 544 | 8 (all supplied) | **~14** | original structure kept, prose rewritten |
| **FULL** | 7 940 | 8 (all supplied) | **~18** | restructured, with new material |

**The CONSERVATIVE version is the recommended one for submission.** It reproduces 205 of the draft's 227 body paragraphs verbatim — 93.4 per cent, or 99.1 per cent excluding the roadmap, which had to change to match the 12-chapter table of contents. Every other correction is made by *adding* text, a table or a figure alongside the author's own wording rather than by replacing it. Its complete edit set is listed in §F below and is generated from an auditable operations list in `src/build_conservative.py`.

\* Wiley's formula: 600 words per page, 2 illustrations per page.

Both versions contain every technical correction. They differ only in structure and depth.

---

## A. Technical corrections

### A1. Table of scaling laws was internally inconsistent — corrected

The original Table 1.3 mixed two different scaling paths within one table. The stress row was evaluated at constant tip speed ("if v_tip is fixed") and the power row at reduced diameter ("if D is reduced"), but the iron-loss and windage rows were evaluated at **fixed diameter** — which contradicts the tip-speed constraint the chapter had just established.

Re-deriving along the tip-speed-limited constant-power path (rotor radius ∝ Ω⁻¹, active length ∝ Ω, so that rated power and peripheral speed are both preserved):

| Quantity | Draft claimed | Corrected | Why |
|---|---|---|---|
| Windage loss | ×8 | **×1.00** | P_w ∝ D⁴lΩ³ → Ω⁻⁴·Ω·Ω³ = Ω⁰. Physically: shear stress is set by tip speed, which is fixed; rotor surface area D·l is preserved because the diameter reduction and length increase cancel. |
| Iron loss | ×4 | **×2.00** | Loss per unit mass rises as f², but iron mass falls with the halving active volume. |
| DC copper loss | "independent of speed" | **×1.00** | Correct in the draft, now derived rather than asserted. |
| Rotor surface area | — | **×1.00** | New row; it is the reason the square–cube argument does not apply. |

Verified numerically in `src/verify_scaling.py`; analytic exponents and the numerical model agree exactly.

### A2. The binding constraint was missing entirely

The draft never quantified the rotordynamic penalty, which is the mechanism that actually stops the pursuit of higher speed. For a rotor treated as a uniform beam, n_cr ∝ r/l². Substituting the same tip-speed-limited path:

    n_cr ∝ Ω⁻¹/Ω² = Ω⁻³        and therefore        n_op/n_cr ∝ Ω⁴

**A doubling of design speed degrades the rotordynamic margin by a factor of sixteen.** This is the single strongest number in the chapter, it explains why high-speed machines run supercritically, and it justifies the weight given to Chapter 8 in the book plan. New Figure (1.4 full / 1.6 minimal) plots the divergence.

The idealisation is flagged in the text: a real rotor is not a uniform beam, bearing span exceeds active length, and shaft extensions add outboard mass. The exponents indicate severity of trend, not design values.

### A3. Three design paths now distinguished

A scaling exponent is meaningless until one states what is held constant. The draft's exponents describe **overspeeding an existing machine**, not designing a new one. Three paths are now separated explicitly:

- **(a) fixed geometry** — the overspeed case; where the ×4 and ×8 figures actually belong
- **(b) tip-speed limited at constant power** — the idealised design path
- **(c) length capped by rotordynamics** — what real designs do

Every column of the new table states its path. Two conclusions follow that reverse the draft's emphasis: the *loss* penalty of high speed is smaller than commonly claimed, and the *rotordynamic* penalty is far larger.

### A4. Square–cube thermal argument corrected

The draft argued that loss-per-surface-area "increases linearly with 1/D" as the machine shrinks. That holds only under isotropic scaling. High-speed machines scale anisotropically — shrinking radially while growing axially — and under that path rotor surface area is preserved. The thermal problem is real but it is not the square–cube law; the text now identifies the actual mechanisms (stator loss density, and the air gap's poor and largely irreducible thermal conductance isolating the rotor).

### A5. Centrifugal stress now quantified

The draft asserted that a central bore "doubles the mechanical stress." Correct, and now derived: for a solid disc σ_max = [(3+ν)/8]ρv², for a bored disc [(3+ν)/4]ρv². Worked through for electrical steel — 252 MPa at 200 m/s, 395 MPa at 250 m/s against a ~450 MPa proof stress — which turns a qualitative claim into a usable design limit. New Figure 1.1.

---

## B. Removals

### B1. Drafting artefacts in the fP passage

Two sentences were removed verbatim:

> "However, **without external resources provided**, no direct literature citation can be offered for the fP product as a formal definition."

> "Literature is still evolving, and while the fP product is gaining recognition as a meaningful metric, explicit references for its adoption in formal classification are limited **in the current context**."

These read as an AI tool commenting on its own retrieval limits. Publishers screen for this, and it was in the first technical section a reviewer would reach.

### B2. The circular fP threshold

The draft set the threshold at 180 000 kW/s because the single Voltcar machine happened to reach it. A reviewer would flag this immediately — and the anchor is doubly weak because Voltcar is *marginal* by tip speed (150.8 m/s against a 150 m/s threshold).

fP is now presented as a **proposed drive-system figure of merit**, with its calibration deferred to the Chapter 2 machine survey. The justification is strengthened rather than weakened: the argument for fP is now that it is the only criterion containing pole number, demonstrated with the two-pole/six-pole comparison at identical rating and tip speed.

### B3. Fourfold repetition of the industrial-vs-mobile contrast

The contrast appeared four times: at the tail of §1.1.2 ("The Divergent Evolution"), in the conclusion of §1.2.1, in the conclusion of §1.2.2, and again in §1.4.2 ("Framing the Comparison") with Table 1.2. Consolidated into one section with one summary table. Roughly 1 500 words recovered.

### B4. Repeated chapter previews

Three subsections each closed by previewing "the chapters that follow." Now done once, in the final section.

---

## C. Additions

- **Worked classification example** (§1.2.5 full / §1.1.1 minimal). The Voltcar machine carried through all three criteria, showing that they disagree and why — the disagreement is the pole count, which is the argument for fP.
- **Converter requirement derived** (§1.5.1 / §1.4.1). f₁ = 1500 Hz at m_f = 21 requires f_sw = 31.5 kHz; a silicon IGBT stage at 16 kHz gives m_f = 10.7, at the stability floor. The machine *cannot* be supplied by silicon. This connects the classification example to the converter argument with a number rather than an assertion.
- **Six analytical figures**, generated from the equations in the text (`src/make_figures.py`), all reproducible.
- **Notation paragraph** (§1.7.2, full version only) fixing symbol conventions for the book.

---

## D. Structural changes

### D1. Trilemma → three constraints and a gate

The draft's §1.6.1 stated the trilemma and then immediately undercut it: *"This trilemma is further complicated by the power electronic interface."* If power electronics is a fourth axis, the trilemma is not a trilemma.

Resolved by treating the converter as a **gate** rather than an axis: it does not trade against the three constraints, it makes part of the space unreachable. This is both more accurate and a better argument — it explains why SiC changed what is designable without implying it removed the constraint. Figure 1.8 was redrawn accordingly.

### D2. Roadmap rewritten for 12 chapters

§1.6.2 described 19 chapters in six parts. Replaced with the 12-chapter structure in four parts.

### D3. Planning skeleton removed

The 40-line outline at the head of the draft had drifted from the text below it (skeleton §1.5.2 was thermal scaling; the text's §1.5.2 was mechanical stress, with thermal at §1.5.4). Removed; the section structure now carries the outline.

### D4. Full version only — reordering

Constraints moved ahead of the paradigms, so that the physics is established before the two design families are explained as different responses to it. The direct-drive history was rewritten as the lead-in to §1.6, where it explains *why* the two paradigms diverge: the industrial machine went high-speed to delete a gearbox, the mobile machine to justify keeping one.

### D5. Figure numbering

Draft had Figures 2, 3, 4, 5 with no Figure 1. Both versions now run 1.1 to 1.8 sequentially.

---

## E. Still needed from the authors

**Figures: complete.** All eight are now supplied and embedded in both chapter documents. Six are generated from the equations in the text (`src/make_figures.py`); the two schematics — geared versus direct-drive architecture, and first and second rotor bending modes — are drawn in `src/make_schematics.py`. All are 300 dpi and reproducible from source, so they can be restyled to Wiley's artwork specification without redrawing.

**Citations.** Every location is listed in the References section of both documents. The only confirmed citation carried from the draft is El Hajji et al. (2024). The ones that matter most for a reviewer are the source for the 150 m/s and n√P thresholds, the Voltcar project reference, and the m_f = 21 synchronous-PWM threshold.

**One open decision.** Whether switched reluctance machines are in scope. The chapter is written on the assumption that SynRM and PM-assisted SynRM are treated in Chapter 3 and that SRM gets a bounded section rather than a chapter, on the grounds that its asymmetric-bridge converter breaks the drive-interface argument running through the rest of the book. If that is wrong, one sentence in §1.7.3 changes.

**Page budget.** The full version is ~18 pages against the 28 budgeted in the table of contents. The gap is real and it can be closed — the most useful additions would be a second worked example carried through the constraints, and expansion of §1.6 with a costed industrial-versus-mobile comparison. Padding it out to reach 28 would weaken it; the alternative is to reduce Chapter 1's budget in the ToC to ~20 and give the recovered pages to Chapter 4.


---

## F. The CONSERVATIVE version: complete edit set

Everything done to the original draft, in full. Generated from the `OPS` list in `src/build_conservative.py`, so the edit set is auditable rather than asserted.

### Removed (2 items)

1. **The planning outline at the head of the chapter** (40 lines). Not prose — a working skeleton that had drifted from the body below it, listing §1.5.2 as thermal scaling where the body has mechanical stress. It would read as unfinished in a submitted sample.
2. **One sentence**, in the fP passage: *"The fP product is discussed in the context of classifying machines beyond simple speed or power alone… However, without external resources provided, no direct literature citation can be offered for the fP product as a formal definition."* This apologises for its own missing citation and cannot be repaired by addition. It sits in the first technical section a reviewer reaches.

### Trimmed (1 item)

3. The closing sentence of the same passage keeps its summary clause — *"In summary, the definitions for high-speed machines remain varied: tip speed, n√P, and now the fP product."* — and loses only the trailing *"…explicit references for its adoption in formal classification are limited in the current context."*

### Replaced (1 item)

4. **Section 1.6.2, the roadmap.** The draft describes 19 chapters in six parts; it now describes the 12 chapters in four parts agreed for the table of contents. This is the only substantial replacement, and it is unavoidable: a sample chapter that promises a different book from the one the proposal offers is incoherent. The closing sentence is preserved verbatim.

### Added — text (6 blocks)

5. **§1.3.1, after the solid-versus-laminated comparison.** The algebraic form of the centrifugal stress, so the draft's statement that a central bore doubles the stress becomes quantitative: σmax = [(3+ν)/8]ρv² for a solid disc against [(3+ν)/4]ρv² with a bore, worked through as 252 MPa at 200 m/s and 395 MPa at 250 m/s against a 450 MPa proof stress. *The original sentence is untouched.*
6. **§1.1.1, after the fP threshold.** Two paragraphs noting that the 180 000 kW/s value rests on a single design point which is itself marginal by tip speed (150.8 against 150 m/s), and that Chapter 2 calibrates it against a machine population. Also states the argument *for* fP: it is the only criterion containing the pole number. *The original threshold sentence is untouched.*
7. **§1.4.1, after the switching-loss trade-off.** The converter requirement for the machine of Table 1.1 worked as a number: 1500 Hz at m_f = 21 needs 31.5 kHz, while a silicon stage at 16 kHz gives m_f = 10.7, so this machine cannot be supplied from silicon.
8. **§1.5.4, after the square–cube passage.** A qualification: the argument assumes isotropic scaling, which high-speed machines do not follow, since the tip-speed limit makes them shrink radially and grow axially, preserving rotor surface area. *The original passage is untouched.*
9. **New §1.5.5 and Table 1.4.** The same speed doubling evaluated along the tip-speed-limited design path. **Table 1.3 is left exactly as written**; the new section explains that its rows are evaluated under different conditions, and that its fourfold and eightfold figures are correct for overspeeding an existing machine but not for a redesign. On the design path, windage is unchanged and iron loss doubles.
10. **New §1.5.6.** The rotordynamic scaling result: n_cr ∝ Ω⁻³ against an operating speed rising as Ω, so n_op/n_cr ∝ Ω⁴ and a speed doubling costs a factor of sixteen. This is the constraint that actually terminates the pursuit of speed, and the draft did not quantify it.

### Added — figures (9, of which 4 fill the draft's own placeholders)

| | Figure | Status |
|---|---|---|
| 1.1 | n√P and fP criteria in the power–speed plane | new |
| 1.2 | Geared versus direct-drive architecture | fills the draft's *Figure 2. Caption* |
| 1.3 | Centrifugal stress against peripheral speed | new |
| 1.4 | First and second rotor bending modes | fills the draft's *Fig. 3 Caption* |
| 1.5 | Taylor–Couette flow regimes in the air gap | fills the draft's *Fig 4 Caption* |
| 1.6 | Required switching frequency, silicon against wide bandgap | new |
| 1.7 | Speed doubling along three design paths | new |
| 1.8 | Operating speed against first critical speed | new |
| 1.9 | The high-speed design space | fills the draft's *Fig. 5 Caption* |

Numbering is now sequential; the draft ran from Figure 2 to Figure 5 with no Figure 1.

### Deliberately left alone

- The fourfold repetition of the industrial-versus-mobile contrast. It is the author's structure and no reviewer will call it an error, only a length question.
- The trilemma framing in §1.6.1, including *"This trilemma is further complicated by the power electronic interface."* The draft's own next sentence calls the semiconductor choice a "gatekeeper", so Figure 1.9 visualises the author's wording rather than replacing it.
- Every heading, every table of the original, and all remaining prose.
