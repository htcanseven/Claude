# New studies (Jan 2025 – Oct 2026) on ageing of winding insulation in ATF, e-fluids and other lubricating oils

Scope and method. Search cut-off: 19 Oct 2026. I used Crossref keyword and author queries filtered to 2024-10-01 onwards (about 1,900 records screened), plus web searches in English and Chinese, the RWTH IEM publication server, Chalmers research, DOAJ and Semantic Scholar. OpenAlex and part of Semantic Scholar were rate-limited. Before searching I read the References section of `reports/Hairpin insulation oil aging and corrosion review.md` and extracted every URL and DOI in `research_notes/Yağda hairpin izolasyon yaşlanması ve korozyon/`. Sources listed there are not repeated below unless a new version appeared.

Access tags:
- **[FULL TEXT]**: I read the whole document.
- **[ABSTRACT]**: I read only the abstract, from the publisher or a Crossref/Semantic Scholar/DOAJ record.
- **[METADATA]**: I saw only the title, authors and venue.
- **[SNIPPET]**: I saw only a search-engine summary, not the page itself. Treat these as low confidence.

All numbers come from the cited source. Values marked "≈ (read from chart)" are my own approximate readings of bar charts, because the source gives no table.

## 1. What new studies exist, and what were their specimens, materials, fluids, ageing set-ups, measurements and results?

### Takeaway
I found 7 new studies that age winding insulation in ATF, e-fluid, transmission oil or a water-based e-motor lubricant and re-measure electrical or chemical properties. Two are 2024 items the existing review missed. Two more test PDIV under hot ATF spray or in an oil-immersed winding model.
- **Most informative new datasets.** The Chalmers/Polestar technical report (2025) aged flat-wire formettes in transmission oil for 1000 h at 150 °C. PDIV fell from ≈2.6–3.8 kV to ≈2.0–2.4 kV and converged across insulation types. The RWTH/TotalEnergies IEMDC 2025 paper compared PEEK and PAI-overcoated ("Damid") twisted pairs and Nomex in water-based lubricants at 70 and 100 °C, with XPS showing lubricant elements and Cu entering PAI more deeply than PEEK.
- **Xi'an Jiaotong (2024, missing from the review).** It introduced a "dual-temperature" motorette test: current-heated conductors at 200 °C, ATF at 100 °C. ATF *vapour* was more damaging than submersion, and a lower oil temperature was more severe.
- **Dongfeng/Sichuan (CEIDP 2025).** Water in ATF drives PAI hydrolysis and oil acidification.
- **Bologna + Mitsubishi Electric (CEIDP 2025).** Confirms a 10–15 % PDIV reduction when ATF is leaked onto 180 °C rectangular conductors.

### Cited Findings

**Overview table (details for each row follow below)**

| # | Study (access) | Specimen | Insulation | Fluid | Ageing | Measurements | Headline result |
|---|---|---|---|---|---|---|---|
| N1 | Serdyuk & Hammarström, Chalmers TR 2025:1 [FULL TEXT] | Formettes (stack of flat wires in a stator slot) and motorettes (random-wound round-wire coil in a rotor-slot holder) | 4 flat wires (85–160 µm), 2 round wires (50 µm), 4 slot liners (150–500 µm), material types not named | "Transmission oil", not named | 150 °C in oil, 500 h and 1000 h, sealed Al containers; air 180 °C for 100 h | PDIV and PDEV, bipolar square wave, 1 kHz | Formette PDIV ≈2.6–3.8 → ≈2.0–2.4 kV after 1000 h (read from chart); systems converge |
| N2 | Peng et al., IEMDC 2025, RWTH + TotalEnergies [FULL TEXT] | Twisted pairs; Nomex strips | Damid (PAI overcoat) enamel; PEEK-coated wire; Nomex 0.25 mm | 2 water-based lubricants (WBL1, WBL2) | 70 and 100 °C, 8 weeks, sealed pots, 7 specimens per point | PDIV, C, tan δ, CTI, XPS (incl. depth profile), photos | Stable at 70 °C. At 100 °C, Damid enamel detached in WBL1 and PEEK failed in WBL1 after 6 weeks; PEEK stable in WBL2 |
| N3 | Li et al., CEIDP 2025, Dongfeng + Sichuan Univ. [ABSTRACT] | Not stated in abstract | PAI | ATF, with and without water | Not stated in abstract | PDIV, BDV, FTIR, oil chemistry | Water promotes PAI hydrolysis and raises oil acidity; C–H and P–O FTIR bands change |
| N4 | Sun et al., CEIDP 2024, XJTU [ABSTRACT] | Motorettes | Not stated | ATF | Dual-temperature: conductor at 200 °C by Joule heating, ATF at 100 °C; submerged vs vapour-exposed | Reliability (failures); ATF properties before and after | ATF vapour significantly reduced EIS reliability |
| N5 | Sun et al., CMD 2024, XJTU [ABSTRACT] | Motorettes (qualification method) | Not stated | Cooling oil (ATF) | Dual-temperature thermal endurance with electrical, mechanical and moisture sub-cycles; two oil temperatures | Not stated | Lower oil temperature "pose[s] more challenges" |
| N6 | Seri et al., CEIDP 2025, Bologna + Mitsubishi Electric [ABSTRACT] | Insulated rectangular conductors with a gap that simulates a hairpin end-winding | Not stated in abstract | ATF leaked onto the conductors | Conductors up to 180 °C (a spray/leak test, not ageing) | PDIV | PDIV reduced by 10–15 %; repeatability limited by the micrometric gap |
| N7 | Wu et al., 电工材料 2024(4), CRRC Zhuzhou [ABSTRACT] | Material specimens | Impregnating varnish, enamelled wire, slot insulation, sleeving | 2 ATF models | Not stated in abstract | Properties before and after | Epoxy-modified UP resin and a PPS–aramid paper composite resisted well; results differ by ATF model |

**N1. Chalmers technical report 2025:1 (with Polestar Performance AB; Swedish Energy Agency project P2022-01299) [FULL TEXT, 14 pp.]**
- **Citation and status.** Y. Serdyuk and T. Hammarström, "Development of an Environmental-Friendly Insulation System for the Next-Generation Sustainable Electric Drive Unit," Technical report 2025:1, Chalmers University of Technology, 2025. It went online in the repository on 12 Aug 2026 — [Chalmers record](https://research.chalmers.se/en/publication/553400); [PDF](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
- **Aim.** Find environmentally friendly and recyclable insulation for an EV drive unit. Materials came from DuPont, Solvay and Huntsman, but the report does not name products — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
- **Specimens and thicknesses** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - Flat wires: A 150 µm, B 160 µm, C 95 µm, D 85 µm.
  - Round wires: W1 and W2, 50 µm.
  - Slot liners: SL1 150 µm, SL2 180 µm, SL3 500 µm, SL4 500 µm.
  - Formette = a stack of flat wires in a stator slot. Motorette = a random-wound round-wire coil in a holder representing a rotor slot. A slot liner separates wires and slot in both.
  - Pairings: A+SL1, B+SL2, C+SL4, D+SL3; motorettes W1/W2 with SL1/SL2. Table 2 lists "W2+SL1" twice, while the figure legends show W2+SL2.
- **Ageing set-up** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - Oil ageing at 150 °C in aluminium containers filled with oil and sealed with 3M 363 high-temperature tape against evaporation, placed in ovens.
  - Formettes: 500 h (1 sample per system) and 1000 h (2 samples).
  - Motorettes: 500 h (2 samples).
  - Air control at 180 °C: formettes 100 h (2 samples), motorettes 100 h (3 samples).
  - The fluid is listed only as "transmission oil". Water content is not reported.
- **Measurement protocol** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - Bipolar rectangular voltage, 500 µs pulse duration, 1 kHz repetition.
  - Voltage raised to PD onset (PDIV), then to 1.1 × PDIV, then lowered to extinction (PDEV).
  - 4–5 tests per sample, reported as mean ± SD.
  - Measured before ageing, at about 1/3 and 2/3 of the period, and at the end.
  - Containers cooled naturally to room temperature (1–2 days per interruption) and stayed sealed. Each was opened only briefly to connect leads, which implies PDIV was measured with the sample still in its oil container.
  - The report does not say which insulation path (turn-to-turn or to slot) the PDIV represents.
- **Formettes, 500 h at 150 °C in oil (Fig. 5, ≈ read from chart)** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - PDIV before ageing: A ≈3.45, B ≈3.45, C ≈2.6, D ≈2.9 kV. After 500 h: all ≈2.2–2.35 kV.
  - PDEV before ageing: ≈2.1–2.8 kV. After 500 h: ≈1.6–1.75 kV.
  - Wires A and D showed a transient PDIV rise at 1/3 of the period.
  - The report says differences between systems are "most pronounced for fresh insulation" and "rather minor" at the end, and that SDs shrink after ageing.
- **Formettes, 1000 h at 150 °C in oil (Fig. 6, 8 systems, ≈ read from chart)** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - Thick wires A and B (150–160 µm): PDIV ≈3.5–3.8 kV fresh → ≈2.25–2.4 kV, about −35 to −40 %.
  - Thin wires C and D (85–95 µm): PDIV ≈2.65–3.15 kV fresh → ≈2.0–2.3 kV.
  - PDEV ≈2.3–3.15 kV fresh → ≈1.55–1.95 kV.
- **Motorettes, 500 h in oil (Fig. 7)** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - Fresh PDIV was "extremely high" for some samples (≈5–5.6 kV, read from chart), but fell to an average level (≈2 kV) after about 160 h. Later changes were small.
  - W1+SL1 and W2+SL1 even improved later. The authors call the cause "unclear".
- **Air control and imaging** — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf):
  - Motorettes at 180 °C for 100 h in air showed no significant PDIV or PDEV change. Formette air results were still being measured when the report was written.
  - Photos show colour change of the wire coatings and "especially oil".
  - The caption of Fig. 11 says "degraded oil … after ageing for 288 h at 180C", which is inconsistent with the 150 °C oil protocol in Table 2.
- **Authors' conclusions.** They could not single out a best system. They call for leakage current, dielectric loss and breakdown-withstand measurements, plus chemical and physical analyses — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)

**N2. Peng, Wu, El Bahi, Charrin, Thul, Hameyer, Steentjes (RWTH IEM + TotalEnergies OneTech), IEEE IEMDC 2025, pp. 123–128 [FULL TEXT]**
- **Citation.** "Compatibility Study of Water-Based Lubricants and Insulation Systems in Low-Voltage Electrical Machines for Automotive Applications," DOI 10.1109/IEMDC60492.2025.11060975 — [DOI](https://doi.org/10.1109/IEMDC60492.2025.11060975); [RWTH full text](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf). This is the follow-up to the Yang et al. 2023 IEMDC preliminary WBL paper already covered in the review.
- **Fluids.** Two TotalEnergies water-based lubricants. WBL1 and WBL2 have identical physical properties but different (confidential) additives. Properties at 40 °C, WBL vs ATF — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf):

  | Property at 40 °C | WBL | ATF |
  |---|---|---|
  | Viscosity (mm²/s) | 24.0 | 31.29 |
  | Density (kg/m³) | 1060 | 828.9 |
  | Thermal conductivity (W/m·K) | 0.384 | 0.1398 |
  | Specific heat (J/kg·K) | 3200 | 2110 |
- **Specimens.** Twisted pairs (per IEC 60317-0-1, as cited) of Damid wire (double-layer, PAI overcoat) and PEEK-coated wire. DuPont Nomex 0.25 mm cut into strips (for C, PDIV, tan δ) and squares (for CTI) — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Ageing.** Immersion in sealed heating pots at 70 °C ("upper-limit working temperature" of the coolant) and 100 °C (accelerated). Eight weeks, sampled at 1 day and 2, 4, 6 and 8 weeks, with 7 specimens per sampling point and type — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Measurements.** PDIV with the IEM impulse generator and a Stahl EW600.B; capacitance; tan δ; CTI per IEC 60112; XPS after 600 s surface etching, including depth profiles — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Wire results** — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf):
  - At 70 °C, both wires kept stable PDIV, C and tan δ for 8 weeks in both WBLs.
  - At 100 °C, the Damid enamel "completely dissolv[ed]" or detached from the copper after 6 weeks in WBL1, and peeled gradually in WBL2.
  - PEEK pairs in WBL1 failed after 6 weeks, while PEEK in WBL2 retained PDIV.
  - The text also says "Damid failed as early as the second week at 100 °C, while PEEK maintained performance until the sixth week". This conflicts internally with the "after six weeks" statement for Damid.
- **XPS results, WBL1 at 100 °C** — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf):

  | Element (at %) | Damid fresh | Damid 4 weeks | PEEK fresh | PEEK 6 weeks |
  |---|---|---|---|---|
  | C | 81.5 | 69.6 | 88.3 | 81 |
  | O | 10.0 | 23.4 | 11.7 | 16.1 |
  | N | 8.6 | 3.7 | — | — |

  - The text attributes the N drop to "6 weeks", but Table II shows no Damid data at 6 weeks because the coating had detached.
  - Lubricant elements (S, P, Si) were found inside the polymer.
  - Depth profiles show Cu decreasing with depth, like S and P. The authors conclude Cu migrates inward from outside rather than diffusing from the core.
  - Cu and WBL elements were undetectable at depth in PEEK but present in Damid, i.e. Damid is more permeable.
  - The authors suspect cut wire ends exposed to the fluid as the Cu source and say the test set-up should be improved.
- **Nomex results, 100 °C for 6 weeks** — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf):
  - PDIV stayed stable and CTI increased in both WBLs.
  - In WBL1, capacitance rose strongly, tan δ rose steadily, and samples were visibly discoloured and darkened.
  - WBL2 gave smaller changes.
  - Planned next step: spray WBL onto motorettes and end windings.

**N3. J. Li, Z. Li (Dongfeng Motor Corp. Technical Center), C. Yu, P. Wang (Sichuan University), CEIDP 2025, pp. 531–534 [ABSTRACT]**
- **Citation and design.** "Aging Effects of Automatic Transmission Fluid on Polyamideimide Insulation for Transportation Traction Motors," DOI 10.1109/CEIDP61707.2025.11218487. The study compares PAI ageing in ATF with and without water and analyses oil chemistry during ageing — [IEEE/Crossref](https://doi.org/10.1109/CEIDP61707.2025.11218487)
- **Results.** Water "facilitates the hydrolysis of PAI insulation, increases the acidity of the oil, and further accelerates material aging". FTIR shows "significant changes in the content of C-H and P-O bonds". Oxidation and hydrolysis driven by temperature and moisture are named as the primary causes. PDIV and BDV were measured "under different stress environments" — [Li et al. 2025](https://doi.org/10.1109/CEIDP61707.2025.11218487)
- **Missing from the abstract.** Specimen geometry, water level, temperature, duration and numeric results — [Li et al. 2025](https://doi.org/10.1109/CEIDP61707.2025.11218487)

**N4. Y. Sun, X. Zhang, C. Shi, Z. Zhang, Y. Xu (Xi'an Jiaotong University, State Key Lab of Electrical Insulation and Power Equipment), CEIDP 2024 (Auburn, 6–9 Oct 2024), pp. 1–5 [ABSTRACT]. A late-2024 item that is not in the existing review.**
- **Citation and design.** "Assessment of the Dual-Temperature Aging Method for the Electrical Insulation System of Direct Oil-Cooled Motors in Electric Vehicles," DOI 10.1109/CEIDP61745.2024.10907300. One motorette was submerged in ATF and another exposed only to ATF vapour. Both carried the same current and self-heated by Joule effect. ATF was held at 100 °C during the 200 °C ageing — [IEEE/Crossref](https://doi.org/10.1109/CEIDP61745.2024.10907300); [XJTU record](https://scholar.xjtu.edu.cn/en/publications/assessment-of-the-dual-temperature-aging-method-for-the-electrica/)
- **Results.** "The ATF vapor significantly reduced the reliability of the EIS." ATF properties were analysed before and after ageing and an ageing mechanism was proposed. The authors say the method "provides more comprehensive information than the traditional oven tests" — [Sun et al. CEIDP 2024](https://doi.org/10.1109/CEIDP61745.2024.10907300)

**N5. Y. Sun, C. Shi, Z. Zhang (XJTU), CMD 2024 (20 Oct 2024), pp. 755–758 [ABSTRACT]. A late-2024 item that is not in the existing review.**
- **Citation.** "The Oil Temperature Influence on the Dual-Temperature Aging for the Electrical Insulation Systems in Direct Oil-Cooled Motors of Electric Vehicles," DOI 10.23919/CMD62064.2024.10766334 — [IEEE/Crossref](https://doi.org/10.23919/CMD62064.2024.10766334)
- **Content.** It proposes a thermal-endurance qualification method based on dual-temperature thermal ageing, including "thermal, electrical, mechanical and moisture exposure". It studied two oil-ageing temperatures, and "the lower aging oil temperature pose[s] more challenges to the reliability of the insulation systems". The temperatures and numbers are not in the abstract — [Sun et al. CMD 2024](https://doi.org/10.23919/CMD62064.2024.10766334)
- **Context.** The abstract states there is "no established method" for long-term reliability evaluation of EIS in the presence of cooling oil — [Sun et al. CMD 2024](https://doi.org/10.23919/CMD62064.2024.10766334)

**N6. P. Seri, I. Iannarelli, F. Zecchin, A. Cavallini (Univ. Bologna), H. Ishikawa (Mitsubishi Electric Advanced Technology R&D, Amagasaki), CEIDP 2025, pp. 756–759 [ABSTRACT]. A new version of the spray result already covered via Martinez et al., WEMDCD 2025.**
- **Citation and design.** "Influence of Automatic Transmission Fluid on Partial Discharge Inception Voltage in Hairpin Stators for Electric Vehicles," DOI 10.1109/CEIDP61707.2025.11218465. "The oil was leaked on insulated rectangular conductors heated up to 180° C, keeping a gap between conductors to simulate the geometry of hairpin motor end-windings" — [IEEE/Crossref](https://doi.org/10.1109/CEIDP61707.2025.11218465)
- **Result.** "PDIV can be reduced by 10 %–15 %", with "repeatability issues … due to variations in the micrometric gap and its temperature dependence" — [Seri et al. 2025](https://doi.org/10.1109/CEIDP61707.2025.11218465). This wording supports the "reduced by 10–15 %" reading. The existing notes had flagged an ambiguity in the WEMDCD paper ("down to 10 %").

**N7. 武传刚, 刘济林, 薛长志, 李燕琴, 兰健, 陈红生 (CRRC Zhuzhou Electric Machinery; Hunan Key Lab of Electrical Insulation Technology), 电工材料 (Electrical Engineering Materials), 2024, no. 4, pp. 41–45 [ABSTRACT]. A 2024 item missing from the existing review.**
- **Citation.** "新能源汽车驱动电机关键绝缘材料耐不同型号ATF研究" (Resistance of key insulation materials of NEV drive motors to different ATF models), DOI 10.16786/j.cnki.1671-8887.eem.2024.04.010 — [NAPSTIC record](https://search.napstic.cn/literature/periodical/010dgcl202404010)
- **Design and result.** Impregnating varnish, enamelled wire, slot insulation and insulating sleeving were tested in two ATF models, with properties compared before and after. Epoxy-modified unsaturated polyester and a PPS–aramid fibre paper composite showed good resistance. "Under identical conditions" the same material behaved differently in different ATFs, so the authors recommend re-evaluating oil resistance whenever the ATF model changes. The record gives no temperatures, durations or values — [NAPSTIC record](https://search.napstic.cn/literature/periodical/010dgcl202404010)

**Partial discharge or breakdown with oil immersion or flow, and fluid-only dielectric data (new)**
- **Hayakawa et al. (Nagoya Univ. + Sinfonia Technology), ICDL 2025 [ABSTRACT]** — [DOI 10.1109/ICDL63868.2025.11068276](https://doi.org/10.1109/ICDL63868.2025.11068276):
  - Aim: use winding-cooling lubricating oil as insulation in electric-aircraft motors.
  - AC BDV of stationary oil was measured at moisture content of 8–52 % (as given in the abstract), with an electrode volume effect of 10⁰–10⁵ mm³. The volume effect dominates over the moisture effect.
  - Streaming oil (0–38 L/min, 23–65 °C, coaxial cylinders): BDV at 30 L/min was 24–42 % higher than stationary. At low flow, BDV decreased with temperature.
- **Journal version: Hayakawa et al., IEEE TDEI 2026, vol. pp. 2345–2352 [ABSTRACT]**, with an open-access copy in the Nagoya repository — [DOI 10.1109/TDEI.2026.3672099](https://doi.org/10.1109/TDEI.2026.3672099); [Nagoya repository](https://nagoya.repo.nii.ac.jp/records/2015031):
  - Adds cold-start and thermal ageing of the oil.
  - Streaming BDV is 24–55 % higher than stationary.
- **Umemoto, Tsuboi, Tanaka, Sato, Kumada (Univ. Tokyo + JAXA), IEEE EIC 2026 [ABSTRACT]** — [DOI 10.1109/EIC68788.2026.11642508](https://doi.org/10.1109/EIC68788.2026.11642508):
  - Aircraft lubricating oil as coolant and insulation: BDV in a sphere gap, and PD in an "oil-immersed arrow-pair winding model" from sea-level pressure to 40,000 ft.
  - BDV, PDIV and PDEV generally fall as pressure decreases.
  - Bubble generation *suppressed* the PDIV reduction under reduced pressure, which the authors attribute to dissolved gas diffusing into the bubbles.
- **Mulyana, Somantri, Anggio (Indonesia Univ. of Education), Research Square preprint 2025 [ABSTRACT; not peer-reviewed]** — [DOI 10.21203/rs.3.rs-6825877/v1](https://doi.org/10.21203/rs.3.rs-6825877/v1):
  - Needle-plane PD in TMO 10W-40 engine oil.
  - PDIV 2.02 kV across a 2 mm gap, i.e. 1.01 kV/mm.

**Adjacent new studies: moisture, dry hairpin ageing, PEEK in liquids, aramid in oil**
- **Dang, Ji, Zheng, Ren, Zhang (Tsinghua, Beijing Jiaotong), IEEE TDEI 2026, pp. 2098–2107 [ABSTRACT]** — [DOI 10.1109/TDEI.2025.3621167](https://doi.org/10.1109/TDEI.2025.3621167):
  - Accelerated hydrothermal ageing of twisted coil samples. Insulation parallel capacitance C_p was tracked online and offline, with TGA-FTIR.
  - "Chemical aging predominates in the early stage, while physical aging becomes more dominant later".
  - "Humidity affects the parameter values, though pure water is proved to have no significant long-term aging effect".
- **Miyaji, Otake (Mitsubishi Electric), Kikuchi (Univ. Hyogo), CEIDP 2025, pp. 523–526 [ABSTRACT]** — [DOI 10.1109/CEIDP61707.2025.11218556](https://doi.org/10.1109/CEIDP61707.2025.11218556):
  - RPDIV of twisted enamelled wires decreased as voltage frequency or humidity increased.
  - At higher frequency, the humidity effect was suppressed.
- **He, Tenbohlen, Beltle (Univ. Stuttgart), Energies 18(6):1376, 2025 [ABSTRACT]** — [DOI 10.3390/en18061376](https://doi.org/10.3390/en18061376):
  - Design-of-experiments electrical and thermal ageing of hairpin windings under PWM. No oil.
  - "RPDIV measurements alone cannot accurately predict the degree of ageing of hairpin windings".
  - Electrical and thermal stresses interact. Failure rate reflects this best.
- **Guana, Liu (Univ. Manchester), Jeschke, Walton (Siemens Energy), Electrical Materials and Applications, Jan 2026 [ABSTRACT; OA PDF blocked]** — [DOI 10.1049/ema3.70030](https://doi.org/10.1049/ema3.70030):
  - AC breakdown strength (BDS) of PEEK immersed in synthetic ester was higher than in mineral oil, attributed to the closer permittivity match.
  - BDS falls with thickness following a power law but is stable over 20–80 °C.
  - Breakdowns occurred mainly near the triple point.
- **Chen et al. (State Grid Gansu), ICEEPS 2026, pp. 626–629 [ABSTRACT]** — [DOI 10.1109/ICEEPS70377.2026.11662825](https://doi.org/10.1109/ICEEPS70377.2026.11662825):
  - Three-layer oil-impregnated Nomex (transformer context) under accelerated thermal ageing.
  - Average and maximum discharge magnitude and repetition rate generally increase with ageing.
  - The PD phase distribution spreads over the whole cycle.
- **Gerner et al. (KIT wbk + Carl Zeiss IMT/GOM), EPTS 2025, pp. 1–9 [ABSTRACT]** — [DOI 10.1109/EPTS67931.2025.11547393](https://doi.org/10.1109/EPTS67931.2025.11547393):
  - A methodology to measure insulation-layer thickness in the *bent zones* of hairpin coils.
  - Applied to compare bending techniques and die designs. No oil.

**Unresolved new item**
- **Z. Wang, F. Wang, J. Zhang, J. Gao, J. Li (Chongqing Univ.), S. Cheng, B. Chen (Naval Univ. of Engineering), IEEE TDEI 2026, early access [METADATA only]** — [DOI 10.1109/TDEI.2026.3735262](https://doi.org/10.1109/TDEI.2026.3735262):
  - "Varnish–Oil Compatibility and Degradation Mechanisms for Enhanced High-Temperature Electrical Insulation Performance".
  - No abstract was retrievable: IEEE Xplore returned a bot challenge and Semantic Scholar had none. Fluid, varnish and application (oil-cooled machine vs transformer) are unknown.

### Inferences
- **The evidence base is still small but has grown.** It went from about six academic oil-ageing sources to about 13. The newest contributors are Chinese OEM, academic and rail-supplier groups (Dongfeng/Sichuan, XJTU, CRRC Zhuzhou) and Chalmers/Polestar, alongside the established RWTH and Bologna groups. Mitsubishi Electric appears on two 2025 papers (N6 and the humidity RPDIV paper).
- **Three new methodological themes:**
  - Vapour or headspace exposure and dual-temperature (hot conductor, cooler oil) testing, which may be harsher than full submersion or isothermal oven immersion (N4, N5).
  - Water-driven hydrolysis of PAI and ingress of additive elements (S, P) into enamel (N2, N3).
  - PDIV *convergence* after oil ageing: the fresh ranking of insulation systems largely vanishes after 500–1000 h at 150 °C (N1).
- **The Chalmers air-vs-oil comparison is confounded.** It used 180 °C for 100 h in air versus 150 °C for 500–1000 h in oil, so the larger PDIV loss in oil cannot be attributed to the oil alone.

### Gaps
- **Paywalled full texts not read:** N3, N4, N5, N6, the varnish–oil TDEI paper, Umemoto, Dang and Miyaji. No numeric results, water contents, temperatures or durations are available beyond their abstracts. N3's numbers (PAI PDIV and BDV in wet vs dry ATF) would be the most valuable to obtain through institutional IEEE Xplore access.
- **No journal version found** of the XJTU dual-temperature work or the Dongfeng/Sichuan PAI work. CNKI is not reachable, and Chinese-journal DOIs (prefixes 10.16790, 10.16786) are not in Crossref, so 2025–2026 Chinese journal papers may have been missed.
- **No new SAE technical paper (2025–2026)** on magnet-wire or varnish compatibility with e-fluids was found. SAE Mobilus is poorly indexed by the search tools used.
- **Searches for new versions of some covered work were rate-limited (HTTP 429):** Zeynalova/Tre Tau, Pauli/Hameyer/RWTH, Kwak/Afton, García-Tuero, Naderiallaf. A new version of one of these could have been missed.
- **Already flagged in the existing notes, still unverified:** Alam 2025, "Impact of Cooling Oil on Partial Discharge and Insulation Reliability in Inverter-Fed EV Motors". The DOI is now known — [DOI 10.47760/cognizance.2025.v05i07.001](https://doi.org/10.47760/cognizance.2025.v05i07.001) — but the venue is low-tier.
- **Outside the window but missing from the existing review** (noted only, not reviewed in depth):
  - Gong, Li, Zhang, Xu (XJTU + CRRC Zhuzhou Institute), Insulating Materials 55(6):45–50, 2022 [ABSTRACT]. ATF with 0.5 vol % deionised water at 155 °C: enamelled round and rectangular wire and impregnating resin were compatible, while acrylic rubber degraded — [CAST journals](https://castjournals.cast.org.cn/joweb/jycl/EN/1210201124573934360)
  - An Afton trade article (Mar 2024) [SNIPPET]. In-house protocol: magnet wire aged in electrified transmission fluid at 150 °C with specified water for 48–120 h, followed by PD and BDV tests. Water above about 2,000 ppm "compromises insulation more markedly" — [EHV Mar 2024](https://ehv.mydigitalpublication.co.uk/march-2024/page-114)
  - Tuero et al. (2024 conference, Bournemouth) on the thermal and electrical compatibility of lubricants [SNIPPET]. Conductivity detects early ATF deterioration better than FT-IR — [Bournemouth record](https://staffprofiles.bournemouth.ac.uk/display/conference/391172)

## 2. Are there new data at several ageing temperatures (Arrhenius-type), on formed hairpins (bend crown, twist zone), or comparing application methods of one polymer?

### Takeaway
- **Temperature.** No new Arrhenius-type or lifetime-line dataset in oil was found. The new multi-temperature evidence is limited to two-level comparisons:
  - 70 vs 100 °C in water-based lubricants: stable vs failures.
  - Two oil temperatures in XJTU's dual-temperature motorette test, where the lower oil temperature was more severe.
  - Oil at 150 °C vs air at 180 °C (Chalmers).
- **Hairpins.** No study aged formed hairpins in oil and examined the bend crown or twist zone. The new hairpin-specific work is either dry (ageing, bend-zone thickness metrology) or a non-ageing ATF-leak PDIV test.
- **Application methods.** No study compared application methods of one polymer (extruded vs tube vs heat-shrink vs tape vs powder). The closest is a PEEK-coated vs PAI-overcoat enamel comparison in water-based lubricants.

### Cited Findings
- **Two temperatures, water-based lubricants.** At 70 °C, Damid (PAI) and PEEK twisted pairs and Nomex were stable for 8 weeks. At 100 °C, the Damid enamel detached in WBL1 within 6 weeks and PEEK failed in WBL1 after 6 weeks. This is a threshold-like temperature effect, not an Arrhenius series — [Peng et al. IEMDC 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Two oil temperatures, dual-temperature test.** The lower oil temperature was more challenging for insulation reliability. Values are not in the abstract — [Sun et al. CMD 2024](https://doi.org/10.23919/CMD62064.2024.10766334)
- **Dual-temperature conditions.** Conductor 200 °C (Joule-heated) and ATF 100 °C; vapour exposure was worse than submersion — [Sun et al. CEIDP 2024](https://doi.org/10.1109/CEIDP61745.2024.10907300)
- **Single oil temperature (150 °C) at two durations**, with an air control at a different temperature (180 °C, 100 h). Oil at 150 °C reduced formette PDIV by about 20–40 % (≈, read from chart). Air at 180 °C for 100 h did not significantly change motorette PDIV — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
- **Fluid-only temperature dependence.** Lubricating-oil BDV at low flow decreased with temperature over 23–65 °C — [Hayakawa et al. ICDL 2025](https://doi.org/10.1109/ICDL63868.2025.11068276). PEEK breakdown strength in synthetic ester was stable over 20–80 °C — [Guana et al. 2026](https://doi.org/10.1049/ema3.70030)
- **Hairpin geometry with ATF, no ageing.** Rectangular conductors at up to 180 °C with an end-winding-like gap, ATF leaked on: PDIV −10 to −15 % — [Seri et al. CEIDP 2025](https://doi.org/10.1109/CEIDP61707.2025.11218465)
- **Hairpin ageing, dry.** DoE electrical and thermal ageing under PWM; RPDIV does not track ageing degree — [He et al., Energies 2025](https://doi.org/10.3390/en18061376)
- **Bend-zone metrology, dry.** Insulation-thickness measurement in bent zones of hairpins, comparing bending techniques and die designs — [Gerner et al. EPTS 2025](https://doi.org/10.1109/EPTS67931.2025.11547393)
- **Dry phase-to-phase PDIV modelling of hairpin machines** [METADATA only] — [Diagnostika 2026, DOI 10.1109/DIAGNOSTIKA70212.2026.11717818](https://doi.org/10.1109/DIAGNOSTIKA70212.2026.11717818); [ICD 2026, DOI 10.1109/ICD64907.2026.11665346](https://doi.org/10.1109/ICD64907.2026.11665346)
- **Closest to an application-method or material comparison:**
  - PEEK-coated wire vs PAI-overcoated (Damid) enamelled wire, in the same water-based-lubricant protocol. PEEK showed lower permeability by XPS and kept its PDIV in WBL2 at 100 °C. It still failed in WBL1 at 100 °C — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
  - Four flat-wire insulations of different build (85–160 µm, types not named) with four slot liners, in one oil protocol — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
  - Varnish, wire, slot insulation and sleeving categories in two ATFs — [Wu et al. 2024](https://search.napstic.cn/literature/periodical/010dgcl202404010)

### Inferences
- The claim in the existing review — no Arrhenius dataset, no oil-aged hairpin bend or twist data, and no single-polymer application-method comparison in oil — still holds as of Oct 2026. A study with ≥2 ageing temperatures on formed hairpins, comparing coating routes, would remain novel.
- The PEEK-vs-PAI contrast in water-based lubricants is not directly transferable to hydrocarbon e-fluids, because water-driven hydrolysis dominates there. It does, however, give the first XPS-depth evidence that additive elements and Cu penetrate PAI enamel more deeply than PEEK.

### Gaps
- No 2025–2026 data were found for parylene, epoxy powder coating, PEEK tube or PEEK heat-shrink, polyimide (Kapton) or FEP tape, or extruded PPS/PFA on conductors in ATF or e-fluid.
- Chalmers' flat-wire types A–D are not identified, so the report cannot be used for a material- or method-specific comparison.

## 3. Are there new review articles or surveys on insulation for oil-cooled electric machines?

### Takeaway
No new dedicated review (2025 – Oct 2026) on insulation for oil-cooled machines was found beyond the two the existing review already covers: Martinez et al., WEMDCD 2025, and Gao, Tan and Li, Frontiers in Mechanical Engineering 2026. Newer survey-type material is limited to:
- the problem statements in conference papers (XJTU: "no established method");
- Chinese trade articles and a government project list that name oil compatibility together with PDIV and corona resistance as joint qualification targets (search snippets only).

### Cited Findings
- **XJTU problem statement.** "Currently, there is no established methods for evaluating the long-term reliability of electrical insulation systems for drive motors in the presence of cooling oil" — [Sun et al. CMD 2024](https://doi.org/10.23919/CMD62064.2024.10766334)
- **RWTH/TotalEnergies.** They cite only the Afton/Lubrizol-led "Lubricant concepts for electrified vehicle transmissions and axles" (Tribology Online) as a broad overview, and call for tests under realistic spray or motorette conditions — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Chalmers.** The report says a literature survey and market analysis preceded material selection, but it does not present them — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
- **Chinese industry, 2026 [SNIPPET].** Drive-motor insulation validation is said to be expanding to PDIV, corona resistance, thermal ageing and oil ageing, and the article cites a 2026 IEEE TTE FE-based PD prediction model for flat-wire motors — [AI汽车网 2026](https://auto.jgvogel.cn/c1600023.shtml)
- **Chinese industry, 2025 [SNIPPET].** Two technical routes are named for 800 V flat-wire motors: thick enamel, or thin enamel plus PEEK film wrap — [OFweek, Mar 2025](https://instrument.ofweek.com/2025-03/ART-8320087-8500-30658794.html)
- **Chinese government project list, start Jan 2025 [SNIPPET].** It targets corona-resistant, cooling-oil-compatible insulation materials and a motor-to-ground PDIV of at least 1.2 kV — [project list PDF](https://www.baicebao.com/upload/portal/20241212/8e56f2be2f91812d062991d486e997b5.pdf)
- **The covered Martinez et al. 2025 paper** is now also in the Mondragon repository; there is no new content — [Mondragon record](https://research.mondragon.edu/documentos/6969ebf59e41074a913018ea)

### Inferences
- The field still lacks a peer-reviewed review of oil-ageing protocols for e-motor insulation. The planned study's literature section can claim this gap with the caveat that CNKI and SAE were not fully searchable.

### Gaps
- The three Chinese trade and project sources were not opened, so treat them as low confidence.
- An IEEE TTE 2026 PD-prediction paper for flat-wire motors is mentioned in the AI汽车网 snippet, but I did not identify or verify it.

## 4. What do the new findings imply for a study that will age several insulation technologies on rectangular/hairpin copper conductors in oil, with before/after electrical measurements and high-resolution imaging?

### Takeaway
The new work suggests seven design choices. Treat these as recommendations, not established practice.
- Control and report the exposure *phase* (immersed vs vapour or headspace).
- Control and report the water content and acidity of the oil.
- Seal or mask cut conductor ends.
- Use more replicates and intermediate read-outs, because PDIV converges and can move non-monotonically.
- Pair PDIV with C, tan δ, IR or leakage current and BDV, plus FTIR or XPS, because PDIV alone is insensitive.
- Run an air control at the *same* temperature and duration.
- Photograph the oil and the conductor ends as well as the insulation.

### Cited Findings
- **Vapour exposure can be harsher than submersion.** A motorette exposed to ATF vapour lost reliability more than a submerged one (200 °C conductor, 100 °C ATF) — [Sun et al. CEIDP 2024](https://doi.org/10.1109/CEIDP61745.2024.10907300)
- **Isothermal immersion may not be worst case.** A lower oil temperature in dual-temperature ageing was more severe — [Sun et al. CMD 2024](https://doi.org/10.23919/CMD62064.2024.10766334)
- **Water drives PAI degradation.** Water in ATF promotes PAI hydrolysis and oil acidity, and FTIR shows changes in C–H and P–O bands — [Li et al. CEIDP 2025](https://doi.org/10.1109/CEIDP61707.2025.11218487). Humidity alone shifts RPDIV and C_p — [Miyaji et al. 2025](https://doi.org/10.1109/CEIDP61707.2025.11218556); [Dang et al. 2026](https://doi.org/10.1109/TDEI.2025.3621167)
- **Cut ends are an artefact path.** Cu and lubricant elements were found inside the enamel, possibly entering through cut wire ends exposed to the fluid. The authors recommend improving the set-up — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Replicates and convergence:**
  - Chalmers used 1–2 formettes per system and 4–5 PD tests per sample. Fresh differences between systems largely vanished after 500–1000 h at 150 °C in oil, and PDIV sometimes rose at 1/3 of the period before falling — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
  - RWTH used 7 specimens per sampling point and 5 sampling points over 8 weeks — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **PDIV alone is insufficient:**
  - In WBL1 at 100 °C, Nomex PDIV stayed stable while capacitance rose strongly and tan δ rose steadily — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
  - RPDIV cannot predict the ageing degree of hairpin windings — [He et al. 2025](https://doi.org/10.3390/en18061376)
  - The Chalmers authors call for leakage current, dielectric loss and breakdown-withstand measurements — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
- **The wetting and measurement state changes PDIV:**
  - Hot ATF leaked onto 180 °C conductors lowered PDIV by 10–15 % — [Seri et al. 2025](https://doi.org/10.1109/CEIDP61707.2025.11218465)
  - Chalmers measured at room temperature inside the sealed oil containers after 1–2 days of cooling — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
  - In oil-immersed winding models, dissolved gas and bubbles changed PDIV behaviour — [Umemoto et al. 2026](https://doi.org/10.1109/EIC68788.2026.11642508)
  - Temperature and relative humidity influence PD in twisted pairs and motors [METADATA only] — [Toscani et al., IEEE Access 2026](https://doi.org/10.1109/ACCESS.2026.3706390)
- **Fluid specificity.** The same insulation material performed differently in two ATF models under identical conditions — [Wu et al. 2024](https://search.napstic.cn/literature/periodical/010dgcl202404010). WBL1 and WBL2 had identical physical properties but different additives, and gave markedly different degradation — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
- **Visible changes are documented and worth imaging:**
  - Colour change of wire coatings and "especially oil" — [Chalmers TR 2025:1](https://research.chalmers.se/publication/553400/file/553400_Fulltext.pdf)
  - Enamel peeling and full detachment from the copper core; Nomex discolouration and darkening — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)
  - Bend-zone insulation thickness of hairpins can be measured with a dedicated metrology method — [Gerner et al. 2025](https://doi.org/10.1109/EPTS67931.2025.11547393)
- **PEEK is not immune.** PEEK twisted pairs failed in one water-based lubricant at 100 °C after 6 weeks, though they were stable in the other — [Peng et al. 2025](http://bib.iem.rwth-aachen.de/IEMpublications/2025HP_Compatibility.pdf)

### Inferences
These are recommendations derived from the findings above.
1. **Exposure phase.** Use fully submerged specimens with a defined, recorded headspace. If feasible, add a vapour or splash group, or at least partially immersed specimens, so that the liquid–vapour interface is imaged. If current-heating is possible, a hot-conductor/cooler-oil arm would mirror the XJTU dual-temperature method; otherwise state that isothermal immersion may not be the worst case.
2. **Water and chemistry.** Measure water (Karl Fischer) and acidity of the oil at start and end, and keep vessels sealed during read-outs as Chalmers did. Consider one wet-oil arm, e.g. the +0.5 vol % water of the CEEIA-type protocols already in the existing review, because water dominates PAI degradation.
3. **Conductor ends.** Encapsulate or keep cut ends and laser-stripped terminals out of the oil, or treat them as a separate imaged zone. Otherwise edge ingress, as seen by XPS in Peng et al., can confound coating-level results and corrosion images.
4. **Replication and schedule.** Plan at least about 5–7 specimens per technology and read-out, as RWTH did, rather than the 1–2 formettes Chalmers used. Include intermediate read-outs, because PDIV can rise and then fall, and rankings converge. Rank technologies on retained properties and degradation rate, not on fresh PDIV.
5. **Measurement set.** Pair non-destructive PDIV or RPDIV with C and tan δ (or dielectric spectroscopy) and IR or leakage current, add BDV on a sacrificial subset, and use FTIR or XPS on the coating surface. Record the wetting state (drained and blotted vs immersed), measurement temperature and RH for every read-out.
6. **Controls.** Run a dry or air control at the same temperature and duration as the oil arm. Chalmers' 180 °C/100 h air vs 150 °C/500–1000 h oil design cannot separate chemical from thermal effects.
7. **Imaging.** Photograph the oil as well (colour or darkening), along with coating colour, gloss, peeling or detachment, cut ends, and bend crowns or twist zones on formed hairpins. Consider bend-zone thickness metrology before and after ageing, in the spirit of Gerner et al. No published study has done oil ageing at bend crowns or twist zones, so this would be a novel contribution.
8. **Temperatures and fluid.** Use ≥2 ageing temperatures to detect threshold behaviour, which the 70 vs 100 °C water-based-lubricant results show can be abrupt. Name the exact fluid and batch, because results are fluid-specific.

### Gaps
- No new data say whether PDIV measured on oil-wetted versus drained specimens after ageing gives systematically different rankings across insulation technologies.
- The fluids in the new studies (unnamed "transmission oil", unnamed ATFs, water-based lubricants) differ from a specific modern EV drive-unit e-fluid. None of the new studies used a named low-viscosity e-fluid with reported water content, so transferring their findings to the planned fluid is uncertain.
- Two peripheral new items on direct oil cooling of hairpin windings report no insulation ageing data in their abstracts:
  - Paredes et al., IEEE Access 2026, an oil-flooded hairpin motorette [ABSTRACT] — [DOI 10.1109/ACCESS.2026.3654831](https://doi.org/10.1109/ACCESS.2026.3654831)
  - Petrov et al. (LUT), IEEE TIA 2026, hollow hairpin winding with direct oil cooling [METADATA only] — [DOI 10.1109/TIA.2026.3711019](https://doi.org/10.1109/TIA.2026.3711019)
