# Fixes applied to the IEEE Access template assembly (access.tex)

Source: the `access.tex` assembled in the official IEEE Access template
(`\documentclass{ieeeaccess}`), which failed to compile.

## 1. Compile-breaking error (the reason it would not build)

**Unclosed `\caption{` brace** in the figure showing within-pair vs.
cross-partner transfer (`Fig3_within_vs_cross.png`, label
`fig:within_cross_transfer`, around line 1550):

```latex
\caption{Within-pair oracle detectability versus directional cross-partner
transfer. ... described in Section~\ref{subsec:statistical_analysis}.
\label{fig:within_cross_transfer}      % <- caption brace never closed
\end{figure}
```

The missing `}` makes TeX swallow the entire rest of the file while
scanning the caption argument, producing:

```
Runaway argument?
{Within-pair oracle detectability versus directional cross-partner tr\ETC.
! File ended while scanning use of \caption@xdblarg.
```

Fix: close the caption after the final sentence, before `\label`:
`...Section~\ref{subsec:statistical_analysis}.}`. This one character is the
entire compile failure.

## 2. Warnings fixed at the same time (not compile-blockers)

- `\section{Conclusion}` had no `\label{sec:conclusion}`, so the
  Introduction's roadmap reference printed `??`. Label added.
- `Appendix~\ref{app:condition}` is referenced three times (Introduction
  contributions, Introduction roadmap, Conclusion) but the appendix section
  was never copied into the file. The appendix ("Operating-Condition
  Reference Experiments", from `paper/manuscript/sections/99_appendix.tex`)
  was inserted after the Conclusion with its cross-references adapted to
  this file's label names (`subsec:physics_features`,
  `subsec:closed_set_results`).
- `\section*{Data Availability}` was empty; filled with the Mendeley Data
  DOI / CC BY 4.0 statement from `paper/manuscript/main.tex`.

## 3. Files the compile still needs next to access.tex

Not included here (use the originals from the Overleaf project):

- `ieeeaccess.cls` (+ `spotcolor` files) from the official template
- Figures: `Fig1_composition_graph.png`, `Fig2_cross_partner_matrix.png`,
  `Fig3_within_vs_cross.png`, `Fig4_preservation_polarity.png`,
  `Fig5_paired_protocol_differences.png`
- Author photos: `evin.png`, `Huseyin_Canseven.png`
- `references.bib` — a copy is provided in this folder
  (all `\cite` keys in access.tex resolve against it with zero BibTeX
  warnings).

Verified: with these fixes the file builds with `pdflatex -> bibtex ->
pdflatex -> pdflatex` to 20 pages, 0 errors, 0 undefined references.
