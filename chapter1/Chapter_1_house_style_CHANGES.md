# Chapter 1 — what the house-style pass changed

`Chapter_1_house_style.docx` is the authors' final chapter (`incoming/Chapter_1_final.docx`, 7 September 2026) with the house style of `House_Style.md` applied by `src/apply_house_style.py`. The stamped copy for circulation is `to_send/Chapter_1.docx`; the copy circulated before this pass is kept as `to_send/archive/Chapter_1_2026-09-07.docx`.

## Presentation

- **Figures 1.1–1.3 and 1.5–1.9** replaced by house-style drawings (`src/ch1_figures.py`), each placed at exactly the text width, 15.92 cm, so that its 11 pt Times text prints at 11 pt. Before, the same nominal 9 pt label printed anywhere from 7 to 12 pt, because each figure had been drawn at one width and placed at another.
- **Figure 1.5** was an AI-generated chart (its legend read "Copper losses — orange", at 96 dpi, wider than the text block). It is now a graph of the scaling laws its caption states.
- **Figure 1.2**: the geared train is drawn in elevation with a closed gearbox, so no gearing can face the wrong way, and the lubrication skid shows tank, pump and **oil cooler**; the direct drive keeps the axial section, AMBs inside, impeller overhung (Juha, 14–15 September).
- **Figure 1.4**, the authors' MATLAB rotor model, is left as it was: restyling it needs its data. Run `src/hsbook_style.m` on the figure and replace the picture.
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
- Figure 1.5 caption: one sentence added stating that its loss values are illustrative and how the efficiency maximum is found
- Table 1.2: full stop added after the number ("Table 1.2." as in every other caption)
- Table 1.2: headings and entries set in sentence case, as in Table 1.4
- Table 1.3: full stop added after the number ("Table 1.3." as in every other caption)
- Table 1.3: "4x", "8x" written as "4×", "8×"
- Table 1.3: headings and entries set in sentence case, as in Table 1.4
- Table 1.4: full stop added after the number ("Table 1.4." as in every other caption)

A paragraph-by-paragraph comparison with the original confirms that nothing else in the text changed.

## Noticed, not changed

- Body paragraphs are indented inconsistently (some 1.25 cm from the margin, most not). That is body text, outside this pass, and the publisher resets it anyway.
- There is no Heading 2 for §1.2: the chapter runs from §1.1.2 straight into §1.2.1.
- §1.1 still reads "mechanical rpm value"; the book writes r/min everywhere else.
