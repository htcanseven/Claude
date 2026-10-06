# Draft: note to the RDDAC/DDACS authors

To be sent by the author (not sent). Dataset creators: Sebastian Baum and Pascal Heinzelmann (University of
Stuttgart). Their descriptor paper: Baum, Heinzelmann, Clauß, Liewald, Weyrich (2026) Statistical analysis of
simulation-to-reality deviation in deep drawing with a benchmark dataset, *Transactions of the Indian Institute of
Metals*, doi:10.1007/s12666-026-03870-5. Purpose: courtesy, domain checks, and avoiding duplicated work. Whether to
offer collaboration or co-authorship is the author's decision.

---

**Subject:** Research using the RDDAC and DDACS datasets – design-stage decisions evaluated against production

Dear Mr Baum, dear Mr Heinzelmann,

Thank you for publishing the RDDAC and DDACS datasets and your recent paper on the simulation-to-reality deviation
in deep drawing. I am preparing a paper for *Research in Engineering Design* that builds on both datasets with a
different question: how close to a requirement a design-stage decision made from simulation can be relied on, and how
much production evidence a design team needs before such decisions become reliable. The work defines a production
floor from batches of consecutive parts and scores fourteen decision rules (from the nominal simulation to
Gaussian-process and gradient-boosting models, each calibrated rule also without the simulation) by how the new
design relates to the produced alternatives: a new lubrication variant, a new blank-holder force, or the other
geometry. All code and extracted feature tables are open, and the datasets and your paper are cited.

Some questions on which your knowledge of the experiments would help:

1. Are there drawing specifications or tolerances for the cups (wall angle, flange, bottom, depth) that could
   replace the general-tolerance scenarios (ISO 2768-1) used in the paper?
2. Measurement: were any parts scanned repeatedly, with re-fixturing, or was a reference artefact scanned during the
   series? Which scanner and fixture were used, and how was the calibration (mm per pixel and per height unit)
   obtained? In the scans the flange width along the scan lines scatters 4-18 times more than across them and the
   north wall reads 0.9-1.6 degrees low on the convex cups; I would like to describe this correctly.
3. What were the blank dimensions and the rolling direction relative to the scan axes, and in which order and on
   which dates were the 18 series produced? Were the parts of a series scanned in production order, and on which
   days? If they were not, scanner drift could not appear as drift in production order. Were any alternatives
   produced on more than one day or coil? That would allow a production floor that covers variation between runs.
4. The simulations overestimate the corner draw-in by about 3 mm and the blank-holder force effect on the draw-in
   by a factor of 2.7 to 5.1, and the simulated cut arms of the concave cups bend the other way from the parts. Is there
   information on the yield criterion and the unloading behaviour in the DDACS material model, or on the
   blank-holder system (cushion, spacers), that would help to interpret this?

I would be glad to send you the manuscript before submission and to hear any comments.

Kind regards,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
