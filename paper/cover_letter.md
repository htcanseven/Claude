# Cover letter — Measurement Science and Technology

Hüseyin Tayyer Canseven
Department of Electrical Engineering
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
ORCID 0000-0001-5703-6539

[Date]

To the Editors
*Measurement Science and Technology*
IOP Publishing

Dear Editors,

Please consider the enclosed manuscript, **"Deployment-Realistic Performance
Measurement of Low-Cost MEMS Sensing for IoT-Based Condition Monitoring of
Induction Machines"**, for publication in *Measurement Science and Technology*
as a **Paper**, for inclusion in the Focus Collection *Intelligent Measurement
and Digitalization for Industrial Asset Health Management* (guest editors
Z. Xu, K. Feng, H. Li and Y. Shi). The manuscript speaks directly to two of that
collection's stated themes. It is an exercise in **uncertainty-aware sensing and
measurement**: diagnostic performance is reported as a measured quantity with
Type A expanded uncertainty and paired significance testing rather than as a
bare accuracy figure. It also addresses **lifecycle health assessment under
evolving data conditions**, in that the degradation of that performance under a
change of operating context is measured directly, through leave-one-speed-out
and leave-one-load-out protocols, instead of being assumed away.

The manuscript treats the diagnostic performance of a low-cost sensor as a
quantity that must itself be measured, rather than as a score to be maximised.
Two measurement questions organise the work: how much fault-relevant information
a consumer-grade MEMS accelerometer can convey at a software-capped 100 Hz, and
how the performance of such a sensing chain must be measured if the resulting
figure is to transfer to deployment. Both are addressed on a public
smartphone-acquired vibration dataset of a 1.1 kW induction machine recorded
across six health states, three supply frequencies, and two load conditions.

**Relevance to Measurement Science and Technology.** The contribution is
metrological rather than algorithmic; no new classifier is proposed. Three
elements place it within the journal's scope. First, the consumer accelerometer
is characterised as the front end of a measurement chain—its effective
resolution, a broadband signal floor that upper-bounds the sensor noise, the
usable band imposed by the Nyquist limit, and the relative informativeness of
its raw and gravity-compensated channels are all established directly from the
acquired data. Second, a measurement protocol is defined for the performance
figure itself, and the bias of the prevailing practice is quantified: random
splitting of overlapping analysis windows is shown to overstate accuracy by
approximately 41 to 47 percentage points, so that the near-perfect accuracies
routinely reported for this class of data are largely a measurement artefact of
window overlap and recording identity. Third, results are reported with Type A
expanded uncertainty and with paired significance tests conducted at a
defensible experimental unit, rather than as bare point estimates. The journal
has published closely related smart-sensor condition-monitoring work—for
example, Shukla, Mahmud and Wang, *Meas. Sci. Technol.* **31** 105104
(2020)—and the present manuscript addresses the measurement rigour that such
sensing systems require.

**Principal findings.** Under a leakage-free, recording-wise protocol the
accuracy of standard classifiers falls from essentially 100% to about 53%, with
comparable reductions under deliberate cross-speed and cross-load shifts; the
residual accuracy nonetheless remains well above the 16.7% chance level, and
coarse health states are recoverable while the staging of incipient bearing
degradation, whose signatures lie beyond the 50 Hz usable band, is not. A
resource-frugal configuration—25 Hz sampling, three raw channels, and a 4 s
window—classifies the health state 23.1 percentage points more accurately than
the full-rate baseline (paired *t*-test, *p* = 0.0001) while reducing the raw
data volume roughly eight-fold, which translates through a communication link
budget and a kilobyte-scale edge-model footprint into concrete operating points
for Bluetooth Low Energy, Zigbee, NB-IoT, and LoRaWAN nodes.

The limitations are stated explicitly rather than left to inference. The study
rests on a single machine in which each fault class is represented by one
physical specimen, so the recording-wise protocol removes window-overlap and
operating-point leakage but not specimen identity; the reported expanded
uncertainty is a reproducibility interval covering resampling variance only; and
the deployment quantities are calculated or emulated rather than measured on
hardware. These bounds are set out in the Limitations section so that the
reported figures are read as a deployment-honest baseline rather than a claim of
field performance.

**Declarations.** The manuscript is original, has not been published previously,
and is not under consideration elsewhere. It is the work of the sole author,
who declares no competing interests and no specific funding for this work. No
new data were created: the vibration data analysed are openly available in
Mendeley Data under a CC BY 4.0 licence, as recorded in the data availability
statement. **Double-anonymous peer review is requested**, and the enclosed
manuscript has been prepared accordingly, with author and affiliation details
removed from the article file.

Thank you for considering this submission. I would be glad to respond to any
questions during the review process.

Yours sincerely,

Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
