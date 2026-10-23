# Draft: request to the RDDAC/DDACS authors

To be sent by the author (not sent). Dataset creators: Sebastian Baum and Pascal Heinzelmann (University of
Stuttgart). Their descriptor paper: Baum, Heinzelmann, Clauß, Liewald, Weyrich (2026) Statistical analysis of
simulation-to-reality deviation in deep drawing with a benchmark dataset, *Transactions of the Indian Institute of
Metals*, doi:10.1007/s12666-026-03870-5. Purpose: courtesy, the production and scanning log and any verification data
that the simulated review panel recommended requesting (items 1–3 below), and the simulation details that the
dataset documentation leaves open (item 4). The revision does not depend on the answer; the paper states what is
unknown. Whether to offer collaboration or co-authorship is the author's decision.

---

**Subject:** Request for production and scanning metadata of the RDDAC dataset

Dear Mr Baum, dear Mr Heinzelmann,

Thank you for publishing the RDDAC and DDACS datasets and your paper on the simulation-to-reality deviation in deep
drawing. I am preparing a paper for the *Journal of Intelligent Manufacturing* that builds on both datasets with a
different question: when a design-stage prediction can replace a physical trial. It scores simulation-based, learned
and production-record decision rules against production, in a unit set by the difference between batches of
consecutive parts within one series (the within-run floor), separately for a new lubrication variant, a new
blank-holder force and the other geometry. All code and extracted feature tables are open, and the datasets and your
paper are cited.

The floor is set by drift within the series, which none of the recorded process signals explains, so whether it
comes from the process or from the measuring chain matters for the paper. Could you tell me, where it is available:

1. **Production and scanning log.** The order and dates of the 18 series; whether the parts of a series were scanned
   in line and in production order, and with what delay and part temperature; the coil or blank batch of each series;
   and whether any alternative was produced on more than one day or coil.
2. **Measurement.** The scanner model and its calibration (mm per pixel across and along the lines, height unit);
   the fixturing and orientation of the parts; and any verification data: a reference artefact scanned through a
   series, repeated scans of one part with and without re-fixturing, or a comparison with a coordinate measuring
   machine. In the scans the flange width in the direction of motion reads 2.3–3.5 mm larger than along the laser line
   and scatters 4–18 times more, the two flange diagonals differ by 1.6–2.2 mm, and the north wall reads 0.9–1.6
   degrees low on the convex cups; I would like to describe this correctly.
3. **Process and tooling.** The blank dimensions and rolling direction relative to the scan axes; the material
   certificate (yield and tensile strength, r-values); the tool dimensions (punch, die radius, drawing depth); the
   press and the blank-holder or cushion system; and how the three lubrication patterns were applied. The measured cup
   depth is 0.7–1.1 mm smaller than in the simulations at nominal settings, and the cup width at 15 mm depth about
   2 mm larger in radius; a difference in effective drawing depth or tool geometry would explain both.
4. **Simulations (DDACS).** The element formulation, whether contact accounts for the shell thickness, the yield
   criterion and hardening law, the blank-holder actuation, the springback procedure, and whether simulations with
   other flow-curve factors exist for the RDDAC tool geometries. The simulations overestimate the effect of the
   blank-holder force on the draw-in by a factor of 2.7 to 5.1, and the cut arms of the concave cups bend the other
   way from the parts.

I would be glad to send you the manuscript and to hear any comments.

Kind regards,
Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
