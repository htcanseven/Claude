Figure 1.2 — geared train and integrated direct drive, in editable form
=======================================================================

Figure_1_2.svg      Vector, and the one to edit. Every label is real text, not
                    outlines, so it can be retyped. The font stack asks for
                    Times New Roman first, with DejaVu Serif as the fallback the
                    layout was set in; if a label reflows after a font change,
                    nudge it rather than resizing the drawing.

Figure_1_2.pdf      Same drawing as vector PDF, for Illustrator or for LaTeX.

Figure_1_2_source.py  The drawing itself, as the matplotlib script that produced
                    it. This is the real master: every coordinate is a number
                    you can change, and re-running it regenerates the PNG, SVG
                    and PDF together, so they never drift apart.
                    Run from the chapter1 directory:  python3 src/make_schematics.py

How to edit
-----------
Inkscape or Illustrator: open the SVG, ungroup, edit, save.

Word: Insert > Pictures for the SVG, then right-click > Graphics Format >
Convert to Shape. Word turns it into native shapes you can move and retype.
Convert a copy, not the original, because the conversion cannot be undone
after saving.

PowerPoint behaves the same way, and is often the easier place to rearrange
labels before pasting the result back into Word.

If the drawing needs a real change rather than a label tweak, change the
Python and re-run it. Hand-edits to the SVG are lost the next time the script
runs.
