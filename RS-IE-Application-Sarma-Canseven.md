# Royal Society International Exchanges 2026/R3 — Full Application Text

*Mirror of `RS-IE-Application-Sarma-Canseven.docx` (the editable Word version). Lead applicant Nur Sarma (Durham); co-applicant Hüseyin T. Canseven (LUT). Project 31 March 2027 – 30 March 2029, £11,950 requested.*

Royal Society International Exchanges 2026 — Global Round 3

Fault signatures under real operating conditions: co-simulation of offshore wind turbine generator faults

Lead applicant: Dr Nur Sarma, Department of Engineering, Durham University, United Kingdom

Co-applicant: Dr Hüseyin T. Canseven, Department of Electrical Engineering, LUT University, Finland

Duration: 2 years  ·  Project dates: 31 March 2027 – 30 March 2029  ·  Requested: £11,950

Submission deadline: Thursday 24 September 2026, 15:00 UK time

Draft for editing. Text in square brackets requires confirmation by the applicants. Word counts are stated against each field limit and were measured on the text as written — re-count after editing, as Flexi-Grant may count hyphenated words differently.


## Part 1 — Application text

### Project title   (limit 20 words — 14 used)
Fault signatures under real operating conditions: co-simulation of offshore wind turbine generator faults.


### Abstract   (limit 400 words — 370 used)
Offshore wind turbines now reach 15–25 MW and increasingly use direct-drive permanent magnet synchronous generators (PMSGs). Offshore access is weather-limited and costly, so operators depend on condition monitoring to detect electrical faults — partial demagnetisation, stator inter-turn short circuits and air-gap eccentricity — before they force unplanned intervention or extended downtime.

The fault signatures underpinning these monitoring systems are almost always derived from isolated, single-domain models: a finite-element model of the generator is driven at fixed speed and torque, and the resulting current, flux or vibration harmonics are catalogued. Real turbines never operate this way. Turbulent wind, wave-induced tower motion, pitch and torque control action, and drivetrain compliance continuously move the operating point, while the fault itself perturbs torque ripple and thermal state, feeding back into drivetrain dynamics and controller response. Whether a signature identified under open-loop conditions remains observable — and separable from ordinary operational variability — inside this closed multi-physics loop is largely unquantified. It is a credible explanation for why diagnostics validated in the laboratory underperform in the field.

This project will develop and exploit a coupled co-simulation framework in which generator electromagnetics, drivetrain mechanics, turbine aero-servo-elastic behaviour and the power-electronic drive are solved together under realistic offshore excitation, with electrical faults injected at machine level. It combines capabilities neither partner holds alone: LUT University contributes fault-resolved PMSG modelling, multiphase drive and thermal expertise; Durham University contributes turbine drivetrain modelling, condition-monitoring signal analysis and an instrumented drivetrain test facility.

Our objectives are to: (i) couple the partners&apos; domain models through a standard co-simulation interface, using the IEA Wind 15 MW reference turbine as a common benchmark; (ii) derive reduced-order, fault-aware generator models fast enough for long closed-loop time-domain simulation, calibrated against detailed finite-element analysis; (iii) quantify how fault detectability varies across the operating envelope under turbulent and controller-driven conditions, producing signature persistence maps for each fault type and severity; (iv) test the framework&apos;s predictions against measurements from Durham&apos;s drivetrain test rig; and (v) release the coupled model and a reference fault dataset openly.

The work will be delivered through four bilateral exchange visits comprising six researcher trips, two co-supervised master&apos;s projects, departmental seminars at both universities and a UK industry visit, establishing a durable Finland–UK partnership positioned for larger joint proposals.


### Lay summary   (limit 250 words — 247 used)
Offshore wind is now a large part of Britain&apos;s electricity supply, and Finland is building its first wind farms in the Gulf of Bothnia. The turbines are enormous — a single machine can supply thousands of homes — and they stand far offshore, reachable only by boat or helicopter in calm weather. When something breaks inside one, the repair bill is rarely the main cost; the electricity lost while engineers wait for a safe weather window is.

Operators therefore try to listen for trouble in advance. Sensors watch the generator for small changes in electrical current or vibration that betray early damage: a weakening magnet, a short circuit between windings, a shaft running slightly off-centre. The warning patterns are worked out on computers — but almost always by studying the generator on its own, spinning steadily, as though the wind never gusted and the turbine never adjusted itself.

Real turbines are nothing like that. The wind is turbulent, waves rock the tower, and the control system constantly changes the machine&apos;s speed to capture energy. This raises a surprisingly unresolved question: do the warning signs engineers depend on survive these messy real conditions, or disappear into the noise?

To find out, we will join our two groups&apos; computer models — Finland&apos;s expertise in the generator itself, Durham&apos;s in the whole turbine and its monitoring — into a single simulation, then test it against laboratory measurements and a visit to a working offshore wind site. Better early warning means cheaper, more reliable clean electricity.


### Research proposal   (limit 500 words — 438 used)
Purpose. Condition monitoring of offshore wind generators relies on fault signatures derived largely from single-domain, open-loop simulation. This project asks whether those signatures persist when the generator is embedded in a complete, closed-loop turbine operating under realistic offshore conditions, and delivers a validated co-simulation framework for answering such questions.

1. Fault-resolved generator modelling (LUT). Finite-element models of a direct-drive PMSG will represent partial and uniform demagnetisation, stator inter-turn short circuits, and static and dynamic eccentricity across a range of severities. Coupled electromagnetic–thermal analysis will capture the temperature dependence of magnet behaviour, which alters signature amplitude and is routinely neglected.

2. Reduced-order surrogates (joint). Finite-element models are far too slow for the multi-minute closed-loop runs required. We will derive reduced-order, fault-aware generator models — magnetic-equivalent-circuit formulations and data-driven surrogates trained on finite-element results — and verify their fidelity against full analysis. These surrogates are the principal methodological contribution and the focus for the co-supervised students.

3. Model coupling (joint). Domain models will be coupled through the Functional Mock-up Interface standard: an aero-servo-elastic turbine model [OpenFAST] supplying rotor torque and speed under turbulent wind and controller action; a torsional drivetrain model; the reduced-order generator; and a power-electronic drive and control model. Coupling stability, time-step selection and interface variables will be treated explicitly, since these determine whether coupled results can be trusted.

4. Signature persistence analysis (Durham). Using the IEA Wind 15 MW reference turbine as a common benchmark, faults will be injected across the operating envelope under turbulence intensities and sea states representative of North Sea and Gulf of Bothnia conditions. Spectral, wide-band converter-signal and machine-learning detection methods will be applied to produce detectability maps: for each fault type and severity, the conditions under which detection is reliable, marginal or impossible.

5. Experimental validation (Durham). Predictions will be tested on Durham&apos;s instrumented drivetrain test rig, where controlled electrical faults and realistic torque profiles can be applied and measured. A visit to a UK offshore wind facility will ground modelling assumptions in operational practice.

Work plan. The project runs from 31 March 2027 to 30 March 2029 around four bilateral visits. April 2027, Durham: start-up meeting, agreement of model interfaces and fault scenarios, departmental seminar. December 2027, Lappeenranta: evaluation of the first coupled prototype, laboratory visits, departmental seminar. May 2028, Durham: mid-project meeting with the LUT master&apos;s student, test-rig validation campaign, departmental seminar and industry visits. March 2029, Lappeenranta: closing meeting with the Durham master&apos;s student, joint analysis and a proposal-development workshop for follow-on funding.

Outputs. An openly released coupled model and reference fault dataset; two co-supervised master&apos;s theses; at least two joint journal papers; and a validated basis for larger collaborative proposals.


### Participants   (limit 200 words — 158 used)
Two master&apos;s students will join the project, one from each institution, each co-supervised jointly by the applicant and co-applicant.

[Name to be confirmed], a master&apos;s student at LUT University working in the co-applicant&apos;s group on permanent magnet machine modelling, will contribute to development and validation of the reduced-order fault-aware generator models, and will travel to Durham in May 2028.

[Name to be confirmed], a master&apos;s student at Durham University in the lead applicant&apos;s condition-monitoring group, will contribute to the detectability analysis and the test-rig measurement campaign, and will travel to Lappeenranta in March 2029.

Joint co-supervision gives each student a supervisor at the partner institution and direct experience of a complementary research environment. This is the principal mechanism by which the collaboration will be embedded below principal-investigator level, where partnerships most often succeed or fail. Both theses will form part of the project&apos;s reported outputs, and both students will contribute to the joint publications arising from the work.


### Benefits to individuals and institutions   (limit 200 words — 180 used)
For the applicants, the collaboration joins capabilities neither holds alone: the co-applicant&apos;s fault-resolved permanent magnet generator modelling, multiphase drive and thermal expertise, and the lead applicant&apos;s turbine drivetrain modelling, condition-monitoring methods and experimental facilities. Each gains a research direction otherwise out of reach — respectively, system-level context for machine-level models, and physically grounded fault models for monitoring research.

Planned outcomes are an openly released co-simulation framework and reference fault dataset, two co-supervised master&apos;s theses, and at least two joint journal publications.

For the institutions, the exchange builds a working link between Durham&apos;s wind energy and condition-monitoring group and LUT&apos;s electrical machines and drives group — complementary centres with no current institutional relationship. Departmental seminars during each visit will extend contact beyond the immediate teams.

We intend to sustain the partnership deliberately. The framework and its first results are designed as the evidence base for a Marie Skłodowska-Curie Staff Exchanges proposal, for cascade-funding calls under the Horizon Europe wind programme, and for parallel national applications to the Research Council of Finland and EPSRC. The closing visit is dedicated to developing these proposals jointly.


### Benefits to the United Kingdom   (limit 200 words — 166 used)
UK offshore wind capacity stands at roughly 16 GW operational, with a record 8.4 GW awarded in Contracts for Difference Allocation Round 7 in January 2026. Sustaining that expansion depends on reducing operation and maintenance costs, of which generator reliability is a significant component.

The project gives UK research direct access to capability with no close domestic equivalent: LUT University&apos;s permanent magnet machine design and modelling group, and the wider Lappeenranta drivetrain ecosystem, which includes large-scale generator manufacturing and test facilities. Detailed fault-resolved generator models of the kind LUT produces are difficult to obtain in the UK, and they are precisely what condition-monitoring research needs in order to move beyond empirical signature catalogues.

The collaboration also brings cold-climate reliability knowledge, increasingly relevant as UK development moves into harsher northern waters. A Durham master&apos;s student will be trained through an international research placement, contributing skilled people to the North East offshore wind cluster. All modelling outputs will be released openly for use by UK researchers and industry.


### Benefits to the overseas country — Finland   (limit 200 words — 183 used)
Finland is at the start of offshore wind deployment. Tahkoluoto, the world&apos;s first offshore wind farm built for freezing sea conditions, remains the country&apos;s only operating site; a substantial extension is planned, Vattenfall&apos;s Korsnäs project in the Gulf of Bothnia will be Finland&apos;s first at commercial scale, and the Finnish Energy Authority is preparing auctions for exclusive economic zone areas. Finland is therefore about to commission assets whose lifetime maintenance costs are being determined by decisions taken now — without the operational experience the UK has accumulated over two decades.

This project transfers that experience directly. Finnish researchers gain access to UK condition-monitoring practice, test-rig methodology and an operating offshore site, and return with methods for assessing fault detectability before turbines are specified and ordered.

Finland also has an industrial stake: permanent magnet generators for offshore turbines are manufactured in Lappeenranta alongside one of Europe&apos;s largest drivetrain test facilities. Better fault modelling supports the design-for-reliability decisions this supply chain faces.

Gulf of Bothnia conditions — sea ice and extreme cold — will be represented explicitly in the simulation scenarios, addressing a reliability question specific to Finland.


### Data management and data sharing   (limit 200 words — 176 used)
The project will generate a coupled co-simulation framework linking generator, drivetrain, turbine and drive models; reduced-order fault-aware generator model parameters; simulated fault-signature datasets spanning the operating envelope; and measurement records from the Durham drivetrain test rig.

The framework and reduced-order models will be released under a permissive open-source licence and the simulated datasets under CC-BY, both deposited in Zenodo with DOIs and cited in the resulting publications. Records will also be catalogued in Durham Research Online and the LUT research portal in line with institutional policy. Datasets will carry metadata describing the turbine model, fault type and severity, and operating conditions, so that others can reproduce and extend the analysis.

These outputs should be of direct value to the wind energy research community, where openly available, well-characterised generator fault datasets are scarce and most published signature studies cannot be independently reproduced. Any operational data provided in confidence by industrial contacts will be excluded from public release; only derived and aggregated results will be published. Deposition in Zenodo ensures long-term preservation beyond the life of the project.


## Part 2 — Financial details

### Budget summary   all figures £ sterling

| Visit (traveller, date, destination) | Flights | Accom. | Subsist. | Internal | Subtotal |
|---|---|---|---|---|---|
| 1. Canseven, Apr 2027, Durham (1 person, 7 days) | 600 | 840 | 280 | 150 | 1,870 |
| 2. Sarma, Dec 2027, Lappeenranta (1 person, 7 days) | 600 | 690 | 490 | 150 | 1,930 |
| 3. Canseven + MSc student, May 2028, Durham (2 people, 7 days) | 1,200 | 1,680 | 560 | 300 | 3,740 |
| 4. Sarma + MSc student, Mar 2029, Lappeenranta (2 people, 7 days) | 1,200 | 1,380 | 980 | 300 | 3,860 |
| Travel total (incl. subsistence) |  |  |  |  | 11,400 |
| Consumables — visa charges (3 × £135) |  |  |  |  | 405 |
| Consumables — printing, stationery, software |  |  |  |  | 145 |
| Consumables total (cap £3,000) |  |  |  |  | 550 |
| PROJECT TOTAL (cap £12,000) |  |  |  |  | 11,950 |

Consumables limit for a 2-year award is £3,000; overall limit is £12,000. The request of £11,950 leaves £50 unallocated — add £50 of printing or software to consumables if you prefer to request the full £12,000.


### Justification for travel (including subsistence)
All travel is between the United Kingdom and Finland; no third-country travel is claimed. Airfares are estimated at economy/APEX rates. Each visit lasts seven days (six nights), allowing a full working week at the partner institution together with a departmental seminar and, in May 2028, industry visits.

Per traveller, costs comprise return flights (£600), accommodation (£140 per night in Durham; £115 per night in Lappeenranta), subsistence at institutional rates (£40 per day UK rate; £70 per day overseas rate) and internal travel (£150, covering the rail connection from the arrival airport to Durham or Lappeenranta and local travel during the visit). Visa charges are claimed under consumables.

Provisional visit plan:

- Canseven: 7 days, April 2027, Durham, United Kingdom, £1,870
- Sarma: 7 days, December 2027, Lappeenranta, Finland, £1,930
- Canseven and one MSc student: 7 days, May 2028, Durham, United Kingdom, £3,740
- Sarma and one MSc student: 7 days, March 2029, Lappeenranta, Finland, £3,860

### Justification for consumables
Visa charges: £405, comprising three six-month UK visitor visas at £135 each — for the co-applicant&apos;s two visits to Durham and for the accompanying LUT master&apos;s student in May 2028.

Printing, poster production and stationery for visiting researchers, and software licences supporting the co-simulation interface: £145.

Total consumables: £550, within the £3,000 limit for a two-year award.


## Part 3 — Points to check before submission

### Corrections applied to the costing document
Travel arithmetic. The four visit totals in the costing document are each internally correct (£2,005, £1,930, £4,010, £3,860), but they sum to £11,805, not the £11,855 stated. With consumables of £145 the project total is £11,950, not £12,000.

Visa costs reclassified. The scheme notes list visa charges as an eligible consumable, not a travel cost. The £405 of visa charges has therefore been moved out of the travel lines into consumables, giving travel of £11,400 and consumables of £550. The overall total is unaffected, but the two budget fields on the form must be entered this way.


### Items requiring your confirmation
- Final visit timing. The project ends 30 March 2029 and the closing visit is scheduled for March 2029, leaving no margin. Consider moving it to January or February 2029 so that a delay does not push activity outside the award period.
- Project start date. 31 March 2027 is the latest start the scheme permits, and awards are announced in March 2027. This is allowable — the Society counts planning activity as the start — but an earlier date within the permitted window would provide buffer.
- Schengen visa for the Durham student. No visa is budgeted for the March 2029 travel to Finland. If the Durham master&apos;s student is not a UK or EU national, a Schengen visa may be required and should be added to consumables.
- Accommodation rates. £140 per night in Durham and £115 in Lappeenranta should be checked against current rates, particularly for a seven-night stay in term time.
- Durham test rig. The description of the rig in the research proposal is written from published accounts; the lead applicant should correct it to match current capability.
- Software. OpenFAST and the Functional Mock-up Interface are named as the coupling toolchain. Substitute whatever you actually license and use.
- Master&apos;s students. Confirm both institutions can commit a student and that cross-institutional co-supervision is permitted under each university&apos;s regulations.
- Offshore site visit. Confirm this can be arranged before it is promised — it is among the strongest justifications for travel in the application.

### Scheme mechanics
- Enter the duration as 2 years. The form accepts only 3 months, 1 year or 2 years; a one-year no-cost extension may be requested later if a third year is needed.
- Four people must complete their Flexi-Grant sections before submission: the co-applicant, both Heads of Department, and Durham&apos;s institutional approver. Target 17 September; the approver must approve by the deadline itself.
- An ORCID identifier is mandatory at submission for both applicants, and both must complete the diversity monitoring form.
- Computer hardware is not an eligible cost; software is.
- Scheme notes §9 requires that any use of generative AI tools in preparing the application is acknowledged, naming the tool and describing how the content was generated. This draft was prepared with AI assistance.