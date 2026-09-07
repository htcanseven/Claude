Figure 1.2 — geared train and integrated direct drive, in editable form
=======================================================================

Figure_1_2.pptx     PowerPoint, and the easiest one to work in. No picture is
                    embedded: the drawing is 115 native PowerPoint shapes, one
                    per part, so you can click a housing and recolour it, drag
                    a leader line, or retype a label straight away. Each panel
                    is its own group — "Figure 1.2 (a)" and "Figure 1.2 (b)" —
                    so a panel moves or scales as one piece; double-click into
                    a group to reach the parts. Shapes are named for the
                    selection pane (Home > Select > Selection Pane).
                    The section hatching is a PowerPoint pattern fill, the
                    centre lines are dash-dot connectors, and every label is
                    Times New Roman text.
                    The slide is 10 x 10 in, i.e. the 6.6 in figure enlarged
                    by 1.52 so the 6 pt labels are workable on screen; scale
                    the two groups together if you need the printed size.

Figure_1_2.svg      Vector, for Inkscape or Illustrator. Every label is real
                    text, not outlines, so it can be retyped. The font stack
                    asks for Times New Roman first, with DejaVu Serif as the
                    fallback the layout was set in; if a label reflows after a
                    font change, nudge it rather than resizing the drawing.

Figure_1_2.pdf      Same drawing as vector PDF, for Illustrator or for LaTeX.

Figure_1_2_source.py  The drawing itself, as the matplotlib script that
                    produced it. This is the real master: every coordinate is a
                    number you can change, and re-running it regenerates the
                    PNG, SVG and PDF together, so they never drift apart.
                    Run from the chapter1 directory:
                        python3 src/make_schematics.py     PNG, SVG, PDF
                        python3 src/mpl_to_pptx.py         the PowerPoint

How to edit
-----------
PowerPoint: open the .pptx and edit. Nothing to convert first.

Word: paste from PowerPoint (Home > Paste > Keep Source Formatting) and the
shapes arrive as shapes. Or Insert > Pictures for the SVG, then right-click >
Graphics Format > Convert to Shape — but convert a copy, because that cannot
be undone after saving.

Inkscape or Illustrator: open the SVG, ungroup, edit, save.

If the drawing needs a real change rather than a label tweak, change the
Python and re-run it: the manuscript PNG comes from make_schematics.py, so
edits made in PowerPoint do not travel back into the book.

A note on the conversion
------------------------
src/mpl_to_pptx.py walks the matplotlib figure itself — its patches, lines and
labels — and re-emits each one as a PowerPoint shape, rather than tracing a
picture. That is why the PowerPoint stays faithful to the drawing when the
drawing changes: re-run the two scripts and both come out of the same source.
src/preview_pptx.py reads the saved .pptx back and re-plots it, which is how
the file was checked without PowerPoint.
