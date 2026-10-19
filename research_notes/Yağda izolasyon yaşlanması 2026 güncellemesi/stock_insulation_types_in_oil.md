# Stock insulation types (a)–(d) in oil: polyimide-tape-wrapped, glass-fibre-covered and film-plus-glass rectangular copper wire

Tag legend used in every bullet:
- Evidence class: **[PEER/GOV]** = peer-reviewed paper or government technical report; **[MFR]** = manufacturer or vendor datasheet/claim; **[PAT]** = patent data; **[STD]** = standard text or standards-catalogue page; **[IND]** = industry or test-lab article.
- Reading status: **{full text}** = I read the document text; **{abstract/record}** = only the abstract or catalogue record; **{search excerpt}** = only the search engine's excerpt/summary of the page (the page itself could not be opened or was not opened); **{patent page}** = the Google Patents page text (for JP documents, its machine translation).

Sources already in the existing review (`Hairpin insulation oil aging and corrosion review.md`, References from line 485) are marked "(already in review)". The review already uses the Kapton summary of properties only for moisture absorption and NaOH retention. It also states that no Kapton-tape data in ATF exist. This search did not change that.

## 1. How do polyimide films and tapes behave in hot oils and in the presence of water (hydrolysis, adhesive/bonding layer, delamination, swelling, breakdown-voltage retention)?

### Takeaway
DuPont says polyimide (Kapton HN-type) resists hydrocarbons, lubricants, resins and varnishes. Because it is a condensation polymer, however, hot water, steam and alkalis degrade it. Damage speeds up with temperature, water activity and mechanical strain, and shows as embrittlement and radial cracking. Magnet-wire tapes are normally heat-sealed with FEP (Kapton FN/FCRC/FWN/FWR types), which lowers moisture uptake and permeation. Oil-filled ESP-motor patents still report delamination at high temperature, a weakened adhesive and fast degradation once water enters. No public quantitative aging data were found for polyimide-tape-wrapped wire in transformer oil, ATF or e-fluid: no BDV retention, swelling or mass change, under either dry or wet conditions.

### Cited Findings

#### Manufacturer data (DuPont)
- The DuPont Kapton *Motor and Magnet Wire Technical Bulletin* (H-29423-4, 11/2014) says the heat-sealable films are the primary insulation on magnet wire. They are "coated with or laminated to a fluoropolymer which acts as a high temperature adhesive". The tape is "helically wrapp[ed] … and heat-seal[ed] to the conductor and itself". Heat-sealable designations are FN, FCRC, FWN, FWR, PRN, PRT and XP. [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)
- Constructions from the same bulletin (Table 1):
  - 150FN019 = 25 µm HN + 12.7 µm fluoropolymer on one side.
  - 200FN919 = 12.7 + 25 + 12.7 µm.
  - 250FN029 = 50 + 12.7 µm.
  - 300FN929 = 12.7 + 50 + 12.7 µm.
  - 150FCRC019 = 25 µm corona-resistant CRC + 12.7 µm.
  - 150FWR019 = 25 µm water-resistant WR + 12.7 µm; 200FWR919 = 12.7 + 25 µm WR + 12.7 µm.
  - Nominal total thicknesses (Table 2): 33 µm (120FWN616B), 38.1 µm (all "150" types), 50.8 µm ("200" types), 63.5 µm (250FN029) and 76.2 µm (300FN929).
  
  [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)
- Hydrolysis statement in the same bulletin: "Continuous exposure to hot water can affect the tensile strength, elongation, and dielectric strength of standard Kapton® HN." Kapton WR "has been developed specifically to combat the effect of water on insulation systems and for applications where hydrolytic stability is important" (standard thickness 25 µm). The bulletin gives no numbers for this. [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)
- Chemical-resistance claim in the same bulletin: "Kapton® has superior chemical resistance to most solvents, hydrocarbons, lubricants, resins, and varnishes." The bulletin gives no oil-immersion data. [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)
- Specification minimums in the same bulletin:
  - Unsealed film: 100HN tensile ≥ 179 MPa, elongation ≥ 55 % and dielectric strength ≥ 6200 V/mil (244 kV/mm). 200HN ≥ 5000 V/mil (197 kV/mm). 100CRC ≥ 6000 V/mil (236 kV/mm).
  - Heat-sealable films: minimum MD elongation 45–65 % and minimum dielectric strength 3100–5300 V/mil, depending on construction (ASTM D882/D149).
  - Minimum heat-seal peel strength: 750–800 g/in (18.7–19.9 N/cm) FEP-to-FEP and 500–750 g/in (12.5–18.7 N/cm) FEP-to-Kapton (ASTM D5213).
  - The text-extracted table columns do not map unambiguously to the grades, so only ranges are reported here.
  
  [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)
- UL thermal index of Kapton film under file E39505: 220–240 °C for electrical properties and 200–220 °C for mechanical properties. The plant thermal-durability check requires ≥ 10 % elongation after 2 h at 400 °C. [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)
- From the DuPont Kapton *Summary of Properties*, "Hydrolytic Stability" section (already in review):
  - "Kapton® polyimide film is made by a condensation reaction; therefore, its properties are affected by water."
  - Long-term exposure to boiling water "will reduce the level of film properties", but "sufficient tensile and elongation remain to ensure good mechanical performance".
  - "A decrease in the temperature and the water content will reduce the rate … whereas higher temperature and pressure will increase it."
  - Figures 3–4 plot HN tensile strength and elongation over about 2,600 h in 100 °C water. The curve values could not be extracted from the PDF text.
  
  [MFR] {full text, figures not digitised} — [DuPont Kapton summary of properties](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-summary-of-properties.pdf)
- From the same document: Type FN (HN coated on one or both sides with Teflon FEP) "imparts heat sealability, provides a moisture barrier, and enhances chemical resistance". Table 11 data:

  | Film | Moisture absorption, 50 % RH | Moisture absorption, 98 % RH | Water-vapour permeability |
  |---|---|---|---|
  | 120FN616 | 1.3 % | 2.5 % | 17.5 g/(m²·24 h) |
  | 150FN019 | 0.8 % | 1.7 % | 9.6 g/(m²·24 h) |
  | 400FN022 | 0.4 % | 1.2 % | 2.4 g/(m²·24 h) |
  | 25 µm HN (for comparison) | 1.8 % | 2.8 % (24 h immersion) | 54 g/(m²·24 h) |

  The document also says loss-of-coolant tests expose Kapton to "steam and sodium hydroxide, both of which tend to degrade Kapton®". [MFR] {full text} — [DuPont Kapton summary of properties](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-summary-of-properties.pdf)
- DuPont statements on Kapton FWR:
  - FWR offers "significantly improved hydrolysis resistance compared to other commonly used polyimide materials".
  - FWR has "a higher modulus and lower water vapor permeability than equivalent Kapton® FN films".
  - No numbers were visible, and the product page returned HTTP 404 when fetched.
  
  [MFR] {search excerpt} — [DuPont Kapton 150FWR019 page](https://www.pp.dupont.com/products/kapton-150fwr019.html)

#### Peer-reviewed / government reports
- Campbell (Naval Research Laboratory), "Problems with Aging Wiring in Naval Aircraft", 1994:
  - The Navy had "a severe aircraft electrical wiring maintenance problem" because aromatic polyimide insulation was "deteriorating at a rate that was unexpected".
  - Accelerated aging came from "moisture, temperature, and strain".
  - MIL-W-81381 insulation aged at high humidity "followed the classical Arrhenius thermal aging relationship". A multifactor life-prediction formula and an automated remaining-life tester were developed.
  - The PDF is a scanned image, and text extraction failed.
  
  [PEER/GOV] {abstract/record} — [NASA NTRS 19950009633](https://ntrs.nasa.gov/citations/19950009633)
- Related work already in the review, not repeated here: hydrothermal aging of a polyimide film ([Braun et al. 2022](https://ualberta.scholaris.ca/handle/123456789/17234)); and neat ethanolamine degrading Kapton within 3 h at 120 °C ([Chen et al. 2025, Adv. Sci.](https://pmc.ncbi.nlm.nih.gov/articles/PMC11967771/)). The second is relevant because many ATFs/e-fluids contain amine-type additives. [PEER/GOV] (already in review)

#### Industry / test-lab
- Lectromec, "forced hydrolysis" testing of aerospace polyimide-film wire:
  - Method: mandrel-wrapped samples (about 0.5 in mandrel for 20 AWG) are immersed in saline at 70 °C "for thousands of hours". Sample ends are kept above the water line "to prevent fluid from wicking between conductor and insulation". Pass/fail is a post-exposure voltage withstand test.
  - The test is part of qualification only for constructions containing polyimide film (AS22759/80–92 and /180–192).
  - "H-film" wire of the 1970s to early 1990s "degraded rapidly" under heat, humidity and mechanical stress, with radial insulation cracks.
  - ETFE and PTFE "are unlikely to degrade under these conditions".
  
  [IND] {full text} — [Lectromec: forced hydrolysis](https://lectromec.com/forced-hydrolysis/)

#### Patent data (oil-filled ESP motors and related)
- US 10,672,532 B2 (Halliburton, assigned from Summit ESP; priority 2012-04-20; granted 2020-06-02), on polyimide tape-wrapped magnet wire in ESP motors:
  - Polyimide tape "is hydroscopic (it readily takes on water) and degrades in the presence of water". Kapton "readily takes on water … and then degrades rapidly".
  - The tape "may delaminate at extremely high temperatures, such as above 300 degrees Fahrenheit" (≈149 °C). "The adhesive used to attach Kapton® tape to the wire may also delaminate at the extreme high temperatures of deep wells."
  - "excessive vibration may also weaken the adhesive". A loose tape can "cause a direct short".
  - Moisture held in the tape "boils out and may cause [the PEEK] layer to blister or swell".
  - The proposed fix: dry the wrap at 300 °F under partial vacuum, then extrude molten PEEK over it.
  - Motor oil flows "through the empty space in the open slots around the enhanced magnet wire" (claim 8).
  - No test data are given.
  
  [PAT] {patent page} — [US 10,672,532 B2](https://patents.google.com/patent/US10672532)
- Same family, US 9,800,110 B2: the same "hydroscopic … degrades rapidly" background, and polyimide tape combined with a thermoplastic layer "that prevents the delaminating at high temperatures". [PAT] {search excerpt} — [US 9,800,110 B2](https://patents.google.com/patent/US9800110)
- US 9,634,535 ("Equipment including epitaxial co-crystallized material"; assignee not verified):
  - It relates hydrolysis resistance of polyimide wraps to tape overlap ("greater than 50% overlap").
  - It describes coating the polyimide film "on one or both sides with PFP … to protect polyimide in the film from hydrolysis".
  
  [PAT] {search excerpt} — [US 9,634,535](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9634535)
- Baker Hughes ESP patent family: at high temperature, the epoxy bonding magnet wires in the slots generates acids that attack the insulation. An "enhanced oil" (PAO-based) with a basic buffering additive is proposed. Which family member contains the quoted passage was not verified. [PAT] {search excerpt} — [US 8,704,416 (Justia)](https://patents.justia.com/patent/8704416); [US 2012/0063933 A1](https://patents.justia.com/patent/20120063933); [US 2012/0063934 A1](https://patents.justia.com/patent/20120063934)

### Inferences
- **Water is the main threat.** The study's wet-oil arm (water-spiked fluid) is the one most likely to separate type (a) from enamel. Dry oil at 120–150 °C alone is unlikely to hurt the polyimide film quickly, because DuPont claims resistance to hydrocarbons and lubricants and no source reported oil-only attack. Hydrolysis needs water, and its rate rises with temperature, water content and pressure (DuPont, Campbell).
- **Watch the tape construction, not just the film.** The weak points reported in service are adhesive and interlayer delamination, tape loosening, blistering from trapped moisture, and liquid wicking along the conductor–tape interface (ESP patents; Lectromec). For an unknown stock tape, the adhesive type (FEP heat-seal versus a pressure-sensitive silicone or acrylic adhesive) should be identified before aging (FTIR on a peeled layer). IEC 60317-44 assumes FEP-type heat-sealed adhesive, so a pressure-sensitive-adhesive tape would fall outside that standard (see Q5).
- **Bends matter.** Strain speeds polyimide hydrolysis (Campbell; Lectromec's mandrel-wrapped method). Bent or U-shaped specimens in the wet arm are therefore more discriminating than straight ones. Radial cracks at the outer bend radius, edge lifting at overlaps, and blistering are the defects to photograph.
- **Amine additives.** E-fluids with amine-containing additives add a possible aminolysis route (Chen et al. 2025, neat amine). No study at ATF additive concentrations exists, so this remains a hypothesis to test, for example by FTIR of the imide C=O bands at about 1775/1720 cm⁻¹ before and after aging. The band positions are general spectroscopy knowledge, not from the sources above.
- **Expected size of the effect.** FN tapes absorb less water (0.8 % versus 1.8 % for HN at 50 % RH) and transmit about 5× less water vapour. A well-sealed FEP-bonded wrap should therefore lose dielectric strength more slowly in wet oil than bare polyimide or enamel. Overlap edges and cut ends stay the entry points.

### Gaps
- No public quantitative data (BDV retention, PD, mass or dimension change, peel strength) were found for polyimide-tape-wrapped wire or Kapton film after immersion in transformer oil, ATF, e-fluid, PAO or POE, either dry or wet. ESP-motor sources are patents only, with no test data.
- DuPont's boiling-water curves (Summary of Properties, Figs. 3–4) were not digitised. The FWR datasheet could not be opened (HTTP 404).
- No data were found on silicone-, acrylic- or polyimide-adhesive Kapton tapes in hot oil. Their swelling or softening in hydrocarbon oils is untested in the public record found.
- The classic hydrolysis study De Iasi & Russell (J. Appl. Polym. Sci., about 1971–72; DOI given in Sroog's review as 10.1002/app.1972.070161116) was not accessed. Its existence and year are only known from a search excerpt.
- Navy and NASA reports on the fluid-immersion resistance of polyimide wire (e.g., DTIC ADA149055) were blocked (HTTP 403).

## 2. How do glass-fibre-covered wires and their varnish binders behave in oils, and how do PET or other films combined with glass behave in hot oil with water?

### Takeaway
IEC defines a transformer-oil resistance clause for glass-fibre-wound rectangular wire (IEC 60317-0-4, and parts 31 and 33 for TI 180/200). However, no public quantitative data were found on oil uptake, wicking, binder softening or BDV/PD change for glass-covered wire in any oil, including ATF. The binder chemistry decides the risk:
- polyester, polyesterimide and epoxy contain hydrolysable ester groups (the review already documents hydrolysis of impregnating resins in wet ATF);
- silicone has a TI of 200.

If the "foil" in type (d) is PET, DuPont data show PET embrittles by hydrolysis once more than about 0.1 % water is present at elevated temperature. Its recommended maximum service temperature is 150 °C. Refrigerant-compressor experience also shows oligomer extraction by ester oils.

### Cited Findings

#### Standards
- IEC 60317-0-4 (general requirements for glass-fibre-wound, resin- or varnish-impregnated, bare or enamelled rectangular copper wire; ed. 2.2 = 1997+A1:1999+A2:2005, and ed. 4.0, 2020): its table of contents lists a clause "Resistance to transformer oil". IEC 60317-31 (TI 180) and IEC 60317-33 (TI 200) also list one. The requirement and method were not visible. [STD] {search excerpt} — [IEC 60317-0-4 ed. 2.2 preview](https://webstore.iec.ch/p-preview/info_iec60317-0-4%7Bed2.2%7Db.pdf); [IEC 60317-31 preview](https://webstore.iec.ch/p-preview/info_iec60317-31%7Bed1.1%7Db.pdf); [IEC 60317-33 preview](https://webstore.iec.ch/p-preview/info_iec60317-33%7Bed1.1%7Db.pdf)
- IEC 60851-4:2016, Test 20 "Resistance to hydrolysis and to transformer oil", says: "This test is applicable to enamelled wire." (the source is already in the review; the review used only the 24 h hydrolysis part). For rectangular wire, the oil-resistance arm works as follows:
  - **Vessel and charge:** a pressure vessel holds 4 U-shaped and 2 mandrel-bent specimens. It is charged with transformer oil (65 ± 5 % of vessel volume), paper (4 ± 1 %), coating (0.275 ± 0.075 %) and steel (by agreement). Oil and paper are dried at ≤ 2 kPa for 16 h at 90 °C or 4 h at 105 °C.
  - **Exposure:** the vessel is held at the wire's class temperature, or at 150 ± 3 °C if the class is above 150 °C, for 1000 ± 10 h.
  - **Breakdown voltage:** measured at 105 °C in air on two U-specimens as removed and two after drying at 125 °C for 30 min.
  - **Cracks:** the mandrel-bent specimens are examined for cracks.
  - **Hydrolysis arm:** two sealed tubes, each with 5 straight pieces in 80 mL dry oil. One tube gets 0.24 mL water. Both are held 24 h at 150 °C.
  - **Drying note:** the test notes that water acts "by hydrolytic degradation and/or by absorption". Only absorption is recovered by the 125 °C / 30 min drying.
  
  [STD] {full text} — [IEC 60851-4:2016 copy](https://www.normsplash.com/FreeDownload/143987489/IEC-60851-4-2016-en-fr.pdf)
- IS 13730 (Part 39), the Indian adoption of IEC 60317-39 (1992), covers glass-fibre-braided, polyester- or polyesterimide-varnish-treated, bare or enamelled rectangular copper wire with TI 180. The varnish itself must have a minimum TI of 180. [STD] {search excerpt} — [BIS SR13730-39](https://services.bis.gov.in/tmp/SR13730_39.pdf)

#### Manufacturer data
- DuPont Teijin Films, *Mylar® polyester film – Physical-Thermal Properties* (H-37232-3, 06/2003):
  - "Mylar® polyester film will hydrolyze and become brittle under conditions of high temperature and humidity" (steam at 100 °C, Figs. 7–9, to 750 h). "care should be taken to ensure that there is a minimum of water in any hermetically sealed unit."
  - Drying 4 h at 160 °C "should reduce the water content of the film to less than 0.1%; more than this amount of water must be present in a system before the film can become embrittled due to hydrolysis".
  - Maximum recommended service temperature is 150 °C. Processing should stay below 200 °C. At 220 °C for 30 min the film loses about 10 % tensile strength, and it "becomes brittle and shatters" after under 1 min at 235 °C.
  - Service life (time to 10 % elongation) falls with water partial pressure and film temperature (curves for 85, 100 and 140 °C).
  
  [MFR] {full text, figures not digitised} — [DuPont Teijin Films H-37232-3](https://people.physics.carleton.ca/~msd/tpc_archival_reports/results_2004/docs/mylar.pdf)
- Rea Magnet Wire's Daglas (polyester-glass) served wire is offered unvarnished, epoxy-varnished, high-temperature polyester-varnished or silicone-varnished, with thermal classes of 155, 180 and 200 °C respectively (see Q5 for the NEMA mapping). The search tool reported that the datasheet text was partly garbled. [MFR] {search excerpt} — [Rea data sheet index](https://www.reawire.com/?p=110); [EIS listing, Rea Daglas SSDDG](https://www.eis-inc.com/product/magnet-wire-ph15-ssddg)
- Melinex 238 is marketed as a low-oligomer, hydrolysis-stable PET for hermetic motors. This is a vendor claim with no numbers seen. [MFR] {search excerpt} — [Knowde: Melinex 238](https://knowde.com/stores/dr-d-mueller/products/melinex-238-fi-13020)

#### Peer-reviewed / industry
- Lubrizol, "Polymer compatibility with refrigeration lubricants" (Industrial Lubrication and Tribology, 1999): even dry polyol-ester lubricants extract oligomers from PET and PBT, and the deposits can affect compressor reliability. [PEER/GOV] {search excerpt} — [Emerald, DOI 10.1108/ilt.1999.01851bab.009](https://www.emerald.com/ilt/article/doi/10.1108/ilt.1999.01851bab.009/170569/Polymer-compatibility-with-refrigeration)
- Already in the review: hydrolysis of impregnating resins in wet ATF, with the OH band growing and the ester C=O band at 1735 cm⁻¹ falling after 2000 h in Dexron ULV + 0.5 % water ([Wei Xiongqiang et al. 2022](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2022.07.008)). This is the closest available evidence on how varnish binders behave in ATF. [PEER/GOV] (already in review)

#### Patent data
- US 4,590,025 (impregnation of thread-covered and braided conductors): "The wetting ability of glass fiber and its capacity to absorb impregnating agents are poor". Impregnation that fills the gaps between fibres improves dielectric properties. [PAT] {search excerpt} — [US 4,590,025](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4590025)
- PET in refrigerant/oil systems:
  - Water in refrigerant oils degrades PET film, and synthetic lubricants extract low-molecular-weight material that forms sludge and embrittles the film ([US 5,939,200](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5939200); [EP 0 767 197 A1](https://data.epo.org/publication-server/rest/v1.2/patents/EP0767197NWA1/document.html)).
  - Time to embrittlement depends on temperature and moisture level ([US 6,020,056](https://patents.justia.com/patent/6020056)).
  - PET with Tg ≥ 65 °C, PAI-coated polyester, PPS and PEEK were reported suitable in sealed tubes with R134a and ester oil ([US 6,258,293](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6258293)).
  - PCT film was proposed for better hydrolysis resistance ([EP 0 484 942 A2](https://data.epo.org/publication-server/rest/v1.2/patents/EP0484942NWA2/document.html)).
  - Low-oligomer PET and PEN reduce extraction ([US 9,422,930](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9422930)).
  
  [PAT] {search excerpts}
- JP H07-335033 A (Showa Electric Wire & Cable/SWCC; filed 1994-06-08), "insulated wire for oil-immersed transformers":
  - Flat conductor wrapped with polymethylpentene tape.
  - It states that polypropylene has poor oil resistance and swells in mineral transformer oil, and that radial swelling can block oil ducts.
  - It lists PPS, PTFE, FEP, PFA and PET as candidate films (dielectric constant ≤ 3, continuous service ≥ 140 °C).
  - It gives no test data.
  
  [PAT] {patent page, machine translation} — [JP H07-335033 A](https://patents.google.com/patent/JPH07335033A/ja)

### Inferences
- **Varnish binder:** for types (b), (c) and (d), the binder (and any enamel underlayer) is the most oil- and water-sensitive part. Glass fibre itself is inorganic. If the binder is polyester, polyesterimide or epoxy, wet ATF can be expected to hydrolyse it, by analogy with Wei Xiongqiang et al. 2022. Expect fibre "blooming", loss of fibre-to-fibre bonding and fraying at bends. A silicone binder (TI 200 grades) can be expected to swell in hydrocarbon oils rather than hydrolyse. That is an inference from general polymer behaviour, not from a source here.
- **Wicking:** glass wets poorly (US 4,590,025). Under-impregnated glass coverings can therefore leave porous paths along which oil and water wick between the conductor and the covering, as Lectromec notes for wrapped constructions. Specimen ends should be sealed, or kept above the fluid, unless wicking is itself the variable under study.
- **Identifying the type (d) "foil":** the DuPont data give a cheap discriminator. PET "becomes brittle and shatters" after under 1 min at 235 °C. Kapton passes 2 h at 400 °C with ≥ 10 % elongation. A short hot-plate or oven exposure of a stripped film piece (or FTIR) should identify PET versus PI before aging. If the film is PET, keep the wet-arm temperature at or below 150 °C (DuPont's maximum service temperature). Expect embrittlement once water in the system exceeds the low threshold stated by DuPont.
- **Test protocol:** IEC 60851-4 Test 20 is written for enamelled wire, and its oil-resistance arm caps at 150 °C for 1000 h. A study of glass-covered or tape-wrapped wire can adopt the same vessel and BDV-after-redrying logic, but should report this as a documented deviation.

### Gaps
- No quantitative data were found on oil uptake, mass change, wicking, binder softening, BDV, PD or mechanical integrity of glass-fibre-covered winding wire (served or braided; polyester, polyesterimide, epoxy or silicone binder) in transformer oil, ATF or e-fluid.
- The contents of the "resistance to transformer oil" clause in IEC 60317-0-4/-31/-33 (method, temperature, acceptance limits) could not be read. The previews were reachable only through search excerpts, and direct downloads returned HTML.
- No public data were found on PET-film-plus-glass or PI-film-plus-glass composite wires in any oil.
- Doerr & Waite (1996, DOE/CE/23810-63, Trane/ARTI), on motor materials under refrigerant-retrofit conditions, may contain sheet-insulation (PET and others) and sleeving results. The AHRI-hosted PDFs returned HTTP 403, so it remains a lead only: [Doerr & Waite 1996 V2 (AHRI)](https://www.ahrinet.org/system/files/2023-06/Compatibility%20of%20Refrigerants%20and%20Lubricants%20with%20Motor%20Materials%20under%20Retrofit%20Conditions-Doerr%20and%20Waite-1996-DOE-CE-23810-63-V2.pdf).

## 3. Are these insulation types used in oil-cooled or oil-immersed traction machines, or in oil-filled transformers and reactors, and what field experience or qualification data exist?

### Takeaway
The clearest oil-immersed use of polyimide-tape-wrapped magnet wire is in oil-filled downhole electric submersible pump (ESP) motors. The public record of field problems there is patent background text:
- water ingress leads to degradation;
- the tape delaminates at high temperature;
- the adhesive weakens.

No published quantitative field or qualification data were found. No public evidence was found that polyimide-tape-wrapped or glass-covered rectangular wire is used in direct oil-cooled traction motors (rail, off-highway, EV, hybrid). For oil-filled transformers, IEC positions paper-covered rectangular wire, not glass or polyimide types, as the wire "primarily intended" for oil-immersed windings.

### Cited Findings
- **ESP motors (oil-filled):**
  - Polyimide (Kapton) tape is the established magnet-wire insulation, and motor oil fills the open slots around the wire.
  - Pump leaks let water into the motor, and cracked insulation causes "premature failure".
  - Motor temperatures in high-temperature wells "may reach in excess of 550° F" (≈ 288 °C).
  
  [PAT] {patent page} — [US 10,672,532 B2](https://patents.google.com/patent/US10672532); {search excerpt} [US 9,800,110 B2](https://patents.google.com/patent/US9800110)
- GE's ESP patent describes the motor as "a hermetically sealed casing containing an oil-filled space". It states that "the prior art winding insulation used in ESP motors has a temperature index less than 250° C". [PAT] {patent page} — [US 2012/0080970 A1](https://patents.google.com/patent/US20120080970A1/en)
- A Chevron paper at the Southwestern Petroleum Short Course describes free water collecting at the bottom of submersible motors. Insulation-resistance monitoring methods "do not provide an indication until the insulation system has already been affected". [IND] {search excerpt; year not seen} — [SWPSC: water detection systems for use with ESP motors](https://www.swpshortcourse.org/paper/water-detection-systems-use-esp-motors)
- **Transformers:**
  - Paper-tape-covered rectangular copper wire (IEC 60317-27 series) "is primarily intended for winding coils for oil immersed transformers". No equivalent statement was found for the glass-fibre or polyimide-tape parts. [STD] {search excerpt} — [BSI: IEC 60317-27-x paper tape covered rectangular wire](https://knowledge.bsigroup.com/products/specifications-for-particular-types-of-winding-wires-paper-tape-covered-rectangular-copper-wire-2)
  - IEEE C57.154-2022 covers liquid-immersed transformers "designed to operate at temperatures above conventional limits using high-temperature insulation systems" and supersedes C57.154-2012. The material tables (e.g., whether polyimide film or glass are listed, and at what temperatures) were not accessible. [STD] {search excerpt} — [IEEE C57.154-2022](https://standards.ieee.org/ieee/C57.154/7418/)
  - The SWCC patent shows that plastic-film-wrapped transformer wire has to be designed for swelling in mineral oil (see Q2). [PAT] {patent page} — [JP H07-335033 A](https://patents.google.com/patent/JPH07335033A/ja)
- **Aerospace:** oil-spray-cooled aircraft generators are an established oil-wetted-winding design. One of the patents states that low-velocity atomised oil impinging on the insulated windings "minimizes, if not eliminates, insulation erosion"; which one was not verified. No insulation-type or oil-compatibility data were found. [PAT] {search excerpts} — [US 8,884,479 B2](https://patents.google.com/patent/US8884479); [US 7,786,630 B2](https://patents.google.com/patent/US7786630); [US 3,648,085 A](https://patents.google.com/patent/US3648085A/en)

### Inferences
- **ESP lessons:** in oil-filled motors, the oil was not reported as the polyimide wrap's problem. Water ingress, high-temperature delamination and vibration-loosened adhesive were. Polyimide-wrapped hairpins in e-fluid are likely to fail by the same mechanisms if water accumulates (condensation, coolant leaks).
- **Glass coverings in EV machines:** glass-fibre coverings at 0.30–0.50 mm build are thick for compact hairpin EV machines (versus 0.10–0.20 mm enamel). That probably explains why no EV/hybrid use was found. In the study they serve better as a contrast class than as a candidate hairpin insulation. This is an inference; no source discusses it.

### Gaps
- No rail, off-highway, EV or hybrid-transmission source was found that documents polyimide-tape-wrapped, glass-covered or film-plus-glass windings in direct oil cooling, with or without field data.
- No CIGRE or IEEE TDEI paper was found on polyimide-film-wrapped or glass-covered conductors in transformer or reactor oil (aging, BDV, PD).
- No published ESP qualification data were found (e.g., autoclave tests of wrapped wire in oil–water–gas mixtures). SPE OnePetro was not searched directly.

## 4. How do tape-wrapped and glass-covered rectangular wires tolerate edgewise and flatwise bending, and what defects arise?

### Takeaway
No manufacturer minimum bend radii (edgewise or flatwise) for polyimide-tape-wrapped or glass-covered rectangular wire were found. The available evidence is qualitative:
- An Indian standard warns that glass-braided, varnish-bonded rectangular conductors "are not necessarily suitable for severe edgewise bending".
- Patents describe the general defects: inner-radius wrinkling or separation, outer-radius cracking, tape splitting of stiff or heat-cured taped insulation, and inner-edge bulging.
- Bending strain also speeds polyimide hydrolysis, so bent regions are where wet-oil damage should appear first.

### Cited Findings
- IS 6181 (Indian standard on rectangular conductors for electrical machines; varnish-bonded, glass-braided covered conductors): "Covered conductors conforming to this Indian Standard are not necessarily suitable for severe edgewise bending." Special bending tests are left to agreement between purchaser and supplier. [STD] {search excerpt; PDF returned 404 when fetched} — [BIS SR6181](https://services.bis.gov.in/tmp/SR6181.pdf)
- **Edgewise bending of insulated rectangular wire, general:** at smaller bend radii the inner-side film tends to separate from the conductor and wrinkle, and the outer-side film may crack. [PAT] {search excerpt} — [EP 3 605 558 A1](https://data.epo.org/publication-server/rest/v1.2/patents/EP3605558NWA1/document.html); [US 11,581,127](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11581127)
- **Taped magnet wire:**
  - Insulation splitting is attributed partly to "rigid insulation tape materials that do not stretch or flex to conform". Heating the tape to cure its adhesive "makes the insulation tape even more brittle and more susceptible to splitting or cracking".
  - The wire deforms plastically through 90° coil bends.
  
  [PAT] {search excerpt} — [US 5,254,806](https://patents.google.com/patent/US5254806)
- **Edgewise-bent coils:** compression makes the inner edge bulge. This can degrade turn-to-turn insulation where bends line up. [PAT] {search excerpt} — [US 9,793,774](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9793774)
- **Strain and hydrolysis:**
  - Aerospace forced-hydrolysis tests deliberately wrap polyimide wire on a mandrel. Tighter bends are a "stress variant", whereas fluid-immersion testing typically uses a bend radius of at least 14 × the wire diameter.
  - Strain is one of the three accelerating factors for polyimide insulation aging, with moisture and temperature.
  
  [IND] {full text} — [Lectromec: forced hydrolysis](https://lectromec.com/forced-hydrolysis/); [PEER/GOV] {abstract/record} — [Campbell 1994, NTRS](https://ntrs.nasa.gov/citations/19950009633)
- **Test specimens:** IEC 60851-4 already uses U-shaped and mandrel-bent rectangular specimens in its 1000 h transformer-oil test and examines them for cracks (see Q2). [STD] {full text} — [IEC 60851-4:2016 copy](https://www.normsplash.com/FreeDownload/143987489/IEC-60851-4-2016-en-fr.pdf)
- **Film elongation limits:** heat-sealable Kapton magnet-wire films have a guaranteed minimum MD elongation of 45–65 % (HN: 55 %). Minimum FEP-to-Kapton heat-seal peel strength is 12.5–18.7 N/cm. [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)

### Inferences
- **Outer-fibre strain (calculation):** the strain at a bend is roughly ε ≈ (h/2)/(R_i + h/2), where h is the conductor dimension in the bending plane and R_i is the inner radius.
  - Edgewise bend of a 10 mm wide conductor at R_i = 10 mm: about 33 %. At R_i = 5 mm: about 50 %.
  - Flatwise bend of a 2 mm thick conductor at R_i = 2 mm: about 33 %.
  - Edgewise hairpin bends with R_i ≈ w therefore push the tape's outer side towards its guaranteed minimum elongation (45–65 %). They also stress the heat-sealed overlaps in peel. Expect tape opening or edge lifting at the outer radius and wrinkling or separation at the inner radius.
  - Glass fibres cannot stretch comparably. Varnish-bonded glass coverings should be expected to crack or craze the binder, with fibre fraying, at the outer radius. This is general materials knowledge; no source here quantifies glass-covering strain limits.
- **Specimen design:** the aging study should include pre-bent specimens (flatwise and edgewise, at the radii a hairpin would need) alongside straight ones. Each bend should be photographed before and after aging. Hydrolysis, wicking and delamination are all expected to start at bends and cut ends.

### Gaps
- No manufacturer datasheet with minimum flatwise or edgewise bend radius, or a mandrel requirement, was found for polyimide-tape-wrapped, glass-fibre-covered or film-plus-glass rectangular wire. No hairpin-forming trials with these wire types were found.
- The flexibility/adherence clauses (mandrel sizes, acceptance criteria) of IEC 60317-0-4/-0-5 and IEC 60317-44 could not be read.

## 5. Which IEC 60317 / NEMA MW 1000 parts cover these wire types, and what thermal classes and typical insulation builds apply?

### Takeaway
- **Type (a):** IEC 60317-44 covers aromatic-polyimide-tape-wrapped rectangular copper wire, class 240. Some countries, including the USA, assign it class 220. It covers widths of 2.00–16.00 mm and thicknesses of 0.80–5.60 mm.
- **Types (b) and (c):** glass-fibre-wound rectangular wire falls under IEC 60317-0-4, with particular parts 31 (TI 180) and 33 (TI 200). Glass-fibre-braided rectangular wire falls under IEC 60317-0-5 and part 39 (TI 180, polyester or polyesterimide varnish).
- **NEMA:** MW 1000 covers "fibrous-covered" wire. Its 2018 edition added glass-fibre-covered, varnish-treated round and rectangular spec sheets. A vendor maps Daglas rectangular wire to MW 46-C (155), MW 53-C (180) and MW 48-C (200); this mapping is unverified.
- **Not found:** no IEC or NEMA part for film-plus-glass composites, and no NEMA designation for polyimide-tape-wrapped wire.

### Cited Findings
- **IEC 60317-44 (1997 + AMD1:2010), "Aromatic polyimide tape wrapped rectangular copper wire, class 240".** [STD] {search excerpts} — [BSI record](https://knowledge.bsigroup.com/products/specifications-for-particular-types-of-winding-wires-aromatic-polyimide-tape-wrapped-rectangular-copper-wire-class-240); [GlobalSpec IEC 60317-44](https://standards.globalspec.com/std/1265230/iec-60317-44); [AFNOR NF EN 60317-44](https://www.boutique.afnor.org/en-gb/standard/nf-en-6031744/specifications-for-particular-types-of-winding-wires-part-44-aromatic-polyi/fa039652/4682)
  - Insulation is "one or two" layers of polyimide tape, coated on one or both sides with "a suitable adhesive, for instance, fluorinated ethylene propylene", and heat-sealed into a continuous sheath.
  - Temperature index 240; heat shock ≥ 260 °C. "in some countries (Canada, Russia, USA) this product is assigned a class 220".
  - Widths 2.00–16.00 mm; thicknesses 0.80–5.60 mm.
  - Ordering example: "60317-44 IEC 4,00 mm x 1,00 mm grade A2".
- IEC 60317-43 is the round-wire counterpart (aromatic polyimide tape wrapped round copper wire, class 240). [STD] {search excerpt} — [IEC 60317-43 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-43{ed1.1}b.pdf)
- **IEC 60317-0-4** (general requirements, glass-fibre-wound, resin- or varnish-impregnated, bare or enamelled rectangular copper wire; ed. 4.0 2020, earlier ed. 2.2). Particular specifications:
  - IEC 60317-31: TI 180; widths 2.0–16.0 mm.
  - IEC 60317-33: TI 200.
  
  [STD] {search excerpts} — [IEC 60317-0-4 ed. 4.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-4{ed4.0}b.pdf); [IEC 60317-31 preview](https://webstore.iec.ch/p-preview/info_iec60317-31%7Bed1.1%7Db.pdf); [IEC 60317-33 preview](https://webstore.iec.ch/p-preview/info_iec60317-33%7Bed1.1%7Db.pdf); [SCC record IEC 60317-0-4](https://scc-ccn.ca/standardsdb/standards/2015499)
- **Glass-fibre-braided rectangular wire:**
  - General requirements: IEC 60317-0-5 (Indian adoption IS 13730-0-5).
  - Particular: IEC 60317-39, glass-fibre-braided, polyester- or polyesterimide-varnish-treated, bare or enamelled, TI 180 (via IS 13730-39, based on the 1992 IEC edition).
  - One search summary said IEC 60317-40 is the TI 200 braided counterpart. This was not verified.
  
  [STD] {search excerpts} — [BIS SR13730-0-5](https://services.bis.gov.in/tmp/SR13730_0_5.pdf); [BIS SR13730-39](https://services.bis.gov.in/tmp/SR13730_39.pdf)
- **Round-wire glass parts (not directly applicable to the rectangular stock):**
  - IEC 60317-0-6 (general).
  - IEC 60317-48 (TI 155): its status conflicts between catalogues; DIN lists the 2012 edition as current and UNE as withdrawn.
  - IEC 60317-49 (TI 180).
  
  [STD] {search excerpts} — [IEC 60317-0-6 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-6{ed2.0}b.pdf); [GlobalSpec IEC 60317-49](https://standards.globalspec.com/std/1531922/iec-60317-49)
- **NEMA MW 1000:**
  - Scope: "round, rectangular, and square film insulated and/or fibrous covered copper and aluminum magnet wire".
  - The 2018 edition harmonised the dimensional requirements for glass-fibre-covered wire with the IEC approach and added "new specification sheets for glass fiber-covered, varnish-treated round and rectangular magnet wire".
  - The current edition is cited as 2020; a NEMA page also mentions 2023, and the review cites 2025.
  
  [STD] {search excerpts} — [NEMA news release](https://www.nema.org/news/Pages/NEMA-Publishes-Updated-Edition-of-Magnet-Wire-Standard.aspx); [ANSI blog](https://blog.ansi.org/ansi/changes-ansi-nema-mw-1000-2016-magnet-wire); [ANSI webstore MW 1000-2020](https://webstore.ansi.org/standards/nema/ansinemamw10002020); (already in review: [NEMA MW 1000 page](https://nema.org/directory/Products/MW-1000))
- **Rea Daglas NEMA mapping (vendor data):**
  - 155 °C (epoxy varnish or fused) → MW 46-C.
  - 180 °C (high-temperature polyester varnish) → MW 53-C.
  - 200 °C (silicone varnish) → MW 48-C.
  - An EIS listing shows Rea double-build Daglas rectangular wire (SSDDG) rated MW 46-C.
  - The search tool flagged the datasheet text as partly garbled, and a second search could not confirm the three numbers. Treat this as unverified.
  
  [MFR] {search excerpt} — [EIS: Rea Daglas SSDDG](https://www.eis-inc.com/product/magnet-wire-ph15-ssddg); [Rea data sheets](https://www.reawire.com/?p=110)
- **Polyimide film for type (a) builds:** the DuPont film constructions and thicknesses are those listed under Q1 (33–76.2 µm nominal). The UL thermal index of the film is 220–240 °C (electrical). [MFR] {full text} — [DuPont H-29423-4](https://www.electro-wind.com/web-files/DuPont/Literature/Kapton-motor-magnet-wire-bulletin.pdf)

### Inferences
- **Type (a) build (calculation):** a single 50 %-overlap helical wrap puts two film thicknesses on each face, so the dimensional increase is about 4 × the tape thickness.
  - 150FN019 (38.1 µm): about 0.15 mm.
  - 200FN919 (50.8 µm): about 0.20 mm.
  - 300FN929 (76.2 µm): about 0.30 mm.
  - Two 150FN019 wraps: about 0.30 mm.
  - The stock's 0.15–0.35 mm build is therefore consistent with one or two 50 %-overlap wraps of 1.5–3 mil FEP/PI tape, matching IEC 60317-44's "one or two" layers. Heat-sealing compression and the actual overlap will shift these figures.
- **Types (b) and (d):** a 0.35–0.50 mm build is consistent with a polyimide or film wrap (about 0.1–0.2 mm) plus a glass serving. No standard part for this composite was found, so it is probably a manufacturer-specific or customer-specified construction.
- **Size range:** stock conductors up to about 18 mm wide exceed the 16 mm upper width in IEC 60317-44 and -31. Those sizes are probably supplied to manufacturer or customer specifications rather than the IEC sheets.
- **Thermal classes:** the expected nominal classes are type (a) 240 (or 220 in North America); type (c) 155/180/200 depending on binder; type (b) at least 180–200, limited by the glass binder; type (d) 130–155 if the film is PET, or 180+ if PI. For type (d) this is an inference that depends on identifying the film.

### Gaps
- No NEMA MW 1000 designation for polyimide-tape-wrapped rectangular wire was found, and the Daglas MW numbers are unverified.
- The IEC 60317-44 grades (e.g., "A2") and their minimum insulation increase or breakdown voltages were not read. Neither were the IEC 60317-0-4/-31/-33/-39 coating grades and increase-in-dimension tables.
- No IEC 60317 part was found for "film plus glass" (PET or PI film with glass serving) rectangular wire.
