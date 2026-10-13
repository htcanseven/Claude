# Industry test protocols, standardisation, reviews, venues and the novelty gap for e-fluid/ATF compatibility with e-motor insulation (hairpin windings, direct oil cooling)

Scope: this file covers industry protocols, standards, review literature, research groups and venues, and the novelty gap. The individual electrical oil-ageing studies are catalogued in the sibling file `electrical_oil_ageing.md` (C1–C15). That catalogue covers RWTH Aachen/Hameyer, Bologna/Cavallini HEFT, Tre Tau PFA vs PAI, Afton SAE paper and patents, Castrol/CEEIA 415-2019, Suzhou Jufeng and Essex patents, Honda SAE 2016-01-1221, Victrex and Proterial. This file mentions them only where they bear on protocols, standards or the gap. When a claim rests on a URL the sibling researcher opened and I did not, it is marked "(sibling C#)".

Source-type labels: [PEER-REVIEWED], [CONFERENCE], [THESIS], [STANDARD], [STANDARD-IN-DEVELOPMENT], [PATENT], [VENDOR] (company paper, white paper, press release, webinar or datasheet, including test labs), [TRADE] (trade or society magazine, not peer-reviewed), [PRESENTATION] (conference programme abstract or slide deck).

Access limits: IEEE Xplore pages came back empty or with HTTP 418. The SAE J3200 page did not render. ASTM work-item WK87553 and MDPI Energies returned HTTP 403. Semantic Scholar and OpenAlex APIs returned HTTP 429. Google Scholar was not reachable. Several IEEE and journal items are therefore listed under Gaps as "identified but not opened".

## 1. How do fluid suppliers, OEMs, wire makers and resin makers test e-fluid/material compatibility for e-motors? (conditions and outputs)

### Takeaway
Industry has converged on energised copper-corrosion tests: Lubrizol's Wire Corrosion Test and the Conductive Deposit Test, now ASTM D8544. These typically run at 130–150 °C for 72–500 h in both the liquid and the vapour phase. Insulation testing is far less mature. Each supplier uses its own magnet-wire protocol, usually enamelled round or rectangular wire or twisted pairs soaked at about 150 °C, often with added water, and measured for breakdown voltage, PD, adhesion or coating voids. The only published PEEK data are vendor adhesion numbers. A Lubrizol author states there is "no standard method agreed upon" for magnet-wire insulation.

### Cited Findings

#### 1a. Protocol overview (details and sources in 1b–1e)
| Organisation (type) | Specimen | Fluid / phase | Temperature, duration | Water / vessel | Outputs |
|---|---|---|---|---|---|
| Lubrizol WCT (now ASTM WK87553 work item) | thin Cu wire of known length/resistance | liquid + vapour | 72 h; run at 130 °C and 150 °C | not stated | real-time resistance increase → corrosion rate |
| CDT = ASTM D8544-24 (originated at IFAS, RWTH Aachen) | circuit board with energised Cu traces | liquid + vapour zones | 80–180 °C; typical 150 °C up to 500 h | not stated | conductance vs time, dendrite/deposit index, end-of-test photos |
| Infineum ECT | oil-immersed energised Cu circuit board in a dedicated cell (live observation) | immersed | not disclosed | not disclosed | corrosion mechanism and parameter sensitivity |
| TotalEnergies company spec | copper-wire coating (adapted existing test); "Printed Circuit Test" | not stated | 120 h EDU durability test (system level) | not stated | optical inspection + continuous resistivity during ageing |
| Lubrizol ex-situ winding test (Brenda & Petek) | industry-standard polyimide-type insulated wires | fluids at "high temperature" | not disclosed | not disclosed | void fraction via electrolyte + potentiostat |
| Lubrizol practice (per Newcomb 2023) | magnet wire | (a) thermal shock with water-contaminated lubricant; (b) isothermal soak in pure lubricant | not given | water in (a) | not given |
| Afton (SAE 2023-32-0145; patents) | round + rectangular MW; polyester, polyamide, polyimide coatings; NEMA MW 1000 twisted pairs (patent) | ETFs | ~150 °C, ~5 days (patent, sibling C9) | ~1500 ppm water added (patent); water level is a variable (paper); glass containers | adhesion, BDV, PD |
| Castrol, per Chinese group standard CEEIA 415-2019 (sibling C10) | round enamel, flat wires, complete system | ATF vs e-fluid | 8 × (155 °C/40 h → −45 °C/8 h) | sealed, 0.5 % water | BDV, withstand |
| Epic Resins + Solvay/Syensqo | KetaSpire PEEK magnet-wire grade + ProPreg E240 epoxy | ATF, immersed + vapour | 150 °C, 500/1000/1500/2000 h | not stated | adhesion pull force (IEC 61033) |
| Tre Tau Engineering (wire maker; sibling C7) | PFA vs PAI rectangular wire | Shell Spirax S6 ATF D971 | 150 °C, 2000 h, per IEC 60851-4 | "oil tester" | BDV |
| Essex (patents; sibling C12) | insulated winding wire | oil per ASTM D1676; ATF | e.g. 150 °C ≈2000 h | sealed vessel | BDV, PDIV, cracking |

#### 1b. Copper-corrosion and conductive-deposit tests (fluid side)
- **Wire Corrosion Test (WCT).** Thin copper wires of known length, and so known resistance, are placed in the liquid and vapour phases of the lubricant and held at a set temperature for 72 h. Real-time resistance change gives the corrosion rate. Savant's Greg Miiller says it catches corrosion and failures that ASTM D130 misses. Wire gauge and voltage are not given [TRADE] — [STLE TLT, Jan 2024 feature](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
- The WCT was developed at Lubrizol and introduced in 2016 (Gahagan & Hunt 2016). It has since been applied to other metals [PEER-REVIEWED mini-review, Lubrizol author] — [Newcomb 2023, Front. Mech. Eng. 9:1139385](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- Reported WCT conditions are 72 h at 130 °C and 150 °C. In March 2024 it was in ASTM round-robin testing as a proposed standard [TRADE] — [F+L Magazine, 14 May 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/)
- **Conductive Deposit Test (CDT).** A test circuit board is immersed with voltage on its copper traces, heated for hundreds to thousands of hours and monitored in real time. It fails when resistance drops below a set value, which signals conductive deposits in the liquid or vapour phase. End-of-test photographs are assessed for deposits and dendrites. The risk being tested is copper-sulphide deposits bridging conductors and shorting circuits or motors [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx). The CDT originated at IFAS, RWTH Aachen — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- **Origin and validation.** The CDT and WCT were developed by "a group of industry experts involving both OEM's and lubricant experts from across the globe". Results "show correlation to field data", and the work looked at ester, base-stock and traction-reducer dilution. Conducting-layer deposits are "identified as a failure mechanism for current electric motor designs" (Miiller, VanBergen/Savant; Kurchan, Gillespie/Cargill; Mueller/APL; Newcomb, Hunt/Lubrizol) [PRESENTATION] — [STLE 2023 Tribology & Lubrication for E-Mobility Conference programme, Cleveland, 14–15 Nov 2023](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
- **Cyclic vs isothermal temperature.** Lubrizol (Hunt, Choo, Newcomb) ran sulphur-containing oils through cyclic thermal profiles in the WCT. Corrosion during cycling "was found to be more significant than expected", so brief high-temperature excursions may matter more than isothermal tests suggest. The transient effect "has not previously been investigated" [PRESENTATION] — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
- **Infineum ECT.** Infineum runs an oil-immersed energised copper-corrosion test whose cell allows live observation. It says "many OEMs see copper compatibility as the most important e-fluid design parameter" and that "multiple testing parameters can lead to test result variability". It discloses no conditions and does not cover insulation or dielectric properties [VENDOR] — [Infineum Insight, 1 Oct 2024](https://infineuminsight.com/en-gb/articles/leading-advances-in-driveline-testing). At STLE 2023, S. Campbell (Infineum) said "Energized corrosion testing is still evolving with much variation in competing test designs" [PRESENTATION] — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
- **TotalEnergies company specification.** It has five parts: physico-chemical, tribological, component, system and fleet testing. It uses internal methods and a 120 h EDU durability test. Copper-wire coating compatibility uses an adapted existing test. The "Printed Circuit Test" combines optical inspection with continuous resistivity monitoring during ageing [TRADE report of VENDOR talk] — [F+L Magazine 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/)
- **Optical rating.** "CuDDI" (Ayalytical Instruments, in development) replaces visual ASTM D130 strip rating with an LED-lit (~4500 K, 45° diffuse) CCD camera system trained on ASTM colour standards. It is not an ASTM method [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)

#### 1c. Magnet-wire and insulation protocols from fluid suppliers
- **Afton Chemical (Kwak, Grzyska, Cleveland; Tsuneo).** SAE 2023-32-0145 (JSAE/SAE PFL 2023; SAE Int. J. Adv. & Curr. Pract. Mobility 6(3):1468–1478) describes sample preparation, ageing, equipment and evaluation. Outputs are adhesion, breakdown voltage and PD for round and rectangular polyester, polyamide and polyimide magnet wire, with fluid water content as a variable. Its conclusion: "Lubricant's additive package or formulation chemistry leads to significant MW performance differences". Temperature and duration are not on the abstract page [CONFERENCE/journal; abstract only] — [SAE Mobilus](https://saemobilus.sae.org/articles/magnet-wire-compatibility-test-electric-drivetrain-fluid-development-2023-32-0145). The same work was presented at STLE 2023, which called MW compatibility "the primary performance requirement" — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf). The patent protocol is in sibling C9.
- **Lubrizol ex-situ winding-durability test (R. Brenda, T. Petek, Lubrizol Derby).** Industry-standard polyimide-type wires are aged in fluids at high temperature. They are then mounted in a cell where a conductive fluid fills any voids in the coating, and a potentiostat measures conduction through the voids to quantify void fraction. The authors say it "can differentiate between fluids that will harm the coating and those that will not" [PRESENTATION] — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
- **Lubrizol's view.** "There is currently no standard method agreed upon to test such parts". Two approaches are in use: thermal-shock tests with water-contaminated lubricant (Canter 2022) and isothermal soak in pure lubricant (Gahagan 2017). SAE J3200 reviews the current state of testing [PEER-REVIEWED] — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- **Fluid electrical properties during ageing.** SwRI (J. Conner) studied how oxidation changes relative permittivity, dissipation factor, conductivity and breakdown voltage of drivetrain lubricants, comparing electrified and non-electrified oxidation tests. Functional Products (J. Scherger) studied how polymer additives change conductivity, dissipation factor and BDV, noting that the target is "a moderate range", not a maximum or minimum. ExxonMobil (Lotfi, Lee) and Valvoline (Kolekar) name dielectric properties, "electrical compatibility and insulation" and material compatibility as design targets but give no methods [PRESENTATION] — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
- **OEM requirements.** "Several original equipment manufacturers (OEMs) now specify both new and aged lubricant electrical conductivity/resistivity". Used ATFs are more conductive than new ones, attributed to oxidation. 2000 ppm water raised conductivity, which returned to nominal after the water was removed thermally [PEER-REVIEWED] — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)

#### 1d. Wire, polymer and resin makers
- **Epic Resins & Solvay (now Syensqo), technical paper dated 06/2023.**
  - Materials: KetaSpire PEEK magnet-wire grade (and KT-880) and Ajedium PEEK slot liner, with ProPreg E240 one-component epoxy secondary insulation.
  - Vendor performance claims: PEEK wire PDIV "~1600-1700 V at 150 microns typical"; extruded PEEK with hairpins raised slot fill "by over 10%".
  - Protocol: ATF at 150 °C for up to 2000 h, with specimens both immersed and vapour-exposed. Adhesion was measured per IEC 61033 by Eltek International Laboratories.
  - Max pull force, N, immersed / vapour: 500 h 413/442; 1000 h 351/384; 1500 h 398/439; 2000 h 415/444.
  - Separation was always between the polymer coating and the copper, never at the epoxy–polymer bond. The system was "tested successfully with multiple ATF types".
  - Not reported: ATF names, electrical data, water content, sealing.
  - [VENDOR] — [Epic Resins/Solvay PDF](https://www.epicresins.com/Content/files/Resources/111721-TechPaper-Epic-Sol.pdf)
- **Victrex + Sedrive, IEEE IES ITeN webinar (27 Nov 2024; S. Nategh, Sedrive; J. Bonnett, Victrex).** Direct cooling with transmission fluid "place[s] heavy stress on insulation", so insulation must be oil-compatible. They propose an oil-cooled 800 V+ insulation system centred on a slot liner, verified on a "new test setup" representing an 800 V+ PWM-fed machine. No oils, ageing conditions or data are given [VENDOR/PRESENTATION] — [IEEE ITeN webinar page](https://iten.ieee-ies.org/upcoming-online-webinar/2024/an-insulation-system-solution-for-oil-cooled-800-v-pwm-supply-electrical-machines/). Victrex's claim of 180 °C/2000 h ATF retention is in sibling C14.
- **Essex Group, parylene patent US 10,366,805 B2** (priority 31 Mar 2016; inventors Knerr, Cain).
  - What it describes: parylene by vacuum vapour deposition on preformed hairpins (batch) or as a post-assembly overcoat that "may replace conventional varnish", applied over bare conductor, enamel or extruded insulation.
  - What it claims: coated wire "hydrolytically stable and resistant to oils … such as transmission fluid"; dielectric strength above ~7000 V/mil; PDIV above ~1000–2500 V.
  - No oil-ageing test data appeared in the first ~60 % of the text read.
  - [PATENT] — [Google Patents US10366805B2](https://patents.google.com/patent/US10366805B2/en)
- **Zeus PEEKshrink datasheet (PEEK heat-shrink tubing).**
  - Geometry: shrink ratio up to 1.4:1; expanded ID 0.038–2.000"; recovered wall 0.003–0.018".
  - Thermal: continuous service 260 °C; recovery shrink temperature 300–340 °C (translucent) or 360–385 °C (opaque).
  - Dielectric strength 3570 V/mil (ASTM D149).
  - Intended uses: wire and cable encapsulation, a "splicing aid for PEEK insulated wire", oil and gas applications.
  - No ATF, e-fluid or e-motor data.
  - [VENDOR] — [Zeus PEEKshrink datasheet](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf)
- **OEM evidence.** Honda (SAE 2016-01-1221) put a PEEK-based layer over enamel for durability in ATF, without published ageing data (sibling C13).

### Inferences
- Industry protocols split into two families. (i) Fluid-qualification tests on bare copper (WCT, CDT/D8544, ECT, D130) under voltage and in both liquid and vapour phases. (ii) Fluid-versus-insulation tests on enamelled wire. Only family (i) has been standardised. Neither uses formed hairpins, and none compares insulation materials; the fluid is always the variable.
- Typical published insulation-ageing conditions are about 150 °C for 5 days up to 2000 h (Afton, Epic/Solvay, Tre Tau, Essex), 160–180 °C in academic work (sibling C1, C5), and cyclic 155/−45 °C with 0.5 % water in China. Water spiking (1500 ppm to 0.5 %) and vapour-phase exposure recur, so a protocol with an immersed zone, a vapour zone, a controlled water level and a dry air control would be comparable with industry practice.
- Fluid electrical properties (conductivity, dissipation factor, BDV) before and after ageing are measured by SwRI, Functional Products and OEM specifications, so measuring the oil alongside the specimens would match industry practice at low cost.

### Gaps
- No full protocols were found for Lubrizol's void-fraction test, Infineum's ECT, TotalEnergies' copper-wire coating test, or any Shell, ExxonMobil, Castrol (beyond sibling C10), Valvoline, FUCHS, Idemitsu, ENEOS, Petronas or Chevron Oronite insulation test. Their e-fluid pages surfaced only as marketing in searches and were not opened.
- No ATF-resistance test methods or data were found from ELANTAS, Axalta, Essex Furukawa, Elektrisola or Superior Essex. Search results showed only product pages, e.g. ELANTAS hairpin "resin–gelcoat" and epoxy powder-coating options, and Axalta Voltatex 4200/4224; these were not opened.
- OEM in-house protocols (GM, Ford, VW, BMW, Toyota and others) are not public. The STLE 2023 keynote by T. Muransky of American Axle is listed by title only.
- A secondary source (F&L Asia, not opened) reportedly lists SwRI AFEV project options including a "motor hairpin coating breakdown project" and a materials-compatibility soak study; this is unverified. The SwRI press release I opened lists only durability, oxidation, aeration, heat transfer, electrical conductivity and fluid ageing.
- MDPI Batteries 10(8):285 (2024), "Copper Wire Resistance Corrosion Test for Assessing Copper Compatibility of E-Thermal Fluids for BEVs", was identified but not opened.

## 2. Standardisation activity (ASTM, SAE, ISO, IEC, DIN, CEC, national)

### Takeaway
ASTM D8544-24, the conductive-deposit test, is the only published method written for EV-driveline fluids, and it concerns bare-copper corrosion and deposits. The wire-corrosion test is an ASTM work item (WK87553). SAE J3200 (2022) is an Information Report that recommends bench tests, including material compatibility, but is not a pass/fail specification. Insulation-side standards (ASTM D1676-24, IEC 60851-4:2016) contain oil and insulating-liquid resistance tests designed around transformer oil or insulating liquids, not ATF or e-fluids. I found no ISO, IEC, DIN, CEC or JASO method for e-fluid compatibility with motor insulation.

### Cited Findings

#### 2a. Fluid-side methods (published)
- **ASTM D8544-24**, "Standard Test Method for Determination of Conductive Deposits of Electrical and Mechanical Components from Fluids in Liquid and Vapor States within an Electrically Charged System".
  - Jurisdiction: D02.09.0G.
  - Test: 80–180 °C on specific circuit boards under power, with conductance tracked in liquid and vapour zones; typical 150 °C, up to 500 h with monitored voltage (1000 h optional, not covered).
  - Use: may assess fluids for "electric vehicle drivelines"; recommended in SAE J3200.
  - Precision statement still interim; an interlaboratory study was due by Dec 2024.
  - [STANDARD] — [ASTM D8544-24](https://store.astm.org/d8544-24.html). Approved and launched 14 March 2024 [TRADE] — [F+L Magazine 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/)
- **ASTM D130 (copper strip)** is still the specification test but is criticised for EV use: visual and operator-dependent, with temperatures and times not representative [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx). It is "qualitative and subject to variation", and motor burnout has occurred with fluids that passed it — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- **Electrical methods** listed for EV lubricants: ASTM D149 (dielectric strength), D257 (DC resistance), D1816 (breakdown voltage), D2624 and D4308 (conductivity). Loss tangent and relative permittivity are marked "to be developed" [PEER-REVIEWED review] — [Tung, Woydt & Shah 2020](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2020.571786/full)

#### 2b. Fluid-side methods (in development, or reports)
- **ASTM WK87553**, "New Test Method for the Determination of Wire Corrosion and Oxidation from Fluids in Liquid and Vapor States Within an Electrically Charged or Mechanical System", is the WCT [STANDARD-IN-DEVELOPMENT]. Its title was seen only in a search listing for https://www.astm.org/workitem-wk87553, which returned HTTP 403 when opened, so its status is unverified. Round-robin in 2024 — [F+L Magazine 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/); "in the process of completing an ASTM test method" — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
- **SAE J3200, "Fluid for Automotive Electrified Drivetrains"** (J3200_202210, Oct 2022), from SAE Fuels & Lubricants TC 3 Driveline and Chassis Lubrication.
  - Content headings: electrical properties; heat-transfer properties; copper corrosion and conductive deposits; oxidation; material compatibility; high-speed aeration; new wear concerns [PRESENTATION] — [R. A. Morrison (AMT Consulting) to California BAR Advisory Panel, 25 Jan 2024](https://www.bar.ca.gov/pdf/bag/202401/ev.pdf)
  - Status: an SAE "information report" for geared systems where the motor is immersed in or contacts the lubricant, "still being refined" [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
  - It recommends the WCT and CDT and discusses material-compatibility testing — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
  - It is already used as a formulation target, e.g. by Indian Oil, and by Functional Products for electrical properties — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
  - The SAE page did not render, so the full text was not accessed.
- **ASTM D02 Coordinating Subcommittee CS 97, "Fluids for Electrified Vehicles and Drive Systems"** (proposed scope, Jan 2024) liaises with D02, D15 (coolants), D27 (Electrical Insulating Liquids and Gases), SAE TC 3, STLE, NCWM, CRC, NLGI, the International Fluids Consortium, DIN and SwRI AFEV. **ASTM D15.26** is developing EV-coolant methods for corrosion, elastomer compatibility and electrical conductivity [PRESENTATION] — [BAR presentation](https://www.bar.ca.gov/pdf/bag/202401/ev.pdf)
- **National and other activity**, reported at F+L Week 2024 [TRADE] — [F+L Magazine 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/):
  - France: GFC is studying dielectric properties, high-speed wear, copper corrosion and water.
  - Germany: FVA project 827 I (Fraunhofer IEM, Leibniz Univ. Hannover IAL) is a preliminary study of high-voltage e-drive oil.
  - China: NB/SH/T 6042-2021 covers EV reducer lubricants (issued 16 Nov 2021, in force 16 May 2022); a RIPP-led group is drafting a GB/T EV-fluid specification.
  - Japan and Korea: mainly OEM-level work.
  - The article mentions no ISO, IEC, DIN, CEC or JASO activity.

#### 2c. Insulation and winding-wire side
- **ASTM D1676-24**, "Standard Test Methods for Film-Insulated Magnet Wire" (Committee D09, Subcommittee D09.12; DOI 10.1520/D1676-24), includes "Chemical Resistance" (§22–28), "Dielectric Breakdown AC Voltage after Conditioning in Refrigerant Atmosphere" (§90–99) and "Resistance to Insulating Liquids and Hydrolytic Stability" (§186–195). Conditions were not visible on the page [STANDARD] — [ASTM D1676-24](https://store.astm.org/d1676-24.html). Essex patents describe the D1676 oil test as about 150 °C for about 2000 h followed by BDV, PDIV and crack inspection (sibling C12).
- **IEC 60851-4:2016**, "Winding wires – Test methods – Part 4: Chemical properties" (Ed. 3.0, 2016-07-06, TC 55): Test 12 solvents, Test 16 refrigerants, Test 17 solderability, Test 20 "Resistance to transformer oil" [STANDARD] — [IEC webstore](https://webstore.iec.ch/en/publication/25335). Tre Tau used this standard with an ATF (Shell Spirax S6 ATF D971, 150 °C, 2000 h) and called it "Resistance to hydrolysis and transformer oil" (sibling C7). That wording differs from the IEC webstore title.
- **IEC 61033** (bond strength of impregnating agents to enamelled wire) was used to measure epoxy–PEEK adhesion after ATF exposure — [Epic/Solvay](https://www.epicresins.com/Content/files/Resources/111721-TechPaper-Epic-Sol.pdf). NEMA MW 1000 twisted pairs were used by Afton (sibling C9).
- **CEEIA 415-2019** (China Electrical Equipment Industry Association group standard) is the only standard found that targets oil-cooled motor insulation and transmission-fluid compatibility directly. It specifies a sealed vessel, 0.5 % water and 8 thermal-shock cycles (sibling C10, via Castrol/Gasgoo).

### Inferences
- No standard yet addresses e-fluid compatibility of motor insulation, and none at all addresses formed hairpins, extruded or tube insulations, or secondary insulation (powder, parylene, tape). A study run under a transparent, standard-derived protocol could contribute method as well as data. Suitable bases are D1676 §186–195 or IEC 60851-4 Test 20-style sealed ageing, with SAE J3200-listed fluid electrical properties and D8544/WCT-style copper witnesses.
- Standards bodies point to ASTM D27 (insulating liquids) as a liaison, so transformer-world methods for fluid dielectric properties are the natural ones to cite for the oil measurements. The D149/D1816/D2624/D4308 family is already used for EV lubricants.

### Gaps
- WK87553's current status (approved or still a work item) could not be verified; the page returned 403.
- I found no ISO, IEC, DIN, CEC or JASO method or new work item on e-fluid–insulation compatibility. Searches for DIN and ISO returned only general lubricant classifications (ISO 6743, DIN 51524).
- I did not open IEC 60034-18-41/-42 (converter-fed machine insulation qualification), IEC 60172 or IEC 61857. Whether they include any fluid-exposure provision is unverified.
- The SAE J3200 full text was not accessed, so its exact recommended material-compatibility procedure (temperature, duration, specimens) is unknown. STLE TLT Aug 2021 (cited in sibling §3) says it recommends "testing the fluid after it has been aged with materials".

## 3. Review articles (2018–2026) and what they say is unknown

### Takeaway
The open-access reviews come from the lubricant side (Frontiers in Mechanical Engineering 2020, 2023, 2026) and the trade press. They agree that polymer and magnet-wire compatibility tests are inconsistent and unstandardised, that copper-corrosion risk is under-assessed, and that electrical properties of aged fluids are under-characterised. None reviews insulation-material performance after oil ageing. No dedicated review of e-fluid and winding-insulation compatibility was found.

### Cited Findings
- **Newcomb (Lubrizol), "A brief review of the rapid transformation of driveline lubricants for hybrid electric and electric vehicles", Front. Mech. Eng. 9 (2023) 1139385**, Mini Review.
  - Polymer compatibility: "Compatibility tests of these polymers vary within the industry", and there is no agreed standard for magnet-wire insulation.
  - Copper: corrosion risk "is not always properly assessed by current specification tests".
  - Electrical properties: OEMs specify new and aged conductivity; data on degraded-fluid conductivity are still being developed.
  - Not covered: varnish, slot liners, PEEK, enamel attack mechanisms, dielectric strength.
  - The author says the review "is not comprehensive".
  - [PEER-REVIEWED] — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- **Tung, Woydt & Shah, "Global Insights on Future Trends of Hybrid/EV Driveline Lubrication and Thermal Management", Front. Mech. Eng. 6 (2020) 571786**, Review.
  - Fluids must suit "polymeric insulations, sensors, and circuits". Copper-wire insulation is listed as a motor concern but not discussed in depth.
  - "strayed voltages or energized circuits can promote corrosion that would normally not occur".
  - Dielectric immersion fluids should keep water below 50 ppm.
  - EV-lubricant electrical properties "have yet to be reviewed and assessed", more corrosion-deposition tests are needed, and loss tangent and permittivity methods are "to be developed".
  - About 63 % of the article was read.
  - [PEER-REVIEWED] — [Tung et al. 2020](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2020.571786/full)
- **Gao, Tan & Li, "A review of structural design for direct oil cooling and integrated thermal management in electric motors for new energy vehicles", Front. Mech. Eng. 12 (2026) 1951365**, Mini Review, published 18 Sep 2026.
  - It lists "compatibility with insulation materials" as a key coolant property but gives no material data.
  - It cites aged-fluid resistivity loss (~34 MΩ·m at 90 °C, Davin et al. 2015) and warns that oil "hygroscopicity" can cause "potential corrosion failures".
  - It names "oil degradation, and sealing reliability" as barriers and concludes "Standardized test protocols and design methodologies will be essential".
  - No IEC, ASTM or ISO methods are cited.
  - [PEER-REVIEWED] — [Gao et al. 2026](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1951365/full)
- **Goetz, Lizana F. & Rivera, "Hairpin Motors for Electromobility: Twists and Bends …"** (arXiv 2312.15830, Dec 2023), a hairpin technology review. The abstract notes material and process difficulties and says much recent industry-driven work "is not public", which the authors think may hinder innovation. Abstract only [preprint] — [arXiv](https://arxiv.org/abs/2312.15830)
- **Trade review of copper-corrosion testing (Aikin, STLE TLT Jan 2024).** It covers D130, extended and vapour-phase D130, WCT, CDT and CuDDI. It does not address insulation, magnet wire or varnish test methods [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
- **Review-type conference paper on the electrical-machine side:** Martinez (Mondragon), Iannarelli, Seri, Cavallini (Bologna), "Insulation Technologies for State-of-the-Art Electrical Machines Used in Transport Electrification", IEEE WEMDCD 2025. It covers ATF spray lowering PDIV, PAI delamination after two weeks at 160 °C in ATF, and low insulation resistance in oil (sibling C6, [PDF opened by sibling](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf)).

### Inferences
- The review literature is split. Lubricant reviews treat insulation as a black-box "compatibility" requirement with no materials data. Electrical-machine and cooling reviews treat oil as a coolant or a PD-modifying medium and do not compare insulation materials. A paper bridging the two (many insulation materials × one oil protocol × electrical + optical evidence) would fill a gap that both sides identify.

### Gaps
- Identified but not opened, so their content is unverified:
  - "Review and Trends in Traction Motor Design: Primary and Secondary Insulation Systems" (IEEE, doc. 8506858, c. 2018).
  - "The Oil Spray Cooling System of Automotive Traction Motors: The State of the Art" (IEEE TTE, doc. 9819945).
  - Ji, Giangrande & Zhao, "Effect of Environmental and Operating Conditions on Partial Discharge Activity in Electrical Machine Insulation: A Comprehensive Review", Energies 17(16):3980 (2024); returned 403.
  - "A review on analysis and modeling of electrical machine insulation system" (Cogent Engineering, 2024).
  - "Survey of Insulation Systems in Electrical Machines" (Marquette).
  - "A Study on Insulation Components of High Voltage Electrical Machines Used in Electric Vehicles" (IEEE doc. 9968892).
- Older reviews often cited for EV tribology, such as Farfan-Cabrera, Tribology International 2019, were not opened.
- I found no review dedicated to e-fluid and winding-insulation compatibility. Because Scholar, Scopus and IEEE Xplore could not be searched directly, an IEEE-only review may have been missed.

## 4. Active research groups and publication venues

### Takeaway
The work sits in two communities that seldom publish together. Lubricant and additive companies publish at STLE, in SAE papers, in Frontiers in Mechanical Engineering and in trade magazines. Electrical-machine and insulation groups publish at ICEM, IEMDC and WEMDCD, in IEEE magazines and in EU-project deliverables. RWTH Aachen (IEM) and Bologna (Cavallini) are the main academic groups on oil and insulation. LUT University has published on conductive particles in oil-cooled machines.

### Cited Findings

#### 4a. Groups
- **RWTH Aachen, Institute of Electrical Machines (K. Hameyer; L. Yang).** PhD thesis "E-fluid oil as coolant in low-voltage rotating electrical machines – impact on the insulation system" (Shaker 2024, ISBN 978-3-8440-9418-3; advisors Hameyer and C. Jędryczka). It finds that oil penetrates the enamel and degrades mechanical properties, that PDIV and capacitance "cannot assess" this, and that particles and humidity lower PDIV [THESIS; abstract] — [RWTH IEM record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1). Related papers appeared at ICEM 2022 (funded by TotalEnergies), IEEE IEMDC 2023 and Archives of Electrical Engineering 2022 (sibling C1–C3).
- **RWTH Aachen IFAS** (fluid power) originated the CDT — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- **University of Bologna (A. Cavallini, G. Seri) with Mondragon**: HEFT Horizon Europe project with GKN; Castrol ATF ageing of PAI and slot-moulding resins (sibling C5–C6).
- **Tre Tau Engineering (Turin)**: PFA vs PAI after ATF ageing, IEEE Electrical Insulation Magazine 2024 (sibling C7).
- **LUT University (Montonen, Nerg, Polikarpova, Pyrhönen)**: IEEE Access 2019 study of conductive particles in oil-cooled machines, cited by RWTH (sibling §3). This is a home-institution precedent for the planned study.
- **Lubricant and additive industry**, from the STLE 2023 programme [PRESENTATION] — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf):
  - Lubrizol (Newcomb, Hunt, Choo, Gahagan, Brenda, Petek; Wickliffe OH and Derby/Belper UK)
  - Afton (Kwak; Richmond VA)
  - Infineum (Campbell, Thaker, Zhao, Cogen; Linden NJ)
  - ExxonMobil (Lotfi, Lee)
  - Valvoline (Kolekar)
  - Chevron (H. Hahn, session chair)
  - Functional Products (Scherger)
  - Clariant (Glänzer)
  - Cargill (Kurchan, Moody, Gillespie)
  - Savant (Miiller, VanBergen)
  - APL Landau (Mueller)
  - Emery Oleochemicals (M. Hof, chair of the material-compatibility panel)
  - Indian Oil (S. Seth)
  - SwRI (J. Conner)
  - Tecnológico de Monterrey (L. Farfan-Cabrera, testing session chair)
- **SwRI AFEV consortium**, launched April 2021 (durability, oxidation, aeration, heat transfer, electrical conductivity, fluid ageing) [VENDOR] — [SwRI press release](https://www.swri.org/press-release/swri-launches-consortium-advanced-fluids-electrified-vehicles)
- **Polymer and insulation suppliers**: Victrex with Sedrive (oil-compatible 800 V+ insulation system) — [IEEE ITeN webinar](https://iten.ieee-ies.org/upcoming-online-webinar/2024/an-insulation-system-solution-for-oil-cooled-800-v-pwm-supply-electrical-machines/); Syensqo/Solvay with Epic Resins — [Epic/Solvay](https://www.epicresins.com/Content/files/Resources/111721-TechPaper-Epic-Sol.pdf); Essex — [US10366805B2](https://patents.google.com/patent/US10366805B2/en)
- **Pre-normative bodies**: GFC (France), FVA 827 I (Fraunhofer IEM / Leibniz Univ. Hannover IAL), RIPP (China) — [F+L Magazine 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/)

#### 4b. Venues, with examples
- **STLE Tribology & Lubrication for E-Mobility Conference.** The 2023 edition (Cleveland, 14–15 Nov) had a "Material Compatibility" panel with CDT/WCT, Lubrizol winding-durability and Afton magnet-wire talks — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf). STLE also publishes the TLT magazine — [TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
- **SAE / JSAE.** SAE technical papers, the JSAE/SAE Powertrains, Energy & Lubricants meeting, and SAE Int. J. Adv. & Curr. Pract. Mobility (Afton 2023-32-0145) — [SAE Mobilus](https://saemobilus.sae.org/articles/magnet-wire-compatibility-test-electric-drivetrain-fluid-development-2023-32-0145); Honda SAE 2016-01-1221 (sibling C13)
- **Frontiers in Mechanical Engineering**, open-access reviews from 2020, 2023 and 2026 — [2020](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2020.571786/full), [2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full), [2026](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1951365/full)
- **Electrical-machine and insulation venues**: ICEM 2022, IEEE IEMDC 2023, IEEE WEMDCD 2025, IEEE Electrical Insulation Magazine 2024, Archives of Electrical Engineering 2022, IEEE Access 2019 (sibling C1–C7, §3); IEEE IES ITeN webinars — [ITeN 2024](https://iten.ieee-ies.org/upcoming-online-webinar/2024/an-insulation-system-solution-for-oil-cooled-800-v-pwm-supply-electrical-machines/)
- **Trade, industry and other channels**:
  - F+L Week / F+L Magazine — [F+L 2024](https://www.fuelsandlubes.com/fli-article/global-drive-for-standardisation-in-ev-fluids-and-technologies/)
  - Company magazines — [Infineum Insight](https://infineuminsight.com/en-gb/articles/leading-advances-in-driveline-testing)
  - Thesis series — [RWTH/Shaker](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1)
  - Horizon Europe deliverables (HEFT, sibling C5)

### Inferences
- For the planned paper, the best-fit journals and conferences are those where the electrical-insulation community already reads oil-ageing work: IEEE TDEI or IEEE Electrical Insulation Magazine, IEEE TTE, IEEE Access, Energies, ICEM, IEMDC, CEIDP and EIC. A companion paper at STLE or SAE would reach the fluid formulators who run the WCT, CDT and magnet-wire tests. CEIDP, EIC and IEEE TTE are inferred, not evidenced by opened examples here.

### Gaps
- Not verified with opened examples: CEIDP, IEEE EIC, INSUCON, CWIEME Berlin talks, and the journals Lubricants, Tribology International and IEEE TDEI. Their relevance is plausible but unconfirmed in this research.
- Asian academic groups (China, Japan, Korea) working on oil-cooled-motor insulation were not mapped. Chinese activity is visible through CEEIA 415-2019, NB/SH/T 6042-2021 and a Suzhou Jufeng patent (sibling C10–C11).

## 5. Novelty gap: does any study compare application methods of the same material, or many insulation types under one oil-ageing protocol with electrical measurements and imaging?

### Takeaway
No study was found that compares application methods of the same polymer (extruded PEEK vs PEEK tube vs PEEK heat-shrink) under oil ageing. None was found that ages a broad set of hairpin insulation systems (enamel PAI/PI, extruded PEEK, PEEK tube or heat-shrink, polyimide tape, epoxy powder, parylene) under one e-fluid/ATF protocol with paired electrical and high-resolution imaging before and after. The closest published comparisons cover two or three enamel or fluoropolymer types on straight wires or twisted pairs. PEEK, parylene, heat-shrink and powder data in oil exist only as vendor claims or patents.

### Cited Findings

#### 5a. Closest multi-material comparisons under one oil protocol (all from the sibling catalogue)
| Study | Materials compared | Oil / conditions | Electrical | Imaging / other | Distance from the planned study |
|---|---|---|---|---|---|
| RWTH ICEM 2022 (sibling C1) | PEI/PAI enamelled round wire + aramid paper | ATF, two e-fluids; 180 °C, 1008 h | PDIV, capacitance | peel, XPS | 2 materials, round wire, no hairpin, no PEEK |
| Tre Tau, IEEE EI Mag 2024 (sibling C7) | PFA vs PAI rectangular wire | Shell ATF; 150 °C, 2000 h (IEC 60851-4) | BDV | — | 2 materials; no application-method variable |
| Afton SAE 2023-32-0145 (sibling C8; [SAE](https://saemobilus.sae.org/articles/magnet-wire-compatibility-test-electric-drivetrain-fluid-development-2023-32-0145)) | polyester, polyamide, polyimide coatings; round + rectangular | several ETFs ± water | BDV, PD | adhesion | enamels only; fluid is the variable |
| Castrol / CEEIA 415-2019 (sibling C10) | round enamel, several flat wires, one complete system | ATF vs e-fluid; cycles 155/−45 °C; 0.5 % water | BDV / withstand | porosity noted | enamels; trade article |
| Bologna HEFT D2.4 (sibling C5) | PAI rectangular + 2 slot-moulding resins | Castrol ATF; 160 °C, 2 weeks, sealed | DS, PDIV at 20/180/210 °C | delamination observed | one wire type |
| Epic/Solvay 2023 ([PDF](https://www.epicresins.com/Content/files/Resources/111721-TechPaper-Epic-Sol.pdf)) | extruded PEEK wire grade + epoxy (and PEEK slot liner, dry) | ATF; 150 °C, 2000 h; immersed + vapour | none | adhesion only | vendor; one PEEK form |

#### 5b. Application-method search results (same polymer, different form)
- **PEEK heat-shrink** exists commercially: Zeus PEEKshrink, recovery 300–385 °C, marketed as a splicing aid for PEEK-insulated wire. The datasheet has no oil or e-motor data [VENDOR] — [Zeus datasheet](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf). Searches combining PEEK heat-shrink or tubing with hairpin, stator, oil or ATF returned only vendor pages and patents, with no comparative ageing study.
- **Parylene on hairpins** is described in an Essex patent that claims transmission-fluid resistance. It is applied by batch vapour deposition on preformed hairpins or as a varnish-replacing overcoat. No oil-ageing data were found [PATENT] — [US10366805B2](https://patents.google.com/patent/US10366805B2/en). Searches for parylene or powder coating with hairpin and transmission-fluid immersion returned no study.
- **Extruded PEEK** in ATF: only vendor or OEM claims and adhesion data — [Epic/Solvay](https://www.epicresins.com/Content/files/Resources/111721-TechPaper-Epic-Sol.pdf); Victrex and Honda (sibling C13–C14).

#### 5c. Imaging and diagnostics in existing protocols
- Industry uses imaging only on copper corrosion specimens: CDT end-of-test photos of circuit boards and CuDDI camera rating of D130 strips — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx). Lubrizol's insulation integrity test measures voids electrochemically rather than optically — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)
- RWTH found that PDIV and capacitance "cannot assess" oil-penetration damage. Measurements need to go beyond PDIV, for example mechanical tests, dielectric spectroscopy or imaging — [RWTH thesis record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1)

#### 5d. Statements of the gap by others
- "There is currently no standard method agreed upon to test such parts" (magnet-wire insulation) — [Newcomb 2023](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2023.1139385/full)
- "Standardized test protocols and design methodologies will be essential" — [Gao et al. 2026](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1951365/full)
- Much industry hairpin know-how "is not public" — [Goetz et al. 2023](https://arxiv.org/abs/2312.15830)
- Thermal-transient (cyclic) effects on corrosivity had "not previously been investigated" before Lubrizol's 2023 work — [STLE 2023 programme](https://www.stle.org/images/PDF/STLE_ORG/TFC_EV/2023_STLE_EMobility_Program_Guide_10.18.23.pdf)

### Inferences
- On current evidence, the planned study would add the following, with the caveat in Gaps below:
  1. The first open comparison of insulation application methods for the same polymer (extruded vs tube vs heat-shrink PEEK) after oil ageing.
  2. The broadest single-protocol comparison of hairpin insulation families, including secondary or conformal coatings (epoxy powder, parylene) and tapes (polyimide/Kapton), which no published oil study includes.
  3. Formed hairpin specimens with bends, stripped ends and interfaces where coatings terminate, instead of the straight wires, twisted pairs or circuit boards used in industry tests.
  4. Paired electrical data and high-resolution imaging before and after on the same specimens, linking the electrical "blind spot" reported by RWTH to visible degradation and copper corrosion at coating ends and defects.
- To make results comparable and citable, the protocol could:
  - follow D1676 §186–195 or IEC 60851-4 Test 20-style sealed ageing;
  - report fluid identity, water content (Karl Fischer) and vessel atmosphere;
  - include immersed and vapour or headspace zones, as the WCT, CDT and Epic/Solvay do;
  - include a dry air or inert control;
  - measure the oil's conductivity, dissipation factor and BDV before and after;
  - optionally add a bare-copper witness (WCT/CDT-like) so insulation degradation can be separated from fluid corrosivity;
  - consider a cyclic-temperature arm, given Lubrizol's finding that cycling increased corrosion.

### Gaps
- The no-prior-study conclusion rests on web searches, vendor, standards and society pages, and the sibling catalogue. Google Scholar, Scopus, IEEE Xplore full-text search, Semantic Scholar and OpenAlex could not be queried (blocked or rate-limited). Before submission, the team should run a final database check with strings such as:
  - ("transmission fluid" OR "e-fluid" OR ATF) AND (hairpin OR "magnet wire" OR "winding wire") AND (PEEK OR parylene OR "heat shrink" OR "powder coating" OR polyimide) AND (aging OR ageing)
- Two items found but not opened may be close: "Impact of Cooling Oil on Partial Discharge and Insulation Reliability in Inverter-Fed EV Motors" (academia.edu, 2025) and "Compatibility of Automatic Transmission Fluids with Structural Polymers Used in Electrified Transmissions" (ResearchGate). The second sits in the polymer–oil slice covered by another researcher.
- Afton's SAE full text, Lubrizol's void-fraction test and Victrex's 2000 h ATF data were not accessible. Any of them could hold unpublished multi-material comparisons, though none was described as including application-method or imaging comparisons.
