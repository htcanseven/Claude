# Draft cover letter

To the Editors-in-Chief and the Guest Editors of the special collection *AI in Design for Manufacturing*,
Research in Engineering Design

Dear Editors,

Please find enclosed the manuscript "Evaluating design-stage manufacturability decisions against the resolution of
production", submitted to the special collection *AI in Design for Manufacturing*. The manuscript is a single
file of 30 pages, including its appendix and references, with no supplementary material.

Design-stage manufacturability decisions increasingly rest on simulation and machine learning. Yet whether a
prediction is fit to decide is rarely evaluated against production. The manuscript proposes a framework whose unit is
set by production: the production floor, the difference that drift and scatter produce between two batches of one
design within a run. A rule that returns *meets*, *fails* or *trial* is characterised by two operating
characteristics in floors:

- a decisive distance, beyond which at least 95 % of its verdicts are correct;
- a safe distance, beyond which at most 5 % are wrong.

Both are evaluated separately for each relation of a new design to the produced evidence: a variant of a produced
setting, a new process setting, or a new family. A six-step procedure turns them into a guard band on the margin of a
single verdict, and the paper evaluates that decision rule itself.

The framework is evaluated on open data of unusual depth: 18 deep-drawn design–process alternatives, mostly process
settings on one tool, each produced as a series of 500 parts, with matched finite-element simulations. Thirteen
rules are compared at a 95 % conformance level, from the nominal simulation to Gaussian-process and
gradient-boosting models and a nearest-produced-setting baseline. Every calibrated rule is also evaluated without
the simulation. The main results are:

- **The best attainable distance grew with the novelty of the design.** With a produced sibling the nearest produced
  setting decided within 3.4 floors (0.17 mm of draw-in). For a new process setting no rule decided closer than
  8.5 floors. In two transfers to a new family no rule was safe closer than 16 floors.
- **Within a family the choice of rule mattered at least as much as the relation.** Requirements at the release
  level of series production, a performance index of 1.33, lay inside every decisive distance.
- **Simulation and learning, in this small-data regime.** The simulation, as used, helped only across families, and
  learned models added abstention rather than accuracy.

For the collection, the paper offers an evaluation standard for AI-based manufacturability support rather than a
verdict on machine learning in general. A learned model is compared with a production-record baseline and scored
by evidence relation, in a unit that production defines, and shown to its user with a guard band. A section on
reuse shows how classifiers and language-model checks can be scored in the same way, and which data the framework
needs in other processes.

All data are public, and the released code reproduces every number from them; a versioned archive is deposited on
Zenodo [DOI to be inserted]. The manuscript has not been published or submitted elsewhere. The use of a large
language model as an assistant is declared in the manuscript.

Yours sincerely,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
