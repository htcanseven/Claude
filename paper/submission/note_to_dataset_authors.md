# Draft: note to the RDDAC/DDACS authors

To be sent by the author (not sent). Dataset creators: Sebastian Baum and Pascal Heinzelmann (University of
Stuttgart). Their descriptor paper: Baum, Heinzelmann, Clauß, Liewald, Weyrich (2026) Statistical analysis of
simulation-to-reality deviation in deep drawing with a benchmark dataset, *Transactions of the Indian Institute of
Metals*, doi:10.1007/s12666-026-03870-5. Purpose: courtesy, domain checks, and avoiding duplicated work. Whether to
offer collaboration or co-authorship is the author's decision.

---

**Subject:** Research using the RDDAC and DDACS datasets – design-stage decisions qualified with production evidence

Dear Mr Baum, dear Mr Heinzelmann,

Thank you for publishing the RDDAC and DDACS datasets and your recent paper on the simulation-to-reality deviation
in deep drawing. I am preparing a paper for *Research in Engineering Design* that builds on both datasets with a
different question: how close to a requirement a design-stage decision made from simulation can be trusted, and how
much production evidence a design team needs before such decisions become reliable. The work defines a production
floor from batches of consecutive parts, scores six decision rules (nominal simulation, calibrated envelopes,
Gaussian-process and gradient-boosting corrections) by leaving each of the 18 alternatives out in turn, and derives
a calibration budget. All code and extracted feature tables are open, and the datasets and your paper are cited.

Three questions on which your knowledge of the experiments would help:

1. Are there drawing specifications or tolerances for the cups (wall angle, flange, bottom flatness, depth) that
   could replace the general-tolerance scenarios (ISO 2768) used in the paper?
2. How confident are you in the linear oil-to-friction mapping of the rddac package for within-series variation of
   the oil film? In the analysis the simulated friction sensitivity is 5 to 630 times the one inferred from the
   measured film.
3. Were any alternatives produced on more than one day or coil? That would allow a long-term production floor.

I would be glad to send you the manuscript before submission and to hear any comments.

Kind regards,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
