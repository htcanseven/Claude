# House style for figures, tables and captions

*High-Speed Electrical Machines and Drives* — rules for every chapter

Every figure, graph and table in the book looks the same, whoever drew it. The rules are short, and most of them are enforced by two small tools, so nobody has to remember them: `hsbook_style.py` for Python and `hsbook_style.m` for MATLAB. Chapter 1 has been brought into this style and is the reference example.

## 1. The one rule that makes the rest work

**Every figure is made at the full text width, 15.92 cm, and inserted into the manuscript at 100 %.** Never scale a figure in Word and never crop it there.

Text in a figure only prints at the size it was drawn if the figure is placed at the width it was drawn at. Before this style, the same 9 pt label in Chapter 1 printed anywhere from 7 to 12 pt for exactly this reason. Only the height varies from figure to figure.

The publisher will rescale the book to its own trim size. Because every figure is built at the same width, they all scale together and stay identical to one another. When Wiley confirms the trim size, the width changes in one place in each tool and every figure is regenerated.

## 2. Text in figures and tables

| | Rule |
|---|---|
| Font | Times New Roman, the font of the text. Liberation Serif or Nimbus Roman are acceptable stand-ins where Times New Roman is not installed; their letter widths are identical. |
| Size | 11 pt, the size of the text, for every piece of text: axis labels, tick numbers, legends, labels and panel titles. Sub- and superscripts follow automatically. |
| Weight | Regular. In figures, nothing is bold. In tables, only the header row is bold. |
| Italic | Quantity symbols only (*n*, *P*, *f*<sub>1</sub>, Ω), exactly as in the text. Units and descriptive subscripts are upright: *v*<sub>tip</sub>, *P*<sub>Fe</sub>, *f*<sub>sw</sub>. |
| Case | Sentence case: "Rotational speed", not "Rotational Speed". |

## 3. Graphs

- **No title inside the figure.** The caption is the title.
- **Frame and ticks**: full box; ticks pointing inward on all four sides; a light grey grid behind the data.
- **Axis labels** take the form *Name symbol (unit)*: "Rotational speed *n* (r/min)", "Loss (% of rated output)". A dimensionless quantity has no parentheses.
- **Numbers**: decimal point; numbers of five or more digits grouped with a thin space (30 000, 100 000); four-digit numbers ungrouped (1500). Logarithmic axes carry plain numbers (0.1, 1, 10, 100 000), not powers of ten.
- **Units**: SI throughout. Speed in r/min, never rpm. Factors are written with ×, not x: 4×, ×16.
- **Line weights**: data curves 1.2 pt; axes and ticks 0.6 pt; grid 0.4 pt; reference and construction lines 0.5 pt.
- **Series**: up to four per graph, each a fixed pairing of colour and line style, so they stay distinguishable in greyscale print. More than four series usually means two graphs.

  | Series | Colour | Line |
  |---|---|---|
  | 1 | blue #1f4e79 | solid |
  | 2 | rust #a6350f | dashed |
  | 3 | green #4a7c1f | dash-dot |
  | 4 | ink #1a1a1a | dotted |

- **Labelling the series**: label curves directly, in the curve's own colour, wherever there is room. Otherwise use a legend without a frame, placed in empty space inside the axes.
- **Marked points**: an open circle, white fill and dark edge, joined to its label by a thin grey leader line.
- **Bar charts** add hatching to the colour (plain, ////, ....) for the same greyscale reason.
- **Panels**: (a), (b) … with a short title, centred below each panel. The caption refers to them by letter.

## 4. Illustrations

Figure 1.2 is the reference. All three of its panels are drawn the same way, and every illustration in the book should look as if the same hand drew it.

- **Two-dimensional engineering drawings only**: an elevation, a half section or a section, drawn as a drafter would draw it. No perspective, no 3-D rendering, no shading gradients, no photorealism. No AI-generated imagery (see §10).
- **Flat fills, no hatching.** Every part is drawn as a flat, light fill from the palette below, with an ink outline. Nothing is hatched.
- **Showing the inside**: draw a *half section*. The upper half is cut and the lower half is seen from outside, with the centre line between them. Cut housing walls take the darker *section* tone. Shafts, rotors and other solid parts on the axis are never cut. A laminated stack is shown by thin grey lines across it, perpendicular to the shaft.
- **Machines in their setting** stand on a floor: a heavy floor line with a light band below it and a baseplate above it, as in Figure 1.2. Anything below floor level, such as an oil skid, is drawn in that band.
- **To scale, from real dimensions.** Draw every part from its real dimensions, in metres, so that its proportions are true; never stretch a part to fit a label or the page. A high-speed machine is small for its power, and the drawing must show it: in Figure 1.2 the high-speed motor is seen at its true size beside the 1500 r/min motor it replaces, about a seventh of its volume.
- **One scale for what is compared.** Arrangements set side by side for comparison share one scale, so that the reader compares sizes directly, and the caption says so.
- **Scale bar.** Every illustration drawn to scale carries one, in empty space: a bar 0.13 cm high in two halves, ink and white, a round length (1 m, 0.2 m), and below it the labels 0 and the length with its unit.
- **Detail views.** Where a part is too small at the common scale to show its inside, repeat it in a panel of its own at a larger scale, with its own scale bar, and give the ratio in the caption: Figure 1.2(c) shows the motor of (b) at twice the scale.
- **Representative dimensions.** When a drawing stands for a class of machine rather than a particular one, take its sizes from catalogue equipment of one stated rating, and say in the caption that they are representative.
- **Scale shared with a graph**: a rotor drawn above its mode shapes shares their axial scale (Figure 1.4).
- **Line weights**: part outlines 1.0 pt. Leader lines, centre lines, dimension lines, lamination lines and small details 0.5 pt.
- **Centre lines**: thin, grey, dash-dot.
- **Labels**: horizontal, sentence case, 11 pt. Main units are named above them, with the speed under the name where it matters ("compressor / 30 000 r/min"). Every other label is joined to its part by a thin grey leader line *without* an arrowhead. A leader that ends inside a part ends in a small dot. Arrows are kept for flow, motion and dimensions.
- **Fills** come from one material palette, light enough for labels to stay legible:

  | Material | Fill |
  |---|---|
  | Housing, casing, seen from outside | #f2f2ef |
  | Housing wall where a section cuts it | #dcdcd6 |
  | Shaft, disc, solid steel | #cfcfcf |
  | Rotor active part, drawn as one body | #a6a6a6 |
  | Laminated core | white, with thin grey lines across the stack |
  | Bearings, AMB stators | white |
  | Windings | #c9a227 |
  | Coolant, cooling jacket | #d7e4f0 |
  | Oil, lubrication | #f4e6d8 |
  | Floor, foundation | #f5f5f5 |

## 5. Diagrams

A diagram shows a relationship rather than an object or a set of data. Figure 1.9, the high-speed trilemma, is the reference.

- **Shapes**: flat fills with ink outlines of 1.0 pt; circles, ellipses and boxes, nothing more. No shadows, no gradients, no 3-D.
- **Arrows** show influence, sequence or flow: ink, 1.3 pt, with a filled head. A cycle that carries the argument may be drawn with broad arrows instead, curved and filled in the colour of the element each one leaves, with a thin ink edge, as in Figure 1.9: steel #a9a9a9, copper #c9a227, coolant #8fb1d1.
- **Colour carries meaning, and keeps it through the chapter.** A region is a light tint of a series colour, the colour at 13 % on white, and the text inside it is set in the colour itself:

  | Colour | Tint | In Chapter 1 it means |
  |---|---|---|
  | blue #1f4e79 | #e2e8ee | the converter: the pulse-ratio lines of Figure 1.6, the gatekeeper of Figure 1.9 |
  | rust #a6350f | #f3e5e0 | silicon IGBTs, and the low-pole industrial topology they reach |
  | green #4a7c1f | #e8eee2 | SiC and GaN, and the high-pole mobile topology that needs them |

- **Elements** may sit on a disc tinted with their material from the illustration palette: steel #ececec, copper #f3e9c9, coolant #e2ebf4, for the mechanical, electromagnetic and thermal corners of Figure 1.9.
- **Draw rather than write.** Mark the elements with small drawings made like the illustrations, from the palette and without shading, so that the reader sees what each element is: in Figure 1.9 the sleeved rotor with its centrifugal load, a machine in cross-section, a liquid-cooled stator, and the two-pole and six-pole rotors of the two paradigms. No clip art and no icon sets.
- **The focal element** may stand on a light grey ring, #ececec, 0.22 cm wide, as the feasible window does in Figure 1.9.
- **Text**: 11 pt, horizontal, sentence case. The names of the elements are set in ink, outside their shapes where there is room.
- **Greyscale**: tints are told apart by their labels, so every tinted region carries one.

## 6. Colour and greyscale

Wiley has not yet said whether the book prints in colour. Until it does, **every figure must read correctly when printed in greyscale**. That is why each colour carries its own line style or hatching, and why every tinted region is labelled. Check by printing the figure in black and white.

## 7. Tables

- **Caption above** the table.
- **Times New Roman 11 pt** throughout, single line spacing, no space before or after paragraphs in cells.
- **Horizontal rules only**: 1 pt above and below the table, 0.5 pt under the header row. No vertical rules, no shading, no grid.
- **Header row** bold and repeated at the top of each page. Units go in the header in parentheses. **Body rows** regular. Rows are not split across pages.
- **Alignment**: text columns left, columns of numbers or short formulae centred.
- **Full text width**, sentence case, × for factors.

The Word table style *HS Book Table* in this document does all of this. Insert a table, choose the style, and mark the first row as a header row.

## 8. Captions

- **Label**: "Figure 4.7." or "Table 4.2.", in bold, followed by the caption in regular type. The full stop after the number is always there.
- **Placement**: figure captions **below** the figure; table captions **above** the table.
- **Content**: the first sentence names what is shown; the following sentences say what to look for. Panels are referred to by letter. Values that are illustrative rather than measured are said to be so, and so are dimensions that are representative rather than those of a particular machine.
- **Style**: the Word paragraph style *Caption* in this document: Times New Roman 11 pt, justified like the text.

## 9. Headings, citations and references

- **Headings** are in sentence case, as in the table of contents: "1.3.2 Rotordynamics and critical speeds", "1.2.1 Industrial high-speed machines: the stationary approach". There is no full stop after the section number or at the end of the heading. Sections take the Word style Heading 2 and subsections Heading 3; a heading below a subsection is a bold paragraph of its own, in sentence case, kept with the paragraph that follows it.
- **Citations** in the text take the form (Author, year) for one author, (Author and Author, year) for two, and (Author et al., year) for three or more: "(Lipo, 2017)", "(Pyrhönen et al., 2013)".
- **References** are listed at the end of each chapter under the heading "References", in alphabetical order of the first author, in the form of Chapter 1: the authors with their initials, the year, the title in sentence case, the journal or book in italics, the volume, issue and pages, and the DOI where there is one. Each entry has a hanging indent.
- **Until Wiley says otherwise.** IEEE Press books often use numbered references instead. If the publisher asks for them, author–year lists convert mechanically, so write author–year now.

## 10. Sources and rights

- **No AI-generated images.** The copyright in them is unsettled, so the authors may not be able to grant Wiley the licence the contract asks for. Several large publishers do not accept them at all.
- **Figures taken from another source** are redrawn in this style and cited in the caption: "Redrawn from [12]." When the redrawing follows the original closely, permission is still needed; ask the chapter owner.
- **Data from another source** is plotted in this style, and the source of the data is cited in the caption.
- **Photographs** are used only of real hardware, at no less than 300 dpi at printed size, and only with the owner's written permission.

## 11. What to deliver with a chapter

| File | Purpose |
|---|---|
| `fig_4_07.png` | in the manuscript: 600 dpi, exactly 15.92 cm wide |
| `fig_4_07.pdf` or `.svg` | for production: vector, text kept as text, fonts embedded |
| the script or `.m` file that draws it | so that any figure can be regenerated when the trim size or a value changes |

Name figures `fig_<chapter>_<number>`, with two-digit numbers: `fig_4_07`.

## 12. The tools

**Python.** `hsbook_style.py` sets matplotlib to this style. `save()` checks every piece of text in the figure and refuses to write a figure whose font, size or weight is off.

```python
import hsbook_style as hs
hs.setup()
fig, ax = hs.figure(8.5)           # a graph, 8.5 cm tall
ax.plot(n, P_loss)
ax.set_xlabel(hs.label('Rotational speed', 'n', 'r/min'))
ax.set_ylabel(hs.label('Loss', 'P_loss', 'kW'))
hs.save(fig, 'figures/fig_4_07')   # .png, .pdf and .svg

fig, ax = hs.canvas(12.0)          # an illustration, in cm
hs.laminated(ax, 2.0, 5.0, 3.1, 4.2)          # a laminated stack
hs.leader(ax, 'stator', (3.5, 3.6), (3.5, 6.0), dot=True)
```

For a drawing to scale, keep the dimensions in metres and convert them once, as `geared_vs_directdrive()` in `src/ch1_figures.py` does: a view maps metres to centimetres of the page at a chosen scale, and every part is placed through it.

**MATLAB.** `hsbook_style.m` takes a finished figure and puts it into this style: width, font, size, line weights, ticks, grid, series colours and styles, no title, no legend box. It then exports it at exactly that size.

```matlab
plot(n, P1, n, P2)
xlabel('Rotational speed \itn\rm (r/min)')
hsbook_style(gcf, 8.5, 'fig_4_07')   % restyle, write .png, .pdf
```

The MATLAB function was written without access to MATLAB. Check the first figure it exports by eye, and report anything it gets wrong so that it can be fixed for everyone at once.

**Word.** The *Caption* paragraph style and the *HS Book Table* table style are defined in this document. Copy them into a chapter with Home → Styles → Manage Styles → Import/Export, or simply paste a table from this document.

## 13. Checklist before sending a chapter

1. Every figure is 15.92 cm wide and inserted at 100 %, with no Word cropping.
2. All text in figures and tables is Times New Roman 11 pt, with symbols in italic.
3. No titles inside figures; panels lettered (a), (b) below the panels.
4. Every graph reads in greyscale, and every tinted region is labelled.
5. Illustrations are 2-D drawings in flat fills from the palette, with no hatching, no AI imagery and no photorealism.
6. Illustrations are drawn to scale from real dimensions; arrangements that are compared share one scale and carry a scale bar.
7. In diagrams, each colour means one thing, and the same thing throughout the chapter.
8. Tables use *HS Book Table*, with the caption above.
9. Captions use *Caption*, labels "Figure c.n." and "Table c.n." in bold.
10. Headings in sentence case; citations as (Author et al., year); a reference list at the end of the chapter.
11. Units in SI, r/min not rpm, × not x, thin space in 30 000.
12. Every borrowed figure is redrawn and cited; every borrowed dataset is cited.
13. The source file of every figure is delivered with it.
