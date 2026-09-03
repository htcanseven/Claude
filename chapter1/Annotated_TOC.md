# High-Speed Electrical Machines and Drives

## Design for Industrial and Mobile Applications

**Annotated table of contents for the Wiley proposal** — draft for discussion among the authors

Authors: Hüseyin Canseven, Ilya Petrov, Juha Pyrhönen (LUT University), with named contributors per chapter.

Alternative titles for discussion: *High-Speed Electrical Machines: Design under the Speed Constraint* · *Design of High-Speed Electrical Machines and Drives*. The recommended title carries both market-broadening words, *drives* and *applications*, and answers the editor's stated interest in "a clear focus on the updated applications in the area".

## 1. Positioning

This is a design book for the regime in which conventional electrical-machine design stops working. It is conceived as the companion to *Design of Rotating Electrical Machines* (Pyrhönen, Jokinen, Hrabovcová; Wiley, 2nd ed. 2014): that book gives the general design process for the whole machine landscape; this one takes the reader to where the general rules fail and shows what replaces them. Nothing covered in the earlier book is repeated; each chapter states which conventional assumption breaks at high speed, why, and what the designer does instead.

Between the review papers on high-speed machines and the research monographs there is no title that gives a practising engineer a design procedure. This book does. Its distinctive claim is that high-speed design runs the other way round from conventional practice: the mechanical and rotordynamic limits fix the rotor first, the converter fixes the admissible pole number, and the electromagnetic design is fitted into the space that remains. The book is ordered accordingly, constraints before electromagnetic design, and two machines are carried through every chapter to make the procedure concrete: a two-pole gearless industrial compressor drive and the six-pole 120 kW, 30 000 r/min traction machine of the EU Voltcar project. They represent the two design paradigms that organise the whole text, the gearless industrial machine judged on availability and the mass-limited mobile machine judged on specific power.

**Readership.** R&D and application engineers at compressor, turbomachinery, e-mobility and aerospace companies; drive-system engineers who must supply such machines; graduate students and researchers in electrical machines and drives. End-of-chapter problems and worked examples make it usable as a supplementary text in graduate courses on electrical machine and drive design.

**New material.** The fP classification criterion for high-speed drives, calibrated against a survey of built machines; the constraints-first sizing procedure; the corrected scaling analysis, including the result that a doubling of design speed degrades the rotordynamic margin sixteenfold; converter co-design rules for the SiC and GaN era; and case studies from current projects, carried from specification to measured validation.

**Companion material.** A set of Python notebooks reproducing every analytical figure in the book and implementing the design procedures of Chapters 6, 7, 9 and 10, published on the Wiley companion site.

## 2. Structure at a glance

Budgets use the publisher's formula of 600 words per page and two illustrations per page. The target is 450 pages against the 500-page ceiling.

| Part | Ch. | Title | Pages | Words | Figures | Lead |
|---|---|---|---|---|---|---|
| I  The high-speed design space | 1 | Introduction: what changes at high speed | 26 | 12 000 | 9 | authors (written) |
| | 2 | Applications and system architectures | 34 | 14 100 | 18 | authors; J. Saari |
| | 3 | Machine topologies for high speed | 38 | 14 400 | 26 | authors |
| II  The constraints that bind first | 4 | Rotor mechanical design and magnet retention | 38 | 14 400 | 26 | J. Sopanen's group; I. Petrov |
| | 5 | Rotordynamics and vibration | 30 | 11 400 | 20 | J. Sopanen's group |
| | 6 | Bearings, lubrication and seals for high-speed rotors | 32 | 12 300 | 20 | J. Sopanen's group; bearing specialist |
| III  Electromagnetic design within the constraints | 7 | Sizing under the speed constraint: the inverted procedure | 36 | 14 400 | 20 | authors |
| | 8 | AC winding losses and conductor design | 28 | 11 100 | 18 | I. Petrov; A. Belahcen |
| | 9 | Losses, cooling and the thermal budget at kilohertz frequencies | 44 | 17 100 | 28 | A. Belahcen; I. Petrov; J. Saari; J. Nerg |
| IV  Delivery: the drive and the applications | 10 | The drive: converter interface and control at high fundamental frequency | 42 | 16 200 | 28 | P. Peltoniemi; L. Aarniovuori |
| | 11 | Industrial case studies: compressor drive and ORC generator | 28 | 9 300 | 22 | authors; J. Saari; L. Aarniovuori |
| | 12 | Mobile case studies: traction, aerospace and e-turbo | 30 | 9 900 | 24 | authors; aerospace contributor |
| | | **Chapters 1–12** | **406** | **156 600** | **259** | |
| | | Front matter, appendices A–D, index | 40 | | | |
| | | **Total** | **446** | | | |

## 3. Devices used throughout the book

**Two running machines.** The two-pole industrial compressor drive and the six-pole Voltcar traction machine are specified in Chapter 2, given their rotor retention in Chapter 4, their rotordynamic verification in Chapter 5, their bearings in Chapter 6, their electromagnetic sizing in Chapter 7, their windings in Chapter 8, their losses and loss budget in Chapter 9, their converters in Chapter 10, and are assembled into complete, measured designs in Chapters 11 and 12. Every design chapter therefore ends with the same two worked examples, and the reader can follow one machine through the whole procedure.

**A closing comparison in every design chapter.** Chapters 3 to 10 each close with a short section stating how the industrial and the mobile machine resolve that chapter's trade-off differently. This is the industrial-versus-mobile spine made explicit.

**The DREM boundary.** Each chapter opens by naming the conventional assumption it will replace, with a reference to the corresponding treatment in *Design of Rotating Electrical Machines*, so that the two books can be used together without overlap.

**Problems and notebooks.** Each chapter carries six to ten end-of-chapter problems, at least two of them built on the running machines, and a pointer to the companion notebook that reproduces the chapter's figures and design calculations.

**One notation.** A single symbol table (Appendix B) follows the conventions of the earlier book so that readers move between the two without relearning symbols.

## 4. Chapter abstracts

### Part I — The high-speed design space

#### Chapter 1. Introduction: what changes at high speed

*Written; supplied with the proposal as the sample chapter.*

High-speed machine design is not conventional design at higher frequency; it is a distinct discipline in which the ordinary margins are consumed and constraints that a mains-frequency designer treats as background compete with one another. The chapter opens with the question the literature answers inconsistently, what "high speed" means, and compares the three criteria in use: peripheral speed, which is the mechanical measure; the empirical n√P criterion; and the fP product, proposed here as a drive-system measure because it alone contains the pole number. The two design paradigms are introduced, the gearless industrial machine and the mass-limited mobile machine, and the physical constraints are set out in the order in which they bind: rotor stress, rotordynamics, windage and thermal loading. A scaling analysis then shows that the commonly quoted exponents describe overspeeding an existing machine rather than designing a new one; along the design path a speed doubling leaves windage unchanged, doubles iron loss, and degrades the rotordynamic margin sixteenfold, which is the constraint that actually terminates the pursuit of speed. The power electronic interface is presented as the gatekeeper that decides which topology is feasible at all. The chapter closes with the trilemma of mechanical, electromagnetic and thermal demands and the plan of the book.

Sections: 1.1 The high-speed landscape · 1.2 The two paradigms: industrial and mobile machines · 1.3 Fundamental physical constraints · 1.4 The role of the power electronic interface · 1.5 Scaling laws and dimensional analysis · 1.6 Summary: framing the design challenges ahead.

Budget: 26 pages, 9 figures, 4 tables. New: the fP criterion; the design-path scaling analysis and the rotordynamic result. DREM boundary: assumes the reader knows conventional sizing and loss estimation; derives nothing that the earlier book contains.

#### Chapter 2. Applications and system architectures

The chapter establishes why high-speed machines exist and why the two paradigms diverge. In industry the converter made it possible to move the speed conversion from a gearbox into the electrical domain, and the gearbox was deleted: centrifugal compressors, wastewater aeration blowers, organic Rankine cycle and turbo-expander generators, and subsea and hermetic process machines are treated with their economics of availability, oil-free operation and total cost of ownership. In mobile applications the converter was needed anyway and high speed bought mass instead, so the gearbox was kept: electric traction and its geared high-speed optimum, hybrid-electric and all-electric aircraft propulsion and generation, and electrically assisted turbochargers and turbo-compounding above 100 000 r/min. Emerging drivers are surveyed, including heat-pump and hydrogen and cryogenic compression and flywheel storage. The chapter then presents a survey of built and published high-speed machines, spanning several decades of power and speed, and maps them onto the three classification criteria of Chapter 1; this is where the fP criterion receives its calibration. It closes by specifying the two running machines and stating the architecture-selection logic, total cost of ownership against specific power, that governs every later trade-off.

Sections: 2.1 The direct-drive transition in industry · 2.2 Gearless industrial units: compressors, aeration blowers, ORC and turbo-expanders · 2.3 Subsea and hermetic process machines · 2.4 Electric traction and the geared high-speed optimum · 2.5 Aerospace and hybrid-electric propulsion · 2.6 e-Turbochargers, turbo-compounding and the >100 000 r/min class · 2.7 Emerging drivers: heat pumps, hydrogen and cryogenic compression, flywheels · 2.8 Architecture selection: total cost of ownership against specific power · 2.9 A survey of built machines: calibrating v_tip, n√P and fP · 2.10 The two running machines specified.

Budget: 34 pages, 18 figures, 3 tables. New: the machine survey and the calibrated criteria; the architecture-selection logic. Contributors: J. Saari (industrial machines); LUT turbomachinery group to be approached for the process side.

#### Chapter 3. Machine topologies for high speed

Topology is chosen under the speed constraint before any electromagnetic optimisation, and this chapter compares the candidates on that basis. Solid-rotor induction machines, slitted, coated and copper-caged, are treated first because they reach the highest peripheral speeds and remain the industrial workhorse; laminated-rotor induction machines follow, with the speed ceiling imposed by the central bore. Synchronous reluctance and permanent-magnet-assisted reluctance machines are assessed for the traction paradigm, and switched reluctance is given a bounded treatment, because its asymmetric-bridge converter falls outside the drive-interface thread that runs through the book. Surface-magnet synchronous machines are presented as sleeve-dominated designs and interior-magnet machines as bridge-dominated ones, and the winding choice at high fundamental frequency, distributed, concentrated and fractional-slot, is compared on loss, harmonic content and manufacturability. A short section explains why axial-flux and other disc geometries are mechanically and rotordynamically hostile at high speed. The chapter closes with the topology decision for each running machine and the reasons the two paradigms choose differently.

Sections: 3.1 Topology selection under the speed constraint · 3.2 Solid-rotor induction machines · 3.3 Laminated-rotor induction machines and their speed ceiling · 3.4 Synchronous reluctance and PM-assisted SynRM · 3.5 Switched reluctance: capability and converter mismatch · 3.6 Surface-magnet PMSM: the sleeve-dominated design · 3.7 Interior PM: bridges, saliency and field weakening · 3.8 Winding choice at high frequency · 3.9 Axial-flux and other emerging topologies at high speed · 3.10 The industrial and the mobile choice.

Budget: 38 pages, 26 figures, 2 tables. DREM boundary: topologies are compared only on their high-speed behaviour; their general theory is referenced.

### Part II — The constraints that bind first

#### Chapter 4. Rotor mechanical design and magnet retention

The rotor material limit is the one hard boundary in high-speed design, and this chapter gives the designer the tools to work against it. Centrifugal stress is derived for solid, hollow and laminated rotors, including the doubling caused by a central bore, and the mechanical and thermal properties of magnet materials are set out as design limits. The two retention families are developed in full: carbon-fibre sleeves, with filament-winding tension, pre-stress, magnet lift-off at overspeed and the electromagnetic price paid in effective air gap; and metallic sleeves in Inconel and titanium with shrink-fit design. Interference fits, thermal growth and assembly tolerance are treated together because they interact. Interior-magnet bridges and ribs are optimised for the narrow window between leakage and strength. Fatigue life, overspeed margin and burst containment are addressed as qualification requirements rather than afterthoughts, and shaft joints, stack retention and rotor assembly are covered as the manufacturing counterpart of the analysis. The chapter closes with the retention design of the two running machines.

Sections: 4.1 Centrifugal stress in solid, hollow and laminated rotors · 4.2 Magnet materials: mechanical strength and thermal limits · 4.3 Carbon-fibre sleeves · 4.4 Metallic sleeves and shrink-fit design · 4.5 Interference fits, thermal growth, assembly tolerance · 4.6 IPM bridges and ribs · 4.7 Fatigue life, overspeed margin, burst containment · 4.8 Shaft joints, stack retention, rotor assembly · 4.9 Retention design of the two running machines.

Budget: 38 pages, 26 figures, 2 tables. Contributors: J. Sopanen's group (stress, fits, fatigue) with I. Petrov (magnet and bridge design). DREM boundary: the earlier book treats rotor mechanics only at conventional speeds.

#### Chapter 5. Rotordynamics and vibration

Along the design path that respects the material limit, the first bending critical speed falls as the cube of the design speed, so most high-speed machines must run supercritically. This chapter makes that manageable. Rigid and flexible rotor behaviour, critical speeds, Campbell diagrams and gyroscopic stiffening are developed for slender rotors with the shaft extensions, sleeves and solid bodies that real machines carry. Subcritical and supercritical operation are compared, and high-speed balancing is treated as a design activity rather than a workshop afterthought. Bearing stiffness and damping enter as the rotordynamic inputs that Chapter 6 then supplies, and the strategies for passing through resonance, squeeze-film and active damping, are set out. Electromagnetic force harmonics are linked to structural response, vibration and noise, connecting the chapter to the loss and harmonic content of Chapters 9 and 10. The chapter closes with the rotordynamic verification workflow applied to the two running machines.

Sections: 5.1 Rigid and flexible rotor behaviour · 5.2 Critical speeds, Campbell diagrams, gyroscopic effects · 5.3 Subcritical and supercritical operation · 5.4 High-speed balancing · 5.5 Bearing stiffness and damping as rotordynamic inputs · 5.6 Passing through resonance: damping strategies · 5.7 Vibration and noise: electromagnetic forces and structural response · 5.8 Rotordynamic verification of the two running machines.

Budget: 30 pages, 20 figures, 2 tables. Contributors: J. Sopanen's group; 5.7 jointly with A. Belahcen (electromagnetic excitation). DREM boundary: not covered in the earlier book.

#### Chapter 6. Bearings, lubrication and seals for high-speed rotors

The first practical question an industrial reader brings to a high-speed machine is which bearing, lubricated how, lasting how long, and no competing title answers it as a design chapter. This one does, treating the tribology of the support system across three orders of magnitude of cost. Rolling-element bearings are covered with hybrid ceramics, cage design, preload, the lubrication regimes from grease through oil-mist to under-race oil, and Dn limits and life at high speed. Fluid-film bearings, tilting-pad and grooved journal and gas bearings, and air-foil bearings with their lift-off, load capacity and whirl behaviour follow. Active magnetic bearings are treated from actuator sizing and sensing through the control interface and losses to touchdown bearings and drop events. Bearing friction losses are quantified and placed in the loss budget beside windage, where they belong. Seals are given their own section, labyrinth, brush and dry gas seals, seal windage and heating, and the hermetic designs of the industrial paradigm. Damage mechanisms close the technical part, wear, fretting and the tribological face of bearing currents, and the chapter ends with the bearing selection for the two running machines.

Sections: 6.1 The bearing question at high speed: load, Dn, life, loss and cost · 6.2 Rolling-element bearings: hybrid ceramics, cages, preload, lubrication regimes, Dn limits and life · 6.3 Fluid-film bearings: tilting-pad, grooved journal and gas bearings · 6.4 Air-foil bearings · 6.5 Active magnetic bearings: actuators, sensing, control interface, losses, touchdown bearings · 6.6 Bearing friction losses in the loss budget · 6.7 Seals: labyrinth, brush and dry gas seals, seal windage, hermetic designs · 6.8 Damage mechanisms: wear, fretting and bearing currents · 6.9 Bearing selection for the two running machines.

Budget: 32 pages, 20 figures, 3 tables. Contributors: J. Sopanen's group (bearing-rotor interaction, fluid-film and magnetic bearings); an industrial bearing application specialist to be identified for lubrication, life and seals. DREM boundary: not covered in the earlier book. New: bearing losses and seal windage placed in the high-speed loss budget.

### Part III — Electromagnetic design within the constraints

#### Chapter 7. Sizing under the speed constraint: the inverted procedure

This is the book's central chapter. It shows why the conventional sizing loop, choose loadings, size the bore, verify mechanically, produces machines that are electromagnetically elegant and mechanically impossible at high speed, and it replaces it with a procedure that runs from the tip-speed and rotordynamic limits of Chapters 4 and 5 inward to the electromagnetic design. Pole number is chosen as a trade between stator mass and fundamental frequency, with the converter capability of Chapter 10 as the constraint. Air-gap length is set against windage, thermal margin and harmonic content rather than torque density alone. Magnetic and electric loading limits are re-derived for the kilohertz range, and slot and tooth geometry for high-frequency operation. A section on optimisation-based multiphysics sizing shows how the procedure is embedded in a modern coupled workflow. The procedure is summarised as a flowchart and then executed in full for both running machines, the two-pole industrial and the six-pole mobile design, so that the reader has a complete worked example of each paradigm.

Sections: 7.1 Why the conventional sizing loop fails at high speed · 7.2 The inverted procedure · 7.3 Pole number selection · 7.4 Air-gap length · 7.5 Magnetic and electric loading limits in the kilohertz range · 7.6 Slot and tooth geometry for high-frequency operation · 7.7 Optimisation-based multiphysics sizing · 7.8 Procedure summary and flowchart · 7.9 Worked sizing of the two running machines.

Budget: 36 pages, 20 figures, 4 tables. New: the procedure itself. Authors only. DREM boundary: the earlier book's sizing chapter is the reference for every step that is unchanged.

#### Chapter 8. AC winding losses and conductor design

A slot conductor sized on its direct-current resistance is wrong once the skin depth approaches its dimensions, which at kilohertz fundamentals it does. Skin and proximity effects in slot conductors are derived and the circulating currents in parallel paths that dominate real windings are treated with the transposition schemes that suppress them. Litz wire is assessed for construction, effectiveness and its practical limits in fill factor and termination; form-wound and hairpin conductors are assessed for the same duty. End-winding losses and leakage are quantified. The AC resistance factor is evaluated by analytical models and by finite-element analysis, and the domain of validity of each is stated. The chapter closes with design rules and with the winding design of the two running machines, checked against the loss budget set in Chapter 9.

Sections: 8.1 Skin and proximity effects in slot conductors · 8.2 Circulating currents and strand transposition · 8.3 Litz wire · 8.4 Form-wound and hairpin conductors at high frequency · 8.5 End-winding losses and leakage · 8.6 The AC resistance factor: analytical models against FE · 8.7 Windings of the two running machines.

Budget: 28 pages, 18 figures, 1 table. Contributors: I. Petrov, A. Belahcen supporting on FE evaluation.

#### Chapter 9. Losses, cooling and the thermal budget at kilohertz frequencies

Loss models fitted below 400 Hz do not extrapolate to 2 kHz, and the air in the gap stops being a passive medium above roughly 100 m/s; this chapter treats every loss mechanism that changes at high speed and the cooling that must remove them. Loss separation is shown to break above 1 kHz, and measurement and model fitting are done for high-frequency operation. The soft magnetic materials are compared as design choices, thin-gauge silicon iron, cobalt iron, amorphous and composites, with the manufacturing effects that degrade them quantified. The rotor side has equal weight: surface and harmonic losses, eddy currents in sleeves, rings and magnets, magnet segmentation, and solid-rotor loss modelling. Aerodynamic and windage losses are developed from laminar Couette flow through Taylor vortices to turbulence, with validated friction correlations, roughness and end effects, and low-density-gas operation. The chapter then turns the thermal problem the right way round for high-speed design: cooling architectures, jackets, in-slot and direct winding cooling, rotor and hollow-shaft cooling, are chosen and lumped-parameter thermal networks built with the air gap as a heat source. Magnet temperature and demagnetisation margin are shown to be the binding thermal constraint in most permanent-magnet high-speed machines. The chapter closes with the loss balance of the two running machines against their thermal budget.

Sections: 9.1 Loss separation above 1 kHz · 9.2 Soft magnetic materials · 9.3 Manufacturing effects · 9.4 Measurement and model fitting · 9.5 Rotor surface and harmonic losses · 9.6 Eddy currents in sleeves, rings and magnets; magnet segmentation · 9.7 Solid-rotor loss modelling · 9.8 Aerodynamic and windage losses: Taylor–Couette flow, correlations, roughness, low-density gas · 9.9 Cooling architectures and thermal networks · 9.10 Magnet temperature and the loss budget of the two running machines.

Budget: 44 pages, 28 figures, 3 tables. Contributors: A. Belahcen (loss modelling, materials, manufacturing effects), I. Petrov (rotor losses), J. Saari (windage), J. Nerg (thermal networks). DREM boundary: the earlier book's loss and thermal chapters cover the conventional frequency range; only the high-speed departures are treated.

### Part IV — Delivery: the drive and the applications

#### Chapter 10. The drive: converter interface and control at high fundamental frequency

The converter is not a fourth constraint but the gatekeeper that decides which region of the design space can be reached. The chapter develops the modulation ratio and the synchronous-PWM and control-stability thresholds, then shows why current harmonics matter more at high speed: they are deposited in a rotor that the air gap thermally isolates. Silicon, silicon carbide and gallium nitride devices are compared on switching-loss economics, and the consequences of fast switching for the machine are treated in full, DC-link voltage and du/dt, output filter options, insulation under fast switching including partial-discharge inception and Type II systems, and bearing currents and their mitigation. Converter integration and EMC follow. The control half of the chapter addresses what changes at low pulse ratios: current regulation, overmodulation and six-step operation, position sensing and sensorless operation, run-up through critical speeds, field weakening and protection. The chapter closes with the co-design procedure, matching pole count to converter capability, applied to both running machines.

Sections: 10.1 Modulation ratio and synchronous PWM · 10.2 Current harmonics and rotor heating · 10.3 Silicon, SiC and GaN: switching-loss economics · 10.4 DC-link voltage, du/dt and filters · 10.5 Insulation under fast switching · 10.6 Bearing currents · 10.7 Converter integration and EMC · 10.8 Control at low pulse ratios · 10.9 Position sensing and sensorless operation · 10.10 Run-up through critical speeds, field weakening, protection · 10.11 Co-design of the two running machines with their converters.

Budget: 42 pages, 28 figures, 2 tables. Contributors: P. Peltoniemi (converter and control), L. Aarniovuori (harmonic losses), with M. Hinkkanen or O. Pyrhönen on control at low pulse ratios. DREM boundary: not covered in the earlier book.

#### Chapter 11. Industrial case studies: compressor drive and ORC generator

Two complete industrial designs are carried from specification to measured performance. The first is the gearless compressor drive that has served as the industrial running machine throughout the book, now assembled: its rotor, bearings, cooling, electromagnetic design and converter are brought together, built and tested. The second is an organic Rankine cycle turbogenerator, chosen because it exercises the generator side and the high-temperature environment. Manufacture and tolerance control are treated as part of the design, since at high speed they are. The test rig, instrumentation and loss segregation at high speed are described in enough detail to be reproduced, with calorimetric methods where electrical methods fail. Qualification is addressed against the standards that industrial customers require, API 617 and API 541, IEC 60034-25 for converter-fed machines, ISO 21940 balancing grades and ISO 20816 vibration. The chapter closes with the failure modes observed in industrial high-speed machines and the design lessons drawn from them.

Sections: 11.1 The gearless compressor drive: from specification to measured performance · 11.2 The ORC turbogenerator · 11.3 Manufacture and tolerance control · 11.4 Test rig, instrumentation and loss segregation at high speed · 11.5 Qualification against standards · 11.6 Failure modes and design lessons.

Budget: 28 pages, 22 figures, 3 tables. Contributors: authors, J. Saari (compressor case), L. Aarniovuori (loss measurement). New: measured case data.

#### Chapter 12. Mobile case studies: traction, aerospace and e-turbo

Three mobile designs close the book. The Voltcar traction machine, the mobile running machine, is assembled and tested, with its performance under drive-cycle and thermal-transient loading reported against the design predictions of the preceding chapters. A high-specific-power aerospace generator illustrates the extreme of the mass-limited paradigm and the qualification culture of that industry. An electrically assisted turbocharger above 100 000 r/min illustrates the extreme of speed, where the machine must be nearly invisible in mass and inertia. Testing under transient conditions and overspeed, thermal and endurance qualification are described, and the failure modes of mobile high-speed machines are contrasted with the industrial ones of Chapter 11. A closing section revisits the two paradigms with the completed designs in hand and states, with numbers, why the same physics produces opposite machines.

Sections: 12.1 The Voltcar traction machine: from specification to measured performance · 12.2 A high-specific-power aerospace generator · 12.3 An e-turbocharger above 100 000 r/min · 12.4 Testing under drive-cycle and thermal transients · 12.5 Overspeed, thermal and endurance qualification · 12.6 Failure modes and design lessons · 12.7 The two paradigms revisited.

Budget: 30 pages, 24 figures, 3 tables. Contributors: authors (Voltcar), an aerospace contributor to be invited for 12.2. New: measured case data from a current EU project.

### Front and back matter

Preface (the two books and how to use them together); list of symbols; Appendix A material property tables for electrical steels, magnets and sleeve materials; Appendix B symbols and units; Appendix C key design formulae; Appendix D index of companion notebooks; index. Budget 40 pages.

## 5. Contributors

The author line is Canseven, Petrov and Pyrhönen. Contributors are credited at chapter level and each chapter has one of the three authors as owner and editor.

| Contributor | Affiliation | Chapters | Status |
|---|---|---|---|
| Jussi Sopanen and group | LUT, machine dynamics | 4, 5, 6 | agreed in principle |
| Anouar Belahcen | Aalto University | 9 lead; 8.6 and 5.7 supporting | expected |
| Juha Saari | industry | 2, 9, 11 | to be invited |
| Pasi Peltoniemi | LUT, power electronics | 10 | to be invited |
| Lassi Aarniovuori | drive loss measurement | 10, 11 | to be invited |
| Janne Nerg | LUT, thermal modelling | 9 | suggested |
| bearing application specialist | industry, to be identified | 6 | open |
| Marko Hinkkanen or Olli Pyrhönen | Aalto / LUT, control | 10 | suggested, one of the two |
| aerospace contributor | to be identified | 12.2 | open |

## 6. Schedule

Indicative, from contract signature: Chapters 2 and 3 with the running-machine specifications at month 6; Part II at month 11; Part III at month 15; Part IV at month 20; complete manuscript with problems and notebooks at month 22; delivery at month 24.

## 7. Material offered with the proposal

Chapter 1 complete; the annotated table of contents above; a partial Chapter 7 demonstrating the inverted sizing procedure on one running machine, to evidence the design-book claim; author and contributor biographies; the competing-titles analysis.
