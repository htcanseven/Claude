# Manuscript: Detectability-driven design of condition monitoring (Research in Engineering Design)

## Build

```bash
cd paper
latexmk -pdf main.tex        # pdflatex + bibtex, three passes
```

Requires TeX Live with `sn-jnl.cls` (included here), natbib, booktabs, tikz, siunitx, manyfoot.

## Layout

The manuscript is a single file, `main.tex`: title page, abstract, Sections 1–7, declarations,
Appendix A and the bibliography call. The three schematic figures (method, generator systems,
fault classes) are TikZ code inside the file; the two data figures are `figures/*.pdf`.

| Path | Content |
|---|---|
| `main.tex` | the whole manuscript; the nine tables sit between `%% BEGIN GENERATED <name>` and `%% END GENERATED <name>` markers and are rewritten by `scripts/make_tables.py` from `results/tables/*.csv` (do not edit those blocks by hand) |
| `figures/*.pdf` | `G_sdr_by_feature_3alt.pdf` (Fig. 4) and `G_severity_combined.pdf` (Fig. 5), copied from `results/figures/` |
| `refs.bib` | references, Springer basic author-year style (`sn-basic` option of `sn-jnl`) |
| `sn-jnl.cls`, `sn-*.bst` | Springer Nature class and bibliography styles |
| `review/` | frozen pre-review PDF, reviewer reports, response to reviewers, change log |

## Regenerating tables and figures

```bash
bash scripts/run_all.sh     # compare, sensor_suites, compare3, sensitivity, revision, figs_paper, make_tables; copies figures
```

The individual steps are `compare.py` (PMSG/SCIG, five-cycle windows), `sensor_suites.py`, `compare3.py`
(three alternatives, three-cycle windows), `sensitivity.py` (window/quantile sensitivity, bootstrap),
`revision.py` (decision table, requirement quantities, decomposition, out-of-reference transfer metrics,
baseline null, screen list), `figs_paper.py` (manuscript figures at text width) and `make_tables.py`
(writes the table blocks of `main.tex`). Feature extraction from the raw public data is `features.py`
(PMSG/SCIG) and `features_wfsg.py` (WFSG); see their docstrings.

## Submission switches

* `\anontrue` in `main.tex` removes the author block for a blinded copy.
* Funding, ORCID and the final code DOI are entered in the editorial system; check the
  `Funding` and `Code availability` declarations before upload.
