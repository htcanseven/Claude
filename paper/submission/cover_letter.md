# Draft cover letter

To the Editors-in-Chief and the Guest Editors of the special collection *AI in Design for Manufacturing*,
Research in Engineering Design

Dear Editors,

Please find enclosed the manuscript "Evaluating design-stage manufacturability decisions against the resolution of
production", submitted to the special collection *AI in Design for Manufacturing*.

Design-stage manufacturability decisions increasingly rest on simulation and machine learning, yet whether a
prediction is fit to decide is rarely evaluated against production. The manuscript proposes a framework that
expresses this fitness in a unit set by production, the production floor: the difference that drift and scatter
produce between two batches of one design. A rule that returns *meets*, *fails* or *trial* is characterised by two
operating characteristics in floors, a decisive distance beyond which at least 95 % of its verdicts are correct and
a safe distance beyond which at most 5 % are wrong. Both are evaluated separately for each relation of a new design
to the produced evidence: a variant of a produced process setting, a new process setting, or a new design family.
A calibration budget, an applicability guard and a six-step procedure turn the framework into a tool for design
teams.

The framework is evaluated on open data of unusual depth: 9,000 deep-drawn and cut parts of 18 design–process
alternatives, each produced as a series of 500 parts, with matched finite-element simulations. Twelve rules, from
the nominal simulation to Gaussian-process and gradient-boosting models, are compared, and every calibrated rule is
also evaluated without the simulation. The relation of the new design to the produced evidence governed decision
fitness more than the model did. With a produced sibling, the nearest produced setting decided within about
3 floors. For a new process setting no rule decided closer than 8.5 floors, and for a new family no rule was safe
closer than 16 floors. The simulation contributed only to the new family, and learned models matched the nearest
produced setting in accuracy while adding calibrated abstention where the produced alternatives resembled the new
design.

The findings bear directly on the questions the collection raises about learning from design and manufacturing
data, about trust in automated manufacturability assessment and about transfer between design families. They also
give the evaluation of AI-based DFM support a production-referenced standard: a learned model is compared with a
production-record baseline and scored by evidence relation, in a unit that production defines.

All data are public, and the released code reproduces every number from them. The manuscript has not been
published or submitted elsewhere. The use of a large language model as an assistant is declared in the manuscript.

Yours sincerely,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
