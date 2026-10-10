# Wrapped insulation (film tapes, papers, mica, glass fibre) for bare rectangular copper hairpin conductors

Compiled 2026-10-10. Conventions used throughout:
- Short-time AC dielectric strengths (ASTM D149 or equivalent) depend strongly on thickness, electrode size and test conditions. They are screening numbers, not design values. Minimum (spec-limit) and typical values are labelled as such.
- "OLDER" marks documents dated 2015 or earlier, or undated documents that look older. Their values may still be valid, but check them against current datasheets.
- Builds are given as the increase in each conductor dimension (double-sided) unless stated otherwise.
- Nothing below was taken from search snippets alone. Anything not verified in an opened source is listed under Gaps.

## Key Question 1: Polyimide (PI) films and tapes (Kapton types, Kaneka Apical, UBE Upilex, PI pressure-sensitive tapes) and their use as wrapped rectangular magnet wire

### Takeaway
Heat-sealable PI/fluoropolymer composite tapes are an established, standardised wrapped insulation for rectangular copper. The usual construction is a 25 µm Kapton HN, CRC or WR core with 2.5–12.7 µm of FEP or another fluoropolymer, helically wrapped once or twice and heat-sealed. It is covered by IEC 60317-44 (class 240) and NEMA MW-62C, and it is in series production for rail traction, industrial, wind and ESP motors. Corona-resistant versions are the relevant candidates for SiC-driven 400–800 V machines: Kapton 100CRC film, 150FCRC019 heat-sealable tape, the e-mobility-targeted Kapton ECRC (2020) and Kaneka Apical CR. Since November 2025 Kapton belongs to Qnity Electronics (the DuPont electronics spin-off). I found no evidence of series EV hairpin production with PI-tape-wrapped conductors.

### Cited Findings

#### Ownership and supply status (2026)
- DuPont's Kapton product pages (e.g., dupont.com/electronics-industrial/kapton-fcrc.html) now return HTTP 301 redirects to qnityelectronics.com, and the Kapton FCRC page is Qnity-branded. Its technical documents are gated behind a "secured content from DuPont" sign-in — [Qnity Kapton FCRC page](https://www.qnityelectronics.com/kapton-fcrc.html)
- Qnity Electronics was formed in December 2024 to own DuPont's electronics division. DuPont completed the spin-off in November 2025, and "Kapton is a brand of the company". The Interconnect Solutions segment was 44 % of 2025 revenue — [Wikipedia: Qnity Electronics](https://en.wikipedia.org/wiki/Qnity_Electronics)

#### Kapton HN (base film), typical and minimum values
- HN is available in 30 (7.5 µm), 50 (12.7 µm), 100 (25.4 µm), 200 (50.8 µm), 300 (76.2 µm) and 500 (127 µm) gauges. 75 (19.1 µm) and 400 (102 µm) are available on request — [DuPont Kapton General Specifications H-38479-9, 03/2012 (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf)
- The motor/magnet-wire bulletin lists standard HN thicknesses of 25, 50, 75 and 125 µm. CRC is listed in 25 and 50 µm and WR (water-resistant) in 25 µm. Kapton is "routinely used in laminations with … Nomex paper or mica, as well as in pressure-sensitive adhesive tape" — [DuPont Kapton Motor & Magnet Wire Technical Bulletin H-29423-4, 11/2014 (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- Typical HN dielectric strength at 60 Hz with 6.4 mm electrodes: 25 µm 303 kV/mm (7700 V/mil), 50 µm 240 kV/mm, 75 µm 205 kV/mm, 125 µm 154 kV/mm.
  - εr at 1 kHz: 3.4 (25 and 50 µm), 3.5 (75 and 125 µm).
  - Dissipation factor (DF): 0.0018–0.0026.
  - Volume resistivity: 1.0–1.5 × 10^17 Ω·cm.
  - Source: [Kapton Summary of Properties H-38492-2 (PDF created 2000, OLDER)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf)
- Other typical HN properties (25 µm): no melting point; second-order transition (taken as Tg) at 360–410 °C; thermal conductivity 0.12 W/m·K; CTE 20 ppm/°C; UL94 V-0; tensile 231 MPa; elongation 72 %. The summary states "there are no known organic solvents for the film" — [Kapton Summary of Properties (OLDER)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf)
- HN specification minima (ASTM D149): 12.7 µm 118 kV/mm, 25.4 µm 236 kV/mm, 50.8 µm 197 kV/mm, 76.2 µm 177 kV/mm, 127 µm 118 kV/mm.
  - Maximum εr at 1 kHz: 3.9–4.0. Maximum DF: 0.0036.
  - Maximum moisture absorption (24 h immersion): 4.0 %.
  - 100HN thickness tolerance: 21.6–29.2 µm.
  - Source: [Kapton General Specifications (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf)
- UL (file E39505) gives Kapton a thermal index of 220–240 °C for electrical properties and 200–220 °C for mechanical properties. The film must keep ≥10 % elongation after 2 h at 400 °C — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- Hydrolysis: "Continuous exposure to hot water can affect the tensile strength, elongation, and dielectric strength of standard Kapton HN". Kapton WR was developed for applications where hydrolytic stability matters — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)

#### Heat-sealable magnet-wire grades (FN, FWN, FWR, PRN, PRT, XP, FCRC)
- DuPont's description of the method: "Heat-sealable Kapton films are used as primary insulation on magnet wire. These films are coated with or laminated to a fluoropolymer which acts as a high temperature adhesive. The film is applied in tape form by helically wrapping it over and heat-sealing it to the conductor and itself."
  - The heat-sealable types are FN, FCRC, FWN, FWR, PRN, PRT and XP.
  - Constructions (fluoropolymer / core / fluoropolymer):
    - 120FWN616B: 3.8/25/3.8 µm
    - 150FN019, 150FWN019, 150XP019: 25 µm HN + 12.7 µm on one side
    - 150PRN411: 10/25/2.5 µm
    - 200FN919: 12.7/25/12.7 µm
    - 250FN029: 50 µm HN + 12.7 µm
    - 300FN929: 12.7/50/12.7 µm
    - 150FCRC019: 25 µm CRC + 12.7 µm
    - 150FWR019: 25 µm WR + 12.7 µm
    - 200FWR919 and 200PRT919: 12.7/25/12.7 µm (both listed under the Kapton WR core group)
  - Source: [Magnet Wire Bulletin H-29423-4 (2014, OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- FN nomenclature: in the three-digit code, the middle digit is the base Kapton thickness in mils. The first and third digits are the FEP coating thickness on each side, with "9" = 12.7 µm (0.5 mil) and "6" = 2.54 µm (0.1 mil). Example: 120FN616 is 2.54 µm FEP / 25.4 µm HN / 2.54 µm FEP.
  - Other listed types: 100FN099, 150FN999, 200FN011, 300FN021, 400FN022, 400FN031, 500FN131 and 600FN051.
  - Source: [Kapton Summary of Properties (OLDER)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf)
- Bulletin minima (ASTM D149, 6.4 mm electrodes) for the magnet-wire composites, as minimum dielectric strength / minimum elongation:

  | Grade | Min. dielectric strength | Min. elongation |
  |---|---|---|
  | 120FWN616B | 209 kV/mm | 60 % |
  | 150FN019 | 169 kV/mm | 60 % |
  | 150FCRC019 | 142 kV/mm | 55 % |
  | 150FWN019 | 173 kV/mm | 65 % |
  | 150FWR019 | 173 kV/mm | 45 % |
  | 150PRN411 | 169 kV/mm | 60 % |
  | 150XP019 | 150 kV/mm | 60 % |
  | 200FN919 | 142 kV/mm | 60 % |
  | 200PRT919 | 157 kV/mm | 50 % |
  | 200FWR919 | 142 kV/mm | 45 % |
  | 250FN029 | 122 kV/mm | 50 % |
  | 300FN929 | 3300 V/mil, printed as "(108)" kV/mm | 60 % |

  - Heat-seal peel minima (ASTM D5213) are about 500–800 g/in. Source: [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
  - Caveat: column assignments were reconstructed from the PDF text layout, so verify them in the PDF.
  - The bulletin's printed N/cm conversions look wrong. For example, "750 g/in (18.7 N/cm)": 750 g/in is about 2.9 N/cm (my conversion).
  - 3300 V/mil equals about 130 kV/mm, which conflicts with the printed 108 kV/mm. The 2012 General Specifications give 300FN929 a minimum of 2700 V/mil (106 kV/mm).
- Older FN minima (2012 General Specifications): 120FN616 165 kV/mm, 150FN019 146, 200FN919 126, 200FN011 126, 250FN029 108, 300FN021/300FN929 106, 400FN022/500FN131 87 kV/mm — [Kapton General Specifications (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf)
- Heat-seal test (seal-strength QC method, not a wire-line process window):
  - Seals made in a jaw sealer at 350 °C (662 °F), 20 psig (1.4 bar), 20 s dwell.
  - Minimum peel between coated sides: 700 g/in (2.7 N/cm), or 450 g/in for 120FN616.
  - Minimum peel FEP-to-copper (FEP side sealed to 25 µm copper foil): 300 g/in (1.2 N/cm).
  - Minimum HN–FEP bond (cold peel): 225 g/in.
  - Source: [Kapton General Specifications (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf)
- Typical FN electrical values (120FN616 / 150FN019 / 250FN029):
  - Dielectric strength: 272 / 197 / 197 kV/mm.
  - εr: 3.1 / 2.7 / 3.0. DF: 0.0015 / 0.0013 / 0.0013.
  - Elongation at 23 °C: 75 / 70 / 85 %.
  - Polyimide/FEP weight ratio: 80/20, 57/43, 73/27.
  - Moisture absorption at 50 % RH: 1.3 % (120FN616), 0.8 % (150FN019), 0.4 % (400FN022).
  - Source: [Kapton FN datasheet K-15347, 03/2006 (OLDER)](https://cshyde.com/Asset/Data%20Sheet%2018-__F%20Dupont%20Kapton%C2%AE%20FN%20Film.pdf)
- Kapton FWN (current Qnity page): "heat fusible composite insulation", bonds reliably to copper, with "enhanced abrasion resistance options" and "low friction for winding". Applications listed include traction motors (rail, auto, mining).
  - 120FWN616B: 33.0 µm, 252 kV/mm, εr 2.60, elongation 92 %.
  - 150FWN019: 38.1 µm, 142 kV/mm, εr 3.00, elongation 55 %.
  - UL RTI 240 °C electrical / 200 °C mechanical.
  - Source: [Qnity Kapton FWN](https://www.qnityelectronics.com/kapton-fwn.html)
- Kapton FWR: PI/FEP composite with "improved hydrolysis resistance compared to commonly used polyimide materials". Applications: traction motors, ESP motors, aerospace wire.
  - 150FWR019: 38.1 µm, 177 kV/mm, εr 2.70, elongation 60 %.
  - 200FWR919: listed as 63.5 µm (conflicts with the bulletin's 12.7/25/12.7 µm = 50.8 µm construction), 197 kV/mm, εr 2.70.
  - Source: [Qnity Kapton FWR](https://www.qnityelectronics.com/kapton-fwr.html)
- Kapton PRN (150PRN411): 25 µm HN core with two "high-melt-temperature fluoropolymer" layers of about 10 µm and 3 µm. Claimed operating temperature above 240 °C; 213 kV/mm; εr 3.40; elongation 88 %. Intended for high-temperature magnet wire, including traction motors — [Qnity Kapton PRN](https://www.qnityelectronics.com/kapton-prn.html)

#### Corona-resistant grades (CR/CRC, FCRC, ECRC)
- Kapton CRC "has been developed specifically to withstand the damaging effect of partial discharge" and has thermal conductivity higher than HN — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
  - CRC minima: 100CRC 236 kV/mm, εr 3.4; 200CRC 177 kV/mm, εr 4, volume resistivity 10^15 Ω·cm — same source.
- Kapton 100CRC (current page): homogeneous corona-resistant film, 25.4 µm, 256 kV/mm, εr 3.40 (1 kHz), elongation 65 %, UL RTI 240 °C electrical / 200 °C mechanical. Listed for AC inverter-duty motors and rail and automotive traction motors. Can be laminated with aramid paper or mica — [Qnity Kapton CRC](https://www.qnityelectronics.com/kapton-crc.html)
- Kapton FCRC (150FCRC019): 100CRC combined with heat-fusible FEP.
  - 38.1 µm, 173 kV/mm (typical), εr 3.40, elongation 79 %.
  - Marketed for magnet wire, traction motors (rail, auto, mining), wind and hydro generators, ESP motors, and aerospace and specialty wire. Features include "reduced thickness versus mica laminates".
  - The page lists UL RTI 130 °C (electrical and mechanical). This conflicts with the 240 °C RTI for 100CRC and the 220–240 °C index for Kapton generally. Verify it in UL iQ.
  - Source: [Qnity Kapton FCRC](https://www.qnityelectronics.com/kapton-fcrc.html)
- Kapton CR voltage endurance (third-party tape-maker datasheet citing DuPont): at 20 kV/mm (500 V/mil) AC 50 Hz, Kapton CR life is ">100,000 hr (11½ years)", compared with 200 h for Kapton HN.
  - The same 1K063CR tape is 1 mil Kapton CR with silicone adhesive, 0.063 ± 0.006 mm total thickness, 6 kV dielectric breakdown, rated to 220 °C. Its listed application is "traction machine manufacturing".
  - Source: [P. Leo 1K063CR datasheet, Rev. 2 ©2007 (OLDER)](https://pleo.com/wp-content/uploads/2024/02/1K063CR_EN.pdf)
- Kapton ECRC (announced 2020-11-19): a corona-resistant wire-insulation film for e-mobility traction motors.
  - In an ABB-led, Swedish Energy Agency-funded study with Chalmers University of Technology, it "increased the average life-time of the insulation by about 8 times" compared with non-corona-resistant Kapton FN.
  - It is "25 percent thinner" than FN.
  - Test conditions: 150–180 °C, 3.0 and 3.5 kV, high switching frequency / high dv/dt (no numerical dv/dt given).
  - Source: [Qnity blog (originally DuPont), 2020](https://www.qnityelectronics.com/blogs/kapton-polyimide-film-addresses-impact-of-higher-switching-frequency-and-faster-voltage-rise.html)
- History: DuPont developed Kapton CR in the 1990s and Kaneka developed Apical CR around 2005. Corona-resistant films "have been widely used" for turn insulation of inverter-fed traction motors — [Wang et al., CRRC Zhuzhou Electric, Insulating Materials 2023, 56(2)](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011)
- CRRC 2023 results for 25 µm corona-resistant films, imported vs domestic Chinese film (test standard T/CEEIA 438-2020):

  | Property | Requirement | Imported | Domestic |
  |---|---|---|---|
  | AC strength | ≥220 kV/mm | 308 kV/mm | 297 kV/mm |
  | εr (23 °C, 50 Hz) | 3.1–3.9 | 3.19 | 3.13 |
  | DF | ≤5.0 × 10⁻³ | 1.74 × 10⁻³ | 2.33 × 10⁻³ |
  | Elongation (MD/TD) | ≥40 % | 67/76 % | 119/119 % |
  | Corona life | ≥30 min | 31 min | 91 min |

  - Corona-life test: bipolar square wave, 20 kHz, 100 ns rise, 50 % duty, 2.0 kVp-p, room temperature.
  - The magnet wire used 0.038 mm corona-resistant film at 53 % overlap on a 2.5 × 6.3 mm conductor. Nominal double-sided build: 0.21 mm.
  - Source: [CRRC 2023](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011)
- CRRC 2023 wire results:

  | Test | Requirement | Imported wire | Domestic wire |
  |---|---|---|---|
  | Breakdown, wide-edge bend | ≥5 kV | 7.9–8.7 kV | 8.0–8.7 kV |
  | Breakdown, narrow-edge bend | ≥5 kV | 7.8–8.3 kV | 7.9–8.5 kV |
  | Breakdown after heat shock | ≥2.5 kV | 5.1–5.3 kV | 5.3–5.6 kV |
  | Stretch-adhesion loss length | ≤6.3 mm | 0.5 mm | 0.3 mm |

  - Heat shock: narrow-edge bend, then 10 cycles of 240 °C for 2 h.
  - Breakdown at the coil nose after coil forming was 6.0–8.7 kV.
  - PDIV fell as square-wave rise time shortened (values shown only in a figure).
  - Source: [CRRC 2023](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011)
- A peer-reviewed comparison point for PI-film corona life (2024): with 25 µm films, 2 kV, 15 kHz, 100 ns rise, room temperature:
  - Fluorene-modified PI: 6.1 min. Modified PI with 1.0 vol % aluminium sec-butoxide: 7.9 min ("2.19×" pure PI, which implies about 3.6 min for pure PI).
  - Source: [Zhang et al., Polymers 2024, 16(6):767](https://pmc.ncbi.nlm.nih.gov/articles/PMC10975545/)
- Self-adhesive Kapton CR tapes are marketed for e-mobility "at 900 V" and for 690–>1000 V wind/solar converters. The supplier cites ABB and Siemens studies showing higher discharge resistance than Kapton HN — [CMC Klebetechnik PD-resistant tapes page](https://www.cmc.de/en/teilentladungsfeste-klebebaender)

#### Thermally conductive Kapton MT
- Kapton MT: thermal conductivity about 0.46 W/m·K; εr 4.20; UL RTI 240 °C electrical / 200 °C mechanical.
  - 100MT 25.4 µm, 217 kV/mm. 150MT 38.1 µm, 201 kV/mm. 200MT 50.8 µm, 181 kV/mm. 300MT 76.2 µm, 161 kV/mm.
  - Elongation 80–100 %.
  - Applications listed are electronics/heat-sink pads and laminate slot liners. Motors and EVs are not mentioned.
  - Source: [Qnity Kapton MT](https://www.qnityelectronics.com/kapton-mt.html)
- A supplier article recommends Kapton MT+ (with Nomex 818–864) for 800 V hairpin slot-liner tubes — [CWIEME Berlin article, 2023-05-02](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)

#### Kaneka Apical and UBE Upilex
- Apical 50AV (12.7 µm), typical values:
  - Dielectric strength 9.5 kV/mil (about 374 kV/mm, my conversion).
  - εr 3.0 and DF 0.0030 at 1 kHz.
  - Elongation 104/100 % (MD/TD); tensile 293 MPa.
  - Water absorption 2.7 %.
  - Listed applications: motor/generator insulation, wire and cable insulation, pressure-sensitive tape.
  - Source: [Apical 50AV, Polymershapes sheet ©2023](https://polymerfilms.com/wp-content/uploads/2024/09/Apical50AV-FILM.pdf)
- Upilex-S grades: 12.5, 25, 50, 75 and 125 µm. Typical values:
  - 25S: 6.8 kV at 25 °C and at 200 °C (about 272 kV/mm, my calculation); εr 3.5 (25 °C) / 3.3 (200 °C) at 1 kHz; DF 0.0013.
  - 75S: 11 kV.
  - 25S mechanical: tensile 520 MPa; elongation 40 %; modulus 9.1 GPa.
  - Heat life 290 °C at 20,000 h (tensile criterion); thermal conductivity 0.29 W/m·K.
  - Water absorption 1.4 % (24 h immersion); insoluble in organic solvents.
  - Source: [UBE UPILEX-S catalog, 2022.04](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf)

#### PI pressure-sensitive-adhesive (PSA) tapes
- 3M 92: 25 µm PI backing with thermosetting silicone PSA, 76 µm total. Dielectric breakdown >7,500 V; elongation ≥55 %. UL-recognised up to 180 °C (UL 510, file E17385). Uses include "wrapping coils" — [3M Tape 92 data sheet, January 2013 (OLDER)](https://ca.electro-wind.com/web-files/3M%5CDatasheets%5C3M92.pdf)
- Kapton CR with silicone PSA: 63 µm total, 220 °C rating — [P. Leo 1K063CR (OLDER)](https://pleo.com/wp-content/uploads/2024/02/1K063CR_EN.pdf)

#### Standards, wire makers and applications for PI-tape-wrapped rectangular wire
- IEC 60317-44 (Ed. 1.1 = 1997 + A1:2010; stability date 2027): "Aromatic polyimide tape wrapped rectangular copper wire, class 240".
  - "The insulation consists of one or two wrappings of aromatic polyimide tape". The tape is "coated on one or both sides with a suitable adhesive, for instance, fluorinated ethylene propylene", and "after wrapping, the tape is heat-sealed to form a continuous and adherent sheath".
  - Class 240 requires a temperature index of 240 and a heat-shock temperature of at least 260 °C. NOTE: in Canada, Russia and the USA this product is assigned class 220.
  - Conductor range: width 2.00–16.00 mm, thickness 0.80–5.60 mm.
  - Ordering example: "60317-44 IEC 4,00 mm x 1,00 mm grade A2".
  - Sources: [IEC webstore 60317-44](https://webstore.iec.ch/publication/1424); [IEC 60317-44 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-44%7Bed1.1%7Db.pdf)
- The standard's test list includes min/max insulation increase (Tables 1–2), elongation, springiness, flexibility and adherence, heat shock, cut-through, abrasion, solvents, breakdown voltage (Table 4), continuity, temperature index, dissipation factor and pin-hole tests. The preview does not show the numeric table values — [IEC 60317-44 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-44%7Bed1.1%7Db.pdf)
- Von Roll (USA motor-repair brochure, undated) lists "Polyimide taped rectangular – Induction and radiant heat-fused polyimide film – 240 °C – NEMA-MW-62C". The same brochure lists mica-covered (Austravolt, 200 °C) and Daglas-glass-covered (Austraflex, 220 °C, MW-46C) rectangular wire, with rectangular sizes from 0.020 in to 0.700 in — [Von Roll "Insulating Systems for the Motor Repair Industry" (EIS-hosted)](https://media.eis-inc.com/m/da351a69383baeb1/original/PH22-77877_9.pdf)
- The DuPont bulletin lists Kapton uses in motors as "magnet wire, turn-to-turn, strand, coil, slot liner, and ground insulation" — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- Bruker-Spaleck (Kern-Liebers group) flat-wire brochure: lists only enamelled flat wire. Coatings range from PU V155 to polyimide W240 (≤240 °C); no tape-wrapped product appears — [Bruker-Spaleck "Lackisolierter Flachdraht"](https://cdn.kern-liebers.com/fileadmin/user_upload/TochterGesellschaften/Bruker-Spaleck/PDF/Bruker-Spaleck_Lackisolierter_Flachdraht.pdf)

### Inferences
- **Candidates for SiC/800 V hairpins.** For a test plan, the PI wraps that matter are:
  - Corona-resistant core plus FEP: 150FCRC019, or ECRC if obtainable.
  - Standard heat-sealable references: 120FN616 / 150FN019 / 120FWN616B as "non-CR" baselines.
  - Kapton HN or CRC plain film or PSA tape: easiest for a lab.
  
  The ECRC claim (8× life vs FN) and the CR claim (>100,000 h vs 200 h at 20 kV/mm) come from supplier sources, so independent PDIV and pulse-endurance tests on the wrapped bar are needed.
- **Choice of FEP side.**
  - One-sided FEP (e.g., 150FN019 / 150FCRC019) wrapped FEP-inward bonds FEP to copper. In the overlaps it bonds FEP to PI (the "Teflon-to-Kapton" peel).
  - Two-sided FEP (120FN616, 200FN919) gives FEP–FEP seals in the overlaps but leaves FEP on the outer surface.
  - This matters for varnish adhesion (see KQ5) and for εr: FEP-rich composites show εr 2.6–2.7 vs 3.4 for HN.
- **Lower εr helps PDIV.** At a given build, composites with more FEP (εr about 2.0 for FEP; 2.6–3.1 for FN/FWN composites) put more of the turn-to-turn voltage across the air gap less readily than εr 3.4–4.2 films (HN, CRC, MT). This is a qualitative series-capacitor argument that should be checked by PDIV measurements.
- **Forming.** Upilex-S has only 40 % elongation and is much stiffer (9.1 GPa) than Kapton (about 2.5 GPa, 65–92 % elongation for the composites). Kapton/FEP grades are therefore the more forming-tolerant PI choice for hairpin U-bends and twists.
- **Thermal class.** Class 240 (IEC) / 220 (US) for heat-sealed PI exceeds typical EV class 180–220 needs. The FEP adhesive (continuous service about 205 °C, melting 260–280 °C, see KQ2) is the thermally weakest constituent of the bond.

### Gaps
- No opened source documents series-production EV hairpin stators using PI-tape-wrapped conductors. Supplier pages list "traction motors (rail, auto, mining)", and ECRC targets e-mobility, but no OEM application is named.
- "Kapton FCR" (as distinct from FCRC): an older DuPont page titled "Kapton FCR Advanced Magnet Wire Insulation" exists, but it now redirects, and I could not open any FCR data. The current corona-resistant heat-sealable grade is 150FCRC019.
- The compositions of the XP and PRT coatings are not described in the opened sources. ECRC thickness, construction and datasheet values are not published openly (the Qnity documents are gated).
- Kaneka Apical heat-sealable FEP grades (named in Prospector listings) and Apical CR datasheet values: I could not open these. The Prospector pages returned 403.
- Saint-Gobain (Norton) heat-sealable PI tapes for magnet wire: the page returned 403, so its RTI could not be verified.
- PI tapes with acrylic adhesive: no datasheet was opened.
- The 0.21 mm build in the CRRC paper is larger than the simple geometric 2 × 2 × 38 µm = 0.152 mm. The paper does not explain the difference; overlap steps, tolerance or a possible enamel undercoat are not specified.
- NEMA MW 1000 itself was not accessible, so MW-62C (polyimide taped) is attested only by the Von Roll brochure. An Indian Railways RDSO specification reportedly requires one layer of Kapton 150FN019 on traction-motor rectangular conductors, but its PDF could not be opened (connection reset / HTTP 503).

## Key Question 2: Other films usable as tape (PEEK, PPS, PEN, PET, PEI, LCP, PTFE/FEP/PFA)

### Takeaway
Several high-performance films can be slit into tapes and wrapped, but none has a dedicated magnet-wire tape standard or product like PI/FEP. They are lab or prototype options for bare-conductor tests. Their values:
- PEEK (APTIV, 8–750 µm, about 270 kV/mm at 25 µm, εr 3.2–3.5, elongation >150 %, upper working temperature about 250 °C) is the most forming-tolerant high-temperature option.
- FEP (εr 2.0, 260 kV/mm at 25 µm, heat-sealable, continuous service to 205 °C) gives the lowest εr and is the natural heat-seal adhesive.
- PEN (Teonex: class F, RTI 180 °C electrical / 160 °C mechanical) and PET are thermally marginal for class 180–220 hairpins.
- PEI film (Ultem: Tg 217 °C, heat-sealable) is a possible thermoplastic "self-bonding" tape.
- I could not verify PPS (Torelina) and LCP (Vecstar) film data.

### Cited Findings
- **PEEK, Victrex APTIV 1000** (unfilled, semi-crystalline):
  - Recommended/available thickness 8–750 µm.
  - Dielectric strength (ASTM D149, 6.35 mm electrode): 270 kV/mm at 25 µm (6750 V), 190 kV/mm at 50 µm, 120 kV/mm at 125 µm, 70 kV/mm at 250 µm.
  - εr 3.5 and DF 0.002 at 10 MHz (50 µm).
  - Water absorption 0.040 % (equilibrium, 50 % RH).
  - Elongation >150 % in MD and TD (25–250 µm).
  - Tensile modulus 2.3–2.8 GPa.
  - Victrex claims "excellent radiation, hydrolysis and chemical resistance".
  - Source: [Victrex APTIV 1000 datasheet, rev. Nov 2023](https://www.victrex.com/-/media/ul-datasheet/aptiv-films-1000-series.pdf)
- **APTIV 1000 per distributor:** upper working temperature 250 °C; εr 3.2–3.3 (50 Hz–10 kHz); 190 kV/mm at 50 µm.
  - Water absorption 0.5 % equilibrium / 0.1–0.3 % in 24 h. This conflicts with Victrex's 0.040 %; conditions are probably different (immersion vs 50 % RH).
  - Source: [Goodfellow APTIV 1000 page](https://www.goodfellow.com/uk/victrex-aptiv-1000-peek-film-group)
- **PEN, Teonex Q51 (TC 00141):**
  - Temperature class F (155 °C); UL RTI 180 °C electrical / 160 °C mechanical; UL 746B working temperature 160–180 °C.
  - Thicknesses 12, 16, 25, 38, 50, 75, 100, 125, 188 and 250 µm, as roll or tape, including self-adhesive.
  - Dielectric strength 250 kV/mm (JIS C-2318); εr 3.0 and DF 0.003 at 60 Hz.
  - Melting point 269 °C; elongation 90 %; water absorption 0.3 %.
  - Developed "for … electrical motors … as slot and phase insulation".
  - Source: [Müller-Ahlhorn Teonex Q51 data sheet](https://www.mueller-ahlhorn.com/wp-content/uploads/2024/04/Teonex-Q51-TC-00141-ENG.pdf)
- **PET, Mylar** (DuPont Teijin bulletin):
  - Mylar A is available 23–500 µm; Mylar C 2.5–12 µm.
  - AC dielectric strength falls with thickness: 6 µm ">600 kV/mm", 350 µm "about 80 kV/mm" (50 Hz, 50 mm electrodes, 25 °C).
  - The bulletin says "Impregnation is required for insulation systems that are to be operated continuously at AC voltages above their corona threshold in air."
  - Source: [Mylar Electrical Properties bulletin (copy distributed 2023)](https://converting-tasm.pl/wp-content/uploads/2024/01/info-mylar-a-electrical-properties_ekotech_2023.pdf)
- **Comparison table** (UBE, citing Modern Plastics Encyclopedia):
  - εr / DF: Upilex-25S 3.5 / 0.0013; general polyimide 3.5 / 0.003; polyester 3.2 / 0.005; polysulfone 3.1 / 0.0008; PTFE 2.1 / 0.0002.
  - PTFE tensile 10–30 MPa, elongation 100–400 %.
  - Source: [UBE UPILEX-S catalog 2022](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf)
- **PEI, SABIC ULTEM 1000B natural film:**
  - Tg 217 °C (DMA); dielectric strength 6,400 V/mil (about 252 kV/mm, my conversion; the sheet labels it "@125 µm" while listing 25–50 µm gauges).
  - Water absorption 1.25 % (24 h immersion) / 0.48 % (50 % RH).
  - UL94 VTM-0.
  - The film "can be heat-sealed to a wide variety of materials".
  - Source: [SABIC ULTEM 1000B film datasheet ©2017 (OLDER)](https://polymerfilms.com/wp-content/uploads/2023/06/Polymerfilms-SABIC-ultem%E2%84%A2-1000b-natural-25-%C2%B5m-%E2%80%9350-%C2%B5m-film-datasheet.pdf)
- **FEP, Chemours Teflon FEP film:**
  - Gauges 12.5–500 µm. Type A general-purpose; Type C cementable on one side (25–125 µm); Type C-20 cementable on both sides.
  - Dielectric strength 260 kV/mm at 25 µm and 70 kV/mm at 0.5 mm (ASTM D149).
  - εr 2.0 (100 Hz–1 MHz) and 1.93–2.02 (−40 to 225 °C); DF 0.0002–0.0007.
  - Melting point 260–280 °C; continuous service −240 to 205 °C; zero-strength temperature 255 °C.
  - Tensile 21 MPa; elongation 300 %; thermal conductivity 0.195 W/m·K.
  - "Heat sealable … excellent hot-melt adhesive"; "superior anti-stick"; "non-wetting".
  - Source: [Chemours Teflon FEP film bulletin (Polymerfilms copy)](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)
- **Skived PTFE tape, 3M 5480:** 50 µm skived PTFE film with silicone PSA, 96 µm total. Temperature range −54 to 204 °C; elongation 140 %. It is a release/low-friction tape, and no dielectric value is given — [3M 5480 data sheet, Sept 2022](https://multimedia.3m.com/mws/media/1571419O/5480-ptfe-plastic-film-tape-data-sheet.pdf)
- **Cold flow:** a PD-resistant-tape supplier contrasts Kapton CR with "some fluoropolymer films" that "yield under pressure (cold flow)". It calls polyester and PEN "insufficient" for demanding PD uses — [CMC Klebetechnik](https://www.cmc.de/en/teilentladungsfeste-klebebaender)
- **Candidate wrap materials in a recent wire patent (Totoku, priority 2020, US grant 2026):** the tape-wrapped winding-wire patent lists PET, PEN, polyimide, polyamide, PPS, PEEK, PFA, ETFE and FEP as candidate insulators, with adhesive layers of 0.2–50 µm — [US12665103B2](https://patents.google.com/patent/US12665103B2/en)

### Inferences
- **Lab screening ranking for class ≥180 °C hairpin turns** (from the cited datasheets):
  1. PI/FEP (standardised).
  2. PEEK film tape: high elongation for bends and low moisture uptake. A bonding route is needed, either thermal fusion or an adhesive or varnish.
  3. FEP: low εr and heat-sealable, but low tensile strength (21 MPa) and cold-flow risk under slot pressure.
  4. PEI: Tg 217 °C, so its heat-seal capability makes it a possible thermoplastic binder layer.
  5. PEN (RTI 180 °C electrical / 160 °C mechanical).
  6. PET (lowest thermal capability), useful only as a cheap mechanical/method rehearsal tape.
- **PTFE/FEP outer surfaces** will resist bonding by impregnating varnish unless a cementable (surface-treated) type is used. This is relevant to both the impregnation and the ATF tests.

### Gaps
- **PPS (Toray Torelina) film:** I could not open any primary film datasheet. The Toray Malaysia product page returned 404, and other hits were moulding-compound data. Torelina's film thickness range, εr, dielectric strength and UL RTI remain unverified.
- **LCP (Kuraray Vecstar) film:** opened Kuraray pages give no numbers, and the 2018 leaflet URL returned 404. The breakdown, εr and melting-point values are unverified.
- **PFA film:** no datasheet opened.
- **PET (Mylar) UL thermal class/RTI:** not verified from an opened source.
- **PEEK film:** Tg, melting point and UL RTI were not given in the opened APTIV sources.
- **ULTEM film:** εr not given in the opened sheet.
- **No opened source** describes a commercial magnet wire made by wrapping PEEK, PPS, PEN, PEI, LCP or PTFE tape on rectangular copper. Extruded PEEK is a different method, covered by another researcher.

## Key Question 3: Papers and mica (aramid paper, Nomex–Kapton laminates, Nomex-wrapped wire, mica tapes, glass-fibre serving)

### Takeaway
- **Aramid paper.** Nomex 410 is now sold by Arclin; datasheet 04-2026 gives 0.05–0.76 mm, UL RTI 220 °C, 18–34 kV/mm and εr 1.6–3.7. It is a mature tape-wrap insulation for rectangular wire: Essex "double Nomex wrapped" rectangular, NEMA MW 60, class 220, 50 % lap. But it is porous, needs impregnation for PD-free operation, and is relatively thick.
- **Nomex 818** (formerly 418; 50 % mica) is explicitly marketed for "motor conductor and coil wrap" with better corona endurance than 410.
- **Mica tapes** (e.g., Von Roll Samicafilm, about 0.09 mm/tape) give the best PD resistance, but builds are 0.30–0.54 mm and bend radii are large. They suit HV form-wound machines, not EV hairpins.
- **Glass-fibre (Daglas) serving** (IEC 60317-31, TI 180; vendor class up to 220 °C) is a legacy option for field coils.

### Cited Findings
- **Nomex 410 (Arclin, 2026), electrical:**
  - Thickness range 0.05–0.76 mm (2–30 mil).
  - AC rapid-rise dielectric strength (50 mm electrodes): 18 kV/mm at 0.05 mm, 22 at 0.08, 28 at 0.13, 34 at 0.18, 33 at 0.25, 27 at 0.76 mm.
  - Full-wave impulse: 39–63 kV/mm.
  - εr at 60 Hz: 1.6 (0.05 mm), 1.6 (0.08), 2.4 (0.13), 2.7 (0.18–0.25), up to 3.7 (0.61–0.76 mm). DF (4–7) × 10⁻³.
  - Arclin recommends continuous stress in dry-type applications of no more than 1.6 kV/mm (40 V/mil) "to minimize the risk of partial discharges".
  - Source: [Arclin Nomex 410 TDS 04-2026](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf)
- **Nomex 410, mechanical and thermal:**
  - Density 0.72 g/cc (0.05 mm) to 1.13 g/cc; basis weight 41 g/m² at 0.05 mm.
  - MD elongation 10 % (0.05 mm) to 23 %; MD tensile 43 N/cm (0.05 mm) to 816 N/cm (0.76 mm).
  - UL RTI 220 °C (electrical and mechanical) for all thicknesses; UL94 V-0 from 0.13 mm. Arclin's UL file is E34739.
  - Compatible with "virtually all classes of electrical varnishes".
  - Nomex papers "have also recently been demonstrated as being the material of choice for insulating motors for electric vehicles, in large part due to demonstrated compatibility with fluids used in automotive applications such as automatic transmission fluids".
  - Partial discharge gradually erodes Nomex. Its voltage endurance is shown as better than polyester film (single 0.25 mm layers, 360 Hz).
  - Source: [Arclin Nomex 410 TDS 04-2026](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf)
- **Nomex 818** (Arclin datasheet 2025, posted 2026): "designed for high-voltage applications, including motor conductor and coil wrap".
  - Calendered aramid paper with about 50 % inorganic mica.
  - Thicknesses 0.08, 0.13, 0.15, 0.20 and 0.25 mm.
  - AC rapid-rise strength 28.1–39.3 kV/mm; impulse 63–67 kV/mm.
  - Dielectric constants are "essentially unchanged" from 23 to 250 °C.
  - Offers "increased voltage endurance compared to Nomex 410 when subjected to corona attack". Recommended continuous stress (transformers) ≤3.2 kV/mm.
  - Former Nomex 418 is identical to 818. Nomex 419 is no longer sold. Nomex 864 (mica-containing) is sold only for laminating with other sheets or films.
  - Source: [Arclin Nomex 818 TDS 2025](https://arclin.com/wp-content/uploads/2026/04/Arclin_Nomex_818_Technical_Data_Sheet_2025.pdf)
- **Nomex-wrapped rectangular wire (Essex, via distributor):** ".114 x .258 Double NOMEX Wrapped (DNX) Rectangular MW 60 Copper Magnet Wire, 220 °C".
  - Insulation: Nomex Type 410 "Aromatic Polyimide [sic] Paper", 50 % lap, Class R 220 °C.
  - Claim: retains "at least 300 V/mil dielectric breakdown strength and 50 % of its initial tensile strength after 10 years at 250 °C".
  - Uses: dry-type and oil-filled transformers, lifting magnets, form-wound coils.
  - Source: [Electro-Wind listing (Essex Furukawa product)](https://www.electro-wind.com/114-x-258-double-nomex-wrapped-dnx-rectangular-mw-60-copper-magnet-wire-220c-white-250-lb-24-reel-average-wght)
- **Nomex–Kapton laminates (NKN / NMN):** Politubes offers spiral-wound NKN (Nomex/Kapton/Nomex) and NMN (Nomex/Mylar/Nomex) hairpin slot tubes in 0.13 and 0.19 mm.
  - Claims: up to 12 kV; "UL system integration up to 220 °C"; for 800 V, Nomex 818–864 and Kapton MT+.
  - It argues that overlapped film seams are the PD weak point and that taped slot insulation is pushed out or displaced during hairpin insertion and bending. These are vendor claims.
  - Source: [CWIEME Berlin article, 2023-05-02](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)
- **Von Roll Samicafilm taped rectangular wire** (datasheet dated 24-04-2007, OLDER):
  - Construction: bare or enamelled rectangular Cu wrapped with SAMICA mica paper laminated to polyester film. "One or more layers … either butt-lapped or overlapped". Optional hot-melt B-stage coating for hot-press consolidation.
  - Conductor range: 2–20 mm × 0.8–6 mm, up to 100 mm², width/thickness ≤10:1.
  - Tape: 0.09 ± 0.02 mm thick, mica paper 50–75 g/m², PET film 23–30 µm, epoxy binder.
  - Insulation builds: 0.36 mm unpressed / 0.30 mm pressed for 2 butt-lapped tapes; 0.54 / 0.45 mm for 3 tapes.
  - Minimum breakdown: 3.5–7.0 kV straight; 2.0–6.0 kV after edgewise bend (6× width) or flatwise bend (4× thickness) plus heat shock (180 °C, 30 min).
  - Temperature index 155 (bare) / 180 (enamelled).
  - Applications: HV motors up to and above 13.8 kV, wind generators.
  - Source: [Von Roll Samicafilm datasheet 2007 (OLDER)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf)
- **Ownership:** Von Roll's former insulation-tape page (vonroll.com/en/electrical/innovative-insulation-tapes) now 301-redirects to ELANTAS. The ELANTAS page shows SAMICA mica paper and mica laminates but no conductor-tape details in the portion read — [ELANTAS innovative insulation tapes page](https://www.elantas.com/en/electrical/innovative-insulation-tapes)
- **Isovolta turn/conductor tapes:** the US Isovolta 437320 sheet (V.10/10, OLDER) lists companion products "Conductofel 2009 – Mica conductor tape", "342204 – Mica turn insulation – Glass backed" and "4902 – Mica turn insulation – film based".
  - The 437320 groundwall tape itself: 0.007 in (0.18 mm), 112 g/m² mica, 15 % resin, ≥425 V/mil (about 16.7 kV/mm), class F.
  - After VPI: 23–28 kV/mm (about 1 mm wall).
  - Source: [Isovolta 437320 datasheet (OLDER)](https://www.electro-wind.com/web-files/Isovolta%5CDatasheets%5C4373-tech.pdf)
- **Mica + corona-resistant PI hybrids (GE patents, expired):**
  - CR Kapton is "a DuPont polyimide film loaded with fumed aluminum oxide" and is used as a backing on mica paper / glass composite tape.
  - Mica paper "has low tensile strength and its flakes can shed during winding", so it is backed with glass fibre.
  - Stator bars use 7–16 half-lapped mica-tape layers.
  - Sources: [US5973269A (GE Canada, filed 1996)](https://patents.google.com/patent/US5973269A/en); [CA2231580 (GE Canada, filed 1998)](https://brevets-patents.ic.gc.ca/opic-cipo/cpd/eng/patent/2231580/summary.html)
- **Glass fibre:**
  - IEC 60317-31:2015 covers "glass fibre wound, resin or varnish impregnated, bare or enamelled rectangular copper winding wire, temperature index 180", width 2.0–16.0 mm × thickness 0.80–5.60 mm. The 2nd edition introduced "glass fibre coverings over grade 1 enamelled conductor". Stability date 2027 — [IEC webstore 60317-31:2015](https://webstore.iec.ch/publication/23565)
  - Von Roll's Austraflex: "Glass over enameled or bare rectangular conductor MW-46C … 220 °C … unique Daglas insulation for AC and DC field coils" — [Von Roll motor-repair brochure](https://media.eis-inc.com/m/da351a69383baeb1/original/PH22-77877_9.pdf)
  - Rea Magnet Wire still publishes a 2026 SDS for "Copper Products (with Fiberglass)" — [Rea data sheets page](https://www.reawire.com/products/data-sheets/)

### Inferences
- **Paper and mica builds are much larger than film builds.** The thinnest Nomex 410 (0.05 mm, actual about 0.06 mm) at 50 % overlap gives at least 0.2 mm double-sided per wrap. Samicafilm gives 0.30–0.54 mm. PI/FEP tapes give 0.12–0.30 mm (KQ4).
- **Porosity and voids.** Low-density Nomex 410 (0.72 g/cc at 0.05 mm, εr 1.6) indicates porosity. Air voids will discharge unless impregnated, which is consistent with Arclin's ≤1.6 kV/mm PD guideline. For an 800 V SiC hairpin turn insulation, aramid paper alone is therefore unlikely to be PD-free. It may be useful as a carrier impregnated with varnish, or as a mechanical overwrap.
- **Where mica fits.** Mica (Samicafilm, Nomex 818, mica tapes) is the reference for PD *endurance* rather than PD *inception*. It could be included in a test plan as a "PD-tolerant" comparator, but forming limits and build make it a poor fit for hairpins.

### Gaps
- Nomex 411 (uncalendered precursor of 410) and T-type Nomex (e.g., T410, T418) datasheets were not opened.
- No opened NKN/NMN laminate datasheet gives the εr or thickness of film-plus-paper laminates. Only the vendor tube thicknesses (0.13 and 0.19 mm) are known.
- Nomex 818 εr and dissipation-factor values at 50 % RH are missing in the extracted table.
- Current (2024–2026) datasheets for mica turn tapes were not found as open documents. This includes Elantas/Von Roll Samicafilm, Isovolta 4902 and 342204, Krempel mica tapes, and PI-film-backed mica tapes.
- Glass-fibre (Daglas) served wire: build thickness, εr and breakdown values were not obtained. Vendor class (220 °C for MW-46C per Von Roll) vs other listings is unverified, and the Rea technical datasheets are no longer online (only SDS).

## Key Question 4: Wrapping methods (helical overlap, butt-lap, gap-lap, layers, longitudinal wrap, heat sealing vs adhesive vs varnish, machines, tension, hand-wrapping, steps/voids, resulting build)

### Takeaway
The standard industrial method is helical (spiral) wrapping with concentric taping heads. It uses about 50 % overlap (1–2 tapes), giving 2–4 film thicknesses per side. Fluoropolymer-coated PI is then heat-sealed: induction pre-heat of the copper followed by IR, radiant or salt-bath sintering, compaction rollers and in-line spark testing. Mica tapes are often butt-lapped in 2–3 layers with staggered seams. For 25–38 µm tapes, one 50 %-overlap wrap adds about 0.10–0.15 mm (double-sided) and two wraps about 0.20–0.30 mm. Hand-wrapping short bare bars in a lab is feasible with narrow tape (6–12 mm). Reproducible heat-sealing (FEP melts at 260–280 °C; DuPont seals at 350 °C) and void-free overlaps are the hard parts.

### Cited Findings
- **Standard definition:** "one or two wrappings of aromatic polyimide tape … coated on one or both sides with a suitable adhesive, for instance, fluorinated ethylene propylene. After wrapping, the tape is heat-sealed to form a continuous and adherent sheath" — [IEC 60317-44](https://webstore.iec.ch/publication/1424)
- **DuPont method:** "applied in tape form by helically wrapping it over and heat-sealing it to the conductor and itself" — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- **Industrial fusing:** Von Roll's polyimide-taped rectangular wire uses "induction and radiant heat-fused polyimide film" — [Von Roll motor-repair brochure](https://media.eis-inc.com/m/da351a69383baeb1/original/PH22-77877_9.pdf)
- **Taping line (WTM srl):**
  - Horizontal lines for flat and round wire with 2, 3 or more concentric taping heads, for PI-FEP tapes "such as Apical, Kapton and Norton".
  - Each head's tape tension is held by a dynamic dancer, described as especially useful for very flat, high width-to-thickness wires.
  - Thermal process: high-frequency induction pre-heater, then infrared, radiant or molten-salt-bath sintering furnaces.
  - After sintering: roller compacting units, then water cooling and air wipers.
  - Optional in-line spark testers and a strobe synchronised to head rotation. Capstan/caterpillar pulling is synchronised with head rotation.
  - No numeric speeds or temperatures are given.
  - Source: [WTM taping lines for polyimide-FEP](https://ssr.expometals.net/en/hall/plants/stand/wtm-srl/products/taping-lines-for-polyimide-fep)
- **Taping line (Newtech):** "R-Evolution" lines for round and rectangular wires taped with Kapton, mica or PTFE. Concentric heads, horizontal or vertical; "vibration-free design"; software-calculated tape tension — [Newtech page](https://expometals.net/de/hall/anlagen/waermebehandlunganlagen-und-oefen/stand/newtech/products/kapton-mica-and-ptfe-taping-lines-for-round-and-rectangular-wires)
- **Overlap practice, industrial data points:**
  - CRRC traction wire: 0.038 mm corona-resistant film at 53 % overlap, giving 0.21 mm nominal double-sided build on 2.5 × 6.3 mm copper — [CRRC 2023](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011)
  - Essex DNX Nomex wire: 50 % lap — [Electro-Wind/Essex listing](https://www.electro-wind.com/114-x-258-double-nomex-wrapped-dnx-rectangular-mw-60-copper-magnet-wire-220c-white-250-lb-24-reel-average-wght)
- **Butt-lap and mixed schemes (Samicafilm types):**
  - 2 or 3 mica tapes butt-lapped (overlap 0 +0/−5 %), with layers displaced by 50 ± 10 % (2 layers) or 33 ± 10 % (3 layers).
  - Or 1 tape at 50 % (+0/−5 %) overlap, optionally over a first 23 µm PET film layer at 50 % overlap.
  - Below 8 mm² only half-overlapped wires can be made. As an alternative to 2–3 butt-lapped layers, 1 tape at 50 % or 66 % overlap can be used.
  - Hot-melt grades are consolidated in a press preheated to 160 °C at 2.5 MPa for about 5 min, then cooled below 80 °C.
  - Source: [Von Roll Samicafilm 2007 (OLDER)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf)
- **Wrap geometry (Totoku patent):**
  - Wrap ratios ½, ⅓ and ⅔ are used; "⅔ wrap (three layers)" is the practical maximum to limit loosening.
  - Winding angle 10–60° (preferably 15–40°).
  - Successive layers are preferably wound in opposite directions for a smooth surface.
  - Tape-edge steps are smoothed with tapered parts.
  - Source: [Totoku US12665103B2](https://patents.google.com/patent/US12665103B2/en)
- **PDIV, tape-wrapped vs enamelled (Totoku patent examples):** 1.0 mm round Cu, IEC 60034-18 method.
  - Enamelled wire with 40 µm coating: PDIV 0.65 kV.
  - Two opposite-direction ½-wrapped constant-thickness tapes, 40 µm total: 0.72 kV.
  - Thick sections of the variable-thickness tape wraps: 0.88–1.53 kV at 62–133 µm total.
  - The tape polymer identity is not clear in the extracted table.
  - Source: [US12665103B2](https://patents.google.com/patent/US12665103B2/en)
- **Wrap tension (DuPont patent):** for heat-sealable PI tape on (superconducting) wire, tension varies "from just enough to prevent wrinkling to enough to stretch and neck down the tape". Multiple wraps are used "to minimize the impact of film weak spots or the seams". Sealing of that thermoplastic-PI-coated tape: 220–250 °C (preferably 235 °C); peel 400–3600 g/in — [US5106667A (DuPont, 1992; thermoplastic PI coating, not FEP)](https://patents.google.com/patent/US5106667A/en)
- **FEP heat-seal temperatures:** DuPont's FN seal-strength test uses a jaw sealer at 350 °C / 1.4 bar / 20 s — [Kapton General Specifications (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-general-specs-2.pdf). FEP melting range is 260–280 °C — [Chemours FEP bulletin](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)
- **Tape put-ups and widths (Kapton):**
  - Universal-wind rolls 3.2–22.2 mm wide; Step-Pac 3.2–38.1 mm; pad rolls at least 9.5 mm.
  - Width increments 1.6 mm; width tolerance ±0.18–0.20 mm for narrow slits.
  - Minimum average splice-free length 610 m for 100HN/100CRC/120FWN616B and the 150-gauge heat-sealable types on Step-Pac/universal rolls. This is a supply-chain detail: lab quantities are more practical from distributors.
  - Source: [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
- **Adhesive (PSA) route:** 3M 92 tape needs no heat ("shall not require heat, moisture or other preparation prior to or subsequent to application"). It is 76 µm total thickness for a 25 µm film and rated 180 °C — [3M 92 (OLDER)](https://ca.electro-wind.com/web-files/3M%5CDatasheets%5C3M92.pdf)
- **Mica groundwall wrapping practice:** tapes are applied "as tight as possible". Porous low-resin tapes are "flexible and conformable allowing tight hand or machine winding … thereby helping to reduce air voids and therefore, the possibility of internal corona discharges". Isovolta suggests 1–1.5 kV AC per half-lapped layer as a green-state proof test — [Isovolta 437320 (OLDER)](https://www.electro-wind.com/web-files/Isovolta%5CDatasheets%5C4373-tech.pdf)
- **Void removal in mica-taped bars:** resin-rich tapes are heated and pressed (press or autoclave) "to eliminate any voids in the insulation layers" — [US5973269A](https://patents.google.com/patent/US5973269A/en)

### Inferences
- **Build arithmetic** (my geometric calculation; real builds are higher because of overlap steps, corner effects and tolerances — CRRC reports 0.21 mm where the simple estimate is 0.152 mm):
  - With fractional overlap p, the number of film layers is 1/(1−p): 2 at 50 %, 3 at 66.7 %.
  - Double-sided build per wrap ≈ 2 × t_tape / (1−p).
  - At 50 % overlap: 25 µm HN gives about 0.10 mm; 120FN616 (30.5 µm) about 0.12 mm; 150FN019/150FCRC019 (38.1 µm) about 0.15 mm; two such wraps about 0.30 mm.
  - A PSA tape such as 3M 92 (76 µm total) at 50 % would add about 0.30 mm for only 2 × 25 µm of PI per side.
- **Hand-wrapping geometry for a lab** (my calculation). On a 3.5 × 2.0 mm bar (perimeter P ≈ 11 mm, ignoring corner radii), the helix angle φ from the cross-section plane satisfies sin φ = (1−p)·W/P:

  | Tape width W | Overlap | Helix angle φ | Axial pitch | Tape length per tape layer per 100 mm of bar |
  |---|---|---|---|---|
  | 6 mm | 50 % | 15.8° | 3.1 mm | ≈0.37 m |
  | 10 mm | 50 % | 27° | 5.6 mm | ≈0.22 m |

  A 600–1000 mm hairpin-length sample with two wraps therefore needs only a few metres of tape. A small universal or Step-Pac roll, or a 33 m PSA roll, is sufficient.
- **Lab heat-sealing options for FEP-coated PI** on cut bars (none validated in the sources; they need trials and peel/BDV checks against the 300 g/in FEP-to-Cu and DuPont seal minima):
  - Oven sealing above the FEP melting range, e.g., 300–350 °C, with the tape held by a light overwrap or clamp.
  - Joule-heating the copper bar with high current, mimicking industrial induction pre-heat.
  - A heated jaw or press for straight sections, mimicking the 350 °C / 1.4 bar / 20 s DuPont seal test.
  - Without compaction rollers, entrapped air at overlap steps is likely to be the main reproducibility issue.
- **Method alternatives worth including in a test plan:**
  - (a) Helical 50 % single wrap.
  - (b) Helical 50 % double wrap in opposite directions, as in the Totoku patent, to stagger steps.
  - (c) Butt-lap, 2 layers, seams displaced 50 %, as in Samicafilm.
  - (d) Gap-lap (small gap) plus a second butt-lap layer covering the gaps.
  - (e) Longitudinal ("cigarette") wrap with a single axial seam, heat-sealed. This is not attested for magnet wire in the opened sources (see Gaps). The seam would probably open in edgewise U-bends.

  Each combines with (i) FEP heat-seal, (ii) PSA, or (iii) unbonded film plus varnish dip/VPI.

### Gaps
- No opened source gives industrial line speeds, sintering temperatures, or residence times for PI/FEP taping lines. WTM and Newtech give no numbers.
- No opened source gives quantitative void and PD data comparing overlap types (50 % vs butt-lap vs gap-lap) on rectangular wire. The NEMA MW 1000 minimum-increase rules for film- and paper-wrapped wire were not accessible.
- Longitudinal ("cigarette") wrap of magnet wire: a patent reportedly describes corona-resistant tape applied along the conductor length and folded around the edges, but the opened GE patents only describe half-lap wrapping. Unverified.
- No published procedure was found for hand-wrapping or heat-sealing short laboratory samples. The lab feasibility statements above are engineering inference.
- No desktop or laboratory taping machine vendor was identified in the opened sources.

## Key Question 5: Hairpin-specific issues (forming after wrapping, stripping before welding, slot-fill penalty, voids vs PD, impregnation, ATF) and material–method summary

### Takeaway
For hairpins, wrapped insulation faces three structural penalties compared with enamel or extrusion:
- **Build.** About 0.10–0.30 mm double-sided for PI/FEP; 0.30–0.54 mm for mica. This costs roughly 3–20 % of the copper fraction for a 3.5 × 2 mm conductor.
- **Overlap steps and edges.** These create voids that can lower PDIV and are where PD erosion starts.
- **Mechanical vulnerability.** Tapes can open, wrinkle or shift at the U-bend, twist and insertion, though PI/FEP tapes fused to copper survived traction-coil forming with 6–8.7 kV residual breakdown.

Stripping is mechanical or thermal (PI has no solvents). Varnish adhesion is poor on FEP-outer surfaces. For ATF exposure, aramid paper has a published compatibility claim, while PI's weakness is hot-water hydrolysis (WR/FWR grades mitigate it). I found no open data on PI/FEP or PEEK film tapes aged in ATF.

### Cited Findings
- **Forming limits, mica-taped wire:** minimum bend radius 3 × width edgewise and 2 × thickness flatwise. Avoid sharp or metal tools and hammer blows. "We recommend to not form the coils after the pressing operation" (hot-melt grades). Flexibility test: edgewise 6 × width, flatwise 4 × thickness, no cracks — [Samicafilm 2007 (OLDER)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf)
- **Forming, PI/FEP corona-resistant film wire (traction coils):**
  - After coil spreading, breakdown at the coil nose (the most deformed region) was 6.0–8.7 kV. The spread (max−min) was 1.7 kV for domestic film and 2.7 kV for imported film.
  - Wide- and narrow-edge-bent wire withstood 7.8–8.7 kV, against a ≥5 kV requirement.
  - Prototype motor inter-turn tests passed 8,000–8,500 V for 1 min.
  - Source: [CRRC 2023](https://castjournals.cast.org.cn/joweb/jycl/EN/PDF/10.16790/j.cnki.1009-9239.im.2023.02.011)
- **Standard tests relevant to forming:** IEC 60317-44 includes elongation, springiness, "flexibility and adherence", heat shock (≥260 °C for class 240), cut-through and abrasion tests — [IEC 60317-44 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-44%7Bed1.1%7Db.pdf)
- **Film elongation values relevant to bending:**
  - Kapton HN 72 % typical (25 µm) — [Kapton Summary (OLDER)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf)
  - FCRC 79 %, FWN 55–92 %, PRN 88 % — [Qnity FCRC](https://www.qnityelectronics.com/kapton-fcrc.html), [Qnity FWN](https://www.qnityelectronics.com/kapton-fwn.html), [Qnity PRN](https://www.qnityelectronics.com/kapton-prn.html)
  - Upilex-S 40 % — [UBE 2022](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf)
  - APTIV PEEK >150 % — [Victrex 2023](https://www.victrex.com/-/media/ul-datasheet/aptiv-films-1000-series.pdf)
  - FEP 300 % — [Chemours FEP](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)
  - Nomex 410 MD 10–23 % — [Arclin 410](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf)
- **Insertion and bending (supplier claim):** overlapped tapes can be "pushed out of the slot" or displaced "during bending" in hairpin stators, and "overlapped film seams are the weakest point" for PD — [CWIEME/Politubes 2023](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)
- **Stripping:**
  - Kapton has "no known organic solvents". For wire and cable, "the use of a heated element, to remove insulation" is routine. Welding arcs "quickly destroy … all types of Kapton film", but film near a weld may survive close to the flame. FEP-coated types require ventilation per the fluoropolymer handling guide — [Kapton Summary (OLDER)](https://www.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-summary-of-properties.pdf)
  - Upilex-S is "insoluble in all organic solvents" — [UBE 2022](https://ube.com/upilex/catalog/pdf/upilex_s_e.pdf)
- **Impregnation and varnish compatibility:**
  - Kapton has "superior chemical resistance to most solvents, hydrocarbons, lubricants, resins, and varnishes" — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf)
  - FEP film is "non-wetting" with "superior anti-stick" properties. Cementable Types C and C-20 exist for adhesive bonding — [Chemours FEP](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)
  - Nomex 410 is compatible with "virtually all classes of electrical varnishes" — [Arclin 410](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf)
  - Nomex 818 "can be readily impregnated with varnishes" — [Arclin 818](https://arclin.com/wp-content/uploads/2026/04/Arclin_Nomex_818_Technical_Data_Sheet_2025.pdf)
  - Samicafilm: "For impregnating varnishes and resins, consult our customer service" — [Samicafilm (OLDER)](https://hallaweb.jlab.org/tech/Detectors/public_html/manuals/data_sheets-manuals/U-V/von_roll/Samicafilm-Taped-315.15-01.pdf)
  - Mylar: impregnation is required for continuous operation above corona threshold in air — [Mylar bulletin](https://converting-tasm.pl/wp-content/uploads/2024/01/info-mylar-a-electrical-properties_ekotech_2023.pdf)
- **ATF and moisture:**
  - Nomex is claimed EV-motor-suitable due to "demonstrated compatibility with … automatic transmission fluids" — [Arclin 410](https://arclin.com/wp-content/uploads/2026/04/Arclin%E2%84%A2-Nomex%C2%AE-410-Technical-Datasheet-04-2026.pdf)
  - Kapton HN degrades under continuous hot-water exposure. WR and FWR address hydrolysis — [Magnet Wire Bulletin (OLDER)](https://ca.electro-wind.com/web-files/DuPont%5CLiterature%5CKapton-motor-magnet-wire-bulletin.pdf); [Qnity FWR](https://www.qnityelectronics.com/kapton-fwr.html)
  - FEP is "chemically inert and resistant to virtually all chemicals" — [Chemours FEP](https://polymerfilms.com/wp-content/uploads/2023/06/Chemours-Teflon_FEP-Datasheet-cobranded-pf.pdf)
  - APTIV PEEK claims hydrolysis and chemical resistance, with 0.04 % water absorption — [Victrex 2023](https://www.victrex.com/-/media/ul-datasheet/aptiv-films-1000-series.pdf)

### Inferences
- **Slot-fill penalty** (my calculation for a bare 3.5 × 2.0 mm hairpin conductor, ignoring corner radii and the slot liner; copper fraction of the insulated cross-section):

  | Wrap | Double-sided build | Copper fraction |
  |---|---|---|
  | 1 × 25 µm HN @ 50 % | 0.10 mm | ≈92.6 % |
  | 1 × 120FN616 @ 50 % | 0.12 mm | ≈91.1 % |
  | 1 × 150FN019/FCRC @ 50 % | 0.15 mm | ≈89.0 % |
  | CRRC-type, as built | 0.21 mm | ≈85.4 % |
  | 2 × 38 µm tapes @ 50 % | 0.30 mm | ≈79.8 % |
  | Samicafilm, 2 butt-lapped | 0.36 mm | ≈76.8 % |

  Compare with the enamel/extrusion builds reported by the other researchers to judge competitiveness.
- **Hairpin-specific risk ranking for wrapped tapes** (inference from the forming and adhesion evidence above):
  - Twisted end (twist plus bend at the leg exit): highest risk of tape lifting or shear-wrinkling. This argues for fusing (FEP or thermoplastic) rather than PSA, and for opposite-hand double wraps.
  - Crown U-bend: the inner radius gets wrinkles and overlap-step bunching; the outer radius gets film elongation. PI/FEP elongation of 55–92 % is ample at moderate radii; mica is not.
  - Straight slot section: overlap steps and air at edges are the main PD sites.
- **Wrap before or after forming.** Wrapping after forming is impractical for hairpins. Wrapping before forming means every test sample should be wrapped straight, then formed (U-bend, twist), then tested. Recommended set: PDIV per IEC 60034-18-41-type sample geometry, breakdown, and heat shock per IEC 60317-44 / CRRC 240 °C × 2 h × 10 cycles.
- **Stripping for welding.** Leave the ends unwrapped (masked) in lab samples. In production, mechanical milling or laser ablation would be needed; FEP and PI residues near the weld will char.
- **ATF tests.** The decisive ones are hot ATF with controlled water content: PI hydrolysis, FEP-bond integrity and PSA swelling. PSA (silicone or acrylic) tapes are the least likely to be ATF-robust and should be treated as lab-only.

#### Material–method matrix
Numbers are taken from the findings above, with sources linked there. Maturity, feasibility, pros and risks are my assessment.

| Material / method | Typical tape and build | Thermal | εr | Dielectric strength | Maturity | Lab feasibility on cut bare bar | Main pros | Main risks for hairpin | Commercial examples |
|---|---|---|---|---|---|---|---|---|---|
| PI/FEP heat-sealable tape, helical 50 %, 1–2 wraps, induction/oven fused | 30–64 µm tape; ≈0.12–0.30 mm double-sided | IEC class 240 (US 220); UL RTI 240/200 °C (FWN) | 2.6–3.1 (composites) | 142–272 kV/mm (min to typical) | Series for rail/industrial/wind/ESP (IEC 60317-44, MW-62C); EV: no series evidence | Medium (hand wrap easy; heat-seal ≥280–350 °C needs a jig) | Solvent-free, uniform, high DS, Cu bond ≥300 g/in | Overlap voids, twist/U-bend lifting, FEP-outer non-wetting, hydrolysis | Kapton 120FN616/150FN019/FWN/FWR/PRN; Apical (Norton named by WTM) |
| Corona-resistant PI/FEP (FCRC, ECRC, Apical CR, Chinese CR) | 38 µm; CRRC 0.21 mm @53 % | RTI 240 (100CRC); FCRC page shows 130 (verify) | 3.4 | 173 kV/mm (FCRC typ.), 256 (100CRC) | Series in inverter-fed rail traction (CRRC); EV marketed (ECRC) | Medium | PD endurance: CR >100,000 h vs HN 200 h (supplier); ECRC 8× FN | Same as above; availability (ECRC docs gated) | Kapton 150FCRC019, ECRC |
| PI + PSA (silicone) tape, helical by hand | 63–76 µm tape; ≈0.25–0.30 mm @50 % | 180 °C (3M 92), 220 °C (Leo CR) | ≈3.4 (film) | >7.5 kV (3M 92), 6 kV (Leo) per tape | Coil/lead wrapping; not a magnet-wire standard | High (simplest) | No heat step, quick | Thick adhesive, lower class, creep, ATF/varnish interaction unknown | 3M 92, P. Leo 1K063CR, CMC Kapton CR tapes |
| PEEK film tape (APTIV) + fusion/adhesive/varnish | 8–750 µm films (25 µm practical) | Upper working temperature 250 °C (distributor) | 3.2–3.5 | 270 kV/mm @25 µm | Lab only for wrap | Medium | Elongation >150 %, low moisture | No proven bonding route; cost | Victrex APTIV 1000 |
| FEP / PTFE film tape | FEP 12.5–500 µm; PTFE 50 µm + PSA 96 µm | FEP 205 °C continuous; 3M 5480 204 °C | 2.0–2.1 | 260 kV/mm @25 µm (FEP) | Lab | Medium–High | Lowest εr (helps PDIV); FEP self-seals | Cold flow, low tensile (21 MPa), non-bondable outer surface | Chemours Teflon FEP film; 3M 5480 |
| PEN / PET / PEI tapes | PEN 12–250 µm; PET 23–500 µm; PEI 25–50 µm | PEN RTI 180/160 °C; PEI Tg 217 °C | ≈3.0 (PEN), 3.2 (PET) | 250 kV/mm (PEN); ≈252 kV/mm (PEI) | Lab (slot/phase use is mature, wrap is not) | High | Cheap (PET), heat-sealable (PEI) | Thermal margin below class 180–220 hairpin needs (PEN/PET) | Teonex Q51, Mylar A, ULTEM 1000B |
| Nomex 410 paper tape, 50 % lap, double (DNX), + varnish | ≥0.05 mm paper; ≳0.2 mm per wrap | RTI 220 °C | 1.6–3.7 | 18–34 kV/mm | Series (transformers, form coils; MW 60) | High (hand wrap) | ATF-compatibility claim, cheap, conformable | Porous: PD unless impregnated; thick; low DS | Essex DNX; Arclin Nomex 410 |
| Nomex 818 (aramid–mica) tape | 0.08–0.25 mm | 220 °C class family | n/a | 28–39 kV/mm | Series for HV conductor/coil wrap | High | Better PD endurance than 410 | Thick; build | Arclin Nomex 818 |
| Mica tape (film- or glass-backed), butt-lap 2–3 layers or 50 % | 0.09 mm tapes; 0.30–0.54 mm build | TI 155/180 | n/a | 3.5–7 kV straight (wire) | Series for HV machines | Medium (brittle; hot-press for B-stage) | Best PD/corona endurance | Very thick; bend radius ≥3 × width edgewise; flaking | Von Roll Samicafilm; Isovolta 4902/342204; Austravolt |
| Glass-fibre / Daglas serving + varnish | n/a | TI 180 (IEC 60317-31); vendor 220 °C | n/a | n/a | Series (field coils, DC traction) | Low (serving machine needed) | Thermal, mechanical | Thick, porous, PD-prone without resin | Von Roll Austraflex; Rea fiberglass products |

### Gaps
- No opened source reports wrapped insulation actually applied to EV hairpins, whether at the U-bend or twist, after insertion, or with PDIV after forming. All hairpin-specific statements are inferences from traction-coil, standard and vendor data.
- No ATF-immersion data were found for PI, PI/FEP, PEEK-film or FEP tapes. An Applied Sciences 2022 paper on ATF compatibility of polymers in electrified transmissions exists, but MDPI returned 403. Its polymer list and results are unknown.
- No quantitative PDIV comparison of film-wrapped vs enamelled rectangular wire at hairpin-relevant builds was found. The Totoku data are for 1.0 mm round wire, and the CRRC PDIV values exist only in a figure.
- Laser or mechanical stripping parameters for PI/FEP-wrapped rectangular wire, and weld-zone contamination effects, were not found.
- The search result attributing "0.5–1 kg corona-resistant PI film per EV" to a Chinese market report (chinabaogao, 2025-10) was not opened. It is not verified here.
- Suppliers named in the brief whose film/paper/glass-covered rectangular wire offerings I could not verify: Superior Essex, Asta, Elektrisola, LWW, Dahrén, and Chinese film-wrapped flat-wire sellers (e.g., Shanghai Youtuo — page HTTP 503). "Bruker" appears to refer to Bruker-Spaleck, whose brochure shows only enamelled flat wire.
