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
whether a prediction is fit to decide is rarely evaluated against production. The paper proposes a framework that
expresses this fitness in a unit set by production, the production floor: the difference that drift and scatter
produce between two batches of one design. A rule that returns meets, fails or send to trial is characterised by a
decisive distance (beyond which 95 % of its verdicts are correct) and a safe distance (beyond which at most 5 % are
wrong), evaluated for each relation of a new design to the produced evidence: a variant of a produced setting, a
new process setting or a new design family. Twelve rules, from the nominal simulation to Gaussian-process and
gradient-boosting models, each calibrated rule also without the simulation, are compared on open data of 9,000
deep-drawn parts of 18 design–process alternatives with matched finite-element simulations (University of
Stuttgart, RDDAC/DDACS). The relation governed decision fitness more than the model did: with a produced sibling
the nearest produced setting decided within about 3 floors, for a new process setting no rule decided closer than
8.5 floors, and for a new family no rule was safe closer than 16 floors. The simulation contributed only to the new
family; learned models added calibrated abstention rather than accuracy.

**Fit to the collection.** It addresses learning from design and manufacturing data, automated manufacturability
assessment with stated confidence, knowledge transfer across design families, and designer trust (the "send to
trial" verdict). The contribution is a framework for evaluating design-stage decisions, with a six-step procedure,
demonstrated on open data with fully reproducible code.

Would a paper of this kind be welcome in the collection? Any guidance on emphasis would be much appreciated.

Kind regards,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
