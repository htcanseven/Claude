# Extruded and melt-processed thermoplastic insulation on rectangular (hairpin) copper conductors

Scope note: this file covers melt-extrusion (crosshead) and other melt processing (injection overmolding, melt-bonding) of thermoplastics onto bare rectangular copper for 400–800+ V traction motors. Enamels, tapes/films, tubes/heat-shrink, powder/e-coat/parylene and test standards are covered in sibling files. Research date: 2026-10-10. The shared web-search budget ran out partway through. Later lookups used only pages already found, so some leads could not be followed; they are listed under Gaps. Most quantitative data on construction versus PDIV comes from patents (Furukawa/Essex/Arkema). Patents are primary technical disclosures but not product datasheets, and most have 2011–2020 priority dates.

## 1. Extruded PEEK rectangular magnet wire: products, makers, resin grades, thickness, construction (direct-on-Cu vs enamel+PEEK), adhesion, crystallinity, εr, Tg/Tm, thermal class, ATF/hydrolysis, PDIV vs enamel

### Takeaway
Extruded PEEK flat wire is in series production as of 2023–2026. Confirmed sources: hpw Metallwerk (Austria), Jiateng Electric (China, with a UK PEEK supplier), and Essex Furukawa's "High Voltage Winding Wire", which the press release only calls "extruded engineering plastic". Bekaert Ampact (single-layer PEEK) is offered commercially. A Syensqo KetaSpire monolayer PEEK insulation is used in Mavel's >800 V sports-car motor. Walls run about 80–300 µm, typically 100–200 µm. There are two constructions: single-layer PEEK straight on copper, which needs adhesion-optimised grades such as KetaSpire KT-857, or a 20–60 µm PAI/PI enamel under the PEEK, with or without a 5–10 µm PEI/PPSU tie layer. On hairpin-size conductors (about 3.4 × 1.8 mm), Furukawa patent data give PDIV (25 °C, 50 Hz, 10 pC) of about 1.35 kVp at 120 µm total, 2.2 kVp at 200 µm and 3.05 kVp at 280 µm. Enamel-only builds of 60–100 µm give 0.82–1.14 kVp.

### Cited Findings

**Commercial products / makers**
- Essex Furukawa "High Voltage Winding Wire (HVWW)". The press release describes it as "coated with extruded engineering plastic" without naming the polymer. Other claims: designed for 800 V applications, allows "high voltages of over 1000V", "partial discharge free", and constant 240 °C operation "without any reduced performance". It covers a 33,000 t contract as sole magnet-wire supplier to an unnamed premium brand of the world's largest automaker, produced exclusively at the Arolsen plant in Germany. The product won first place in the 2017 Magna Innovation Award. Press release dated 12 Aug 2021 (older information). — [Kyodo/PRNewswire release](https://kyodonewsprwire.jp/index.php/release/202108138772)
- The Google Patents record for an Essex extruded-thermoplastic patent notes a 2024 name change from "Essex Furukawa Magnet Wire USA LLC" to "Essex Solutions USA LLC". Search under both names. — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- hpw Metallwerk GmbH (9 Nov 2023 press release):
  - Its "patented PEEK wire" is already in series production at Leonding, Upper Austria, with full utilisation expected in 2025.
  - PEEK-insulated wires are planned at a new North American plant "from 2026".
  - It holds a major order from an international automotive OEM worth a "mid three-digit million euro" amount.
  - The flat wires are "primarily used in 800 volt applications" such as e-buses and e-lorries, and allow "significantly tighter bending radii".
  - No thickness, PDIV or adhesion values are given.
  - — [hpw press release](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L)
- Bekaert Ampact, from its wire Düsseldorf 2024 deck:
  - "Ampact = Single layer PEEK".
  - "400V BEV's use enamel PAI as standard solution (typically 40–80 µm thickness)".
  - "PEEK is available as single layer (superior) or dual layer coating solution (>100µm)".
  - Stated drivers: breakdown voltage >10 kV (PDIV >1500 V), surviving "bending of 1x wire thickness", >180 °C peak, and lifetimes >20,000 h.
  - Typical hairpin cross-sections are 5–10 mm² (e.g. 3.5 × 2.0 mm) in 4–8 layers.
  - A bend-over-1×-thickness image is labelled "PAI crack / PEEK no crack".
  - — [Bekaert Ampact deck (PDF)](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf)
- Bekaert (V. Vermeersch, 4 Oct 2023): PAI enamel's typical maximum thickness is "roughly 120–130 µm". PEEK handles "maximum operating temperatures of more than 240 °C" and is applied in one extrusion step, versus multi-pass solvent-based PAI. — [LinkedIn article](https://www.linkedin.com/pulse/enamel-vs-peek-why-wire-coating-matters-high-voltage-vermeersch)
- Syensqo (ex-Solvay) KetaSpire KT-857, launched 24 May 2023:
  - It is "a new PEEK extrusion compound designed especially for copper magnet wire insulation" applied as a monolayer.
  - Solvay states that "one of the biggest challenges of standard PEEK extrusion is to obtain an adequate level of adhesion of the insulation to the copper magnet wire". KT-857 claims "better adhesion in a faster and more cost-efficient monolayer process" and a "more uniform insulation layer".
  - "Higher voltage e-motors typically require thicker magnet insulation up to 180 microns".
  - No VOCs, and less energy than enamelling.
  - — [CompositesWorld](https://www.compositesworld.com/products/peek-for-monolayer-e-motor-magnet-wire-insulation)
- Mavel Powertrain (Italy, 6 Oct 2025) chose "monolayer KetaSpire PEEK magnet wire insulation" plus Ajedium PEEK slot liners and wedges for a motor "supporting operations at over 800 volts" for an unnamed premium sports-car maker. The wire maker is not named and no thickness is given. — [Magnetics Magazine](https://magneticsmag.com/mavel-powertrain-selects-syensqo-materials-for-high-performance-ev-motor-project/); same project in [e-Mobility Engineering](https://www.emobility-engineering.com/?p=16587), which also lists peak power ">300 kW" for high-performance applications.
- Victrex XPI (resin, for wire makers):
  - XPI grades are "designed for extrusion wire processing".
  - Typical XPI coating is 80–300 µm versus 5–100 µm for enamel.
  - "Class 220 °C" (versus 180 °C quoted for PAI enamel) and operation from −40 °C to 260 °C.
  - About 2× the thermal conductivity of PI and "at least 2x tighter bending radius" than enamel.
  - Withstands ATF and dielectric fluids at 180 °C for up to 2,000 h with retained electrical properties, "validated by OEM oil experts".
  - Up to 60% less energy than enamelling. Made under IATF 16949.
  - Mechanical and laser stripping both work, though no parameters are given.
  - — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)
- Victrex Japanese e-book (© 2024). Its comparison table lists:

  | Construction | Max thickness | Temperature class |
  |---|---|---|
  | Multi-layer PAI enamel | 130 µm | 220 °C |
  | Polyimide tape wrap | 230 µm | 240 °C |
  | Extruded XPI | 300 µm | "240 °C*" |

  The asterisk notes that 240 °C is an estimated RTI based on tests of similar products. The e-book also claims "electrical RTI 240 °C*", a bend radius half that of enamel, and ATF/dielectric-fluid resistance at 180 °C up to 2,000 h. It quotes a simulated 2% smaller battery, or a potential US$270 saving per battery at 2018 pack prices (WLTP-3b drive cycle). Note the conflict: the e-book rates PAI enamel at 220 °C, while the English web page says 180 °C. — [Victrex XPI e-book (JA, PDF)](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)
- A Victrex K 2022 flyer lists "Stable operation from −40 °C up to 250 °C" and "Low levels of moisture absorption combined with excellent hydrolysis resistance". The flyer is from 2022, and its 250 °C figure is lower than the 260 °C on the current web page. — [Victrex K2022 flyer (PDF)](https://www.victrex.com/-/media/downloads/literature/k2022_ipad_auto_formatted_f.pdf)
- Jiateng Electric (佳腾电业, China), announced 6 Aug 2025:
  - It "successfully achieved mass production of PEEK insulated flat wire" with "威格斯", described as a UK specialty-polymer supplier and inventor of PEEK polymerisation. Cooperation began in 2018 and became a "global strategic partner" relationship in April 2025.
  - Design wins at Lotus, BMW, Audi, Mercedes-Benz and NIO, with more than 80% of wins from global top-tier OEMs.
  - PEEK withstands "above 2300 V" (metric unspecified).
  - Plants are being launched in Germany, Thailand and the USA.
  - No thickness or PDIV is given.
  - — [ifeng Tech](https://tech.ifeng.com/c/8lbM26LSIAO)
- Zeus (USA/Ireland):
  - PEEK and PFA insulated wire in "round, square, and rectangular profiles".
  - Wall 0.001–0.080 in (0.025–2.032 mm), "100% AC spark tested" during extrusion, insulating properties maintained up to 260 °C.
  - Splices are made with PEEKshrink heat-shrink tubing.
  - — [Zeus PEEK wire page](https://zeusinc.com/products/insulated-wire/peek-wire)
  - The datasheet (PDF filed under a 2026/07 upload path, but its internal metadata dates from 2020) lists round AWG 2–40 as standard, "stranded sizes and custom shapes available upon request", spools up to 200 lb, "PEEK polymer is UL rated up to 260 °C", and thermal conductivity 0.29 W/m·K. — [Zeus PEEK datasheet V2R5 (PDF)](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf)
- Other Chinese marketing pages; treat these as unverified claims.
  - Ningbo Jintian Copper headlines "PEEK Flat Wire: 2300V+ Voltage Resistance" (about Feb 2025) but gives no thickness or PDIV data. It quotes PEEK Tg 143 °C and Tm 343 °C. — [Jintian (jtcopper)](https://en.jtcopper.com/peek-flat-wire-2300v-voltage-resistance-and-flame-retardant.html)
  - Dongguan Xinglian claims "PEEK-insulated magnet wire and enameled rectangular wire" "rated for 240 °C+ continuous operation" for 800 V+ hairpins. It gives no thickness, PDIV or process data. — [Xinglian](https://xingliancable.com/peek-magnet-wire/)
  - Zhejiang BW Industry ("BWPEEK") claims PEEK keeps ">91% of its original adhesion" after 2,000 h in 150 °C ATF. It also gives PDIV grades: >1,200 V at 30–60 µm, >1,400 V at 60–90 µm, >1,600 V at 90–120 µm, >1,800 V at 120–150 µm and >2,100 V above 150 µm. Flat wire runs 0.30–25 mm wide × 0.20–5.00 mm thick. The page contains template text and a process list (lacquering and curing) that contradicts "extruded", so reliability is low. — [BWPEEK](https://peekmaterials.com/peek-forms/peek-wire/)

**Resin grades and material data**
- VICTREX XPI 150 datasheet. Properties come from moulded coupons; breakdown data is for equivalent-thickness APTIV film.
  - Tg (onset) 143 °C and Tm 343 °C.
  - MFR 6.5 g/10 min (400 °C / 2.16 kg).
  - εr 3.20 (23 °C, 1 kHz) and tan δ 3.0 × 10⁻³ (1 MHz).
  - Dielectric strength (ASTM D149, 2000 V/s): 16.6 kV at 100 µm, 21.4 kV at 150 µm, 25.4 kV at 200 µm. At 500 V/s: 15.7, 19.9 and 23.0 kV.
  - Volume resistivity 1 × 10¹⁶ Ω·cm and tensile yield 102 MPa.
  - Described as having "good ductility for demanding wire forming" and resistance to ATF, oils and cooling fluids, with no quantitative data.
  - — [XPI 150 datasheet](https://victrex.com/de/downloads/datasheets/victrex-xpi-150-polymer)
- The Furukawa patents used these grades: Syensqo KetaSpire KT-820 (εr 3.1) and modified-PEEK grade "AV-650" ([US9514863B2](https://patents.google.com/patent/US9514863B2/en)), and Victrex PEEK 381G ([US10109389B2](https://patents.google.com/patent/US10109389B2/en)).
- Zeus PEEK wire dielectric strength (ASTM D149), in V/mil:

  | Temperature | 0.0015 in (38 µm) wall | 0.003 in (76 µm) wall |
  |---|---|---|
  | 22 °C | 4113 | 3830 |
  | 180 °C | 5040 | 4393 |
  | 200 °C | 3487 | 3357 |
  | 220 °C | 3133 | 2107 |
  | 240 °C | 2393 | 1443 |
  | 260 °C | 153 | 483 |

  — [Zeus datasheet](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf)

**Construction, adhesion, crystallinity (patent disclosures)**
- Essex US9324476B2 (Essex Group; filed 5 Feb 2014; granted 26 Apr 2016):
  - Claim 1: an enamel layer plus an extruded PEEK or PAEK layer "bonded directly to the enamel with substantially no bonding agent", 25–610 µm thick, concentricity about 1.1–1.5.
  - Performance claimed: PDIV >1,300 V, dielectric strength >10,000 V, continuous operation at about 220 °C. Dependent claims add PDIV >1,500 V and 240 °C.
  - Enamel is 25–254 µm (preferred 76–127 µm); extruded layer preferred 76–178 µm; example total 85–240 µm.
  - Adhesion without adhesive comes from heating the conductor to about 200 °C (≈400 °F) or more before extrusion.
  - Post-extrusion heating helps crystallinity, and a water quench follows.
  - Earlier PPS-over-enamel designs "required an adhesive layer".
  - Oil test: ASTM D1676-03 oil bomb at 150 °C for about 2,000 h, no results given. Flexibility test: 25% elongation plus a 90° bend around a 4.0 mm mandrel.
  - Table 1 (thicknesses not given per row), dielectric strength / PDIV in kV:

    | Construction | Dielectric strength (kV) | PDIV (kV) |
    |---|---|---|
    | PEEK only | 9.0 | 1.5 |
    | PI + PEEK | 10.0 / 11.7 | 1.6 / 2.7 |
    | PAI + PEEK | 11.1 | 1.8 |

  - — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- Furukawa US9514863B2 (priority 30 Nov 2012):
  - Construction: rectangular Cu 1.8 × 3.4 mm with 0.3 mm corner chamfer, PAI enamel ≤60 µm, a 2–20 µm adhesive layer (PEI preferred; PPSU or PES as alternatives), and extruded PEEK ≤200 µm with crystallinity ≥50% (examples 62–71%).
  - Targets: conductor-to-coating adhesion ≥20 g (180° peel), coating-to-coating adhesion 100 to <400 g, PDIV 1,200–3,200 Vp, and ≥90% breakdown retention after 300 °C for 168 h.
  - Results:

    | Construction | Total thickness | PDIV | Note |
    |---|---|---|---|
    | PAI 40 / PEI 5 / PEEK 40 µm | 85 µm | 1,350 Vp | |
    | PAI 15 / PEI 6 / PEEK 105 µm | 126 µm | 1,750 Vp | |
    | PAI 45 / PEI 7 / PEEK 91 µm | 143 µm | 1,910 Vp | |
    | PAI 31 / PPSU 10 / PEEK 151 µm | 192 µm | 2,520 Vp | |
    | PAI 60 / PEI 6 / modified PEEK 181 µm | 247 µm | 3,120 Vp | |
    | PAI 38 / PEI 10, no extrusion | 48 µm | 950 Vp | |
    | PEEK 171 µm directly on Cu, no enamel or adhesive (Comp. Ex. 3) | 171 µm | 2,220 Vp | Shown as "✕" on dielectric after winding + heating (comparative symbol rows extracted with uncertain column alignment; verify in original) |
    | Extruded layer 220 µm (Comp. Ex. 9) | — | — | Poorer breakdown after winding + heating |

  - — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Furukawa US10109389B2 (priority 12 Mar 2014):
  - Construction: multilayer baked enamel ≥60 µm (preferred 60–100 µm) plus extruded PEEK or PPS 20–200 µm, with adhesion between baked layers 5–10 g/mm.
  - Comparative Examples 6 and 7 (30 µm enamel + 100 or 120 µm PEEK): adhesion "too high", so a bend crack reached the PAI layer or the conductor.
  - PDIV criterion (10 pC, 50 Hz, 25 °C): <800 Vp fails, 800–1,200 Vp passes, ≥1,200 Vp is "excellent".
  - Conductor range: 1.0–5.0 × 0.4–3.0 mm with corner radius ≤0.6 mm (preferred 0.2–0.4 mm).
  - — [US10109389B2](https://patents.google.com/patent/US10109389B2/en)
- Furukawa/Denso US8847075B2 (priority 12 Aug 2011) shows adhesive-free extrusion over enamel. Introducing carboxyl, ester, ether or hydroxyl groups onto the PAI enamel surface (atmospheric plasma, corona, primer or UV) gives good adhesion and solvent resistance without an adhesive layer. Prior-art PPSU tie layers lowered solvent resistance. Denso is a co-assignee. — [US8847075B2](https://patents.google.com/patent/US8847075B2/en)
- Essex US12278026B2 (priority 7 Aug 2020): PEEK mould shrinkage is about 1.1–1.5 versus about 0.7 for PPSU, and the higher shrinkage "may lead to relatively low adhesion properties". This motivates co-extruding a lower-shrinkage first layer. — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- MFL Group/Frigeco, an extrusion-line supplier, claims "precise control over the crystalline structure of the material" to achieve minimal insulation thickness and better adhesion to the conductor. — [Wire & Cable India, 14 Sep 2024](https://www.wirecable.in/?p=32084)

**PDIV vs thickness on hairpin-size conductors: enamel only vs enamel + extruded PEEK**
- Furukawa US10109389B2 example table (rectangular Cu; PDIV in Vp at 25 °C):

  | Construction | Total thickness | PDIV |
  |---|---|---|
  | Enamel only, PAI 20 / polyester 40 µm | 60 µm | 820 Vp |
  | Enamel only, PI 25 / PAI 40 µm | 65 µm | 850 Vp |
  | Enamel only, 2–3 layers | 80 µm | 900–920 Vp |
  | Enamel only, PEst 35 / PAI 60 µm | 95 µm | 1,080 Vp |
  | Enamel only, 3-layer | 100 µm | 1,120–1,140 Vp |
  | ~80 µm enamel + PEEK 40 µm | 120 µm | 1,350 Vp |
  | Enamel + PEEK 75 µm | 155 µm | 1,720 Vp |
  | Enamel + PEEK 60 µm | 160 µm | 1,770 Vp |
  | Enamel + PEEK 120 µm | 200 µm | 2,200 Vp |
  | Enamel + PEEK 150 µm | 235 µm | 2,550 Vp |
  | Enamel + PEEK 180 µm | 255–260 µm | 2,780–2,820 Vp |
  | Enamel + PEEK 200 µm | 280 µm | 3,050 Vp |
  | Enamel + modified PEEK | 125 / 200 / 285 µm | 1,380 / 2,180 / 3,100 Vp |

  Breakdown after bending: 5.8–9.5 kV, with no cracks in any example. — [US10109389B2](https://patents.google.com/patent/US10109389B2/en)
- Essex US12278026B2 Table 2: single extruded PEEK directly on a rectangular aluminium conductor (about 9.80 × 3.81 mm, no base insulation):

  | PEEK thickness | PDIV (room temp) | Shotbox breakdown |
  |---|---|---|
  | 120 µm | 1,679 V | 9,478 V |
  | 155 µm | 1,820 V | 13,530 V |
  | 160 µm | 1,905 V | 12,093 V |

  In Table 1 (PAI base on 3.384 × 1.834 mm OFC copper), a PEEK control at 182 µm gave PDIV 1,201 V and breakdown 11,734 V. — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- Peer-reviewed evaluations exist, but the accessible abstracts give no numbers.
  - Kilper, Baader, Naumoski, Hameyer (Mercedes-Benz AG / RWTH Aachen), EDPC 2020, DOI 10.1109/EDPC51184.2020.9718555, compared PD test methods (ramp-to-ramp with two conductors placed against each other, steel-sphere bath, salt bath) on "PAI, PPS and PEEK" insulation on a hairpin conductor. — [FAU CRIS abstract](https://cris.fau.de/publications/270664426)
  - Mancinelli, Stagnitta, Cavallini, IEEE Trans. Ind. Appl. 53(3), 2017, pp. 3110–3118, ran hairpin qualification under IEC 60034-18-41 plus ISO 16750-3 vibration. Turn-to-turn insulation was the weakest link, samples were PD-free until breakdown, and "the root cause for breakdown was, in all cases, traced back to cracks". The abstract page does not name the insulation material. — [Unibo IRIS](https://cris.unibo.it/handle/11585/598944)

### Inferences
- From the Furukawa table, enamel+PEEK builds on about 3.4 × 1.8 mm copper rise about 10–11 Vp per µm of total thickness between 120 and 280 µm, at 25 °C. Enamel-only builds rise about 8 Vp/µm between 60 and 100 µm. A 25 °C PDIV of ≥1.5 kVp needs roughly 130–150 µm total; ≥2.2 kVp needs about 200 µm. Hot and reduced-pressure PDIV (covered by the test-standards researcher) will be lower and must be measured.
- Direct-on-copper single-layer PEEK is now offered commercially (Ampact, KT-857 monolayer, Zeus). hpw's construction is not disclosed in opened sources. In Furukawa's 2012 work, PEEK straight on copper appears to have failed the post-winding/heating dielectric criterion; the comparative-table symbols extracted imperfectly, so verify this in the original patent. Conductor adhesion after forming and thermal cycling should therefore be a primary test item, for example peel after bending.
- Interlayer adhesion is two-sided: too little gives delamination, too much lets a crack in the stiff outer layer run through to the conductor (US10109389 comparative examples). Adhesion should be specified as a window, not a minimum.
- Thermal-class claims are inconsistent: "Class 220 °C" (Victrex web), "RTI 240 °C (estimated)" (Victrex e-book), 240 °C constant (Essex Furukawa HVWW), "UL rated up to 260 °C" (Zeus, polymer). The 260 °C figure is a polymer rating, not a wire-system RTI. Treat 220 °C as the conservative design class until wire-level IEC 60172 or UL data is obtained.
- Essex Furukawa's HVWW is very likely enamel + extruded PEEK, given its patent family (US9324476) and the 240 °C claim. The press release itself only says "extruded engineering plastic", so this is unconfirmed.

### Gaps
- Proterial (ex-Hitachi Metals), Sumitomo Electric, Jingda and Gold Cup: no confirmed extruded-PEEK rectangular wire product information was found before the search budget ran out.
- Evonik VESTAKEEP wire grades: no source found.
- Essex Furukawa trade name "NEXCEL": not verified.
- No resin was confirmed for Essex HVWW. A 2018 Solvay/EFMWE KetaSpire PEEK + HVWW Magna-award document appeared in search results but could not be opened (HTTP 404), so it is unverified.
- No independent peer-reviewed PDIV/RPDIV values for commercial extruded-PEEK hairpin wire at 25 °C and 150–180 °C were found. The RWTH/Mercedes EDPC 2020 paper likely has data but was not accessible.
- Quantitative hydrolysis data for PEEK wire (e.g. breakdown after humidity ageing) was not found; only qualitative Victrex claims.
- hpw's claim of "adhesion on copper without bonding layer" appeared only in a search snippet of a brochure that returned 404, so it is unverified.

## 2. Other PAEKs on wire: PEKK (Arkema Kepstan), low-melt PAEK (Victrex LMPAEK/AE 250), PEK

### Takeaway
PEKK is the only other PAEK with documented magnet-wire extrusion work. Arkema promotes Kepstan PEKK for EV magnet wire, and its patent describes single-layer PEKK extruded continuously onto copper at 330–350 °C and 10–13 m/min, kept pseudo-amorphous so turns can be heat-welded, then annealed to crystallise. No public data was found for Victrex LMPAEK/AE 250 on wire. PEK and PEKEKK appear only as listed options in Furukawa blend patents.

### Cited Findings
- Arkema markets Kepstan PEKK wire coatings for "applications like magnet wire to power more efficient electric vehicles". "Alloyed options" improve "glass transition temperature, dielectric performance, or even cost". Fire data: UL 94 V-0 at 0.8 mm; LOI listed as "35-35 %O₂" at 1.6 mm. — [Arkema Kepstan wire coatings](https://hpp.arkema.com/en/product-families/kepstan-pekk-polymers/wire-coatings/)
- Arkema EV page: Kepstan PEKK is "a great solution for e-motor magnet wires", provides "excellent adhesion to conductive metal components", and meets "high voltage isolation requirements at low thicknesses". It gives no numbers. — [Arkema EV page](https://hpp.arkema.com/en/markets-and-applications/automotive-and-transportation/electric-vehicles)
- Arkema patent US12148548B2 (priority 30 Apr 2020; granted 19 Nov 2024):
  - Construction: an insulated conductor whose outermost layer is "pseudo-amorphous" and contains ≥50 wt% PAEK. Preferred terephthalic share is 48–75% of T+I (very preferably 58–73%).
  - Example 1, single-layer PEKK by continuous melt extrusion on 1 mm copper wire:

    | Polymer | Extrusion temp | Line speed | Sheath thickness |
    |---|---|---|---|
    | KEPSTAN 6000 series (T ≈60%) | 330 °C | 10 m/min | 77 µm |
    | KEPSTAN 7000 series (T ≈70%) | 350 °C | 10 m/min | 102 µm |
    | Higher-flow 7000 grade (MFI 65 cm³/10 min) | 350 °C | 13.3 m/min | 69 µm |

  - Process: wire degreased with ethanol, preheated with a heat gun set to 500 °C, resin dried 12 h at 150 °C. Extrusion temperature range Tm + 5 °C to Tm + 100 °C (preferred Tm + 10 to Tm + 75 °C).
  - Optional anneal at 190–310 °C for 1–30 min (example 250 °C / 5 min). Claimed crystallinity is >7% by WAXS.
  - Example 4 "adhesion" test (pull-out force ÷ contact length, Zwick at 5 mm/min) on 3 mm wires with about 75 µm sheath, held 20 min at temperature. Given the heat-welding claims, this is most likely wire-to-wire heat-weld bond strength, not sheath-to-copper adhesion. Pseudo-amorphous 7000-series PEKK reached 7.5–16.8 N/mm at 200–250 °C. The 8000-series grade (T ≈80%) bonded weakly (1.9 N/mm at best), and crystalline 8000 did not bond.
  - Dielectric constant target ≤3.5, preferably ≤3.1, at 1 kHz (IEC 62634-2-1). Preferred thickness 50–250 µm.
  - It also claims heat-welding turns of the coil together. Examples are round wire only, with no PDIV or bend data.
  - — [US12148548B2](https://patents.google.com/patent/US12148548B2/en)
- Arkema presented "PEKK – A High Performance Thermoplastic For Wire Insulation" (Z. Eckel) at IWCS on 12 Oct 2022; no abstract or data is posted. — [Arkema IWCS 2022 page](https://hpp.arkema.com/en/media/event/hpp/2022/IWCS/)
- Essex co-extrusion patent claim 12: PEKK as the outer, higher-thermal-index layer over a lower-index first layer, total 15–200 µm. — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- Furukawa blend patent lists the crystalline resin (A) as PEEK, PEKK, PEK, PEKEKK or PPS, blended with an amorphous resin (B) of PPSU, PSU, PES, PEI or TPI. — [US10037833B2](https://patents.google.com/patent/US10037833B2/en)
- The Rosendahl Nextrom RA-I hairpin line lists PEEK, PAEK, PEKK, PSU, PPSU, PPS and TPI as processable insulation materials. — [WIRE, 26 Oct 2023](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more)

### Inferences
- PEKK's slower crystallisation (at T ≈60–70%) allows an amorphous, bondable (heat-weldable) extruded state that can be annealed later. That suggests a test variant: form hairpins in the pseudo-amorphous state, then anneal, compared with forming after crystallisation. The patent is aimed at heat-welding, so the forming benefit is unproven.
- PEKK extrudes 20–50 °C cooler than PEEK (330–350 °C versus about 375–400 °C), which eases conductor preheat and tooling. This is a modest process advantage, not shown on rectangular wire.

### Gaps
- No rectangular-conductor PEKK data (PDIV, bending, ATF) and no commercial PEKK magnet-wire product were found. PEKK Tg/Tm values for Kepstan 6000/7000 were not retrieved from an opened source.
- Victrex LMPAEK/AE 250 and Victrex PEK (HT) wire use: no sources found.
- The Kepstan εr "2.9" and "adheres to metal without a primer" appeared only in a search snippet and were not confirmed on the opened Arkema pages.

## 3. Other extrudable high-temperature thermoplastics on flat wire: PPS, PEI, PPSU/PSU/PES, TPI (AURUM), PA/PPA/PET, LCP, fluoropolymers

### Takeaway
PPS, PEI, PPSU and TPI have all been extruded over enamelled rectangular copper in Furukawa/Essex patent work, at PDIVs comparable to PEEK for the same thickness. Each has a hairpin limitation:
- PPS: Tm about 278–285 °C (fails 300 °C heat tests) and UV-sensitive.
- PEI and PPSU: amorphous with Tg about 215–225 °C, so stress-cracking and solvent risks; they are used mainly as tie layers or co-extruded inner layers.
- TPI: Tg 245 °C, a promising niche.

No commercial PPS-, PEI- or TPI-extruded hairpin wire product was confirmed. Fluoropolymer (PFA) rectangular extrusion is available from Zeus but no EV hairpin use was found. No LCP wire-extrusion data was found.

### Cited Findings

**PPS**
- Furukawa US10109389B2: PPS (Polyplastics FORTRON 0220A9) extruded over about 80–85 µm of three-layer enamel on rectangular Cu. No bend cracks; breakdown after bending 7.3–8.5 kV. — [US10109389B2](https://patents.google.com/patent/US10109389B2/en)

  | PPS thickness | Total thickness | PDIV |
  |---|---|---|
  | 45 µm | 125 µm | 1,400 Vp |
  | 80 µm | 165 µm | 1,800 Vp |
  | 115 µm | 195 µm | 2,150 Vp |
  | 180 µm | 260 µm | 2,840 Vp |
  | 195 µm | 275 µm | 2,950 Vp |

- Furukawa/Denso US8847075B2 (priority 2011): PPS 100–105 µm over 30–34 µm plasma-, corona-, primer- or UV-treated PAI or PAI+PI on 2.4 × 3.2 mm rectangular Cu gave PDIV 1,460–1,500 Vp and breakdown 21.4–22.5 kV with no adhesive layer. The PPS had Tm ≈280 °C and Tc ≈120 °C. Comparatives with a 3 µm PPSU adhesive layer gave PDIV 1,048–1,480 Vp and poorer solvent resistance. — [US8847075B2](https://patents.google.com/patent/US8847075B2/en)
- Furukawa US9514863B2: PPS (grade "FZ-2100") extruded at barrel zones 260/300/310 °C, head 320 °C, die 330 °C. PPS with melting point 278 °C (Comp. Ex. 10: PAI 35 / PEI 10 / PPS 121 µm, PDIV 2,150 Vp) failed the 300 °C/168 h heat-resistance criterion. — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Hi-ECOWIRE (Materia Nova, Belgium): PPS is semicrystalline, "melts at 285 °C", needs at least 315 °C processing to avoid high pressure, "has poor resistance to UV light", and can be blended with PPSU or PEI. — [Hi-ECOWIRE technical sheet (PDF)](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- Essex says earlier PPS-over-enamel wire "required an adhesive layer". — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- Mercedes-Benz/RWTH tested PPS insulation on a hairpin conductor (EDPC 2020). — [FAU CRIS](https://cris.fau.de/publications/270664426)
- Syensqo positions Ryton PPS for "precision components", not wire, in the Mavel motor. — [e-Mobility Engineering](https://www.emobility-engineering.com/?p=16587)

**PEI (SABIC ULTEM)**
- Hi-ECOWIRE: PEI is amorphous with "glass transition temperature about 215–225 °C", "must be processed at around 360 °C", and has adhesive properties. — [Hi-ECOWIRE sheet](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- Essex US12278026B2 Table 1 (PAI base, 3.384 × 1.834 mm Cu):
  - ULTEM 1000 extruded single layer, 324 µm: PDIV 1,513 V, shotbox breakdown 16,046 V.
  - Co-extruded PEI (inner) / PEEK (outer), 280 µm: PDIV 2,758 V, breakdown 11,480 V.
  - — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- Furukawa used PEI as a 5–11 µm baked tie layer between PAI and PEEK ([US9514863B2](https://patents.google.com/patent/US9514863B2/en)). It also used PEEK/PEI blends, e.g. PAI 39 µm + PEEK/PEI 150 µm for 189 µm total. In blends, PEEK at 51 mass% or more gave over 100% elongation against an ≥80% requirement ([US10037833B2](https://patents.google.com/patent/US10037833B2/en)).

**PPSU / PSU / PES (Syensqo Radel / Udel / Veradel)**
- Essex US12278026B2: on Cu with PAI base, Radel 5800 PPSU extruded at 354 µm gave PDIV 1,764 V and breakdown 12,636 V, and PPSU/PAEK co-extruded at 250 µm gave 2,248 V and 13,940 V. Co-extruded PPSU/PEEK on a rectangular Al conductor:

  | PPSU/PEEK ratio | Thickness | PDIV | Breakdown |
  |---|---|---|---|
  | ~75/25 | 112 µm | 1,602 V | 4,733 V |
  | ~55/45 | 166 µm | 1,758 V | 9,250 V |

  The text describes PPSU as a 200 °C thermal-class material versus ≥240 °C for PEEK. — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- Hi-ECOWIRE: PPSU is amorphous, Tg about 220 °C, with "high hydrolytic resistance". — [Hi-ECOWIRE sheet](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- Furukawa US9514863B2: PPSU (Radel RS800, Tg 220 °C) is an alternative tie layer. A double extrusion of PES 50 µm + modified PEEK/PPS 50 µm (Comp. Ex. 11/12, 145 µm, PDIV 1,800 Vp) had poorer interlayer adhesion. — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Rea Magnet Wire US7125604B2 (2004; expired): rectangular magnet wire with polyphenylsulfone (RADEL R "rated 180 °C", ACUDEL "220 °C") or a TFE copolymer (HYFALON) extruded only on the minor-axis edges and shoulders. Extrusion is in line, after continuous extrusion of the conductor itself, and uses about 75% less polymer. — [US7125604B2](https://patents.google.com/patent/US7125604B2/en)
- MFL/Frigeco reports "progress with PEEK and PPSU insulated magnet wire". — [Wire & Cable India](https://www.wirecable.in/?p=32084)

**Thermoplastic polyimide (Mitsui AURUM)**
- Mitsui: Tg 245 °C, "100 °C higher than PEEK resin". Mould shrinkage 0.7%, about half of PEEK's 1.5–2.0%. Wire extrusion coating is listed (aerospace). No εr, dielectric strength or RTI is on the page. — [Mitsui AURUM](https://us.mitsuichemicals.com/service/product/aurum.htm)
- WIRE magazine (22 Apr 2024): TPI-coated magnet wires suit "high-voltage applications (800V and above)", with "comparative tracking index (CTI) >600V". Extruded layers can be "30% to 40% thinner than PEEK", which is a vendor claim. Stable "well above 150 °C continuously". Sold in Europe by Bieglo GmbH, Hamburg. — [WIRE: Polyimide coated magnet wires](https://umformtechnik.net/wire/Content/Reports/Polyimide-coated-magnet-wires)
- Furukawa/Denso US8847075B2 Ex. 6: TPI 105 µm extruded over plasma-treated PAI+PI 30 µm on rectangular Cu gave PDIV 1,460 Vp and breakdown 22.4 kV. — [US8847075B2](https://patents.google.com/patent/US8847075B2/en)

**PET / polyester / nylon / PA / PPA**
- US8847075B2 Ex. 5: PET 103 µm extruded over PAI 34 µm on rectangular Cu gave PDIV 1,450 Vp and breakdown 24.2 kV. — [US8847075B2](https://patents.google.com/patent/US8847075B2/en)
- Essex co-extrusion claim 1 allows polyester, nylon, PPS or PPSU as the lower-thermal-index first layer under PEEK/PAEK/PEKK. — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- Arkema Rilsan PA11 is used for busbars (cross-head extrusion or overmolding), not magnet wire. — [Arkema EV page](https://hpp.arkema.com/en/markets-and-applications/automotive-and-transportation/electric-vehicles)
- Syensqo Amodel PPA is used for busbars and high-current connectors. — [e-Mobility Engineering](https://www.emobility-engineering.com/?p=16587)

**Fluoropolymers (PFA/FEP/ETFE)**
- Zeus: "Round, square, and rectangular profiles are available for both PEEK and PFA". PFA wire is AWG 2–24 and maintains insulating properties up to 260 °C. Zeus can also extrude PTFE and FEP and make co-extrusions ("double-insulated wire"). — [Zeus PEEK wire page](https://zeusinc.com/products/insulated-wire/peek-wire)
- TRUMPF lists the common hairpin insulations as "PAI", "PEEK" and "Polyamide-imides with polyimide foil (PAI+FEP)". That last one is a tape construction, covered by the film/tape researcher. — [TRUMPF whitepaper (PDF, 2021)](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)

**Equipment-level confirmation**
- Rosendahl Nextrom's RA-I hairpin line processes "PEEK, PAEK, PEKK, PSU, PPSU, PPS, and TPI". — [WIRE, 26 Oct 2023](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more)

### Inferences
- For a ≥180 °C hotspot plus ATF test plan, the realistic extruded candidates are PEEK (reference), PEKK, TPI (AURUM) and PPS as a lower-cost comparison. PPS's 278–285 °C melting point and failure at 300 °C make it marginal for 220 °C-class claims, and its UV sensitivity matters if corona is present.
- PEI and PPSU are best used as thin tie layers or co-extruded inner layers under PEEK, not alone. Their Tg of about 215–225 °C and amorphous structure suggest ATF/solvent stress-cracking risk at 150–180 °C, so test them in hot ATF if used. This is inferred from polymer class; no ATF data was found.
- At equal total thickness, PPS-over-enamel and PEEK-over-enamel give very similar 25 °C PDIV (US10109389: about 1.4 kVp at 125 µm, about 2.15–2.2 kVp at 195–200 µm). Material choice between them will therefore turn on thermal class, hot PDIV, ATF and forming behaviour, not room-temperature PDIV.
- PFA has very low permittivity and outstanding chemical resistance, but no hairpin-specific data was found on creep or cut-through under slot pressure, or on forming. Treat it as a lab-only candidate.

### Gaps
- No LCP wire-extrusion data or product was found.
- PPS resin grades from Toray (Torelina), Kureha (Fortron KPS), DIC and Solvay (Ryton) specifically for magnet wire were not confirmed. The patents identify only Polyplastics FORTRON 0220A9 and "FZ-2100", which is likely a DIC grade by its designation (inference).
- No commercial PPS-, PEI-, PPSU- or TPI-extruded rectangular hairpin wire product was found, and no ATF ageing data for any of them.
- εr and dielectric strength for AURUM and PFA were not obtained from opened sources.

## 4. Multi-layer / co-extrusion concepts and extrusion over enamel

### Takeaway
Three architectures are documented:
- **Enamel + extruded PEEK**, with or without a thin PEI/PPSU tie layer or a plasma-functionalised enamel surface (Furukawa, Essex). This is the most data-rich option and most likely the series construction for Essex Furukawa.
- **Single-layer PEEK directly on copper** (Ampact, KT-857, Zeus).
- **Two co-extruded thermoplastics**: an amorphous inner layer (PEI, PPSU, PSU, PES, PPS, nylon or polyester) of at least 55% of thickness under a PEEK/PAEK/PEKK skin (Essex, 2020 priority). On hairpin copper, PEI/PEEK at 280 µm reached PDIV 2,758 V.

Double extrusion of different resins without a designed interface had poor interlayer adhesion in Furukawa's tests.

### Cited Findings
- Essex US12278026B2 (priority 7 Aug 2020; Essex Solutions USA):
  - Claim 1: co-extrude a first layer of polyester, nylon, PPS or PPSU (lower thermal index), making up at least 55% of insulation thickness, and a second layer of PEEK, PAEK or PEKK. The extruded insulation must have PDIV of at least 1,200 V.
  - Claim 12: PEKK outer layer, total 15–200 µm. Claim 17: total 250–600 µm.
  - The description also covers PEI/PEEK, PESU/PEEK and PSU/PEEK pairs, with the first layer directly on the conductor or over PI/PAI enamel. It says bonding works "without the use of a bonding agent, adhesion promoter, or adhesive layer", with optional tie layers.
  - Conductor preheat is "approximately 180 °C or greater, 200 °C or greater", followed by a water trough.
  - Data are in sections 1 and 3: PEI/PEEK 280 µm, PDIV 2,758 V; PPSU/PAEK 250 µm, 2,248 V.
  - — [US12278026B2](https://patents.google.com/patent/US12278026B2/en)
- Essex US9324476B2: enamel (PI or PAI) + extruded PEEK/PAEK bonded without adhesive. Total 85–240 µm; PDIV >1,300 V; 220 °C. — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- Furukawa US9514863B2:
  - PAI enamel ≤60 µm + PEI or PPSU tie layer 2–20 µm + extruded PEEK ≤200 µm. A total of 50 µm gives ≥1,000 Vp and 80 µm gives ≥1,200 Vp.
  - Double extrusion of two different resins (PES 50 µm + modified PEEK/PPS 50 µm) gave "poorer coating-to-coating adhesion".
  - Single PEEK on bare copper (Comp. Ex. 3) reached 2,220 Vp but is shown as failing ("✕") the post-winding/heating dielectric test (symbol-column alignment uncertain in the extracted table).
  - — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Furukawa US10109389B2: three baked enamel layers (e.g. PAI/PI/polyester, about 80 µm) + extruded PEEK or PPS. An interlayer adhesion window of 5–10 g/mm is needed to avoid crack propagation in bending. — [US10109389B2](https://patents.google.com/patent/US10109389B2/en)
- Furukawa/Denso US8847075B2: an enamel surface functionalised by plasma, corona, primer or UV replaces the adhesive layer under PPS, PET or TPI extrusions. — [US8847075B2](https://patents.google.com/patent/US8847075B2/en)
- Furukawa US10037833B2:
  - A single extruded blend layer of crystalline PEEK/PEKK/PEK/PEKEKK/PPS with amorphous PPSU/PSU/PES/PEI/TPI, at mass ratio 90:10 to 51:49.
  - Tg of the amorphous resin must exceed that of the crystalline resin by at least 30 °C.
  - Layer thickness 5–250 µm; total 50–300 µm (preferred 60–200 µm).
  - Above 90:10, the breakdown-voltage loss on winding was not suppressed; below 51:49, elongation and thermal ageing suffered.
  - — [US10037833B2](https://patents.google.com/patent/US10037833B2/en)
- Arkema US12148548B2: a two-layer PEKK sheath. The inner 7000-series layer is crystallised by annealing at 250 °C for 5 min, then an outer 6000-series layer is extruded and air-cooled to stay pseudo-amorphous for heat-welding. — [US12148548B2](https://patents.google.com/patent/US12148548B2/en)
- Bekaert: "PEEK is available as single layer (superior) or dual layer coating solution (>100 µm)". — [Bekaert deck](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf)
- Zeus offers "co-extrusions (double-insulated wire)". — [Zeus PEEK wire page](https://zeusinc.com/products/insulated-wire/peek-wire)
- Rosendahl RA-I is specified as "single layer". — [WIRE 2023](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more)

### Inferences
- For the test plan, a useful construction ladder on the same bare conductor would be:
  - (a) single-layer PEEK on bare copper;
  - (b) about 20–40 µm PAI + PEEK;
  - (c) about 20–40 µm PAI + about 5–10 µm PEI tie + PEEK;
  - (d) co-extruded PEI/PEEK or PPSU/PEEK, at matched total thickness (e.g. about 150 µm and about 200 µm).

  This separates adhesion, crack-propagation and PDIV effects. It requires access to an enamel line and an extrusion line with tandem or co-extrusion capability.
- On the same 3.384 × 1.834 mm copper with PAI base, co-extruded PEI/PEEK gave about 9.9 V/µm of PDIV against about 6.6 V/µm for the 182 µm PEEK control. The single control value looks anomalously low next to the 1.68–1.9 kV that 120–160 µm PEEK gave on aluminium, so treat this comparison cautiously.

### Gaps
- No public data was found on enamel+PEEK or co-extruded constructions after ATF ageing, or on hairpin-specific edgewise bending.
- No information was found on which construction Bekaert's "dual layer" uses.

## 5. Process: crosshead tooling for rectangular profiles, melt temperature, conductor preheat, cooling/annealing, line speed, minimum wall, corner uniformity

### Takeaway
Industrial hairpin PEEK lines use a dedicated flat-conductor crosshead on a high-temperature extruder. Rosendahl Nextrom's RA-I runs up to 60 m/min with walls of 0.03–0.4 mm on 0.5–15 mm² conductors at aspect ratios 1:1–1:8; MFL/Frigeco is another line supplier. Typical PEEK settings:
- Resin dried at 120–150 °C for 3–5 h to ≤0.02% moisture.
- Barrel 365–385 °C, die >390 °C, melt about 375 °C at the die exit (Victrex). Furukawa used zones of 300/380/380 °C, head 390 °C and die 400 °C.
- Conductor preheat 100–200+ °C; Essex uses ≥200 °C to bond PEEK to enamel without adhesive.
- Water quench, with optional post-heating or annealing to set crystallinity (≥50% in Furukawa examples).

No opened source compared pressure versus tubing (draw-down) tooling for rectangular conductors.

### Cited Findings
- Rosendahl Nextrom RA-I:
  - A "specially developed crosshead for flat conductors" with high-temperature extruder technology, and all components from pay-off to take-up synchronised.
  - "Production speed up to 60m/min"; single-layer wall "typically 0.03mm – 0.4mm"; cross-sections "typically 0.5mm² – 15mm²"; thickness/width ratio 1:1 to 1:8.
  - Breakdown voltage is "several times" higher than enamel, and extrusion beats enamelling in speed and energy "by far".
  - "Extruded hairpins are already used in premium and sports cars."
  - — [WIRE, 26 Oct 2023](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more)
  - Rosendahl presented this as "the first industry-ready PEEK extrusion line for hairpin wire" at wire Eurasia (14 Mar 2025). — [Expometals](https://www.expometals.net/en/hall/equipment/extrusion-equipment/stand/rosendahl-nextrom-gmbh/news/rosendahl-nextrom-at-wire-eurasia-advancing-cable-manufacturing-for-the-future)
- MFL Group (Frigeco brand, Italy, 5 Sep 2024):
  - Supplies machinery for the whole PEEK magnet-wire process "from the initial rod breakdown machine to the final extrusion process".
  - Manages the crystalline phase to reach minimal insulation thickness.
  - Cites motor voltages up to 1,000 V and PEEK service up to 240 °C.
  - Planned a PEEK testing extrusion line at Spinetoli, Italy.
  - — [Expometals](https://ssr.expometals.net/en/hall/plants/stand/mfl-group/news/peek-extrusion-lines-tackling-new-electrical-insulation-challenges)
  - Frigeco has over 10 years of PEEK cable lines, mainly for oil-pump cable. — [Wire & Cable India](https://www.wirecable.in/?p=32084)
- VICTREX XPI 150 typical extrusion settings: drying 120–150 °C for 3–5 h, max moisture 0.020%, hopper <100 °C, barrel 365–385 °C, die >390 °C, melt "nominally 375 °C exiting die", conductor preheat "usually 100 to 200 °C; >200 °C depending on wire requirements". — [XPI 150 datasheet](https://victrex.com/de/downloads/datasheets/victrex-xpi-150-polymer)
- Furukawa US9514863B2 (lab line):

  | Item | PEEK (KT-820) | PPS ("FZ-2100") |
  |---|---|---|
  | C1 | 300 °C | 260 °C |
  | C2 | 380 °C | 300 °C |
  | C3 | 380 °C | 310 °C |
  | Head | 390 °C | 320 °C |
  | Die | 400 °C | 330 °C |

  The extruder used a 30 mm full-flight screw, L/D 20, compression ratio 3. Extrusion temperature is about 40–60 °C above Tm. The wire was water-cooled 10 s after extrusion (alternatively cooled to about 250 °C and then air), giving crystallinity ≥50% (62–71%). — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Furukawa US10037833B2 (PEEK/PPSU and PEEK/PEI blends): preferred zones C1 260–310 °C, C2 300–380 °C, C3 310–380 °C, head and die 320–390 °C; example 300/370/380/390/390 °C. — [US10037833B2](https://patents.google.com/patent/US10037833B2/en)
- Essex: preheat the conductor to ≥200 °C (≈400 °F) to bond PEEK to enamel without adhesive; post-extrusion heating "maintains temperature and helps attain crystallinity"; quench in a water bath whose cooling rate is set by liquid temperature and quencher length. Annealing also softens the conductor (elongation, spring-back), described qualitatively. — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- Arkema PEKK lab line: heat-gun preheat set to 500 °C, extrusion at 330–350 °C, 10–13.3 m/min, and fast cooling to keep PEKK pseudo-amorphous. — [US12148548B2](https://patents.google.com/patent/US12148548B2/en)
- Enamel comparison (Furukawa): about 5 µm per pass in an 8 m furnace at 450 °C, about 15 s per pass. A 40 µm PAI layer took eight passes. — [US9514863B2](https://patents.google.com/patent/US9514863B2/en); [US10109389B2](https://patents.google.com/patent/US10109389B2/en)
- Corner and thickness-distribution parameters in patents:
  - Corner radius r ≤0.6 mm (preferred 0.2–0.4 mm) is used "in terms of suppressing partial discharge from corners". — [US10109389B2](https://patents.google.com/patent/US10109389B2/en)
  - Example chamfer 0.3 mm on 1.8 × 3.4 mm. The thickness ratio between opposing face pairs is allowed at 1.01–5, i.e. the edge and flat faces may be deliberately different. — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
  - Concentricity (thickness non-uniformity) 1.1–1.5 claimed and 1.1–1.8 described. — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- Minimum wall: Rosendahl 30 µm; Zeus 25 µm; Furukawa claims extruded layers down to 5–20 µm, with ≥40 µm preferred. — [WIRE](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more); [Zeus](https://zeusinc.com/products/insulated-wire/peek-wire); [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Inline quality control: Zeus PEEK wire is "100% AC spark tested during extrusion". — [Zeus datasheet](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf)
- Energy and solvents:
  - Victrex claims "up to 60% less energy" than enamelling. — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)
  - Solvay says monolayer extrusion "requires less energy" with no VOCs. — [CompositesWorld](https://www.compositesworld.com/products/peek-for-monolayer-e-motor-magnet-wire-insulation)

### Inferences
- PEEK melt at 375–400 °C on a copper core preheated to about 200 °C makes crystallinity a function of quench timing. The Furukawa 10 s air gap before the water quench gave ≥50% crystallinity. Crystallinity, measured by DSC on stripped insulation, should be recorded per sample, because it drives Tg-range stiffness, ATF resistance and forming cracks.
- Rectangular crosshead dies can set the edge-to-face thickness ratio (patents allow 1.01–5). Extrusion should therefore give better corner coverage control than enamel, which tends to thin at corners. That enamel-corner claim is not sourced here; check against the enamel researcher's file.

### Gaps
- No opened source compared pressure versus tubing (draw-down) tooling for flat PEEK. PEEK's melt viscosity and the need for adhesion suggest pressure or semi-pressure tooling, but this is unverified.
- No opened source gave enamel line speeds for direct comparison with 60 m/min, or industrial PEEK flat-wire line speeds other than Rosendahl's "up to 60 m/min".
- No measured corner-versus-face thickness distribution for commercial extruded PEEK hairpin wire was found.

## 6. Prototype feasibility: short cut bare conductors vs continuous wire; toll-extrusion / prototype services; minimum order lengths

### Takeaway
Every documented extrusion route is continuous, from pay-off through crosshead and cooling to take-up, including lab lines at 10–13 m/min. No source describes extruding thermoplastic onto short cut bare bars. For a prototype test plan, the practical routes are:
- buy pre-insulated PEEK flat wire on spools from Zeus (custom rectangular PEEK and PFA, walls from 25 µm), hpw, Bekaert, Essex/Essex Solutions or Jiateng;
- send the team's own bare flat wire, as a continuous coil, to an extrusion trial partner such as MFL's planned Spinetoli test line or Rosendahl/MFL demonstration lines;
- for cut lengths, use melt processes that work on discrete parts (insert overmolding) or the tube, heat-shrink and powder routes covered in sibling files.

No minimum-order-length data was found.

### Cited Findings
- Rosendahl RA-I: "Every component from pay-off to take-up is synchronised", a continuous process. — [WIRE 2023](https://umformtechnik.net/wire/Content/Reports/Paving-the-way-for-800V-and-more)
- Arkema's lab-scale PEKK extrusion was still a continuous wire run, at 10–13.3 m/min with heat-gun preheat. — [US12148548B2](https://patents.google.com/patent/US12148548B2/en)
- Zeus offers PEEK and PFA in rectangular profiles, wall from 0.025 mm, spools up to 200 lb, "custom shapes available upon request", and PEEKshrink tubing for splices. — [Zeus page](https://zeusinc.com/products/insulated-wire/peek-wire); [Zeus datasheet](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf)
- MFL Group planned a "PEEK testing extrusion line" at its Spinetoli (Italy) facility (Sept 2024). — [Expometals](https://ssr.expometals.net/en/hall/plants/stand/mfl-group/news/peek-extrusion-lines-tackling-new-electrical-insulation-challenges)
- Materia Nova (Mons, Belgium) is an R&D partner in the Interreg NWE project Hi-ECOWIRE. The project develops "environmental-friendly coating alternative based on the combination of a high thermal resistant polymeric layer (using extrusion process) and a primer (based on sol-gel) to ensure high adhesion on copper wire". Its lab has a Thermo Fisher Process 11 twin-screw compounder and Babyplast injection moulding. Contact: hi-ecowire@materianova.be. — [Hi-ECOWIRE sheet](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- Series suppliers: hpw ([press release](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L)), Bekaert Ampact ([deck](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf)), Essex Furukawa ([release](https://kyodonewsprwire.jp/index.php/release/202108138772)) and Jiateng ([ifeng](https://tech.ifeng.com/c/8lbM26LSIAO)).
- Victrex offers "expert on-site or remote" processing support and a partner ecosystem (wire makers, impregnation-resin and oil-compatibility partners), and says it has "abundant data" on hairpin XPI wire. — [Victrex JP e-book](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)

### Inferences
- Crosshead extrusion onto cut hairpin-length bars of about 0.3–1 m is not practical. Threading, start-up and steady-state melt and quench conditions require a continuous moving conductor, and start-up scrap would exceed the part length (no source quantifies start-up length).
- If the team insists on its own bare cut conductors, two options exist. One is to butt-weld cut bars into a continuous strand with a leader wire, which risks die damage and defects at the joints. The other is to buy the same bare flat wire as a coil and have it extruded.
- The most efficient prototype path is probably dual. First, procure spool samples of commercial PEEK flat wire, single-layer and enamel+PEEK, at about 100/150/200 µm, and run them through the forming, PDIV and ATF plan. In parallel, use an extrusion trial partner (MFL test line, Rosendahl/MFL demo lines, Zeus custom runs, or a resin supplier's tech centre via Victrex or Syensqo) for non-commercial materials such as PEKK, TPI, PPS and co-extrusions.

### Gaps
- No public toll-extrusion price lists, minimum order lengths or sample spool lengths were found for any supplier.
- Whether Rosendahl or MFL demonstration lines accept customer conductor for trials was not confirmed.
- Victrex, Syensqo and Arkema application-centre trial services for wire were not detailed in opened sources.

## 7. Hairpin-specific issues: forming (edgewise/flatwise bending, twisting), stripping before welding, slot-fill penalty, cost

### Takeaway
Suppliers claim PEEK forms more tightly than PAI: Bekaert shows "PAI crack / PEEK no crack" at a 1× thickness bend, and Victrex claims ≥2× tighter radius. The patent record shows three real failure modes:
- cracks running to the conductor when interlayer adhesion is too high;
- loss of post-winding breakdown above about 200 µm of extrusion, and apparently with PEEK directly on copper in a 2012 design;
- cracking under combined thermo-mechanical stress, the root cause of all hairpin breakdowns in Mancinelli 2017.

PEEK laser-strips well as a volume absorber, but more slowly per area than PAI (4 cm²/s versus about 7 cm²/s average and 13 cm²/s maximum in TRUMPF's tests). Thicker insulation costs slot fill. On a 3.5 × 2.0 mm conductor, copper's share of the insulated cross-section falls from about 94% at 40 µm to about 80% at 150 µm (computed). Supplier claims that slot liners can be removed may partly offset this. No resin or wire price data was found.

### Cited Findings

**Forming**
- Bekaert requires "bending of 1x wire thickness"; its image shows "PAI crack / PEEK no crack". — [Bekaert deck](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf)
- Victrex claims "at least 2x tighter bending radius" for hairpin and wave winding ([e-motor page](https://www.victrex.com/en/emotor-solutions)) and "half the bending radius of enamel" ([JP e-book](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)).
- hpw claims PEEK "allows significantly tighter bending radii". — [hpw](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L)
- Essex enamel+PEEK test: about 25% elongation plus a ≥90° bend around a 4.0 mm mandrel. Claim 22 covers adhesion after this test. — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- Furukawa bend test: 5 µm scratch, then a 180° bend around a 1.0 mm iron core. Too-high interlayer adhesion (Comp. 6/7) let cracks reach the PAI layer or the conductor. — [US10109389B2](https://patents.google.com/patent/US10109389B2/en)
- Furukawa winding test: 30 mm mandrel, 280 °C for 30 min, then 10 kV for 1 min. Per the patent text, an extruded layer >200 µm (Comp. Ex. 9, 220 µm) gave poorer breakdown after winding + heating. PEEK directly on copper without adhesive (Comp. Ex. 3) is shown as "✕" in the extracted table (alignment uncertain). — [US9514863B2](https://patents.google.com/patent/US9514863B2/en)
- Furukawa blend layers: elongation >100% with PEEK ≥51 mass% (requirement ≥80%). Heat-aged winding test: 10 turns on a 30 mm core, 200 °C for 30 min, then breakdown. — [US10037833B2](https://patents.google.com/patent/US10037833B2/en)
- Hairpin motor qualification: under combined thermal and vibration ageing, "the root cause for breakdown was, in all cases, traced back to cracks", and turn-to-turn insulation was the weakest link. — [Mancinelli et al. 2017](https://cris.unibo.it/handle/11585/598944)

**Stripping before welding**
- TRUMPF (2021): "PEEK behaves as a volume absorber for laser light anyway", whereas PAI and PAI+FEP need a first pass to carbonise. — [TRUMPF whitepaper](https://chargedevs.com/wp-content/uploads/2021/04/TRUMPF_Whitepaper_Laser-stripping_welding_EV.pdf)
  - Removal rates: PAI up to 13 cm²/s (average 7 cm²/s) with TruMicro; PEEK-coated hairpins 4 cm²/s with TruMark.
  - Laser is "40 and 80% faster than mechanical processes".
  - TruMicro 7070: 2 kW average, 100 mJ maximum pulse; parameters >20 kHz, >40% pulse and line overlap, >40 mJ.
  - Strategies: four sides at 90° for large cross-sections; three at 120°; two at <60°, which risks residues.
- Victrex: "Mechanical and laser stripping" both work (no parameters). — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)

**Slot fill / thickness**
- XPI 80–300 µm versus enamel 5–100 µm. — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)
- PAI 40–80 µm for 400 V BEVs; PEEK dual layer >100 µm. — [Bekaert deck](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf)
- Up to 180 µm for high-voltage motors. — [CompositesWorld](https://www.compositesworld.com/products/peek-for-monolayer-e-motor-magnet-wire-insulation)
- For some applications "little or no varnish is needed, and slot liners may not be required". — [Zeus](https://zeusinc.com/products/insulated-wire/peek-wire)
- XPI may allow "elimination or reduction of secondary insulation materials". — [Victrex JP e-book](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)
- Compatibility with "many standard varnishes/potting compounds" is confirmed with unnamed resin suppliers. — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)

**Cost**
- No price per kg or per metre was found.
- Victrex simulation claims a 2% smaller battery, a potential US$270 per battery at 2018 prices, and up to 60% less coating energy. — [Victrex JP e-book](https://cdn.victrex.com/-/media/downloads/literature/ja/victrex_auto_ebook_wirecoatings_04_2024.pdf)
- PEEK is "one of the most expensive high-performance polymer on the market". — [Hi-ECOWIRE sheet](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- Solvay claims monolayer extrusion is "faster and more cost-efficient". — [CompositesWorld](https://www.compositesworld.com/products/peek-for-monolayer-e-motor-magnet-wire-insulation)
- The hpw OEM order is worth a "mid three-digit million euro range" amount; no unit price is given. — [hpw](https://webdisclosure.com/press-release/hpw-metallwerk-gmbh-etr-hpw-metallwerk-significantly-expands-production-of-peek-high-performance-wires-and-responds-to-high-demand-in-the-electromobility-sector-4JiKH4q2n8L)

### Inferences
- Slot-fill arithmetic for Bekaert's example 3.5 × 2.0 mm conductor (7.00 mm², corner radii ignored), copper share of the insulated wire cross-section:

  | Insulation per side | Insulated cross-section | Copper share |
  |---|---|---|
  | 40 µm | 7.45 mm² | 94.0% |
  | 80 µm | 7.91 mm² | 88.5% |
  | 150 µm | 8.74 mm² | 80.1% |
  | 200 µm | 9.36 mm² | 74.8% |

  Part of this is offset if the slot liner can be thinned or removed. The test plan should include a "PEEK wire + no or thin liner" variant for PDIV to the stator core.
- From TRUMPF's figures, stripping PEEK may take roughly 1.75–3.3× longer per area than PAI, at unspecified thicknesses. Thicker PEEK also needs a larger ablated volume, so stripping-quality checks should be part of the test plan: residue on the copper before welding, and the heat-affected edge of the insulation.
- Forming tests should cover:
  - the conductor's own minimum radii, flatwise and edgewise, at 1× and 2× thickness;
  - the 3D twist at the crown;
  - crack and delamination inspection after a 5 µm scratch (Furukawa method);
  - breakdown and PDIV after forming plus thermal shock;
  - peel adhesion on formed legs.
- Above PEEK's Tg of 143 °C, stiffness drops. The Zeus dielectric-strength data drop steeply above 200 °C (e.g. 1443 V/mil at 240 °C for the 76 µm wall), so test hot breakdown and PDIV at the intended hotspot (180–220 °C).

### Gaps
- No public edgewise-bending or twist data was found for extruded PEEK rectangular wire, nor springback comparisons with enamel.
- No PEEK-specific laser-stripping parameters for 150–200 µm walls were found. TRUMPF does not state the PEEK thickness behind its 4 cm²/s figure.
- No wire price data (EUR/kg) for PEEK versus PAI enamel flat wire was found.

## 8. Related melt processing: injection overmolding of PEEK/PPS/LCP/PA around conductor sections (busbars, terminals) and relevance to hairpin segments

### Takeaway
Thermoplastic overmolding and crosshead coating are documented for busbars and high-current connectors: PA11 by overmolding or crosshead extrusion; PPA busbars; PEKK busbars for thermal runaway; PPS precision parts. No opened source describes overmolding the insulation of individual hairpin legs. For a test plan, insert-overmolding of PEEK, PPS or PPA onto cut straight conductor segments is a feasible way to make discrete-part specimens. Expect much thicker walls than extrusion, and treat these specimens as a separate method class.

### Cited Findings
- Arkema: for Rilsan PA11 busbar insulation, "The coating can be obtained by injection molding/overmolding or cross-head extrusion", and cross-head extrusion lets you "coat a long length of copper or aluminum". Kepstan PEKK provides "excellent adhesion to conductive metal components" and "reliability under high temperatures" for busbars (thermal-runaway context). — [Arkema EV page](https://hpp.arkema.com/en/markets-and-applications/automotive-and-transportation/electric-vehicles)
- Syensqo materials in Mavel's >800 V motor: Amodel PPA for busbars and high-current connectors, Ryton PPS for precision components, Xencor PPA LFT for structural slot wedges, Ajedium PEEK for slot liners and wedges. — [e-Mobility Engineering](https://www.emobility-engineering.com/?p=16587)
- Rosendahl Nextrom presented its PEEK hairpin line "alongside solutions for bus bar insulation" (Mar 2025). — [Expometals](https://www.expometals.net/en/hall/equipment/extrusion-equipment/stand/rosendahl-nextrom-gmbh/news/rosendahl-nextrom-at-wire-eurasia-advancing-cable-manufacturing-for-the-future)
- Victrex makes only general busbar claims about temperature and flammability, with no numbers. — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)
- AURUM TPI suits powder coating, injection moulding and extrusion, and powder-coated busbars were studied. — [WIRE 2024](https://umformtechnik.net/wire/Content/Reports/Polyimide-coated-magnet-wires)
- PPS's melt fluidity "allows it to be manufactured in complex shaped pieces". — [Hi-ECOWIRE sheet](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf)
- Melt-bonding variant: Arkema claims heat-welding coil turns that carry a pseudo-amorphous PAEK outer layer, followed by crystallisation, as a coil consolidation route. — [US12148548B2](https://patents.google.com/patent/US12148548B2/en)

### Inferences
- Overmolding is the only melt process here that works on short cut bare conductors. It suits straight-leg specimens for breakdown and PDIV, insulated terminal or crown regions, and welded-joint insulation. It also tests realistic resin–copper adhesion and CTE mismatch.
- Overmolding cannot reproduce a thin, uniform 100–200 µm wall over metre-scale lengths, and overmolded specimens cannot be formed afterwards like hairpin wire. Treat them as a separate method class, not a substitute for extruded wire.
- LCP and PPS have the best flow for thin-wall overmolding. PEEK needs high mould temperatures for crystallinity. These are general polymer-processing facts; no hairpin-specific source was opened.

### Gaps
- No opened source covers injection overmolding of insulation onto hairpin conductor segments, minimum moldable wall thickness on copper bars, or PDIV of overmolded copper bars.
- No LCP busbar or overmolding data was opened.

## 9. Material–method summary matrix for the test plan (synthesis of sections 1–8)

### Takeaway
For a SiC-fed 800 V hairpin test plan, extruded PEEK is the best-documented thermoplastic route, either single-layer or over 20–60 µm enamel. PPS, PEKK, TPI and PEI/PPSU co-extrusions are credible comparison variants with patent-level data. Fluoropolymers and LCP lack hairpin evidence. All extrusion variants need continuous conductor; only overmolding works on cut pieces.

### Cited Findings
Values are taken from the cited findings above; each row lists its key sources.

| Material / method | Typical thickness | Thermal rating | εr | Dielectric / PDIV data | Maturity | Proto on cut bare conductor? | Pros | Hairpin risks | Examples | Key sources |
|---|---|---|---|---|---|---|---|---|---|---|
| PEEK, single layer extruded directly on Cu | 80–300 µm (Victrex); ≤180 µm HV (Solvay) | Class 220 °C (Victrex web); RTI 240 °C est. (e-book); polymer UL 260 °C (Zeus) | 3.20 at 1 kHz (XPI 150) | 120/155/160 µm on rectangular Al: PDIV 1,679/1,820/1,905 V; 171 µm on Cu: 2,220 Vp, shown "✕" post-winding (2012 design; verify) | Series (Ampact, Zeus, KT-857 in Mavel motor; hpw construction undisclosed) | No (continuous only) | No solvent; one pass; ductile; ATF 180 °C/2,000 h claim | Adhesion to bare Cu; crystallinity control; thicker wall; slower laser strip | Bekaert Ampact; Zeus; Syensqo KT-857 | [XPI 150](https://victrex.com/de/downloads/datasheets/victrex-xpi-150-polymer), [Victrex](https://www.victrex.com/en/emotor-solutions), [US12278026B2](https://patents.google.com/patent/US12278026B2/en), [US9514863B2](https://patents.google.com/patent/US9514863B2/en), [Bekaert](https://www.bekaert.com/content/dam/corporate/en/events/wire-d%C3%BCsseldorf/docs-mobility/Ampact%20copper%20magnet%20wire%20for%20e-motors.pdf) |
| Enamel (PAI/PI 20–60 µm) + extruded PEEK, ± PEI/PPSU tie layer 5–10 µm | 85–280 µm total | 220 °C continuous (240 °C dependent claim); HVWW "constant 240 °C" | KT-820 3.1 | 120 µm: 1,350 Vp; 200 µm: 2,200 Vp; 280 µm: 3,050 Vp (25 °C) | Series (Essex Furukawa HVWW material undisclosed, likely) | No | Highest PDIV per µm documented; enamel gives adhesion base | Adhesion window (too high leads to cracks); two process lines | Essex Furukawa HVWW | [US10109389B2](https://patents.google.com/patent/US10109389B2/en), [US9324476B2](https://patents.google.com/patent/US9324476B2/en), [Kyodo](https://kyodonewsprwire.jp/index.php/release/202108138772) |
| PEKK (Kepstan) single or two-layer extruded | 69–102 µm lab; 50–250 µm preferred | Not found | Target ≤3.5 (≤3.1) | None found | Lab / patent | No | Lower melt temperature (330–350 °C); amorphous-then-anneal; heat-welding of turns | No rectangular or ATF data | Arkema (no product) | [US12148548B2](https://patents.google.com/patent/US12148548B2/en), [Arkema](https://hpp.arkema.com/en/product-families/kepstan-pekk-polymers/wire-coatings/) |
| PPS extruded over enamel | 45–195 µm PPS; 125–275 µm total | Tm 278–285 °C; failed 300 °C/168 h | Not found | 125 µm: 1,400 Vp; 195 µm: 2,150 Vp; PPS 100–105 µm on 30–34 µm PAI: 1,460–1,500 Vp, 21–22.5 kV | Patent / lab (no product found) | No | Lower cost than PEEK (inference); good flow | Low Tm; UV sensitivity; needs adhesive or surface treatment | Furukawa/Denso patents | [US10109389B2](https://patents.google.com/patent/US10109389B2/en), [US8847075B2](https://patents.google.com/patent/US8847075B2/en), [Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf) |
| PEI (ULTEM 1000) extruded, or as tie/inner layer | 324 µm single; 5–11 µm tie | Tg 215–225 °C | Not found | 324 µm: PDIV 1,513 V, 16 kV; PEI/PEEK 280 µm: 2,758 V | Patent / lab | No | Adhesive; amorphous (no crystallinity control) | Tg limit; ATF/solvent stress cracking (unverified) | Essex co-extrusion patent | [US12278026B2](https://patents.google.com/patent/US12278026B2/en), [US9514863B2](https://patents.google.com/patent/US9514863B2/en) |
| PPSU/PSU/PES extruded, or as co-extruded inner layer | 112–354 µm | PPSU "200 °C" class; Tg ≈220 °C | Not found | PPSU 354 µm: 1,764 V; PPSU/PEEK 166 µm: 1,758 V | Patent / lab | No | Hydrolysis resistance; low shrinkage | Tg limit; interlayer adhesion with PEEK | Essex patents; MFL trials | [US12278026B2](https://patents.google.com/patent/US12278026B2/en), [Hi-ECOWIRE](https://vb.nweurope.eu/media/13371/hi-ecowire_technical_sheet_polymer_extrusion.pdf) |
| TPI (AURUM) extruded | 105 µm (patent example) | Tg 245 °C | Not found | 105 µm on 30 µm PAI+PI: 1,460 Vp, 22.4 kV; CTI >600 V | Lab / niche | No | High Tg; low shrinkage 0.7% | Supply and cost; little data | Mitsui / Bieglo | [Mitsui](https://us.mitsuichemicals.com/service/product/aurum.htm), [US8847075B2](https://patents.google.com/patent/US8847075B2/en), [WIRE 2024](https://umformtechnik.net/wire/Content/Reports/Polyimide-coated-magnet-wires) |
| PET / nylon (low-temperature reference) | 103 µm | Not found | Not found | PET 103 µm on 34 µm PAI: 1,450 Vp, 24.2 kV | Patent | No | Cheap reference | Thermal class too low for 180 °C+ (inference) | — | [US8847075B2](https://patents.google.com/patent/US8847075B2/en) |
| PFA (FEP) extruded on rectangular profile | Not stated | 260 °C | Not found | Not found | Commercial niche (Zeus); no EV hairpin use | No | Chemical inertness | Creep / cut-through; forming; adhesion (unverified) | Zeus PFA | [Zeus](https://zeusinc.com/products/insulated-wire/peek-wire) |
| Co-extruded PEI/PEEK or PPSU/PEEK | 112–280 µm | Outer PEEK ≥240 °C (as described) | Not found | PEI/PEEK 280 µm: 2,758 V; PPSU/PAEK 250 µm: 2,248 V | Patent (Essex, 2020 priority) | No | Better adhesion than PEEK alone (claimed) | Needs co-extrusion crosshead | Essex Solutions | [US12278026B2](https://patents.google.com/patent/US12278026B2/en) |
| Injection overmolding (PEEK/PPS/PPA/PA11) | Not quantified | Resin-dependent | Not found | Not found | Series for busbars; none for hairpin legs | Yes | Works on cut segments | Thick walls; not formable afterwards | Arkema PA11; Syensqo PPA busbars | [Arkema EV](https://hpp.arkema.com/en/markets-and-applications/automotive-and-transportation/electric-vehicles), [e-Mobility Eng.](https://www.emobility-engineering.com/?p=16587) |
| LCP | No data | No data | No data | No data | Not found | Overmolding only (inference) | — | — | — | — |

### Inferences
- A minimum extruded test matrix covering the "PEEK extrusion" method and its realistic alternatives would be:
  - (1) single-layer PEEK, about 150 µm;
  - (2) about 30 µm PAI + about 120 µm PEEK;
  - (3) about 200 µm variants of (1) and (2) for 800 V SiC margin;
  - (4) PPS-over-enamel at matched thickness, as a lower-cost comparison;
  - (5) optionally PEKK or a PEI/PEEK co-extrusion if a trial line is available.

  Variants (1)–(3) are commercially sourceable on spools. Variants (4)–(5) need a trial-extrusion partner.
- Enamel-only references should match total thickness where possible. Enamel's practical maximum is about 120–130 µm (Bekaert, Victrex), so above that the comparison necessarily uses enamel + extrusion or tape.

### Gaps
- Matrix cells marked "Not found" could not be filled from opened sources; the main ones are εr for PPS, PEI, PPSU, TPI and PFA, the PEKK thermal rating, and LCP entirely.
- Thermal-class values are supplier statements, not wire-level IEC 60172 or UL 1446 results.
