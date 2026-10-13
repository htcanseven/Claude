# Copper / insulated-conductor corrosion in EV drive-unit fluids, ATF and oil-immersed electrical systems, and imaging / surface-characterisation methods for documenting degradation

Source-type labels: [PEER] peer-reviewed journal; [CONF] conference paper (SAE technical papers listed as CONF); [STD] standard or standards-body page; [PATENT]; [THESIS]; [VENDOR] additive, lubricant, instrument, test-lab or equipment company material; [TRADE] trade press or society magazine. "Abstract only" means only the abstract or landing page could be opened. Where an abstract was read through the Crossref or Semantic Scholar API (publisher pages blocked automated access), the API URL is cited. Research cut-off: October 2026.

## Q1. Mechanisms: how copper and insulated conductors corrode or degrade in ATF, e-fluids and analogous oil-immersed electrical systems

### Takeaway
In EV drive-unit fluids, the main threat to copper is sulfur chemistry from additives. Extreme-pressure (EP) and antiwear chemistry, and some sulfur-bearing inhibitors that break down at about 150 °C, form copper sulfide. That sulfide can thin bare wires (metal loss) or form loose, partly conductive deposits that bridge conductors at different potentials (the EV "conductive deposit" failure mode). The rate depends strongly on formulation and phase (liquid vs vapour), and it is not monotonic with temperature. The transformer "corrosive sulfur" literature shows the insulated-conductor analogue. Under a paper wrap, Cu2S forms by crevice-type electrochemical corrosion, migrates into the wrap and lowers its dielectric strength. Oxygen and temperature control whether the sulfide stays on the copper or moves into the insulation. Enamel acts as a barrier, so bare copper (cut ends, stripped or welded zones) and wrapped or creviced regions are the places most at risk.

### Cited Findings

**EV/ATF fluids: additive chemistry, temperature and phase**
- Lubrizol's wire-resistance study used 64 µm Cu wire at 130 °C. Two EP gear oils (an API GL-4 mineral and a thermally stable API GL-5 synthetic) caused "complete disintegration of the wires after 30 and 60 hours". Four ATFs left the wires intact. Conclusion: "The EP containing fluids are extremely corrosive to bare uncoated copper". On mechanism: the dimercaptothiadiazole (DMTD) inhibitor is planar and adsorbs on copper through its sulfur atoms, which "donate electrons to the unoccupied d orbital of copper to form a strong coordinate bond". The choice of dispersant changed both corrosion rate and morphology. Without a metal deactivator, the films formed were non-protective: "the presence of a metal deactivator is required to produce a protective film" [PEER, JSAE Int. J. Automotive Eng.; full PDF opened] — [Gahagan & Hunt (Lubrizol Ltd), IJAE 7 (2016) 115-120](https://www.jstage.jst.go.jp/article/jsaeijae/7/4/7_20164092/_pdf)
- Two commercial ATF corrosion inhibitors were tested at 110, 120, 130 and 150 °C. They were "equally as effective up to temperatures of 130 °C; however ... at 150 °C, the thiadiazole inhibitor is breaking down leading to severe pitting on the surface. Corrosion performance therefore, cannot be assumed to be effective at all temperatures" (abstract only) [PEER] — [Warren, Hunt, Bryant, Neville, Morina, Gahagan, Lubrication Science 2018, DOI 10.1002/ls.1422 (Crossref record)](https://api.crossref.org/works?rows=1&query.bibliographic=Automatic%20transmission%20fluid%20corrosion%20inhibitor%20interactions%20with%20copper)
- Leeds PhD findings:
  - "increasing the temperature at which testing took place did not always speed up the corrosion process". In one case corrosion slowed at higher temperature, and in most cases the mechanism changed.
  - Additive antagonisms appeared at 120 °C (dispersant 1 vs an antiwear/antioxidant/friction-modifier mix) and at 150 °C (detergent 2 vs the same mix).
  - Three fully formulated fluids produced flaking copper-sulfide-type surfaces. All of them lacked the benzotriazole-type inhibitor and had higher levels of the thiadiazole inhibitor and a quaternary-amine dispersant. The sulfur came from additive molecules, not the base oil (<0.03 % S).
  - In one fluid, FIB cross-section plus EDX showed a cracked, porous surface layer made mostly of Cu and S. Wire-radius loss (2 µm) understated the copper found in the oil (306 ppm). The author explains this by noting that "copper sulfide is known to be partially conductive".

  [THESIS] — [B. Warren, "The Interaction of Automatic Transmission Fluid Additives with Copper", PhD, Univ. of Leeds, 2018 (record)](https://etheses.whiterose.ac.uk/id/eprint/22729/); [full PDF](https://etheses.whiterose.ac.uk/id/eprint/22729/1/Warren_BLM_Mechanical_Engineering_PhD_2018.pdf)
- Vapour vs liquid phase (Hunt & Prengaman, Lubrizol, SAE 2020-01-0561, as summarised in a trade review): five electrified/conventional transmission lubricants were tested at 110, 120, 130 and 150 °C. "Lubricant A in the vapor phase featured the highest amount of corrosion at 130 °C, yet much less corrosion at any other temperature, even higher temperatures". In the solution phase, "Lubricant C had the most corrosion at 150 °C" [CONF via TRADE; SAE full text not opened] — [Shah et al., PIN Feb/Mar 2023 (PDF)](https://koehlerinstrument.com/wp-content/uploads/2023/05/The-Possibility-of-Using-Copper-Corrosion-Tests-for-Lubricants-Used-with-Electric-Vehicles.pdf)
- In immersion-cooling candidate fluids (130 °C, 336 h), even PAO and diester showed significant vapour-phase corrosion in one test. The formulated dielectric coolant showed minimal corrosion (abstract only) [PEER] — [Tormos et al., Batteries 10(8):285, 2024 (Crossref record)](https://api.crossref.org/works/10.3390/batteries10080285)
- EP additives that protect gears "can promote copper corrosion". According to Lubrizol, one OEM accepted a compromise that retained some EP chemistry, based on wire-test data. Corrosion of aluminium busbars can be tested the same way [TRADE] — [Donaldson, E-Mobility Engineering](https://www.emobility-engineering.com/lubrizol-wire-corrosion-test/)
- Antiwear, EP and friction-modifier additives compete with copper passivators for the metal surface. Passivators such as triazoles and thiadiazoles are film formers that "react chemically with the surface", and "<0.1 %" is usually enough where little copper is exposed. Water, oxygen and "active sulfur" attack copper, and metal temperature in operation promotes corrosion [TRADE, quoting additive-supplier chemists] — [Aikin, STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)

**Conductive deposits: the EV-specific failure mode**
- Lubrizol patent US 12,529,004 B2 (priority 2022-04-06, granted 2026-01-20):
  - Definition: "A conductive layer deposit is defined as the formation of solids created by corrosion or lubricant degradation by-products". Its "chemical identity ... [was] determine[d] to be copper sulfide". "Formation of this conductive deposit may result in catastrophic failure of the electric drive unit".
  - In the PCB test (150 °C, 5 V, solution and vapour phases), a lower-sulfur lubricant formed no deposits. A higher-sulfur comparator formed deposits in both phases at the same time. A fluid optimised for FZG wear and solution-phase copper corrosion still failed.
  - The patent cites a figure in SAE 2020-01-0561 that shows a motor failure caused by a conductive deposit shorting the windings.
  - Claimed mitigation: borate ester plus thiadiazole.

  [PATENT] — [US12529004B2](https://patents.google.com/patent/US12529004B2/en)
- Copper sulfide deposits can bridge conductors at different electrical potentials and cause shorts in circuits or motors [TRADE] — [Plant Engineering reprint of STLE article, 15 Apr 2024](https://www.plantengineering.com/evolution-of-copper-corrosion-testing-for-electric-vehicle-lubricants/)

**Water and hydrolysis (insulation-side mechanism that interacts with fluid chemistry)**
- "The transmission oil resistance can be directly affected by the hydrolysis resistance due to water included". "The insulation retention property of the transmission oil resistance may be affected by type or amount of oil additives" [PATENT, Hitachi Cable / Hitachi Magnet Wire, priority 2008] — [US8193451B2](https://patents.google.com/patent/US8193451B2/en)
- The Afton SAE paper also studied water concentration in electric transmission fluid as a magnet-wire ageing factor, and found that additive package/formulation drives large differences in magnet-wire performance (abstract only) [CONF/journal] — [SAE 2023-32-0145 (Crossref record)](https://api.crossref.org/works?rows=1&query.bibliographic=Magnet%20Wire%20Compatibility%20Test%20for%20Electric%20Drivetrain%20Fluid%20Development)
- Polyimide tape: "Continuous exposure to hot water can affect the tensile strength, elongation, and dielectric strength of standard Kapton® HN". DuPont offers Kapton WR "for applications where hydrolytic stability is important" [VENDOR, DuPont bulletin H-24923-3, 2006] — [DuPont Kapton motor and magnet wire bulletin (PDF)](https://stenbacka.fi/wp-content/uploads/sites/3/2019/08/Kapton-Polyimidefilms-eng.pdf)
- E-fluid oil "damages the enamelled wire by penetrating the coating layer and deteriorating its mechanical properties" [THESIS, abstract/record only] — [L. Yang, RWTH Aachen PhD 2023](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1)

**Transformer analogue: corrosive sulfur, Cu2S formation and migration into wrapped insulation**
- Doble (Griffin & Lewand, 74th Doble Client Conference, 2007):
  - Corrosive sulfur forms metal sulfides that "contaminate the insulating paper". "Since the metal sulfides are conductive, the dielectric breakdown strength of the paper is reduced".
  - A second mechanism is "flaking of copper sulfide from the conductor that then bridges across electrical insulation". Detached Cu2S flakes are 1-2 µm thick, with flakes up to 8 µm measured.
  - "The enamel creates a barrier preventing reaction with the corrosive sulfur". Lower-voltage apparatus with enamelled conductors therefore have an advantage over paper-wrapped ones.
  - "Corrosive sulfur problems are both time and temperature dependent". Sealed units are more susceptible, apparently because oxygen competes with sulfur for reaction sites. This "slows down the formation of the conductive metal sulfides but does not stop their formation". Sealed designs also run 10-15 °C hotter.
  - Failures occurred in oils that had passed ASTM D1275A or DIN 51353 at the time.

  [VENDOR/CONF] — [Griffin & Lewand, "Understanding Corrosive Sulfur Problems in Electric Apparatus" (PDF)](https://www.doble.com/wp-content/uploads/2007-Understanding_Corrosive_Sulfur.pdf)
- Oxygen and temperature control where Cu2S ends up:
  - "most of the deposition found in the paper was in air breathing vials and not sealed vials".
  - "the sealed vials pushed the deposition towards the copper instead of the paper".
  - Ageing at 150 °C pushed deposition toward the copper. Ageing at 140 °C for 4 days pushed it toward the paper.

  [VENDOR, Doble app note, 2007] — [Doble AppNote CCD tests (PDF)](https://www.doble.com/wp-content/uploads/Doble_AppNote_CCD_tests.pdf)
- Crevice mechanism under a wrap. Evidence comes from a failed 500 kV reactor and from lab ageing under IEC 62535 conditions with 500 mg/kg DBDS:
  - The paper winding pattern produced "an alternate appearance of a non-corroded crevice and a strip-shaped corrosion deposit on the copper conductor".
  - More paper layers aggravated sulfur corrosion, hindered copper-ion diffusion into the oil and accelerated acid formation.
  - The crevice formed by the wrap is "an important occurrence precondition of crevice corrosion". The mechanism is theorised as electrochemical corrosion that forms copper sulfide.

  (abstract only) [PEER] — [Gao, Yang, Ding, IEEE Access 2019, DOI 10.1109/ACCESS.2019.2894125 (Semantic Scholar API record)](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ACCESS.2019.2894125)
- Paper-wrapped and bare copper wires were thermally aged in oil at 130 °C and 150 °C. "Copper sulfide deposition on surfaces of copper wires and insulation paper changes the surface structures of copper wires and insulation paper". "The copper sulfide deposition greatly reduces the electrical breakdown strength of oil-paper insulation". "Metal passivator is capable of preventing copper wires from sulfur corrosion" (abstract only) [PEER] — [Li, He, Bao, Yang, Energies 4:1563, 2011, DOI 10.3390/en4101563 (Crossref record)](https://api.crossref.org/works?rows=1&query.bibliographic=Influences%20of%20Corrosive%20Sulfur%20on%20Copper%20Wires%20and%20Oil-Paper%20Insulation%20in%20Transformers%20Energies)
- Copper corrosivity is not directly tied to total sulfur content but to the chemical types of sulfur compounds present [STD, scope page only] — [ASTM D130-26](https://store.astm.org/d0130-26.html)

**Exposed copper on hairpins (cut ends, stripped and welded zones)**
- After hairpin welding, "the side of the stator where the welds are exposed needs protection from oxidation, moisture" and conductive materials. An epoxy powder coating is applied ("This process is called impregnation"), and the epoxy is later laser-stripped from connector tabs. Typical hairpin insulations listed are PAI, PEEK and PAI + polyimide foil [VENDOR, Laserax, 23 Feb 2023] — [Laserax: What is a Hairpin Motor](https://www.laserax.com/blog/hairpin-motor)
- A CO2 laser strips the bulk insulation but leaves "the residual 1-2 µm layer", which a nanosecond fiber laser then removes. "a single micron of insulation residue on the copper produces weak welds". Residue removal was verified by fluorescence ("<9 RFU") [VENDOR, Novanta, 3 Sep 2023] — [Novanta white paper page](https://novanta.com/precision-manufacturing/resources/whitepapers/unlocking-efficiency-in-electric-motors-the-power-of-hairpin-stripping/)

### Inferences
- For oil-cooled hairpins, the copper actually exposed to fluid is limited to cut ends, stripped or welded zones not fully covered by epoxy powder, damaged spots and coating defects. These areas behave like the bare wires in the WCT and CDT, so sulfur-active fluids (EP-rich, or with inhibitors that break down at ≥150 °C) could corrode them and produce conductive Cu-S deposits near the weld zones and connection tabs. This is inferred from the Lubrizol, Leeds and patent findings plus the hairpin process descriptions.
- Wrapped or sleeved constructions (Kapton tape, PEEK tube, heat-shrink) can create oil-filled crevices over copper. The transformer evidence (crevice corrosion and Cu2S migration under paper wraps, worse with more layers) suggests that cut ends and overlaps under tapes or tubes should be opened and inspected after ageing. This is an analogy, not shown for EV fluids.
- Because corrosion is non-monotonic with temperature and differs between liquid and vapour phases, an ageing protocol at a single temperature with fully immersed specimens may miss worst cases. Partially immersed specimens, or a separate headspace specimen, would cover both phases.
- Water content of the oil is a confounder for polymer insulation (hydrolysis of PAI/PI/polyimide film) and should be controlled or recorded. This is inferred from the Hitachi and Afton statements and the DuPont note.

### Gaps
- Electric-field or voltage effects: search listings point to Yang et al., Ind. Eng. Chem. Res. 2017 (DOI 10.1021/acs.iecr.7b01666; electric fields accelerate Cu2S deposition on insulation windings) and De Carlo et al., IEEE TDEI 2013 (DOI 10.1109/TDEI.2013.6508759; higher field strength increased deposits on paper). Neither page could be opened (403 or empty), so these claims are unverified here. No primary source was found on how electric field or current flow alters copper corrosion in EV e-fluids, beyond the voltage-biased CDT.
- ZDDP specifically in ATF/e-fluids: no primary source opened that isolates ZDDP's effect on copper in EV fluids. Friction modifiers appear only as part of mixed-additive antagonisms (Leeds thesis).
- Under-film corrosion beneath magnet-wire enamel in oil, and corrosion initiating at enamel pinholes: no direct study found. Doble states that enamel is a barrier, but there is no data on defects.
- Galvanic effects (Cu-Al busbars, brazes, steel laminations) in oil with water contamination: no relevant source found.
- Dissolved-oxygen effects in EV fluids specifically: not found. Only the transformer evidence (Doble) is available.

## Q2. Test methods and rating scales (ASTM D130, corrosive-sulfur tests, EV wire-corrosion and conductive-deposit tests, magnet-wire oil and hydrolysis tests)

### Takeaway
For EV fluids, two methods have largely taken over from the subjective D130 strip rating:
- The Lubrizol-originated Wire Corrosion Test (WCT): a thin Cu wire is held in the liquid and vapour phases with resistance logged in real time, typically at 80-150 °C for 72 h. It is in ASTM standardisation as work item WK87553 and is cited in SAE J3200.
- The Conductive Deposit Test (CDT): copper-trace PCBs are energised at 150 °C for up to 500 h, with liquid and vapour monitored. It was published as ASTM D8544-24.

Transformer practice uses ASTM D1275 (bare Cu, 150 °C/48 h) and IEC 62535 (paper-wrapped Cu, 150 °C/72 h). Both give visual pass/fail on the copper (D130 tarnish 4a-4c = corrosive) and on the paper (deposits with a metallic sheen = fail). Magnet-wire makers assess oil resistance with an ASTM oil-bomb test (150 °C, about 2000 h) or sealed-tube hydrolysis tests (with water), followed by breakdown voltage, PDIV and visual crack inspection.

### Cited Findings

**ASTM D8544-24, Conductive Deposit Test (CDT)**
- Title: "Standard Test Method for Determination of Conductive Deposits of Electrical and Mechanical Components from Fluids in Liquid and Vapor States within an Electrically Charged System". Committee D02, subcommittee D02.09.0G.
- Scope: monitors "the formation of dendrites and deposits that are conductive". Conditions "can vary from 80 °C to 180 °C". Typical testing is "150 °C over a period of up to 500 h with a monitored voltage applied". 1000 h is an option not covered by the method. "Both the liquid and vapor areas are monitored". A rate-based index "may be implemented".
- "Fluids known to perform poorly in the field have been shown to fail this test". The method is recommended in SAE J3200. Precision is interim only (scope page only opened).

[STD] — [ASTM D8544-24](https://store.astm.org/d8544-24.html)
- Test-lab description:
  - The PCB copper traces "stand in" for motor windings. Flow is minimal, and the headspace is closed but not sealed.
  - Failure is a fall of gap resistance to a low value. The Conductive Deposit Index (CDI) quantifies resistance variability. Limits are currently set per OEM.
  - ICP (ASTM D5185) of the oil before and after the test is commonly requested to track Cu and S.
  - In a dilution study, one fluid was poor in the vapour phase and another in the oil phase.

  (undated, about mid-2024) [VENDOR, Savant Labs] — [Savant Labs: Electric Driveline Fluid Testing Update](https://www.savantlab.com/testing-highlights/electric-driveline-fluid-testing-update/)
- Lubrizol's version: Cu PCBs in the solution phase and headspace, in a closed, vented vessel at 150 °C with 5 V applied, real-time conductance in µS, and end-of-test (EOT) visual inspection [PATENT] — [US12529004B2](https://patents.google.com/patent/US12529004B2/en)
- G. Miiller (Savant): "The CDT offers an index value over time that can be utilized by the OEMs or specification setting organizations to determine critical limits". "If the resistance drops below a specific value, the fluid has failed". End-of-test board photographs are assessed for deposits and dendrites [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)

**Wire Corrosion Test (WCT)**
- Original configuration:
  - A 1 m long, 64 µm Cu wire with 1 mA DC, which gives no ohmic heating. Repeatability is ±0.05 Ω at end of test.
  - Fluid at 130 ± 0.25 °C, with resistance logged every 10 s. Wire diameter loss is derived from resistance (R = ρl/A).
  - After the test: SEM/EDS of the wire and ICP-OES (ASTM D4951) of the oil.

  [PEER] — [Gahagan & Hunt 2016](https://www.jstage.jst.go.jp/article/jsaeijae/7/4/7_20164092/_pdf)
- Current commercial form:
  - "A thin wire is exposed to an oil and its vapor with a separate circuit for each phase" for 72 h at 80-150 °C.
  - The wires are "spaced sufficiently far apart that no deposits would be able to bridge the gap", so the WCT isolates metal loss from deposit bridging.
  - "the hottest temperature is not always the most severe", especially in the vapour phase.
  - Offered by Savant since 2021. An ASTM D02 SC9 interlaboratory study was planned before December 2024.

  [VENDOR] — [Savant Labs](https://www.savantlab.com/testing-highlights/electric-driveline-fluid-testing-update/)
- Miiller: the "WCT detects corrosion and failures when the D130 test does not". WCT and D130 "can provide distinctly different results". The CDT "will capture conductive deposit failures that neither of the other two tests ... are able to directly assess" [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
- Developers named as G. Hunt and M. Gahagan (Lubrizol), who received an SAE award. The test "is going through the ASTM accreditation process" [TRADE] — [E-Mobility Engineering](https://www.emobility-engineering.com/lubrizol-wire-corrosion-test/)
- Resistance is normalised for temperature (copper resistivity temperature coefficient) and to a 1.01 m standard length to compute material lost [TRADE/VENDOR] — [PIN 2023](https://koehlerinstrument.com/wp-content/uploads/2023/05/The-Possibility-of-Using-Copper-Corrosion-Tests-for-Lubricants-Used-with-Electric-Vehicles.pdf)
- An academic adaptation for immersion-cooling fluids ran 130 °C for 336 h, with vapour and oil circuits followed by SEM [PEER, abstract only] — [Tormos et al. 2024 (Crossref)](https://api.crossref.org/works/10.3390/batteries10080285)
- Solenoid test (Bares et al., SAE Int. J. Fuels Lubr. 13(3), 2020): a transmission solenoid immersed for 250 h and energised at 1 Hz. Brass spacer and bearing are photographed before and after at 120 and 150 °C. The ATF was least corrosive at 120 °C and much more corrosive at 150 °C. A gear oil corroded at both temperatures [TRADE summary of CONF/journal] — [PIN 2023](https://koehlerinstrument.com/wp-content/uploads/2023/05/The-Possibility-of-Using-Copper-Corrosion-Tests-for-Lubricants-Used-with-Electric-Vehicles.pdf)

**ASTM D130 and its optical successors**
- ASTM D130-26 is active (updated March 2026). Its scope covers lubricating oil among other petroleum products, and it is "designed to assess the relative degree of corrosivity of a petroleum product" [STD, scope page only] — [ASTM D130-26](https://store.astm.org/d0130-26.html)
- Criticisms of D130:
  - It relies on operator judgement and varies between labs. It applies no voltage and gives only an end-point rating, and its temperatures and durations do not match EV duty.
  - J. Ayala notes that 7-8 % of people have some colour-vision deficiency.
- CuDDI (Copper Digital Detection Imaging, Ayalytical) is a draft optical rating method, "not yet ... an ASTM test method". Its setup:
  - a CCD camera and a stabilised LED source at about 4,500 K, diffused at 45°;
  - a controlled light box, automatic strip sizing, and auto-rotation to image both faces;
  - an algorithm trained on the D130 colour standards and D130 Table 1 logic.

[TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx); [Plant Engineering reprint](https://www.plantengineering.com/evolution-of-copper-corrosion-testing-for-electric-vehicle-lubricants/)
- The Leeds thesis found that D130 ratings did not correlate well with weight change, Cu in the fluid or wire-radius change, and that film formation was sometimes mistaken for corrosion [THESIS] — [Warren 2018](https://etheses.whiterose.ac.uk/id/eprint/22729/)

**Transformer corrosive-sulfur tests**
- ASTM D1275-24, bare copper:
  - Since 2015 it is a single method with the former Method B parameters: 150 ± 2 °C for 48 h, 220 mL of oil in a 250 mL sealed glass bottle after a 5 min N2 sparge at 0.5 L/min.
  - The strip is a V-bent 6 × 25 mm Cu foil (0.127-0.254 mm thick). A silver-strip option exists.
  - Results "cannot be compared or correlated to the method prior to 2006" (old Method A was 19 h at 140 °C).
  - "Copper is slightly less sensitive to sulfur corrosion than silver but the results are easier to interpret".

  [STD, preview page] — [ASTM D1275-24 (iTeh preview)](https://standards.iteh.ai/catalog/standards/astm/ca64b1cb-2b34-4bf0-9884-c67570d10657/astm-d1275-24)
- IEC 62535:2008 (TC 10, stability date 2029): "a copper conductor, wrapped with one layer of paper, immersed in the oil and heated ... to evaluate the capability of the oil to yield copper sulphide and transfer it to paper layers". Tests with and without paper are complementary [STD] — [IEC webstore](https://webstore.iec.ch/en/publication/7167)
- CIGRE WG A2.32 CCD test (proposed as IEC 62535):
  - Run in duplicate with air-saturated oil in capped vials, 3 days (72 h) at 150 °C.
  - Copper is rated on the ASTM D1275B/D130 tarnish scale: 1a-3b pass (non-corrosive), 4a/4b/4c fail (corrosive).
  - Paper fails if deposits show a "metallic sheen". Dull deposits of any density pass.
- Doble's own CCD variant runs 4 days at 140 °C with one vented and one sealed vial. Optional confirmatory tests on the paper are dielectric strength, resistivity and SEM/EDX.

[VENDOR] — [Doble AppNote CCD (PDF)](https://www.doble.com/wp-content/uploads/Doble_AppNote_CCD_tests.pdf)
- DIN 51353:2021-06, "Testing of insulating oils - Detection of corrosive sulfur - Silver strip test", replaces the 1985 edition (title and edition page only) [STD] — [DIN Media page](https://www.dinmedia.de/en/standard/din-51353/336710044)

**Magnet-wire oil and hydrolysis resistance tests (insulated conductor, not just bare copper)**
- In the ASTM oil-bomb test ("Resistance to Insulating Liquids and Hydrolytic Stability of Film-Insulated Magnet Wire"), wire is held in oil "at a temperature of 150° C. for approximately 2000 hours". Afterwards "the wire is again tested for dielectric breakdown, PDIV, and a visual inspection for cracking may be performed". The patent says transmission fluid "can break down traditional magnet wire insulation materials, such as enamel insulations", and proposes an extruded PEEK/PAEK-based layer over the enamel [PATENT, Essex, priority 2014] — [US9543058B2](https://patents.google.com/patent/US9543058B2/en)
- Sealed-tube hydrolysis test: a twisted pair with 0.4 mL water in a 400 mL fused glass tube (0.1 vol %), 140 °C for 1000 h. The result is reported as residual breakdown voltage (80.5-88.3 % in the examples) [PATENT, Hitachi] — [US8193451B2](https://patents.google.com/patent/US8193451B2/en)
- Afton's magnet-wire/ETF compatibility procedure covers sample preparation, ageing and evaluation. Criteria are adhesion, breakdown voltage and partial-discharge behaviour, on round and rectangular wire with polyester, polyamide and polyimide coatings, with water content as a variable (abstract only) [CONF/journal] — [SAE 2023-32-0145 (Crossref)](https://api.crossref.org/works?rows=1&query.bibliographic=Magnet%20Wire%20Compatibility%20Test%20for%20Electric%20Drivetrain%20Fluid%20Development)
- Rig-level check: Infineum reports "over 1,000 hours of durability testing in an OEM electric drive unit rig". The end-of-test parts "look almost brand new, with no impact to gears, bearings and copper windings" (EOT visual inspection; no protocol given) [VENDOR, 20 May 2025] — [Infineum Insight: Balancing efficiency and durability](https://www.infineuminsight.com/en-gb/articles/balancing-efficiency-and-durability/)

### Inferences
- The proposed study (insulated hairpins aged in e-fluid) sits between two established families. One is fluid-centric copper tests (D130, WCT, D8544), which use bare copper as a sensor of fluid aggressiveness. The other is insulation-centric magnet-wire tests (oil bomb, sealed-tube hydrolysis), which use electrical retention and a visual crack check. Adding bare-copper witness specimens (D130 strip or a thin wire) to each ageing vessel would tie the insulation observations to a recognised measure of fluid corrosivity.
- The transformer CCD test is the closest standardised precedent for visually rating a wrapped conductor after oil ageing. Its two-part pass/fail (conductor tarnish plus deposit appearance on the wrap) could be adapted to rate tape-, tube- or sleeve-insulated hairpin specimens.
- D8544's choice of 150 °C, ≤500 h, energised, liquid plus vapour, gives a recognised reference condition for an ageing temperature and duration that reviewers will accept.

### Gaps
- ASTM WK87553 (titled in search listings "New Test Method for the Determination of Wire Corrosion and Oxidation from Fluids in Liquid and Vapor States Within an Electrically Charged or Mechanical System") returned HTTP 403. Its current status (work item or published method) could not be verified. No 2025-2026 source confirming publication of a WCT ASTM standard was found.
- SAE J3200 content was not opened. Its listing of CDT and WCT relies on the ASTM D8544 page and vendor statements.
- DIN 51353 test conditions (search snippets: silver strip, 18 h at 100 °C) were not verified on an opened page.
- The ASTM D130 rating table (1a-4c descriptions) was not opened. The 4a-4c = corrosive convention is sourced only through the Doble note.
- The oil-bomb test's ASTM designation (reported as ASTM D1676 in search listings) was not confirmed in the opened patent text.
- Infineum's "energised corrosion test" with video imaging of dendrite growth appeared only in a search-engine summary. No primary page was found, so it is unverified.

## Q3. Imaging and surface characterisation used for oil-aged insulation or conductors (protocols and what they revealed)

### Takeaway
Documentation practice in this field is dominated by:
- end-point visual colour rating of copper (D130 scale);
- photographs of end-of-test PCBs and parts (CDT, solenoid test, rigs);
- SEM/EDS of copper wires and coupons, with FTIR/XPS, FIB cross-sections and ICP of the oil;
- for the transformer analogue, visual plus SEM/EDX inspection of wrap paper.

Quantitative image or colour methods are only now emerging: CuDDI machine-vision rating, and CIELAB ΔE*ab, which separated samples that were all D130/ISO 2160 "Class 1" with ΔE of 0.4-11.1. Standard frameworks exist for colour difference (ASTM D2244, with CIEDE2000 recommended for small differences) and for blister rating (ASTM D714 photographic references). No published protocol was found for calibrated before/after photography of insulated EV conductors.

### Cited Findings

**SEM/EDS and analytical protocols on oil-exposed copper**
- Lubrizol's protocol:
  - Tabletop SEM (Hitachi TM-1000) with EDS (Z>11), giving approximate relative Cu and S atomic %. Images at ×1500 with a 50 µm scale bar, plus a new-wire reference image.
  - Approximate wire diameter measured in the SEM. ICP-OES (ASTM D4951) of the oil.
- What it showed:
  - EP gear oils: wires disintegrated, with only fragments left.
  - "chemically induced pitting corrosion" in some ATF-type blends.
  - Protective films in others; loosely bound, possibly polymeric films with "slight flaking"; clean surfaces; "sporadic covering and dark gaps" when the metal deactivator was absent.

  [PEER] — [Gahagan & Hunt 2016](https://www.jstage.jst.go.jp/article/jsaeijae/7/4/7_20164092/_pdf)
- Leeds thesis protocol:
  - Coupon immersion followed by FTIR, SEM and XPS, plus 64 µm wire tests (1 m on a 3D-printed nylon former, about 400 mL fluid, 1 mA, 10 s logging).
  - Fluid sent for ICP-AES. Wires stored in clean polythene bags before analysis.
  - FIB cross-section plus EDX of a corrosion layer.
- What it showed: SEM grouped samples by surface features (flaking = copper sulfide, pitting at 150 °C with a thiadiazole inhibitor). FTIR peak groupings "showed little correlation" with formulation, so SEM morphology was more diagnostic. XPS distinguished Cu(I) and Cu(II) species (Cu2O, CuO/Cu(OH)2, CuSO4).

  [THESIS] — [Warren 2018 PDF](https://etheses.whiterose.ac.uk/id/eprint/22729/1/Warren_BLM_Mechanical_Engineering_PhD_2018.pdf)
- How D130 colours relate to film chemistry (literature reviewed in the thesis): Kashima & Nose used electron diffraction and found D130 films were often Cu2O at low ratings with Cu2S overlayers, with Cu2S alone only at high ratings. The 1a-3a colours reflect oxide-film thickness (interference), and "the degree of corrosion shown in the ratings was not linear". SEM of strips exposed to elemental sulfur showed sulfide nodules whose number rose with sulfur concentration [THESIS, secondary] — [Warren 2018 PDF](https://etheses.whiterose.ac.uk/id/eprint/22729/1/Warren_BLM_Mechanical_Engineering_PhD_2018.pdf)
- SEM of wires from 336 h/130 °C tests distinguished vapour-phase corrosion (PAO, diester) from minimal attack (formulated coolant) (abstract only) [PEER] — [Tormos et al. 2024](https://api.crossref.org/works/10.3390/batteries10080285)

**Photographic, visual and colorimetric documentation**
- CDT: end-of-test photographs of boards are assessed for deposit accumulation and dendrite formation [TRADE] — [STLE TLT Jan 2024](https://www.stle.org/files/TLTArchives/2024/01_January/Feature.aspx)
- Lubrizol CDT boards: EOT visual inspection found no visible deposits for the passing fluid, although "the vapor-phase PCB base material showed some darkening". The failing fluid had visible deposits [PATENT] — [US12529004B2](https://patents.google.com/patent/US12529004B2/en)
- CuDDI machine-vision rating setup (draft): CCD camera, stabilised ~4,500 K LED diffused at 45°, enclosed light box, both faces imaged, D130-trained classifier. The algorithm "is fixed and not subject to variations in color perception or color blindness" [TRADE] — [Plant Engineering reprint](https://www.plantengineering.com/evolution-of-copper-corrosion-testing-for-electric-vehicle-lubricants/)
- Colorimetry of copper strips (EN ISO 2160): all samples were visual Class 1, yet colorimetry gave ΔE*ab of 0.4-11.1, highest for aged fuels. The authors conclude colorimetry "enables differentiation between fuels within the same acceptance category" (abstract only) [PEER] — [Vlčková et al., Fuels 7(3):42, 2026 (Crossref)](https://api.crossref.org/works?rows=1&query.bibliographic=Colorimetric%20Assessment%20as%20a%20Complementary%20Approach%20to%20Visual%20Copper%20Corrosion%20Evaluation%20in%20Automotive%20Fuels)
- ASTM D2244 (colour-difference calculation; D2244-23 page, D2244-25 active) covers CIELAB ΔE*ab, CMC, CIE94, DIN99o and CIEDE2000:
  - ΔE00 is "highly recommended" for differences up to about 5 ΔE*ab units.
  - Compare differences only within the same colour system. Report the three components as well as the scalar.
  - The equations are based on daylight, so metamerism should be checked (D4086) under other illuminants.

  [STD, scope page] — [ASTM D2244-23](https://store.astm.org/d2244-23.html)
- ASTM D714 "employs photographic reference standards to evaluate the degree of blistering" (size and density). It is primarily for metal and other non-porous coated surfaces. D714-02(2017) page opened; D714-25 is active [STD, scope page] — [ASTM D714](https://store.astm.org/d0714-02r17.html)
- Solenoid test: brass spacers and bearings photographed after 250 h at 120 and 150 °C to compare fluids [TRADE] — [PIN 2023](https://koehlerinstrument.com/wp-content/uploads/2023/05/The-Possibility-of-Using-Copper-Corrosion-Tests-for-Lubricants-Used-with-Electric-Vehicles.pdf)

**Transformer analogue: imaging of Cu2S in wrapped insulation**
- Doble, 2007:
  - SEM/EDX of CCD-test paper at 400-8000×: copper sulfide coats the fibres, grows "bridges between two fibers" and shows cracks. EDX shows C and O from the paper and Cu and S from the deposits. The authors believe Cu2S "begins as small deposits on and perhaps in the paper then grows outward from the nucleus".
  - Visually, tarnish "turns gray and can be mistaken for carbon from overheating". "Unwrapping the copper conductor can reveal further tarnish". Cu2S on paper "ranges considerably in coloration depending upon severity, oxygen levels, closeness to the conductor" and "is also not uniformly distributed", so multiple regions must be searched.
  - SEM showed Cu2S flakes 1-2 µm thick, up to 8 µm.

  [VENDOR/CONF] — [Griffin & Lewand 2007 (PDF)](https://www.doble.com/wp-content/uploads/2007-Understanding_Corrosive_Sulfur.pdf)
- CCD visual classes for paper: no deposition; heavy, moderate or light dull deposits (pass); heavy, moderate or light deposits with metallic sheen (fail). Example photographs of rods and papers are included. Confirmatory SEM/EDX, dielectric strength and resistivity are available [VENDOR] — [Doble AppNote CCD (PDF)](https://www.doble.com/wp-content/uploads/Doble_AppNote_CCD_tests.pdf)
- Field and lab documentation of paper-wrapped windings showed the wrap pattern imprinted on the copper: alternating non-corroded crevice and strip-shaped deposit (abstract only) [PEER] — [Gao et al., IEEE Access 2019 (Semantic Scholar API)](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ACCESS.2019.2894125)
- Cu2S deposition "changes the surface structures of copper wires and insulation paper". It was characterised alongside broadband dielectric spectroscopy of paper and oil (abstract only) [PEER] — [Li et al., Energies 2011 (Crossref)](https://api.crossref.org/works?rows=1&query.bibliographic=Influences%20of%20Corrosive%20Sulfur%20on%20Copper%20Wires%20and%20Oil-Paper%20Insulation%20in%20Transformers%20Energies)

**Hairpin-specific surface checks**
- Laser-stripped hairpin ends: residual insulation (1-2 µm after CO2 laser) is verified by fluorescence ("<9 RFU") [VENDOR] — [Novanta](https://novanta.com/precision-manufacturing/resources/whitepapers/unlocking-efficiency-in-electric-motors-the-power-of-hairpin-stripping/)

**Counter-example: ageing studies without visual documentation**
- PEI/PAI enamelled wire aged to 15,000 h at 40 °C/93 % RH was characterised by Weibull breakdown, TGA and FTIR only. Specimens were microscope-checked for cracks only before testing, and no post-ageing images were reported [PEER, IIETA MMEP 2024] — [Kerkarine & Nedjar 2024](https://www.iieta.org/journals/mmep/paper/10.18280/mmep.110423)

### Inferences
- A defensible imaging protocol for the planned study, assembled from the sources above (not a published protocol):
  1. Fixed-geometry, diffuse-illumination photography of both faces of each specimen at fixed magnification, with a colour/grey reference in frame. CuDDI's enclosed box, ~4,500 K diffuse 45° LED and two-face imaging is a precedent.
  2. Colour change quantified as CIELAB ΔE (ΔE00 for small changes, with components reported) at pre-defined regions of interest (ASTM D2244), from a spectrophotometer or a calibrated camera.
  3. Stereo or optical microscopy for crazing, cracking and blistering, rated with an ASTM D714-style size and density scale.
  4. SEM/EDS (Cu, S, O, plus Zn, P, Mo, B from additives) on cut ends, stripped and welded zones, and any deposits.
  5. Cross-sections (metallographic or FIB) at cut ends and tape or tube overlaps to look for under-film or crevice attack.
  6. ICP of the aged oil for Cu and S, as in the CDT and WCT practice.
- The Leeds result that SEM morphology was more diagnostic than FTIR groupings, and the D130 colour/chemistry non-linearity, both argue for pairing colour metrics with SEM/EDS rather than relying on colour alone.
- Ex-situ wiping or cleaning can remove loosely bound films ("slight flaking", "loosely bound"). The cleaning procedure (e.g., solvent rinse vs none) should be fixed and reported, because it changes what the images show.

### Gaps
- No published, validated protocol was found for colour-calibrated before/after photography of insulated conductors (enamel, PEEK, tapes) after oil ageing. ΔE has been applied to copper strips in fuels (2026), but no source was found applying it to oil-aged magnet-wire insulation.
- Confocal or 3D profilometry and FTIR mapping on oil-aged winding insulation: no source found within the tool-call budget.
- Raman detection of corrosive sulfur in transformer oil (High Voltage 2022, DOI 10.1049/hve2.12238) and the High Voltage 2021 corrosive-sulphur review (DOI 10.1049/hve2.12155) are open access, but Wiley/IET blocked automated access, so their content was not used.

## Q4. Studies combining oil ageing of insulated wires (or insulated conductors) with before/after imaging, and how visual change was quantified

### Takeaway
No peer-reviewed study was found that photographed insulated EV hairpins (or other magnet wire) before and after ageing in ATF/e-fluid and quantified the visual change (e.g., ΔE or image analysis). The closest EV work is the Afton SAE paper on magnet-wire compatibility with electric transmission fluids, whose criteria are adhesion, breakdown voltage and PD (imaging content not verifiable), and the RWTH Aachen PhD showing that e-fluid penetrates and mechanically weakens enamel. Bare-copper studies (Lubrizol, Leeds, Tormos) document wires by SEM after ageing. The closest methodological precedent for "insulated conductor + oil ageing + visual rating" is the transformer covered-conductor deposition test (IEC 62535 / CIGRE / Doble). It rates the conductor and the wrap after ageing, by visual class with optional SEM/EDX, but qualitatively. A calibrated before/after imaging study of differently insulated hairpins would therefore fill a documented gap.

### Cited Findings
- **Afton SAE magnet-wire compatibility study:** the closest EV-specific study. Round and rectangular magnet wire (polyester, polyamide, polyimide coatings) were aged in electric transmission fluids, with water concentration varied. Evaluation used adhesion, breakdown voltage and PD. Additive chemistry produced "significant MW performance differences", and the authors discuss deterioration mechanisms. Abstract only, so whether before/after images or quantitative visual metrics were used is unknown. [CONF/journal] — [Kwak, Grzyska, Cleveland, Tsuneo, SAE 2023-32-0145 (Crossref)](https://api.crossref.org/works?rows=1&query.bibliographic=Magnet%20Wire%20Compatibility%20Test%20for%20Electric%20Drivetrain%20Fluid%20Development)
- **RWTH Aachen PhD on e-fluid direct cooling:**
  - Study: e-fluid oil and a water-based lubricant as direct coolants for low-voltage machines. Twisted pairs plus electrical, mechanical and thermal ageing in oil, with humidity and contamination studies.
  - Results: e-fluid oil penetrates enamel and degrades its mechanical properties. PDIV rises with oil impregnation, and PD disappears when oil fills voids. Oil had no significant influence on mechanical ageing. The water-based lubricant was compatible.
  - Conventional PDIV and capacitance diagnostics "cannot evaluate the material compatibility appropriately". This supports adding non-electrical (visual or microscopic) evidence.
  - The record does not state which imaging was used.

  [THESIS, record only] — [L. Yang, RWTH 2023](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1)
- **Transformer: wrapped and bare copper wires** aged in oil at 130 and 150 °C. Surface-structure changes of the copper and paper were documented, and breakdown strength was greatly reduced; passivator prevented corrosion (abstract only) [PEER] — [Li et al., Energies 2011 (Crossref)](https://api.crossref.org/works?rows=1&query.bibliographic=Influences%20of%20Corrosive%20Sulfur%20on%20Copper%20Wires%20and%20Oil-Paper%20Insulation%20in%20Transformers%20Energies)
- **Transformer: field reactor plus IEC 62535-condition lab ageing** of paper-wrapped conductors. The documented pattern was crevice versus strip-shaped deposit, and severity was graded by "corrosion degree" (abstract only) [PEER] — [Gao et al., IEEE Access 2019](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/ACCESS.2019.2894125)
- **Transformer: CCD test** as a standardised before/after visual rating of a wrapped conductor. Copper is rated against the D130 tarnish scale and paper by deposit density and sheen, with photographic examples and optional SEM/EDX [VENDOR] — [Doble AppNote CCD](https://www.doble.com/wp-content/uploads/Doble_AppNote_CCD_tests.pdf); SEM/EDX images of CCD paper at 400-8000× [VENDOR/CONF] — [Griffin & Lewand 2007](https://www.doble.com/wp-content/uploads/2007-Understanding_Corrosive_Sulfur.pdf)
- **Magnet-wire industry oil tests:** the post-test "visual inspection for cracking" is binary or qualitative; no imaging metric is described [PATENT] — [US9543058B2](https://patents.google.com/patent/US9543058B2/en). The sealed-tube hydrolysis test reports only residual breakdown voltage [PATENT] — [US8193451B2](https://patents.google.com/patent/US8193451B2/en)
- **Bare-wire EV-fluid studies with post-test imaging:**
  - SEM of 64 µm wires after 130 °C ageing (×1500, 50 µm scale bar, EDS Cu/S %). Visual change was described qualitatively (pitting, films, flaking, disintegration) and quantified only through resistance-derived diameter loss and ICP [PEER] — [Gahagan & Hunt 2016](https://www.jstage.jst.go.jp/article/jsaeijae/7/4/7_20164092/_pdf)
  - FIB/EDX cross-sections [THESIS] — [Warren 2018](https://etheses.whiterose.ac.uk/id/eprint/22729/)
- **Drive-unit rig:** EOT teardown photos showed windings "with no impact" after more than 1,000 h. This is qualitative only [VENDOR] — [Infineum 2025](https://www.infineuminsight.com/en-gb/articles/balancing-efficiency-and-durability/)
- **Counter-example:** a long-term humid-ageing study of PEI/PAI wire did not image specimens after ageing [PEER] — [Kerkarine & Nedjar 2024](https://www.iieta.org/journals/mmep/paper/10.18280/mmep.110423)

### Inferences
- The planned design (photograph dry insulated hairpins, age in oil at operating temperature, re-photograph, document corrosion and degradation) has precedents only in pieces:
  - qualitative visual pass/fail on wrapped conductors (transformer CCD);
  - SEM of bare wires (EV fluids);
  - electrical retention plus a crack check on magnet wire (oil bomb and hydrolysis tests).
- Combining calibrated photography and ΔE with microscopy, SEM/EDS at exposed copper and an electrical retention metric across several insulation systems would be novel, and is defensible from the cited methods.
- Including a bare-copper witness (D130 strip or a thin wire) and ICP of the aged oil in each ageing vessel would let reviewers separate insulation degradation from fluid corrosivity, matching how D8544 and the WCT are reported.

### Gaps
- A Shanghai Zhongtuo Magnet Wire page reportedly reports polyimide enamelled wire aged in transmission oil at different water contents and cycle counts, with appearance, breakdown voltage and PDIV assessed. The page returned HTTP 403, so this is unverified.
- A Chinese patent on ATF-resistant enamelled wire (US 12,159,731) reportedly uses sealed-tube ATF immersion with 155 °C/40 h and -45 °C/8 h cycles ×8. Seen only in a search summary, not opened.
- Full texts of SAE 2023-32-0145, SAE 2020-01-0561 and Bares et al. 2020 (which reportedly includes a motor-failure photograph and before/after part photos) were not accessible.
- No source was found that documents before/after imaging of PEEK-extruded, PEEK-tube, heat-shrink, Kapton-tape, epoxy-powder or parylene-insulated conductors after oil ageing. (Polymer-oil compatibility data were assigned to another researcher and were not searched here.)
