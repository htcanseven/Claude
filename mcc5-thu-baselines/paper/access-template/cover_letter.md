# Cover Letter

**To the Editor in Chief, IEEE Access**

**Subject.** Submission of the original research article "Beyond Closed-Set
Accuracy: Constituent-Level Generalization in Compound Motor Fault Diagnosis"

Dear Editor,

We submit the enclosed manuscript for consideration as a regular research
article in IEEE Access. The work is original, it has not been published
previously, and it is not under consideration by any other journal.

Data driven fault diagnosis for electrical machines now reports accuracies
close to ceiling on standard laboratory benchmarks, yet those numbers are
obtained under a formulation that industrial deployment rarely matches. A
machine in service can develop two faults at once, and the specific
combination it presents is usually absent from the training history. A closed
set classifier cannot even express that situation, because an unseen
combination constitutes an unseen class. Our manuscript asks whether the
elementary mechanisms of a compound fault can be recovered when the exact
combination, the compound context, and the operating condition are varied
independently of what the model has seen.

We believe the study offers four things that are new to this literature.
First, it evaluates compound faults whose constituents live in different
sensing modalities, pairing a mechanical bearing defect with broken rotor
bars, eccentricity, or a stator winding short circuit, whereas prior work on
compound fault decoupling and zero shot compound recognition has evaluated
almost exclusively bearing and gear pairings observable in one vibration
channel. Second, it varies novel composition, compound context deprivation,
and operating condition novelty jointly in a single crossed protocol under
run level and severity aware splits, rather than testing any one of them in
isolation. Third, it interprets every principal metric against input
independent constant predictor references, which shows that several
apparently favorable partial recovery scores are at or below what label
prevalence alone achieves. Fourth, it resolves the failure by mechanism and
finds that poor decomposition has no single cause. Dynamic eccentricity is
almost perfectly learnable in isolation, at an AUROC of 0.9995, yet collapses
to a compound recall of 0.017, while static eccentricity is limited mainly by
classifier family and the winding fault is already weakly specific in
isolation.

The headline result is a gap rather than a score. Closed set accuracy over
the 24 diagnostic states reaches 0.913, while exact recovery of unseen
constituent sets remains between 0.083 and 0.157. We regard the analysis of
that gap, rather than any single number, as the contribution.

We also draw the Editor's attention to a result we report against our own
interest. Our primary crossed analysis indicated that compound context
deprivation is more harmful when the operating condition is also unseen. We
subjected that finding to clustering at the composition level and to matching
of total training set cardinality between regimes, and under those stricter
analyses the interaction remained positive on average but was no longer
statistically resolved. We report this explicitly in the abstract, the
results, and the conclusion, and we have qualified the corresponding
recommendation for commissioning practice accordingly. We took the same
approach to the physical features, verifying the order integration bandwidth
and the placement of the broken bar sidebands directly from the released
signals and stating where the descriptors act as carrier relative proxies
rather than slip parameterized measurements.

The study uses the public MCC5-THU motor dataset, so every reported protocol
can be reconstructed by other groups, and we hope the constituent level
protocol and the prevalence references transfer to other multimodal releases.
We believe the topic suits the broad readership of IEEE Access, since it sits
at the intersection of electrical machine condition monitoring, multimodal
signal processing, and machine learning evaluation methodology, and since its
central caution, that closed set accuracy is not deployment readiness,
applies well beyond the specific machine studied here.

A supplementary document accompanies the submission. It reports reference
experiments on evaluation protocol difficulty, on what a shared multimodal
feature space does to the weaker constituent of a compound fault, and on the
release level properties of the dataset that affect protocol design.

Both authors have read and approved the manuscript and agree to its
submission. The authors declare no conflict of interest. Correspondence
should be addressed to Hüseyin Tayyer Canseven at huseyin.canseven@lut.fi.

We thank you for considering our work and we look forward to the reviewers'
comments.

Sincerely,

Hüseyin Tayyer Canseven, on behalf of the authors
Department of Electrical Engineering
Lappeenranta-Lahti University of Technology (LUT University)
Lappeenranta, Finland
