# Draft: pre-submission enquiry to the guest editors

To be sent by the author (not sent). Suggested recipient: one guest editor whose work is closest, e.g.
Prof. Yaoyao Fiona Zhao (McGill; transferability and reproducibility of ML in manufacturing) or Prof. David Rosen
(A*STAR; ML for process selection and DFM). Keep it to one screen.

---

**Subject:** Pre-submission enquiry – Research in Engineering Design, special collection "AI in Design for Manufacturing"

Dear Professor Zhao,

I am preparing a manuscript for the special collection *AI in Design for Manufacturing* and would be grateful
for a brief indication of whether it falls within its scope before I submit it in December.

**Working title:** Qualifying design-stage manufacturability decisions with production evidence

**Summary.** Design-stage manufacturability decisions increasingly rest on simulation and machine learning, but
whether a prediction can be trusted to decide is a property of production that is rarely measured. The paper
scores design-stage decisions (meets / fails / send to physical trial) against production. It defines a
production floor – the difference that drift and scatter produce between two batches of one design – as the unit,
and characterises each decision rule by a decisive distance (beyond which 95 % of its verdicts are correct) and a
safe distance (beyond which at most 5 % are wrong). Six rules – nominal simulation, conformal and
Gaussian-process calibration, and gradient-boosting models with and without the simulation – are compared on an
open dataset of 9,000 deep-drawn parts of 18 design–process alternatives with matched finite-element simulations
(University of Stuttgart, RDDAC/DDACS). A Gaussian-process calibration on the production record of a design family
decides correctly within 7 floors; four to five produced alternatives that bracket the new design's process
settings make calibrated rules reliable; across geometries no rule is safe closer than 20 floors, and an
applicability guard sends such designs to trial.

**Fit to the collection.** It addresses learning from historical design and manufacturing data, automated
manufacturability checks with stated confidence, knowledge transfer across design families, and designer trust
(the "send to trial" verdict). The contribution is a design-decision method with a six-step procedure, demonstrated
on open data with fully reproducible code.

Would a paper of this kind be welcome in the collection? Any guidance on emphasis would be much appreciated.

Kind regards,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
