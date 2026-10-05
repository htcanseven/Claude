# Draft: pre-submission enquiry to the guest editors

To be sent by the author (not sent). Suggested recipient: one guest editor whose work is closest, e.g.
Prof. Yaoyao Fiona Zhao (McGill; transferability and reproducibility of ML in manufacturing) or Prof. David Rosen
(A*STAR; ML for process selection and DFM). Keep it to one screen.

---

**Subject:** Pre-submission enquiry – Research in Engineering Design, special collection "AI in Design for Manufacturing"

Dear Professor Zhao,

I am preparing a manuscript for the special collection *AI in Design for Manufacturing* and would be grateful
for a brief indication of whether it falls within its scope before I submit it in December.

**Working title:** Evaluating design-stage manufacturability decisions against the resolution of production

**Summary.** Design-stage manufacturability decisions increasingly rest on simulation and machine learning, but
whether a prediction is fit to decide is rarely evaluated against production. The paper proposes a framework whose
unit is set by production, the production floor: the difference that drift and scatter produce between two batches
of one design within a run. A rule that returns meets, fails or send to trial is characterised by a decisive distance
(beyond which 95 % of its verdicts are correct) and a safe distance (beyond which at most 5 % are wrong), evaluated
for each relation of a new design to the produced evidence: a variant of a produced setting, a new process setting
or a new design family. A procedure turns them into a guard band on the margin of a single verdict. Thirteen rules,
from the nominal simulation to Gaussian-process and gradient-boosting models and a nearest-produced-setting
baseline, each calibrated rule also without the simulation, are compared at a 95 % conformance level. The data are
open: 18 deep-drawn design–process alternatives of 500 parts each, mostly process settings on one tool, with matched
finite-element simulations (University of Stuttgart, RDDAC/DDACS). With a produced sibling the nearest produced
setting decided within 3.4 floors, for a new process setting no rule decided closer than 8.5 floors, and in two
transfers to a new family no rule was safe closer than 16 floors. Within a family the choice of rule mattered at
least as much as the relation. In this small-data regime the simulation, as used, helped only across families, and
learned models added abstention rather than accuracy.

**Fit to the collection.** It addresses learning from design and manufacturing data, automated manufacturability
assessment with stated confidence, knowledge transfer across design families, and designer trust (the "send to
trial" verdict). The contribution is a framework for evaluating design-stage decisions, with a six-step procedure,
demonstrated on open data with fully reproducible code.

Would a paper of this kind be welcome in the collection? Any guidance on emphasis would be much appreciated.

Kind regards,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
