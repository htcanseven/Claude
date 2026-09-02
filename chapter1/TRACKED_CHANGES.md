# Chapter 1 — what was changed in `Chapter_1_HS_machines_TRACKED.docx`

The file is the author's own `The_first_Ch_of_HS_machines_1.docx` with every edit recorded as a Word tracked change under the author name **Claude** (403 revisions). Open it with Review → Tracking → **All Markup**; Accept or Reject works on each change individually. Track Changes is switched on in the document, so further edits by the co-authors are recorded too.

Nothing outside the items below was touched. Three of the four existing figures (the fourth, Figure 1.9, is replaced as a tracked change), the eight Word equations, the styles, footers and page setup are exactly as they were. Reject-all reproduces the original text paragraph for paragraph (verified, 267 of 267).

## Deleted

1. **The 40-line planning outline at the head of the chapter.** It had drifted from the section structure below it (it lists §1.5.2 as thermal scaling; the body has mechanical stress there). A tracked deletion: one Reject restores it if it is wanted.
2. **One sentence in the fP passage** that apologises for its own missing citation — *"…without external resources provided, no direct literature citation can be offered…"*. This would be the first technical sentence a reviewer reads.

## Trimmed

3. The closing sentence of that passage keeps *"In summary, the definitions for high-speed machines remain varied: tip speed, n√P, and now the fP product."* and loses the trailing *"Literature is still evolving … limited in the current context."*

## Copy-edits (ten, each a few words)

4. "mechanical rpm value" → "mechanical r/min value" (unit consistency)
5. "10, rather to 20 times" → "10 to 20 times"
6. "In EU financed Voltcar project" → "In the EU-financed Voltcar project"
7. "(2–5… mm)" → "(2–5 mm)"
8. "stress in in inner radius" → "stress at the inner radius"
9. "a high airgap" → "a large air gap"
10. "the airgap magnetic-flux density" → "the air-gap magnetic-flux density"
11. "rises the switching frequency" → "raises the switching frequency"
12. "If only possible mf ≥ 21 should be followed" → "Wherever possible, mf ≥ 21 should be maintained"

## Captions written for the author's four existing figures

The pictures were already in the document; only their captions were placeholders. All figures are now numbered in sequence, 1.1 to 1.9.

13. **Figure 1.2** — geared versus direct-drive architecture (was "Figure 2. Caption").
14. **Figure 1.4** — the computed rotor bending mode shapes, modes 1–4 with frequencies (was "Fig. 3 Caption"). The caption ends with **[machine and source to be stated]** — I did not want to guess which rotor this is.
15. **Figure 1.5** — loss components against speed (was "Fig 4 Caption"). The caption states that the chart is drawn at fixed machine geometry, which ties it to the new §1.5.5.
16. **Figure 1.9** — the high-speed trilemma (was "Fig. 5 Caption"). **The picture itself is also replaced** (a tracked replacement: the original picture is marked deleted and the new one inserted, so a single Reject restores the original). The new drawing follows the text of §1.6.1 literally: the three remedies form a directed cycle — sleeve → larger effective air gap, pole count and frequency → iron and windage loss, cooling geometry → lower stiffness and higher l/D — around a feasible design window, and the power-electronic interface is drawn as the gatekeeper splitting that window into the low-pole industrial topology (reachable with silicon IGBT converters) and the high-pole mobile topology (SiC/GaN only). Source: `src/make_trilemma.py`.

## Added text and figures

17. **§1.1.1, after the 180 000 kW/s threshold** — two paragraphs. The threshold rests on a single design point that is itself marginal by tip speed (150.8 m/s against 150 m/s), so fP is presented as a descriptive figure of merit with its calibration deferred; and the positive argument for fP is stated: it is the only criterion that contains the pole number, shown with the two-pole/six-pole comparison at identical rating. The author's threshold sentence is untouched. **New Figure 1.1**: the n√P and fP criteria in the power–speed plane.
18. **§1.3.1, after the solid-versus-laminated comparison** — the algebraic form of the centrifugal stress, so the author's statement that a central bore doubles the stress becomes quantitative: σmax = [(3+ν)/8]ρv² solid, [(3+ν)/4]ρv² bored, worked to 252 MPa at 200 m/s and 395 MPa at 250 m/s against a 450 MPa proof stress. **New Figure 1.3**.
19. **§1.4.1, after the switching-loss trade-off** — the converter requirement for the Table 1.1 machine as a number: 1500 Hz at m_f = 21 needs 31.5 kHz; silicon at 16 kHz gives m_f = 10.7, so the machine cannot be supplied from silicon. **New Figure 1.6**.
20. **§1.5.4, after the square–cube passage** — a qualification: the argument assumes isotropic scaling, which high-speed machines do not follow (they shrink radially and grow axially, preserving rotor surface area). The author's passage is untouched.
21. **New §1.5.5 "Reading the scaling table" with Table 1.4** — the same speed doubling evaluated along the tip-speed-limited design path. **Table 1.3 is left exactly as written**; the new text explains that its rows are evaluated under different conditions and that its fourfold and eightfold figures are right for overspeeding an existing machine but not for a redesign, where windage is unchanged and iron loss doubles. **New Figure 1.7** compares the paths.
22. **New §1.5.6 "Rotordynamic scaling"** — the first bending critical speed falls as Ω⁻³ while operating speed rises as Ω, so the margin degrades as Ω⁴ and a speed doubling costs a factor of sixteen. This is the constraint that actually ends the pursuit of speed, and the draft did not quantify it. It cross-references the author's own mode-shape figure (1.4). **New Figure 1.8**.

## Deliberately not changed

- **§1.6.2, the roadmap.** It still describes the 19-chapter plan. Left alone because the table of contents is to be discussed next; it will need to match whatever is agreed.
- The repeated industrial-versus-mobile contrasts, the trilemma framing, every heading, and all three original tables.
- The `[ref]` placeholders, which are the author's own markers.

## Notes

- The new equations are typed as formatted text (italic symbols, subscripts, superscripts) rather than as Word equation objects, so they can be edited freely; they can be converted with Insert → Equation if the house style requires it.
- The five new figures are 300 dpi PNG at the same 15.9 cm width as the author's figures, generated from the equations in the text (`src/make_figures.py`), so they can be restyled without redrawing.
- The package passes the OOXML schema validation and the redlining check (every changed character is inside an `ins`/`del`). It could not be rendered to PDF in this environment — LibreOffice refuses to load any .docx here, the original included — so the page layout has not been checked visually.
