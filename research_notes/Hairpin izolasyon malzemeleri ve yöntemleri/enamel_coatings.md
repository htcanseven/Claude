# Enamel (solvent-borne thermoset wire-enamel) insulation for bare rectangular hairpin copper conductors

> Scope: enamel coatings only (extrusion, tapes, tubes, powder/e-coat/parylene and test standards are covered by other researchers). Research date: 2026-10-10. Conventions: "Vp"/"kVpk" = peak volts; "per side" = single-wall film thickness; "Dt" = total insulation between two conductors. Source dates are given in brackets; anything older than ~2022 is flagged as older. All numbers below come from pages/PDFs that were actually opened (several PDFs were downloaded and text-extracted).

## Q1. Which enamel chemistries are used on rectangular hairpin wire, what thermal classes apply, and which IEC 60317 / NEMA MW 1000 specifications cover them?

### Takeaway
The enamel systems that matter for hairpins are THEIC-polyesterimide (PEsI, class 180/200), dual-coat PEsI (or polyester) base + polyamide-imide (PAI) overcoat (class 200), sole-coat PAI (class 220) and aromatic polyimide (PI, class 240). Each has a dedicated IEC rectangular-copper part (60317-28, -82, -29, -58, -47), all read with the general part IEC 60317-0-2 and all limited to conductor 2.0–16.0 mm × 0.80–5.60 mm with only grade 1 and grade 2 builds. Sumitomo's published history shows Japanese OEM practice moving from esterimide to PAI ("AIW") to PI ("PIW") for HEV/EV drive motors. Polyurethane and plain polyester are low-class and only of historical or reference interest.

### Cited Findings

#### IEC 60317 rectangular-copper parts (all: width 2.0–16.0 mm, thickness 0.80–5.60 mm, grade 1 and grade 2 only; combinations of width/thickness are defined in IEC 60317-0-2)
- **IEC 60317-0-2 (general requirements, enamelled rectangular copper wire):** the current edition is Ed. 4.0 (BS EN IEC 60317-0-2:2020, published 31 Aug 2020, identical to IEC 60317-0-2 Ed. 4.0). It specifies the minimum and maximum increases in width and thickness caused by the insulation (and any bonding layer). New in Ed. 4.0: clause 4.5, which sets minimum, nominal and maximum overall dimensions including the bonding layer, plus new references to copper-rod specifications — [BSI Knowledge](https://knowledge.bsigroup.com/products/specifications-for-particular-types-of-winding-wires-general-requirements-enamelled-rectangular-copper-wire)
- **IEC 60317-28:** polyesterimide rectangular copper wire, **class 180**, sole coating of PEsI (may be modified). The current consolidated version is 2013 ed. 2 + AMD1:2024 (ed. 2.1, 2024-06-18). The 2013 edition deleted the "high temperature failure" clause and changed the pin-hole test (Clause 23) — [IEC webstore](https://webstore.iec.ch/en/publication/96016)
- **IEC 60317-82:2020 (June 2020):** polyesterimide rectangular copper wire, **class 200**, sole coating — [AFNOR](https://www.boutique.afnor.org/en-gb/standard/iec-60317822020/specifications-for-particular-types-of-winding-wires-part-82-polyesterimide/xs137256/248845)
- **IEC 60317-29:1990 (ed. 1.0, 1990-10-15, stability date 2027; older document):** polyester or polyesterimide underlying coat **overcoated with polyamide-imide**, rectangular copper, **class 200**. It requires a minimum temperature index of 200 and a heat-shock temperature of at least 220 °C — [IEC webstore](https://webstore.iec.ch/publication/1387)
- **IEC 60317-58 (Ed. 1.0, 2010-08):** **polyamide-imide** rectangular copper wire, **class 220**, sole coating. Class 220 requires a minimum temperature index of 220 and a heat shock of at least 240 °C. The test clauses listed are: dimensions, electrical resistance, elongation, springiness, flexibility and adherence, heat shock, cut-through, resistance to abrasion, resistance to solvents, breakdown voltage, continuity of insulation, temperature index, resistance to refrigerants, solderability, heat bonding, dielectric dissipation factor, resistance to transformer oil, loss of mass, and pin-hole test. There is no PD/PDIV clause — [IEC 60317-58 preview PDF (VDE)](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-58%7Bed1.0%7Db.pdf)
- **IEC 60317-47:** **aromatic polyimide** rectangular copper wire, **class 240**, sole coating. The current version is 2013 ed. 2 + AMD1:2024 (ed. 2.1, 2024-06-14). The 2013 edition added a pin-hole test (Clause 23) and revised the dissipation-factor notes — [IEC webstore](https://webstore.iec.ch/en/publication/95918)
- The round-wire PAI counterpart is IEC 60317-57, "Polyamide-imide enamelled round copper wire, class 220" (Ed. 1.1, 2024-06) — [IEC 60317-57 preview PDF (VDE)](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-57%7Bed1.1%7Den.pdf)
- IEC 60317-80:2019 covers polyvinyl acetal rectangular wire, class 120, with a bonding layer. It is not a traction-motor candidate and is listed only for completeness — [IEC webstore](https://webstore.iec.ch/en/publication/60783)

#### NEMA MW 1000 (only indirect access)
- Essex GP/MR-200 rectangular wire (0.130 in × 0.312 in), **NEMA MW 36**, heavy build, **modified polyester basecoat + polyamide-imide topcoat**, Class H **200 °C**. The manufacturer field reads "Essex Solutions" and the distributor says it supplies "Essex Furukawa" products — [Electrowind listing](https://www.electro-wind.com/superior-essex-130-312-heavy-gp-mr-200-mw-36-magnet-wire-24in)
- Axalta states that Voltatex 8536 (nano-modified PAI) exceeds IEC 60317-13/22/25 and can be used for ANSI/NEMA MW 35-C, MW 36-C, MW 73-C and MW 102-A-C (with other Voltatex products) — [Axalta Voltatex 8536](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/product-catalog/Voltatex-8536.html)

#### Chemistry-level property comparison (Elantas-affiliated PhD thesis, Univ. Camerino/ELANTAS Europe, 2022)
- Temperature index per IEC 60172: PVF ≤120 °C; polyester 120–150 °C; THEIC-modified polyester 155–200 °C; polyesterimide ≤155 °C; THEIC-modified PEsI 180–200 °C; PU 155–180 °C; **PAI ≤220 °C; PI ≥240 °C** — [Leone 2022 thesis, Table 3](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- Same table: cut-through PAI 390–420 °C, PI >550 °C, THEIC-PEsI 390–440 °C. Heat shock PAI 240 °C, PI >260 °C, THEIC-PEsI ≤180 °C. Breakdown voltage **PAI and PI 150–190 V/µm**, THEIC-PEsI 130–160 V/µm, PU 120–150 V/µm. The THEIC-mod PE entry is printed as "120-1510", an apparent typo. Qualitative ratings: adherence PAI "++" and PI "++" (acceptable) vs PE/PVF "+++++"; flexibility PI "+++", PAI "++++"; abrasion resistance PAI and PI "+++++"; resistance to transformer oils PAI and PI "+++++", THEIC-PEsI "++++" — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- Polyurethane (mention only): solderable at 375 °C and used in small transformers, relays and motors — [Axalta "What are wire enamels"](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html)

#### Usage history at a hairpin/flat-wire maker (Sumitomo Electric, SEI Technical Review; 2017–2020, older)
- Dual-coat origin: in 1968 a PEsI single coat failed requirements, so Sumitomo developed a double-coated wire with a **180 °C-class modified PEsI base layer + PAI topcoat**. The PAI topcoat compensated for the PEsI's disadvantages and the combination reduced cost — [SEI TR No. 84 (2017), "History and Future Prospects of Magnet Wire Development"](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- Sumitomo's UTZ wire was adopted in the world's first HEV drive motor. An amide-imide wire (AIW) was then used for newer HEV drive motors because of its more stable thermal resistance and better "anti-degradation in wire treatment". Sumitomo then commercialised a polyimide wire (PIW) — [SEI TR No. 84 (2017)](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- **AIW (PAI) vs PIW (PI), Sumitomo data:**

  | Property | AIW (PAI) | PIW (PI) |
  |---|---|---|
  | Thermal class | 220 °C | 240 °C |
  | Thermal durability | 220 °C × 500 h "NG" | 280 °C × 2000 h "OK" |
  | Ultimate elongation of film | ~45 % | ~80 % |
  | Permittivity | 4.3 | 3 |
  | Water absorption | 4.5 % | 3.0 % |
  | Tg | 280 °C | 350 °C |
  | Elastic modulus at 400 °C | 30 MPa | 1000 MPa |

  PIW is more expensive than AIW. Sumitomo cut its price by refining the resin synthesis — [SEI TR No. 84 (2017)](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- Early drive motors used esterimide (low permittivity, giving higher PDIV) and amidimide (slightly worse permittivity, better heat resistance). Sumitomo then marketed PI rectangular wire, which is superior in "resistance to degradation of wire treatment" while combining low permittivity and high heat resistance, and made it price-competitive. PI permittivity is 3.0, and chemical modification of the PI only reached 2.7 — [SEI TR No. 90 (2020), "Magnet Wires for Driving Motors in Electric Vehicles"](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)
- A grade-2, 220 °C-class round-wire enamel of 30 µm measured εr = 4.55 at 25 °C and 4.59 at 180 °C (Novocontrol Alpha-N). The authors treat it as PAI with Tg well above 180 °C — [Gao et al., IEEE TDEI 30 (2023) 2870, postprint](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)

#### Supplier positioning (enamel makers)
- ELANTAS (ALTANA): its polyimide wire enamels are presented as primary insulation for e-mobility motors from 400 V up to 1,200 V. Claims: "enhanced corona resistance", "special oil resistance", "very low permittivity" (no number given), excellent adhesion on copper, and multiple PI layers combined in a single insulation system. The page is undated; embedded image metadata shows 2026 — [ELANTAS "Wire Enamels PI"](https://www.elantas.com/en-br/stories/wire-enamels-pi/)
- ELANTAS e-mobility page: wire enamels provide thermal endurance and partial-discharge resistance and are "tailored to modern motor concepts such as hair-pin and concentrated windings" for 400–1,200 V systems — [ELANTAS eMobility](https://www.elantas.com/solutions/market-segments/emobility/)
- ELANTAS Tongling lists high-thermal enamel brands (ALLOTHERM, SUPRADURIT, THERMEX, ULTRATHERM, TRITHERM) and "elevated electrical stress" brands (**CORONA-PROTECT, ELAN-SHIELD**). It mentions corona-resistant and oil-resistant specialty grades without per-product data — [ELANTAS Tongling PAI enamels page](https://elantas.com/tongling/products/wire-enamels/polyamideimide-enamels.html)
- Axalta Voltatex: PAI "single or dual coat". Voltatex 8300 is a flexible PAI topcoat over polyester/PEsI basecoats and is recommended for flat wire in large transformers and generators. THEIC-PEsI and THEIC-polyester basecoats are also offered — [Axalta "What are wire enamels"](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html)
- Furukawa's patent examples use **Hitachi Chemical HI-406** as the PAI varnish and **Unitika "U Imide"** as the PI varnish — [US10418151B2 (Furukawa; 2013 priority)](https://patents.google.com/patent/US10418151B2/en)

### Inferences
- **Candidate systems for the test plan, by IEC class:** (1) PEsI + PAI dual coat, class 200, IEC 60317-29 (the cost/"workhorse" baseline); (2) PEsI sole coat, class 180 (-28) or class 200 (-82), as a low-cost reference; (3) PAI sole coat, class 220 (-58); (4) aromatic PI, class 240 (-47); plus (5) nano-filled corona-resistant PAI variants (Q2) and (6) foamed or low-k PI (Q3). PU and polyester (class ≤155) are not relevant for traction hairpins.
- **PD properties are not standardised:** the IEC wire parts define thermal and mechanical acceptance (heat shock, flexibility/adherence, springiness, cut-through, breakdown). Inverter/PD qualification therefore has to come from the separate PD test standards (covered by the test-standards colleague).
- **What the dielectric data imply:** PAI's higher permittivity (4.3–4.6) and higher water uptake (4.5 %) explain why makers moved to PI (εr ~3.0, 3.0 %) for higher-voltage HEV/EV motors despite its cost.

### Gaps
- The numerical grade 1 and grade 2 "increase in dimension" tables in IEC 60317-0-2 could not be read: the standard is paywalled, the VDE preview PDF had no extractable text, and the BIS draft link returned 404. I could not confirm whether a grade 3 or thick-film grade exists for rectangular wire.
- The NEMA MW 1000 text was not accessed. MW 36(-C) is known only via a distributor listing and Axalta's compatibility list. The MW 20-C (polyimide rectangular) requirements were not verified because the distributor page returned 403.
- Pyre-ML (Industrial Summit Technology) polyamic-acid enamel datasheets (εr, cure schedule) could not be opened (UL Prospector returned 403). Search snippets alone indicate a NEMA 240 °C rating; this is unverified.
- No product pages were opened for Von Roll, Totoku or Resonac enamels. The Resonac link to Hitachi Chemical HI-406 is not verified here.

## Q2. Inverter-grade / corona-resistant (partial-discharge-resistant) enamels: products and reported gains

### Takeaway
Corona-resistant (CR) enamels add nano or sub-µm inorganic fillers (SiO2, TiO2, Al2O3, hybrid sol-gel) to PAI or PEsI, used as single coat, basecoat, midcoat or topcoat. Commercial enamels exist (Axalta Voltatex 8536, Axalta Voltron 7700/8500 system, ELANTAS CORONA-PROTECT/ELAN-SHIELD). Reported lifetime gains above PDIV range from about 3× (a Chinese patent on its own PAI vs a commercial composite) to about 43× (an ALTANA/Schenectady patent). These figures come from patents and vendors and are condition-specific. CR enamels extend life once PD occurs; none of the opened sources shows them raising PDIV. Their advantage collapses after stretching or forming (10 % elongation left <20 % of corona life) and after ATF ageing for PEsI/PAI composites.

### Cited Findings
- **Axalta Voltatex 8536:** "a nano-modified polyamide-imide enamel, based on an innovative inorganic-organic hybrid polymer". Solids 34.0–37.0 % (1 g, 1 h, 180 °C); viscosity 2,200–4,500 mPa·s (DIN 53015, 23 °C); thermal class 200 °C; wire-diameter range 0.20–3.00 mm. Usable as single coat, basecoat, mid-coat or topcoat, and the "overcoat and single coat [are] designed for rectangular and heavy round wire". Claims "outstanding resistance to partial discharges" for inverter-fed motors but gives no numbers. Used in "Voltron Systems" with Voltatex 7740/7735 FL on large round and flat wire — [Axalta Voltatex 8536](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/product-catalog/Voltatex-8536.html)
- **Axalta Voltron system:** a patented system of Voltatex 7700 basecoat + Voltatex 8500 topcoat for inverter-fed motors, wind generators and hybrid motors. Axalta notes it "can only be used under certain conditions" — [Axalta "What are wire enamels"](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html)
- **ELANTAS:** CORONA-PROTECT and ELAN-SHIELD brands for "elevated electrical stress"; PI enamels with "enhanced corona resistance" for 400–1,200 V. No quantitative data on the opened pages — [ELANTAS Tongling](https://elantas.com/tongling/products/wire-enamels/polyamideimide-enamels.html); [ELANTAS PI](https://www.elantas.com/en-br/stories/wire-enamels-pi/)
- **ALTANA/Schenectady patent US6337442B1** (priority 1997; lapsed 2010; older):
  - Composition: PD-resistant top coat of PAI (or PE/PEsI/PU) binder with TiO2 at 5–30 wt % of binder (10–20 wt % preferred) plus pyrogenic silica up to 20 wt % relative to TiO2; solids 20–50 wt %; viscosity 200–2000 mPa·s.
  - Coating example: commercial PEsI basecoat in 8 passes + filled top coat in 2 passes, oven at 520 °C, 0.71 mm wire, take-off speed 34 m/min.
  - Result: IEC twisted pairs at 4.5 kV, 50 Hz, stored at 140 °C, lasted "about a factor of 43 longer" than conventional enamel. Only a factor is reported, with no absolute lifetimes or sample statistics.
  - The patent criticises Cr2O3/Fe2O3 fillers (high density, sedimentation) and alumina (abrasive to coating nozzles).
  - — [Google Patents US6337442B1](https://patents.google.com/patent/US6337442B1/en)
- **Suzhou Jufeng patent US12159731B2** (CN priority 2020-04-14; granted 2024-12-03):
  - Background: "200-grade" PEsI/PAI composite corona-resistant enamelled wires are the main CR products for EV motors, but they show poor ATF resistance. Japanese single-coat PAI wire has good ATF resistance but is "expensive due to Japanese technology monopoly".
  - Structure: five layers (ATF-protective PES / CR PAI with nano-SiO2 of 40–50 nm, D50 ≤100 nm / protective / PAI / protective).
  - Corona test: 155 °C, 20 kHz, 100 ns pulse time, 3000 V square wave.
  - Fresh corona life: commercial composite **36 h 52 min**; single-coat PAI **109 h 36 min**; embodiments **116–128 h**.
  - After ATF cycling: commercial composite **3 h 18 min**, with breakdown falling from 15.39 kV to **5.53 kV**; single PAI 59 h 12 min (breakdown 15.52 → 10.82 kV); embodiments 95–110 h (breakdown 14.15–15.09 kV).
  - The text and tables contain minor internal inconsistencies.
  - — [Google Patents US12159731B2](https://patents.google.com/patent/US12159731B2/en)
- **Furukawa US10418151B2** (2013 priority):
  - Fillers: alumina, silica or titania (titania preferred) with primary particles ≤100 nm (preferably ≤20 nm) at 10–50 mass %.
  - PD-resistance criterion: breakdown time at 1.6 kVp, 10 kHz, 25 ± 10 °C; >10 h is "particularly excellent", >2 h is "excellent".
  - — [Google Patents US10418151B2](https://patents.google.com/patent/US10418151B2/en)
- **Effect of stretching on CR wire** (Shanghai Electrical Apparatus Research Institute, 2017; older): CR enamelled wire was stretched 10 % and 15 %. Corona-resistance time fell sharply, with the 10 % sample retaining **<20 %** of its corona-resistance time. Breakdown voltage fell only slightly, with the 15 % sample retaining **>85 %** — [Electric Machines & Control Application 44(8) 115–119, abstract](https://opaj.napstic.cn/periodicalArticle/0120171002033563)
- **Mechanism (Sumitomo):** above PDIV, partial discharges erode the film until dielectric breakdown. At motor terminals, the inverter surge peak "may reach about double the inverter voltage" — [SEI TR No. 88 (2019)](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf)

### Inferences
- In an 800 V SiC design, a CR enamel is a life-extension margin rather than a PDIV improvement: none of the opened sources shows nano-fillers raising PDIV, only time-to-failure above PDIV. Test plans should therefore measure both PDIV/RPDIV and voltage endurance (V–t), on straight samples and on formed/stretched samples.
- Because 10 % strain removed more than 80 % of CR life, CR performance should be tested after edgewise/flatwise bending and twisting, and after ATF ageing (the composite lost about 91 % of its corona life in the Jufeng test).
- For lab application of filled enamels, filler sedimentation and agglomeration (flagged for dense oxides) and die abrasion (alumina) are practical risks. Re-dispersion and the use of commercial pre-dispersed grades (e.g., Voltatex 8536) are advisable.
- **Corona-resistance vs ATF ranking from the Jufeng data:** for oil-cooled hairpin stators, sole-coat PAI or multilayer CR systems outperform standard PEsI/PAI composites after ATF ageing.

### Gaps
- No independent, open-access voltage-endurance data were found for commercial nano-filled enamels on rectangular hairpin wire. The ELANTAS Deatherm E 641 GL press item could not be opened (page empty). A Polish institute's "≥100× PD resistance" nano-PAI claim could not be opened (403). The Korean nanosilica-PAI paper failed to download (connection reset).
- No product datasheets were found for CR rectangular wire from Essex Solutions/Essex Furukawa, Proterial, LS Cable/LS EVC, Elektrisola, Jingda or Gold Cup. Jintian Copper lists "corona-resistant", "high PDIV" and "ATF oil-resistant" flat wires but gives no data — [Jintian article](https://en.jtcopper.com/do-you-know-why-enamel-insulated-flat-wire-is-now-being-used-in-new-energy-vehicles-provided-by-customer.html)
- The test conditions in these sources (50 Hz sine vs 20 kHz square vs 10 kHz sine; 140–155 °C) are not comparable to each other. A normalised comparison is not possible from these sources.

## Q3. Low-permittivity enamels: foamed/porous PI or PAI and low-k PI, with εr values and PDIV gains

### Takeaway
Sumitomo Electric (Wintec) has the best-documented low-k enamel: polyimide with uniformly distributed **closed micro-cells**.
- Permittivity: εr falls from 3.0 to **2.2 at ~30 vol %** cells and to **1.7 at ~50 vol %**.
- PDIV: rectangular pair samples gain **+200 Vp at 60 µm** (1230 → 1440 Vp), or reach the same 1230 Vp with **44 µm instead of 60 µm** (about 30 % thinner).
- Breakdown: closed cells raised breakdown voltage from 4.9 kV (open-cell foam) to 10.8 kV.
- Chemical modification of PI reached only εr 2.7.

Furukawa (now Essex Furukawa/Essex Solutions per patent assignee data) patented foamed PI/PAI laminates with εr ≤3.0 at 200 °C. As of the 2020 Sumitomo paper, microcellular wire was "under development"; its 2026 production status is unconfirmed.

### Cited Findings
- **Sumitomo rectangular low-k wire** (SEI TR No. 88, April 2019; older):
  - Permittivity: microcells of about 30 vol % reduce PI εr from 3.0 to 2.2, and about 50 vol % to 1.7.
  - PDIV method: pair samples of two rectangular wires pressed flat-face to flat-face, 60 µm film, 60 Hz AC ramped at 1.0 kV/min, 25 °C, 50 % RH, mean of 10 runs.
  - PDIV result: **PI 1230 Vp vs microcellular (30 vol %) 1440 Vp**.
  - Breakdown voltage (foil-wrapped AC test): conventional open-cell foam **4.9 kV** vs new closed-cell **10.8 kV**.
  - Withstand-voltage life at 10 kHz sine, 25 °C: at **1600 Vp, 25 min vs 402 min**; at **1400 Vp, 49 min vs no breakdown after 3,000 min**.
  - Temperature and pressure: PDIV fell with temperature and with lower pressure at the same rate for both wires.
  - Dakin relation used: V = √2 × 163 × (2t/εr)^0.46 (V in Vp, t in µm).
  - — [SEI TR No. 88, "Rectangular Magnet Wire for Electric and Hybrid Electric Inverter-Drive Motors"](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf)
- **Sumitomo summary** (SEI TR No. 90, April 2020): to reach 1,230 Vp, PI needs 60 µm while the microcellular coating needs 44 µm, "about 30%" thinner. Chemical modification of PI reached only εr 2.7 (PI 3.0). Sumitomo reported the microcellular wire as "under development" — [SEI TR No. 90](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)
- **Sumitomo round-wire predecessor** (SEI TR No. 84, April 2017; older):
  - Samples: 1.0 mm wire, 30 µm PI, twisted pairs per JIS C 3216-5.
  - PDIV: foamed (30 vol %, εr 2.2) **985 Vp vs 770 Vp** for solid PI.
  - V–t at 10 kHz, 25 °C (table values): 1200 Vp gave 35 vs 80 min; 900 Vp gave 80 min vs no breakdown.
  - V–t at 200 °C: 1200 Vp gave 25 vs 40 min; at 800 Vp the foamed wire did not break down.
  - The running text gives slightly different minutes (36/80, 78, 25/43).
  - — [SEI TR No. 84, "Magnet Wire with Enhanced Tolerance for High Frequency Voltage"](https://global-sei.com/technology/tr/bn84/pdf/84-17.pdf)
- Sumitomo's porous coating with 50 % air in the PI reached εr 1.7 — [SEI TR No. 84 (2017)](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- Sumitomo Electric Wintec Magnet Wire (Changzhou) was established 21 March 2019 to make rectangular magnet wire, with full operation planned for 2022 — [Magnetics Magazine](https://magneticsmag.com/sumitomo-advances-development-manufacturing-of-its-rectangular-magnet-wire-for-evs/)
- **Furukawa foamed laminate patent US10418151B2** (2013 priority; current assignees per Google include Essex Solutions Inc. / Essex Furukawa Magnet Wire LLC):
  - Structure: foamed region of thermosetting PAI or PI (PI preferred) with alternating cell and non-cell layers; closed cells ≤20 µm (preferably ≤5 µm) in the thickness direction.
  - Porosity 10–70 % (preferably 20–50 %); total laminate ≥40 µm (preferably ≥60–80 µm).
  - **εr at 200 °C ≤3.0** (preferably ≤2.7, ≤2.5), versus 3–4 for prior-art resins.
  - Rating thresholds: PDIV ≥1.0 kVrms (1414 Vp) at 25 °C, 50 Hz, 10 pC is "particularly excellent"; breakdown ≥80 kV/mm is "particularly excellent".
  - Background: experience shows the insulating layer must be 100 µm or more to address PDIV.
  - — [Google Patents US10418151B2](https://patents.google.com/patent/US10418151B2/en)
- ELANTAS claims "very low permittivity" for its PI e-mobility enamels but publishes no value — [ELANTAS PI](https://www.elantas.com/en-br/stories/wire-enamels-pi/)

### Inferences
- Under Dakin scaling, PDIV ∝ (t/εr)^0.46. Cutting εr from 3.0 to 2.2 is therefore worth the same as raising the build by a factor of 3.0/2.2 ≈ 1.36, which matches Sumitomo's 44 µm vs 60 µm. Foamed enamels give fill-factor benefits, not just PDIV.
- Foamed or microcellular enamels need controlled bubble nucleation inside a production enamelling tower (closed cells only; open cells halved breakdown in Sumitomo's data). They are not realistically reproducible by hand on a cut bar. For a test plan they are "obtain supplier samples" items, not lab-application items.
- Under the same scaling, fluorinated or alicyclic low-k PI chemistries (εr ~2.7 per Sumitomo's best chemical result) give only a modest PDIV gain (~5 % for 3.0 → 2.7).

### Gaps
- I could not confirm whether Sumitomo's microcellular PI rectangular wire, or Furukawa/Essex foamed enamel wire, is in series production in 2026.
- Patent hits on fluororesin-filled or alicyclic low-k PI enamel layers were not opened. No commercial low-k fluorinated PI wire enamel with a published εr was found.
- No low-k PAI enamel data were found, other than Furukawa allowing PAI in the foamed region.

## Q4. Typical build thickness per side, corner/edge thinning ("dog-bone"), corner-radius effects and number of passes

### Takeaway
Enamel is built from many thin passes of about 2–5 µm each.
- Builds: 30–60 µm per side is well documented (e.g., Sumitomo PI rectangular at 60 µm). A 40 µm PAI film took 15 passes at 520 °C.
- Pass limit: Furukawa reports adhesion "drops sharply" beyond ~20 passes because copper oxide grows. Yet "≥100 µm" is cited as necessary for PDIV, which pushes thick builds toward hybrid (enamel + extruded) solutions.
- Corner thinning: corners come out thinner than flats because wet-film surface curvature drives enamel from corners to flats. In a 20 µm-target example, corners were 12–13 µm vs 15–26 µm on flats, and a die redesign raised breakdown from 3.26 to 4.71 kV.
- Corner radius: a measurable PDIV factor (Naderiallaf et al. 2024).

### Cited Findings
- **Pass build:** "Six to eight coats of enamel are applied, with individual coats of the order of 0.002 to 0.005 mm". Multiple coats cover blow-holes and bare spots, and thin coats cure fast (general wire-enamelling description) — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- Axalta: enamel is applied "in up to 30 layers" — [Axalta](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html)
- **Furukawa pass and thickness data** (round-wire context):
  - Comparative Example 4: a PAI-only 40 µm coating made in **15 passes at 520 °C for 30 s**.
  - Repeated passes increase copper oxide, and adhesion "drops sharply" when passes through the baking furnace exceed **20**.
  - Experience shows **≥100 µm** insulation is needed to address PDIV.
  - — [US10418151B2](https://patents.google.com/patent/US10418151B2/en)
- **Dog-bone mechanism and data** (Hitachi Metals, now Proterial, US9330817B2; 2010 priority, granted 2016):
  - Mechanism: solid dies leave the coating thinner on rounded corners and thicker on flats. Surface-curvature differences in the wet varnish drive flow from corners to flats before baking. A die-hole corner radius smaller than the conductor's makes it worse, and varnish pooling can tilt the conductor off-centre.
  - Example on a 1.0 × 5.0 mm conductor with 20 µm design thickness: conventional die gave flats **15–26 µm** and corners **12–13 µm** (max–min 14 µm), breakdown **3.26 kV**. The die with protrusions gave flats 20–25 µm and corners **23–24 µm** (max–min 5 µm), breakdown **4.71 kV** (~1.4×).
  - Claims: flat-surface variation ≤25 % of target; flat-vs-corner difference ≤20 %; target thickness 20–100 µm; conductor sides 0.5–17 mm.
  - Die types: four-part adjustable die assemblies vs solid dies. Apply-and-bake is repeated several times with different dies.
  - — [Google Patents US9330817B2](https://patents.google.com/patent/US9330817B2/en)
- **Sumitomo:**
  - "The thickness of the coating formed by baking is always less at the corners of rectangular wire." Insulation must be guaranteed at the thinnest point, which forces unnecessarily thick areas. Sumitomo developed a baking method that made the coating uniform and reduced material cost — [SEI TR No. 84 (2017)](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
  - The outer dimension is set by the maximum film thickness, so non-uniformity lowers the space factor and raises material use — [SEI TR No. 90 (2020)](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)
  - Film thickness used in its rectangular PI and microcellular pair tests: 60 µm — [SEI TR No. 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf)
- **Dip-coating edge effect** (GE US3850773A, 1974; old): dip coating needs "as many as five or more" passes through bath and tower. Square magnet wire and flat strip end up with more coating at the centre than at the edges — [Google Patents US3850773A](https://patents.google.com/patent/US3850773A/en)
- **Corner/fillet radius:** Naderiallaf, Degano, Gerada, Gerada, IEEE TDEI 31(4) 2084–2093 (2024), DOI 10.1109/TDEI.2024.3355032. They show that fillet radius changes turn-to-turn PDIV and its dispersion (tests at 30 °C, 35 % RH, 1000 mbar, 50 Hz, per IEC 60034-18-41; Weibull model based on Schumann's criterion) and propose choosing the radius to maximise PDIV. The abstract page gives no numbers — [UNNC research portal](https://unnc.globalimpact.cn/en/publications/fillet-radius-impact-of-rectangular-insulated-wires-on-pdiv-for-t)
- Hairpin PDIV samples in Gao et al. used a 2.48 × 2.78 mm² conductor with **0.8 mm corner radius** — [Gao 2023 postprint](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- Grade-2 round enamel thickness in the same study: 30 µm — [Gao 2023](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- A University of Padua MSc thesis with industrial partner De Angeli Prodotti (2023/24) characterises enamel on copper flat wire and models the deposition process from enamel physical properties and die geometry. Only the abstract is public; the full text is restricted — [Padua thesis record](https://thesis.unipd.it/handle/20.500.12608/78306)

### Inferences
- Plausible enamel-only builds for hairpins are ~30–80 µm per side (10–25 passes at 3–5 µm). Builds of ~100–150 µm per side by enamel alone would need ~30–50 passes, beyond the ~20-pass adhesion warning. This is consistent with the industry shift to enamel + extruded PEEK (e.g., Essex Furukawa's PEEK-over-enamel rectangular wire per [Magnetics Magazine](https://magneticsmag.com/sumitomo-advances-development-manufacturing-of-its-rectangular-magnet-wire-for-evs/)).
- For test specimens: measure **corner thickness** (cross-section microscopy) as well as flat thickness. Both breakdown (Hitachi example) and PDIV (field enhancement) are governed by the thinnest, most curved region. Report the corner radius of the bare conductor, which drives both dog-boning and PDIV.

### Gaps
- No numerical "increase in dimension" values were obtained for IEC grade 1/2 or NEMA heavy build on rectangular wire (see Q1 gaps).
- No public measurements were found of corner/flat thickness ratios on current commercial EV hairpin enamel wires. Only patent examples are available.
- The numerical PDIV-vs-fillet-radius results of Naderiallaf 2024 are behind a paywall.

## Q5. Application methods: industrial lines, lab-scale coating of a cut bare conductor, solvents (NMP/REACH alternatives), water-borne/UV

### Takeaway
- **Industrial:** a continuous anneal–clean–coat–cure process. Vertical ovens are used for large round and flat wire; horizontal ovens for medium/fine wire. Enamel is metered by dies (felts only for fine wire), in many thin passes, with oven air at 500–700 °C and catalytic solvent combustion. Flat wire uses rectangular solid dies whose geometry controls dog-boning.
- **Lab, on a cut bar:** no standard bench method was found. Dip, brush, spray and drawdown all suffer centre-over-build/edge-thinning, solvent blistering in thick coats, and poor cure-profile reproduction. The closest industrial-like approach is multiple thin wiped/dipped coats, each flashed and cured, with a final post-cure (inference).
- **Solvents:** NMP is restricted under REACH Annex XVII entry 71 (≥0.3 %; worker DNEL 14.4 mg/m³ inhalation, 4.8 mg/kg/day dermal). The obligations have applied to wire coating since **9 May 2024**. Proven drop-in alternatives are scarce: an ELANTAS-linked study found MDPA works for PI enamels, while NFM fell short for PAI and Cyrene was unsuitable.
- **Water-borne / UV-curable:** no current commercial water-borne or UV-curable hairpin enamel was found.

### Cited Findings

#### Industrial enamelling
- Vertical ovens are preferred for large diameters (round and flat wires) with medium-high viscosity enamels (2,000–10,000 cP at 23 °C). Horizontal ovens suit medium-fine wire with 100–2,000 cP enamels. Dies are used for wires >0.2 mm with viscosity >200 cP; felts for 0.05–0.2 mm wires with <200 cP — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- Line sequence: annealing and cleaning of the bare wire at high temperature in a reducing steam atmosphere, then enamel applied by dies or felts before each oven pass. Curing comprises solvent evaporation, molecular-weight build-up, crosslinking and ring closure (imidisation). Oven temperature is **500–700 °C**. Catalytic ovens burn solvent vapours over a catalyst at up to ≈600 °C and recirculate the heat — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- Typical PAI enamel solids are **35–45 %**. Polyamic acid (the PI precursor) is cured to PI on copper or aluminium wire in the enamelling oven "at around 500 °C". PAI/PAA are synthesised in NMP, DMF, DMAc or DMSO, while PEsI enamels are sold in cresylic solvents with hydrocarbons — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)
- Enamel solids range from ~8 % to 60 % (1 g/1 h/180 °C) and viscosity from 30 to 60,000 mPa·s at 23 °C. Application is horizontal or vertical, by dies or felts — [Axalta](https://www.axalta.com/electricalinsulation_global/en_US/wire-enamels/what-are-wire-enamels.html)
- Industrial examples: 0.71 mm round wire with 8 basecoat + 2 topcoat passes, oven 520 °C, 34 m/min — [US6337442B1](https://patents.google.com/patent/US6337442B1/en). A 40 µm PAI coating in 15 passes at 520 °C × 30 s — [US10418151B2](https://patents.google.com/patent/US10418151B2/en)
- Flat-wire dies: four-part adjustable die assemblies (easy to resize, imprecise gap) vs solid rectangular dies (tighter thickness control). Apply-and-bake is repeated with different dies. A die with flat-wall protrusions counteracts corner thinning — [US9330817B2](https://patents.google.com/patent/US9330817B2/en)
- **Cure-state metrology:** the degree of cure of PI films (imidisation releases water) is "an important index" but hard to measure. Sumitomo developed a proprietary evolved-gas analysis–MS method to quantify it and studied the PI/Cu interface by HAXPES — [SEI TR No. 90 (2020), "Analysis Technologies for Quality Improvement in Magnet Wires of Electrified Vehicles"](https://global-sei.com/technology/tr/bn90/pdf/E90-05.pdf)
- **Historical alternative** (GE US3850773A, 1974): electrocoating of polyamic-acid salt deposits about 1 mil (~25 µm) or more per pass (examples 0.4–2 mil). Bath at 5–60 °C; stepped cure tower from 40 to 450 °C (example 150–160 / 220 / 250–270 °C, 1–4 min); voltage 0–350 V. The patent also criticises dip coating for solvent carry-out and ≥5 passes. E-coat is covered by another researcher — [US3850773A](https://patents.google.com/patent/US3850773A/en)

#### Solvents / regulation
- REACH Annex XVII **entry 71**, NMP (CAS 872-50-4): applies to substances and mixtures with **≥0.3 %** NMP. Worker DNELs are **14.4 mg/m³ inhalation and 4.8 mg/kg/day dermal**. It applies after 9 May 2020 generally, and **"from 9 May 2024"** for use "as a solvent or reactant in the process of coating wires" — [Commission Regulation (EU) 2018/588, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2018/588/oj)
- A trade press confirmation (2020; older) gives the same threshold and DNELs and lists wire coatings among NMP uses — [European Coatings](https://www.european-coatings.com/articles/2020/nmp-restriction-to-take-effect-soon)
- NMP-free enamel R&D at ELANTAS Europe / Univ. Camerino (2022):
  - Cyrene turned out to be a "bad solvent" for both PAI and PAA.
  - NFM gave PAI with good film aspect, but the molecular weight was too low and all jerk tests failed.
  - **MDPA (3-methoxy-N,N-dimethylpropionamide)** gave PI-enamelled wires "comparable to standard PIs". MDPA is already reported in the literature for PAI.
  - The thesis notes that NMP and DMF are both on the REACH restricted list.
  - — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)

### Inferences

#### Lab-scale application on a cut bare rectangular conductor (my synthesis; no published bench protocol was found)

| Method | How to do it | Main limitations for rectangular bars (sources) | Verdict |
|---|---|---|---|
| Dip coating with controlled vertical withdrawal | Repeat dip → flash → cure cycles at 3–5 µm per coat | Centre over-build vs thin edges on square/flat conductors, many passes ([US3850773A](https://patents.google.com/patent/US3850773A/en)); corners thinned by surface-curvature flow ([US9330817B2](https://patents.google.com/patent/US9330817B2/en)); gravity sag/tear-drop along the bar and at cut ends | Most practical; needs many thin coats and inversion of the bar between coats |
| Hand-pulled wiping die (bar drawn through a rectangular die or felt wiper) | Closest to industry | Die/conductor clearance and corner radius must match ([US9330817B2](https://patents.google.com/patent/US9330817B2/en)); short cut bars give entry/exit end effects | Feasible for 0.3–1 m bars; needs a custom die per conductor size |
| Brush | — | Uncontrolled thickness and corner coverage | Only for repair or masking; not for qualification |
| Spray | — | Corner coverage and solvent popping in thick coats | Possible for thin coats; poor reproducibility |
| Drawdown on flat Cu strip | — | Not a wire geometry, but gives flat coupons | Useful for εr / dielectric-strength / FTIR cure coupons |

Cure-related cautions:
- Industrial cure is seconds per pass at 500–700 °C air in a moving line ([Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)). A static lab oven cannot copy this. The supplier's technical data sheet cure window (stepped flash → cure → post-cure) has to be requested, and the degree of cure verified (FTIR imide bands, Tg, solvent rub), because under-cured PI/PAI changes εr, adhesion and hydrolysis behaviour ([SEI TR 90 E90-05](https://global-sei.com/technology/tr/bn90/pdf/E90-05.pdf)).
- Thick single coats will blister. Industry uses 2–5 µm coats precisely to avoid blow-holes and bare spots ([Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)).
- Too many cure cycles oxidise the copper and hurt adhesion (>20 passes per [US10418151B2](https://patents.google.com/patent/US10418151B2/en)). Clean/deoxidise and anneal the bar first, and consider an inert atmosphere.
- NMP-based PAI/PI enamels used in a lab must respect the 14.4 mg/m³ inhalation and 4.8 mg/kg/day dermal DNELs (fume hood, gloves) ([EUR-Lex 2018/588](https://eur-lex.europa.eu/eli/reg/2018/588/oj)).

#### Material–method matrix (values from sources cited in Q1–Q6; "lab feasibility" is my judgement)

| System | Thermal class | εr | Breakdown / PD data | Maturity | Lab feasibility on cut bar | Main hairpin risk | Examples |
|---|---|---|---|---|---|---|---|
| THEIC-PEsI sole coat | 180 ([IEC 60317-28](https://webstore.iec.ch/en/publication/96016)) / 200 ([IEC 60317-82](https://www.boutique.afnor.org/en-gb/standard/iec-60317822020/specifications-for-particular-types-of-winding-wires-part-82-polyesterimide/xs137256/248845)) | "low permittivity" (qualitative, [SEI 90](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)) | 130–160 V/µm ([Leone](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf)) | Series | Good (cresylic solvent, lower cure T) | Lower thermal class; heat shock ≤180 °C | Axalta THEIC-PEsI basecoats |
| PEsI (or PE) base + PAI overcoat | 200 ([IEC 60317-29](https://webstore.iec.ch/publication/1387); NEMA MW 36) | n/a | CR composite life 36.9 h fresh → 3.3 h after ATF ([US12159731B2](https://patents.google.com/patent/US12159731B2/en)) | Series; the main Chinese EV CR wire per the same patent | Moderate (two enamels, two cure windows) | Poor ATF resistance (same patent) | Essex Solutions GP/MR-200 ([Electrowind](https://www.electro-wind.com/superior-essex-130-312-heavy-gp-mr-200-mw-36-magnet-wire-24in)) |
| PAI sole coat | 220 ([IEC 60317-58](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-58%7Bed1.0%7Db.pdf)) | 4.3 ([SEI 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)); 4.55–4.59 ([Gao](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)) | 150–190 V/µm; elongation ~45 %; water uptake 4.5 % | Series (Japanese HEV/EV; Sumitomo AIW) | Moderate (NMP, high cure T, adhesion "++") | Higher εr, so lower PDIV; cost (Jufeng) | Hitachi Chemical HI-406 (in Furukawa patent); Voltatex 8300 topcoat |
| Nano-filled CR PAI (single/base/mid/top) | 200 (Voltatex 8536) | n/a | ~43× life (TiO2/SiO2 topcoat, [US6337442B1](https://patents.google.com/patent/US6337442B1/en)); 109–128 h at 155 °C, 20 kHz, 3 kV ([US12159731B2](https://patents.google.com/patent/US12159731B2/en)) | Series (enamel available) | Moderate (filler dispersion, die wear) | CR life <20 % after 10 % stretch ([2017 study](https://opaj.napstic.cn/periodicalArticle/0120171002033563)) | Axalta Voltatex 8536; Voltron 7700/8500; ELANTAS CORONA-PROTECT/ELAN-SHIELD |
| Aromatic PI (polyamic acid) | 240 ([IEC 60317-47](https://webstore.iec.ch/en/publication/95918)) | 3.0 ([SEI 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf)) | 1230 Vp at 60 µm, flat pair; elongation ~80 %; Tg 350 °C | Series (Sumitomo PIW rectangular) | Hard (imidisation ~500 °C line cure, water evolution, adhesion "++") | Cost; cure state | Sumitomo PIW; ELANTAS PI; Unitika U-Imide (patent) |
| Microcellular/foamed PI | n/a (PI base) | 2.2 (30 vol %) / 1.7 (50 vol %) | 1440 Vp at 60 µm; breakdown 10.8 kV | Development (2019–2020) | Not feasible by hand | Cell control, forming, ATF unknown | Sumitomo (dev.); Furukawa patent |

### Gaps
- No published lab-scale protocol (bench die/dip rig, cure schedule) for enamelling cut rectangular hairpin bars was found. The KIT "slot-die coater" hit is a battery-paste tool. The Padua deposition-modelling thesis is restricted.
- Supplier TDS cure schedules (e.g., ELANTAS PI, Pyre-ML, Voltatex 8536) are behind request forms and were not obtained.
- **Water-borne enamels:** searches returned only 1970s–80s patents on aqueous PEsI/PAI wire enamels (not opened in full). No current commercial water-borne hairpin enamel was found.
- **UV-curable enamels:** nothing relevant to hairpin wire was found.
- I found no source confirming whether NEP or DMAc-based wire enamels are commercially used post-2024. DMAc/DMF are flagged as REACH-restricted only in general terms in the thesis.

## Q6. Hairpin-specific performance: forming, adhesion, springback, stripping, ATF/hydrolysis, thermal class achieved, cost vs PEEK, typical PDIV

### Takeaway
- **Forming:** hairpin forming of PI-enamelled bars left PDIV/PDEV near straight-bar values but "significantly" lowered breakdown voltage. A 10 % stretch cut corona life of CR enamel by more than 80 %. PI's film elongation (~80 %) is roughly double that of PAI (~45 %), which matters for edgewise bends and twists.
- **Stripping:** laser stripping of PAI is fast (up to 13 cm²/s, average 7 cm²/s) and faster than PEEK (4 cm²/s).
- **ATF/oil:** standard PEsI/PAI composites lose most of their breakdown strength and corona life after ATF cycling, while sole-coat PAI and multilayer systems hold up better. Moisture-driven hydrolysis is the mechanism, and PI absorbs less water (3.0 % vs 4.5 %).
- **Typical PDIV of enamelled flat wire:** about 1.2–1.4 kVp for 60 µm PI/microcellular PI flat-to-flat at 25 °C, and 1.5–1.8 kVpk for 125–175 µm PI-FEP insulated flat wire at room temperature, dropping by about 0.2 kV at 180 °C.
- **Cost vs extruded PEEK:** no quantitative source was found.

### Cited Findings

#### Forming and mechanical behaviour
- Taylor, Hiziroglu, Foss (Kettering Univ.), IEEE conference paper, 2014 (IEEE Xplore doc. 6995774; older): polyimide-based enamel on rectangular copper formed into hairpins and tested in carbon powder. Average PDIV and PDEV of hairpin samples were close to unstrained straight conductors, but **breakdown voltages were significantly lower** than straight conductors. The abstract gives no numbers — [Kettering research profile](https://researchprofiles.kettering.edu/en/publications/electrical-discharge-in-enamel-insulated-hairpin-copper-conductor/)
- Stretching CR enamelled wire by 10 % left <20 % of its corona-resistance time; 15 % stretch kept >85 % of breakdown voltage — [EMCA 2017 abstract](https://opaj.napstic.cn/periodicalArticle/0120171002033563)
- Ultimate elongation of film: AIW (PAI) ~45 %, PIW (PI) ~80 %. Elastic modulus at 400 °C: 30 MPa vs 1000 MPa — [SEI TR No. 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- IEC 60317-58 (rectangular PAI) contains elongation, springiness, flexibility-and-adherence, heat-shock and abrasion clauses. Values were not accessible — [IEC 60317-58 preview](https://assets.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-58%7Bed1.0%7Db.pdf)
- Adherence is rated only "++" (acceptable) for PAI and PI vs "+++++" for PE/PVF — [Leone 2022](https://pubblicazioni.unicam.it/bitstream/11581/483506/1/30_05_2022%20PhD%20Thesis%20Ezio%20Leone.pdf). Sumitomo studies the PI/copper interface chemistry (HAXPES) to improve interfacial adhesion — [SEI TR No. 90 E90-05](https://global-sei.com/technology/tr/bn90/pdf/E90-05.pdf)
- All five of Jufeng's ATF/CR wire embodiments passed jerk (no peeling-off) and elongation (no cracking) tests, both fresh and after ATF exposure. The patent reports static friction coefficients of 0.025–0.033 for the embodiments vs 0.049 for the commercial composite and 0.045 for single PAI — [US12159731B2](https://patents.google.com/patent/US12159731B2/en)

#### Stripping before welding (TRUMPF whitepaper hosted by Charged EVs, 2021; older)
- Common hairpin insulations are **PAI, PEEK, and PAI with polyimide foil ("PAI+FEP")**. PEEK is a volume absorber; for PAI and PAI+FEP the first laser pass should carbonise the material to raise absorption — [TRUMPF whitepaper](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)
- Ideal short-pulse parameters (TruMicro 7070/7060): frequency >20 kHz, pulse overlap >40 %, line overlap >40 %, pulse energy >40 mJ. PAI removal rate is up to **13 cm²/s (average 7 cm²/s)** and PEEK **4 cm²/s** (TruMark). Laser processes are "between 40 and 80% faster than mechanical processes" — [TRUMPF whitepaper](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)

#### ATF / oil / hydrolysis
- **Jufeng ATF protocol:** sealed tubes of ATF, 8 cycles, each 25 → 155 °C at ~2 °C/min, 40 h at 155 °C, then −45 °C for 8 h. Commercial PEsI/PAI composite: breakdown 15.39 → 5.53 kV, corona life 36 h 52 min → 3 h 18 min. Single PAI: 15.52 → 10.82 kV and 109 h 36 min → 59 h 12 min — [US12159731B2](https://patents.google.com/patent/US12159731B2/en)
- 2,000 h high-temperature ATF immersion of impregnating resins, enamelled flat wires and aramid papers for oil-cooled motors. Water and air promote hot-oxygen ageing of ATF into acidic products that accelerate hydrolysis. Only enamelled flat wire "D" (unnamed) plus two resins and two papers showed excellent oil resistance. The abstract gives no temperature or numbers — [Insulating Materials 57(2) 60–64 (2024), DOI 10.16790/j.cnki.1009-9239.im.2024.02.008](https://castjournals.cast.org.cn/joweb/jycl/EN/1209927011296997871)
- Water absorption: PAI 4.5 % vs PI 3.0 % — [SEI TR No. 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)
- ELANTAS claims "special oil resistance" for its PI e-mobility enamels — [ELANTAS PI](https://www.elantas.com/en-br/stories/wire-enamels-pi/)

#### Thermal class achieved
- PEsI/PAI: 200 (IEC 60317-29); PAI: 220 (IEC 60317-58); PI: 240 (IEC 60317-47) — see Q1 sources. Sumitomo PIW passed 280 °C × 2000 h, whereas AIW failed 220 °C × 500 h in its durability test — [SEI TR No. 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf)

#### Typical PDIV values
- Rectangular PI, 60 µm per side, flat-to-flat pair, 60 Hz, 25 °C, 50 % RH: **1230 Vp**. Microcellular PI 60 µm: **1440 Vp**; 44 µm microcellular: 1230 Vp — [SEI TR No. 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf); [SEI TR No. 90](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)
- Gao et al. 2023, hairpin turn-to-turn models:
  - Samples: 2.48 × 2.78 mm² conductor, 0.8 mm corner radius, "enameled by Polyimide-FEP" at 125 µm and 175 µm (εr 3.5 at 25 °C). Test: 50 Hz AC, 25 V steps with 5 min holds, minimum of 10 repetitions.
  - Minimum PDIVpk: **1.51 kV (Dt 250 µm) and 1.83 kV (Dt 350 µm) at room temperature; 1.30 kV and 1.62 kV at 180 °C**.
  - Fitted design lines: PDIVpk = 0.0032·Dt + 0.71 (kV, Dt in µm) at RT and 0.0032·Dt + 0.5 at 180 °C.
  - — [Gao et al. 2023 postprint](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- Furukawa's rating scale for its (round) foamed wires counts PDIV ≥1.0 kVrms (1414 Vp) at 25 °C/50 Hz/10 pC as "particularly excellent" and states ≥100 µm insulation is generally needed — [US10418151B2](https://patents.google.com/patent/US10418151B2/en)
- The inverter surge peak at motor terminals may reach about 2× the inverter (DC) voltage — [SEI TR No. 88](https://global-sei.com/technology/tr/bn88/pdf/E88-10.pdf); [SEI TR No. 84 (84-17)](https://global-sei.com/technology/tr/bn84/pdf/84-17.pdf)

#### Cost / positioning vs PEEK
- PI wire is more expensive than PAI wire, though Sumitomo reduced the gap — [SEI TR No. 84](https://global-sei.com/technology/tr/bn84/pdf/84-19.pdf); [SEI TR No. 90](https://global-sei.com/technology/tr/bn90/pdf/E90-04.pdf)
- Japanese single-coat PAI is described as expensive relative to Chinese PEsI/PAI composites — [US12159731B2](https://patents.google.com/patent/US12159731B2/en)
- Essex Furukawa's "high-voltage rectangular magnet wire" is an enamelled rectangular wire over-coated with extruded PEEK (first place, powertrain category, 2017 Magna Innovation Award). Enamel-only and enamel+PEEK hybrids therefore coexist — [Magnetics Magazine](https://magneticsmag.com/sumitomo-advances-development-manufacturing-of-its-rectangular-magnet-wire-for-evs/)

### Inferences
- **Dakin estimates (25 °C, sea level, flat-to-flat)** using Sumitomo's form V = √2·163·(2t/εr)^0.46, which reproduces its measured 1230 Vp at 60 µm/εr 3.0 (calculated ≈1258 Vp). My calculations:

  | Film per side | PI, εr 3.0 | PAI, εr 4.3 | Microcellular PI, εr 2.2 |
  |---|---|---|---|
  | 100 µm | ≈1590 Vp | ≈1350 Vp | ≈1835 Vp |
  | 150 µm | ≈1920 Vp | ≈1625 Vp | — |

  PDIV falls at 180 °C. Gao's fit implies about −0.2 kV between RT and 180 °C.
- **Same quantities from Gao's empirical fit** (εr 3.5; derived from Dt 250–350 µm data only, so extrapolation is uncertain):

  | Film per side (Dt) | RT | 180 °C |
  |---|---|---|
  | 100 µm (200 µm) | ≈1.35 kVpk | ≈1.14 kVpk |
  | 150 µm (300 µm) | ≈1.67 kVpk | ≈1.46 kVpk |

- With an 800 V DC link and terminal surges up to ~2× (≈1.6 kVp), enamel-only builds of ~100 µm per side are not PD-free for the most stressed adjacent conductors (phase-to-phase / first turns) at hot-spot temperature. This is why 800 V hairpin designs use thicker or hybrid builds, low-k/foamed films, CR layers and/or extra phase separators. The actual turn-to-turn share depends on the winding's surge distribution, which needs a high-frequency model (as Gao et al. note).
- For the test plan: (a) test PDIV/RPDIV and V–t both before and after forming (edgewise/flatwise bend, twist at end turns) and after ATF ageing, since these are where enamels differ most; (b) PI is the strongest enamel-only candidate for forming and hydrolysis (elongation ~80 %, water uptake 3.0 %), PAI/PEsI+PAI are cheaper; (c) laser-strip compatibility is not a differentiator for PAI vs PI, but PEEK hybrids strip about 2× slower.

### Gaps
- No quantitative cost comparison ($/kg or $/m) between enamelled hairpin wire and extruded-PEEK hairpin wire was found.
- No numbers were found for edgewise-bending crack limits, springback, or adhesion (peel/jerk) of commercial enamelled hairpin wire. The Kettering 2014 paper is available to me only as an abstract. A 2014 Univ. of Windsor MSc thesis on wire-bending damage mechanisms appeared only as a search hit and was not opened.
- No hairpin ATF test with stated water content and post-ageing PDIV was found.
- No chemical-stripping data for PAI/PI hairpins were found. The mechanical-stripping risk of removing copper is stated only in a trade article that was not opened.
- The Gao "PI-FEP" insulation is called "enameled", but PI-FEP is commonly a film/tape system. Its classification as an enamel is uncertain, so those PDIV values may belong to the film/tape researcher's slice.
