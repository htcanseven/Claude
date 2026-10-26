# Chapter 1 — what the house-style pass changed

`Chapter_1_house_style.docx` is the authors' final chapter (`incoming/Chapter_1_final.docx`, 7 September 2026) with the house style of `House_Style.md` applied by `src/apply_house_style.py`. The stamped copy for circulation is `to_send/Chapter_1.docx`; the copy circulated before this pass is kept as `to_send/archive/Chapter_1_2026-09-07.docx`.

A second pass on 26 October redrew Figures 1.2 and 1.9 and made the wording changes agreed with the authors; they are listed under their headings below and marked *(26 October)*. Since then the circulated copy carries no Word comments: `src/add_confidentiality.py` removes them, because they are the authors' working notes. The copy of 7 September carried all fifteen, so every contributor who received the chapter has seen them.

## Presentation

- **All nine figures** replaced by house-style drawings (`src/ch1_figures.py`), each placed at exactly the text width, 15.92 cm, so that its 11 pt Times text prints at 11 pt. Before, the same nominal 9 pt label printed anywhere from 7 to 12 pt, because each figure had been drawn at one width and placed at another.
- **Figure 1.9** *(26 October)* is redrawn as a cycle, drawn rather than written. The three domains sit at the corners, each a small drawing in the illustration style on a disc tinted with its material: the sleeved rotor with the centrifugal load on it, a six-pole machine in cross-section with copper in its slots, a liquid-cooled stator. Broad curved arrows, each in the colour of the domain it leaves, carry the cycle of remedies, each creating the next problem. At the centre the feasible window, ringed in grey, is split by the power-electronic gatekeeper into the two paradigms, each shown by its rotor: two poles for the industrial machine with silicon IGBTs, six for the mobile machine with SiC or GaN. The colours of the paradigms and the gatekeeper are those of Figure 1.6. The caption follows: the triangle's edges become the cycle, and one sentence explains the rotors.
- **Figure 1.5** was an AI-generated chart (its legend read "Copper losses — orange", at 96 dpi, wider than the text block). It is now a graph of the scaling laws its caption states.
- **Figure 1.2**: the geared train is drawn in elevation with a closed gearbox, so no gearing can face the wrong way, and the lubrication skid shows tank, pump and **oil cooler** (Juha, 14–15 September). *(26 October)* Every part is now drawn to scale from its real dimensions, for a compressor unit of about 300 kW at 30 000 r/min: a four-pole 315 kW motor in IEC frame 355 (1.56 m long, 1.01 m high), a two-stage gearbox of ratio 20 in a closed casing 0.6 m by 0.8 m, couplings for 1.9 kN m and 95 N m, a compressor with a volute 0.56 m across, and an oil tank of about 160 l. Panels (a) and (b) share one scale and a scale bar, so the high-speed motor (0.79 m long, 0.33 m across) is seen at its true size: about a seventh of the volume of the motor it replaces. Its inside would be lost at that scale, so a new panel (c) repeats it at twice the scale, upper half in section: radial and axial AMBs, touchdown bearings, the stator and its cooling jacket, the rotor (0.12 m by 0.24 m), and the impeller overhung on the shaft end. The compressor of (b) stays directly below the one in (a). The editable copy in `figures/editable/` follows, with (c) as a third group.
- **Figure 1.4** is redrawn in the same manner: the rotor of the authors' model drawn to scale in flat fills, with the first four mode shapes plotted below it on the same axial scale. The vertical lines carry the three radial-AMB planes down from the drawing into the graph. **The curves were traced from the picture of the MATLAB figure** (`src/trace_fig_1_04.py`, to within about half a pixel of the original lines) because the model data are not in the repository. Before publication, export the four mode shapes from the model into `data/fig_1_04_modes.csv` and rerun `src/ch1_figures.py 1.4`. The part names (radial AMB, active part) are read from the model drawing; the authors should confirm them.
- **Captions**: one paragraph style, *Caption* (Times New Roman 11 pt, justified), label in bold; figure captions below, table captions above and kept with their table.
- **Tables**: one style, *HS Book Table*: full text width, horizontal rules only (1 pt above and below, 0.5 pt under the header), Times New Roman 11 pt, header bold and repeated across pages, body regular, text left and numbers centred, rows not split across pages.
- Every figure carries its caption as alternative text.
- Figure 1.4: image and caption separated into two paragraphs, as for every other figure
- Figure 1.2: Word crop of the old picture removed (the new drawing has no title or margin to trim)
- Figure 1.5: Word crop of the old picture removed (the new drawing has no title or margin to trim)
- Figure 1.6: Word crop of the old picture removed (the new drawing has no title or margin to trim)
- Figure 1.7: Word crop of the old picture removed (the new drawing has no title or margin to trim)
- Figure 1.8: Word crop of the old picture removed (the new drawing has no title or margin to trim)
- Table 1.2: bold removed from the body rows; only the header is bold
- Table 1.3: bold removed from the body rows; only the header is bold
- Table 1.4: bold removed from the body rows; only the header is bold

## Wording — the only text changes

- Figure 1.2 caption: "Left:" and "Right:" made "(a)" and "(b)", since the panels are stacked
- Figure 1.2 caption: "(AMBs)" added, the abbreviation the drawing uses. *(26 October)* The sentence on the half section of (b) is replaced by two: the units are drawn to scale for a compressor of about 300 kW, (a) and (b) at one scale and (c) at twice it; the dimensions are representative of catalogue equipment, not those of a particular machine
- Figure 1.4 caption: one sentence added explaining the rotor drawing above the mode shapes and the lines marking the radial AMBs
- Figure 1.5 caption: one sentence added stating that its loss values are illustrative and how the efficiency maximum is found
- Table 1.2: full stop added after the number ("Table 1.2." as in every other caption)
- Table 1.2: headings and entries set in sentence case, as in Table 1.4
- Table 1.3: full stop added after the number ("Table 1.3." as in every other caption)
- Table 1.3: "4x", "8x" written as "4×", "8×"
- Table 1.3: headings and entries set in sentence case, as in Table 1.4
- Table 1.4: full stop added after the number ("Table 1.4." as in every other caption)

*(26 October)* The wording agreed with the authors, made by `fix_text()` in `src/apply_house_style.py`:

- Headings in sentence case, as in the table of contents: the fifteen numbered headings that were in title case, and the 24 bold headings within the sections, which are now also kept with the paragraph that follows. The full stops after "1.4" and "1.5" are gone.
- "The r/min fallacy: why speed is a relative term" and "Different definitions of high speed" were Heading 3 without a number, beside the numbered §1.1.1 and §1.1.2; they are now bold headings within §1.1.1, like the others at that depth. §1.1.1 itself was already numbered by Word, which a text extraction does not show.
- §1.2 has its heading, "1.2 The two paradigms: industrial and mobile"; the chapter used to run from §1.1.2 straight into §1.2.1.
- §1.1.1: "a mechanical rpm value" reads "a mechanical value in r/min".
- The four citations not in the form "(Author et al., year)" are brought to it: Armengaud, Canseven, Lipo, Pyrhönen.
- **The open comments.** The six comments still open each held the full reference for an in-text citation. They are now a reference list at the end of the chapter, alphabetical, with hanging indents. El Hajji et al. gain their full author list and DOI and Armengaud et al. their DOI, both from the publishers' records; Hrabovcová gets her accent, and the Pyrhönen book is the second edition, which is the 2013 one. All fifteen comments are marked resolved in the master.

A paragraph-by-paragraph comparison with the original confirms that nothing else in the text changed.

## Noticed, not changed

- Body paragraphs are indented inconsistently (some 1.25 cm from the margin, most not). That is body text, outside this pass, and the publisher resets it anyway.
- The Canseven et al. paper is cited as 2024, but volume 40 of *IEEE Transactions on Energy Conversion* is the 2025 volume. The year was left as the authors wrote it.
- Wiley-IEEE Press may ask for numbered references; the list is in author–year form because the chapter is.
