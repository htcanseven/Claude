# Cover letter — Measurement (Elsevier)

Hüseyin Tayyer Canseven
Department of Electrical Engineering
LUT University, Lappeenranta, Finland
huseyin.canseven@lut.fi
ORCID 0000-0001-5703-6539

[Date]

To the Editor-in-Chief
*Measurement*
Elsevier

Dear Editor,

Please consider the enclosed manuscript, **"Leakage-Free Performance Evaluation of
Low-Rate MEMS Sensing for IoT-Based Condition Monitoring of Induction Machines"**,
for publication in *Measurement*.

**The measurement problem addressed.** The manuscript is not a fault-diagnosis
method paper, and no new classifier is proposed. Its subject is a measurement
procedure: how the diagnostic performance of a low-cost sensing chain should be
estimated so that the number obtained means what it appears to mean. Diagnostic
accuracy is treated throughout as a measured quantity with a defined measurand, a
stated sampling unit, an interval, and an experimentally characterised bias. That
framing is what the paper contributes; the induction machine and the
smartphone-grade accelerometer are the measurement object and the instrument.

**Principal findings.** Conventional random-split evaluation is shown to overstate
accuracy by $41$ to $47$ percentage points on a public $100$~Hz smartphone-MEMS
dataset. Rather than stopping at that observation, the paper isolates the
mechanism with a ladder of partitionings, and the result is not the one the
literature assumes: window overlap, the cause most often named and most often
guarded against, accounts for none of the inflation, and neither does temporal
proximity between windows. Recording identity accounts for all 46.7 points.
Enforcing non-overlapping windows, a widespread precaution, therefore offers no
protection whatever on data of this kind.

A second controlled experiment addresses an apparent paradox. Decimating to
25 Hz improves leakage-free accuracy even though it removes every shaft
rotational frequency in the dataset, all of which lie above the resulting 12.5 Hz
Nyquist frequency. Holding the frequency content fixed while varying the sample
rate shows that band-limiting alone is mildly harmful, that the entire gain
follows from the reduced number of samples per analysis window, and that omitting
the anti-alias filter costs 24.9 points. The consequence is general: a
sampling-rate sweep conducted with a fixed time-domain feature set does not
measure the information content of the band, because the descriptors themselves
are not invariant to the sampling rate.

**Reporting.** Performance is scored per held-out recording and summarised with
intervals clustered on that unit, which is the unit a new installation actually
samples. The resulting intervals are approximately three times wider than those
obtained by repeating the analysis over re-partitionings of the same data, and one
comparison that would have appeared strongly significant under the latter is shown
not to be. The manuscript states plainly that this is a reproducibility interval
over the available recordings and not a GUM-conformant uncertainty budget, since
the dominant influence quantities — machine, fault specimen, mounting and session
— do not vary within the dataset. Those unquantified contributions are set out
qualitatively instead.

**Relation to the existing literature.** Section 2 reviews the relevant
instrumentation and measurement body of knowledge and states what this work adds
to it: the metrological characterisation of MEMS accelerometers, including
calibration, thermal behaviour and cross-axis sensitivity; the documented
measurement errors of smartphone-grade inertial sensors; evaluation methodology
and leakage; operating-condition shift; and uncertainty evaluation for quantities
produced by learned models. Section 4 is explicit that what it reports is a
data-derived characterisation of the delivered signal channels and not a
calibration of the transducer, which archived data cannot support.

**Scope and limitations.** All recordings come from one 1.1 kW machine in which
each fault class is a single physical specimen. The estimated quantity is
therefore performance on an unseen recording of that machine, and this is stated
in the abstract, the introduction and the limitations section rather than left to
inference. The deployment quantities are calculated rather than measured on
hardware and are labelled as such.

**Declarations.** The manuscript is original, has not been published previously
and is not under consideration elsewhere. It is the work of the sole author, who
declares no competing interests and no specific funding for this work. The
vibration data analysed are openly available in Mendeley Data under a CC BY 4.0
licence, as recorded in the data availability statement.

Thank you for considering this submission.

Yours sincerely,

Hüseyin Tayyer Canseven
LUT University, Lappeenranta, Finland
