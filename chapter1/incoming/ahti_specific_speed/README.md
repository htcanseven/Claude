# Ahti Jaatinen-Värri — the specific-speed text (thread of 9 Sept – 6 Oct 2026)

Files in this directory, in order:

| File | What it is |
|---|---|
| `thread.msg` | the whole exchange, Juha ↔ Ahti, Hüseyin and Ilya in copy |
| `01_Ahti_draft1_2Oct.docx` | Ahti's first draft, 283 words, two comments of his own |
| `02_Pyrhonen_returned_2Oct.docx` | the same with Juha's three tracked insertions and two comments |
| `03_Ahti_draft2_6Oct.docx` | draft 2, 702 words: five new equations and a worked table |

## What was asked and what came back

Juha wrote to Ahti on 9 September asking for "virtaustekniikkaa for idiots" — a compact
statement of what specific speed is, what its equation is, what justifies it, and why it so
often ends in a demand for high rotational speed, with a few practical examples of how the
enthalpy difference is defined. He said the destination is the book's **Introduction**,
because the Introduction and the table of contents are the teaser going to Wiley.

Draft 1 gave the definition, the fluid dependence, and the good range for centrifugal
compressors (0.6–0.9, Rodgers 1980). Juha asked for worked numbers: an air compressor at
pressure ratio 3 from room conditions, hydrogen, perhaps a steam turbine, and an answer to
whether the volume flow in (1) is the inlet volume in both the compressor and the turbine
case. Draft 2 adds equations (2)–(6) — ideal-gas enthalpy rise, specific gas constant,
isentropic outlet temperature, inlet volume flow, inlet density — and Table 1 comparing air
and hydrogen.

## The check of Table 1

The arithmetic is internally consistent and the physics is right, with one error.

**The inlet density is evaluated at 0 °C while the enthalpy rise is evaluated at 15 °C**,
and the caption says 15 °C. Air: ρ = 1.277 kg/m³ needs T = 272.8 K; Δhs = 106 615 J/kg needs
T = 287.9 K. Hydrogen behaves the same way, ρ = 0.088 at 273.4 K against Δhs = 1 549 090 at
287.9 K. Recomputed consistently at 15 °C:

| | tabulated | at a consistent 15 °C |
|---|---|---|
| air, ρ | 1.277 kg/m³ | 1.209 kg/m³ |
| air, qv | 2.3497 m³/s | 2.4810 m³/s |
| air, N | 29 405 rpm | **28 640 rpm** |
| hydrogen, ρ | 0.088 kg/m³ | 0.0835 kg/m³ |
| hydrogen, qv | 34.065 m³/s | 35.935 m³/s |
| hydrogen, N | 57 473 rpm | **55 995 rpm** |

Both speeds fall about 2.7 %. The error cancels in the ratio, so the point the table is
making is untouched: hydrogen needs **1.96 times** the speed of air for the same duty, by
either set of numbers.

Everything else in the table reproduces: N follows from Ns = Ω√qv / Δhs^(3/4) to within
rounding, Δhs from cp = Ri/(1−1/γ), and the 14.5× enthalpy ratio quoted in the text matches
the table's 14.53.

Worth keeping: the air case is 3 kg/s at pressure ratio 3, which is about 400 kW of shaft
power at 29 000 r/min. That is the book's industrial running machine arriving from the
turbomachinery side rather than being asserted.

## Smaller corrections

1. **Equation (1) is broken.** Ω now sits outside the equation object as plain text, so the
   formula renders as Ns = √qv/Δhs^(3/4) with a dangling Ω beside it. It happened when the
   symbol was changed from ω to Ω in Juha's copy; draft 1 had ω inside the equation.
2. **Equation (3) reads Ri = Ri/M.** The numerator should be Ru, the universal gas
   constant, as the sentence after it says.
3. **ρin is tabulated as [g/m³].** The values are kg/m³.
4. **pin is tabulated in bar** but equation (6) wants pascals. Tabulate 10⁵ Pa, or say so.
5. **Tin is not a column** although it drives every other number in the row. Add it; it is
   also what would have caught the 0 °C / 15 °C slip.
6. "where pin s the compressor inlet pressure" → "is". "equation (1) show that" → "shows".
7. Yes to Juha's question in the margin: (1) is dimensionless in SI as written —
   (rad/s)·(m³/s)^½ / (J/kg)^¾ reduces to 1 — so the units he added are right.

## Still open from Juha's comments

- **The turbine case is unanswered.** He asked specifically whether the volume flow in (1)
  is the inlet volume for a turbine as well as for a compressor. It is the convention that
  differs, and a reader who assumes inlet for both will size a turbine wrong. One sentence
  settles it.
- **No steam-turbine example**, which he asked for, and no statement of how the enthalpy
  difference is obtained for a real fluid beyond "use CoolProp or Refprop".
- **The figure.** Ahti offers one but it is not his; Juha said to supply the sample and the
  bibliographic reference so it can be redrawn copyright-free. Ahti's reply gives a
  ConceptsNREC blog post. A company blog is not a citable source for a Wiley book: the
  underlying material is the Balje specific-speed/specific-diameter chart (Balje,
  *Turbomachines: A Guide to Design, Selection and Theory*, Wiley 1981) or Rodgers 1980,
  which he already cites. Redraw from one of those.

## Two decisions for the book, not for Ahti

**Where does this text go?** Juha asked for it for the Introduction. Chapter 1 is finished,
stamped and circulating. But §2.2 of the table of contents — "Why the driven machine sets
the speed: specific speed and the turbomachinery optimum" — is Juha Saari's, in Chapter 2.
Two people are now writing specific speed. The natural split is a short version in Chapter 1
(the equation, the rule that Ns fixes the speed, one worked number) and the full treatment
with the table and the fluid comparison in §2.2 — but then Ahti's text is Chapter 2's and
Saari needs to know.

**Ahti's standing.** He is already offered Chapter 13 jointly with Jonna Tiainen, and his
draft support letter argues that the speed requirement originates in the driven machine.
This text is the evidence for that argument, which is good for the coherence of both. It
does mean his name now appears in three places, and the contributor list should say so.

## One thing the thread settles

Juha's opening email of 9 September tells Ahti: "Hüseyin, Ilya ja minä olisimme kirjan
editorit. Liittokirjoittajia kymmenkunta" — Hüseyin, Ilya and I would be the book's
**editors**, with about ten co-authors. So the authors → Editors change in his revision of
the annotated table of contents is deliberate and of long standing; he has been describing
the book as an edited volume to contributors since early September. That answers the
question raised when his revision came in, at least as to his intention.
