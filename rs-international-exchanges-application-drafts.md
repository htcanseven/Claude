# Royal Society International Exchanges 2026/R3 — Application Text Drafts

**Lead applicant:** Nur Sarma (Durham University, UK) · **Co-applicant:** Hüseyin T. Canseven (LUT University, Finland)
**Project:** Co-simulation of offshore wind turbine faults · **Duration to enter on the form: 2 years** (£12,000 option)
**Deadline:** Thursday 24 September 2026, 15:00 UK time

> These are drafts to edit, not final text. Everything in <mark>square brackets</mark> needs your confirmation. Word counts are given after each section and were measured on the text as written — re-count after you edit.

---

## The central design problem, and how these drafts solve it

A co-simulation project is, on its face, the hardest kind of project to justify travel money for: an assessor will reasonably ask why two people who model things on computers need six flights. Every section below is written so the exchanges are **load-bearing**:

- **Experimental validation** at Durham's instrumented drivetrain test rig — you cannot run a rig remotely.
- **A UK offshore site visit** grounding the simulation scenarios in operational reality.
- **Two co-supervised master's students**, each of whom works at the partner institution — the mechanism that makes the partnership outlive the grant.
- **Coupling two in-house toolchains**, which in practice is done sitting next to each other, not over email.

The science is also deliberately positioned as a *step beyond* your 2026 joint paper: that work was open-loop, single-domain finite-element analysis feeding a classifier. This project asks whether those signatures survive inside a closed, multi-physics loop. Given assessors will know about the prior paper, showing clear progression is the strongest position available to you.

---

## 1. Abstract (limit 400 words)

Offshore wind turbines now reach 15–25 MW and increasingly use direct-drive permanent magnet synchronous generators (PMSGs). Offshore access is weather-limited and costly, so operators depend on condition monitoring to detect electrical faults — partial demagnetisation, stator inter-turn short circuits and air-gap eccentricity — before they force unplanned intervention or extended downtime.

The fault signatures underpinning these monitoring systems are almost always derived from isolated, single-domain models: a finite-element model of the generator is driven at fixed speed and torque, and the resulting current, flux or vibration harmonics are catalogued. Real turbines never operate this way. Turbulent wind, wave-induced tower motion, pitch and torque control action, and drivetrain compliance continuously move the operating point, while the fault itself perturbs torque ripple and thermal state, feeding back into drivetrain dynamics and controller response. Whether a signature identified under open-loop conditions remains observable — and separable from ordinary operational variability — inside this closed multi-physics loop is largely unquantified. It is a credible explanation for why diagnostics validated in the laboratory underperform in the field.

This project will develop and exploit a coupled co-simulation framework in which generator electromagnetics, drivetrain mechanics, turbine aero-servo-elastic behaviour and the power-electronic drive are solved together under realistic offshore excitation, with electrical faults injected at machine level. It combines capabilities neither partner holds alone: LUT University contributes fault-resolved PMSG modelling, multiphase drive and thermal expertise; Durham University contributes turbine drivetrain modelling, condition-monitoring signal analysis and an instrumented drivetrain test facility.

Our objectives are to: (i) couple the partners' domain models through a standard co-simulation interface, using the IEA Wind 15 MW reference turbine as a common benchmark; (ii) derive reduced-order, fault-aware generator models fast enough for long closed-loop time-domain simulation, calibrated against detailed finite-element analysis; (iii) quantify how fault detectability varies across the operating envelope under turbulent and controller-driven conditions, producing signature persistence maps for each fault type and severity; (iv) test the framework's predictions against measurements from Durham's drivetrain test rig; and (v) release the coupled model and a reference fault dataset openly.

The work will be delivered through six exchange visits, two co-supervised master's projects and a UK offshore site visit, establishing a durable Finland–UK partnership positioned for larger joint proposals.

**Word count: 361** (39 words spare)

---

## 2. Lay Summary (limit 250 words)

Offshore wind is now a large part of Britain's electricity supply, and Finland is building its first wind farms in the Gulf of Bothnia. The turbines are enormous — a single machine can supply thousands of homes — and they stand far offshore, reachable only by boat or helicopter in calm weather. When something breaks inside one, the repair bill is rarely the main cost; the electricity lost while engineers wait for a safe weather window is.

Operators therefore try to listen for trouble in advance. Sensors watch the generator for small changes in electrical current or vibration that betray early damage: a weakening magnet, a short circuit between windings, a shaft running slightly off-centre. The warning patterns are worked out on computers — but almost always by studying the generator on its own, spinning steadily, as though the wind never gusted and the turbine never adjusted itself.

Real turbines are nothing like that. The wind is turbulent, waves rock the tower, and the control system constantly changes the machine's speed to capture energy. This raises a surprisingly unresolved question: do the warning signs engineers depend on survive these messy real conditions, or disappear into the noise?

To find out, we will join our two groups' computer models — Finland's expertise in the generator itself, Durham's in the whole turbine and its monitoring — into a single simulation, then test it against laboratory measurements and a visit to a working offshore wind site. Better early warning means cheaper, more reliable clean electricity.

**Word count: 246** (4 words spare)

---

## 3. Research Proposal (limit 500 words)

**Purpose.** Condition monitoring of offshore wind generators relies on fault signatures derived largely from single-domain, open-loop simulation. This project asks whether those signatures persist when the generator is embedded in a complete, closed-loop turbine operating under realistic offshore conditions, and delivers a validated co-simulation framework for answering such questions.

**Methods.**

*1. Fault-resolved generator modelling (LUT).* Finite-element models of a direct-drive PMSG will represent partial and uniform demagnetisation, stator inter-turn short circuits, and static and dynamic eccentricity across a range of severities. Coupled electromagnetic–thermal analysis will capture the temperature dependence of magnet behaviour, which alters signature amplitude and is routinely neglected.

*2. Reduced-order surrogates (joint).* Finite-element models are far too slow for the multi-minute closed-loop runs required. We will derive reduced-order, fault-aware generator models — magnetic-equivalent-circuit formulations and data-driven surrogates trained on finite-element results — and verify their fidelity against full analysis. These surrogates are the principal methodological contribution and the natural focus for the co-supervised students.

*3. Model coupling (joint).* Domain models will be coupled through the Functional Mock-up Interface standard: an aero-servo-elastic turbine model <mark>(OpenFAST)</mark> supplying rotor torque and speed under turbulent wind and controller action; a torsional drivetrain model; the reduced-order generator; and a power-electronic drive and control model. Coupling stability, time-step selection and interface variables will be treated explicitly, since these determine whether coupled results can be trusted.

*4. Signature persistence analysis (Durham).* Using the IEA Wind 15 MW reference turbine as a common benchmark, faults will be injected across the operating envelope under turbulence intensities and sea states representative of North Sea and Gulf of Bothnia conditions. Spectral, wide-band converter-signal and machine-learning detection methods will be applied to the resulting signals to produce detectability maps: for each fault type and severity, the operating conditions under which detection is reliable, marginal or impossible.

*5. Experimental validation (Durham).* Predictions will be tested on Durham's instrumented drivetrain test rig, where controlled electrical faults and realistic torque profiles can be applied and measured. A visit to a UK offshore wind site, arranged by the lead applicant, will ground modelling assumptions in operational practice and inform the scenarios studied.

**Work plan.** In year one the co-applicant visits Durham to build the coupling interface and define fault scenarios against rig data, and the lead applicant visits LUT to specify the generator fault models. In year two both visits are repeated, each accompanied by a co-supervised master's student — the lead applicant and her student to LUT, the co-applicant and his student to Durham — for joint validation, analysis and writing. Six visits in total.

**Outputs.** An openly released coupled model and reference fault dataset; two co-supervised master's theses; at least two joint journal papers; and a validated basis for larger collaborative proposals.

**Word count: 446** (54 words spare — use them to add a sentence on <mark>your specific software licences</mark> or a named fault-severity range)

---

## 4. Benefits to individuals/institutions (limit 200 words)

For the applicants, the collaboration joins capabilities neither holds alone: the co-applicant's fault-resolved permanent magnet generator modelling, multiphase drive and thermal expertise, and the lead applicant's turbine drivetrain modelling, condition-monitoring methods and experimental facilities. Each gains a research direction otherwise out of reach — respectively, system-level context for machine-level models, and physically grounded fault models for monitoring research.

Planned outcomes are an openly released co-simulation framework and reference fault dataset, two co-supervised master's theses, and at least two joint journal publications.

For the institutions, the exchange builds a working link between Durham's wind energy and condition-monitoring group and LUT's electrical machines and drives group — two complementary centres with no current institutional relationship. Co-supervision embeds the partnership below principal-investigator level, where collaborations most often survive or fail.

We intend to sustain it deliberately. The framework and its first results are designed as the evidence base for a Marie Skłodowska-Curie Staff Exchanges proposal in April 2027, for cascade-funding calls under the Horizon Europe wind programme, and for parallel national applications to the Research Council of Finland and EPSRC. Continued student exchange and shared supervision will maintain momentum between funded phases.

**Word count: 187** (13 words spare)

---

## 5. Benefits to Overseas Country/Territory — Finland (limit 200 words)

Finland is at the start of offshore wind deployment. Tahkoluoto, the world's first offshore wind farm built for freezing sea conditions, remains the country's only operating site; a substantial extension is planned, Vattenfall's Korsnäs project in the Gulf of Bothnia will be Finland's first at commercial scale, and the Finnish Energy Authority is preparing auctions for exclusive economic zone areas. Finland is therefore about to commission assets whose lifetime maintenance costs are being determined by decisions taken now — without the operational experience the UK has accumulated over two decades.

This project transfers that experience directly. Finnish researchers gain access to UK condition-monitoring practice, test-rig methodology and an operating offshore site, and return with methods for assessing fault detectability before turbines are specified and ordered.

Finland also has an industrial stake: permanent magnet generators for offshore turbines are manufactured in Lappeenranta alongside one of Europe's largest drivetrain test facilities. Better fault modelling supports the design-for-reliability decisions this supply chain faces.

Finally, Gulf of Bothnia conditions — sea ice and extreme cold — will be represented explicitly in the simulation scenarios, addressing a reliability question specific to Finland that no other national programme currently examines.

**Word count: 191** (9 words spare)

---

## Also required on the form — "Benefits to UK" (200 words)

You did not list this one, so presumably Nur is writing it. If it would help, the material is ready: UK offshore wind at roughly 16 GW operational with a record 8.4 GW awarded in Contracts for Difference Allocation Round 7 in January 2026; the UK gaining access to LUT's permanent magnet generator design capability and the Lappeenranta drivetrain test ecosystem, which has no direct UK equivalent; cold-climate reliability knowledge relevant to UK offshore expansion into harsher northern waters; and skills development for the North East offshore cluster through a trained master's student.

---

## Checks before you submit

**Facts to verify in the drafts**

- <mark>Durham's test rig</mark> — confirm what it can actually do. My description ("instrumented drivetrain test rig… controlled electrical faults and realistic torque profiles") is written from published descriptions of the Durham condition-monitoring rig; Nur should correct it to match current capability, and state the rating if that strengthens it.
- <mark>OpenFAST and the Functional Mock-up Interface</mark> — these are credible, standard choices, but swap in whatever you actually use (Bladed, HAWC2, Simulink coupling). Do not name software you do not have licences for.
- <mark>Master's students</mark> — confirm both institutions can commit a student in year two, and that co-supervision across institutions is permitted under each university's regulations. Reviewers may check this is realistic.
- <mark>Offshore site visit</mark> — confirm feasibility before promising it; it is one of the strongest justifications for travel in the whole application, so it needs to be real.
- <mark>Finite-element dimensionality</mark> — I wrote "finite-element models" without specifying 2D or 3D; add if useful.

**Scheme mechanics not to overlook**

- Enter the duration as **2 years**, never 36 months — the form only accepts 3 months, 1 year or 2 years. Request the one-year no-cost extension later if you need the third year.
- Budget: £12,000 maximum, of which no more than £3,000 consumables. Six person-visits will consume most of the travel allowance — check the arithmetic against real fares before finalising.
- The travel justification needs a **provisional visit plan** in the prescribed format: `Surname: length, estimated date, destination, cost`.
- **Hardware is not an eligible cost** (software is). If the project needs sensors or interrogators, they cannot come from this grant — which is another reason the modelling-plus-existing-rig design works.
- Visa charges *are* eligible consumables — budget them if needed for travel to the UK.
- Confirm your **LUT contract covers the full award duration** (to approximately March 2029 for a two-year award starting by 31 March 2027). This remains the outstanding eligibility item.
- Four people must complete Flexi-Grant sections before submission: you, Durham's Head of Department, LUT's Head of Department, and Durham's institutional approver — target **17 September**, and note the approver must approve *by* the deadline itself.
- **Declare AI assistance.** Scheme notes §9 requires that where generative AI tools are used in a proposal, their use is acknowledged "by naming the AI source and specifying how the content was generated (for example by listing the prompt used)". These drafts were AI-assisted, so if you carry the text across, disclose it as the scheme requires.

**One editorial suggestion.** The lay summary is the section the panel weights most heavily and the one most engineers under-invest in. Before submitting, give it to someone with no engineering background and ask them to explain the project back to you. If they cannot, it needs another pass — that single test is worth more than any further polish on the abstract.
