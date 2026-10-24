# Cover letter

*For the submission to the Journal of Intelligent Manufacturing. Replace the bracketed DOI before sending.*

To the Editors-in-Chief, Journal of Intelligent Manufacturing

Dear Editors,

Please consider the enclosed manuscript, "When can a prediction replace a physical trial? A production-referenced
evaluation of design-stage decision rules in deep drawing", for publication as a research article in the Journal of
Intelligent Manufacturing. The manuscript has 31 pages, including the declarations and the references, and no
appendix. Online Resource 1 (16 pages) holds the tables behind statements of the paper; the archived results hold
everything else.

**The problem.** Simulation and machine learning increasingly inform manufacturability decisions: learned
manufacturability checks, surrogates of process simulations, predictive-quality models and virtual metrology. Such
models are judged by their prediction error on held-out data. That does not tell a team whether a prediction can be
relied on to decide, that is, to release a design or a process setting without a physical trial.

**The contribution.** The manuscript proposes a production-referenced evaluation of design-stage decision rules. Its
unit, the within-run floor, is the difference that drift and scatter of production and measurement produce between
two batches of one design within a run. A rule that returns *meets*, *fails* or *trial* is characterised, for each
relation of a new design to the produced evidence (a produced sibling, a new process setting, a new family), by two
points on its operating characteristic:

- a decisive distance, beyond which at least 95 % of its verdicts are correct;
- a safe distance, beyond which at most 5 % are wrong.

A procedure turns them into a guard band for single verdicts, estimated from the evidence a team has when it decides
and validated out of sample, and prices the verdicts by the costs of errors and trials. Any predictor can be scored this way; the scoring
is released as a small function, and a proposed reporting checklist closes the paper.

**The evidence.** The application is exploratory: one laboratory deep-drawing process, 18 design–process alternatives
of 500 scanned parts, each produced in one run, and a generic simulation dataset that was not calibrated to the
process. Simulation-based, learned and production-record rules are compared, every calibrated rule with and without
the simulation, among them Gaussian processes, a trend Gaussian process specified for six to nine produced
alternatives, an autoregressive multi-fidelity model, a calibration with a discrepancy term and gradient boosting.
The main observations:

- **The attainable distance grows with the novelty of the design.** The nearest produced setting, one rule applied
  to every relation, decided at 3.4 floors with a produced sibling (1.6 when the produced siblings did not differ
  resolvably, 4.4 when they did) and at 8.5 floors for a new process setting. For a new family only rules using the
  simulation decided, none closer than 30 floors.
- **What learning contributes with little production data.** No simulation-based or learned rule was more decisive
  than the production record within a family; the learners reduced to it. What made the record safe for new settings
  was evidence borrowed from the other family on the same relation, not learning; such intervals carry no coverage
  guarantee, and the paper reports their coverage per family and characteristic.
- **Release-level decisions need replicated runs.** A limit at a performance index of 1.33 lay inside every attainable
  distance except, marginally, that of a near-replicate sibling, and confirming the index needed replicated runs,
  which neither a prediction nor a short trial replaced once runs differed by a floor or more.

**Why this journal.** For readers who develop and deploy AI in manufacturing, the paper offers a way to show where a
learned model can be trusted to decide and where production evidence or a trial is still needed: against a
production-record baseline, by evidence relation, and in a unit that production defines. It complements the
journal's work on predictive quality, virtual metrology and datasets for manufacturability assessment.

**Data, code and declarations.** All data are public. The code, the extracted feature tables and the result files
that reproduce every number are archived on Zenodo (version 3, doi:[DOI to be inserted after deposit]), with a data
dictionary of the result files. The
manuscript has not been published and is not under consideration elsewhere. The use of a large language model,
including simulated reviews of earlier versions that led to rules and analyses being added, is documented in
Section 4.5, in Online Resource 1 and in the declarations.

Yours sincerely,

Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
