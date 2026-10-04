# Public Datasets for an AI-in-DFM Paper Aimed at the RED Special Collection

Survey date: 4 Oct 2026. Target: *Research in Engineering Design* (Springer), Special Collection
**AI in Design for Manufacturing**. Companion to `dataset-survey-RED.md` on branch
`claude/research-topics-summary-wsvzb0`, which did the same job for the condition-monitoring paper, and
to `METHODOLOGY.md` on that branch (this file is Phase 1 of that playbook).

---

## 1. What the call and the journal will accept

**The call** ([link.springer.com/collections/ejdehjghgg](https://link.springer.com/collections/ejdehjghgg),
read through r.jina.ai because Springer blocks plain fetches): open, **deadline 31 December 2026**.
Guest editors: Sara Behdad (Florida), Iñigo Flores Ituarte (Tampere), David Rosen (A*STAR), Charlie Wang
(Manchester), Yi Xiong (SUSTech), Yaoyao Fiona Zhao (McGill), Mingdong Zhou (SJTU).

It asks for AI (machine learning, data-driven methods, large language models) that "learns from historical
design and manufacturing data" and, in particular, for contributions that "advance fundamental understanding
of design processes, methodologies, and reasoning in DFM through AI": novel design theories, computational
design methods, human–AI interaction studies, and empirical case studies of design decision-making. Listed
topics: AI in DFM processes (additive manufacturing, injection moulding, machining, casting); restrictive
aspects (automated manufacturability checks, tolerance analysis, defect prediction); opportunistic aspects
(topology optimisation, generative design, lightweighting, functional integration); process selection and
planning, including cost-aware planning; manufacturing-system and production-line design; knowledge-based
and learning approaches (experience codification, knowledge transfer, intelligent guidelines); AI with
CAD/PLM (real-time feedback, design-for-X tools, intelligent digital twins); life-cycle-aware DFM
(cost–performance–carbon trade-offs, sustainable material and process selection, circular manufacturing);
human–AI collaboration (explainable AI, designer trust, decision support); case studies.

**Published in the collection so far:** one paper, *AfGNN: adaptive graph neural networks for causal failure
reasoning in DFMEA* (Liu, Li, Bao; RED 37:27, 29 June 2026, doi:10.1007/s00163-026-00490-4). It formalises
DFMEA knowledge as a causal graph and was evaluated on five public datasets plus a self-built automotive
failure knowledge graph; data and code "available upon reasonable request". It is the template this survey
aims at: a method tested on public data, framed as a reusable design workflow.

**The journal's own rule still applies.** Collection papers go through RED's normal review, and RED
desk-rejects papers that "primarily present case studies of individual design efforts or focus solely on
applying existing tools or methods". A defect classifier with a high accuracy is not a RED paper. The data
must let a method turn manufacturing evidence into a design-stage decision: a manufacturability rule with
stated confidence, a process or machine choice, a tolerance allocation, a cost–carbon trade-off.

## 2. Selection criteria

The deciding criterion, as in the first survey, is whether the data allow a *design* question; data quality
comes second. The analysis machinery of the first paper is meant to carry over: limit-of-detection rules
become design rules with confidence (the smallest feature a process makes reliably, the smallest defect a
test catches); the bootstrap meets/fails/uncertain table compares alternatives (processes, machines,
sensor or inspection suites); the transfer step tests whether what is learnt on one machine holds on another.
That requires several design alternatives produced under one protocol.

| Code | Criterion | Why it matters for RED |
|---|---|---|
| **D** | Design variants under one protocol: several geometries, features, design parameters, materials, processes or machines | The object of study is the comparison between alternatives, not the predictor |
| **M** | Machine-readable design description per specimen (CAD/STL/B-rep, feature dimensions, parameter table) | Needed to turn outcomes into rules a designer can apply |
| **O** | Measured manufacturing outcomes: defects, porosity, dimensional deviation, distortion, roughness, success/failure, cost, time, energy | The manufacturability evidence itself |
| **P** | In-process or in-line signals: melt-pool or thermal images, acoustic emission, forces, spindle power, weld current/voltage/OCT, injection pressure, end-of-line test signals | Brings in the author's signal-processing and detectability strength |
| **R** | Replication and/or several machines or labs | Uncertainty quantification (bootstrap) and the transfer step |
| **L** | Open download and licence (CC BY ideal; NC usable; ND blocks derived-data release); practical size | A data-availability statement with a DOI is expected |
| **N** | Novelty: recent and/or little used | Benchmarks used in hundreds of papers give a reviewer nothing new |
| **E** | Link to the author's domain (electrical machines, electromechanical systems, power electronics, monitoring) | Credibility and reuse of earlier work; a plus, not a requirement |

Scores in the tables: ✓ meets, ~ partly, ✗ no.

---

## 3. Headline findings

The sweep ran on 4 October 2026 as eight parallel searches: four by repository type (generalist
aggregators; machine-learning platforms; national labs, domain portals and university repositories; RED
precedent and the guest editors' own data) and four by topic (additive manufacturing; forming, moulding,
machining and welding; electrical-machine, electronics and battery manufacturing; CAD and other
design-representation data). Several thousand records were screened; about 300 were opened and checked on
their landing page or API record, and the six finalists were checked file by file (Section 6).

1. **Open data that link design alternatives to measured manufacturing outcomes are rare.** Most
   manufacturing datasets are condition-monitoring or defect-image sets of a single product, and most
   in-situ AM sets cover one geometry. Only a handful combine several design or process alternatives,
   one protocol, measured outcomes and replication.
2. **The author's own process chain has almost no open data.** No public dataset was found for hairpin
   forming, welding or stripping, coil winding, impregnation, magnet insertion, die-cast rotor cages or
   lamination stacking. The only hairpin item is a set of contact-resistance tests on reversible joints (DTU,
   September 2026). The electrical-machine domain enters through end-of-line testing (two new e-drive sets,
   September 2026) or as a secondary case, not as the core.
3. **No RED paper of 2023–2026 rests on a public manufacturing dataset.** Of about 64 RED papers screened,
   none used one; 26 declare no data and 8 offer data on request. The one paper in the collection keeps its
   domain data private. A paper on open data with a FAIR release of the derived data would stand out.
4. **The large CAD benchmarks carry labels or simulated performance only.** Feature recognition,
   assembly, generative design and topology optimisation sets have no measured manufacturing outcome, and
   shape-only process classification is saturated (reported accuracies of about 97–99 %).
5. **Dead ends worth recording:** the NIST Smart Manufacturing Systems test-bed portal no longer resolves;
   Korea's KAMP platform needs a login and blocks automated access; the León injection-moulding pair is
   embargoed until 31 December 2027; RWTH's MPCS-AM build is a single 324 GB archive; several promising
   Zenodo records are restricted, probably while under review.

---

## 4. Candidates by area

All entries below were opened on their landing page or API record by one of the search agents; figures
are copied from those records. Order of scores: D M O P R L N E.

### 4.1 Forming, moulding, machining and welding

| Dataset | Host, year | Alternatives and specimens | Outcomes | Signals | Replication | Size | Licence | D M O P R L N E |
|---|---|---|---|---|---|---|---|---|
| **RDDAC**, real deep drawing and cutting, [10.18419/DARUS-5589](https://doi.org/10.18419/DARUS-5589) | DaRUS (Stuttgart), v2.0 Sep 2026 | DP600 cups: 2 geometries (concave, convex) × 3 blank-holder forces (100/300/500 kN) × 3 lubrication patterns = 18 cells × 500 consecutive parts = 9,000 | 3D laser height maps after drawing (OP10) and after cutting (OP20); sheet-thickness and oil-film traverses | 4 load cells, total force, punch position, punch temperature | 500 per cell; one press; 396 matched FE simulations in DDACS | 87.0 GB (sample 174 MB) | CC BY 4.0; code MIT | ✓ ~ ✓ ✓ ✓ ✓ ✓ ✗ |
| **DDACS**, simulation twin of RDDAC, [10.18419/DARUS-4801](https://doi.org/10.18419/DARUS-4801) | DaRUS, v3.0 Jun 2026 | ≈32,000 FE simulations: 3 base geometries × min/max corners of curvature radius, bottom radius and wall angle × material scaling, friction, sheet thickness, blank-holder force | Stress, strain, thickness and displacement fields, incl. after springback (OP10, OP20) | – | Simulation | 646.9 GB (7.9 GB matched to RDDAC; 20 MB sample) | CC BY 4.0; code MIT | ✓ ✓ ~ ✗ ✗ ~ ✓ ✗ |
| U-Channel drawability, [10.5281/zenodo.15327950](https://doi.org/10.5281/zenodo.15327950) | Zenodo 2025 | 2,533 geometries from 4 parametric CAD families (STEP, mesh, graph, point cloud) | Simulated drawability labels and strains | – | – | 17.5 GB | CC BY 4.0 | ✓ ✓ ~ ✗ ✗ ✓ ✓ ✗ |
| BenDFM, [10.5281/zenodo.18622958](https://doi.org/10.5281/zenodo.18622958) | Zenodo 2026 | 20,000 synthetic bent sheet-metal parts with flat patterns | Feasibility labels, intrinsic vs machine/tool-configuration-dependent (simulated) | – | Simulated configurations | 3.1 GB | GPL-3.0+ | ✓ ✓ ~ ✗ ~ ✓ ✓ ✗ |
| Synthetic deep drawing, [10.18419/DARUS-5158](https://doi.org/10.18419/DARUS-5158) | DaRUS 2025 | 228 tool geometries × 10 blank-holder forces = 2,280 simulations; STEP | Simulated | – | – | 10.0 GB | CC BY 4.0 | ✓ ✓ ~ ✗ ✗ ✓ ✓ ✗ |
| DB4ISF, incremental sheet forming, [10.5281/zenodo.10000815](https://doi.org/10.5281/zenodo.10000815) | Zenodo 2023 | 76 real parts with CAD, CAM toolpaths and robot programs | 3D scans; deviation at every toolpath point | – | One cell | 3.7 GB | CC BY 4.0 | ✓ ✓ ✓ ✗ ~ ✓ ~ ✗ |
| Injection-moulding simulations, [10.5281/zenodo.18598121](https://doi.org/10.5281/zenodo.18598121) (+ 17831586) | Zenodo 2024–26 | 624 (+196) CAD geometries from the ABC set, random gate, Moldflow, PP-GF30 | Simulated warpage, shrinkage, fibre orientation, residual stress | Simulated fields | – | 32.8 GB (+2.0) | CC BY 4.0 | ✓ ✓ ~ ~ ✗ ✓ ✓ ✗ |
| SKZ/IPA ProBayes injection moulding (B2SHARE k0v7s-jf859, v64sz-f0f41) | B2SHARE 2022–23 | One "warpage shell" part; PP vs ABS with 70 % recyclate; 47 DoE points × 12 parts = 564 | OK/NOK, camera, scale, IR | 334 features from 9 sources | 12 per point | 107 + 78 MB | CC BY 4.0 (DOI redirect broken; use record ID) | ~ ✗ ✓ ✓ ✓ ✓ ~ ✗ |
| Sirris drying faults, [10.5281/zenodo.22027505](https://doi.org/10.5281/zenodo.22027505) | Zenodo 2026 | 2 moulds × 6 polymers; drying 0–4 h; 5,001 parts | Drying-adequacy labels | ≈75 cycle variables incl. cavity pressure | 83 batches | 12 MB | CC BY 4.0 | ~ ✗ ~ ✓ ✓ ✓ ✓ ✗ |
| Milling on three machines (LUH), [10.17632/zpxs87bjt8](https://doi.org/10.17632/zpxs87bjt8) | Mendeley 2023 | 9 end mills worn to end of life on 3 five-axis centres; identical workpiece and parameters | Flank wear | Dynamometer 25 kHz; drive torque/current 500 Hz | 3 machines | 9.1 GB | CC BY 4.0 | ~ ~ ✓ ✓ ✓ ✓ ~ ~ |
| KIT multimodal CNC milling 1 and 2, [10.35097/hvvwn1kfwf7qt48z](https://doi.org/10.35097/hvvwn1kfwf7qt48z), [10.35097/vnnu3n9z7ndsnhfd](https://doi.org/10.35097/vnnu3n9z7ndsnhfd) | RADAR4KIT 2025 | 33 + 54 runs; 3 component types (STEP + G-code in set 1); 3 materials; 3 tools; 8 induced anomaly types | Anomaly labels | Controller axis/spindle current and torque 500 Hz; force, acceleration 10 kHz | 2 machines | 44.6 + 55.2 GB | CC BY 4.0 | ✓ ✓ ~ ✓ ✓ ~ ✓ ~ |
| Pro2Future CNC machining repository, [10.17632/gtvvwmz7r7](https://doi.org/10.17632/gtvvwmz7r7) | Mendeley 2025 | 4 part geometries × aluminium and PLA; STEP/STL, NC code, tool lists | Energy and time per operation and part | Per-axis current, torque, load, power at 500 Hz | One machine | 186 MB | CC BY | ✓ ✓ ✓ ✓ ~ ✓ ✓ ✓ |
| Inconel 718 feature profiles, [10.7910/DVN/1G3SSB](https://doi.org/10.7910/DVN/1G3SSB) | Harvard Dataverse 2024 | 5 features (pockets, slots, hole), Box–Behnken | Power; energy per volume removed | Force, acceleration, AE, power | Repeats; 2 tools | 5.8 GB | CC BY-NC 4.0 | ✓ ~ ✓ ✓ ✓ ~ ✓ ~ |
| Resistance spot welding insights, [10.17632/rwh8kjzdch](https://doi.org/10.17632/rwh8kjzdch) | Mendeley 2025 (v3) | 495 welds, AISI 1010; electrode angle 0°/15°; current, time, force DoE | Pull-test force, nugget diameter, quality class; IR and RGB | Current and force | ≈250 per angle | 59 MB | CC BY 4.0 | ~ ~ ✓ ✓ ✓ ✓ ~ ✓ |
| Al busbar remote laser welding, [10.5281/zenodo.15833960](https://doi.org/10.5281/zenodo.15833960) | Zenodo 2025 | 12 power levels × 5 part-to-part gaps × 3 repeats | Weld quality only in the paper | Optical microphone | 3 repeats | 2.2 GB | CC BY 4.0 | ~ ✗ ~ ✓ ✓ ✓ ✓ ✓ |

### 4.2 Additive manufacturing

| Dataset | Host, year | Alternatives and specimens | Outcomes | Signals | Replication | Size | Licence | D M O P R L N E |
|---|---|---|---|---|---|---|---|---|
| **AIMEN Metal AM Open Repository (INTEGRADDE)**, [10.5281/zenodo.5031586](https://doi.org/10.5281/zenodo.5031586) | Zenodo, v2.0 2020 | One "CC coupon" design made by AIMEN (laser DED, powder, 13), MX3D (WAAM, 8), University West (WAAM, 8 scanned), IREPA (laser DED, wire, 3); plus T-coupons and a jet-engine part | Point-cloud scans against one common nominal for 29 coupons (none for IREPA); CT for AIMEN and MX3D | HDF5 logs with camera frames; MX3D current/voltage logs | 3–13 per producer | 35.5 GB (0.2–12 GB per producer) | CC BY 4.0 | ✓ ✓ ✓ ✓ ✓ ✓ ✓ ~ |
| **AIMEN WAAM Open Repository**, [10.5281/zenodo.17608626](https://doi.org/10.5281/zenodo.17608626) | Zenodo, Nov 2025 | Walls: 2 wires × 6 dwell times (0–240 s) = 12; STEP, AutomationML process plans | Clamped and released scans (distortion); radiography; hardness, macro- and micrographs | Arc voltage and current, wire and robot speed, thermocouples; IR and weld-camera video; FEM thermal and distortion predictions | One wall per condition | 9.1 GB | CC BY 4.0 | ✓ ✓ ✓ ✓ ✗ ✓ ✓ ~ |
| **NTNU PA12 dimensional and geometric accuracy**, [10.18710/DHACHZ](https://doi.org/10.18710/DHACHZ) | DataverseNO 2021 (v1.1 2023) | One artefact; 135 specimens over 3 builds at random orientations on a position grid, plus anchor parts | CMM dimensional and GD&T characteristics, each measured three times | Room climate only | 3 builds | 35 MB | CC0 | ✓ ~ ✓ ✗ ✓ ✓ ~ ✗ |
| NIST AMMT overhang X4/X16, [10.18434/M32233](https://doi.org/10.18434/M32233); registered set mds2-3761 | NIST 2020–25 | 4 and 16 identical IN625 parts with overhang and horizontal hole | XCT | 10 kHz melt-pool camera, layer camera, photodiode | Replicates | 0.34 GB registered; raw ≈80–100 GB | NIST open | ~ ✓ ✓ ✓ ✓ ~ ~ ✗ |
| NIST overhang/support artefact, [10.18434/M32112](https://doi.org/10.18434/M32112) | NIST 2020 | Overhang 5–85° with and without supports; CAD | None measured after the build | High-speed thermography | One build | 13.8 GB | NIST open | ✓ ✓ ✗ ✓ ✗ ✓ ~ ✗ |
| RWTH MPCS-AM, [10.7910/DVN/PHC9L3](https://doi.org/10.7910/DVN/PHC9L3) | Harvard Dataverse 2025 | 17 geometries incl. ISO/ASTM 52902 artefacts; CAD, CAM, job files | CT, optical and tactile metrology, density, tensile, distortion | Layer camera, optical tomography | One build | 324 GB, one archive | CC BY 4.0 | ✓ ✓ ✓ ✓ ✗ ~ ✓ ✗ |
| ORNL registered DED, [10.13139/OLCF/2446626](https://doi.org/10.13139/OLCF/2446626) | ORNL 2024 | One IN718 coupon (bulk, thin walls, overhangs) × 8 parameter conditions | XCT flaws registered to the toolpath | Melt-pool camera, positions | One per condition | Not stated | Globus account; licence not stated | ✓ ~ ✓ ✓ ~ ~ ✓ ✗ |
| SUPSI laser DED In718 series (7 Zenodo records, e.g. [10.5281/zenodo.3978982](https://doi.org/10.5281/zenodo.3978982)) | Zenodo 2020–21 | Tracks, thin walls, corners × speeds, spirals | Bead width, height, roughness | Coaxial melt-pool images | 2 repeats (walls) | 2.4 GB | CC BY 4.0 | ✓ ✓ ✓ ✓ ~ ✓ ~ ✗ |
| KU Leuven FFF thermal failure, [10.48804/B0CMEN](https://doi.org/10.48804/B0CMEN) | KU Leuven RDR 2026 | 256 single-wall prints; 4 wall CAD variants × print parameters | Thermally induced failure modes | IR video | DoE, one printer | 396 GB (3.35 GB image subset) | CC BY 4.0 | ✓ ✓ ✓ ✓ ~ ~ ✓ ✗ |
| 3D-printed hole accuracy (UPB), [10.17632/4h6ttzh9bf](https://doi.org/10.17632/4h6ttzh9bf) | Mendeley 2022 | Holes 2.3–10 mm; shells, layer height, speed, axis angle; 5 sites | Hole-diameter deviation | – | 5 sites | 32 MB | CC BY 4.0 | ✓ ~ ✓ ✗ ✓ ✓ ~ ✗ |
| Aalto 316L TPMS lattices, [10.5281/zenodo.7260218](https://doi.org/10.5281/zenodo.7260218) | Zenodo 2022 | Gyroid and diamond × 3 wall thicknesses × 5 replicates; 3D models | MicroCT geometric accuracy, tensile, corrosion | – | 5 replicates | 23.9 GB | CC BY 4.0 | ✓ ✓ ✓ ✗ ✓ ✓ ~ ✗ |
| TUHH design-guideline family (e.g. [10.15480/882.14567](https://doi.org/10.15480/882.14567)) | TUHH TORE 2020–26 | Support spacing; TPMS cells; metal-extrusion benchmark features; bipolar plates, 6 designs × 2 processes | Scan deviation, shrinkage, printability | – | Single lab | Not seen (bot wall) | CC BY / public domain | ✓ ~ ✓ ✗ ~ ~ ✓ ~ |
| r3DiM FFF resource use, [10.6084/m9.figshare.19314266](https://doi.org/10.6084/m9.figshare.19314266) | figshare 2022 | 68 equal-volume components × orientations = 184 prints; STL, G-code | Energy and material, per layer | Printer power logs | No repeats | 109 MB | CC BY 4.0 | ✓ ✓ ✓ ~ ✗ ✓ ~ ~ |
| Three hybrid processes compared (CIRP 2025), [10.17632/8cjjsxstfc](https://doi.org/10.17632/8cjjsxstfc) | Mendeley 2025 | One 316L artefact by friction surfacing, WAAM and laser DED (+ machining) at 3 labs | Cycle time, energy, distortion, hardness, tensile | Per-layer energy | 3 labs (process and lab confounded) | 141 MB | CC BY 4.0 | ✓ ~ ✓ ✓ ~ ✓ ✓ ~ |
| Arcam A2X time and energy, [10.17632/4ysymgxs7g](https://doi.org/10.17632/4ysymgxs7g) | Mendeley 2025 | 9 part designs in 6 build jobs | Per-layer energy, build time | Energy logs | No repeats | 87 MB | CC BY 4.0 | ✓ ✓ ✓ ✓ ✗ ✓ ✓ ~ |
| DeepSLM eddy-current monitoring, [10.5281/zenodo.7886192](https://doi.org/10.5281/zenodo.7886192) | Zenodo 2023 | 66 Ti64 parts in 7 prints | Porosity (Archimedes, per layer) | Eddy-current impedance on the recoater | 7 prints | 0.81 GB | CC BY 4.0 | ~ ~ ✓ ✓ ✓ ✓ ✓ ✓ |
| LUIS 316L/CuCrZr cluster incl. AM stator teeth ([10.25835/epj4ecfj](https://doi.org/10.25835/epj4ecfj) and companions) | LUIS Hannover 2023–25 | Multi-material parameter study, down-skin tabs, stator teeth | µCT, microscopy | Camera snapshots | Not stated | 0.1–0.6 GB | CC BY 3.0 / NC | ✓ ✓ ✓ ~ ~ ~ ✓ ✓ |

### 4.3 Electrical machines, electronics and batteries

| Dataset | Host, year | Alternatives and specimens | Outcomes | Signals | Replication | Size | Licence | D M O P R L N E |
|---|---|---|---|---|---|---|---|---|
| **End-of-line vibroacoustics of e-drive units**, [10.5281/zenodo.22311390](https://doi.org/10.5281/zenodo.22311390) (descriptor *Data* 11:257) | Zenodo, Sep 2026 | 58,249 tests of 54,505 units; 2 anonymised product variants; 4 test benches | System-level conformity (4.76 % non-conforming) | 13 processed spectra and order matrices: motor- and gearbox-housing acceleration, sound, torsional | 4 benches; 3,743 retests | 1.24 GB | CC BY 4.0 | ~ ✗ ✓ ✓ ✓ ✓ ✓ ✓ |
| **Gear metrology linked to EOL NVH**, [10.5281/zenodo.22808711](https://doi.org/10.5281/zenodo.22808711) | Zenodo, Sep 2026 | 3,157 gear-metrology records; 107 units with paired component and EOL tests (metrology matched for 14–18) | EOL non-conformity | Component and EOL order spectra | – | 0.58 GB | CC BY 4.0 | ~ ✓ ✓ ✓ ~ ✓ ✓ ✓ |
| Lenze-QI geared-motor EOL, [10.5281/zenodo.13854459](https://doi.org/10.5281/zenodo.13854459) | Zenodo 2024 | 5,771 tests; 700 anonymised variants with 62 coded configuration attributes | Quality grade 0–3 | EOL audio | One line | 11 GB | CC BY-NC 4.0 | ✓ ~ ✓ ✓ ~ ~ ✓ ✓ |
| DTU reversible hairpin joints, [10.11583/DTU.33464725.v1](https://doi.org/10.11583/DTU.33464725.v1) | DTU Data, Sep 2026 | Cu–Cu joints: contact area × preload vs a welded reference | Contact resistance | – | Lab | 28 MB | CC BY 4.0 | ✓ ~ ~ ✗ ~ ✓ ✓ ✓ |
| KU Leuven static eccentricity, [10.48804/MONDJS](https://doi.org/10.48804/MONDJS) (+ simulation set NSQJCU) | KU Leuven RDR 2025 | 0/25/50 % eccentricity × 4 directions on a 1.1 kW induction motor; magnetic-equivalent-circuit twin | Unbalanced magnetic pull | Voltage, current, temperature | One motor + twin | 1.7 GB | CC BY 4.0 | ✗ ~ ~ ✓ ~ ✓ ✓ ✓ |
| SynRM rotor assembly tolerances, [10.21227/hbkc-6q88](https://doi.org/10.21227/hbkc-6q88) | IEEE DataPort 2026 | 76-case FEA DoE of rotor-segment offsets; FEMM files | Simulated torque and ripple; one measured trace | – | One prototype | Small | CC BY, but DataPort login/subscription | ✓ ✓ ~ ~ ✗ ~ ✓ ✓ |
| Cardiff punched-edge magnetic properties, [10.17035/d.2017.0043126286](https://doi.org/10.17035/d.2017.0043126286) | Cardiff 2017/2024 | 2 non-oriented steels; properties vs distance from the punched edge | Local loss, permeability | – | One rig | 162 MB | CC BY 4.0 | ~ ~ ✓ ✗ ✗ ✓ ~ ✓ |
| HELLA LEDs × solder pastes (Kaggle `andreaszippelius/hellastudy-of-leds2`) | Kaggle 2023 | 1,800 LEDs: 9 package types × 5 solder pastes; thermal shock to 1,500 cycles | Void and crack ratios, thermal resistance | Transient thermal analysis, acoustic microscopy, X-ray at ageing stages | ≈40 per combination | 1.7 GB | CC BY-NC-SA 4.0; Kaggle login | ✓ ~ ✓ ✓ ✓ ~ ✓ ~ |
| TUM coin cells with induced production defects, [10.14459/2023mp1695276](https://doi.org/10.14459/2023mp1695276) | mediaTUM 2023 | Defect classes vs reference cells | EOL quality tests | Cycler and EIS data | Multi-cell sets | 974 MB | CC BY 4.0 | ✓ ~ ✓ ✓ ~ ✓ ✓ ✓ |
| InZePro formation, [10.5281/zenodo.13373274](https://doi.org/10.5281/zenodo.13373274) | Zenodo 2024 | Same electrodes in 4 cell formats; formation protocols; electrolyte volume | Capacity, EOL test | Formation curves, EIS | 4 institutes; 2–10 cells per configuration | 12 GB | CC BY 4.0 | ✓ ✓ ✓ ✓ ✓ ✓ ✓ ~ |
| Parallel-module factorial, [10.17632/zh58byr53c.2](https://doi.org/10.17632/zh58byr53c.2) | Mendeley 2024 | 54 conditions: interconnect resistance × chemistry × temperature × ageing | Current and temperature imbalance | Per-cell currents, thermocouples | One lab | 727 MB | CC BY 4.0 | ✓ ✓ ~ ✓ ~ ✓ ✓ ✓ |

### 4.4 Design-representation data without measured outcomes

Useful for demonstrating breadth, not as a core: MachinePlan-10K (10,000 B-reps with process plans and
computed machining time, [10.5281/zenodo.21653081](https://doi.org/10.5281/zenodo.21653081), CC BY); the
machining-feature sets MFCAD++, CADSynth, HeteroMF, HybridCAD++ and SMCAD (labels only); AutoMate (452k
Onshape parts with mates, Dryad, CC0); SimJEB, CarHoods10k and topology-optimisation sets (simulated
performance only); NIST PMI/GD&T test models (CAD only); BenDFM, U-Channel and the injection-moulding
simulations (Section 4.1). For language models: FailureSensorIQ (failure-mode–sensor questions, including
electric motors and generators, Apache-2.0) and student-made DFM guideline corpora on Hugging Face (no
licence, unvetted); no peer-reviewed public DFM guideline corpus was found.

### 4.5 Saturated benchmarks (avoid as the core)

CWRU and Paderborn bearings, Paderborn motor temperature, MVTec AD, NEU and Severstal steel surfaces,
casting-product images, WM-811K, SECOM, the Bosch production line, AI4I 2020, NASA and PHM 2010 milling,
the Michigan CNC tool-wear set, C-MAPSS, CAXTON (177 citations), and the CAD benchmarks ABC, DeepCAD,
Fusion 360 Gallery and MFCAD++. A reviewer reads work on these as "applying existing tools".

---

## 5. Precedent and positioning

**What RED has accepted near this topic (2023–2026).** No public manufacturing data; the framings that
worked were: a design activity turned into a computable representation offered as a reusable workflow
(AfGNN, producibility analysis); an index or threshold checked against independent ground truth (shape
complexity threshold between machining and AM, 10.1007/s00163-023-00429-z; Design Robustness Index,
10.1007/s00163-026-00485-1); a controlled comparison of frameworks or alternatives with effect sizes
(autoinjector reliability framework, 10.1007/s00163-026-00493-1; omitted measures in alternative selection,
10.1007/s00163-026-00488-y); and transparency of the decision logic. The detectability statistic, the
limit-of-detection rule and the decision table of the first paper fit the second and third patterns directly.

**Guest editors' open questions** (from their 2023–2026 output):

| Editor | Themes | Hook for this paper |
|---|---|---|
| Yaoyao Fiona Zhao | Data quality and imbalance; reproducibility of ML in AM; transferability between PBF and DED; digital-twin reusability; released Melt-Pool-Kinetics (CC BY) | The transfer test is her "transferability"; bootstrap and detection limits answer her reproducibility agenda |
| David Rosen | Process selection from shape (≈97–99 % already); feature recognition; review of ML for process selection, planning and DFM | Decisions that can abstain ("uncertain") and that use tolerance and cost, not shape alone |
| Iñigo Flores Ituarte | DED/WAAM melt-pool learning; low-cost sensing; generative AI from design to manufacturing; digital-twin design | Limit of detection of cheap versus expensive sensing; trust in digital twins |
| Sara Behdad | Disassembly, repairability, remanufacturing, battery health | Life-cycle-aware decisions |
| Charlie Wang, Yi Xiong, Mingdong Zhou | Slicing and process planning; fibre-composite AM; eco-design rules; topology optimisation with AM constraints; tolerance analysis of EV battery stacks | Rule codification; tolerance-driven decisions |

**Papers a new submission should cite or position against:** AfGNN (10.1007/s00163-026-00490-4); Safdar et al.
on PBF-to-DED transferability (10.1115/1.4065090); Xie et al. on digital-twin reusability
(10.1016/j.jmsy.2025.12.006) and on ML reproducibility in AM (10.1016/j.engappai.2025.112223); Yan, …, Rosen
on ML for process selection, planning and DFM (10.1016/j.eng.2025.11.034); BenDFM
(10.1007/s10845-026-02857-9); Ben Slama et al., machining-to-AM threshold (10.1007/s00163-023-00429-z); the
JMD "Design by Data" editorial (10.1115/1.4067871); and, for the chosen dataset, its descriptor papers.

---

## 6. Finalists checked file by file

These checks were made directly on the repositories (index files, file listings, sample files), not taken
from the search agents.

**RDDAC + DDACS (deep drawing).**
- Index (`process_parameters`): 9,000 rows, exactly 500 per cell over 2 geometries × 3 blank-holder forces ×
  3 lubrication patterns; point clouds present for 8,990 experiments, oil traverse for 8,877; recommended
  split 7,200 / 900 / 900.
- Each HDF5 file holds the force record (1,140 samples × time, four load cells, punch temperature, punch
  position, total force), a 208-point sheet-thickness traverse, an oil-film traverse of about 420 points, and
  3,200 × 2,000 height and luminescence maps after drawing and after cutting.
- The mean punch temperature warms up within each 500-part series (ranges of 1.5–7 K per cell, 20–32 °C
  overall), with up to ten interruptions per cell where it drops by more than 0.5 K. This is a natural drift
  inside every cell, the counterpart of the healthy drift in the first paper. Cell means differ by up to
  6 K, so temperature must be handled as a covariate when alternatives are compared.
- In the 18-file sample, peak total force is about 545–666 kN for the concave cup and 275–420 kN for the
  convex cup. Raw height maps are in sensor units and the after-cutting scan covers a smaller area, so quality
  characteristics require the point-cloud reconstruction and alignment provided by the MIT-licensed `rddac`
  package (PyPI, v2.0.0; `ddacs` v3.2.3 for the simulations).
- Remote access: DaRUS serves byte ranges. The 4,491-entry listing of the 41.6 GB convex archive took 4 s and
  one 9.4 MB experiment was read in under 3 s without downloading the archive, so all 9,000 experiments can be
  streamed and reduced to features without storing 87 GB.
- DDACS: 646.9 GB in 18.6–44.3 GB packages; `rddac.zip` (7.9 GB) holds the 396 simulations matched to the
  RDDAC conditions.
- What has been done with it: the descriptor paper (Baum et al. 2026, *Trans Indian Inst Met* 79:176,
  10.1007/s12666-026-03870-5; 2 citations) decomposes the simulation-to-reality deviation (geometry 77–92 % of
  the variance; blank-holder force up to 33 % of the remainder) and fits a gradient-boosted model of the
  residual (R² 0.81–0.92). It names transfer learning and uncertainty quantification as next steps and does
  not address design decisions.

**AIMEN INTEGRADDE (AM, four producers).** Archive contents listed remotely: scans (text point clouds of
94–424 MB each, plus Datapixel disparity maps) against one common nominal (`CCOUPON.stl`) exist for AIMEN
(13 coupons), MX3D (8) and University West (8), none for IREPA; CT volumes for AIMEN (13) and MX3D (8);
current/voltage logs for MX3D, HDF5 logs with camera frames for AIMEN. The cross-producer comparison
therefore rests on 29 scanned coupons from three producers and two processes.

**AIMEN WAAM.** Twelve walls (two wires × dwell times 0, 30, 60, 90, 120, 240 s); clamped and released scans
for eleven; FEM distortion predictions only for three walls, thermal predictions for ten; combined process
files with voltage, current, speeds and thermocouples; IR and weld-camera video; radiography as PDF reports.
One wall per condition.

**E-drive EOL and gear metrology.** The README confirms processed spectra only, no geometry, no acceptance
thresholds, a system-level conformity label, two anonymised variants and four benches that may confound
pooled models. The gear-metrology set links metrology to EOL results for 14–18 units only.

**NTNU PA12.** CC0; 135 specimens over three builds (plus 372 parts outside the main study); EOSINT P395 with
a 50/50 virgin/recycled PA2200 blend; Zeiss Duramax CMM; results table 33.7 MB.

---

## 7. Shortlist ranked by fit

| Rank | Dataset(s) | Design question it supports | Why it ranks here | Main risk |
|---|---|---|---|---|
| **1** | **RDDAC + DDACS** (deep drawing, Stuttgart) | When can a design-stage simulation or AI surrogate be trusted to accept, reject or send to trial a design–process alternative? | The only open set with a full factorial of design and process alternatives, 500 replicates per cell, in-process force, measured 3D outcomes and a matched simulation twin; CC BY; released 2025–26 and barely used | Two physical geometries; not AM; dataset owners plan transfer learning and uncertainty quantification |
| 2 | **AIMEN INTEGRADDE** (+ AIMEN WAAM) | Which process or producer can hold which tolerance class on which feature of a given design, and does a deviation model transfer between producers? | Same design made by several producers and processes, with scans, CT and process logs; CC BY; little used; matches three editors' interests (DED/WAAM, process selection, transferability) | 8–13 coupons per producer, one design, heterogeneous logs; WAAM set has one wall per condition |
| 3 | **NTNU PA12** | Achievable tolerance grade per feature and build orientation, with confidence | Clean replicated design (three builds, triple measurement), CC0, 35 MB; orientation is a genuine DfAM decision | No process signals; one machine and material |
| 4 | **E-drive EOL + gear metrology** (Széchenyi István University) | Cheapest adequate EOL channel set across four benches; gear tolerance → NVH rule | Author's domain; released September 2026; CC BY; multi-bench with retests | Test-system design rather than product design; anonymised; method nearly identical to the first paper |
| 5 | Pro2Future CNC energy + r3DiM + Arcam A2X + three-process CIRP set | Carbon-aware process selection at the design stage | Geometry linked to energy and time with drive signals; all CC BY | Small and heterogeneous; no replication |
| 6 | HELLA LEDs × solder pastes | Component–material selection and cheapest adequate inspection | Cleanest factorial with replication (9 × 5 × ≈40) | Reliability rather than manufacturing; NC-SA; Kaggle login |
| 7 | KIT multimodal CNC + LUH three-machine milling | Monitorability of a process plan; sensor-suite choice across machines | Controller drive signals on two or three machines; CC BY | Anomaly or wear labels, no part-design variation |
| 8 | U-Channel, BenDFM, injection-moulding and synthetic deep-drawing simulations | Breadth demonstrations of a decision method | Many geometry variants; mostly CC BY | Simulated labels only |

---

## 8. Recommendation

**Core dataset: RDDAC with its simulation twin DDACS.**

**Object of study, in one sentence:** the design decision, not the predictor — which design–process
alternatives can be accepted, rejected, or must be sent to physical trial, given what simulation and an AI
surrogate predict and what production scatter allows.

**How the first paper's machinery carries over**

| First paper | This paper |
|---|---|
| Three generator types under one fault protocol | 18 geometry × blank-holder-force × lubrication alternatives under one forming protocol, 500 parts each |
| Signal-to-drift ratio: fault signature over healthy drift | Effect-to-scatter ratio: difference between alternatives (springback, thinning, draw-in) over the scatter of 500 nominally identical parts, including the punch-temperature drift inside each series |
| Minimum detectable extent | Minimum resolvable design change: the smallest change in a design or process parameter whose effect exceeds production scatter plus simulation error, i.e. the resolution below which design iterations made on the simulation cannot be told apart in production |
| Bootstrap meets/fails/uncertain table → cheapest adequate sensor suite | Bootstrap meets/fails/uncertain table per alternative and tolerance → cheapest adequate process window (lowest blank-holder force, least lubrication), and whether simulation suffices or physical trials are needed |
| Transfer test across generator types | Transfer concave → convex, simulation → reality, and across lubrication regimes |
| Sensor-suite question | In-line verifiability: limit of detection of out-of-tolerance parts from press-force features |

**AI component.** A surrogate trained on DDACS (design and process parameters → springback and thinning;
gradient boosting on scalar characteristics, or a graph or point-cloud network on the fields), a
simulation-to-reality correction model trained on RDDAC, and calibrated uncertainty (for example conformal
intervals) feeding the decision table. The "uncertain" class is the model saying when it does not know.

**Fit.** To the call: restrictive aspects (manufacturability checks, tolerance analysis), AI with CAD/PLM
(intelligent digital twins), knowledge transfer. To the editors: Zhao's transferability and digital-twin
reusability, Rosen's process selection that can abstain, Flores Ituarte's digital-twin design. To RED's
accepted patterns: a threshold validated against independent ground truth and a controlled comparison of
alternatives with effect sizes.

**Second demonstration for breadth (optional, one section).** Apply the same decision layer to a different
process: NTNU PA12 (achievable tolerance by build orientation; cheap, CC0) if time is short, or INTEGRADDE
(process and producer selection in metal AM) if an AM emphasis is wanted for this editorial team.

**Keep in reserve:** the e-drive EOL and gear-metrology sets. They are in the author's domain and new, but
the question they answer is test-system design, and the method would repeat the first paper almost
unchanged; they suit a separate paper.

**Risks and how to handle them**
- *Two physical geometries:* treat them as validation points, use DDACS for the design space, test transfer
  between them, and state the limitation as a threat to validity (as the first paper did with one machine
  per topology).
- *The dataset owners name transfer learning and uncertainty quantification as next steps:* frame the paper on
  design decisions for the RED readership, cite their work, start soon, and consider contacting them.
- *Outcomes need point-cloud alignment:* run the `rddac` preprocessing on the 18-file sample first and fix a
  small set of scalar quality characteristics (springback at defined sections, flange draw-in, wall-angle
  deviation, thinning) before streaming all 9,000 files.
- *No tolerances in the data:* treat tolerances as design requirements and report decisions over a range of
  requirements, as the first paper did with e_req.
- *Not AM, no electrical link:* acceptable under the call's "e.g." list; the in-line force-signal analysis
  carries the author's signal-processing strength.

**Data plan.** Stream all 9,000 RDDAC files through HTTP range requests and keep only extracted features
(tens of MB); download `rddac.zip` (7.9 GB of matched simulations) and the DDACS index; stream further DDACS
packages only if the surrogate needs them. Then the pipeline of the first paper: features → statistics →
decision tables → transfer → figures → tables, with `run_all.sh`, fixed seeds and generated tables.

---

## 9. Practical notes

- **Licences.** RDDAC and DDACS CC BY 4.0, code MIT; INTEGRADDE and AIMEN WAAM CC BY 4.0; NTNU CC0; e-drive
  EOL and gear metrology CC BY 4.0. Lenze-QI (CC BY-NC) and HELLA (CC BY-NC-SA) allow analysis but not
  commercial reuse; BenDFM is GPL-3.0.
- **Access.** DaRUS and Zenodo both serve byte ranges, so archives can be listed and read file by file
  (Python `remotezip`). The RDDAC and DDACS code is on PyPI, so their GitHub repositories are not needed; if
  one is, it should be attached to the session properly.
- **Contacts.** RDDAC/DDACS: Sebastian Baum and Pascal Heinzelmann (University of Stuttgart). INTEGRADDE:
  Carlos González-Val (AIMEN). WAAM: Félix Vidal (AIMEN). E-drive EOL: Krisztián Horváth (Széchenyi István
  University).
- **Deposit.** Derived features and code on Zenodo with a DOI under CC BY 4.0; this alone sets the paper apart
  from the one already in the collection.

---

## 10. Coverage log

- **Generalist aggregators:** DataCite (with repository-prefix scans), OpenAIRE Graph, Zenodo API,
  figshare, Dryad, Harvard Dataverse and other Dataverse installations (Borealis, DataverseNO, DaRUS, KU
  Leuven RDR, Recherche Data Gouv, DataverseNL), Mendeley Data, 4TU.ResearchData, B2SHARE.
- **Machine-learning platforms:** Kaggle (≈150 queries, 2,253 unique records), Hugging Face (incl. the
  Papers-with-Code archive of 15,008 datasets), UCI (all 689 datasets), OpenML (6,434 datasets by name),
  IEEE DataPort, PHM Society repository and challenges 2024–2026, Roboflow, Code Ocean, NASA PCoE (all 21
  sets), Fraunhofer IPT/FFB catalogue.
- **National labs and domain portals:** NIST PDR (all 1,465 records filtered; AM Data Collection), ORNL
  Constellation, OSTI, Materials Data Facility, PNNL, LLNL, NREL, data.nasa.gov, America Makes (member-only),
  CESMII (none), data.europa.eu, Fraunhofer Fordatis, KIT, TUM (mediaTUM via OAI), RWTH, ETH, DLR, Empa, UK
  repositories (Cambridge, Edinburgh, Bristol, Sheffield, Manchester, Nottingham, Imperial), TU Delft/4TU,
  KU Leuven, DTU, SND, Fairdata/Etsin (incl. Aalto, Tampere, LUT), KAMP (login), Science Data Bank, NIMS MDR,
  CiNii.
- **Literature:** Crossref (all 98 RED records since 2023; citation counts for about 100 descriptor papers),
  Europe PMC, arXiv; reader proxy for Springer and other blocked pages.
- **Not usable today:** OpenAlex (daily budget exhausted), Semantic Scholar (rate-limited), GitHub API
  (blocked in this session; GitHub-hosted datasets identified through papers and mirrors).
- **Topics with no relevant open data:** hairpin forming, welding and stripping; coil winding and slot fill;
  impregnation; magnet gluing; cage porosity; lamination interlocking or welding; solder-paste inspection
  linked to pad or stencil design; power-module void or sintering process data.

---

## 11. Sources

Call for papers: link.springer.com/collections/ejdehjghgg (read through r.jina.ai). Journal scope and
record: link.springer.com/journal/163; api.crossref.org (ISSN 0934-9839). Datasets: DOIs in the tables
above, checked on their landing pages or API records on 4 October 2026. Descriptor papers as cited.
