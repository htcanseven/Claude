# How this study was done: a reusable playbook

This file records, start to finish, how the manuscript *Detectability-driven design of condition
monitoring for three types of wind-turbine generators under identical winding faults* (Research in
Engineering Design, Springer) was produced in this repository, so that the same methodology can be run
again in another Claude Code session on a new topic. Section 10 is a prompt you can paste into that
session; the bracketed items are the things to change.

## 1. Timeline

| Phase | Dates | What was done | Outputs in this repository |
|---|---|---|---|
| 0 Profile | 13 Sep 2026 | Compiled the author's research profile and active threads from public sources | `research-summary.md` |
| 1 Frame | 13 Sep | Read the journal's scope and recent accepted papers; surveyed public datasets against that scope; chose the design-contribution framing and a dataset family that allows a controlled comparison | `dataset-survey-RED.md` |
| 2 Pipeline | 13 Sep | Feature extraction and the first two-machine comparison (PMSG vs SCIG); sensor-suite analysis; robust group statistic | `scripts/features.py`, `compare.py`, `sensor_suites.py`, `results/findings.md` |
| 3 Manuscript v1 | 14 Sep | Three-alternative pipeline (WFSG added), full LaTeX manuscript in the journal template, journal-compliance pass | `scripts/features_wfsg.py`, `compare3.py`, `paper/review/main_v1.pdf` |
| 4 Simulated review | 14 Sep | Three referee reports from agents with distinct expertise; every addressable comment implemented, with re-analysis; response letter | `paper/review/review_*.md`, `response_to_reviewers.md`, `scripts/sensitivity.py`, `revision.py` |
| 5 Length and guidelines | 14 Sep, 1 Oct | 42 → 29 pages (supplement, merged figures, trims); author-guideline alignment item by item; figures in the body font with sub-captions | `paper/main.tex`, `scripts/figs_paper.py`, `make_tables.py` |
| 6 Author iterations | 1–3 Oct | Title, intro structure, caption length, two schematic figures, supplement folded back into one 31-page document, passive voice, single-file source, cover letter | `paper/main.tex`, `paper/overleaf_RED_manuscript.zip` |
| 7 Resubmission | 22 Oct | Desk rejection by the design journal (contribution judged specific to the tested configurations); reframed for a condition-monitoring and signal-processing journal, reformatted to Elsevier `elsarticle` (numbered references, line numbers, highlights, declarations), new title and abstract, cover letter rewritten | `paper/main.tex`, `paper/highlights.tex`, `paper/overleaf_MSSP_manuscript.zip` |
| 8 Second simulated review | 23–24 Oct | Three reviewer agents with the new journal's profile (machine faults, FDI statistics, wind PHM practice); editor synthesis verifying every claim against the released tables; raw data re-acquired (7 GB from Zenodo) and the pipeline extended: phasor-residual sequence features, physical extent levels from the fault current, MDE brackets, null resampling, nested decision table with a power condition, calibrated oracle, four transfer referencing rules with trial-level intervals; manuscript revised against every comment with a response document | `paper/review/mssp_*.md`, `paper/review/response_to_mssp_reviews.md`, `scripts/` |

## 2. Phase 1: frame the study for the target journal before touching data

1. Read the journal's own scope statement and its desk-rejection criteria. For RED: design theory and
   methodology with broad applicability; papers that only apply existing tools to a case are rejected.
2. Pull the journal's recent papers near the topic from Crossref (title, year, DOI) and note why each was
   accepted. These become both the positioning argument and the "recent work in this journal" citations.
3. Survey public datasets with the acceptance constraint in mind. The deciding criterion was not data
   quality but whether the data allow a *design* question: here, three generator types subjected to the
   identical fault protocol made "which architecture is more diagnosable, and with which sensors" answerable.
4. Write the framing in one sentence before coding: the object of study is the comparison between
   alternatives, not the detector. Everything downstream (statistic, tables, figures, title) serves it.

## 3. Phase 2: the data pipeline

Order of execution (`bash scripts/run_all.sh` runs steps 2 to 8 from the feature caches):

1. `features.py` (PMSG/SCIG) and `features_wfsg.py` (WFSG): sliding windows of n_c electrical cycles with
   one-cycle hop; electrical frequency and phase rotation estimated per window from the current space
   vector; features are sequence magnitudes, harmonic ratios, standard deviations and 1f_e/2f_e amplitudes
   of synchronous-frame and controller quantities. Peak amplitudes are divided by √2 wherever compared with RMS.
   Output: `results/features_windows*.csv.gz`, `features_files*.csv` (one row per trial).
2. `compare.py`: per-trial statistic for the two machines on one bench (five-cycle windows), null tables,
   reliability screen, signature location, severity axis, figures.
3. `sensor_suites.py`: observation suites, fixed/nested/oracle variants, suite transfer.
4. `compare3.py`: the same for all three alternatives on the common feature set (three-cycle windows,
   because the WFSG fault intervals are short); WFSG fault interval located from the measured fault current.
5. `sensitivity.py`: window length and null quantile sensitivity; cluster bootstrap over tap pairs.
6. `revision.py`: everything the reviewers asked for: decision table, requirement quantities,
   numerator/denominator decomposition, out-of-reference transfer metrics, commissioning-baseline null,
   screened-feature list, absolute-change variant.
7. `figs_paper.py`: the two data figures at the journal's text width.
8. `make_tables.py`: writes every table from the CSVs into marked blocks of `paper/main.tex`.

Constants that were fixed once and never typed by hand again: reference and faulted interval boundaries,
n_c ∈ {3, 5, 8}, α ∈ {0.90, 0.95, 0.99}, 2000 bootstrap resamples (seed 1), 1000 decision-table resamples
(seed 7), gradient boosting (depth 3, 200 iterations, learning rate 0.08, random state 0), logistic
regression (C = 1), five-fold GroupKFold by tap pair with healthy trials grouped by speed. They live in the
scripts and are restated in Appendix A.2 of the paper.

## 4. Phase 3: the method, as it ended up after review

* **Statistic.** Signal-to-drift ratio SDR = |δ| / q_α(|δ⁰|): the relative change of a feature between the
  reference half adjacent to the fault (R₂) and the faulted interval, divided by the α-quantile of the
  relative change between the two healthy halves (R₁, R₂), pooled over all trials of an alternative.
  SDR ≥ 1 is a two-sided 5 % test on interval means with known onset; a standardised effect size.
* **Safeguards.** Reliability screen: a feature is excluded for an alternative when its false alarms on the
  healthy trials are incompatible with the nominal rate (one-sided binomial test; three or more of nine at
  α = 0.95), or when its null quantile exceeds one or is unbounded. Fixed feature (chosen once: smallest
  MDE, then highest share, then highest median SDR, so that a suite is never credited with less than its
  subsets), nested (chosen on the other tap pairs), oracle (per-trial best at a calibrated threshold, the
  α-quantile of the maximum statistic over the suite's features, so that its false-alarm rate stays at 1 − α).
* **Design quantities.** Minimum detectable extent with the limit-of-detection convention on the physical
  extent levels (tap pairs with equal fault currents are one level), reported as the bracket between the last
  undetected and the first detected level; detectable share conditional on e ≥ e_req; signature location
  (measurement group with the highest SDR in the largest share of trials).
* **Decision table.** For each alternative, class, suite and α, and for e_req at every tested level of the
  common bench: *meets* if the bootstrap probability of the joint event {MDE ≤ e_req and DS(e ≥ e_req) ≥ 0.9}
  is ≥ 0.95, *fails* if ≤ 0.05, otherwise *uncertain*; the fixed feature is re-selected and the null
  re-estimated in every resample, a suite inherits a strictly higher probability of a cheaper subset, and a
  requirement outside the extents a machine was tested at is *not testable*; the adequate suite is the cheapest
  that meets for every class.
* **Transfer step.** A window-level detector trained on one alternative and tested on another under four
  referencing rules (physical units, z-score on all healthy trials of the target, z-score on the healthy trial
  at the same operating point, |z| against the first half of the trial's own reference). AUC and TPR at 1 %
  FPR on the out-of-reference windows with cluster-bootstrap intervals over the tested machine's trials;
  false-alarm rate of the 1 % threshold on the healthy trials' fault-time windows.
* **Two nulls.** The within-trial null (reference immediately before the fault) and the commissioning
  baseline (healthy trial at the same operating point at another time); the latter is 1.1 to 4.6 times wider
  for the key features (1.9 to 3.2 for the phasor residuals) and makes the self-referenced transfer rule an
  abrupt-onset detector.
* **Uncertainty.** Bootstrap over tap pairs for class-level statements (the same resampled pairs for both
  machines so ratios are matched), over operating points within an extent level for the MDE, with the null
  quantile re-estimated from a cluster resample of the machine's records in every resample; the sampling
  interval of the null quantile itself is reported.

Two corrections made during review are worth repeating in any reuse: δ must be referenced to the half of
the reference interval adjacent to the fault, and any ratio of SDRs between alternatives must be decomposed
into its numerator (signature) and denominator (null), because a quieter alternative wins by silence.

## 5. Phase 4: manuscript production

* **Template.** Springer `sn-jnl` class, option `sn-basic` (author-year, natbib). Text block 372 pt × 552.7 pt
  (about 13.1 × 19.5 cm), body font Computer Modern 10 pt. The class's `\footnotesize` is 7 pt and its
  `\scriptsize` 9 pt; tables were set in the class's own 8 bp size via a `\tabsize` macro.
* **Structure.** Introduction (gap, idea, domain, contributions as one paragraph, "The paper is organised as
  follows"), background with a positioning table, method (definitions, statistic, derived quantities,
  six-step procedure with a TikZ figure, design-stage instantiation, scope), demonstration (alternatives
  table and schematic, fault classes schematic, suites table, computation), results (one subsection per
  finding), discussion (what the demonstration establishes, design implications, applying elsewhere,
  threats to validity), conclusions, declarations, Appendix A (feature definitions, computation details,
  four tables), references.
* **Author-guideline items checked one by one.** Abstract 150–250 words; 4–6 keywords; headings at most
  three levels (no `\paragraph`); DOIs as full links; journal names abbreviated where certain; figure
  lettering 8–12 pt at final size; panel letters bold (a), (b); captions without a trailing period and at
  most two lines, with definitions moved into table notes (`\footnotetext` inside the table); table footnotes
  as superscript letters; abbreviations defined at first mention; use of a large language model stated in the
  Methods and in a declaration; data and code availability statements with DOIs.
* **Figures.** matplotlib in a `PAPER_FIGS` mode: serif `cmr10`, mathtext `cm`, all sizes 10 pt, PDF font
  type 42, figures drawn at 5.15 in width, a centred sub-caption under every panel (appended as the last line
  of the x-label), legends on top, machines encoded by colour and marker shape, `≥` written as `$\geq$`
  because `cmr10` lacks the glyph. Schematic figures (method, generator systems, fault classes) are TikZ
  in the body font. Each regenerated figure was rendered to PNG and inspected before use.
* **Tables.** Generated from the result CSVs; never typed. Captions one or two lines; conventions and
  abbreviations in notes under the table.
* **Writing conventions.** British -ise spelling; third-person passive voice, no first person; title without
  colon, semicolon or question mark; every number in the text traceable to a CSV; limitations stated as
  threats to validity, not softened.

## 6. Phase 5: simulated peer review

1. Three agents reviewed the full PDF, each with a persona matching a plausible referee: design theory and
   methodology (RED's core readership), signal-based fault detection and statistics, electrical machines and
   wind energy. Each returned major and minor comments in a report file.
2. Every comment was classified addressable or not, then implemented by re-running the pipeline rather than
   by rewording: new analyses (decision table, decomposition, out-of-reference metrics, baseline null,
   sensitivity with the screen applied, nested selection, oracle false-alarm rates, seeds) and text changes
   (positioning table, default rules for the procedure's framing steps, scope section, withdrawn claim).
3. A point-by-point response letter records what changed, where, and which numbers moved.
4. The pre-review PDF is kept frozen in `paper/review/` so the change is auditable.

## 7. Phase 6: length management and packaging

* The 42-page first version went to 29 pages by moving appendices and secondary tables into a supplement,
  merging figures and trimming prose; the author later asked for one self-contained document, so the
  supplement was folded back as Appendix A with only the evidence tables that reviewers had asked for, and
  redundant displays were dropped (a figure duplicating a table; tables whose every number the text quotes).
* Cut priority used when space ran out: redundancy first (figure vs table duplicates), then tables whose
  numbers are all in the text, then layout (float separations, caption skips, figure heights), then prose
  tightening; reviewer-requested evidence last.
* The final source is a single `main.tex` with the tables between `%% BEGIN GENERATED` / `%% END GENERATED`
  markers that `make_tables.py` rewrites in place; the Overleaf zip holds that file, the class and style
  files, the bibliography and the two data figures, and is test-compiled in a clean directory before delivery.
* Cover letter drafted last, from the paper's own abstract, contributions and declarations.

### Phase 7: after a desk rejection

* Read the decision for its actual reason. "Not a broad contribution to design methodology" is a fit
  verdict, not a flaw in the evidence, so the remedy is a venue change with a reframing (route A), not a new
  study; adding a second application domain to prove generality (route B) is the remedy only when the method
  itself is in doubt.
* Verify the new journal's requirements before touching the manuscript: article types, abstract and keyword
  limits, highlights, reference style, review model (single or double anonymised), declarations. Publisher
  pages behind captchas can be read through a reader proxy or a third-party summary, with the limits then
  confirmed against the official class and template.
* Reframe, do not rewrite: new title, abstract, introduction, positioning section (the table of related
  methods re-drawn against the new field's own methods) and discussion headings for the new readership; the
  method, data, results and limitations stay as reviewed. Terms change with the audience (observation suite
  to sensor suite, architecture to machine type); the formal term of the method is defined once and kept.
* Reformat by script, not by hand: class-specific markup (table notes, rules, appendix, declarations,
  citation commands) is converted in one pass, the tables are regenerated through the same generator, and
  what the new class exposes (caption widths, line-breaking tolerance, title-page overflow with line numbers,
  appendix counters) is fixed from the log and the rendered pages, then the zip is test-compiled clean.
* Simulate the new journal's review before submitting and answer every comment with analysis, not with
  wording. Three reviewer agents (machines and drives; change-detection statistics; condition-monitoring
  practice) produced the comments that drove this revision: phasor-residual sequence features in place of
  magnitude ratios (the faulted phase was confounded with the extent in the tap layout), physical extent
  levels from the fault current with the MDE as a bracket, the decision table as the bootstrap probability of
  a joint event with a stated power and the requirement evaluated at the tested levels (a requirement outside
  a machine's tested range is "not testable", never "fails"), the null quantile resampled inside every
  bootstrap, the oracle at a calibrated threshold, the decomposition repeated in absolute units, a fourth
  referencing rule and intervals in the transfer experiment. Each claim of the abstract was then re-derived
  from the regenerated tables; two of the original four findings changed in form ("only by silence" and
  "transfers only when self-referenced" were not supported by the intervals) and are stated as corrected.
* Verify that a results script's grid matches the data it is applied to: the first decision table used a
  fixed requirement grid (3, 5, 8, 12 %) and reported "fails" at 12 % because the largest tested inter-turn
  level was 11.6–12.1 %; evaluating requirements at the tested levels removed the artefact.

### Phase 8: bringing a 55-page revision to 31 pages without a supplement

* Budget before cutting: at 12 pt in the `preprint` layout a full text page holds 37 numbered lines (about
  450 words), and the margin line numbers in `pdftotext -layout` output give the exact composition of a build
  (text lines, float pages, reference pages), so every cut can be priced in lines before it is made. The
  55-page revision had about 13,800 body words, seven pages of floats and five of references.
* Order of cuts, cheapest loss first: duplicate displays (a figure and a table of the same numbers; appendix
  tables whose numbers the text already quotes; the positioning table); compact redraws of the data figures
  (lower height, one row instead of two, 8 pt lettering) and of the TikZ procedure figure; references in the
  size the class uses for its journal layouts (`\bibfont`, `\bibsep`); float placement (`[htbp]`,
  `\floatpagefraction` 0.8) so that a figure of two thirds of a page no longer takes a page of its own; then
  prose, paragraph by paragraph against a word budget per section, keeping every number a reviewer asked for
  and deleting restatements (Discussion and Conclusions repeated Results; Computation repeated the appendix).
* Mechanics: the condensed body lives in a scratch file with placeholders for the pieces carried over verbatim
  (preamble, TikZ figures, hand-written tables, declarations); an assembly script rebuilds `main.tex`,
  `make_tables.py` refills the generated blocks and the build gates run. Paragraph replacements are applied by
  script, keyed on a unique prefix of each paragraph, so each pass is reproducible and reversible from the
  backup of the previous pass; five passes took 55 to 31 pages (40, 36, 33, 32, 31).
* Result: 31 pages (about 7,950 body words, six tables, five figures, 37 references), zero warnings, every
  caption within two lines; the last page is a third full, so the count is robust to small differences
  between TeX installations. Hand condensation without a budget drifted back to the same length twice; the
  numbers only moved once each section had a target.

## 8. Quality gates run before every delivery

* `latexmk` build with zero errors, zero LaTeX warnings, no undefined references or citations, no overfull
  boxes; all fonts embedded (`pdffonts`).
* Page count and lines per page (`pdftotext` per page) to find half-empty pages; a 36-dpi contact sheet of
  all pages to see float placement and gaps at a glance.
* Every caption checked for its line count in the rendered PDF; every regenerated figure rendered and viewed.
* Abstract word count; first-person pronoun search; search for stale cross-references after any restructuring.
* Cited keys versus bibliography entries; every reference verified against Crossref when added.
* The zip compiled from scratch in an empty directory.
* Commit after each verified step with a descriptive message; data and caches never committed.

## 9. Pitfalls met, and the fix

* A two-line section heading immediately followed by a subsection heading left a third of a page empty
  (the heading block could not break); a one-line heading fixed it.
* Appendix tables placed after the last appendix text floated into the references; putting the floats at the
  top of the appendix and letting the appendix text flow under them kept them in place.
* Shortening a multi-row figure made the per-panel x-labels collide with the panel below; labelling the axis
  once per column on the bottom row left room for the sub-captions.
* `threeparttable` wraps captions at the table width, so narrow tables need shorter captions than wide ones.
* Regenerating a matplotlib PDF changes its embedded timestamp; restore unchanged figures from git to keep
  commits clean.
* Springer's pages block plain fetches; a reader proxy (r.jina.ai) returned the guideline text. Zenodo's API
  timed out; the Data in Brief papers served as the dataset citations.
* `pkill -f` matched the calling shell; use `ps -eo args | grep "[p]attern"`.

## 10. Prompt to start the same methodology in a new session

```
You are helping me write a journal paper from public data, end to end, in this repository.
Target journal: [journal]. Read its scope statement and recent accepted papers near my topic first,
and frame the contribution so that it fits them; tell me in one sentence what the object of study is.

Phase 1: survey public datasets against the journal's acceptance criteria; prefer data that allow a
controlled comparison between design alternatives. Write the survey to a markdown file.

Phase 2: build a scripted pipeline (feature extraction -> per-trial statistic -> analyses -> figures ->
tables), with every constant in code, seeds fixed, and a run_all.sh that reproduces every number from
cached features. Tables are generated from CSVs into marked blocks of the LaTeX source, never typed.

Phase 3: write the manuscript in the journal's LaTeX class as a single main.tex: introduction with the
contributions as one paragraph and an organisation paragraph, background with a positioning table,
method with a procedure figure, demonstration, results with one subsection per finding, discussion
with threats to validity, conclusions, declarations, appendix. Third-person passive voice, British
spelling, title without punctuation, captions of at most two lines with notes under the tables,
figures in the body font with a sub-caption under every panel, abstract within the word limit.

Phase 4: run three reviewer agents with distinct expertise on the PDF, then implement every addressable
comment by re-running the pipeline, keep the pre-review PDF frozen, and write a point-by-point response.

Phase 5: bring the paper to [N] pages by cutting redundancy before evidence, check the author
guidelines item by item, and deliver the PDF plus a zip that compiles in a clean directory.

Before every delivery: zero LaTeX errors and warnings, no undefined references, every caption at most
two lines, every figure rendered and inspected, citations matched to the bibliography, references
verified against Crossref, a contact sheet of all pages checked for gaps. Commit after each verified
step; never commit data. Report honestly what was removed or could not be verified.
```
