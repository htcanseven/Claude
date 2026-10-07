# Cover letter

*For the submission to Research in Engineering Design. Replace the bracketed DOI before sending.*

To the Editor-in-Chief and the Guest Editors of the special collection *AI in Design for Manufacturing*,
Research in Engineering Design

Dear Editors,

Please find enclosed the manuscript "Evaluating design-stage manufacturability decisions against the resolution of
production", submitted to the special collection *AI in Design for Manufacturing*. The manuscript is a single file of
30 pages, including its appendix and references, with no supplementary material.

**The problem.** Design-stage manufacturability decisions increasingly rest on simulation and machine learning, yet
whether a prediction is fit to decide is rarely evaluated against production.

**The framework.** The manuscript proposes a framework whose unit is set by production: the production floor, the
difference that drift and scatter of production and measurement produce between two batches of one design within a
run. A rule that returns *meets*, *fails* or *trial* is characterised by two points on its operating characteristic,
in floors:

- a decisive distance, beyond which at least 95 % of its verdicts are correct;
- a safe distance, beyond which at most 5 % are wrong.

Both are evaluated separately for each relation of a new design to the produced evidence: a variant of a produced
setting, a new process setting, or a new family. A six-step procedure turns them into a guard band on the margin of a
single verdict, and the paper evaluates that decision rule itself.

**The evaluation.** It uses open data of unusual depth: 18 deep-drawn design–process alternatives, each produced as a
series of 500 parts, with matched finite-element simulations. Most of the alternatives are process settings on one
tool. Fourteen rules are compared at a 95 % conformance level, from the nominal simulation to Gaussian-process and
gradient-boosting models, with a nearest-produced-setting baseline and a linear force trend. Every calibrated rule is
also evaluated without the simulation. The main results are:

- **The best attainable distance grew with the novelty of the design.**
  - With a produced sibling, the nearest produced setting was right for requirements more than 3.4 floors from the
    truth (0.17 mm of draw-in): 0.85 floors for near-replicate siblings and 4.9 for resolvable ones.
  - For a new process setting, the nearest produced setting needed 4.7 floors interpolating and 4.9 extrapolating to
    500 kN. The force trend needed 8.9 floors extrapolating to 100 kN, where the stroke speed also changed.
  - In two transfers to a new family, the best rule was safe at 16–17 floors, in the floor of either family.
- **Within a family, the choice of rule mattered more than the relation.** Requirements at a process performance index
  of 1.33, the usual release level of series production, lay inside every decisive distance except that of a
  near-replicate sibling. They therefore need a trial unless a sibling has been produced.
- **Simulation and learning, in this small-data regime.** The simulation, as an offset or rescaled, helped only across
  families. Learned 90 % intervals covered 85–96 % of the truths with a produced sibling, but under 50 % when
  extrapolating or for a new family.

**Why it suits the collection.** The paper offers an evaluation standard for AI-based manufacturability support rather
than a verdict on machine learning in general. Under that standard, a learned model is:

- compared with a production-record baseline;
- scored by evidence relation, in a unit that production defines;
- shown to its user with a guard band.

A section on reuse shows how classifiers and language-model checks can be scored in the same way, and which data the
framework needs in other processes.

**Data, code and declarations.** All data are public. The code, the extracted feature tables and the result files that
reproduce every number are archived on Zenodo (version 4, doi:[DOI to be inserted after deposit]). The manuscript has
not been published or submitted elsewhere. The use of a large language model as an assistant is declared in the
manuscript.

Yours sincerely,

Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
