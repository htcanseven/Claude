# Revision kit — IET EPA submission

Everything from the pre-submission review (`analysis/08_iet_epa_presubmission_review.md`) that
can be done without the manuscript source, prepared and tested.

| File | What it is | Status |
|---|---|---|
| `figures/fig6_macro_f1.pdf` | Figure 6 regenerated with error-rate labels (vector, fonts embedded) | Ready — swap in |
| `figures/fig6_macro_f1.png` | Preview of the same | — |
| `references.bib` | All 24 references verified against Crossref; wrong years, missing data and name order fixed | Ready |
| `latex_changes.tex` | Every text change as LaTeX: abstract, Sections 2, 3, 5.1, 5.2, 5.4, Table 4, five captions, Acknowledgments | Compile-tested |
| `cover_letter_iet_epa.md` | Cover letter for submission | Ready |

Regenerate Figure 6 with `python3 tools/make_fig6.py revision/figures`.

## Reference corrections found by verification

| Ref | Problem in the submitted PDF | Corrected |
|---|---|---|
| [2] Bai et al. | No year, volume or pages | IEEE TEC **41**(2):1574–1584, **2026** |
| [4] Ehya et al. | Year 2021 | **2022** (vol. 69) |
| [6] Wu et al. | Names in family-first order ("Wu Yucai") | Yucai Wu, Qianqian Ma, Bochong Cai |
| [8] Bechara et al. | Year 2023 | **2024** (vol. 60, no. 1) |
| [10] Lui | Broken entry | PhD thesis, Newcastle University, 2018 ("Lui" is the repository spelling) |
| [13] Krüger et al. | Missing venue details | CBMag 2024, Goiânia, pp. 248–254 |
| [17] Frosini et al. | Year 2014 | **2015** (vol. 62) |
| [22] Gurusamy et al. | Year 2020 | **2021** (vol. 70) |

The double commas (",, and") in the submitted PDF come from the template's bibliography style,
not the entries: this `.bib` renders cleanly with a standard style. The style itself is fixed
when the changes are applied to the source.

## Still needs the manuscript source

Applying the changes, the Table 3/Table 4 layout fix, making Figure 5 full width, and fixing the
bibliography style all require the LaTeX project (Overleaf: *Menu → Download → Source*).

## Only the authors can provide

- **Grant number** for the Acknowledgments, and confirmation of the funder name
- **ORCID** — required for all IET journals
- **CNN implementation details** (architecture, window length, optimiser, learning rate, batch
  size, epochs, β, hyperparameter grids) — optional now, likely requested in review
- **Confirmation** that Figs. 1–3 are reproduced from [14] (the captions assume so)
- **APC funding** check with the LUT library
