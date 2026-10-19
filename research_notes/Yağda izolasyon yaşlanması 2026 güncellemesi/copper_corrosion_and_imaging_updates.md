# Copper corrosion, conductive deposits and imaging of oil-aged copper and insulated conductors: new public findings, January 2025 – October 2026

Source-type labels: [PEER] peer-reviewed journal; [CONF] conference paper or conference abstract (SAE technical papers listed as CONF); [STD] standard, standards listing or ASTM work-item page; [PATENT]; [BOOK]; [VENDOR] material from an additive, lubricant, instrument or test-lab company; [TRADE] trade press.

Reading status is stated for every source:
- "full text": the whole document was read.
- "abstract only".
- "metadata only": title, authors and date from Crossref or Semantic Scholar, with no abstract available.
- "search summary only": the page was blocked, so its content is known only from search-engine result text.

Sources already in the existing review are excluded unless new data appeared. The one exception, Vlčková et al. 2026, is flagged: the review had only its abstract, and the full text has now been read.

Search cut-off: 19 October 2026. Search scope:
- web search;
- Crossref and Semantic Scholar APIs, filtered to 2024-10 → 2026-12;
- Google Patents;
- STLE 2025 programme.

The STLE 2026 programme could not be opened (blocked by the host).

## Q1. Which new studies or data exist (2025–2026), and what were their methods, conditions, fluids and quantitative results?

### Takeaway
Very little new peer-reviewed, quantitative work on copper corrosion in EV drive-unit fluids appeared in the window. The new numbers come almost entirely from patents:
- Afton US 12,662,647 B2 (granted June 2026): extended ASTM D130 (150 °C/168 h) copper-leaching data.
- Chevron Japan US 12,529,005 B2 (granted January 2026): copper-in-oil data after ISOT (165.5 °C/96 h).
- Tannas/Lubrizol: the WCT apparatus patent (granted September 2024; missing from the review).

Everything else is abstract-level or qualitative:
- an IOCL SAE paper (June 2026, abstract only);
- Shell and Chevron Oronite talks at STLE 2025;
- an Infineum article (February 2025) describing an energised corrosion test with video imaging of dendrite growth;
- a 2025 CRC book chapter, "Solving for Corrosion and Conductive Deposit Concerns" (metadata only).

Standards moved only slightly:
- ASTM D8544-24 is still the current edition (February 2026 listing).
- No published ASTM wire-corrosion standard was found.
- A D130 revision adding a calibrated digital-imaging step (WK99361) is open.

Transformer work from 2025–2026 adds:
- passivator dose-response data on paper-wrapped copper;
- temperature dependence and saturation of Cu2S deposition;
- activation of "inactive" thiophenic sulfur to H2S and elemental S;
- modelling of how Cu2S deposits promote partial discharge.

### Cited Findings

**EV drive-unit fluids: new papers, patents and conference items**

- **IOCL SAE paper (2026), abstract only:**
  - Fluids: conventional GL-5, manual transmission fluid (MTF), automatic transmission fluid (ATF) and dedicated e-fluids, studied "to understand additive and viscosity effects".
  - Conclusion: "additive chemistry plays a significant role on key properties such as electrical properties, corrosion resistance, oxidation resistance, and tribological performance".
  - The abstract and landing page name no copper test method, temperature, duration or numeric result.

  [CONF] — [Katta L., Seth S., Singh S., Bhardwaj A., Arora A. K. (Indian Oil Corp. R&D), "Electrical and Copper Compatibility Studies of Transmission Lubricants for Advanced Electric Vehicles", SAE Technical Paper 2026-01-5036, 3 June 2026, DOI 10.4271/2026-01-5036](https://saemobilus.sae.org/papers/electrical-copper-compatibility-studies-transmission-lubricants-advanced-electric-vehicles-2026-01-5036)

- **Afton patent US 12,662,647 B2 (2026). Patent data.**
  - Bibliographic: inventors Kun Liu, Yungwan Kwak and Joseph Remias; filed and priority 23 Aug 2024; granted 23 June 2026; pre-grant publication US 2026/0055333 A1.
  - Claim 1: an EV/HEV driveline lubricant containing:
    - a phosphorus antiwear additive providing "about 100 ppm or less" P;
    - an oil-soluble organomolybdenum friction modifier/corrosion inhibitor with ester and/or amide groups (about 1–15 wt % Mo);
    - "less than about 300 ppm" total sulfur.
  - Test method: ASTM D130 extended to 150 °C for 168 h. It reports copper leached into the oil (ppm; detection method not stated) plus the D130 tarnish rating.
  - Pass criteria: Cu leaching < 120 ppm, and HFRR friction < 0.160 (130 °C, 400 g, 20 Hz).
  - Blend base: Group III base oil (KV100 ≈ 3.7 cSt) with 0.06 wt % ashless dialkyl dithiophosphate in every blend. The tables list 133 ppm P, and total S of 174 ppm except 229 ppm for the MoDTC blend.
  - Results (Cu leached, ppm / D130 rating / HFRR):

    | Blend | Additive and treat rate | Cu (ppm) | D130 rating | HFRR |
    |---|---|---|---|---|
    | Baseline | no friction modifier | 144 | 2B | 0.155 |
    | Inventive | Mo ester/amide FM, 0.04 wt % | 117 | 2B | 0.146 |
    | Inventive | Mo ester/amide FM, 0.2 wt % | 61 | 2A | 0.115 |
    | Inventive | Mo ester/amide FM, 0.5 wt % | 64 | 2B | 0.056 |
    | Comparative | MoDTC, 0.05 wt % | 121 | 3A | 0.145 |
    | Comparative | fatty polyamine FM, 0.04 wt % | 206 | 4A | 0.132 |
    | Comparative | fatty polyamine FM, 0.2 wt % | 326 | 4A | 0.127 |
    | Comparative | fatty polyamine FM, 0.5 wt % | 347 | 4A | 0.080 |
    | Comparative | methyl-1H-benzotriazole, 0.04 wt % | 43 | 2A | 0.160 |

  - Only the three Mo ester/amide blends met both criteria.
  - Reading status: full text read through the fetch tool (first ~100k of ~170k characters). A direct download to re-check the table cells was blocked by Google.

  [PATENT] — [US 12,662,647 B2, "Use of molybdenum compounds in driveline lubricants for reduced friction and copper corrosion", Afton Chemical Corp.](https://patents.google.com/patent/US12662647B2/en)

- **Chevron Japan patent US 12,529,005 B2 (published 2025, granted 2026). Patent data.**
  - Bibliographic: inventors Sawairi, Shimizu, Fuchi, Nakagawa, Ohta, Kubo and Minami; priority 16 Nov 2021; published as US 2025/0109350 A1 on 3 Apr 2025; granted 20 Jan 2026.
  - Claim 1:
    - base oil with KV100 of 1.5–20 mm²/s;
    - a thiadiazole plus a sulfurized polyolefin, together supplying 0.01–0.2 wt % S;
    - a phosphorus compound;
    - a borated PIB-succinimide dispersant at 0.3–2.0 wt %.
  - Dependent claims: < 50 ppm metals with volume resistivity > 1.0 × 10⁹ Ω·cm at 80 °C, and a triazole (tolyltriazole-type) corrosion inhibitor.
  - Test methods:
    - Copper corrosion: Cu (ppm, ICP) in the oil after the Indiana Stirring Oxidation Test (ISOT). The ISOT followed JASO M315-2015 §5.16, "except that the temperature was raised to 165.5° C. to make the test more stringent (the standard … is 150° C.)", for 96 h, with copper and steel catalyst plates and a glass varnish rod.
    - Volume resistivity: JIS C2101 at 80 °C and 250 V, on new oil and after the 96 h ISOT.
    - Wear: Shell four-ball (1800 rpm, 80 °C, 392 N, 60 min).
    - Deposits: Komatsu hot tube (KHT) at 250 °C, chosen because the "thermal durability of the protective coating of polyimide ester or polyamide-based enamel on the wire used in hybrid and electric vehicles is 200 to 240° C". KHT was also run at 270 °C.
  - Results (Table 1, parsed directly from the patent HTML):

    | Blend group | Composition | ISOT Cu (ppm) |
    |---|---|---|
    | Comparatives with conventional sulfurized olefins | — | 309; 421 (the second also produced sludge) |
    | Comparatives with sulfurized PIB only (0.031 wt % S) | three different P additives; no thiadiazole, no added inhibitor | 62, 45, 71 |
    | Examples 1–4 and 6–9 | sulfurized PIB + thiadiazole + 0.03 wt % corrosion inhibitor | 5–18 |
    | Example 5 | 0.102 wt % S from sulfurized PIB + 0.034 wt % S from thiadiazole | 95 |

    The table row for the thiadiazole is labelled "sulfur EP additive". Its sulfur values match 34.0 wt % S × dose (my identification).
  - Same total S, different sulfur source: at 0.136 wt % total S, Example 4 (0.068 % from PIB + 0.068 % from thiadiazole) gave 18 ppm Cu, and Example 5 (0.102 % + 0.034 %) gave 95 ppm.
  - Volume resistivity: 2.4–10 × 10⁹ Ω·cm new, and 1.8–3.9 × 10⁹ Ω·cm after ISOT.
  - Four-ball wear scar: 1.69–1.85 mm for the comparatives vs 0.54–0.66 mm for the examples.
  - KHT merit at 250 °C: 3.5–9.0. Removing the dispersant gave KHT 4.0–6.0 at 250 °C and "Blocked"/0.0 at 270 °C, plus ISOT sludge.
  - Patent text on enamel: oil is "directly sprayed onto the enamel wire". "If a highly reactive extreme pressure agent is used in the lubricating oil, a high temperature deposit may be formed. The deposit can build up around the enamel wire, reducing cooling efficiency and causing damage."
  - Reading status: full text read; tables re-parsed from the HTML.

  [PATENT] — [US 12,529,005 B2, "Lubricating oil compositions for electric vehicles", Chevron Japan Ltd.](https://patents.google.com/patent/US12529005B2/en)

- **Tannas Co. patent US 12,092,562 B2 (late 2024; not in the existing review): the WCT apparatus. Patent data.**
  - Bibliographic: inventors G. J. Hunt, M. P. Gahagan, M. A. Peplow, C. P. Prengaman and R. Riman; priority 31 Jan 2020; granted 17 Sep 2024.
  - Wire: ≥ 95 wt % Cu (other metals optional), diameter 0.05–5 mm. The example uses 0.064 mm × ~1 m, chosen to approximate gearbox solenoid wire (~0.128 mm). Paired wires are matched within ±5 % in diameter.
  - Phase separation:
    - A "solution wire" sits in the liquid and a "vapour wire" sits only in the headspace.
    - The part of the solution wire that passes through the vapour space may be replaced by larger-gauge or coated wire (≥ 2–3 × diameter), so that only the immersed part acts as the sensor.
  - Operating range: the description states a bulk-fluid temperature range of 20–300 °C. A constant-current source limits self-heating. An electrode-based embodiment applies 5–800 V.
  - Measurement:
    - Four-wire resistance (Fluke 8846A; NI-9226/NI-9216 modules, up to 16 channels) after 12 h of stabilisation.
    - Resistance change is converted to wire-radius loss. Figures show radius loss in nm vs time and Arrhenius plots of corrosion rate; the values are only plotted.
  - Reading status: full text partly read (~100k of ~245k characters).

  [PATENT] — [US 12,092,562 B2, "Device and testing apparatus for liquid and vapor wire exposure testing", Tannas Co.](https://patents.google.com/patent/US12092562B2/en)

- **Shell talk, STLE 2025 (abstract only):**
  - Problem statement: "Laboratory tests frequently show that fluids with sulfur-containing additives tend to exhibit poorer performance with respect to copper corrosion, but the mechanism of corrosion has not been well established."
  - Hypothesis: "corrosive molecules such as hydrogen sulfide, a potential degradation product of sulfur-containing additives, may contribute".
  - Method: a new "test method developed to detect degraded gaseous byproducts in lubricants". It "has been correlated with other standard copper corrosion test methods", and "solid analysis on corroded deposits" was performed.
  - No numbers or techniques are given in the abstract.

  [CONF] — [Vo L., Uy D., Ogunsola O., Matthews S. (Shell Global Solutions US), "Copper Corrosion Inhibition in e-Transmission Fluids – A Mechanistic Insight", abstract 4203368, 79th STLE Annual Meeting, Atlanta, 18–22 May 2025 (preliminary programme PDF dated 20 Dec 2024)](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)

- **Chevron Oronite talk, STLE 2025 (abstract only):**
  - Electric driveline fluids need "low susceptibility to copper corrosion".
  - The talk covers "tribological, corrosion, and oxidation properties of functionalized sulfur-containing antiwear additives". No data in the abstract.

  [CONF] — [Tanuwidjaja J., Holbrook T., Stribling L., Wall D., Curtis M., Singa T. (Chevron Oronite), "Structure-Property of Functionalized Sulfur-Containing Antiwear Additives for Application in Electric Driveline Fluids", abstract 4242868, STLE 2025 (same programme PDF)](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)

- **Lubrizol talk, STLE 2025 (abstract only; no corrosion data):**
  - Describes "an advanced fluid" that "protects and cools inverter, e-motor and gearbox", as a single oil cooling and lubrication circuit.
  - Consortium of FlandersMake, Dana, Diabatix and Lubrizol. The abstract presents thermal-hydraulic modelling and hardware tests.

  [CONF] — [Gahagan M. (Lubrizol), "All-In-One e-Fluid Technology to Cool Inverter, e-Motor and Provide EV Gear Lubrication", abstract 4205093, STLE 2025](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)

- **Infineum article, 27 Feb 2025 (full text):**
  - Why it matters: with motors in the transmission, "the copper wire and connections are susceptible to corrosion", leading to current leakage or short circuit.
  - The energised corrosion test (ECT):
    - The ECT uses "a single printed circuit board with copper grids". It "can be used with a covering board to provide a capillary gap".
    - "Board spacing can be tuned with a spacer washer", and "various board designs have been used to investigate trace spacing impact".
    - Tuning trace and board spacing "had a significant impact on fluid performance", which shows "the critical importance of tuning test conditions and set-up".
  - Imaging: a "novel video imaging system" has given "new insights into copper corrosion mechanisms". The figure caption reads "Deposit / dendrite growth between anode and cathode".
  - Not given: temperature, voltage, duration or numeric results.

  [VENDOR] — [Wood A., Campbell S., Thaker H., Ishikawa M. (Infineum), "Leading the way in e-fluid developments", CTI Symposia, 27 Feb 2025](https://cti-symposium.world/leading-the-way-in-e-fluid-developments/)

- **CRC Press book chapter (2025), metadata only:**
  - Chapter: Gregory Miiller, "Solving for Corrosion and Conductive Deposit Concerns", pp. 62–73. The Crossref record gives no affiliation; he is probably the Savant Labs G. Miiller quoted in the review's STLE TLT source (name match only).
  - Book: *Electric Vehicle Fluid Testing*, CRC Press, 10 Sep 2025, DOI 10.1201/9781003496069; credited to L. I. Farfán-Cabrera, P. Lee and A. Erdemir in Semantic Scholar.
  - Companion chapters: "Electrical Properties of EV Fluids" (ch. 3), "Degradation Testing" (ch. 4), "Grease Degradation/Water Resistance" (ch. 10) and "Electrified Pin-on-Disk Testing of Greases" (ch. 11).
  - The publisher page returned HTTP 403, so the contents are unknown.

  [BOOK] — [Miiller G., "Solving for Corrosion and Conductive Deposit Concerns", in *Electric Vehicle Fluid Testing*, CRC Press 2025, DOI 10.1201/9781003496069-2 (Crossref record)](https://api.crossref.org/works/10.1201/9781003496069-2)

- **Savant Labs EV-fluid testing page (full text; undated, latest dated asset September 2025). This is a different page from the Savant page cited in the review.**
  - Afton-developed tests:
    - "extended D130": copper strip exposure extended to "168 hours or another desired duration", with samples pulled for ICP of soluble copper;
    - "vapor phase copper test": a strip hung above the heated sample in a closed container, visually rated after 48 h.
  - Neither Afton test uses powered circuits. "Test methods are being formalized", and Savant took part in the interlaboratory studies.
  - WCT: heated for 72 h; corrosion rate is computed per phase from the rise in resistance. Lubrizol found the rate "responds uniquely to temperature" (Hunt & Prengaman 2020).
  - CDT: runs for "a few hundred hours to 1000 hours". Failure is a resistance drop below a critical value for a given time. A figure shows "dendrite growth" on a board that caused a short.
  - Draft Federal Test Methods were submitted for both the WCT and the CDT, and both are referenced in the draft SAE J3200.

  [VENDOR] — [Savant Labs, "Electric Vehicle Lubricant and Fluid Testing"](https://www.savantlab.com/testing-highlights/electric-vehicle-lubricant-and-fluid-testing/)

**Standards and test-method status (2025–2026)**

- **ASTM D8544 still at the 2024 edition:** a February 2026 ASTM Book of Standards (vol. 05.05) listing still shows D8544-24. No D8544-25 or -26 was found (search summary only) [STD] — [ASTM BOS listing, vol. 05.05, Feb 2026](https://store.astm.org/products-services/standards-and-publications/standards/bos-standards.html?volume=05.05&year=2026&month=february); [DIN Media record of ASTM D 8544-2024](https://www.dinmedia.de/en/standard/astm-d-8544/379236773)
- **CDT considered for EV coolants:** an ASTM D15 presentation dated 24 Sep 2025 lists a "CDT Conductive Deposit Test based on ASTM D8544" under "Tests Under Consideration" for subcommittee D15.26 (Electric Vehicle Coolants). This means the CDT is spreading from driveline fluids to EV coolants. Search summary only; the PDF returned HTTP 503 [STD] — [Morrison A., ASTM International presentation to ARSO, 24 Sep 2025 (PDF)](https://www.arso-oran.org/wp-content/uploads/2025/10/USA-ASTMInternational-2025-09-24-ARSO-Presentation-Updated-Allan-Morrison-ASTM-D15-26-.pdf)
- **ASTM WK99361 (revision of D130-26; page returned HTTP 403, search summary only):** the work item proposes to add "an objective digital imaging protocol" after the standard visual exam.
  - It would use "a calibrated imaging system under controlled lighting" to measure colorimetric parameters (RGB, hue, saturation, intensity).
  - It adds an expanded digital adjunct with a wider range of corrosion examples.
  - Its rationale is that the current rating depends on observer colour perception, lab lighting and borderline strips.

  Related work items appear in search results only: WK95661 would allow machine vision as an alternative to manual rating, and WK91029 would add a coupon-sizing gauge. Their dates and status were not verified. [STD] — [ASTM WK99361](https://www.astm.org/membership-participation/technical-committees/workitems/workitem-wk99361); [ASTM WK95661](https://store.astm.org/workitem-wk95661)

**Transformer corrosive-sulfur work (2025–2026) relevant to wrapped or enamelled conductors**

- **Benzotriazole dose on paper-wrapped copper (2026, abstract only):**
  - Set-up: kraft-paper-wrapped copper aged in mineral oil containing 7 ppm elemental sulfur (S8), with BTA at 0, 10, 50 and 100 ppm, for 14 days at 104 °C.
  - Result: inhibition was clearly concentration-dependent. At 100 ppm BTA, paper surface resistivity improved by up to 83.1 % and tensile strength by up to 11.9 %.

  [CONF] — [Zulkefli N. I. H., Khiar A., Chairul I. S., Ghani S., Mohamad Saleh S. H., "Effect of Benzotriazole Concentration on Kraft Paper Insulation Degradation in Sulfur-Contaminated Mineral Oil", 2026 IEEE 6th Int. Conf. on Dielectrics (ICD), June 2026, DOI 10.1109/ICD64907.2026.11665189](https://doi.org/10.1109/ICD64907.2026.11665189)

- **Cu2S deposits and partial discharge (2025, abstract only; simulation, point–plane electrodes):**
  - Cu2S deposits on oil–paper "enhance the intensity of the electric field within the oil gap", speed up streamer progression and cause "severe surface discharge" when the streamer reaches the Cu2S.
  - Greater deposit thickness shortens the streamer diffusion distance and reduces the onset time of surface discharge.
  - Wider deposits spread charge, so surface charge density rises more slowly and peaks lower.

  [PEER] — [Cong H.-X., Su W., Wang Y., Qiao L., Li Q.-M., Xu M., "Mechanism of Copper Sulfide Deposition on Oil-Paper Insulation Partial Discharge Under Extremely Uneven Electric Field", IEEE Trans. Dielectr. Electr. Insul., April 2025, DOI 10.1109/TDEI.2024.3466113](https://doi.org/10.1109/TDEI.2024.3466113)

- **"Inactive" thiophenic sulfur can become corrosive (2025, abstract only):**
  - Pyrolysis of thiophenic sulfides yields "hydrogen sulfide and its ion (H2S, HS−), elemental sulfur (S, S2), and hydrogen and its ion (H2, H+)".
  - Thiophene has the lowest activation energy, followed by benzothiophene and dibenzothiophene.
  - "Long-term thermal action" decomposes them into "low molecular corrosive sulfides", which intensifies oil corrosivity and leads to corrosion of oil–paper insulation.
  - Methods: analysis of decomposition products, activation energy at varied heating rates, molecular dynamics and a thermal-ageing verification test.

  [PEER] — [Gao S.-H., Lei Y., Liu Y., Huang C., Yang L.-J., "The Corrosion and Activation Mechanism of Thiophenic Sulfides in the Oil-Paper Insulation", IEEE TDEI, June 2025, DOI 10.1109/TDEI.2025.3539260](https://doi.org/10.1109/TDEI.2025.3539260)

- **Temperature dependence of sulfide deposition on Cu–Ag contacts (2026, abstract only; contacts rather than windings):**
  - Set-up: DBDS-containing oil aged at 90, 115 and 140 °C.
  - Deposition: the deposition rates of copper sulfide and silver sulfide increase with temperature, but "when the aging process reaches a certain threshold" deposition saturates.
  - Oil effects: DBDS significantly raises oil acid value and moisture and increases the dielectric loss factor, while breakdown voltage falls. The authors attribute this to "shedding of sulfur corrosion products" and the higher moisture.

  [PEER] — [Hu X., Liu Y., Cong H.-X., Kong L., Su W., Zheng H., Li Q.-M., "Thermal Aging Behavior and Deterioration Mechanism of Copper–Silver Contacts and Insulating Oil Under Sulfur Corrosion", IEEE TDEI, April 2026, DOI 10.1109/TDEI.2026.3656479](https://doi.org/10.1109/TDEI.2026.3656479)

- **DBDS and partial discharge in mineral oil (2025, abstract only; the abstract does not state whether copper was present):**
  - Set-up: mineral oil with different DBDS concentrations aged at 150 °C for 5 days.
  - AC breakdown voltage decreased as DBDS concentration rose, for all electrode configurations.
  - Average apparent PD charge increased. PDIV increased at a 10 mm gap.

  [PEER] — [Selva A. M., Azis N., Tariq M. U., Ab Kadir M. A., Jasni J., Zainuddin H., "Investigation of Partial Discharge Characteristics in Mineral Oil Induced by Dibenzyl Disulfide", Pertanika J. Sci. & Technol. 33(2), 7 Mar 2025, DOI 10.47836/pjst.33.2.17 (open access)](https://doi.org/10.47836/pjst.33.2.17)

**Insulation-side ageing in ATF that touches fluid chemistry or surface analysis**

- **PAI in ATF with and without water (2025, abstract only):**
  - Water in the oil "facilitates the hydrolysis of PAI insulation, increases the acidity of the oil, and further accelerates material aging".
  - FTIR of the PAI showed "significant changes in the content of C-H and P-O bonds". The authors confirm that "oxidation and hydrolysis driven by temperature and moisture" are the main causes.
  - PDIV and breakdown voltage were also measured.

  [CONF] — [Li J., Li Z., Yu C., Wang P., "Aging Effects of Automatic Transmission Fluid on Polyamideimide Insulation for Transportation Traction Motors", 2025 IEEE CEIDP, Sep 2025, DOI 10.1109/CEIDP61707.2025.11218487](https://doi.org/10.1109/CEIDP61707.2025.11218487)

**Non-oil EV analogues (electrical bias, dendrites)**

- **Hyundai high-voltage cable connectors, 2025 (full text; not oil-immersed):**
  - Failure: severe oxidation and pitting at Sn-coated Cu ground terminal / Al connector interfaces.
  - Multi-stress test (14 cycles):
    - vibration per ISO 16750-3 (24 h);
    - DC bias of 10.0 mA (2.0 mA/cm²);
    - salt spray, 3 h at 35 °C with 5 % NaCl;
    - humidity, 14 h at 49 °C and 95 % RH.
  - Documentation: SEM/EDS (fretting wear, Al2O3), plus X-ray imaging of the cables to identify material interfaces.
  - Leakage currents in AC and DC systems fell "within critical stray current corrosion thresholds", especially during deceleration and braking.

  [PEER] — [Shin S., Ahn S., Lim H., "Investigation into the Corrosion Mechanism of High-Voltage Cables in Eco-Friendly Vehicles", Corrosion Science and Technology 24(4):203–211, 2025, DOI 10.14773/cst.2025.24.4.203 (PDF)](https://www.j-cst.org/data/issue/CST/C002404/C00240400203.pdf)
- **Dendrites in power modules, 2025 (abstract only; gas phase and humidity, not oil):** dendritic corrosion products grow in power-module isolation trenches under humidity and corrosive gases, until they bridge the trenches. Applied heating "effectively inhibit[s]" the growth by lowering the effective relative humidity and the adsorbed water layer [PEER] — [Rautio J. et al., "Reliability of Power Modules in Corrosive Environments: Effect of Heating on Dendritic Corrosion Growth in the Isolation Trenches", IET Power Electronics 2025, DOI 10.1049/pel2.70015 (open access)](https://doi.org/10.1049/pel2.70015)

### Inferences
- **Patents dominate the new numbers.** In this window, the only new quantitative copper-loss data for EV fluids are patent examples from lubricant and additive companies. They come from fluid-centric tests: extended D130 copper leaching, ISOT copper in oil, and WCT radius loss. None involves insulated conductors. The planned insulated-hairpin ageing-and-imaging design therefore still has no direct precedent.
- **The fluid must be characterised.** Copper attack varies by up to about two orders of magnitude between plausible formulations: 5–421 ppm Cu after ISOT at 165.5 °C/96 h, and 43–347 ppm after D130 at 150 °C/168 h. The e-fluid chosen for the study should therefore be analysed before and after ageing (ICP for Cu, S, P, Mo, B and metals). Without this, the results cannot be generalised.
- **Industry reference temperatures:**
  - 150 °C (CDT, extended D130);
  - 165.5 °C (Chevron's harsher ISOT);
  - 250 °C (KHT for hot-enamel deposits).

  Chevron's explicit link of the KHT temperature to enamel thermal durability (200–240 °C) is new evidence that fluid developers now design deposit tests around magnet-wire enamel.
- **A prior gap is closed.** The Infineum CTI article (Feb 2025) is the primary source for the energised test with video imaging of dendrite growth. The existing review could cite that test only from a search-engine summary.

### Gaps
- **Not accessible:** full texts of SAE 2026-01-5036 and the 2025 CRC chapter by Miiller. Their test methods and data are unknown.
- **Abstract or metadata only:**
  - abstract only: the TDEI, ICD, CEIDP and Pertanika items, so their numbers could not be checked in the full text;
  - metadata only (no abstract available): CSEE JPES 2026, "Effects of Pyrolysis of Metal Passivator on Characteristics of Insulating Oil Under Thermal Condition" ([DOI 10.17775/cseejpes.2022.08940](https://doi.org/10.17775/cseejpes.2022.08940));
  - metadata only: IEEE TDEI 2026, "Varnish–Oil Compatibility and Degradation Mechanisms for Enhanced High-Temperature Electrical Insulation Performance" ([DOI 10.1109/TDEI.2026.3735262](https://doi.org/10.1109/TDEI.2026.3735262));
  - metadata only: Fuel 2026, "Traceability of unqualified copper strip corrosion in light naphtha: Formation and impact of elemental sulfur" ([DOI 10.1016/j.fuel.2025.137939](https://doi.org/10.1016/j.fuel.2025.137939)).
- **STLE 2026 not screened:** the Annual Meeting programme PDF was blocked (Incapsula), so 2026 STLE talks are not covered.
- **No new SAE data:** no 2025–2026 SAE paper with numeric WCT or CDT results was found. No publication of the ASTM wire-corrosion method (WK87553) was found.
- **Screened and excluded (not about copper corrosion):**
  - Shore & Kadiric, Tribology Transactions 2025 (EV drivetrain efficiency; [DOI 10.1080/10402004.2025.2488799](https://doi.org/10.1080/10402004.2025.2488799));
  - García Tuero et al., Lubricants 13(5):209, 2025 (ionic-liquid ATF tribology under electrification; [DOI 10.3390/lubricants13050209](https://doi.org/10.3390/lubricants13050209));
  - SAE 2026-26-0053 (e-transaxle efficiency).
- **Possibly relevant, outside the window and absent from the review (not read; for the coordinator to decide):**
  - "100 Years of Corrosion Testing—Is It Time to Move beyond the ASTM D130? The Wire Corrosion and Conductive Deposit Tests", SAE Int. J. Fuels Lubr. 17(1) (publication date not verified) ([SAE page](https://www.sae.org/publications/technical-papers/content/04-17-01-0002/));
  - "Understanding Conductive Layer Deposits: Test Method Development…", SAE Int. J. Electrified Vehicles 12(2), 2023 ([SAE page](https://saemobilus.sae.org/articles/understanding-conductive-layer-deposits-test-method-development-for-lubricant-performance-testing-hybrid-electric-vehicle-applications-14-12-02-0014)).

## Q2. When do e-fluids form conductive copper-sulfide deposits, and how do liquid-phase and vapour-phase behaviour differ? (Includes fluid chemistry, temperature, electrical bias and field evidence.)

### Takeaway
The 2025–2026 material does not overturn the review's picture. Conductive deposits are copper sulfide formed from sulfur-bearing additive chemistry, and the risk depends on the type of sulfur and the additive balance rather than total sulfur. It adds four refinements:
1. **Mechanism.** Shell hypothesises that H2S from degrading sulfur additives drives the attack, and transformer work shows that even "inactive" thiophenic sulfur pyrolyses to H2S and elemental S. Volatile species of this kind give a plausible route for headspace (vapour-phase) attack. However, no 2025–2026 public source quantifies liquid versus vapour behaviour.
2. **Formulation.** Patent data show that copper loss rises sharply with amine friction modifiers and conventional sulfurized olefins. It falls with thiadiazole, triazole-type inhibitors and Mo ester/amide chemistry. At equal total S, shifting sulfur from sulfurized PIB to thiadiazole cut copper in oil about five-fold.
3. **Geometry and bias.** Infineum's energised test shows that trace spacing and capillary gaps strongly change fluid performance, and video shows deposits and dendrites growing between anode and cathode. No numbers are public.
4. **Field evidence.** No new field failure analysis of an oil-cooled e-machine or e-axle was published in the window.

### Cited Findings

**Sulfur activation and the H2S hypothesis**
- **Shell's hypothesis (2025):** sulfur-containing additives "tend to exhibit poorer performance" for copper. H2S, "a potential degradation product of sulfur-containing additives", may contribute, and Shell built a test that detects "degraded gaseous byproducts" [CONF, abstract only] — [Vo et al., STLE 2025](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)
- **Transformer analogue for thermal activation:** thiophenic sulfides pyrolyse to H2S/HS−, S and S2. Thiophene is easiest to activate. Long-term heating turns "inactive" sulfur into "low molecular corrosive sulfides" [PEER, abstract only] — [Gao et al., IEEE TDEI 2025](https://doi.org/10.1109/TDEI.2025.3539260)

**Type of sulfur and EP chemistry**
- **Same total sulfur, different copper loss:** at the same total S (0.136 wt %), ISOT Cu was 18 ppm when the S was split 0.068/0.068 between sulfurized PIB and thiadiazole, and 95 ppm when it was split 0.102/0.034.
- **Conventional sulfurized olefins:** comparatives with these gave 309–421 ppm Cu, against 45–71 ppm for sulfurized PIB alone, all without added inhibitor.

  [PATENT, full text] — [US 12,529,005 B2](https://patents.google.com/patent/US12529005B2/en)
- **Deposits on hot enamel:** "highly reactive extreme pressure agent[s]" can form high-temperature deposits that "build up around the enamel wire" in spray-cooled motors [PATENT] — [US 12,529,005 B2](https://patents.google.com/patent/US12529005B2/en)
- **Sulfur-containing antiwear additives:** Chevron Oronite is still developing functionalized sulfur-containing antiwear additives that aim for "low susceptibility to copper corrosion". No data are public [CONF, abstract only] — [Tanuwidjaja et al., STLE 2025](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)

**Friction modifiers, phosphorus and passivators**
- **Afton (extended D130, 150 °C/168 h), relative to the 144 ppm baseline (2B):**
  - Fatty polyamine friction modifier: Cu leaching rose with dose to 206, 326 and 347 ppm, all rated 4A.
  - Mo ester/amide friction modifier: Cu fell to 117, 61 and 64 ppm.
  - MoDTC: 121 ppm (3A).
  - Methyl-benzotriazole at 0.04 wt %: 43 ppm (2A), but friction 0.160 failed the < 0.160 limit. This shows a passivator-versus-friction trade-off.
  - The claims cap total S below about 300 ppm and antiwear P at about 100 ppm or less.

  [PATENT] — [US 12,662,647 B2](https://patents.google.com/patent/US12662647B2/en)
- **Chevron Japan:**
  - An N-alkyl tolyltriazole inhibitor (≤ 0.1 wt %; 0.03 wt % in the examples) "further reduces the copper corrosion levels".
  - Metal-based (e.g., Mo) friction modifiers can lower volume resistivity, so total metals are kept at ≤ 50 ppm.
  - Note: all inventive examples contain the inhibitor and none of the comparatives do. The inhibitor and thiadiazole effects are therefore confounded in Table 1.

  [PATENT] — [US 12,529,005 B2](https://patents.google.com/patent/US12529005B2/en)
- **Passivator on paper-wrapped copper (transformer):** BTA at 10–100 ppm protected paper-wrapped copper in S8-contaminated oil (104 °C, 14 days) in a concentration-dependent way. At 100 ppm, surface resistivity improved by up to 83.1 % and tensile strength by up to 11.9 % [CONF, abstract only] — [Zulkefli et al., ICD 2026](https://doi.org/10.1109/ICD64907.2026.11665189)

**Water**
- **Water in ATF:** water promotes PAI hydrolysis and oil acidification. FTIR shows changes in C–H and P–O bonds [CONF, abstract only] — [Li et al., CEIDP 2025](https://doi.org/10.1109/CEIDP61707.2025.11218487)
- **DBDS raises moisture (transformer):** DBDS raised oil moisture and acid value during sulfur-corrosion ageing [PEER, abstract only] — [Hu et al., IEEE TDEI 2026](https://doi.org/10.1109/TDEI.2026.3656479)

**Temperature**
- **Cu–Ag contacts (transformer):** sulfide deposition rate rises from 90 to 115 to 140 °C, then saturates [PEER, abstract only] — [Hu et al., IEEE TDEI 2026](https://doi.org/10.1109/TDEI.2026.3656479)
- **WCT and temperature:** WCT corrosion rate "responds uniquely to temperature" (Lubrizol; Hunt & Prengaman 2020, cited) [VENDOR] — [Savant Labs EV page](https://www.savantlab.com/testing-highlights/electric-vehicle-lubricant-and-fluid-testing/)
- **WCT apparatus patent:** shows Arrhenius plots of corrosion rate vs temperature; the values are only plotted [PATENT] — [US 12,092,562 B2](https://patents.google.com/patent/US12092562B2/en)
- **Harsher oxidation test:** ISOT was raised from 150 to 165.5 °C "to make the test more stringent" [PATENT] — [US 12,529,005 B2](https://patents.google.com/patent/US12529005B2/en)

**Liquid versus vapour phase**
- **WCT apparatus:** the patent formalises separate solution and vapour wires. Larger-gauge or coated wire is used where the solution wire crosses the headspace, so that each sensor reports only its own phase [PATENT] — [US 12,092,562 B2](https://patents.google.com/patent/US12092562B2/en)
- **Afton's unpowered tests:** the "vapor phase copper test" (strip over heated oil in a closed container, rated after 48 h) and the "extended D130" (168 h, with ICP sampling) are being formalised in interlaboratory studies [VENDOR] — [Savant Labs EV page](https://www.savantlab.com/testing-highlights/electric-vehicle-lubricant-and-fluid-testing/)

**Electrical bias, gap geometry and dendrites**
- **Infineum energised corrosion test:**
  - single PCB with copper grids, optionally with a covering board that creates a capillary gap;
  - board and trace spacing tuned, with "a significant impact on fluid performance";
  - video imaging of "deposit / dendrite growth between anode and cathode".

  [VENDOR] — [Infineum, CTI Symposia, 27 Feb 2025](https://cti-symposium.world/leading-the-way-in-e-fluid-developments/)
- **CDT failure:** on CDT boards, failure is a resistance drop below a critical value "for a given time". A board photo shows dendrite growth that caused a short [VENDOR] — [Savant Labs EV page](https://www.savantlab.com/testing-highlights/electric-vehicle-lubricant-and-fluid-testing/)
- **Electrode embodiment of the WCT apparatus:** applies 5–800 V [PATENT] — [US 12,092,562 B2](https://patents.google.com/patent/US12092562B2/en)
- **Electrical consequence of deposits (transformer, simulation):** Cu2S deposits raise the oil-gap field and promote surface discharge [PEER, abstract only] — [Cong et al., IEEE TDEI 2025](https://doi.org/10.1109/TDEI.2024.3466113)
- **DBDS-aged oil:** lower AC breakdown voltage and higher apparent PD charge [PEER, abstract only] — [Selva et al., Pertanika 2025](https://doi.org/10.47836/pjst.33.2.17)
- **Non-oil analogues:**
  - DC bias combined with vibration, salt and humidity accelerated corrosion of Sn-coated Cu/Al connectors [PEER] — [Shin et al., CST 2025](https://www.j-cst.org/data/issue/CST/C002404/C00240400203.pdf)
  - Heating suppressed dendritic corrosion in power modules by lowering effective relative humidity [PEER, abstract only] — [Rautio et al., IET PE 2025](https://doi.org/10.1049/pel2.70015)

**Field observations**
- **No new teardown reports:** no 2025–2026 public failure analysis of an oil-cooled e-machine or e-axle was found. The only drive-unit rig statement in the window, Infineum (May 2025, "no impact to … copper windings" after more than 1,000 h), is already in the review.
- **Fluid now reaches power electronics:** Lubrizol's 2025 single-circuit e-fluid that "protects and cools inverter, e-motor and gearbox" shows that drive-unit fluids now also reach power electronics. This widens the copper and PCB surfaces exposed to fluid [CONF, abstract only] — [Gahagan, STLE 2025](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)

### Inferences
- **Working mechanism (my synthesis, not shown in any single source):** sulfur-bearing additives, and possibly even nominally inactive sulfur, decompose thermally, especially at or above about 150 °C. This releases H2S or elemental sulfur, which reaches exposed copper in both the liquid and the headspace. Inhibitor films such as triazoles and thiadiazoles form from the liquid and may not protect headspace copper. That would explain why vapour-phase attack can be worse or behave differently.
- **Planned study design:** age specimens both immersed and in the headspace of a closed but vented vessel. Log oil and headspace temperatures. Run ICP for Cu and S on the oil before and after. Add a bare-copper witness in each phase.
- **Formulation as the main variable:** additive choice (friction modifier type, sulfur type, inhibitor) changes copper loss more than total sulfur does. Conclusions drawn with one e-fluid should not be generalised, and the fluid's elemental and additive composition should be reported.
- **Gap geometry:** Infineum's sensitivity to spacing suggests that energised specimens with controlled gaps could reveal deposit bridging that unenergised immersion would miss. This matters for hairpins, where end-winding and weld-to-weld gaps between conductors at different potentials are small.

### Gaps
- **No new public data:**
  - no 2025–2026 numbers comparing vapour and liquid phases;
  - no numeric ECT or CDT results;
  - no study of passivator behaviour in the headspace;
  - no new data on temperature cycling;
  - no source quantifying how DC or AC bias magnitude changes copper-sulfide growth rate in e-fluids.
- **Shell's method is unpublished:** the gas-detection method, its correlation with standard copper tests and its deposit analyses exist as an abstract only.
- **ZDDP not isolated:** no 2025–2026 source isolates ZDDP's effect on copper in EV fluids. The new patents use ashless dithiophosphates, phosphates or phosphonates.
- **Out of window, but directly relevant and absent from the review: Scania's 2021 field failure.** Flagged for the coordinator; not counted as a 2025–2026 finding.
  - Some Scania city plug-in hybrid buses "failed after about 6,000 hours in operation" from "corrosion of the copper wire hairpins".
  - The suspected root cause was a "top-up of 10%-15% of axle fluid".
  - In wire tests (140 °C oil phase and 80 °C vapour phase, 96 h), relative corrosion fell by 80 % from axle oil to MTF, by a further 10 % to ATF, and by a further 90 % to a dedicated e-fluid, for 98 % in total.
  - For the stator, the vapour-phase rate was "about 10 times higher" than the oil-phase rate.

  [TRADE, full text, 2 Aug 2021] — [Kamchev B., "Progress by Failure", Lubes'N'Greases](https://www.lubesngreases.com/magazine/27_8/progress-by-failure/)

## Q3. Are there data on copper corrosion beneath enamel, tape or tubing, or at cut ends and stripped or welded zones?

### Takeaway
No public study from January 2025 to October 2026 was found that measured copper corrosion under magnet-wire enamel, tapes or tubing, or at hairpin cut ends, laser-stripped zones or welds after exposure to EV drive-unit fluids. The gap noted in the existing review remains. The new evidence is only indirect:
- a Chevron patent statement that reactive EP chemistry forms high-temperature deposits that "build up around the enamel wire";
- Infineum's capillary-gap energised test (a crevice-like geometry), which shows that gap size strongly affects outcomes;
- transformer work on paper-wrapped copper (BTA dose-response; Cu2S deposits and partial discharge);
- a 2025 finding that water in ATF hydrolyses PAI enamel and acidifies the oil, which could weaken the enamel barrier over cut or stripped edges (inference).

### Cited Findings
- **Deposits on hot enamel:** in oil-spray-cooled motors, "the oil comes into direct contact with the surface of the high temperature enamel wire", and a "highly reactive extreme pressure agent" may form a deposit that can "build up around the enamel wire, reducing cooling efficiency and causing damage". KHT at 250 °C is used because enamel durability is "200 to 240° C" [PATENT, full text] — [US 12,529,005 B2](https://patents.google.com/patent/US12529005B2/en)
- **Crevice-like geometry in an energised test:** a "covering board to provide a capillary gap" over a copper-grid PCB, and trace or board spacing "had a significant impact on fluid performance" [VENDOR] — [Infineum, CTI Symposia 2025](https://cti-symposium.world/leading-the-way-in-e-fluid-developments/)
- **Wrapped-conductor passivation (transformer):** in kraft-paper-wrapped copper with 7 ppm S8 at 104 °C for 14 days, BTA at 100 ppm improved paper surface resistivity by up to 83.1 % [CONF, abstract only] — [Zulkefli et al., ICD 2026](https://doi.org/10.1109/ICD64907.2026.11665189)
- **Deposits on the wrap (transformer):** the thickness and width of Cu2S deposits on paper change the field, streamer behaviour and surface discharge [PEER, abstract only] — [Cong et al., IEEE TDEI 2025](https://doi.org/10.1109/TDEI.2024.3466113)
- **Enamel barrier and water:** water in ATF accelerates PAI hydrolysis and oil acidification [CONF, abstract only] — [Li et al., CEIDP 2025](https://doi.org/10.1109/CEIDP61707.2025.11218487)

### Inferences
- **The planned study can fill this gap directly.** Include deliberately exposed copper features:
  - cut ends;
  - laser-stripped zones;
  - welded joints with and without the production coating;
  - creviced configurations: tape overlaps, tube ends, and enamel scratched to a defined defect.

  After ageing, open or section these features (unwrap tapes, slit tubing, metallographic cross-sections at cut ends and through overlaps), then image them and run SEM/EDS. Compare them with a bare-copper witness aged in the same vessel.
- **Look for deposits as well as corrosion.** The Chevron statement implies that hot enamel surfaces can collect lacquer-type deposits as well as corroding at defects. Imaging should therefore separate deposit build-up from discoloration of the enamel itself, for example by microscopy plus FTIR or EDS.
- **Passivator level matters for wrapped copper.** The transformer BTA dose-response suggests this, so the e-fluid's inhibitor content, if known, should be recorded.

### Gaps
- **No data on the specific hairpin weak points:** nothing on corrosion starting at enamel pinholes or defects, at the 1–2 µm insulation residue left by laser stripping, or in weld heat-affected zones, in e-fluids or ATF, in 2025–2026.
- **Coated copper under electric field: metadata only.** A 2026 study of epoxy coatings on copper under combined high electric field and corrosion could not be read, though it may bear on under-coating corrosion with bias: [Yang J.-G. et al., "Degradation and failure mechanism of epoxy coatings for copper packaging under the synergistic effect of high electric field and corrosion", Colloids Surf. A, Dec 2026, DOI 10.1016/j.colsurfa.2026.141567](https://doi.org/10.1016/j.colsurfa.2026.141567)
- **Weld-zone protection has no oil-exposure data:** vendor information lists powder coating, gel coating, potting and dipping. The source is undated and was seen only as a search summary ([bdtronic stator coating page](https://www.bdtronic.com/en-en/impregnation-applications/stator-coating/)).
- **Pre-window cut-end test:** the 2021 Scania case (see Q2 Gaps) tested "cutouts of the hairpin wires … polished on the ends" at 125 °C in closed and open cups. This is the closest cut-end precedent, but it is outside the window.

## Q4. Are there new quantitative imaging and surface-characterisation protocols (colour-calibrated photography, ΔE00, microscopy, SEM/EDS, XPS, Raman, cross-sections, 3D profilometry) applied to copper or insulation surfaces?

### Takeaway
Instrumental colour rating of copper advanced in two ways in the window:
- **ASTM WK99361** proposes an optional calibrated digital-imaging step for D130, with controlled lighting and RGB/hue/saturation/intensity parameters. It is a work item, not yet a standard.
- **The 2026 Fuels study** (Vlčková et al.; full text now read) is the only peer-reviewed copper colorimetry protocol found:
  - D65 colorimeter, CIELAB ΔE*ab (CIE76) against an unexposed polished reference strip, two spots per strip;
  - ΔE*ab of 0.44–11.06 separated strips that were all visually Class 1.

Other findings:
- No 2025–2026 source applied ΔE00 or colour-chart-calibrated photography to copper or insulation aged in oil.
- Infineum added video imaging of deposit and dendrite growth in its energised test, but gave no protocol.
- Afton's patent data show that D130 tarnish classes track copper loss only loosely (2B at both 64 and 144 ppm leached). Colour should therefore be paired with ICP, mass or resistance.
- No new 2025–2026 papers were found applying XPS, Raman, metallographic cross-sections or 3D profilometry to copper aged in e-fluids.
- New imaging items beyond that are peripheral: SEM/EDS plus X-ray imaging in an EV connector study (not oil), FTIR on PAI aged in ATF, and structured-light 3D metrology of hairpin shape.

### Cited Findings
- **ASTM WK99361 (D130 revision):**
  - Rationale: the current rating "relies only on visual comparison" and is subjective, owing to observer colour perception, lab lighting and borderline strips.
  - Proposal: after the visual exam, an extended rating with "a calibrated imaging system under controlled lighting", measuring RGB, hue, saturation and intensity, plus an expanded digital adjunct of example images.
  - WK95661 would allow machine vision as an alternative to manual rating.
  - Search summary only; the pages returned HTTP 403.

  [STD] — [ASTM WK99361](https://www.astm.org/membership-participation/technical-committees/workitems/workitem-wk99361); [ASTM WK95661](https://store.astm.org/workitem-wk95661)
- **Vlčková et al. 2026, full protocol. Already in the review as abstract only; the full text is now read, and the details below are new to the review.**
  - Test: copper strips per EN ISO 2160 with modified surface preparation.
  - Instrument: 3nh NR200 colorimeter under D65.
  - Output: CIE L*a*b*, C* and h, with ΔL*, Δa*, Δb*, ΔC*, ΔH*. ΔE*ab was computed by the CIE76 formula against "a single polished copper strip … not exposed to fuel".
  - Sampling: two measurements "on visually homogeneous areas" per strip, averaged. One strip per fuel, each fuel tested once.
  - Photography: photos were taken "under as similar lighting conditions as possible". Uniform exposure adjustments were made in Zoner Photo Studio X, with "no selective image enhancement or color correction". No colour chart is reported.
  - Reference strip: L* 86.94, a* 18.59, b* 15.67.
  - Mean ΔE*ab: G1 1.51, G2 3.03, G3 0.44, G4 (aged gasoline) 11.06, D1 1.95, D2 3.0, D3 8.73, D4 3.6. The abstract attributes the highest values to aged fuels.
  - All strips were visual Class 1 (mostly 1a; G4 approached 1b).

  [PEER, full text] — [Vlčková L., Šeděnka D., Pravda Š., Helebrant F., Kudrna L., Blata J., "Colorimetric Assessment as a Complementary Approach to Visual Copper Corrosion Evaluation in Automotive Fuels", Fuels 7(3):42, 29 June 2026, DOI 10.3390/fuels7030042 (PDF)](https://mdpi-res.com/d_attachment/fuels/fuels-07-00042/article_deploy/fuels-07-00042.pdf)
- **Visual tarnish class against measured copper loss (Afton, D130 at 150 °C/168 h):**
  - 2B covered 64, 117 and 144 ppm Cu leached;
  - 2A covered 43 and 61 ppm;
  - 3A was 121 ppm;
  - 4A covered 206–347 ppm.

  [PATENT] — [US 12,662,647 B2](https://patents.google.com/patent/US12662647B2/en)
- **Video imaging of dendrite growth:** a "novel video imaging system" records "deposit / dendrite growth between anode and cathode" during the energised corrosion test. No camera, magnification or lighting details are given [VENDOR] — [Infineum, CTI Symposia 2025](https://cti-symposium.world/leading-the-way-in-e-fluid-developments/)
- **CDT board photographs:** these document "dendrite growth" that caused a short [VENDOR] — [Savant Labs EV page](https://www.savantlab.com/testing-highlights/electric-vehicle-lubricant-and-fluid-testing/)
- **Non-imaging corrosion metric with nm resolution:** in the WCT apparatus, resistance change is converted to wire-radius loss and plotted in nm against time [PATENT] — [US 12,092,562 B2](https://patents.google.com/patent/US12092562B2/en)
- **Deposit analysis (Shell):** "Solid analysis on corroded deposits" was used to identify the species involved; the techniques are not stated [CONF, abstract only] — [Vo et al., STLE 2025](https://www.stle.org/images/PDF/STLE_ORG/AM/2025/Program/STLE2025_Preliminary_Program_12.20.24.pdf)
- **FTIR on PAI aged in ATF:** FTIR tracked chemical change (C–H and P–O bonds) in PAI aged in ATF with and without water [CONF, abstract only] — [Li et al., CEIDP 2025](https://doi.org/10.1109/CEIDP61707.2025.11218487)
- **Multi-modal documentation of an EV corrosion failure (not oil):** X-ray images of cables to locate material interfaces and coatings, then SEM/EDS of the corroded Sn-Cu/Al interface [PEER, full text] — [Shin et al., CST 2025](https://www.j-cst.org/data/issue/CST/C002404/C00240400203.pdf)
- **3D metrology of hairpins (geometry, not corrosion):** a "noncontact structured light sensor array system", with "a robust calibration technique", for rapid in-process measurement of the full 3D hairpin wire-form shape [PEER, abstract only] — [Wagner S., "Rapid In-Process 3D Shape Inspection of Magnet Wire Hairpins During Electric Motor Assembly", Materials Evaluation, Jan 2026, DOI 10.32548/2026.me-04552](https://doi.org/10.32548/2026.me-04552)

### Inferences
- **Instrumental colour rating is gaining acceptance.** WK99361 and the 2026 colorimetry paper support recording calibrated colour data rather than visual classes alone.
  - WK99361's RGB, hue, saturation and intensity values depend on the device unless the camera is calibrated.
  - For academic comparability, a better choice is CIELAB with ΔE00, as recommended in ASTM D2244 (in the review), reporting the components ΔL*, Δa* and Δb*.
- **The 2026 protocol can be improved on in four ways:**
  1. use the same specimen region before and after ageing as the reference, instead of a separate polished strip;
  2. put a colour/grey target in every frame, use fixed D65-like diffuse illumination and fixed geometry, and capture RAW images;
  3. replicate across specimens and measurement spots, and report variability;
  4. report ΔE00 alongside ΔE*ab.
- **Colour alone does not measure corrosion.** Tarnish class tracks copper loss poorly (Afton data), so colour metrics should be paired with a quantitative corrosion measure: ICP of copper in the oil, mass change, or a thin-wire witness (WCT-style radius loss).
- **Witness wires are needed for resistance-based measurement.** A hairpin's own resistance is far too insensitive to surface attack, because its cross-section is large.
- **Colour cannot separate deposits from oxidation on insulation.** ΔE on insulation surfaces quantifies discoloration but cannot tell deposit build-up (e.g., EP-derived lacquer) from polymer oxidation. Microscopy, plus FTIR or EDS on the same regions, is needed. Structured-light or other 3D metrology could document swelling or dimensional change of insulated hairpins, but no corrosion-focused 3D study was found.

### Gaps
- **ASTM work items unverified:** the WK99361 and WK95661 pages were blocked, so their dates, status and full technical content are not verified.
- **No ΔE00 or colour-chart calibration on oil-aged surfaces:** no 2025–2026 source applied ΔE00 or colour-chart-calibrated photography to copper or insulation aged in oil or ATF. The only new copper colorimetry study (2026) is in fuels and uses ΔE*ab (CIE76).
- **No new surface-analysis studies on e-fluid copper:**
  - no 2025–2026 XPS, Raman, metallographic cross-section, confocal or 3D-profilometry study of copper aged in e-fluids or ATF;
  - no published details of Infineum's video imaging (optics, frame rate, quantification);
  - the deposit-analysis techniques in Shell's 2025 talk are not public.
- **Raman for oil–paper ageing (title only):** a 2026 Energies paper on "Aging Evaluation Method of Oil-Paper Insulation Based on Raman Spectrum and Frequency-Domain Spectroscopy" was found only as a title. It is about oil–paper, not copper ([DOI 10.3390/en19092139](https://doi.org/10.3390/en19092139)).
- **No machine-vision colour indices for oil-paper:** a search on colour or machine-vision indices for oil–paper insulation ageing found only pre-2025 RGB-based work.
