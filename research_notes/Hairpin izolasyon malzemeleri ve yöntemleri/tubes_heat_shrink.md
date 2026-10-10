# Tubes and heat-shrink sleeves for insulating bare rectangular (hairpin) copper conductors

Scope: slip-on tubes, heat-shrink tubes, braided and spiral-wound sleeves that could be applied to BARE rectangular hairpin copper for a test plan (PDIV, breakdown, thermal, forming, ATF). Research date: 2026-10-10. Each source is dated where the date is known; anything before 2023 is flagged "(older)". Unit conversions such as V/mil to kV/mm (1 V/mil = 0.03937 kV/mm) and all geometric or PD calculations are my own. They are marked as calculations in the Inferences sections.

## Q1. PEEK tubing and PEEK heat-shrink: walls, shrink ratio, recovery temperature, service temperature, dielectric strength, rectangular/profile availability

### Takeaway
I found only one commercial PEEK heat-shrink: Zeus PEEKshrink™. Its specs: shrink ratio ≤1.4:1, recovered wall about 0.08–0.46 mm, recovery at 300–385 °C (right at PEEK's melting point), 260 °C continuous service and 3500–3570 V/mil. Gunze has a PEEK shrink tube that starts shrinking at 150 °C (≤25 % shrinkage, ID 4.5–20 mm, wall 50–300 µm), but it is still "under development". Extruded, non-shrink PEEK tubing from Zeus and Optinova is round and mostly small-bore (catalogue OD ≤6.35 mm). Neither vendor offers a catalogue rectangular PEEK tube or PEEK shrink. Rectangular PEEK would have to be a custom profile extrusion.

### Cited Findings
**Zeus PEEKshrink™ (heat-shrink)**
- Product page: shrink ratio "up to 1.4:1". Expanded ID up to 2.0″ (50.8 mm). Translucent recovery 572–644 °F (300–340 °C), opaque recovery 680–725 °F (360–385 °C). Continuous service 500 °F (260 °C). Uses listed include "Wire and Cable Encapsulation and Insulation" and "Electrical Component Covering", for industries "ranging from automotive to medical devices". The page mentions no profiled or non-round PEEKshrink — [Zeus PEEKshrink page](https://www.zeusinc.com/products/heat-shrinkable-tubing/peekshrink/)
- Datasheet V1R4 (June 2024), general range:
  - Expanded ID 0.038–2.000″ (0.965–50.800 mm); recovered wall 0.003–0.018″ (0.076–0.457 mm).
  - Standard put-up length 4 ft.
  - Standard AWG series (AWG 17 to AWG 0): expanded ID min 0.965–9.957 mm, recovered ID max 0.686–7.112 mm, wall min/nominal/max 0.127/0.178/0.229 mm (0.005/0.007/0.009″).
  - Example sizes: AWG 8 is 4.064 → 2.896 mm; AWG 7 is 4.420 → 3.150 mm; AWG 6 is 5.080 → 3.632 mm; AWG 5 is 5.613 → 4.013 mm; AWG 4 is 6.401 → 4.572 mm.
  - Source: [Zeus PEEKshrink datasheet V1R4](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf)
- Datasheet V1R4 (June 2024), properties:
  - Tensile modulus 1,309 ksi (≈9.0 GPa, as listed); tensile stress at yield 14,503 psi (≈100 MPa).
  - Tg 321 °F / 161 °C (ASTM D3418).
  - Dielectric strength 3570 V/mil (ASTM D149) ≈ 140 kV/mm.
  - "Thermal Endurance (NEMA MW 1000) 752 °F / 400 °C". Note that 400 °C is an endurance-test figure, not the 260 °C continuous rating on the same sheet.
  - Crystallinity 40 %. The sheet lists "Adhesion to metals" as a key property.
  - Note on the sheet: "Tubing performance and characteristics may change based on tubing size."
  - Source: [Zeus PEEKshrink datasheet V1R4](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf)
- Zeus Heat Shrink Comparison & Recovery Guide V1R7 (August 2026), PEEKshrink row: operating temperature 500 °F (260 °C); ratio up to 1.4:1. Expanded ID 0.038–0.392″ (0.965–9.957 mm), recovered ID 0.027–0.280″ (0.686–7.112 mm), recovered wall 0.005–0.009″ (0.127–0.229 mm). Longitudinal change "TBD". Recovery 650–725 °F (343–385 °C). Dielectric strength 3500 V/mil (≈138 kV/mm). Footnote: "Dielectric strength is dependent on wall thickness. Values shown are for reference only." — [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
- Conflicting figures between Zeus documents:
  - Dielectric strength: 3570 V/mil (2024 datasheet) vs 3500 V/mil (2026 guide).
  - Recovered wall: 0.076–0.457 mm (2024 datasheet) vs 0.127–0.229 mm (2026 guide table).
  - Recovery temperature: 300–340 °C translucent / 360–385 °C opaque (product page and datasheet) vs 343–385 °C (guide).
  - Sources: [V1R4](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf); [Guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
- Recovery practice (Zeus guide 2026):
  - "PEEK, for instance, melts at 650 °F (343 °C) and its heat shrink recovery temperature is very near this same temperature."
  - In Zeus tests a Steinel HG 2310 heat gun with a reflector baffle had to be set to 850 °F (454 °C) to get 640–700 °F (338–371 °C) at the baffle. Zeus calls this "a fine line between complete heat shrink recovery and melting the product."
  - Ovens and vertical laminators are the most reliable methods. The guide rates heat guns and hot boxes as R&D tools with low repeatability.
  - Zeus QC recovers heat shrink "for 10 minutes after the defined oven temperature is achieved."
  - Source: [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)

**Gunze low-temperature PEEK heat-shrink tube (development)**
- Status: "Product under development". The page is undated; its images were uploaded in February 2025.
- Shrinking starts at 150 °C. Gunze says conventional PEEK shrink tube needs at least 320 °C.
- Maximum shrinkage 25 %; inner diameter Φ4.5–20 mm; wall 50–300 µm; maximum length 1,000 mm.
- Target uses: automotive (non-conductive, heat resistant), office equipment and electronics.
- Service temperature and dielectric data appear only as images, which I could not read.
- Source: [Gunze PEEK heat-shrinkable tube](https://www.gunze.co.jp/e/epd/products/peek/)

**Extruded (non-shrink) PEEK tubing**
- Zeus PEEK extruded tubing V2R2 (June 2024): walls down to 0.002″ (0.051 mm); working temperature up to 500 °F / 260 °C; UL 94 V-0. Catalogue sizes are small HPLC sizes, OD 0.020–0.125″ (0.508–3.175 mm). Uses include "Wire harness or cable wrap (spiral wrap)". The catalogue lists no profile shapes — [Zeus PEEK Extrusions V2R2](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEK-Extrusions-V2R2.pdf)
- Zeus custom profiles: "tight-tolerance" custom profile extrusions in PTFE, PEEK, FEP, PFA, PVDF, ETFE, ECTFE and nylon. Zeus makes its dies in-house, and working temperature is up to 500 °F (260 °C) depending on resin. The page mentions neither rectangular profiles nor heat-shrink profiles — [Zeus Custom Profiles](https://zeusinc.com/products/tubing/custom-profiles)
- Optinova, current web page (read 2026-10):
  - ID 0.10–3.2 mm, OD 0.40–6.35 mm, wall 0.038–1.59 mm.
  - ID/OD/wall tolerances ±0.02–0.05 mm.
  - "We can develop sizes larger than OD 1/4″ if desired."
  - Applications include "Insulation for wires in cables for aerospace or EV applications". Material is PFAS-free.
  - Source: [Optinova PEEK Tubing](https://optinova.com/peek-tubing/)
- Optinova datasheet (2022, older):
  - Size range: ID 0.10 mm up to OD 4.00 mm. Raw material Victrex PEEK 381G. Optinova can extrude "multi-lumen, monofilament, and ultra-thin wall" forms.
  - Maximum continuous service 250 °C.
  - εr 3.2 at 23 °C / 50 Hz (IEC 60250) and **4.5 at 200 °C / 50 Hz**.
  - Dielectric strength 23 kV/mm at 2 mm thickness and 190 kV/mm at 50 µm (IEC 60243-1).
  - Volume resistivity 10^16 Ω·cm at 23 °C, 10^15 at 125 °C and 10^9 at 175 °C. These are as printed; the superscripts were lost in text extraction.
  - Water absorption 0.45 % (saturation, 23 °C). Yield strength 98 MPa, elongation at break 45 %, tensile modulus 4 GPa.
  - Elongation at Fmax of sample tubes ranged from 20 % to 379 % (tests at RISE, 2022).
  - Source: [Optinova PEEK datasheet 2022](https://optinova.com/app/uploads/2022/09/optinova-peek-tubing.pdf)
- PEEK dielectric strength vs temperature, from Zeus extruded PEEK magnet wire (same polymer, but wire insulation rather than tube):
  - 0.0015″ wall: 4113 V/mil at 22 °C, 5040 at 180 °C, 3487 at 200 °C, 3133 at 220 °C, 2393 at 240 °C, 153 at 260 °C.
  - 0.003″ wall: 3830, 4393, 3357, 2107, 1443 and 483 V/mil at the same temperatures.
  - Other data: "PEEK polymer is UL rated up to 260 °C"; thermal conductivity 0.29 W/m·K; "custom shapes available upon request".
  - Source: [Zeus PEEK Insulated Wire V2R5 (July 2026)](https://www.zeusinc.com/wp-content/uploads/2026/07/PEEK-Insulated-Wire-V2R5.pdf)
- Older Zeus paper (2014, older): PEEK melts near 343 °C, practical upper service limit 260 °C, Tg 150 °C, dielectric strength 504 V/mil (D149). It gives εr as 2.2–3.0 at 1 MHz (D150), which conflicts with the 3.2–3.3 reported elsewhere. It also reports a 0.75 hp, 460 V, 4-pole induction motor rebuilt with PEEK magnet wire "and other PEEK insulating products" that performed equal to or better than the OEM motor — [Zeus RESINATE No.3 (2014)](https://www.zeusinc.com/wp-content/uploads/2014/03/RESINATE_No3-PEEKInsWire_Zeus.pdf)
- PEEK εr 3.2–3.3 (50 Hz–10 kHz); dielectric strength 190 kV/mm at 50 µm — [Professional Plastics, Electrical Properties of Plastics (2008, older)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)

### Inferences
- **Sizing PEEKshrink on a hairpin-size bar (calculation; method explained in Q6).** Example bar: 4 × 2 mm with 0.5 mm corner radius. This is an illustrative size, not a sourced hairpin dimension.
  - The tube must slip over the bar's circumscribed diameter (4.16 mm) and also recover below perimeter/π (3.55 mm).
  - Of Zeus's standard AWG sizes, only AWG 7 meets both conditions (expanded ≥4.420 mm, recovered ≤3.150 mm).
  - AWG 6 (recovered ≤3.632 mm) would stay slack on the flats. AWG 8 (expanded 4.064 mm) will not slip on.
  - So PEEKshrink is geometrically possible on straight cut samples, but the insertion clearance is only about 0.26 mm (on the diameter).
- **Process on bare copper.** Recovery at 343–385 °C, inside a heat-gun window of a few tens of °C, will likely oxidise bare copper in air and may soften hard-drawn copper. I found no source for either effect. Inert gas or short oven cycles should be tested, and the conductor surface (oxide) included as a test variable.
- **Translucent vs opaque recovery.** Translucent (lower-temperature) recovery probably leaves PEEK less crystalline than the 40 % quoted for the standard product. Amorphous PEEK softens above Tg (about 150–161 °C), so opaque, crystalline recovery is probably preferable for a 180–220 °C class. This needs verification, for example by DSC.
- **PD at temperature.** PEEK's εr rises from 3.2 to 4.5 at 200 °C (Optinova). That increases the share of voltage across any air gap and should lower PDIV at temperature; see the model in Q6. The wire data also show dielectric strength collapsing above about 220–240 °C, so the margin for a 220 °C class is thin.
- **Round extruded PEEK tube as a slip-on sleeve.** The ID must exceed the bar diagonal. On the illustrative 4 × 2 mm bar, a 4.2 mm ID tube leaves about 1.1 mm of air over the middle of each wide face. That is unsuitable for PD testing.
- Only a custom rectangular profile extrusion (Zeus and Optinova both offer custom extrusion) or post-forming of the tube above Tg could give a close fit. That would be a prototype item with die cost.
- **Maturity for hairpin use:**
  - PEEKshrink: commercial product, but lab/prototype for this use, because I found no published hairpin use.
  - Gunze PEEK shrink: development stage.
  - Round PEEK tube: lab reference only.
  - Rectangular PEEK profile: custom prototype.

### Gaps
- I found no catalogue rectangular or flat PEEK tube or PEEK heat-shrink from Zeus, Optinova, Junkosha or Polyfluor.
- Junkosha: a search snippet says it started PEEK tubing production in 2018, but I could not confirm this on a Junkosha page.
- Polyfluor: no PEEK tube or shrink data found.
- Zeus publishes no εr and no longitudinal change ("TBD") for PEEKshrink. I found no PDIV, ATF-immersion or forming (bend) data for PEEKshrink-covered conductors.
- Gunze service temperature and electrical data are image-only and could not be extracted.

## Q2. Polyimide tubing (MicroLumen, Zeus, Nordson/Vention): wall, sizes, rectangular profiles, rating

### Takeaway
Polyimide tubing is film-cast PI, a thermoset, so it cannot be heat-shrunk. All suppliers found stop at about 2.2–2.3 mm ID, far below the diagonal of a hairpin conductor. Wall thicknesses are about 10–250 µm, with ≥4000 V/mil, εr 3.4 and a 220 °C (20,000 h) rating. No rectangular PI tube was found. At hairpin size, the commercially available PI tube is spiral-wound Kapton, alone or as Nomex/Kapton/Nomex laminate (see Q5 and Q7).

### Cited Findings
- Zeus PI tubing V2R9 (July 2026):
  - "Polyimide (PI) is a class of high performing thermoset polymers." Process: film-cast.
  - ID 0.0045–0.090″ (0.1143–2.286 mm); nominal wall 0.0004–0.005″ (0.0102–0.127 mm).
  - Wall tolerance ±25 %; ID tolerance ±0.0051–0.025 mm; cut length up to 78″ (1981.2 mm).
  - Applications include "High temperature insulation" and "Electrical & mechanical insulation".
  - Source: [Zeus Polyimide Tubing V2R9](https://www.zeusinc.com/wp-content/uploads/2026/07/Polyimide-Tubing-V2R9.pdf)
- MicroLumen:
  - ID 0.004–0.086″ (0.10–2.18 mm); wall 0.0005–0.008″ (0.0127–0.2032 mm).
  - Dielectric strength "4,000 Volts/0.001″ Minimum" (≈157 kV/mm); εr 3.4; tensile strength 20,000 psi minimum.
  - "Thermal Rating @ 20,000 Hours: 220 °C Minimum"; "Thermal Endurance: 400 °C Minimum".
  - The page mentions no non-round profiles.
  - Source: [MicroLumen polyimide](https://www.microlumen.com/medical-tubing/polyimide/)
- MicroLumen dimension table runs from code 039 (0.0039″, 0.10 mm) to code 860 (0.0860″, 2.18 mm). "Products are custom manufactured to meet customer specifications" — [MicroLumen dimensions](https://www.microlumen.com/medical-tubing/dimensions/)
- Nordson MEDICAL (formerly Vention/Advanced Polymers):
  - Online stock ID 0.004–0.080″. Custom ID 0.004–0.085″ (≈0.10–2.16 mm); custom wall 0.0005–0.010″ (0.0127–0.254 mm).
  - "Outstanding electrical insulation properties". Nordson also coats wire: "We can insulate any wire material with polyimide".
  - Source: [Nordson polyimide datasheet](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-Polyimide-DS-01-DIGITAL.pdf)
- PI bulk values: εr 3.4 (1 MHz); 22 kV/mm — [Professional Plastics table (2008, older)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)
- Spiral-wound polyimide tubes (Pleo, February 2024): "Kapton tubes" −60 to 220 °C with shrinkage <2 %; "Kapton+Nomex" −60 to 220 °C — [Pleo Tube/Sleeve sheet](https://pleo.com/wp-content/uploads/2024/02/Tube-Sleeve.pdf)

### Inferences
- Film-cast PI tubes cannot be shrunk, so on a rectangle they could only be a loose slip-on with large air gaps. Their maximum ID (≤2.3 mm) also rules them out for hairpin cross-sections. For the test plan, PI tubing is not a feasible "tube" option.
- PI belongs under film or tape wrapping (another researcher's slice) or under spiral-wound tubes made on a rectangular mandrel.

### Gaps
- I found no large-diameter (≥4 mm) or rectangular film-cast PI tubing from MicroLumen, Zeus or Nordson/Vention.
- I found no dielectric or PDIV data for spiral-wound Kapton tubes, apart from the Politubes "up to 12 kV" vendor claim (Q5).

## Q3. Fluoropolymer tubes and heat-shrinks: PTFE, FEP, PFA, ETFE, dual-wall PTFE/FEP melt-liner

### Takeaway
PTFE, FEP and PFA shrinks all have εr ≈ 2.1, the most PD-favourable of any tube material.
- PTFE: up to 4:1, recovery 343 ± 10 °C, 260 °C service, 600 V/mil.
- FEP: 1.3/1.6/2:1, recovery 216 ± 10 °C, 205 °C service, 2000 V/mil.
- PFA: ≤1.6:1, recovery 210 ± 10 °C, 260 °C service, 2000 V/mil.
- Zeus Dual-Shrink melt-liner tubes: PTFE/FEP rated 205 °C, PTFE/PFA ("HTDS") rated 260 °C, both 1.3–1.4:1 with 343 °C recovery. The inner layer melts and fills the space.
- ETFE shrink is rated only 150 °C, below the class target.
- Longitudinal change is ±15–20 %.

### Cited Findings
Unless marked otherwise, the values below come from the Zeus Heat Shrink Comparison & Recovery Guide V1R7 (August 2026) — [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf):

| Product | Operating temperature | Shrink ratio | Expanded ID | Recovered ID | Recovered wall | Longitudinal change | Recovery temperature | Dielectric strength |
|---|---|---|---|---|---|---|---|---|
| PTFE | 500 °F (260 °C) | up to 4:1 | 0.864–101.6 mm | 0.381–26.035 mm | 0.152–0.635 mm | ±20 % | 343 ± 10 °C | 600 V/mil (≈23.6 kV/mm) |
| PTFE Sub-Lite-Wall™ | 260 °C | up to 2:1 | 0.305–9.525 mm | 0.127–4.750 mm | 0.025–0.127 mm | ±20 % | 343 ± 10 °C | 600 V/mil |
| FEP | 400 °F (205 °C) | up to 2:1 | 0.635–50.8 mm | 0.508–31.75 mm | 0.076–0.762 mm (≥1.8:1 versions: 0.254–0.330 mm) | ±15 % | 420 ± 50 °F (216 ± 10 °C) | 2000 V/mil (≈78.7 kV/mm) |
| FEP Lay-Flat™ | 205 °C | up to 1.6:1 | 10.16–127 mm | 6.35–80.772 mm | 0.051–0.508 mm | ±15 % | 216 ± 10 °C | 2000 V/mil |
| PFA | 260 °C | up to 1.6:1 | 0.635–50.8 mm | 0.508–31.75 mm | 0.102–0.508 mm | ±15 % | 410 ± 50 °F (210 ± 10 °C) | 2000 V/mil |
| Dual-Shrink™ (PTFE outer / FEP inner) | 205 °C | 1.3:1 to 1.4:1 | 0.914–25.4 mm | 0–17.78 mm* | up to 1.651 mm* | ±20 % | 343 ± 10 °C | 2000 V/mil |
| LTDS (FEP outer / EFEP inner) | 302 °F (150 °C) | 1.3–1.4:1 | 1.168–10.490 mm | 0–6.35 mm* | up to 1.499 mm* | ±20 % | 210 ± 10 °C | N/A |
| HTDS (PTFE outer / PFA inner) | 260 °C | 1.3–1.4:1 | 0.914–22.225 mm | 0–6.35 mm* | up to 1.651 mm* | ±20 % | 343 ± 10 °C | N/A |

\*Zeus: "When heated, Dual-Shrink™'s outer layer shrinks tightly while the inner layer melts and flows into a solid or near-solid encapsulation. The recovered ID and recovered wall are dependent on the reflowed material and geometry of the substrate."

- Other statements from the same guide:
  - PTFE is offered in 2:1, 4:1 and Sub-Lite-Wall™ versions; Sub-Lite-Wall™ means a recovered wall of 0.005″ (0.127 mm) or less.
  - "FEP heat shrink is an excellent choice for electrical insulation", offered in 1.3:1, 1.6:1, 2:1 and Lay-Flat™.
  - Dual-Shrink™ is "designed to fully encapsulate components to lock out moisture and other chemicals".
  - Source: [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
- Fluorotherm comparison table:
  - εr at 1 MHz (D150): PTFE 2.1, FEP 2.1, PFA 2.1, ETFE 2.6.
  - Dielectric strength (D149): 18, 53, 80 and 79 V/µm (kV/mm). The column assignment to these four polymers is inferred from position on the page.
  - Maximum continuous use: PTFE 260 °C, FEP 204 °C, PFA 260 °C, ETFE 149 °C.
  - Melting points: PTFE 327 °C, FEP 270 °C, PFA 305 °C, ETFE 275 °C, PVDF 177 °C.
  - Source: [Fluorotherm material comparison](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/)
- Professional Plastics table (2008, older): PTFE εr 2.0–2.1 and 50–170 kV/mm; FEP εr 2.1 and 20 kV/mm at 3.2 mm; PFA εr 2.05–2.06; ETFE εr 2.6 and 25 kV/mm — [Professional Plastics](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)
- Dielectric strength figures differ between sources by thickness and test method: PTFE is 600 V/mil (≈23.6 kV/mm) in Zeus shrink data, 18 V/µm at Fluorotherm and 50–170 kV/mm at Professional Plastics. Zeus notes the values are thickness-dependent and "for reference only" — [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
- ETFE heat-shrink to AS23053/14 (formerly M23053/14): "semi-rigid" ETFE sleeving, −100 to 150 °C continuous. It is "intended for use in component cables and electronic lead strain relief where low expansion ratios are satisfactory" — [Wiremasters M23053/14](https://www.wiremasters.com/product/harness-management-products/heat-shrink-tubing/m23053/m23053-14)
- Non-shrink PTFE tubing (slip-on):
  - Daburn DTT500 thin-wall extruded PTFE: "Rated for continuous operation of 250 °C" — [Daburn DTT500](https://www.daburn.com/dtt500-thin-wall-ptfe.aspx)
  - Daburn DUT ultra-thin PTFE: walls to 0.0015″ (0.038 mm) and IDs to 0.002″ — [Daburn DUT](https://www.daburn.com/dut-ultra-thin-wall-ptfe.aspx)

### Inferences
- **Temperature fit for a class 180–220 °C target:**
  - FEP (205 °C) and PTFE/FEP Dual-Shrink (205 °C) cover class 180 but are marginal for 200 °C and too low for 220 °C.
  - PFA (260 °C), PTFE (260 °C) and HTDS PTFE/PFA (260 °C) cover 220 °C.
  - ETFE (150 °C) and LTDS (150 °C) are below target.
- **PD.** With εr ≈ 2.1, fluoropolymers put the smallest share of voltage on any internal air gap of all tube materials (model in Q6). That matters more for PDIV than their modest per-mil breakdown strength.
- **Lab handling.** FEP (216 °C) and PFA (210 °C) recover far below PEEK (343–385 °C) and PTFE (343 °C). They are the easiest high-temperature shrinks to recover on bare copper in a lab oven, with less copper oxidation; this is an inference with no source.
- **Melt-liner tubes.** Dual-Shrink-type tubes are the only commercial tubes found that are designed to fill voids by melt flow. They also seal the tube ends, which in PD specimens are triple-junction sites.
  - Penalty: total recovered wall up to about 1.65 mm and a non-uniform inner layer, which costs slot fill and makes thickness uneven.
  - Best use: a "gap-free reference" variant in the test plan, or for weld or lead zones rather than slot sections.
- **Sizing windows (calculation, illustrative 4 × 2 mm bar with r = 0.5 mm; method in Q6).** The expanded ID must exceed 4.16 mm, and expanded ID divided by ratio must stay below 3.55 mm:
  - FEP 1.3:1: expanded ID 4.16–4.61 mm.
  - FEP or PFA 1.6:1: 4.16–5.68 mm.
  - FEP or PTFE 2:1: 4.16–7.09 mm.
  - PTFE 4:1: up to about 14.2 mm, but with thick recovered walls of 0.152–0.635 mm.

### Gaps
- I found no catalogue rectangular or flat-profile fluoropolymer heat-shrink. Zeus custom profiles cover non-shrink extrusions only, and FEP Lay-Flat™ is a flattened round tube offered in large sizes only.
- I found no PDIV or partial-discharge data for FEP, PFA or PTFE shrink on rectangular conductors, and no ATF-immersion data for any fluoropolymer shrink.
- Junkosha FEP shrink specs (e.g., −65 to +200 °C) appeared only in search snippets and are unverified.

## Q4. Other heat-shrinks: PVDF, thin-wall PET, polyolefin (EV busbar), silicone, FKM (Viton), adhesive-lined dual wall

### Takeaway
None of these is a clean fit for a 180–220 °C hairpin with good PD behaviour.
- PVDF/Kynar: 175 °C and εr 8.4, the worst possible εr for PD.
- Thin PET: walls 2.5–100 µm and recovery 70–190 °C, but service only 135 °C.
- Polyolefin: an EV-busbar series product (TE VOLINSU, rated 1000–2500 V) at 120–150 °C. Hot-melt liners soften at about 85 °C.
- Silicone (Shin-Etsu ST-OR, 2024): 200 °C and 28 kV/mm. It is new and aimed at EV busbars.
- FKM/Viton: 200 °C, but thick (1.2 mm on a 12.7 mm size) with only 8 kV/mm.

### Cited Findings
**PVDF (Kynar)**
- HellermannTyton Kynar TDS 332-51273 (generated 29 May 2026):
  - 2:1; minimum shrink temperature +175 °C; operating −55 to +175 °C.
  - Dielectric strength 30 kV/mm (IEC 684 P2); UL 224 VW-1; insulation class F (VDE 0530).
  - Longitudinal change −5 % max; wall 0.30 mm (12.7 → 6.4 mm size).
  - Specifications: MIL-DTL-23053/8, DEF STAN 59-97/3, UL 224.
  - Source: [HellermannTyton Kynar TDS](https://www.hellermanntyton.com/shared/assets/TDS_332-51273_com.pdf)
- PVDF εr 8.4 (1 MHz) and 13 kV/mm (bulk) — [Professional Plastics (2008, older)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)

**Thin-wall PET heat-shrink**
- Zeus PET Sub-Lite-Wall™ (August 2026):
  - Expanded ID 0.018–0.390″ (0.457–9.906 mm); expanded wall 0.00025–0.003″ (0.00635–0.076 mm), depending on ID; wall tolerance as low as ±0.0001″ (±0.0025 mm).
  - Recovered ID is "15 % below Expanded ID Min. with no tension". Ratio 1.1:1; "Shrink ratios beyond 1.1:1 can be achieved by applying tension".
  - Recovery 158–374 °F (70–190 °C); working temperature up to 275 °F (135 °C).
  - Dielectric strength 4000 V/mil (≈157 kV/mm). Applications include "Electrical insulation".
  - Sources: [Zeus PET SLW V1R1](https://www.zeusinc.com/wp-content/uploads/2026/08/PET-SLW-Heat-Shrink-V1R1.pdf); [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
- Nordson MEDICAL PET (formerly Advanced Polymers/Vention; sheet dated June 2024):
  - Diameter 0.006–0.5″ (0.15–12.7 mm); wall 0.0001–0.004″ (0.0025–0.10 mm); shrink ratios 1.1:1 up to 3:1.
  - Shrink temperature 185–374 °F (85–190 °C); melt temperature 473 °F (245 °C); recommended hot box 300–450 °F (149–232 °C).
  - "Tight fit is best: 15 % gap or less". "Recovery >20 % can be achieved by drawing or holding the ends of the heat shrink as it is heated."
  - Dielectric strength ">4,000 V/mil (60 Hz)"; tensile strength "up to and exceeding 20,000 psi".
  - "Can be transformed into custom parts by drawing/shrinking onto a shaped mandrel (conical, square, triangular, etc.)" and "Can be 'heat-set' so that it is stable up to a prescribed temperature". "Axial shrinkage pulls components together."
  - Source: [Nordson PET datasheet](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf)
- PET εr 3.0 (1 MHz); 17 kV/mm (bulk) — [Professional Plastics (2008, older)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)

**Polyolefin (including EV busbar lines)**
- TE VOLINSU EVBB (EV busbar tubing): 2:1; EV orange; "thinner wall"; fits "a variety of busbar shapes". It "does not propagate burning as specified in UL224", per TE's internal testing. Numeric temperature and voltage ratings are not on the page — [TE EVBB page](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-busbar-tubing.html); [Avnet EVBB page](https://my.avnet.com/abacus/products/new-products/npi/te-connectivity-volinsu-busbar-heat-shrink-tubing/)
- TE VOLINSU EVSW (single wall): 2:1; −55 to 150 °C; "rated for 2500V"; UL224 flame test done internally — [TE EVSW page](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/intersection/volinsu-heat-shrink-tubing/electric-vehicle-single-wall-tubing.html)
- TE VOLINSU EVDW (dual wall): "meltable inner layer"; 3:1; continuous −40 to 125 °C; "rated for 1000V" — [TE EVDW page](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-dual-wall.html)
- WKK busbar insulation tubing (article, August 2022, older):
  - Modified polyolefin; 2.5:1; −40 to 120 °C.
  - Wall after shrinking: medium wall 2.5–2.9 mm, heavy wall 4–4.1 mm.
  - Full-shrink temperature stated inconsistently on the page: 110 °C in the text vs 120 °C in product names.
  - Source: [WKK busbar tubing](https://www.wkk-europe.com/news/post/busbar-insulation-tubing-what-is-it-and-for-which-applications-is-it-used)
- Raychem BPTM busbar tubing:
  - Non-halogen thermoplastic; for "both circular and rectangular copper or aluminium busbars". It "shrinks snugly over the busbar profile ensuring that the required minimum wall thickness is obtained".
  - Flashover protection is given as both 24 kV and 25 kV on the same page.
  - The page says the product "is not currently available".
  - Source: [TE BPTM](https://www.te.com/en/product-CAT-BPTM.html)
- Polyethylene εr 2.2–2.4 (HDPE/LDPE, 1 MHz) — [Professional Plastics (2008, older)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)

**Adhesive-lined dual-wall polyolefin**
- Farnell dual-wall kit datasheet (October 2014, older):
  - Co-extruded polyolefin plus hot-melt adhesive; 3:1; −55 to +125 °C; minimum shrink temperature 80 °C; UL224 125 °C 600 V VW-1.
  - Dielectric strength ≥20 kV/mm (IEC 243); volume resistivity ≥1×10^14 Ω·cm.
  - **Adhesive softening point 85 ± 5 °C**; longitudinal shrinkage 0 to −10 %.
  - Recovered total wall 0.90–1.95 mm, of which adhesive is 0.35–0.55 mm (sizes 3.2–19.1 mm).
  - Source: [Farnell dual-wall kit](https://www.farnell.com/datasheets/1937594.pdf)

**Silicone rubber heat-shrink**
- Shin-Etsu ST-OR (news release, 11 September 2024):
  - "industry-first heat-shrinkable silicone rubber tubing for busbar covering", per Shin-Etsu's own research as of end-August 2024.
  - Dielectric strength 28 kV/mm; −40 to +200 °C; stays flexible after shrinking; orange; for EV and HEV busbars.
  - A sister grade, ST-TC-1, has 1.0 W/m·K thermal conductivity.
  - Source: [Shin-Etsu release 2024](https://s24.q4cdn.com/622300748/files/doc_news/Shin-Etsu-Chemical-Develops-Industry-First-Heat-Shrinkable-Silicone-Rubber-Tubing-for-Busbar-Covering-2024.pdf)
- The Alstom/GE patent prefers elastomer shrink tubes for rectangular stator bars: "Especially in thermally highly loaded machines silicone elastomers are preferably used" (priority 2000, granted 2006, older) — [EP1154543B1](https://patents.google.com/patent/EP1154543B1/en)

**FKM (Viton) heat-shrink**
- HellermannTyton Viton-E TDS 330-01270 (generated 5 June 2026):
  - Cross-linked fluoroelastomer; 2:1; minimum shrink temperature +170 °C; −55 to +200 °C.
  - Dielectric strength 8 kV/mm; wall 1.20 mm (12.7 → 6.4 mm size); longitudinal change −10 % max.
  - Heat ageing 168 h at 250 °C; heat shock 4 h at 300 °C; insulation class C (VDE 0530).
  - Tensile strength 10.5 MPa; elongation ≥500 %; specification VG 95343-5.
  - Source: [HellermannTyton Viton-E TDS](https://www.hellermanntyton.com/shared/assets/TDS_330-01270_com.pdf)

### Inferences
- **Excluded on temperature for a 180–220 °C class** (they could still serve as low-temperature references in the test plan):
  - PVDF (175 °C)
  - PET (135 °C)
  - ETFE (150 °C)
  - Polyolefin (120–150 °C)
  - Hot-melt adhesive liners (softening about 85 °C)
- PVDF's εr of 8.4 is about four times that of the fluoropolymers (2.1). It would push most of the voltage into any air gap, so it is a poor PD choice even where temperature allows.
- **Thin PET:**
  - A 6–76 µm wall gives very little series "voltage cushion". Any air gap under it takes most of the voltage (Q6 model), so PET only makes sense if it is gap-free.
  - With only about 15 % free recovery, a round PET tube cannot conform to a rectangle without tension or pre-shaping. Nordson's "shrinking onto a shaped mandrel (square…)" plus "heat-set" is the realistic route to a pre-shaped rectangular PET sleeve.
- **Silicone and FKM shrink:**
  - Both reach 200 °C, but they are thick, soft elastomers: Viton is 1.2 mm wall at 8 kV/mm.
  - They fit end-winding, lead or busbar zones better than slot sections.
  - Silicone's swelling in hot ATF is a known class risk, but I found no source for it; it should be tested.

### Gaps
- **TE datasheets blocked.** The EVBB and EVSW datasheets returned HTTP 403/503.
  - Unverified search-snippet figures: EVBB 70 °C minimum shrink, 90 °C full recovery, up to 125 °C operating with 200 °C short-term, 2500 V; EVSW datasheet −55 to 135 °C.
  - The 135 °C snippet conflicts with the EVSW product page (−55 to 150 °C). These need confirmation from TE.
- **Other unretrieved data.**
  - Shin-Etsu ST-OR shrink ratio, shrink temperature and wall thickness were not found.
  - The 3M VTN-200 (FKM) datasheet could not be retrieved (HTTP 503).
  - No εr was found for silicone or FKM shrink.
- **ATF.** I found no ATF-immersion data for any shrink material.

## Q5. Braided/woven sleeving (varnished, silicone- or acrylic-coated glass, Nomex) and spiral-wound tubes

### Takeaway
Fibreglass sleevings are mature, series-production insulation for motor leads and crossovers:
- Acrylic-coated: class 155 °C; NEMA Grade A ≥7 kV average breakdown.
- Silicone-rubber or silicone-resin coated: 200 °C.
- Viton-coated: class 220 °C.
- Nomex braid: up to 240 °C.

They are porous braids and relatively bulky, so on their own they are not PD-free at 800 V; they rely on impregnation. Spiral-wound Kapton and Nomex tubes (Pleo; Politubes "EVtubes") are commercial and rated 220 °C. Politubes markets thin 0.13–0.19 mm Nomex/Kapton/Nomex tubes specifically for 400/800 V hairpin motors.

### Cited Findings
- Daburn D155 acrylic-coated fibreglass sleeving:
  - "used to insulate leads and crossovers in fractional and integral horsepower motors" and in "dry and oil-filled transformers".
  - Operating −25 to +155 °C; MIL-I-3190/3 Grade A; NEMA TF-1 Type 6; ASTM D372.
  - NEMA Grade A: 7,000 V minimum average, 5,000 V minimum individual. Grade C-1: 2,500 V minimum average, 1,500 V minimum individual.
  - Source: [Daburn D155](https://www.daburn.com/D155-DAFLEX-Acrylic-Coated-Fiberglass-Sleeving-MIL-I-3190/3.aspx)
- Daburn D200 silicone-rubber-coated fibreglass: flexible from −55 to +200 °C; MIL-I-3190/6 Grade A. It "Can be 'pushed-back' easily and has high cut through resistance" — [Daburn D200](https://www.daburn.com/d200-rubber-fiberglass.aspx)
- Daburn D210 silicone-resin-coated fibreglass: "operating temperatures up to 200 °C"; MIL-I-3190/5 — [Daburn D210](https://www.daburn.com/d210-silicone-resin-fiberglass.aspx)
- Daburn D220 Viton-coated fibreglass: "Up to 220 °C"; MIL-I-3190/7 Grade A; exceeds NEMA TF-1 and ASTM D372; VW-1; "Class 220" — [Daburn D220](https://www.daburn.com/d220-viton-fiberglass.aspx)
- Daburn D130 vinyl-coated fibreglass: UL 1441; MIL-I-3190/2; VW-1; "NEMA GRADE B-B-1 4000 V" — [Daburn D130](https://www.daburn.com/d130-vinyl-coated-fiberglass.aspx)
- Daburn D300: heat-cleaned fibreglass braid with acrylic resin binder (non-fray) — [Daburn D300](https://www.daburn.com/d300-acrylic-resin-fiberglass.aspx)
- Hilec 542R silicone-rubber-coated braided fibreglass (Delfingen; discontinued):
  - Class H 200 °C; −55 to +200 °C; NEMA TF-1 Type 5; "two-component liquid silicone rubber continuously applied" to the braid.
  - The page is inconsistent for grade C-1: the title says 2500 V, while the body gives a 4000 V minimum average.
  - Source: [Electro-Wind Hilec 542R](https://www.electro-wind.com/wpgrp-sleeving-tubing/1-awg-542r-c-1-2500v-silicone-rubber-coated-braided-fiberglass-sleeving-200c-white-100-ft-per-spool)
- Nomex braided sleeving: meta-aramid; continuous −60 to 240 °C "in optimum conditions"; self-extinguishing; sizes 3–45 mm. No dielectric data is given; this is a low-detail vendor page — [Textile Technologies Nomex sleeving](https://www.textiletechnologies.co.uk/en-sv/products/nomex-braided-sleeving.oembed)
- Spiral-wound tubes (Pleo, February 2024):
  - "Kapton tubes" −60 to 220 °C, shrinkage <2 %. "Nomex sleeves" −60 to 220 °C. "Kapton+Nomex" −60 to 220 °C.
  - PET tubes −60 to 150 °C (one type −60 to 180 °C). Some PET tubes have 25–35 % shrinkage.
  - Source: [Pleo Tube/Sleeve](https://pleo.com/wp-content/uploads/2024/02/Tube-Sleeve.pdf)
- Politubes "EVtubes" (CWIEME Berlin article, 2 May 2023):
  - Construction: spiral-wound Nomex/Kapton/Nomex (NKN) tubes "supplied with thicknesses of only 0.13 and 0.19 mm" without overlap.
  - Ratings: custom-designed for 400 V and 800 V motors; "Nomex 818–864 and Kapton MT+" recommended for 800 V; "Dielectric strength up to 12 kV"; "UL system integration up to 220 °C".
  - Hairpin use: they can be formed in the slot or fitted onto "copper bars" to take the rectangular hairpin shape.
  - PD claim: reduced PD is attributed to "hermetic tube closure", with no PD figures given.
  - Using Nomex 410 instead of 464 reduces Nomex dust during hairpin insertion.
  - Certifications: UL TEOU2-8 E350605; ISO 9001:2015; IATF 16949 in progress.
  - Source: [CWIEME Berlin article](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)

### Inferences
- **Braided sleeves** contain air in the braid interstices and between the coating and the conductor. At 800 V SiC stress they are unlikely to be PD-free unless fully impregnated (varnish, trickle or VPI). They fit phase leads, neutral and terminal regions, not slot sections.
- **Lab test of braided sleeves.** Test them twice: as-sleeved and after impregnation. The difference will measure the effect of the air.
- **Spiral NKN or Kapton tubes.**
  - Of the tube products found, these are the closest match to "pre-shaped rectangular tube" for hairpins. They are thin (0.13–0.19 mm), 220 °C capable, and wound to shape on a mandrel.
  - Their PD behaviour depends on how tightly they fit and on the spiral seams. The vendor's PD claim needs independent PDIV testing.

### Gaps
- I found no wall-thickness or PDIV data for fibreglass or Nomex sleevings, and no oil/ATF data.
- I found no independent test data for Politubes EVtubes. The Politubes product page itself was not retrieved; the information comes from the CWIEME article.

## Q6. Conformity to a rectangular cross-section, air gaps and PD, ways to eliminate gaps, application before vs after forming

### Takeaway
A round heat-shrink only hugs all four faces of a rectangle if two conditions hold:
1. The expanded ID clears the bar's circumscribed diameter.
2. The free-recovered circumference is smaller than the bar's perimeter.

Otherwise the flats stay slack and air gaps form.
- **Corners and flats.** Round tubes contact the corners first and can tear at the edges (Alstom patent). Walls thicken where recovery is unconstrained, so walls should end up thinner at corners and thicker on flats.
- **Length.** Expect 5–20 % longitudinal change.
- **PD.** Any residual air gap of width g takes the fraction g/(g + t/εr) of the voltage. Air's minimum breakdown voltage is 327 V at about 7.5 µm (Paschen minimum).
- **Remedies:** higher shrink ratio and tight sizing; pre-shaped rectangular tubes (patented for stator bars; PET shrunk on a square mandrel); melt-liner or adhesive tubes; post-impregnation.
- **Order of operations.** The Alstom patent prefers sleeving before bending, using elastomer tubes and a protective bending tool.

### Cited Findings
- **Alstom/GE patent EP1154543B1** (priority 12 May 2000, granted 8 February 2006; older, but it is the key prior art) — [EP1154543B1](https://patents.google.com/patent/EP1154543B1/en)
  - Problem: round-section shrink tubing on rectangular conductors "tends to rupture due to thermal and mechanical stress" at the edges, either right after shrinking or after brief operational load. Wrinkles and cavities are named as defects. Cavities between the bar and the main insulation can cause electrical discharges.
  - Solution: a shrink tube whose inner and outer cross-section is rectangular, matched to the bar, which "conforms to the conductor bar at any point without the formation of wrinkles and cavities". The tube is prefabricated by extrusion or injection moulding and can be electrically tested before assembly.
  - Application variants:
    - Cold-shrink: the tube is pre-stretched on a support sleeve that is removed by spiral separation along perforations.
    - Meltable support sleeve: the sleeve melts and acts as adhesive or sealant, or, if conductive, as inner corona protection.
    - Warm-shrink.
    - Compressed-air expansion during assembly.
  - Adhesive: a thermally stable adhesive at the contact surfaces avoids cavities, improves heat conduction and avoids "electrical cavity discharges".
  - Bending: the preferred process brings the bars to final shape "only after the casing with the elastomer", using a bending device with a protective layer. The patent also allows bending before insulation.
- **Zeus guide (2026)** — [Zeus guide V1R7](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf)
  - Sizing: Expanded ID Min. must exceed the substrate. Recovered ID Max. must be below the substrate, otherwise "the material may not shrink down completely, leaving a gap".
  - "The more irregular the shape, the greater the heat shrink ratio needed".
  - "As heat is applied and the tube begins to shrink, the wall thickness of the heat shrink tubing will increase". Recovered wall is specified for "complete unconstrained recovery".
  - Longitudinal change can be shrinkage or growth: PTFE ±20 %, FEP and PFA ±15 %, Dual-Shrink ±20 %.
  - Ovens and vertical laminators give even heating. Overheating "can lead to brittleness and cracking".
- **Longitudinal change of other shrinks:**
  - Kynar −5 % max — [HellermannTyton Kynar TDS](https://www.hellermanntyton.com/shared/assets/TDS_332-51273_com.pdf)
  - Viton-E −10 % max — [HellermannTyton Viton-E TDS](https://www.hellermanntyton.com/shared/assets/TDS_330-01270_com.pdf)
  - Dual-wall polyolefin 0 to −10 % — [Farnell (2014, older)](https://www.farnell.com/datasheets/1937594.pdf)
- **Nordson PET.** "Tight fit is best: 15 % gap or less". More than 20 % recovery is possible by drawing or holding the tube ends while heating. PET can be shaped onto square or triangular mandrels and heat-set — [Nordson PET datasheet](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf)
- **Raychem busbar tubing** "shrinks snugly over the busbar profile ensuring that the required minimum wall thickness is obtained" on rectangular busbars — [TE BPTM](https://www.te.com/en/product-CAT-BPTM.html)
- **Rockwell Automation patent EP4345850A1** (published 3 April 2024) — [EP4345850A1](https://data.epo.org/publication-server/rest/v1.2/patents/EP4345850NWA1/document.html)
  - On overmoulded busbar insulation: "Some air may become trapped between the bus bars and the plastic material creating narrow air gaps"; "because the air gap is unintentional, the width may vary along the length of the bar"; "Within this air gap, partial discharge may occur", eventually causing "breakdown and eventually failure of the insulation".
  - Their remedy is the opposite philosophy: a rigid slide-on holder whose internal ribs set a *uniform, deliberate* 0.2–0.5 mm gap (0.3 mm in one embodiment), so that the electric field is spread evenly.
- **Paschen minimum.** For air at standard pressure the minimum breakdown voltage is "327 V … at a distance of 7.5 μm". The equation "loses accuracy for gaps under about 10 μm in air at one atmosphere" — [Wikipedia: Paschen's law](https://en.wikipedia.org/wiki/Paschen%27s_law)
- **εr values used in the model below:**
  - PTFE/FEP/PFA ≈2.1 and ETFE 2.6 — [Fluorotherm](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/)
  - PET 3.0, PI 3.4, PEEK 3.2–3.3, PVDF 8.4, PE 2.2–2.4 — [Professional Plastics (2008)](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf)
  - PEEK 3.2 at 23 °C rising to 4.5 at 200 °C — [Optinova 2022](https://optinova.com/app/uploads/2022/09/optinova-peek-tubing.pdf)

### Inferences
- **Sizing rule for round shrink on a rounded rectangle** (my geometry; a × b bar with corner radius r):
  - Circumscribed diameter: D_c = √((a−2r)² + (b−2r)²) + 2r.
  - Perimeter: P = 2(a+b) − (8−2π)·r.
  - Conditions: expanded ID_min > D_c, plus handling clearance; and free-recovered ID_max < P/π, so the tube is still in hoop tension when it touches all four faces.
  - Minimum free shrink ratio: R_min = π·D_c / P.
  - Illustrative results (sizes are examples, not sourced hairpin dimensions):

    | Bar a × b, corner r | D_c | P/π | R_min |
    |---|---|---|---|
    | 4 × 2 mm, r 0.5 | 4.16 mm | 3.55 mm | 1.17 |
    | 5 × 2.5 mm, r 0.5 | 5.27 mm | 4.50 mm | 1.17 |
    | 6 × 1.5 mm, r 0.4 | 6.05 mm | 4.56 mm | 1.33 |

  - Flatter conductors need higher ratios, consistent with Zeus's "irregular shapes" statement.
  - With insertion clearance, a practical ratio of about 1.3–1.6:1 or more is needed. That makes PEEKshrink (≤1.4:1) and PET (about 1.15–1.18:1 free recovery) tight or marginal. FEP and PTFE at 1.6–2:1, and Gunze PEEK (≤25 % shrinkage, about 1.33:1), are more forgiving.
- **Corner thinning and flat thickening (mechanism inference, consistent with the Zeus statements).**
  - The tube touches the corners first. Friction and the substrate then stop recovery there, so the corner wall stays near its thinner, still-expanded value.
  - Wall over the flats keeps recovering and thickens until it touches.
  - With an over-sized tube (ratio below R_min), the flats never touch and air pockets remain.
  - With a stiff, thick wall (PEEK, thick PTFE) relative to the corner radius, small "tented" voids can remain next to each corner.
  - The sharpest field enhancement (copper corner) coincides with the thinnest wall. Measure both by cross-sectioning.
- **Air-gap PD model (calculation; planar series-capacitor approximation, ignoring corner field enhancement, surface charge and temperature/pressure effects).**
  - For applied voltage V across a tube of wall t and permittivity εr over an air gap g, the gap voltage is V_g = V · g / (g + t/εr).
  - Since air breakdown is ≥327 V for any gap, a rough lower bound for PD inception is PDIV ≳ 327 V · (g + t/εr) / g.
  - Examples for g = 20 µm:

    | Tube | t | εr | t/εr | Share of V on gap | PDIV lower bound |
    |---|---|---|---|---|---|
    | PEEKshrink, 23 °C | 0.178 mm | 3.2 | 55.6 µm | 26 % | ≈1.24 kV |
    | PEEKshrink, 200 °C | 0.178 mm | 4.5 | 39.6 µm | 34 % | ≈0.97 kV |
    | FEP | 0.254 mm | 2.1 | 121 µm | 14 % | ≈2.3 kV |
    | Thin PET | 25 µm | 3.0 | 8.3 µm | 71 % | ≈0.46 kV |

  - Thin PET or PI skins therefore give almost no PD margin if any gap exists. Thick, low-εr fluoropolymer walls give the most, and hot PEEK loses margin.
  - These are order-of-magnitude guides only. Measured PDIV must govern the test plan.
- **Gap elimination options, ranked for lab practicality:**
  1. Correct sizing (R ≥ R_min) and oven recovery (Zeus recovers 10 min after the oven reaches temperature).
  2. Melt-liner tubes: Zeus Dual-Shrink PTFE/FEP at 205 °C, HTDS PTFE/PFA at 260 °C.
  3. Pre-shaped rectangular tubes: PET shrunk and heat-set on a rectangular mandrel; custom rectangular extrusion; spiral-wound NKN/Kapton made on a rectangular mandrel.
  4. A thermally stable adhesive or primer under the tube, as in the Alstom patent.
  5. Post-impregnation (trickle or VPI resin) of tube ends or porous sleeves. This is my inference; I found no tube-specific source.
- **Test-specimen practice (my recommendations for the plan):**
  - Deburr or radius the cut conductor ends so they do not puncture thin walls.
  - Cut the tube 15–25 % longer than the target coverage to allow for ±15–20 % longitudinal change.
  - Seal or recess the tube ends, or keep PD electrodes well away from them, because a tube end is a copper–polymer–air triple junction.
  - Section specimens to measure corner and flat wall thickness and gaps.
  - Include a deliberately gapped variant (shim) and a melt-lined, gap-free variant to bracket the effect of the gap on PDIV.
  - Record the recovery temperature and time, because PEEK has to be recovered close to its melting point.
- **Before vs after hairpin forming (inference):**
  - Hairpin geometry: a U-shaped crown with 3D bends plus straight legs.
  - Sleeving before forming covers the whole length, but bending risks wrinkling the tube on the intrados, thinning or cracking it on the extrados, and moving it along the bar. Alstom handled this with elastomer tubes and a protective bending tool.
  - Stiff PEEK (yield ≈100 MPa; elongation at break 45 % in the Optinova bulk data) and PET will be more sensitive.
  - Sleeving after forming is only practical on straight legs, lead ends or weld zones, because a continuous tube cannot pass the crown bends.
  - For the test plan, include "sleeve → bend → PDIV" vs "bend → sleeve straight sections → PDIV" pairs.

### Gaps
- I found no quantitative published data, experimental or finite-element, on corner thinning, flat-face gaps or wrinkling of heat-shrink on rectangular copper.
- I found no PDIV dataset comparing tube-insulated with enamel-insulated rectangular conductors.
- I found no published effect of heat-shrink processing temperatures (343–385 °C for PEEK and PTFE) on bare copper oxidation or annealing.

## Q7. Published use of tubes/heat-shrink on hairpins, busbars or EV motor leads, and typical practice

### Takeaway
- **EV busbars:** heat-shrink is a series-production solution. Examples are TE's VOLINSU EV tubing (EVBB busbar 2:1; EVSW rated 2500 V; EVDW rated 1000 V) and Shin-Etsu's 2024 ST-OR silicone shrink at 200 °C.
- **Hairpin stators:** the only tube-type product found is Politubes' spiral-wound Nomex/Kapton/Nomex "EVtubes", fitted onto bars to take the rectangular hairpin shape (vendor article, 2023).
- **Stator bars:** shrink-on insulation of rectangular bars was patented by Alstom (2000/2006) for large machines.
- **Motor leads:** traditional practice uses fibreglass sleevings (class 155–220 °C).
- **Research gap:** I found no peer-reviewed PDIV or ageing study of heat-shrink-insulated hairpins, and no published use of PEEKshrink in e-motors.

### Cited Findings
- **EV busbars.**
  - TE VOLINSU EVBB "fits a variety of busbar shapes", orange, 2:1 — [TE EVBB](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-busbar-tubing.html)
  - EVSW: 2500 V, −55 to 150 °C — [TE EVSW](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/intersection/volinsu-heat-shrink-tubing/electric-vehicle-single-wall-tubing.html)
  - EVDW: meltable liner, 1000 V, −40 to 125 °C — [TE EVDW](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-dual-wall.html)
  - Shin-Etsu ST-OR silicone shrink for EV/HEV busbars: 28 kV/mm, −40 to +200 °C (2024) — [Shin-Etsu](https://s24.q4cdn.com/622300748/files/doc_news/Shin-Etsu-Chemical-Develops-Industry-First-Heat-Shrinkable-Silicone-Rubber-Tubing-for-Busbar-Covering-2024.pdf)
- **Hairpins.** Politubes NKN EVtubes: 0.13 and 0.19 mm; 400/800 V; up to 12 kV; UL system up to 220 °C; fitted onto copper bars to take the rectangular hairpin shape (2023) — [CWIEME Berlin](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)
- **The same article** describes ultrasonically welded caps of Nomex 411 plus heat-shrinkable polyester for insulating joints and motor cable terminations — [CWIEME Berlin](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem)
- **Stator bars.** Rectangular shrink tubes (elastomer or silicone) for rectangular stator bars, sleeved before bending (older; priority 2000) — [EP1154543B1](https://patents.google.com/patent/EP1154543B1/en)
- **Motor leads.** Acrylic-fibreglass sleeving is "used to insulate leads and crossovers in fractional and integral horsepower motors" — [Daburn D155](https://www.daburn.com/D155-DAFLEX-Acrylic-Coated-Fiberglass-Sleeving-MIL-I-3190/3.aspx)
- **PEEK in motors (older, 2014).** PEEK magnet wire "and other PEEK insulating products" in a rebuilt 0.75 hp 460 V motor — [Zeus RESINATE No.3](https://www.zeusinc.com/wp-content/uploads/2014/03/RESINATE_No3-PEEKInsWire_Zeus.pdf)
- **EV wire.** Optinova lists PEEK tubing for "insulation for wires in cables for aerospace or EV applications" — [Optinova](https://optinova.com/peek-tubing/)
- **Busbar air-gap PD** under rigid insulation, and a design that controls the gap uniformly at 0.2–0.5 mm — [EP4345850A1 (2024)](https://data.epo.org/publication-server/rest/v1.2/patents/EP4345850NWA1/document.html)

### Inferences
- In practice tubes and shrink sleeves are used on busbars, leads and terminals, joints and caps. Their use on hairpin slot sections is a vendor (Politubes) and patent-level proposition. For this test plan most tube options are lab or prototype studies.

#### Consolidated material–form matrix (synthesis of the cited findings above; maturity, feasibility, pros and risks are my assessment)

| Material – form | Wall range | Service temperature | Recovery temperature / shrink ratio | Dielectric strength | εr | Maturity for hairpin use | Lab feasibility on a cut bare bar | Pros | Main risks for hairpins | Commercial examples | Sources |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PEEK heat-shrink | 0.076–0.457 mm (std 0.127–0.229 mm) | 260 °C | 300–340 °C translucent / 360–385 °C opaque (343–385 °C in 2026 guide); ≤1.4:1 | 3500–3570 V/mil | 3.2 (23 °C) → 4.5 (200 °C) for PEEK | Lab/prototype | Feasible but hard: oven at about 343–385 °C, narrow window vs melting, copper oxidation | 260 °C, tough, adheres to metals | Low ratio vs rectangle; near-melt process; εr rises when hot; strength falls >220 °C; forming cracks | Zeus PEEKshrink™ | [Zeus page](https://www.zeusinc.com/products/heat-shrinkable-tubing/peekshrink/), [V1R4](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEKshrink-Heat-Shrink-V1R4.pdf), [Guide](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf), [Optinova](https://optinova.com/app/uploads/2022/09/optinova-peek-tubing.pdf) |
| PEEK low-temperature shrink | 50–300 µm | n/a | starts at 150 °C; ≤25 % shrinkage; ID 4.5–20 mm | n/a | n/a | Development | Samples only (ask Gunze) | Easy recovery; hairpin-scale IDs | Not yet a product; data image-only | Gunze | [Gunze](https://www.gunze.co.jp/e/epd/products/peek/) |
| PEEK extruded tube (round), slip-on | 0.038–1.59 mm (Optinova); ≥0.051 mm (Zeus) | 250–260 °C | n/a (no shrink) | 190 kV/mm at 50 µm; 23 kV/mm at 2 mm | 3.2 / 4.5 | Lab reference only | Easy to slide on; large air gaps | PFAS-free, 260 °C | Round ID > diagonal gives mm-scale gaps; custom rectangular profile needs a die | Optinova, Zeus (custom profiles) | [Optinova](https://optinova.com/peek-tubing/), [Zeus V2R2](https://www.zeusinc.com/wp-content/uploads/2024/06/PEEK-Extrusions-V2R2.pdf), [Zeus profiles](https://zeusinc.com/products/tubing/custom-profiles) |
| PI film-cast tube | 0.010–0.254 mm | 220 °C (20,000 h) | not shrinkable (thermoset) | ≥4000 V/mil | 3.4 | Not feasible (ID ≤2.3 mm) | No hairpin-size stock | High temperature and strength | Size; no shrink; no rectangle | MicroLumen, Zeus, Nordson | [MicroLumen](https://www.microlumen.com/medical-tubing/polyimide/), [Zeus PI](https://www.zeusinc.com/wp-content/uploads/2026/07/Polyimide-Tubing-V2R9.pdf), [Nordson PI](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-Polyimide-DS-01-DIGITAL.pdf) |
| Spiral-wound Kapton / NKN tube | 0.13–0.19 mm (NKN) | 220 °C | not shrink (<2 % shrinkage) | "up to 12 kV" (vendor) | n/a | Vendor offering for hairpins | Feasible if tubes made on a rectangular mandrel | Thin, 220 °C, pre-shaped | Spiral seams; fit gaps; vendor-only PD claims | Politubes EVtubes, Pleo | [CWIEME](https://berlin.cwiemeevents.com/articles/e-motor-400---800v-insulation-thermal-managem), [Pleo](https://pleo.com/wp-content/uploads/2024/02/Tube-Sleeve.pdf) |
| PTFE heat-shrink (2:1, 4:1, Sub-Lite-Wall) | 0.025–0.127 mm (SLW); 0.152–0.635 mm (4:1) | 260 °C | 343 ± 10 °C; up to 4:1 | 600 V/mil | 2.0–2.1 | Lab/prototype | Feasible (oven at 343 °C) | Highest ratio; low εr; 260 °C | High process temperature; ±20 % length change; low per-mil strength | Zeus | [Guide](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf), [Fluorotherm](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/) |
| FEP heat-shrink (1.3, 1.6, 2:1) | 0.076–0.762 mm | 205 °C | 216 ± 10 °C; up to 2:1 | 2000 V/mil | 2.1 | Lab/prototype | Easy (about 216 °C oven) | Lowest-temperature fluoropolymer recovery; low εr | 205 °C limit vs 220 °C class; ±15 % length | Zeus (also Junkosha, unverified) | [Guide](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| PFA heat-shrink | 0.102–0.508 mm | 260 °C | 210 ± 10 °C; ≤1.6:1 | 2000 V/mil | 2.05–2.1 | Lab/prototype | Easy (about 210 °C) | 260 °C with low recovery temperature | Ratio ≤1.6:1; ±15 % length | Zeus | [Guide](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| Dual-wall melt-liner: PTFE/FEP; HTDS PTFE/PFA | total wall up to 1.651 mm | 205 °C / 260 °C | 343 ± 10 °C; 1.3–1.4:1 | 2000 V/mil (PTFE/FEP) | ≈2.1 | Lab/prototype | Feasible; gap-free reference | Melt fills voids and seals ends | Thick, non-uniform wall; low ratio | Zeus Dual-Shrink™ / HTDS | [Guide](https://www.zeusinc.com/wp-content/uploads/2026/08/Heat-Shrink-Comparison-Recovery-Guide-V1R7.pdf) |
| ETFE heat-shrink | n/a | 150 °C | low expansion ratio | 25–79 kV/mm (bulk) | 2.6 | Below target | Feasible | Tough | 150 °C | AS23053/14 products | [Wiremasters](https://www.wiremasters.com/product/harness-management-products/heat-shrink-tubing/m23053/m23053-14), [Fluorotherm](https://www.fluorotherm.com/technical-information/materials-overview/material-comparison/) |
| PVDF (Kynar) heat-shrink | 0.30 mm (12.7/6.4 size) | 175 °C (class F) | ≥175 °C; 2:1 | 30 kV/mm | 8.4 | Below target | Easy | Cheap, tough | εr 8.4 (bad for PD); 175 °C | HellermannTyton, 3M | [HT Kynar](https://www.hellermanntyton.com/shared/assets/TDS_332-51273_com.pdf), [PP table](https://www.professionalplastics.com/professionalplastics/content/downloads/ElectricalPropertiesofPlastics.pdf) |
| Thin-wall PET heat-shrink | 0.0025–0.10 mm | 135 °C (Zeus) | 70–190 °C (hot box 149–232 °C); 1.1–3:1 | ≥4000 V/mil | 3.0 | Lab only (temperature too low) | Easy; best pre-shaped on a rectangular mandrel | Thinnest walls; shapeable and heat-settable | 135 °C; almost no PD margin over gaps | Zeus PET SLW, Nordson PET | [Zeus PET](https://www.zeusinc.com/wp-content/uploads/2026/08/PET-SLW-Heat-Shrink-V1R1.pdf), [Nordson PET](https://interventional-solutions.nordsonmedical.com/files/interventional-solutions-nordsonmedical-com/Literature/Sell%20Sheets/MAR-PET-Heat-Shrink-Tubing-DS-01-DIGITAL.pdf) |
| Polyolefin single-wall (EV busbar) | medium/heavy busbar walls 2.5–4.1 mm | 120–150 °C | about 2:1–2.5:1 | (≥20 kV/mm for a dual-wall product) | ≈2.2–2.4 (PE) | Series production on busbars; below target for hairpins | Very easy | EV-qualified product lines, 2500 V | Temperature class | TE VOLINSU EVBB/EVSW, Raychem | [TE EVSW](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/intersection/volinsu-heat-shrink-tubing/electric-vehicle-single-wall-tubing.html), [WKK](https://www.wkk-europe.com/news/post/busbar-insulation-tubing-what-is-it-and-for-which-applications-is-it-used) |
| Polyolefin adhesive-lined dual wall | 0.90–1.95 mm total | 125 °C | ≥80 °C; 3:1 | ≥20 kV/mm | n/a | Busbars/joints; below target | Very easy | Seals, fills gaps | Adhesive softens at about 85 °C | TE VOLINSU EVDW, generic | [TE EVDW](https://www.te.com/en/products/heat-shrink-tubing/orange-heat-shrink-tubing/resources/volinsu-heat-shrink-tubing/electric-vehicle-dual-wall.html), [Farnell](https://www.farnell.com/datasheets/1937594.pdf) |
| Silicone heat-shrink | n/a | 200 °C | n/a | 28 kV/mm | n/a | New for EV busbars (2024) | Likely easy (no data) | 200 °C, flexible | Thick and soft; ATF swelling untested | Shin-Etsu ST-OR | [Shin-Etsu](https://s24.q4cdn.com/622300748/files/doc_news/Shin-Etsu-Chemical-Develops-Industry-First-Heat-Shrinkable-Silicone-Rubber-Tubing-for-Busbar-Covering-2024.pdf) |
| FKM (Viton) heat-shrink | 1.20 mm (12.7/6.4 size) | 200 °C (class C) | ≥170 °C; 2:1 | 8 kV/mm | n/a | Leads/joints only | Easy | 200 °C, chemical resistance (ATF data not found) | Thick; low kV/mm; −10 % length | HellermannTyton Viton-E | [HT Viton](https://www.hellermanntyton.com/shared/assets/TDS_330-01270_com.pdf) |
| Acrylic / silicone / Viton-coated glass sleeving | n/a | 155 / 200 / 220 °C | n/a (slip-on) | Grade A ≥7 kV average; C-1 ≥2.5 kV average | n/a | Series production on motor leads | Easy (slip-on) | Mature, MIL/NEMA graded | Porous; needs impregnation; bulky | Daburn D155/D200/D210/D220; Hilec/Delfingen | [D155](https://www.daburn.com/D155-DAFLEX-Acrylic-Coated-Fiberglass-Sleeving-MIL-I-3190/3.aspx), [D200](https://www.daburn.com/d200-rubber-fiberglass.aspx), [D220](https://www.daburn.com/d220-viton-fiberglass.aspx) |
| Nomex braided sleeving | n/a | up to 240 °C | n/a | n/a | n/a | Leads only | Easy | High temperature | Porous; no dielectric data | Textile Technologies | [Nomex](https://www.textiletechnologies.co.uk/en-sv/products/nomex-braided-sleeving.oembed) |
| Non-shrink thin PTFE tube | from 0.038 mm | 250 °C | n/a | see PTFE | 2.0–2.1 | Lab reference | Easy; gaps on a rectangle | Low εr | Round-on-rectangle air gaps | Daburn DTT500/DUT | [DTT500](https://www.daburn.com/dtt500-thin-wall-ptfe.aspx), [DUT](https://www.daburn.com/dut-ultra-thin-wall-ptfe.aspx) |

### Gaps
- I found no OEM teardown, conference paper or journal paper documenting heat-shrink or PEEK tubes on hairpin slot sections in series EV motors.
- I found no peer-reviewed PDIV, thermal-ageing or ATF data for any tube or sleeve on hairpins.
- Junkosha and Polyfluor hairpin-relevant tube products could not be confirmed.
- The TE EVBB/EVSW datasheets (temperature and voltage details) were access-blocked (HTTP 403/503).
