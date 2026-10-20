# Insulation capability vs DC-bus voltage (800 / 1200 / 1600 V): PD inception and voltage endurance of hairpin and rectangular-wire insulation

Scope note for the report writer: these notes add to `reports/Hairpin izolasyon malzemeleri ve yöntemleri.md`. That report already covers the Lusuardi/IEC 60034-18-41 critical-voltage formula and its 800 V numbers, the Gao 2023 PI-FEP drop of about 0.2 kV from room temperature to 180 °C, the He/Tenbohlen/Beltle 2025 PWM ageing study, Wakimoto 2016 (humidity), Elorza Azpiazu 2023 (humidity and pressure, PDIV minimum at 50–70 mbar), the patent PDIV and ATF data, and the Kapton CR vendor claims. I do not repeat those here.

Access tags:
- **[FT]**: I read the full text.
- **[ABS]**: I read only the abstract or catalogue page.
- **[SEC]**: the number comes from a review that cites the primary source; I did not read the primary source.
- **[VEND]**: manufacturer or vendor claim.
- **Own calc.**: my own calculation or extrapolation, not a published value.

All sources were accessed on 20 Oct 2026.

## Q1. Published PDIV/RPDIV values versus thickness, permittivity, temperature, humidity and pressure; design models; thickness needed to be PD-free at 800, 1200 and 1600 V

### Takeaway
Measured turn-to-turn PDIV of rectangular and hairpin pairs is about 1.3–1.8 kV peak (50 Hz AC) for 250–350 µm of total insulation between conductors. The best-documented empirical model is Dakin's: PDIV_rms = 163·(d/εr)^0.46, with d the total insulation between conductors in µm. A hairpin-specific linear fit also exists: PDIV_pk[kV] = 0.0032·Dt + 0.71 at room temperature and 0.0032·Dt + 0.5 at 180 °C. PDIV falls by about 11–19% between room temperature and 180–230 °C. At 95% RH it falls by 20–26% when the wire surface is ionically contaminated. Low pressure lowers it further.

Scaling the IEC/Lusuardi requirement linearly raises the PD-free target by 1.5× at 1200 V and 2× at 1600 V (own calc.). Turn-to-turn insulation then still looks feasible at about 40–160 µm per wire for 1200 V and 80–270 µm for 1600 V. Phase-to-phase and phase-to-ground need about 0.5–1.1 mm of total insulation. A 1200 or 1600 V bus also puts the machine above the 700 V rms line voltage that IEC associates with Type I systems.

### Cited Findings

**Thickness and permittivity models, with fitted parameters**

- Furukawa quotes Dakin's relation as V = 163·(t/εr)^0.46, with t in µm and εr assumed to be 4. It agrees with their Paschen/field model for insulation thinner than about 30 µm. The twisted-pair and parallel-plate models diverge above 40 µm, and the gap widens with thickness. — [Muto, Oya, Aoi, Ueno, "A Study on Partial Discharge Phenomena of Winding Wires", Furukawa Review 45 (2014) 13–21 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- In the same Paschen model (εr = 4), the minimum crossing voltage is 720 V at a 25 µm critical air gap for 30 µm insulation, and 1210 V at a 50 µm gap for 100 µm insulation. — [Furukawa Review 45 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- Measured twisted-pair PDIV (1 mm Cu; 25 °C/50% RH; 50 Hz; 50 V/s ramp; 10 pC threshold), as average/minimum Vpeak versus 2t/εr:

  | 2t/εr | Average (Vpeak) | Minimum (Vpeak) |
  |---|---|---|
  | 16.0 | 775 | 728 |
  | 20.0 | 830 | 788 |
  | 23.2 | 902 | 849 |
  | 28.8 | 1055 | 994 |
  | 45.0 | 1330 | 1245 |
  | 58.8 | 1501 | 1445 |

  - Samples were 29–107 µm thick with εr 2.9–4.5 (measured at 100 Hz). Sample 1 was PAI enamel (36 µm, εr 4.5). The others were extruded PEEK, PPS and PET, with sample 5 a PEEK/PPS laminate (72 µm, εr 3.2). Figure labels suggest sample 6 (107 µm, εr 3.6) is PET, but the extracted table does not make this certain.
  - The Paschen estimate (750–1430 V) tracks the minimum measured PDIV.
  - Furukawa recommends the Paschen route over Dakin for design, because the minimum PDIV is what matters.

  — [Furukawa Review 45, Tables 2–3 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- **Own calc., important for using Dakin:** Furukawa's tabulated "Equation (1)" values (823–1506 V) equal 163·(2t/εr)^0.46·√2 within ±4 V. In other words, Dakin's formula gives an **rms** value, and d is the **total** thickness between the two conductors (2t). Peak = √2 × rms. — calculated from [Furukawa Table 3](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- Gao et al. measured hairpin turn-to-turn samples: two PI-FEP flat wires, 2.48 × 2.78 mm, corner radius 0.8 mm, εr 3.5 at 25 °C, minimum PDIV under 50 Hz AC.

  | Build per wire | Dt (total) | Room temperature | 180 °C |
  |---|---|---|---|
  | 125 µm | 250 µm | 1.51 kVpk | 1.30 kVpk |
  | 175 µm | 350 µm | 1.83 kVpk | 1.62 kVpk |

  - Average field in the insulation falls from 6.04 to 4.63 kV/mm.
  - Fitted design lines (kV, µm): PDIV_pk,fw = 0.0032·Dt + 0.71 at room temperature and 0.0032·Dt + 0.5 at 180 °C.
  - AC was used deliberately because, on twisted pairs, it gives the minimum PDIV compared with repetitive square-wave and surge voltages.

  — [Gao, Rumi, He, Cavallini, IEEE TDEI 30 (2023) 2870–2877, doi:10.1109/TDEI.2023.3284414 [FT postprint]](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- Gao et al. also give fits for enamel + film composites (random-wound), in kV and µm:
  - Phase-to-phase at room temperature: 0.0039·Dt + 0.7316
  - Phase-to-ground at room temperature: 0.0029·Dt + 0.678
  - Phase-to-ground at 180 °C: 0.0017·Dt + 0.6182

  Measured points:
  - Phase-to-phase, room temperature: 1.175, 1.275, 1.70 and 1.925 kVpk for Kapton 50 µm, Nomex 80 µm, NMN 190 µm and NMN 240 µm (with 2 × 30 µm PAI enamel).
  - Phase-to-ground, 180 °C: 0.775–1.125 kVpk for Dt 80–270 µm.
  - Neither the classical Dakin equation nor a three-parameter power law could fit the composite data. — [Gao et al. 2023 [FT]](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- Gao et al. also derived a Schumann streamer constant K for hairpin turn-to-turn: 5.95 (125 µm) and 5.71 (175 µm). This is close to Lusuardi's K = 5.98 for twisted pairs. For phase-to-phase and phase-to-ground composites K is 3.5–8.65, so a single K does not transfer between geometries. The FEM + Schumann model reproduced PDIV within 1.48% at room temperature and 10.49% at high temperature. — [Gao et al. 2023 [FT]](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- A temperature-dependent turn-to-turn PDIV model for round and rectangular wire needs no FEM and no γ or Schumann K fitting. Validated on more than 100 measurements: about half within ≤5% error, 87% within ≤12%, maximum 18%. The equation itself is in the full text, which is embargoed until 31 Oct 2026. — [Elorza Azpiazu, Egea, Almandoz, Ugalde, Sarasola, ICEM 2024, doi:10.1109/ICEM60801.2024.10700559 [ABS]](https://ebiltegia.mondragon.edu/handle/20.500.11984/6786?show=full)
- A 2026 FEM model (Schumann/Townsend) for enamelled flat wire covers insulation thickness, εr, temperature, **cooling oil**, impregnation, switching frequency, rise time and overshoot factor. The abstract gives no numbers. — [Elmezain, Güleç, Sergeant, IEEE TTE 12(3) (2026) 4746–4755, doi:10.1109/TTE.2026.3663628 [ABS]](https://trid.trb.org/View/2734892)

**Hairpin slot and formette data**

- Stuttgart built a miniaturised slot block from a 54-slot, delta, three-parallel-path stator with 8 bars per slot, and tested 6 conductor arrangements (AC, 10 repeats each).
  - Turn-to-turn PDIV: 710–872 V for "P130" (the production wire), 525–657 V for "PI100" and 661–810 V for "Peak100".
  - Phase-to-ground (configuration d): 1296, 913 and 1190 V respectively.
  - P130 and Peak100 are the same material and P130 is thicker.
  - Arrangement symmetry changes PDIV. Ungrounded asymmetric arrangements are lowest.
  - The paper does not say whether the values are rms or peak.

  — [He, Beura, Tenbohlen, ISEIM 2020 [FT]](https://www.ieh.uni-stuttgart.de/dokumente/publikationen/2020_09_He_Investigation_of_Partial_Discharge_Activity.pdf)

**Temperature**

- Normalised PDIV versus temperature (Grade II PAI twisted pairs, unipolar impulse, 150 ns rise, 2.5 kHz, 20–230 °C): y = −0.0009·T[°C] + 1.0169. — [Madonna et al., IEEE TIA 57 (2021) 1389–1398, doi:10.1109/TIA.2020.3046434, via Ji/Giangrande/Zhao review [SEC]](https://www.mdpi.com/1996-1073/17/16/3980). Own calc.: 0.855 at 180 °C, 0.837 at 200 °C, 0.81 at 230 °C.
- The Gao hairpin PI-FEP data give a 180 °C/room-temperature ratio of 0.86–0.89. — own calc. from [Gao et al. 2023](https://cris.unibo.it/bitstream/11585/955904/3/PDIV%20prediction%20Gao%20PREPRINT_clean.pdf)
- Hewitt et al. used PDIV(230 °C) ≈ 0.86 × the room-temperature value, taken from a twisted-pair temperature/pressure equation in the literature. — [Hewitt et al., IEEE ECCE 2022, doi:10.1109/ECCE50734.2022.9948103 [FT]](https://eprints.whiterose.ac.uk/id/eprint/201859/)
- Furukawa's twisted pairs at 25–230 °C:
  - PDIV falls with temperature, at a material-dependent rate.
  - An air-density (Paschen) correction alone over-predicts PDIV above 150 °C.
  - The rise of εr with temperature explains the rest. PAI rises linearly. PEEK rises sharply above 150 °C, i.e., above its Tg.
  - The PDIV ratio in Fig. 7 spans 70–100%; individual curve values are not in the text.

  — [Furukawa Review 45 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- PDIV falls monotonically up to about 150 °C and then stays roughly constant up to 240 °C in form-wound Litz windings (Balachandran 2018). From 25 to 230 °C, PEEK twisted pairs drop slightly more than PAI (Muto 2014). PAI and PEEK (100 and 130 µm) twisted pairs drop monotonically at 23, 100 and 180 °C (He et al., ICD 2022, doi:10.1109/ICD53806.2022.9863473). — [Ji, Giangrande, Zhao, Energies 17 (2024) 3980, doi:10.3390/en17163980 [FT review; primaries SEC]](https://www.mdpi.com/1996-1073/17/16/3980)

**Humidity and surface contamination**

- Furukawa tested two parallel rectangular wires (100 mm, 50 Hz, 25 °C):
  - PDIV retention at 95% RH relative to 50% RH was **80% for PPS and 74% for PAI**.
  - PD charge at inception fell from about 100 pC (50% RH) to about 10 pC (95% RH).
  - EPMA found Na, K and Cl from bare-hand handling on the surface. After washing in pure water the humidity dependence almost disappeared. Re-touching with bare hands brought it back.
  - Soaking PPS in water for 24 h raised εr by only about 3%, worth 1–2% of PDIV.

  — [Furukawa Review 45 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- A much larger PDIV drop occurs for a PEEK wire than for PAI when RH goes from 80% to 100% (He et al., ICD 2022). Impregnated twisted pairs are more humidity-sensitive because the varnish is porous (Ji et al., IEEE TTE 2023, doi:10.1109/TTE.2023.3287197). — [Ji/Giangrande/Zhao 2024 review [SEC]](https://www.mdpi.com/1996-1073/17/16/3980)

**Pressure and altitude**

- Driendl, Pauli and Hameyer (IEEE TIE 2022) derived a pressure enhancement factor of 1.25 for a worst case of 500 mbar in automotive use (vehicles up to 5500 m). Billard et al. (EIC 2016) found that the PDIV benefit of Grade I/II/III builds (28/53/80 µm) shrinks at 100 mbar. Discharge power rises about eightfold from 1750 to 100 mbar. — [Ji/Giangrande/Zhao 2024 review [SEC]](https://www.mdpi.com/1996-1073/17/16/3980)
- In a 1 kV slot design (200 µm insulation, εr 3.9), PD is negligible at 1 bar. At 230 mbar (35,000 ft), PD can start in defects larger than 10 µm, up to a 600 µm air gap. — [Ramin, Montanari, Yang, Materials 14 (2021) 7555, doi:10.3390/ma14247555 [FT]](https://www.mdpi.com/1996-1944/14/24/7555)

### Inferences

- **Required PD-free levels at 800, 1200 and 1600 V (own calc.)**
  - Method: I scaled the IEC 60034-18-41/Lusuardi factors already used in the existing report. These are overshoot factor OF 1.2–1.5; EF_PD 1.25; EF_ageing 1.2; EF_T 1.3 for turn-to-turn and phase-to-phase and 1.1 for phase-to-ground; and winding factor WF 1.4 for phase-to-ground and 2 for phase-to-phase.
  - For turn-to-turn I used WF 0.7 (the random-wound default) and WF 1.0. WF 1.0 is my assumption for hairpin slots, where adjacent bars can belong to distant parts of the path.

  | Bus | V_LL,rms fundamental (SPWM to SVPWM max) | T/T (WF 0.7) | T/T (WF 1.0) | P/G | P/P |
  |---|---|---|---|---|---|
  | 800 V | 490–566 V | 1.31–1.64 kVpp | 1.87–2.34 kVpp | 2.22–2.77 kVpp | 3.74–4.68 kVpp |
  | 1200 V | 735–849 V | 1.97–2.46 kVpp | 2.81–3.51 kVpp | 3.33–4.16 kVpp | 5.62–7.02 kVpp |
  | 1600 V | 980–1131 V | 2.62–3.28 kVpp | 3.74–4.68 kVpp | 4.44–5.54 kVpp | 7.49–9.36 kVpp |

- **Implied insulation build (own calc.; extrapolations).** I assumed an AC test with the same peak-to-peak value (AC peak = Vpp/2) and used the Gao fits and Dakin with εr 3.5.
  - **Turn-to-turn, per wire:**
    - 800 V: ≤35–72 µm. The low end is outside the fitted range and sets no real constraint.
    - 1200 V: about 40–163 µm.
    - 1600 V: about 77–270 µm. With the room-temperature fit plus EF_T, the worst case is 255–270 µm. With the 180 °C fit, it is about 200 µm.
  - **Phase-to-ground, total** (slot liner + enamel; Gao Eq. 5 at 180 °C): about 230–380 µm at 800 V, 530–750 µm at 1200 V, 820–1120 µm at 1600 V.
  - **Phase-to-phase, total** (Gao Eq. 3 at room temperature with EF_T): about 290–410, 530–710 and 770–1010 µm.
  - The Gao fits were built on Dt of 80–350 µm, so values above about 350 µm are extrapolations.
- **Steep thickness penalty.** Dakin's exponent of 0.46 means the required d/εr scales as V^2.17. Doubling the voltage needs about 4.5× more t/εr, so thickness quickly becomes impractical for slot fill.
  - Own calc. with Dakin (room temperature): for 2.0 kVpk, the per-wire build is about 192 µm at εr 3.5 versus about 115 µm at εr 2.1 (PFA/FEP-like). For 4.0 kVpk it is about 870 versus 520 µm.
  - So low εr, foamed enamels, field grading and air-wedge-free construction (impregnation or potting) are the levers, rather than thickness alone.
- **Moving beyond Type I.** At 1200 V and 1600 V the fundamental line voltage (735–1131 V rms) exceeds the 700 V rms boundary that IEC 60034-18-41 links with Type I systems (see Q4). PD-free (Type I) design is still possible, but outside the standard's typical domain.
- **For the planned study:**
  - Control surface ionic contamination (gloves, documented cleaning), because the RH sensitivity in Furukawa came from hand contamination, not from the polymer.
  - Measure at ≥180 °C, with RH reported.
  - Use one PD threshold across all voltage levels.

### Gaps
- No peer-reviewed hairpin turn-to-turn PDIV dataset above about 350 µm total build or about 1.9 kVpk was found. All 1200 and 1600 V thickness numbers above are extrapolations.
- No published fit of Dakin's prefactor and exponent specifically for flat or rectangular conductors was found. Gao reports that Dakin fails for composites.
- The ETH Zurich twisted-pair d/εr model (IEEE TDEI 2023, "On the Frequency Dependence of the PDIV in Twisted Pair Magnet Wire Analogy in Dry Air", research-collection.ethz.ch handle 20.500.11850/610475) could not be opened (HTTP 500). Its parameters are not recorded here.
- The Elorza Azpiazu 2024 temperature-model equation is embargoed. The Elmezain 2026 TTE model numbers (including cooling oil) were not accessible.
- The hairpin-specific turn-to-turn winding factor depends on the winding plan. These leads were not read:
  - [Springer e&i 2025, doi:10.1007/s00502-025-01333-1](https://link.springer.com/article/10.1007/s00502-025-01333-1), on winding-plan criteria to reduce common-mode stress at 800 V.
  - [EP4024060A1](https://patents.google.com/patent/EP4024060A1/en), a hairpin insulation test-model patent.

## Q2. How the candidate technologies compare, including voltage endurance under repetitive impulses

### Takeaway
PD inception is set by t/εr and by air-wedge geometry. So low-εr thermoplastics (PFA/FEP about 2.0–2.1; PEEK about 3.1–3.2 at room temperature but 4.5–4.7 at 200–250 °C) and foamed enamels win on PDIV per µm.

Corona-resistant (CR) fillers do not raise PDIV; they slow erosion once PD has started. Under PD, the inverse-power-law (IPL) exponent n of non-CR material falls from about 10 to 5.4, while CR stays at about 10. Once PD is present, organic Type I systems last minutes to hours. Glass-fibre and mica (Type II) builds tolerate PD but need thicker insulation, and in one study a thinner PEEK wire reached higher RPDIV after poling. No PD or endurance data were found in this search for parylene, epoxy powder or PFA on hairpins.

### Cited Findings

- **IPL exponents and design fields** (Ramin et al.; 60 Hz accelerated life tests at 1% failure probability, thin specimens):
  - For a life of 2×10^5 h, non-CR material allows ≤7 kV/mm and CR material ≤36 kV/mm.
  - With size scaling (0.03 → 0.2 mm thick, design length 10× test length, Weibull βe = 2), the CR design field drops from 36 to about 4.5 kV/mm and non-CR to 0.8 kV/mm.
  - The IPL exponent n "drops down for NCR (from 10 to 5.4) when PD are active, but it remains almost constant (about 10) for CR materials".
  - The authors adopt a 5 kV/mm design field and recommend CR material "always" as redundancy.

  — [Ramin, Montanari, Yang, Materials 14 (2021) 7555 [FT]](https://www.mdpi.com/1996-1944/14/24/7555)
- **Kapton 200CR tape** (50 µm nominal; a PI core between two nanostructured outer layers; adhesive-backed and wrapped):
  - Pristine PDIV B10 ≈ 1590 Vpp (50 Hz, 20 °C, 25% RH, 5 pC sensitivity).
  - Endurance at 7 kVpp, 1 kHz unipolar square wave: B10 time to failure fell from about 80 min to about 40 min (about −50%) after sequential ageing at 270 °C/864 h, then 80 °C/80% RH/294 h, then 320 °C (stated elsewhere as 300 °C)/432 h.
  - The chapter has internal inconsistencies: thickness 50 versus 100 µm; stage 3 at 320 versus 300 °C; a "90%" PDIV loss in the conclusions versus about 9% in the results.

  — [Han & Cavallini, "Electrical Endurance of Corona-Resistant Polyimide for Electrical Traction", IntechOpen 2020, doi:10.5772/intechopen.93253 [FT, read via fetch tool]](https://www.intechopen.com/chapters/72854)
- **Frequency dependence of endurance (unfilled conventional enamel twisted pairs, SiC pulse generator):**
  - Average failure at about **4 min at 11 kHz versus about 55 min at 1 kHz**. Life "decreases almost linearly with increasing frequency".
  - Shorter rise time and higher temperature also shorten life (values only in figures).
  - Bench: 1.5 kV peak, rise time >25 ns, ≤60 kV/µs, 20 kHz, >180 °C; extendable to 0.4–12 kVpp, 200 kV/µs and 2–20 kHz.

  — [Sahan et al., Bodo's Power Systems Apr 2024, doi:10.25968/opus-3119 [FT]](https://serwiss.bib.hs-hannover.de/frontdoor/deliver/index/docId/3119/file/sahan_etal2024-dv-dt_pulse_generator_testbench.pdf). Own calc.: the frequency exponent γ = ln(55/4)/ln(11) ≈ 1.09, i.e., life ∝ f^−1.
- **Glass fibre (Type II) versus PEEK (Type I) under unipolar square waves:**
  - Glass fibre: Von Roll 2 Silix VSI, 100 µm on 0.9 mm Cu, silicone varnish, TI 200 °C.
  - PEEK: Zeus, 40 µm on 0.9 mm Cu, TI 245 °C.
  - After poling, the thinner PEEK wire "can deliver a considerably higher RPDIV" than the thicker glass-fibre wire. In one case PEEK gave 150 V higher PDIV despite being thinner. Polarity, frequency and rise-time details are in Q3.

  — [Naderiallaf, Giangrande, Galea, IEEE Access 11 (2023), doi:10.1109/ACCESS.2023.3279886 [FT]](https://aisberg.unibg.it/retrieve/edaf162d-7b1c-4f32-b1df-9de9c6f1b09d/J42.pdf)
- **CR wires and pressure.** CR magnet wires show "improved ground-level behavior but are not viable at reduced pressures". The review cites the same paper: PDIV and failure probability are almost unchanged between CR and non-CR wires at 1000 and 100 mbar. — [Rumi, Marinelli, Barater, Cavallini, Seri, IEEE TTE 8(4) (2022) 4646–4653, doi:10.1109/TTE.2022.3191064 [ABS]](https://doi.org/10.1109/TTE.2022.3191064); [Ji/Giangrande/Zhao 2024 review, Fig. 10 [SEC]](https://www.mdpi.com/1996-1073/17/16/3980)
- **CR wire in a machine design.** A starter/generator case study compares CR (added inorganic layer) and non-CR wire on PDIV, electrical endurance, thermal properties, slot fill and rated current. The abstract gives no numbers. — [Ji et al., IEEE TTE 9(2) (2023) 3192–3202, doi:10.1109/TTE.2022.3230055 [ABS]](https://unnc.globalimpact.cn/en/publications/electrical-machine-design-considering-corona-resistant-wire-for-m)
- **CR versus conventional enamel ageing.** Corona-resistant "B" enamel ages better than conventional enamel under both sine and PWM-like waveforms, and PWM degrades faster than sine (Guastavino et al.). — [Höpner & Wilhelm, Energies 14 (2021) 1738, doi:10.3390/en14061738 [FT survey; primary SEC]](https://www.mdpi.com/1996-1073/14/6/1738)
- **Enamel + thermoplastic and porous enamel (Furukawa).**
  - A two-layer build (enamel plus an outer thermoplastic layer) gives thick insulation "difficult in conventional enamel wires". It lets designers drop inter-layer insulation paper and shorten coil ends.
  - A PAI enamel containing air bubbles lowers εr as porosity rises (values only in a figure).

  — [Furukawa Review 45 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- **PFA wire [VEND].** PFA-insulated magnet wire (Daikin with Additive Drives) halved insulation thickness versus PAI enamel wire while giving "higher PDIV". The resulting copper-fill increase gave ">10%" more continuous power. It is marketed for "800+ V" passenger cars, commercial vehicles and heavy trucks. No PDIV values, test conditions or thicknesses are published. — [Daikin Chemical Europe blog, 6 Feb 2025 [VEND]](https://www.daikinchem.de/blog/boosting-electric-motor-performance/)
- **Thermal-ageing comparison, PEEK versus nanofilled enamel.**
  - PDIV fell 32% for PEEK versus 42% for nanofilled "Allotherm" enamel after 16 ageing cycles.
  - The changes in differential dissipation factor and capacitance were 2.4× and 4.5× larger for the enamel.
  - Estimated RTI: 245 °C for PEEK and 226.25 °C for the enamel.

  — [Khowja et al., IEEE Access 2024, doi:10.1109/ACCESS.2024.3374637 [ABS via DOAJ]](https://doi.org/10.1109/ACCESS.2024.3374637)

### Inferences

- **Ranking for PDIV per µm** (own inference from t/εr scaling and the εr values already in the existing report):
  1. PFA/FEP (εr about 2.0–2.1) and Parylene HT (about 2.2)
  2. Foamed PI/PAI
  3. PI/FEP tape (about 2.6–3.5)
  4. PEEK at room temperature (about 3.1–3.2), losing ground above Tg (143 °C) as εr rises to 4.5–4.7
  5. PI enamel (about 3.0–3.5)
  6. PAI and PEsI/PAI (about 3.9–4.6)

  CR-filled enamels and Kapton CR should not be expected to raise PDIV; their value lies in survival once PD starts.
- **How endurance scales with voltage (own calc.).** With n ≈ 10 (CR, or non-CR without PD), a 1.5× field increase (800 → 1200 V at the same thickness) shortens life by about 1.5^10 ≈ 58×, and a 2× increase (→ 1600 V) by about 2^10 ≈ 1000×. With n = 5.4 (non-CR under PD), the factors are about 9× and 42×. In both cases the life is already short because PD is present.
  - Comparison of the two worst cases assumes equal starting lives, which is not the case: non-CR life under PD starts from a much lower baseline.
  - The planned 1200/1600 V tests on unchanged builds will therefore mostly measure PD-driven failure, not thermal ageing.
- **Type II comparators.** Glass fibre and mica tapes should be treated as PD-tolerant comparators rather than PD-free ones. Their measured advantage depends on poling, polarity and frequency (Q3).

### Gaps
- No repetitive-impulse IPL exponents for extruded PEEK, PI/FEP or PFA hairpin wire were found in open sources.
- No PD or endurance data for parylene, epoxy powder or PFA on rectangular conductors were found in this search.
- Wang, Cavallini, Montanari, "The influence of repetitive square wave voltage parameters on enameled wire endurance" (IEEE TDEI 2014) was seen only as a listing. A search excerpt said other studies give frequency exponents of 0.6–0.8 rather than 1; I could not confirm which paper this comes from.
- An AGC Chemicals slide deck reportedly gives PDIV of about 800–900 V for PI enamel and about 1400 V for PI + PEEK, with a "new criterion" above 1500 V. I could not open the PDF (blocked), so this is unverified and should not be cited.
- A patent (US12518895) said, according to a search excerpt, that 800 V motors need an effective PDIV of ≥1400 V. The USPTO PDF is image-only, so this is unverified.

## Q3. Effects of SiC rise times and high switching frequency (PD, insulation heating, turn-to-turn ageing), and of DC or unipolar stress at higher DC voltages

### Takeaway
With SiC, the DC-link voltage, not the rise time (20–60 ns), dominates terminal overshoot and life. In one SiC ageing study (230 °C), life went from 802 h at 600 V (no PD) to 54–403 h at 800 V and 1.1–8.4 h at 1000 V. PD occurred on about 30% of switching events at 800 V and about 80% at 1000 V.

Rise-time effects on inception are modest: about 6% lower PDIV going from 800 ns to 100 ns on a mica coil. Under unipolar repetitive pulses, surface and interface charge and bulk space charge shift PDIV and RPDIV by 0.1–1.2 kV over one hour of poling, most strongly at fast rise times and high repetition rates. No quantitative dielectric-heating data for low-voltage hairpin insulation were found.

### Cited Findings

- **Rise times in IEC 60034-18-41.** Converter rise times are 0.05–2.0 µs, and the standard's default is 0.3 µs. Turn-to-turn severity is specified through peak-to-peak voltage and rise time. — [IEC 60034-18-41:2014 preview (iTeh), Introduction and terminal-voltage section [FT preview]](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **SiC ageing study by bus voltage (Hewitt et al.).** Setup: 2.8 kW random-wound PM servo stators (Nomex 410 slot liner, polyester resin), 230 °C oven, two-level SiC inverters, fractional-factorial design over 600/800/1000 V, 20/40/60 kHz and 20/40/60 ns. Results (Table VI) by bus voltage:

  | Bus | Lifetime | Electrical loss of life |
  |---|---|---|
  | 600 V, no PD (sample 1) | 802 h | 0% |
  | 600 V, PD present | 106.6–412.6 h | 44.5–86.2% |
  | 800 V | 53.6–402.8 h | 25.4–86.6% |
  | 1000 V | 8.4, 1.1 and 2.6 h | 97.6–99.85% |

  - The thermal life expected without PD is 840 h. Arrhenius fit: L0 = 1917.6 h at 215 °C, B = 13497 K.
  - Terminal-to-ground jump voltages were 900–1241 V at 600 V, 1191–1270 V at 800 V and 1448–1834 V at 1000 V. DC-link voltage was the key parameter; rise time over 20–60 ns had only a weak effect.
  - PD occurred on about 12% of switching events at 600 V (sample 6), about 30% at 800 V (about 2 PD per PWM cycle) and about 80% at 1 kV (4.8 PD per cycle).
  - Ageing lowered εr and capacitance, which raised surge impedance and overshoot during the test.

  — [Hewitt, Sundeep, Wang, Griffo, Diab, Yuan, IEEE ECCE 2022, doi:10.1109/ECCE50734.2022.9948103 [FT]](https://eprints.whiterose.ac.uk/id/eprint/201859/1/ECCE%202022%20paper%20Experimental%20assesment%20of%20Lifetime%20Final_resub.pdf). Own calc.: the overshoot factor was 1.49–1.59 p.u. at 800 V and 1.45–1.83 p.u. at 1000 V.
- **Rise-time effect on a mica coil (Hu et al.).** Setup: 2 kV-rated form-wound coil with mylar-mica tape groundwall, 10 µs pulse width, rise/fall time reduced from 800 ns to 100 ns.
  - Average PDIV fell from 3.95 to 3.71 kV. The authors call this 6.5%; it computes to 6.1%.
  - Fitted model: PDIV(trf, tw) = k(tw)·[ln(trf) − x0] + y0, with k(tw) = a·e^(−tw/t0) + b. Parameters: a = 0.081, b = 0.047, t0 = 49.16, x0 = 3.90, y0 = 3.63; R² = 0.976.
  - Repetition rate and duty (1–8 kHz) changed RPDIV by less than 90 V.
  - Unipolar and bipolar RPDIV were close, bipolar slightly higher.
  - The SPWM modulation index changed RPDIV by less than 75 V.

  — [Hu et al., IEEE OJPEL 2 (2021) 225–235, doi:10.1109/OJPEL.2021.3069780 [FT via PMC]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/)
- **Unipolar square waves: polarity and space charge (Naderiallaf et al.).** Setup: 1013 mbar, rise time 80 or 800 ns, 50 Hz or 2.5 kHz, poling at 0.85 × PDIV for up to 1 h, 5 fresh samples per case.

  Glass fibre (Type II), PDIV:
  - 80 ns, 50 Hz: −90 V after 1 h with positive polarity; +210 V with negative.
  - 80 ns, 2.5 kHz, positive: +150 V after 1 h.
  - 80 ns, 2.5 kHz, negative: +450 V in the first half hour, then −210 V by 1 h.
  - 800 ns, positive: −250 V, to a minimum of 1.79 kV.

  Glass fibre, RPDIV versus frequency:
  - At 2.5 kHz RPDIV is lower than at 50 Hz by 820 V (positive, unpoled) and 680 V (positive, after 1 h).
  - With negative polarity, the corresponding drops are 530 V and 700 V.

  PEEK (Type I), RPDIV:
  - At 2.5 kHz with positive polarity, RPDIV is 800 V below the 50 Hz value after 0.5 h of poling.
  - It is 1.18 kV higher under negative than positive polarity after 0.5 h (80 ns, 2.5 kHz).
  - Before poling it is 450 V (positive) and 120 V (negative) lower at 80 ns than at 800 ns.
  - After poling with negative polarity it is 820 V (0.5 h) and 770 V (1 h) higher at 80 ns.

  The authors attribute these shifts to interface charge from PD between consecutive pulses and to bulk space charge. Variation is largest at the fastest rise time and highest repetition rate. They equate poling time with motor service hours.

  — [Naderiallaf, Giangrande, Galea, IEEE Access 11 (2023), doi:10.1109/ACCESS.2023.3279886 [FT]](https://aisberg.unibg.it/retrieve/edaf162d-7b1c-4f32-b1df-9de9c6f1b09d/J42.pdf)
- **Bipolar versus unipolar inception (Wang et al.).** Bipolar repetitive square waves give higher PDIV than unipolar ones of either polarity, which the authors attribute to space-charge accumulation before PD. Very short rise times with high overshoot gave higher PDIV, and the rise-time effect depends on the overshoot's shape and duration. The abstract has no numbers. — [Wang, Xu, Wang, Zhou, Cavallini, CEIDP 2016, doi:10.1109/CEIDP.2016.7785635 [ABS]](https://cris.unibo.it/handle/11585/598932)
- **Turn-voltage concentration with fast switching.** With very short switching times the voltage drop concentrates on the first couple of turns. In a 1 kV segmented aircraft design the first-turn maximum was 150 V (166.6 V × 0.9), and later turns were negligible. — [Ramin et al. 2021 [FT]](https://www.mdpi.com/1996-1944/14/24/7555)
- **SiC-fed rail traction motor turn insulation (CRRC Zhuzhou / Sichuan University).** Turn insulation of 0.23 mm and 0.30 mm was tested for PDIV and endurance versus voltage, frequency, rise time and temperature. The thicker build performed better, and temperature and rise time strongly affected life. The abstract gives no numbers. — [Luo et al., Insulating Materials 57(4) (2024) 88–99, doi:10.16790/j.cnki.1009-9239.im.2024.04.013 [ABS]](https://castjournals.cast.org.cn/joweb/jycl/EN/1209927811654095527)
- **Frequency.** Switching frequency over 50–1000 Hz barely changes PDIV but changes PD amplitude and number, especially at low pressure. Unipolar-impulse RPDIV falls with switching frequency and levels off by about 100 kHz. — [Ji/Giangrande/Zhao 2024 review [SEC]](https://www.mdpi.com/1996-1073/17/16/3980)
- **Frequency and endurance.** Life falls roughly linearly with pulse frequency: 55 min at 1 kHz versus 4 min at 11 kHz. — [Sahan et al. 2024 [FT]](https://serwiss.bib.hs-hannover.de/frontdoor/deliver/index/docId/3119/file/sahan_etal2024-dv-dt_pulse_generator_testbench.pdf)

### Inferences

- **Bus voltage drives overshoot (own inference).** Because DC-link voltage, not 20–60 ns rise time, sets the overshoot, the 1200 and 1600 V cases should be modelled mainly as a peak-to-peak scaling. SiC rise time mostly matters for how voltage is distributed between turns (the first coil or first bars).
- **Hairpin first turn exposure.** In hairpin windings the first bar of each coil group is directly exposed to the front. A segmented or interleaved winding plan can cut the turn-to-turn share (cf. Ramin's 150 V first-turn design), which matters more at 1600 V than at 800 V.
- **Dielectric heating is likely negligible (own order-of-magnitude estimate; assumptions are mine).**
  - Inputs: εr 4.5, tanδ 0.02, an equivalent 50 kHz harmonic content, 2 kV/mm rms in a 100 µm build over a 12 mm perimeter.
  - Volumetric loss: P/V = 2π f ε0 εr tanδ E² ≈ 1 W/cm³, i.e., about 1.2 W/m of conductor.
  - The temperature rise across the insulation is about 0.05 K (k ≈ 0.2 W/m·K).
  - For comparison, copper loss is about 130 W/m at 200 A rms in 8 mm² Cu at 150 °C.
  - So dielectric heating is unlikely to matter for low-voltage hairpin insulation compared with PD erosion and copper loss. This should be checked if MHz-range ringing or very high-εr fillers are involved.
- **DC component (own inference).** In an EV drive the winding sees bipolar common-mode steps around a chassis reference set by the Y-capacitors, not a steady DC field across the turn insulation. The space-charge relevance at higher DC bus therefore lies in repetitive same-polarity edges and in poling over service hours, as in Naderiallaf 2023, rather than in pure DC conduction. Under unipolar edges, RPDIV can drift by up to about ±1 kV within an hour, so test protocols at 1200 and 1600 V should fix polarity, frequency and pre-stress time.

### Gaps
- No open data were found on dielectric heating of low-voltage enamel, PEEK or PI/FEP under SiC PWM.
  - Leads: Gavrilenko et al., EAPPC 2021 (HAL hal-04404713) on high switching frequency and dielectric-barrier discharges in enamel; not read.
  - Lead: the ETH Zurich paper "Dielectric Losses in Dry-Type Insulation of Medium-Voltage Power Electronic Converters" ([research-collection.ethz.ch](https://www.research-collection.ethz.ch/entities/publication/50d03886-e9e0-40f0-a601-36717f41f1c6)), which gives analytical PWM loss expressions; not read.
- No hairpin-specific RPDIV versus rise time data at 1200–1600 V were found. The CRRC paper's numbers are behind the abstract.
- No study was found comparing a DC-biased inverter waveform with a pure bipolar one on enamelled flat wire (as also noted in a search excerpt).
- Hewitt's data are for random-wound windings, not hairpins.

## Q4. Insulation designs publicly reported for 800 V passenger-car motors and for 1200 V+ machines (trucks, off-highway, rail, e-aviation): Type I or Type II?

### Takeaway
IEC 60034-18-41 associates PD-free Type I systems with machines "rated at 700 V r.m.s. or less" and random windings. Type II (IEC TS 60034-18-42) is associated with form-wound coils "mostly rated above 700 V r.m.s.". An 800 V bus (490–566 V rms line voltage) sits in Type I territory, and public 800 V hairpin designs aim to be PD-free using thicker or low-εr wire. A 1200 or 1600 V bus (735–1131 V rms; own calc.) crosses into the typical Type II domain.

Open sources show only aerospace (1 kV-class) and rail examples of how the step is handled: PD-free thickness at ground level, plus CR or Type II materials, VPI and PD monitoring as backup. No public 1200–1600 V truck or off-highway hairpin insulation designs were found.

### Cited Findings

- **IEC scope wording.** Type I systems are "generally used in rotating machines rated at 700 V r.m.s. or less and tend to have random wound windings". Type II systems "tend to have form-wound coils, mostly rated above 700 V r.m.s.". Type II qualification uses "destructive ageing" and life curves under repetitive impulses, including any stress grading. — [IEC 60034-18-41:2014 preview, Introduction [FT preview]](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Line voltage by bus voltage (own calc.).** Fundamental line-to-line rms is 0.612·Vdc for SPWM and up to 0.707·Vdc for SVPWM:

  | Bus | Line-to-line rms |
  |---|---|
  | 800 V | 490–566 V |
  | 1200 V | 735–849 V |
  | 1600 V | 980–1131 V |

- **800 V hairpin wire build.** Furukawa's HV/EV rectangular wire puts a thermoplastic layer over the enamel to get thick, high-PDIV insulation, which lets inter-layer paper be dropped. — [Furukawa Review 45 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf). (Existing report: Essex HVWW, Victrex XPI 80–300 µm, Sumitomo foamed PI, PAI Grade 3 for 800 V.)
- **PFA for 800+ V [VEND].** PFA magnet wire is marketed for "800+ V" passenger cars, commercial vehicles and heavy trucks, with about half the build of PAI enamel. — [Daikin 2025 [VEND]](https://www.daikinchem.de/blog/boosting-electric-motor-performance/)
- **Aerospace hairpin at 800 V.** Six PEEK-insulated hairpin wire types were assessed for an 800 V DC bus at up to 25,000 ft, using PDIV under 20 kHz PWM with 15 ns rise time and 50% duty, below and above Tg. — [Naderiallaf, Degano, Gerada, Gerada, CMD 2024, pp. 226–229, doi:10.23919/CMD62064.2024.10766278 [ABS]](https://unnc.globalimpact.cn/en/publications/investigating-the-thermal-aging-effect-on-hairpin-peek-insulated-/)
- **1 kV electric-aircraft motor (Ramin et al.).** Minimum PD-free thicknesses for a 100 µm cavity at 230 mbar (Table 1):

  | Condition | Turn-to-turn | Phase-to-ground | Phase-to-phase |
  |---|---|---|---|
  | Nominal | 43 µm at 150 V | 770 µm at 1000 V | 110 µm at 333 V; worst case 1200 µm at 1333 V |
  | Benign test | 55 µm at 227 V | 1150 µm at 1287 V | 700 µm at 953 V; worst case 1650 µm at 1619 V |
  | Extreme test | 250 µm at 529 V | 2070 µm at 1892 V | 3500 µm at 2621 V (worst case) |

  - The authors conclude that PD "cannot be always avoided even through conservative design criteria".
  - They recommend corona-resistant materials, VPI to avoid cavities, and frequent PD diagnostics or monitoring.

  — [Ramin, Montanari, Yang, Materials 14 (2021) 7555 [FT]](https://www.mdpi.com/1996-1944/14/24/7555)
- **CR wires at altitude.** CR wires are judged not viable at reduced pressure. — [Rumi et al., IEEE TTE 2022 [ABS]](https://doi.org/10.1109/TTE.2022.3191064)
- **NASA eVTOL insulation testing.** NASA is building lifetime models for eVTOL winding insulation from twisted pairs and potted motorettes (heavy-build MW-16C PI wire; aramid slot liner 0.08 mm). Thermo-mechanical cycling matters more than thermo-chemical ageing (numbers in Q5). — [Tallerico, Anderson, Hurrell, Gutknecht, Valco, NASA GRC, NTRS 20240007451 (2024) [FT]](https://ntrs.nasa.gov/api/citations/20240007451/downloads/Winding%20Lifetime%20Testing%20V4.pdf)
- **Rail traction with SiC.** CRRC qualifies turn insulation of 0.23 and 0.30 mm for SiC-fed high-voltage traction motors. — [Luo et al. 2024 [ABS]](https://castjournals.cast.org.cn/joweb/jycl/EN/1209927811654095527). (Existing report: CRRC uses corona-resistant PI/FEP tape on inverter-fed rail traction motors.)
- **Type II on a 2 kV form-wound coil.** The groundwall is mylar-mica tape plus Dacron-glass armour and varnish. PDIV is about 3.7–4.0 kV under fast pulses. — [Hu et al. 2021 [FT via PMC]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/)
- **Si-designed insulation on SiC.** A servo motor insulated for Si-IGBT drives showed PD in most samples already at 600 V with SiC. The authors conclude its phase-to-phase insulation would need enhancement to run at 600 V on SiC. — [Hewitt et al. 2022 [FT]](https://eprints.whiterose.ac.uk/id/eprint/201859/)

### Inferences

- **Industry practice by voltage (own inference).**
  - 800 V passenger cars: Type I (PD-free) design remains the norm. Thicker extruded or low-εr wire is used, and qualification follows IEC 60034-18-41.
  - 1200–1600 V (heavy trucks, off-highway, aircraft, rail): open literature points to hybrid strategies. These are PD-free sizing at ground level plus CR materials, stress control, impregnation and monitoring, and for rail, Type II tapes and mica.
  - IEC wording makes 700 V rms a typical, not mandatory, boundary.
- **Required PDIV at higher bus (own calc., Q1 table).** The jump from 800 to 1600 V doubles the required PDIV. Phase-to-phase and phase-to-ground builds of about 0.8–1.1 mm (1600 V) would be needed for a PD-free hairpin. That is incompatible with high slot fill, so in practice the 1600 V case is likely to be PD-tolerant (Type II-like) or to need winding and segmentation measures.

### Gaps
- No public insulation build, PDIV target or Type I/II statement was found for any 1000–1600 V road vehicle or off-highway hairpin motor. This includes heavy trucks and BYD's 1000 V platform; searches returned only launch news.
- No OEM-published PDIV acceptance values for 800 V hairpin motors were found. Only vendor and patent statements exist, and some were unverifiable (Q2 Gaps).
- These leads were not read:
  - ["Electrical Insulation at 800 V Electric Vehicles" (ResearchGate 348370015; German with English abstract; authors not checked)](https://www.researchgate.net/publication/348370015_Electrical_Insulation_at_800_V_Electric_Vehicles)
  - ["Lifetime Model for Inverter-fed Electrical Machines Windings Including Thermal Aging and PD Risk" (ResearchGate 384892624; includes an 800 V aircraft case)](https://www.researchgate.net/publication/384892624_Lifetime_Model_for_Inverter-fed_Electrical_Machines_Windings_Including_Thermal_Aging_and_Partial_Discharge_Risk)
  - ["The Insulation Resilience of Inverter-Fed Low Voltage Traction Machines" review](https://www.researchgate.net/publication/363897798_The_Insulation_Resilience_of_Inverter-Fed_Low_Voltage_Traction_Machines_Review_Challenges_and_Opportunities)

## Q5. Which capability measures change after thermal or oil ageing (PDIV/RPDIV, water uptake), and by how much?

### Takeaway
Thermal ageing alone lowers PDIV by roughly 24–42%: PI −24% (270 °C, 500 h), PEEK −32%, nanofilled enamel −42%. Thermo-mechanical cycling is more damaging: a potted PI motorette lost 56% of turn-to-turn PDIV. Humidity or water uptake costs about 9% (CR PI, with εr +8%), and up to 20–26% at 95% RH when surfaces are contaminated. PD-assisted SiC ageing left phase-to-ground PDIV 17–78% lower at failure. Endurance under impulses fell about 50% for Kapton CR after combined thermal and humid ageing. No peer-reviewed PDIV or RPDIV data after ATF or e-fluid ageing were found.

### Cited Findings

- **PEEK versus nanofilled enamel, thermal ageing.** After 16 thermal ageing cycles, PDIV fell 32% for PEEK and 42% for nanofilled "Allotherm" enamel. Both showed delamination. Estimated RTI was 245 °C for PEEK and 226.25 °C for the enamel; the authors report lifetimes 72.1% (PEEK) and 25.5% (enamel) below the manufacturers' RTI claims. — [Khowja et al., IEEE Access 2024, doi:10.1109/ACCESS.2024.3374637 [ABS via DOAJ]](https://doi.org/10.1109/ACCESS.2024.3374637)
- **NASA GRC, heavy-build MW-16C PI wire:**
  - Unimpregnated twisted pairs: PDIV fell from 700 to 532 Vrms after about 500 h at 270 °C (−24%, own calc.). About −180 Vrms after 483 h at 300 °C. Only 25–50 Vrms after cycles at 250 °C.
  - Epoxy-coated pairs: −482 Vrms.
  - Epoxy-potted pairs: about −900 Vrms after the first 270 °C cycle, because of large cracks.
  - Motorettes under eVTOL takeoff/climb thermal cycling: median turn-to-turn PDIV fell from 1250 to 550 Vrms (−56%, own calc.), with every coil losing at least 175 Vrms; half the phase-to-ground coils broke down.

  — [NASA NTRS 20240007451 (2024) [FT]](https://ntrs.nasa.gov/api/citations/20240007451/downloads/Winding%20Lifetime%20Testing%20V4.pdf)
- **Kapton 200CR (Han & Cavallini):**
  - Thermal stage 1 (270 °C) first raised PDIV B10, from 1590 to about 1715 Vpp by 192 h, then it stabilised.
  - Humid stage (80 °C, 80% RH, 294 h): εr at 50 Hz rose from 3.8 to 4.0, PDIV B10 fell from 1660 to 1520 V (−9%), and bulk conductivity rose about 10×. The chapter reports the εr rise as about 8%, but 3.8 → 4.0 is about +5%. Conductivity recovered after re-drying at high temperature.
  - Low-frequency ε′ reached about 7 because of absorbed water.
  - Endurance at 7 kVpp, 1 kHz fell from about 80 to about 40 min overall.

  — [Han & Cavallini 2020 [FT, read via fetch tool]](https://www.intechopen.com/chapters/72854)
- **Water versus surface contamination (Furukawa).** A 24 h water soak raised PPS εr by about 3%, worth only 1–2% of PDIV. The large 20–26% PDIV loss at 95% RH came from ionic (Na/K/Cl) surface contamination. — [Furukawa Review 45 [FT]](https://www.furukawaelectric.com/review/fr045/fr45_04.pdf)
- **SiC + 230 °C ageing (Hewitt et al.).** Phase-to-ground PDIV went from 1246–1685 V before to 350–1029 V at failure (−17% to −78%, own calc.). The authors attribute this to wire insulation thinning (loss of volatiles) and groundwall degradation; εr and capacitance decreased with ageing. — [Hewitt et al. 2022 [FT]](https://eprints.whiterose.ac.uk/id/eprint/201859/)
- **Combined conditions.** When low pressure, high temperature and thermal degradation are combined, PDIV is about 40% below standard ambient (Kaji, Amano, Asai, SAE 2016-01-1226, doi:10.4271/2016-01-1226). — [Ji/Giangrande/Zhao 2024 review [SEC]](https://www.mdpi.com/1996-1073/17/16/3980)
- **Aged PEEK hairpin wires.** At ground pressure and room temperature, fresh PEEK hairpin wires outperform aged ones. At reduced pressure, fresh and aged samples differ only slightly, both at room temperature and above Tg, so low-pressure PDIV is a poor ageing indicator. — [Naderiallaf et al., CMD 2024 [ABS]](https://unnc.globalimpact.cn/en/publications/investigating-the-thermal-aging-effect-on-hairpin-peek-insulated-/)
- **Class-200 enamels aged with conditioning voltage.** Four class-200 twisted-pair enamels (conventional; PEI+PAI; PEI+PAI with TiO2 micro-filler; PEI+PAI with SiO2 nano-filler) were aged at 200, 220, 230, 240 and 250 °C under a 395 Vrms, 500 Hz conditioning voltage below PDIV.
  - PDIV declined over time following an inverse power law in ageing time, extrapolated to 1000 h and 1 year.
  - Changes in DC/AC capacitance and resistance did not explain the decline; increased surface conductivity is suspected.
  - The per-curve values are only in figures and were not extracted.

  — [Khan, Guastavino, Della Giovanna, Torello, Energies 17 (2024) 4578, doi:10.3390/en17184578 [FT]](https://doi.org/10.3390/en17184578)
- **Hotspot temperature margin from aged rectangular wire.** PDIV and PDEV were measured at several temperatures on rectangular automotive wire at different thermal-ageing states. The aim is to set a hotspot temperature margin, replacing the rule of "30 °C below thermal class". — [Ji, Giangrande et al., IEEE TTE 10(1) (2024) 2057–2069 [ABS, via search listing; DOI not captured]](https://research.nottingham.edu.cn:443/en/publications/determination-of-hotspot-temperature-margin-for-rectangular-wire-)

### Inferences

- **Margins to plan for (own synthesis).** For dry-to-aged comparisons in the planned study:
  - PDIV/RPDIV losses of about 25–40% from thermal ageing alone, and more where thermo-mechanical cracking or delamination occurs (PEEK and nanofilled enamels both delaminated).
  - About 10% from water uptake.
  - These are larger than the existing IEC ageing factor of 1.2 (about −17%).
  - So an insulation that is barely PD-free at 800 V when new may not be PD-free after ageing. At 1200 and 1600 V, the ageing margin multiplies the already doubled thickness requirement.
- **Opposing trends for Kapton CR.** In Kapton CR, thermal exposure first raised PDIV (post-cure or drying), while humid exposure lowered it and raised εr and conductivity. Water-content control of the ATF (dry versus wet e-fluid) is therefore likely to dominate PDIV changes after oil ageing (inference; no direct ATF data).
- **Low-pressure PDIV is a weak ageing indicator.** Because PDIV at reduced pressure discriminates little between fresh and aged PEEK, before/after comparisons in the study should be made at 1 bar and at operating temperature.

### Gaps
- No peer-reviewed PDIV/RPDIV values after ATF or e-fluid immersion ageing (with known water content) were found for any hairpin insulation. The existing report's ATF data are patent breakdown and endurance values only.
- A 2025 item, "Impact of Cooling Oil on Partial Discharge and Insulation Reliability in Inverter-Fed EV Motors" (ResearchGate 394109973), could not be accessed. According to a search excerpt only (unverified), oil coating raises PDIV at ambient, the benefit shrinks with temperature, PDIV drops sharply during natural cooling in ester and mineral oils, and thermally aged natural ester causes large PDIV reductions.
- A 2025 Leeds PhD thesis on esters in EV transmission cooling is embargoed until 2029.
- No RPDIV-after-ageing data were found for PI/FEP tapes, PFA, parylene, epoxy powder or glass-fibre-covered rectangular wire. Glass fibre: [Naderiallaf et al., IEEE Access 10 (2022) 41186–41200](https://nottingham-repository.worktribe.com/output/7787609/a-contribution-to-thermal-ageing-assessment-of-glass-fiber-insulated-wire-based-on-partial-discharges-activity) proposes the Weibull shape parameter of PDIV as an ageing indicator; only a search excerpt was seen, not read.
