# Public Datasets for an ML-Based Fault-Diagnosis Paper Aimed at *Research in Engineering Design*

Survey date: 13 Sept 2026. Compiled from repository APIs/pages and the journal's public scope
statement and Crossref record. Companion to `research-summary.md`.

---

## 1. What the journal will accept — the constraint that decides the dataset

*Research in Engineering Design* (Springer, ISSN 0934-9839) publishes **design theory and
methodology** across all engineering branches. Its scope statement says it prioritises
"fundamental theories, principles, frameworks, and methods with broad applicability", lists
"data-driven and AI-enabled design" and "cyber-physical systems, robotics, AI" as welcome
areas — and states that papers which "primarily present case studies of individual design efforts
or focus solely on applying existing tools or methods … will be desk-rejected."

So a "hybrid classifier on dataset X reaches 99 %" paper will not survive desk review, however good
the ML is. The fault-diagnosis work has to be framed as a **design contribution**. Crossref shows
what the journal has actually accepted in this direction (2021–2026):

| Year | Paper (DOI) | Why it matters as precedent |
|---|---|---|
| 2026 | AfGNN: adaptive graph neural networks for causal failure reasoning in DFMEA (10.1007/s00163-026-00490-4) | ML on failure data, framed as a DFMEA method |
| 2026 | An efficient design framework for developing and demonstrating high reliability in an autoinjector (10.1007/s00163-026-00493-1) | Reliability + "mapping critical parameters to the fault model" as a design framework |
| 2026 | The domain relationship diagram: a mapping framework for digital twin design in cyber-physical ecosystems (10.1007/s00163-026-00491-3) | DT/monitoring architecture as a design object |
| 2026 | A semantic-geometric digital twin framework for performance-driven design evaluation (10.1007/s00163-026-00478-0) | DT used to evaluate designs |
| 2025 | Reliability-based robust design considering performance degradation: an ML-driven approach for helical springs (10.1007/s00163-025-00463-z) | ML + degradation inside a design-optimisation method |
| 2025 | Mapping of the digital twin design process landscape (10.1007/s00163-025-00468-8) | DT design process |
| 2025 | Probabilistic early design quality-risk and crux identification with stochastic Petri nets (10.1007/s00163-025-00466-w) | Early-stage risk/fault modelling |
| 2021 | Improving reliability engineering in product development based on design theory: FMEA in semiconductors (10.1007/s00163-021-00360-1) | Reliability methods reframed through design theory |

Framings that fit this pattern (and the datasets that support each):

1. **Design for diagnosability** — a method/metric that tells a designer, at design time, how
   detectable a fault class will be for a given machine variant and sensor suite.
   Needs: several *design variants* with the same faults; ideally design metadata.
2. **Design-stage (simulation) → in-service (measurement) transfer as a validation method** —
   the FEA + transfer-learning idea from the *Machines* 2026 paper, generalised into a design
   methodology with a stated procedure and uncertainty treatment.
   Needs: paired simulation + measurement data, or measurement data plus a full parameter set.
3. **Monitoring-system design** — sensor selection/placement/sampling as a design decision, with
   a cost-vs-diagnosability trade-off method.
   Needs: multi-sensor, synchronously sampled data.
4. **Closing the loop from field failures to design** — field anomaly/fault logs used to update
   DFMEA priors or design requirements.
   Needs: fleet/field data with fault logbooks.

The dataset criteria that follow: (a) design variants, (b) design metadata (geometry, winding,
materials), (c) simulation–measurement pairing, (d) multi-sensor, (e) fleet/field data with labels.
Plain single-machine benchmark sets (CWRU etc.) score on none of these.

Note also the ASME *Journal of Mechanical Design* "Design by Data" special issue (2025), which
explicitly lists "operational data of complex engineering systems used for condition monitoring,
fault diagnosis and digital twins" as an engineering-design dataset category — evidence that the
design community treats this as in scope when the design link is made explicit.

---

## 2. Repository-by-repository sweep

Legend for the "RED fit" column: **a** variants · **b** design metadata · **c** sim+meas ·
**d** multi-sensor · **e** field/fleet.

### 2.1 Zenodo (searched via the REST API — the web UI is currently bot-throttled)

| Dataset | Content | Licence | RED fit |
|---|---|---|---|
| **Interturn Short Circuit Fault Mitigation in PMSMs – Datasets** (Brno Univ. of Technology / CEITEC, 2026-07) — [zenodo.org/records/21717722](https://zenodo.org/records/21717722) | 3-phase PMSM drive, ITSC at 3/25, 6/25, 9/25 turns with stepped SC resistance; dq currents/voltages, fault current, Pin/Pout/losses, severity estimates; ωe = 1400, 2000 rad/s; 0.5/1.0/1.5 Nm; ~601 MB .mat + Live Scripts | CC BY 4.0 | severity ladder; includes loss channels → thermal/electrical co-design angle |
| **Diagnostics of ITSC in PMSMs with Online Fault Indicators – Dataset** (Brno/CEITEC, 2024-02) — [zenodo.org/records/15631383](https://zenodo.org/records/15631383) | Same group, various operating points and severities | check record | pairs with the above |
| **PMSM Fault Severity Estimation under Parameter Offsets and Non-Ideal Simulation Conditions** (Zhejiang Univ., 2026-07) — [zenodo.org/records/21450701](https://zenodo.org/records/21450701) | MATLAB simulation datasets + PyTorch conversions + code; "channel-selective physics–data fusion"; parameter offsets explicitly varied; ~874 MB | CC BY 4.0 | **c** — simulation under parameter uncertainty is exactly the design-stage problem |
| **CARE to Compare — wind turbine SCADA** (2024) — [zenodo.org/records/14006163](https://zenodo.org/records/14006163) | 95 datasets, 89 turbine-years, 36 turbines, 3 farms (1 onshore PT = EDP open data; 2 offshore DE); 45 labelled anomaly windows leading to faults, 50 normal; 86/257/957 features; 5.5 GB; CARE metric defined in *Data* 9(12):138 | CC BY-SA 4.0 | **e** — best public field dataset with fault logs; farm differences give a crude "design variant" axis |
| **Kelmarsh / Penmanshiel wind farms** (Cubico) | 6 + 14 turbines, 10-min SCADA, 2016–2022, UK | CC BY 4.0 | **e**, weaker labels than CARE |
| **PMSM Inverter Fault Dataset v1.0.0** (Bacha et al., 2024; *Data in Brief* 58:111286) — [zenodo.org/records/13974425](https://zenodo.org/records/13974425) | Inverter-driven PMSM: open-circuit, short-circuit, overheating in switches; 8 raw + 15 derived features; 10 Hz; 10,892 samples; 9 conditions; <1 MB | CC BY 4.0 | small; system-level (converter) faults |
| **Induction motor startup currents** — [zenodo.org/records/17048028](https://zenodo.org/records/17048028) | 1 healthy + 3 rotor-fault motors (1 BRB, 2 BRB, end-ring) | check | **a** (light) |
| **AURSAD — UR-3e screwdriving anomalies** — [zenodo.org/records/4487073](https://zenodo.org/records/4487073) | 2,045 samples, 5 classes, 100 Hz, 6.4 GB HDF5, `aursad` PyPI loader | CC BY 4.0 | robotics (RED-welcome domain) |
| **IMAD-DS** — [zenodo.org/records/12665499](https://zenodo.org/records/12665499) | Scaled robotic arm + brushless motor; audio + vibration + time series under domain shift (speed/load/noise) | check | **d**, domain-shift design |
| Force/torque labelled assembly data, Delta robot (2024) — [zenodo.org/records/13641620](https://zenodo.org/records/13641620) | Assembly-process anomaly detection | check | robotics |

### 2.2 Mendeley Data

| Dataset | Content | Licence | RED fit |
|---|---|---|---|
| **KAIST — Vibration & current dataset of 3-phase PMSMs with stator faults** — [data.mendeley.com/datasets/rgn5brrgrn](https://data.mendeley.com/datasets/rgn5brrgrn/4); *Data in Brief* 2023 (PMC9957734) | **Three PMSMs, 1.0 / 1.5 / 3.0 kW**, same faults (healthy, inter-coil SC, ITSC) at 8 severities, same speed/load; 1 accelerometer @ 25.6 kHz, 3 CTs @ 100 kHz; TDMS | CC BY 4.0 | **a + d** — the cleanest "product family" dataset for PMSMs |
| **KAIST — Industrial-scale motors under randomised speed/load** — 7 Mendeley sets + HVAC set (10.17632/5tt3zb2pns.1); *Data in Brief* 2025 (PMC12361783) | AC motors **1, 3, 5, 7.5 HP** + 1.5 kW HVAC; misalignment, bearing spalling, coil/inter-turn shorts (10/40/60 %), journal-bearing clearance, belt looseness; current 100 kHz, vibration/torque 25.6 kHz, RPM 100 kHz; ±4 %/±16 % random speed, 0–90 % load; >60 GB | CC BY 4.0 | **a + d** — scale-up axis for whatever is developed on the PMSM trio |
| **Univ. of Ottawa Electric Motor Dataset (UOEMD-VAFCVS)** — [data.mendeley.com/datasets/msxs4vj48g](https://data.mendeley.com/datasets/msxs4vj48g/2); PMC11636780 | Healthy, unbalance, misalignment, stator winding, voltage unbalance, bowed rotor, BRB, bearings; vibration + acoustic; constant and variable speed | CC BY 4.0 | **d** |
| **Univ. of Ottawa bearing sets (UORED-VAFCLS)** — [data.mendeley.com/datasets/y2px5tg92h](https://data.mendeley.com/datasets/y2px5tg92h/5) | 20 bearings × 3 states; accelerometer, microphone, load cell, Hall | CC BY 4.0 | **d** |
| **Haizhe AUV fault-diagnosis dataset** — [data.mendeley.com/datasets/7rp2pmr6mx](https://data.mendeley.com/datasets/7rp2pmr6mx/1); *Data in Brief* 2021 | Quadrotor AUV, 1,225 samples, 5 fault types (thrusters) | CC BY 4.0 | matches the *Applied Ocean Research* thread |

### 2.3 IEEE DataPort (mostly **subscription** — check LUT's institutional access before planning on these)

| Dataset | Content | Access |
|---|---|---|
| **Three-phase PMSM with ITSC faults of stator winding** (HUST) — [link](https://ieee-dataport.org/documents/three-phase-pmsm-itsc-faults-stator-winding-dataset); code github.com/XHX-HUST/PMSM-ITSC | Custom fault prototype; 12 torque–speed points × 9 shorted-turn levels × 3 SC resistances; 3-ph V, I, SC current; 66.9 GB | Subscription |
| **Synthetic dataset for IM broken rotor bar** (UFES, 2024) — [link](https://ieee-dataport.org/documents/synthetic-dataset-induction-motor-broken-rotor-bar-analysis) | **26 real motors' parameters** → 390 simulated scenarios (0–4 BRB × 3 loads); 3-ph currents @ 8 kHz; 4.4 GB; parameter PDF included | Subscription — **a + b + c** on paper, the best design-variant structure of any set found, if accessible |
| **Experimental database for rotor broken bar** (UFES) — [link](https://ieee-dataport.org/open-access/experimental-database-detecting-and-diagnosing-rotor-broken-bar-three-phase-induction) | Vibration 7.6 kHz, electrical 50 kHz; loads × severities × 10 repeats | Open access |
| Data: Short circuit and fault in IM, BLDC and PMSM — [link](https://ieee-dataport.org/documents/data-short-circuit-and-fault-induction-motor-bldc-and-pmsm) | Three machine types | check |
| GEM-based PMSM digital-twin simulation data | Gym-Electric-Motor high-fidelity sim under data-scarce conditions | check |

### 2.4 University / national repositories

| Dataset | Content | Licence | RED fit |
|---|---|---|---|
| **CREATOR Case — PMSM** (TU Graz / TU Darmstadt / JKU, CRC TRR 361) — [repository.tugraz.at/records/sns1d-77m43](https://repository.tugraz.at/records/sns1d-77m43), DOI 10.3217/sns1d-77m43; paper arXiv 2501.15921 / COMPEL 44(4) | **Complete design parameter set** (geometry, materials, winding scheme, electrical params), measured equivalent-circuit params, high-resolution recordings on 6 drive cycles; IM companion described in the paper | CC BY-NC 4.0 | **b + c** — the only public PMSM set with full design data; no faults, so it is the *design-side* half of a pairing |
| **USP PMSG benchmark for condition monitoring** — [github.com/InnovaPower/MitDev-Eletrica](https://github.com/InnovaPower/MitDev-Eletrica), Zenodo 10.5281/zenodo.15741561; *Data in Brief* 62:112040 (2025) | 2.5 kVA, 4-pole PMSG; **24 inter-turn/inter-winding SC cases** (D01–D24) + healthy; 3 speeds × 3 torques **scaled from the IEA 15 MW offshore reference turbine**; 32 channels @ 20 kHz incl. dq, converter, torque, speed, relay; pre/fault/post transients; 225 .mat, 1.2 GB; Python viewer | CC BY | direct hit for the offshore-wind PMSG thread; no demagnetisation cases though |
| **Rotating electromechanical system dataset** (UAQ Mexico / UPC) — CORA/CSUC Dataverse 10.34810/data2500; *Scientific Data* 13:873 (2026) | 1.43 kW IM + 4:1 gearbox + DC load; bearing, half/full BRB, unbalance, misalignment; gear wear 0/25/50/75 %; triaxial vib 3 kHz, 3 currents 4 kHz, 6 RTDs 1 kHz, thermal camera, encoder; ramps + 45-min stationary; 1,878 files | **CC BY-NC-ND 4.0** | **d** — but ND blocks redistributing derived data |
| **Paderborn KAt bearing DataCenter** — [mb.uni-paderborn.de/kat/…](https://mb.uni-paderborn.de/kat/forschung/bearing-datacenter/data-sets-and-download) | Synchronous motor current + vibration; 6 healthy, 12 artificially damaged, 14 run-to-failure damaged bearings | CC BY-NC 4.0 | **d**; artificial-vs-real damage is itself a test-design question |
| **NREL Gearbox Reliability Collaborative vibration** — [data.openei.org/submissions/738](https://data.openei.org/submissions/738) | Healthy vs field-damaged gearbox of the **same design**, 2.5 MW dynamometer; accelerometers + HSS RPM | CC BY | **e**, same-design comparison |
| **MaFaulDa** (UFRJ) — [www02.smt.ufrj.br/~offshore/mfs](https://www02.smt.ufrj.br/~offshore/mfs/page_01.html) | SpectraQuest simulator; 1,951 multivariate series; unbalance, misalignment (H/V), bearing faults; 13 GB | open | **d** |
| **NASA PCoE / PHM Society mirror** — [data.phmsociety.org/nasa](https://data.phmsociety.org/nasa/) | IMS bearings, C-MAPSS/N-CMAPSS, milling, servomotor ball-screw degradation, etc. | open | classical; C-MAPSS FD001–FD004 give operating-condition/fault-mode variants |
| **PHM Society data challenges** — [data.phmsociety.org](https://data.phmsociety.org/) | 2009 gearbox; 2023 gearbox degradation; **PHM Europe 2026: brushless-motor door actuator RUL (Crouzet motor)**; **PHM NA 2026: spur-gear surface-damage progression with vibration + ground-truth images (7 run-to-failure tests)**; 2024/2025: turbine/jet engines | challenge terms | 2026 sets are fresh and under-published |
| **CSUC / Fairdata (Finland)** — Etsin searched: no electrical-machine fault datasets found | — | — | Fairdata/IDA is the natural **deposit** target for LUT-produced derived data (DOI, FAIR compliance for the paper) |

### 2.5 figshare / 4TU / Dataverse / Dryad

| Dataset | Content | Licence |
|---|---|---|
| **Motor fault detection data** — [figshare 27216219](https://figshare.com/articles/dataset/MOTOR_FAULT_DETECTION_DATA/27216219); *Scientific Data* 12:1468 (2025) | 0.2 kW SCIM; phase removal, misalignment; vibration + voltage + current @ 50 kHz; 10 CSVs | CC BY |
| **Motor current & vibration for an e-motor-driven centrifugal pump** — 4TU.ResearchData 10.4121/2b61183e-… (2026); *Data in Brief* | System-level faults on a pump drivetrain | check |
| Harvard Dataverse, Dryad, DataverseNO | Searched; nothing electrical-machine-specific surfaced | — |

### 2.6 Hugging Face / GitHub / Kaggle / UCI

| Dataset | Content | Licence | RED fit |
|---|---|---|---|
| **FactoryNet** (Forgis Labs, ICML 2026) — `load_dataset("factorynet/factorynet")`; [github.com/Forgis-Labs/FactoryNet](https://github.com/Forgis-Labs/FactoryNet) | 6 embodiments (UR3e, KUKA KR10, Yu-Cobot, UR5 sim, CNC, UR3e-AURSAD); 27 anomaly types + counterfactual pairs; 23k executions (13.3k real, 9.8k synthetic); unified **Setpoint–Effort–Feedback–Context schema** | CC BY-NC-SA 4.0 | **a + c**; the S-E-F-C schema is itself a design-representation idea |
| **SIMSHIFT — electric motor rotor structural FE** (HF, arXiv 2506.12007) | Rotor at burst speed: press-fit + centrifugal loads; von Mises stress/deformation fields; 3,195 samples, ~4.8k nodes each, ~15 GB; OOD splits on geometry | CC BY 4.0 | **b + c** design-side surrogate data; no faults |
| **Paderborn LEA PMSM temperature** — [kaggle.com/datasets/wkirgsn/electric-motor-temperature](https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature) | OEM prototype PMSM; 185 h, 2 Hz; dq voltages/currents, speed, torque, coolant, stator yoke/tooth/winding, PM temperature | CC BY-SA | thermal thread; no faults |
| **UR3 CobotOps** — [archive.ics.uci.edu/dataset/963](https://archive.ics.uci.edu/dataset/963/ur3+cobotops) | 7,409 multivariate instances; joint currents/temps/speeds, gripper, protective stops, grip losses | CC BY 4.0 | robotics; weak labels |
| **MCC5-THU gearbox benchmark** — [github.com/liuzy0708/MCC5-THU-Gearbox-Benchmark-Datasets](https://github.com/liuzy0708/MCC5-THU-Gearbox-Benchmark-Datasets) | Variable conditions, compound faults, multiple severities | check | compound faults |
| Multi-mode fault datasets of 3-phase asynchronous motor (arXiv 2601.02278, Jan 2026) | Single + electro-mechanical compound faults; triaxial vib, 3-ph current, torque, key-phase; steady + transitional | repository not confirmed in abstract | **d**, compound faults |
| Meta-catalogues: [awesome-industrial-datasets](https://github.com/jonathanwvd/awesome-industrial-datasets) (190 sets), [phm_public_data](https://github.com/ShaunRBK/phm_public_data), [PHM_datasets](https://github.com/hustcxl/PHM_datasets), [awesome-bearing-dataset](https://github.com/VictorBauler/awesome-bearing-dataset), [Wind-turbine-available-data](https://github.com/cesartadeub/Wind-turbine-available-data), PHMD loader (*SoftwareX* 2025) | Use to re-sweep periodically | — | — |

---

## 3. Alternative design axis: same faults across different machine *topologies* (USP/InnovaPower trio)

The USP InnovaPower group (Tominaga et al.) has released three CC BY 4.0 datasets on
[github.com/InnovaPower/MitDev-Eletrica](https://github.com/InnovaPower/MitDev-Eletrica) that apply
the **same winding short-circuit protocol** to **different generator topologies** — the design
decision a wind-turbine designer actually makes.

### 3.1 What is strictly comparable and what is not

| | **PMSG-3phase** (*DiB* 62:112040, 2025; Zenodo 10.5281/zenodo.15741561) | **SCIG-3phase** (*DiB* 63:112286, 2025; Zenodo 10.5281/zenodo.17161986) | **Generators-Dataset** (*DiB* 57:111018, 2024; Zenodo 10.5281/zenodo.13685630) |
|---|---|---|---|
| Topology | PM synchronous generator, 4-pole, 2.5 kVA, 230 V, 6.3 A YY, 1800 rpm | Squirrel-cage induction generator, 4-pole, 2.5 kW, 230 V, 7.7 A YY, 1750 rpm | Wound-field synchronous generators: **A** 2 kVA salient-pole fixed-speed; **B** 3 kVA smooth-pole fixed-speed; **C** 2 kVA salient-pole variable-speed |
| Bench | Same bench, same prime mover (WEG 3.7 kW IM + CFW500), same Imperix B-Box, same Equacional manufacturer | ← identical | Three different benches/labs (São Carlos, Schulich, USP); DC-motor or IM prime movers; A/B via emulated transmission line (no converter), C via 3L-NPC + 2L converters, dSPACE |
| Fault set | 24 cases: 12 inter-turn (TURNS) + 12 inter-winding (WINDINGS), R = 2.6 Ω, 400 ms, derivation points D01–D24 with tabulated % distance from neutral | **Identical** derivations and identical 24-case list | Same D01–D24 scheme, plus phase-ground and phase-phase; not all faults on all benches |
| Operating points | 3 speeds (1200/1500/1800 rpm) × 3 torques (5.2/6.4/8.0 Nm), scaled from the IEA 15 MW reference turbine | identical | Bench-specific |
| Acquisition | 20 kHz, 3 s (1 s healthy → 0.4 s fault → recovery), 225 .mat, 1.2 GB, 32 variables incl. dq, references, PI actions, Vdc, duty cycles, torque, encoder, fault relay, fault current | 20 kHz, 3 s, 225 .mat, 35 variables (adds flux-observer flux, flux reference, observer angle) | ~977 Hz (1024 µs), ~260 ms records, CSV; A: 3,314 files/146 MB (19 features); B: 637 files/21 MB (reduced columns); C: 618 files/2.45 GB (51 features, generator + grid side) |
| Design metadata | Nameplate + derivation table | Nameplate + derivation table | Equivalent-circuit reactances and time constants per generator (Tables 7–9) |
| Repetitions | None ("all test combinations are unique") | None | Not stated |

**Tier 1 (rigorous core): PMSG vs SCIG** — same bench, same protocol, same file naming; the only
difference beyond topology is the control structure the topology forces (encoder-FOC vs
flux-observer-FOC), which is itself part of the design decision.
**Tier 2 (generalisation): WFSG A/B/C** — same fault scheme but 20× lower sampling, 12× shorter
windows, different labs and fault subsets; usable only after harmonisation (down-sample Tier 1 to
~977 Hz and 260 ms windows; restrict to the overlapping inter-turn / inter-coil cases).

### 3.2 Why this axis fits *Research in Engineering Design* better than the rating axis

- **Topology is a first-order design decision; rating is sizing.** RED already publishes
  alternative/topology selection as method (10.1007/s00163-026-00488-y "system alternative
  selection", 2026; 10.1007/s00163-019-00310-y product-family topology, 2019).
- **The design argument is stated in the data papers.** The SCIG paper: rotor electrically
  inaccessible, stator-only instrumentation, and "the effects of these faults on the measured
  signals are often mitigated or obscured by the control system itself". Diagnosability is thus a
  property of topology + control + sensor suite — a design property, not an algorithm property.
- **The comparison is an open, invited gap.** The PMSG paper states "different machine topologies
  exhibit unique behaviors when subjected to the same type of fault" and the SCIG paper explicitly
  declines to compare ("not the purpose of this work"). No cross-topology study using these sets was
  found (Sept 2026); the repo provides no harmonised set or comparison notebook.
- **Control-loop variables are recorded** (PI actions, references, duty cycles, observer states),
  enabling "co-design of controller and monitoring" — a question no motor-only dataset supports.
- The papers list *Machine Design* among their subjects — a small hook for the scope argument.

### 3.3 Weaknesses to design around

1. **n = 1 machine per topology, no repeats** → topology effect is confounded with unit-to-unit
   variation; no general "PMSG is more diagnosable than SCIG" claim is supportable from data alone.
   Remedy: present a *procedure*, generate topology-level populations with FEA/analytical models under
   parameter variation (the *Machines* 2026 approach), and use the measured machines as validation
   points — this also supplies the sim-to-real element.
2. **Tier 2 heterogeneity** (see above) — keep the core method on Tier 1; treat harmonisation as an
   explicit method step and Tier 2 as robustness. At ~977 Hz only fundamental-band indicators
   (negative-sequence, dq residuals) survive, which itself poses a useful "minimum sensing" question.
3. **Electrical signals only** (plus torque/speed) — fine for RED if the sensor-suite question is
   posed within the electrical domain (phase currents vs dq vs controller internals).
4. **Leakage channels**: `Ifault`, `Fault_Relay` are ground truth only and must be excluded from
   diagnostic inputs; the 1 s pre-fault segment inside "FAULT" files is healthy data (useful for
   onset detection, dangerous for naive file-level labelling).
5. **Single fault resistance (2.6 Ω)** — severity comes only from turn position (D-points).
6. **Lab scale (2–3 kVA)** — the 15 MW link is a proportional scaling of *operating points*, not of
   fault physics; state it as such.

### 3.4 Paper concepts on this axis

- **A. Design-stage diagnosability across generator topologies** — a topology-agnostic metric
  (e.g. minimum detectable severity at fixed false-alarm rate, or mutual information between
  stator-side features and severity, per operating point), computed for PMSG/SCIG (Tier 1) and
  WFSG A/B/C (Tier 2), feeding a topology-plus-sensing selection procedure. Position against the
  model-based structural-analysis diagnosability index (Zhang & Rizzoni, 2017) as its data-driven,
  cross-topology counterpart.
- **B. Transferability as a design property** — train on one topology, test on another; identify
  which physics-informed features transfer; derive monitoring-architecture rules for product
  families that span topologies. Closest to the existing hybrid-ML / transfer-learning work.
- **C. Two-axis design-space map** (outlook) — topology (USP) × rating (KAIST); different labs and
  protocols, so keep as an extension rather than the core.

---

## 4. Shortlist ranked by fit to the journal

| Rank | Dataset(s) | Framing it supports | Why it ranks here |
|---|---|---|---|
| 1 | **USP topology trio — PMSG + SCIG core, WFSG A/B/C as generalisation** (+ own FEA populations) | Design-stage diagnosability / transferability across generator topologies (Section 3) | Same faults, same protocol, different topologies — the design decision itself; open invited gap; CC BY 4.0; control-loop variables recorded; needs FEA to fix n = 1 |
| 2 | **KAIST PMSM trio (1.0/1.5/3.0 kW)** ± KAIST industrial-scale set (1–7.5 HP) | Design-for-diagnosability across a rating ladder within one topology | Only open PMSM set with identical faults on several ratings; CC BY 4.0; current + vibration at high rates; secondary validation axis for the same method |
| 3 | **ZJU parameter-offset simulation set + own FEA** | Simulation-to-measurement transfer as a design-stage validation method, with explicit design-parameter uncertainty | Extends the *Machines* 2026 FEA + transfer-learning work into a methodology; CC BY |
| 4 | **CREATOR Case PMSM (+ IM)** | Same as 3, but with a fully documented machine so the design→signal chain is reproducible by readers | Only open PMSM with full design data; CC BY-NC |
| 5 | **Brno/CEITEC ITSC sets (2024, 2026)** | Fault-tolerant-control and mitigation as design decisions; severity ladders with loss channels | Fresh (2026), CC BY 4.0, dq-frame signals ready for physics-informed features |
| 6 | **CARE wind SCADA (+ NREL GRC)** | Field-data → DFMEA prior updating / design-requirement derivation (mirrors the AfGNN-DFMEA precedent in RED) | Largest labelled field set; CC BY-SA; 3 farms as a variant axis |
| 7 | **FactoryNet / AURSAD / UR3 CobotOps** | Cross-embodiment diagnosis via a shared representation (design-representation contribution) | RED explicitly welcomes robotics; FactoryNet spans 6 embodiments; NC-SA licence |
| 8 | **Rotating electromechanical system / Paderborn KAt / Ottawa** | Sensor-suite design (which sensors, what rate) as a cost–diagnosability trade-off | Multi-sensor, synchronous; watch the NC-ND licence on the first |
| 9 | **SIMSHIFT motor rotor + PHM 2026 challenges** | Design-space-aware surrogates; fresh challenge data with imaging ground truth | Supporting roles |

Recommended: **Rank 1 as the core, Rank 2 as a second validation axis, Rank 3 to supply the
topology-level populations** — "a design-stage diagnosability method across machine topologies,
validated by simulation-to-measurement transfer". That is squarely the kind of framework/method
paper the journal's 2025–26 record shows it accepts, and it reuses the FEA, transfer-learning and
PMSM/SCIG fault-mechanism work already published.

---

## 5. Practical notes

- **Licences.** Mendeley/Zenodo sets above are mostly CC BY 4.0 (re-use and derived data fine).
  CREATOR and Paderborn are **NC**; the UAQ/UPC set is **NC-ND** (no derived-data redistribution).
  IEEE DataPort is largely subscription — confirm LUT access before designing around it.
- **Deposit your processed data.** RED authors are expected to provide a data-availability
  statement; Zenodo (DOI, CC BY) or Fairdata/IDA (Finnish, LUT-supported) are the natural targets.
  The "Design by Data" call spells out FAIR documentation expectations that reviewers in this
  community now look for.
- **Zenodo's web search is bot-throttled** at the moment; use the REST API
  (`https://zenodo.org/api/records?q=…&type=dataset`) for sweeps.
- **Checked with no relevant hits:** Fairdata/Etsin, Harvard Dataverse, Dryad, DataverseNO.
  **Not swept:** OpenML, Science Data Bank (CN), Kaggle beyond the named sets.

---

## 6. Sources

Journal scope and record: link.springer.com/journal/163/aims-and-scope; api.crossref.org
(ISSN 0934-9839). Datasets: links in the tables above; dataset papers in *Data in Brief*,
*Scientific Data*, *Data*, COMPEL, arXiv as cited. ASME JMD "Design by Data" CFP:
asmejmd.org/2025/02/18/call-for-papers-design-by-data-cultivating-datasets-for-engineering-design/.
