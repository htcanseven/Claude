# Cover letter

*For the submission to the Journal of Intelligent Manufacturing. Replace the bracketed DOI before sending.*

To the Editors-in-Chief, Journal of Intelligent Manufacturing

Dear Editors,

Please consider the enclosed manuscript, "Evaluating AI-based manufacturability decisions against the resolution of
production", for publication as a research article in the Journal of Intelligent Manufacturing. It is a single file of
30 pages, including its appendix and references, with no supplementary material.

**The problem.** AI increasingly informs manufacturability and quality decisions: learned manufacturability checks,
surrogates of process simulations, predictive-quality models and virtual metrology. Such models are judged by their
prediction error on held-out data. That does not tell a team whether a prediction can be relied on to decide, that
is, to release a design or a process setting without a physical trial.

**The contribution.** The manuscript proposes a production-referenced standard for evaluating such decisions. Its
unit, the production floor, is the difference that drift and scatter of production and measurement produce between
two batches of one design within a run. A rule that returns *meets*, *fails* or *trial* is characterised, for each
relation of a new design to the produced evidence, by two distances in floors:

- a decisive distance, beyond which at least 95 % of its verdicts are correct;
- a safe distance, beyond which at most 5 % are wrong.

A procedure turns them into a guard band for single verdicts. The standard applies to any predictor. A section on
reuse shows how classifiers and language-model checks are scored in the same way, and ends with a minimal reporting
checklist.

**The evidence.** The evaluation uses open data: 18 deep-drawn design–process alternatives of 500 scanned parts each,
with matched finite-element simulations. Fourteen rules are compared at a 95 % conformance level, among them the
nominal simulation, calibrated simulations, Gaussian processes, gradient boosting with jackknife+ intervals and
production-record baselines. Every calibrated rule is evaluated with and without the simulation. The main results:

- **The attainable distance grows with the novelty of the design.**
  - With a produced sibling, the nearest produced setting was right for requirements more than 3.4 floors from the
    truth (0.17 mm of draw-in): 0.85 floors for near-replicate siblings and 4.9 for resolvable ones.
  - For a new process setting, the nearest produced setting needed 4.7 floors interpolating and 4.9 extrapolating
    to 500 kN. A linear force trend needed 8.9 floors extrapolating to 100 kN, where the stroke speed also changed.
  - In two transfers to a new family, the best rule was safe at 16–17 floors.
- **Release-level requirements need trials.** Requirements at a process performance index of 1.33 lay inside every
  decisive distance except that of a near-replicate sibling.
- **What AI and simulation contribute with little production data.** The simulation, as an offset or rescaled,
  helped only across families. Learned 90 % intervals covered 85–96 % of the truths with a produced sibling, but
  under 50 % when extrapolating or for a new family.

**Why this journal.** For readers who develop and deploy AI in manufacturing, the paper offers a way to show where a
learned model can be trusted to decide and where production evidence or a trial is still needed: against a
production-record baseline, by evidence relation, and in a unit that production defines. It complements the
journal's work on predictive quality and on datasets for manufacturability assessment.

**Data, code and declarations.** All data are public. The code, the extracted feature tables and the result files
that reproduce every number are archived on Zenodo (version 1, doi:[DOI to be inserted after deposit]). The
manuscript has not been published and is not under consideration elsewhere. The use of a large language model as an
assistant is documented in Section 4.5 and in the declarations.

Yours sincerely,

Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
