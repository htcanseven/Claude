Figure 1.2 — geared train and integrated direct drive, in editable form
=======================================================================

These files are the house-style Figure 1.2 exactly as it stands in the
manuscript: 15.92 cm wide, every label Times New Roman 11 pt.

Figure_1_2.pptx     PowerPoint, and the easiest one to work in. No picture is
                    embedded: the drawing is about 230 native PowerPoint
                    shapes, one per part, so you can click a housing and
                    recolour it, drag a leader line, or retype a label
                    straight away. Each panel is its own group, "Figure 1.2
                    (a)" and "Figure 1.2 (b)", so a panel moves or scales as
                    one piece; double-click into a group to reach the parts.
                    Shapes are named for the selection pane
                    (Home > Select > Selection Pane).
                    The slide is the printed size of the figure, so the labels
                    are 11 pt as they will print.

Figure_1_2.svg      Vector, for Inkscape or Illustrator. Every label is real
                    text, not outlines, so it can be retyped. The font stack
                    asks for Times New Roman first, with Liberation Serif (the
                    same letter widths) as the fallback the layout was set in.

Figure_1_2.pdf      The same drawing as vector PDF, for Illustrator or LaTeX.

Figure_1_2.png      The picture that goes into the manuscript, 600 dpi.

The master is not here. It is the function geared_vs_directdrive() in
chapter1/src/ch1_figures.py, drawn with the house-style module
chapter1/src/hsbook_style.py. Every coordinate there is a number in
centimetres of the printed page. Run from the chapter1 directory:

    python3 src/ch1_figures.py 1.2      the manuscript figure, figures/ch1/fig_1_02.*
    python3 src/mpl_to_pptx.py          this folder: .pptx, .svg, .pdf, .png

How to edit
-----------
PowerPoint: open the .pptx and edit. Nothing to convert first.

Word: paste from PowerPoint (Home > Paste > Keep Source Formatting) and the
shapes arrive as shapes. Or Insert > Pictures for the SVG, then right-click >
Graphics Format > Convert to Shape. Convert a copy, because that cannot be
undone after saving.

Inkscape or Illustrator: open the SVG, ungroup, edit, save.

If the drawing needs a real change rather than a label tweak, change the
Python and run it again. The manuscript PNG comes from ch1_figures.py, so
edits made in PowerPoint do not travel back into the book.

A note on the conversion
------------------------
src/mpl_to_pptx.py walks the matplotlib figure itself, its patches, lines and
labels, and writes each one again as a PowerPoint shape rather than tracing a
picture. That is why the PowerPoint stays faithful when the drawing changes:
run the two scripts again and both come out of the same source.
src/preview_pptx.py reads the saved .pptx back and plots it again, which is
how the file was checked without PowerPoint.
