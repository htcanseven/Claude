# Manuscript: A signal-to-drift ratio for quantifying winding-fault detectability and selecting condition monitoring across three wind-turbine generator types (Mechanical Systems and Signal Processing)

## Build

```bash
cd paper
latexmk -pdf main.tex        # pdflatex + bibtex, the passes latexmk needs (the class writes main.spl on the first run)
pdflatex highlights.tex      # the separate highlights file the editorial system asks for
```

Requires TeX Live with `elsarticle.cls` (the CTAN version is included here), natbib, booktabs, multirow,
threeparttable, array, tikz, lineno, hyperref and xurl.

## Layout

The manuscript is a single file, `main.tex`, in Elsevier's `elsarticle` class (`preprint,12pt`, single column,
line numbers, numbered references in order of citation): front matter (title, author, abstract, keywords),
Sections 1–7, the Elsevier declarations (CRediT, competing interest, funding, data availability,
acknowledgements) and the bibliography call; there is no appendix, the feature definitions and computation
details being in Sections 4.3 and 4.4. The three schematic
figures (procedure, generator systems, fault classes) are TikZ code inside the file; the positioning table (Table 1) and
the two description tables (Tables 2 and 3) are hand-written in the file; the four data figures are
`figures/*.pdf`. The manuscript is 38 pages in this layout (about 9,500 words of body text, three hand-written and
seven generated tables, seven figures, 46 references) and has no supplementary material.

| Path | Content |
|---|---|
| `main.tex` | the whole manuscript; the seven generated tables (Tables 4–10: MDE, sensor suites, decision table, decision cells, transfer, operating envelope, conventions) sit between `%% BEGIN GENERATED <name>` and `%% END GENERATED <name>` markers and are rewritten by `scripts/make_tables.py` from `results/tables/*.csv` (do not edit those blocks by hand) |
| `highlights.tex` | three to five highlights of at most 85 characters each (uploaded as a separate file at submission) |
| `figures/*.pdf` | `G_sdr_illustration.pdf` (Fig. 1), `G_sdr_by_feature_3alt_compact.pdf` (Fig. 5), `G_pairs_by_phase.pdf` (Fig. 6) and `G_pod.pdf` (Fig. 7), copied from `results/figures/`; the other PDFs there are pipeline outputs not used in the manuscript |
| `refs.bib` | references; `elsarticle-num-names.bst` prints them numbered, with the DOI as a link |
| `elsarticle.cls`, `elsarticle-num-names.bst` | Elsevier class and bibliography style (CTAN `elsarticle` bundle, LPPL) |
| `review/` | frozen pre-review PDF, the simulated MSSP reviewer reports (round 1 and round 2), the editor syntheses and the response document; the `review_*`/`response_to_reviewers.md` files are from the earlier submission cycle |

## Regenerating tables and figures

```bash
bash scripts/run_all.sh     # compare, sensor_suites, compare3, sensitivity, revision, revision_round2, revision_round3, figs_paper, make_tables; copies figures
```

The individual steps are `compare.py` (PMSG/SCIG, five-cycle windows; defines the SDR, the phasor-residual
features and the physical extent levels), `sensor_suites.py`, `compare3.py` (three alternatives, three-cycle
windows; MDE brackets, calibrated oracle, false-alarm counts), `sensitivity.py` (window/quantile sensitivity;
bootstrap with the null re-estimated per resample; null-quantile intervals), `revision.py` (decision tables with
nested feature selection and a power condition, requirement quantities, decomposition in relative and absolute
units, transfer with four referencing rules and cluster-bootstrap intervals, per-phase and per-tap-pair tables,
baseline null, screen list), `figs_paper.py` (manuscript figures at text width) and `make_tables.py` with
`make_tables_rev.py` (write the table blocks of `main.tex`, each as a `threeparttable` with its notes). Feature
extraction from the raw public data is `features.py` (PMSG/SCIG) and `features_wfsg.py` (WFSG); the raw data
are the three Zenodo release archives of the InnovaPower MitDev-Eletrica repository, unpacked so that
`data/mitdev/` holds `PMSG-3phase-Dataset`, `SCIG-3phase-Dataset` and `Generators-Dataset`.

## Submission notes

* Peer review at the target journal is single-anonymised, so the author block stays in the manuscript.
* The editorial system asks for the highlights, the cover letter, the declaration-of-interests form and the
  subject area ("Signal processing in machine/system health monitoring") separately. The manuscript carries no
  generative-AI declaration and no code-availability statement (removed at the author's request); the data
  availability paragraph names the three public datasets only.
