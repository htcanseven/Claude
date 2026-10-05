# Draft cover letter

To the Editors-in-Chief and the Guest Editors of the special collection *AI in Design for Manufacturing*,
Research in Engineering Design

Dear Editors,

Please find enclosed the manuscript "Qualifying design-stage manufacturability decisions with production evidence",
submitted to the special collection *AI in Design for Manufacturing*.

Design-stage manufacturability decisions increasingly rest on simulation and machine learning, yet whether a
prediction can be trusted to decide is a property of production that design research rarely measures. The
manuscript proposes a method that scores such decisions against production. It defines the production floor – the
difference that drift and scatter produce between two batches of one design – as the unit of design decisions, and
characterises any decision rule that returns *meets*, *fails* or *send to trial* by two distances: a decisive
distance, beyond which 95 % of its verdicts are correct, and a safe distance, beyond which at most 5 % are wrong.
A calibration budget and a calibration design state how many, and which, produced variants of a design family a
rule needs before its verdicts become reliable, and an applicability guard sends designs outside the calibrated
family to trial. The method is summarised as a six-step procedure.

The demonstration uses open data of unusual depth: 9,000 deep-drawn and cut parts of 18 design–process
alternatives, each produced as a series of 500 parts, with matched finite-element simulations. Each alternative is
judged as a new design. The findings bear directly on the questions the collection raises about learning from
historical design and manufacturing data: a Gaussian-process calibration of the simulation on the production record
of a design family decides correctly within 7 floors; four to five produced variants that bracket a new design make
calibrated decisions reliable; and across design families no rule is safe closer than 20 floors, while models
without the simulation fail – the simulation carries a decision into a new family, and learning carries production
evidence within it. Against general tolerances, the best rule decides 89 % of 162 design questions correctly
without a false accept.

The contribution is methodological: a definition, a decision procedure and design guidelines, with the case as a
demonstration rather than the object of the paper. All data are public, and the released code reproduces every
number from them. The manuscript has not been published or submitted elsewhere. The use of a large language model
as an assistant is declared in the manuscript.

Yours sincerely,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
