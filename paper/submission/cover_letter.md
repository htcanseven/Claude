# Cover letter

*For the comment field of the submission to the Journal of Intelligent Manufacturing (plain text). Replace
"[DOI to be inserted]" with the Zenodo DOI after the deposit.*

Dear Editors,

Please consider the enclosed manuscript, "A production-referenced evaluation of design-stage decision rules in deep drawing: when can a prediction replace a physical trial?", for publication as a research article in the Journal of Intelligent Manufacturing. The manuscript is a single document of 33 pages, including the declarations and the references.

Finite-element simulation has long informed manufacturability decisions in sheet-metal forming, and in recent years machine learning has been added to it. However, such models are judged by their prediction error, not by whether their verdicts could replace a physical trial. In this study, a production-referenced evaluation of design-stage decision rules is proposed. Firstly, the within-run floor is introduced as its unit: the difference that drift and scatter of production and measurement produce between two batches of one design within a run. After that, a rule that returns meets, fails or trial is characterized, for each relation of a new design to the produced evidence, by its decisive and safe distances. Finally, a guard band turns these distances into verdicts for single designs, and the verdicts are priced by the costs of errors and trials.

The framework is demonstrated on open data: 9,000 deep-drawn and cut cups, produced as 18 design-process alternatives of 500 consecutive parts each, and a generic simulation dataset of the same process that was not calibrated to it. The main findings of this exploratory application are as follows. The nearest produced setting decided at 3.4 floors with a produced sibling and at 8.5 floors for a new process setting, and no simulation-based or learned rule was more decisive. A Gaussian process specified for small data reduced to a force trend, and errors borrowed from the other family on the same relation, not learning, made the production record safe for new settings. For a new family, only simulation-based rules decided, none closer than 30 floors. Moreover, once runs differed by a floor, confirming a performance index of 1.33 needed replicated runs, which neither a prediction nor a short trial replaced.

These results are relevant to the readers of the journal who develop and deploy AI-based manufacturability tools. The study shows how such a tool can be compared with a production-record baseline, by evidence relation and in a unit that production defines, and it provides a proposed reporting checklist and an open scoring function for other processes.

All data are public. The code, the extracted feature tables and the result files that reproduce every number of the paper are archived on Zenodo (DOI: [DOI to be inserted]). The manuscript has not been published and is not under consideration elsewhere. The use of a large language model in the preparation of the study, including simulated reviews of earlier versions, is described in Section 4.5 and in the declarations. The author declares no competing interests.

Thank you for considering the manuscript.

Yours sincerely,

Hüseyin Tayyer Canseven
Department of Electrical Engineering, LUT University, Lappeenranta, Finland
