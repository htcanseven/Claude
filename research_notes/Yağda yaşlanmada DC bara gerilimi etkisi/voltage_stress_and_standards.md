# DC-bus voltage (800 / 1200 / 1600 V) → winding-insulation stresses and standard requirements for inverter-fed traction motors

*Conventions: Vpp = peak-to-peak; Vp = peak (0-to-peak); P/P = phase-to-phase; P/G = phase-to-ground; T/T = turn-to-turn (conductor-to-conductor); Udc = Vdc = DC-link voltage; OF = overshoot factor (terminal peak ÷ Udc); WF = winding factor; EF = enhancement factor; Uj = jump voltage; a = fraction of Uj across the turn insulation. "Calculation" marks my own arithmetic (scripted, reproducible); everything else is cited. All sources were opened on 2026-10-20 unless flagged:
- "search-result extract": only a search-engine summary was readable;
- "preview only": only the cover, contents, foreword, introduction, scope and early definitions of a standard were readable;
- "earlier notes": taken from the 2026-10-10 notes, not re-opened today. This file builds on the 800 V calculation in `reports/Hairpin izolasyon malzemeleri ve yöntemleri.md` (lines 18–46) and on `research_notes/Hairpin izolasyon malzemeleri ve yöntemleri/requirements_and_tests.md` §1; those numbers are reproduced exactly below and extended, not repeated.*

---

## 1. How DC-bus voltage, topology, switching device, rise time, switching frequency, cable length and surge impedance set the P/G, P/P and T/T voltages (including uneven first-turn distribution in hairpin windings)

### Takeaway
For a 2-level inverter, the IEC 60034-18-41 framework gives operating peak-to-peak stresses of P/P = 2·OF·Udc and P/G ≈ 1.4·OF·Udc (both reconstructed from the standard's tables), and T/T = 2·a·Uj (Uj ≈ OF·Udc is my assumption). All three scale linearly with the DC bus, so 1200 V and 1600 V buses raise every stress by ×1.5 and ×2 relative to 800 V. OF is set by the reflection coefficient Γ = (Zm − Zc)/(Zm + Zc) and by whether the rise time is shorter than the cable's round-trip time (critical length ≈ v·tr/2, v ≈ 150–180 m/µs). With SiC rise times (10–50 ns) the critical length shrinks to about 1–2.5 m, so a cabled SiC drive must be assumed to reach OF ≈ 2, and ringing or double pulsing can push it to 3–4 p.u. The fraction a falls hardest on the first turns: 30–90 % of the incident peak, and up to 1.47 p.u. of Udc measured on adjacent first/last turns. A 3-level (NPC/ANPC/T-type) inverter halves each switching step and therefore the jump voltage and T/T stress, but not the P/P peak-to-peak envelope.

### Cited Findings

**Framework, definitions and how severity is specified**
- The drive-system integrator "shall inform the machine manufacturer what voltage will appear at the machine terminals in service". Severity is based on "the impulse rise time, the peak to peak voltage and, in the case of Type II systems, the impulse repetition rate". After installation, the integrator should measure P/P and P/G terminal voltages to check compliance. "A default value of 0,3 µs is attributed to the impulse rise time." — [IEC 60034-18-41:2014+AMD1:2019 CSV, Ed. 1.1, preview only (iTeh)](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf)
- **Definitions (Type II standard, shared with 18-41).**
  - Up = maximum numerical value of a unipolar impulse; for bipolar impulses, Up is half the peak-to-peak value.
  - Ua = steady-state impulse magnitude.
  - Ub = "voltage overshoot: magnitude of the peak voltage in excess of the steady state impulse voltage".
  - PDIV is quoted r.m.s. for sinusoidal voltage and peak-to-peak for impulses.
  - RPDIV = "minimum peak to peak impulse voltage at which more than five PD pulses occur on ten voltage impulses of the same polarity".

  — [IEC 60034-18-42:2017+AMD1:2020 CSV, Ed. 1.1 (2020-08), preview only (VDE-Verlag)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf)
- **Jump voltage.** Uj is the "change in voltage at the terminals of the machine occurring at the start of each impulse when fed from a converter". "The voltage stressing the turn insulation will be a fraction, a, of the jump voltage. This fraction will depend on winding design and will become larger as the rise times get shorter." The maximum turn voltage is "the peak of the jump voltage multiplied by a coefficient, a"; because a is hard to calculate, IEC gives worst-case estimates (an "a vs rise time" figure) — [CIGRE WG D1.43, *Insulation degradation under fast, repetitive voltage pulses*, Technical Brochure final draft (PDF hosted by CIGRE CZ; ISBN not yet assigned; convenor A. Cavallini)](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **What the 18-41 contents list confirms** (body text beyond clause 3.5 not readable):
  - Clause 4 "Machine terminal voltages arising from converter operation" and 5.2–5.4 "Voltages stressing the phase/phase, phase/ground, turn and strand insulation".
  - Figure 2 "Five step phase to phase voltage at the terminals of a machine fed by a 3-level converter".
  - Figure 3 "Jump voltage (Uj) at the machine terminals".
  - Figure 4 "Voltage enhancement at the terminals of a motor due to reflection as a function of cable length for various impulse rise times".
  - Figure 7 "Worst case voltage stressing the turn/turn insulation in a variety of random wound stators as a function of the rise time of the impulse".
  - Figure B.4 "... peak/peak voltage of 2aUj on the turn/turn insulation".
  - Table A.1 "Examples of maximum peak voltages"; Table B.3 "Maximum peak/peak operating voltages related to Udc for a 2-level converter".

  — [IEC 60034-18-41 CSV preview (iTeh)](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf); [IEC 60034-18-41 CSV sample (normsplash)](https://www.normsplash.com/Samples/IEC/165459798/IEC-60034-18-41-2014-AMD1-2019-CSV-en-fr-2.pdf)
- **Winding factors when no measurement or simulation exists.** Lusuardi et al. restate the 18-41 empirical equation as Vc = Vdc·OF·WF·EF_PD·EF_T·EF_Aging, with WF = 2 (P/P), 1.4 (P/G) and 0.7 (T/T) "when experimental results or simulations are missing" — [Lusuardi, Rumi, Cavallini et al., "Partial discharge phenomena in electrical machines for the more electrical aircraft. Part III", IEEE Access 2021 (Zenodo record, as extracted in the earlier notes)](https://zenodo.org/records/4562202)
- **Reproducing the P/P and P/G formulas from the standard's own tables (calculation).** IEC 60034-18-41 AMD1 Table D.1 gives the maximum allowable peak-to-peak voltages in units of U_N for IVIC A/B/C/D:

  | IVIC | P/P | P/G |
  |---|---|---|
  | A | 3.0 | 2.1 |
  | B | 4.1 | 2.8 |
  | C | 5.4 | 3.8 |
  | D | 6.7 | 4.7 |

  These values "are calculated using the formulae described in Clause B.5", without the 1.1 line-variation factor — [AMD1:2019 full amendment text (iTeh sample)](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf); [Table D.1, French text (normsplash sample)](https://www.normsplash.com/Samples/IEC/165459798/IEC-60034-18-41-2014-AMD1-2019-CSV-en-fr-2.pdf).

  With Udc = 1.35·U_N and OF = 1.1/1.5/2.0/2.5, the formulas P/P = 2·OF·Udc and P/G = 1.4·OF·Udc give P/P = 2.97/4.05/5.40/6.75 and P/G = 2.08/2.84/3.78/4.73 × U_N. These match the table to its rounding. *(Calculation.)*

**Reflection, cable length and surge impedance**
- **Reflection basics.** The cable characteristic impedance is "a few tens of Ohms", while the machine's is "generally hundreds of Ohms". The reflection coefficient Γ = (Zm − Zc)/(Zm + Zc) "is often close to unity, and the peak voltage of the surge is doubled at the winding termination". The inverter acts as a short circuit, so the wave reflects back with negative Γ. Propagation speed is 160–180 m/µs. "If the switch closes and opens in a very short time ... the total overvoltage can reach about three times the DC bus voltage." — [CIGRE WG D1.43 TB](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **Measured industrial PWM-drive examples (GAMBICA/BEAMA guide, 4th ed., 2016; device type not stated, IGBT era).**
  - Propagation speed in a typical PVC cable is about 1.7 × 10⁸ m/s ("in 100 ns the pulse travels only 17 m").
  - "With 20 m of cable ... any pulse with a rise-time less than 235 ns can be expected to increase by nearly 100%", i.e. critical length = v·tr/2.
  - Measured at a 460 V supply: "Even with 4 m of cable some overshoot is apparent. With 42 m the overshoot is virtually 100%."
  - With polarity-reversing (bipolar) switching, reflections of "up to 4Ud" are theoretically possible.
  - IEC and NEMA define rise time differently; the IEC value is "approximately twice" the NEMA value.

  — [GAMBICA/BEAMA Technical Guide, *Motor insulation voltage stresses under PWM inverter operation*, 4th ed. 2016](https://www.gambica.org.uk/static/uploaded/e41820bb-886a-463b-829aaa07c6ec486c.pdf)
- **SiC-drive transmission-line study (simulation).**
  - Uses v ≈ 0.47·c for a cable with εr = 4.5.
  - The terminal voltage "can reach twice as much as that at inverter terminals with ... rise time tr ~10–20 ns and a cable length l ~2 m".
  - With a 2 m cable: "very little overvoltage is seen ... when tr = 50, 150 ns, while Vpeak = 2 p.u. occurs when tr = 10 ns".
  - "Peak voltages ~1.5–2 times higher than that at inverter terminals may easily occur" with WBG rise times of 10–20 ns, with repetition "up to megahertz".

  — [Barzkar & Ghassemi, "Precise Evaluation of Repetitive Transient Overvoltages in Motor Windings in Wide-Bandgap Drive Systems", *Vehicles* 2022, 4, 697–726, doi:10.3390/vehicles4030040](https://par.nsf.gov/servlets/purl/10383379)
- **SiC-specific numbers from a patent (calculated examples, not measurements).**
  - "a SiC MOSFET can be switched with a dv/dt of 50 V/ns to 100 V/ns".
  - With SiC, "the minimum length to have significant overvoltage reduces to approximately 1-2 meters. For example, with 20 V/ns dv/dt, 1.37 meters of cable can cause an 88% overvoltage."
  - "the dv/dt of a 100 kW SiC inverter can easily reach 17 V/ns, so the rise time will be smaller than 50 ns for 800 V input voltage. The maximum cable length ... to have a full reflection is reduced to 2.5 meters, compared to 20 meters for the 400 ns rise time case."

  — [US11114972B2, "System, method and device for reflected wave cancellation" (Google Patents full text)](https://patents.google.com/patent/US11114972B2/en)
- **Rise times and stress category.** State-of-the-art SiC MOSFETs produce "rise times of less than tr = 30 ns ... slew rates of du/dt ≈ 20 kV/µs". With long cables and mismatched impedances "overshoot factors of OF ≈ 2 can occur". "Particularly for rise times tr < 200 ns oscillation processes of parts of the winding can occur". "The stress category must be assumed to be extreme (D) for a rise time tr < 0.1 µs of a modern SiC semiconductor." — [Pauli, Ruf, Hameyer, "Low voltage winding insulation systems under the influence of high du/dt slew rate inverter voltage", *Arch. Electr. Eng.* 69(1):187–202, 2020, doi:10.24425/aee.2020.131767](http://bib.iem.rwth-aachen.de/IEMpublications/2020FPLow.pdf)
- **Older Si-era range.** IEC 60034-18-41:2014 states "modern converter output voltage rise times may be in the 0,05 µs – 2,0 µs range" — [IEC 60034-18-41:2014 preview (iTeh), as extracted in the earlier notes](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf). A 2024 review cites OF determination at a 6.5 ns rise time — [Zhou et al., *Energies* 2024, 17, 1987](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)
- **Magnitude of field surges.** Surges "can be as much as three or four times the rated, rms phase-to-ground voltage, with a risetime as short as 50 ns", and "the turns in the first coil see much higher stress than the rest of the winding" — [Stone & Lloyd, "IEC standards for variable speed drives and motor winding insulation", PCIC Middle-East 2014, paper 2014-08 (Qualitrol-Iris Power)](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
- **Above 3 p.u. (search-result extract; full text not read).** One SiC study reports terminal overvoltage above 3 p.u. caused by inverter ringing. Shortening the rise time from 50 to 30 ns raised the motor terminal voltage from 715 V to 1000 V on a 540 V DC drive — [Taghia, Cougo, Piquet, Malec, Belinger, Carayon, "Overvoltage at motor terminals in SiC-based PWM drives", *Math. Comput. Simul.* 158 (2019) 264–280, doi:10.1016/j.matcom.2018.09.009](https://www.researchgate.net/publication/327909969_Overvoltage_at_motor_terminals_in_SiC-based_PWM_drives)
- **Measured worst cases (random-wound motor, earlier notes).** The worst T/T stress was 1.47 p.u. of Vdc (2 m cable, rise time < 25 ns, first and last turns adjacent). The maximum P/G overvoltage was 1.2 p.u. (15 m cable). The reflection coefficient was limited to 1.85 by the cable/machine impedance mismatch — [Lusuardi et al., Part III, IEEE Access 2021](https://zenodo.org/records/4562202)

**Uneven (first-turn) voltage distribution**
- **General windings.**
  - The winding is a cascade of cells: turn self- and mutual inductance, resistance, turn/turn capacitance and turn/ground capacitance. "Most of the line voltage will be applied to the first few turns."
  - Lebey et al. measured accessible turns and found that "the first couple of turns" withstand most of the voltage, with ringing (about 2 MHz) "only in the first turn".
  - For random-wound motors the distribution is "inherently probabilistic", so the worst-case curve from IEC 60034-18-41 is used. For form-wound coils, "FEM software can be used to derive the exact turn voltage distribution".

  — [CIGRE WG D1.43 TB](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **Share of the incident peak.** Depending on motor rating, winding type, number of turns, coil size and turn propagation time, "the voltage appearing between turns or randomly within a coil may briefly reach between 30% and 90% of the incident peak voltage" — [GAMBICA/BEAMA 2016](https://www.gambica.org.uk/static/uploaded/e41820bb-886a-463b-829aaa07c6ec486c.pdf)
- **Where the worst turn sits (EV PMSM, multiconductor-line model).** The "voltage distribution in motor windings is non-uniform". The peak occurs "in turns closer to the motor terminals and/or turns closer to the neutral point", depending on whether the neutral is grounded or floating and on how the phases are excited. "The overvoltage in turns closer to the neutral point can be harsher than in turns closer to the motor terminals." — [Barzkar & Ghassemi 2022](https://par.nsf.gov/servlets/purl/10383379)
- **Hairpin-specific sources.**
  - Dittmann, Behrendt and Ponick present a distributed-network method for inverter-fed hairpin stators. It identifies "spots with high potential differences" so that conductors with high differential potential can be insulated individually (abstract only) — [Dittmann, Behrendt, Ponick, "Prediction of the Voltage Distribution in a Inverter-Fed Hairpin Stator Winding", ICEMS 2022, doi:10.1109/ICEMS56177.2022.9983323](https://doi.org/10.1109/ICEMS56177.2022.9983323)
  - Berardi, Nategh and Bianchi estimate voltage differences between points in a hairpin winding (and between turns in the same slot) as a function of rise time (abstract via search-result extract) — [Berardi, Nategh, Bianchi, "Inter-turn Voltage in Hairpin Winding of Traction Motors Fed by High-Switching Frequency Inverters", ICEM 2020, pp. 909–915, doi:10.1109/ICEM49940.2020.9270727](https://doi.org/10.1109/ICEM49940.2020.9270727)
  - Ju et al. calculate and measure hairpin voltage stress under SiC MOSFET drive (citation only; abstract not readable) — [Ju, Cheng, Yang, Cui, Sun, Liu, He, "Voltage Stress Calculation and Measurement for Hairpin Winding of EV Traction Machines Driven by SiC MOSFET", *IEEE Trans. Ind. Electron.* 69 (2022) 8803–8814, doi:10.1109/TIE.2021.3116577](https://doi.org/10.1109/TIE.2021.3116577); follow-up: [Ju et al., *CES Trans. Electr. Mach. Syst.* 9 (2025) 26–35, doi:10.30941/CESTEMS.2025.00005](https://doi.org/10.30941/CESTEMS.2025.00005)
  - A 2025 e&i paper treats the position of the first conductor as a winding-plan criterion. It cites placing the first conductor "in the last layer where the inductance is the smallest" (search-result extract) — [*e&i Elektrotechnik und Informationstechnik* 2025, doi:10.1007/s00502-025-01333-1](https://link.springer.com/article/10.1007/s00502-025-01333-1)
  - A hairpin patent on open-end-winding (OEW) drives states that "the maximum voltage difference 'Vdc' occurs between a first turn and a last turn of one phase" (search-result extract) — [USPTO 12695348](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12695348)

**Multilevel topologies**
- **3-level waveforms in the standards.**
  - Both 18-41 (Figure 2, five-step P/P waveform) and CIGRE (Figures 4–5) illustrate 3-level terminal waveforms and the corresponding jump voltage — [18-41 CSV contents](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf); [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
  - IEC 60034-18-41 Table 4 itself is titled "Stress categories ... based on a 2-level converter".
  - 18-42 Annex A.2 gives a "Calculation of the contributions to ageing from a 3-level converter drive". Its Table A.1 gives the "Contribution to electrical ageing by 1 kHz impulses from a 3-level converter as a percentage of the ageing from the 50 Hz fundamental voltage (endurance coefficient of 10)"; the values were not readable — [18-42 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf)

**Switching frequency and dv/dt (ageing, not PD inception)**
- "The number of surges per second ... will be equal to the carrier frequency"; lower modulating frequencies favour space-charge formation — [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **Form-wound coils.** Raising the switching frequency by about 1 kHz raised groundwall hot-spot temperature by about 10 °C on average. The service-life drop at the source's switching frequency was about 58 % at room temperature and about 31 % with cooling, a difference that "highlights the role played by dielectric heating" — [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **Enamel wire above PDIV (Pauli et al.).**
  - Lifetime falls with higher switching frequency, amplitude and slew rate, and "the variation of the frequency shows ... a more significant influence on the lifetime than the predicted linear relation".
  - At 20 kHz and 45 kV/µs the mean PDIV was 872 V. At 950 V the lifetime "decreased to 140 min".
  - The test generator's own OF was 1.04 at 22 kV/µs and 1.10 at 45 kV/µs.

  — [Pauli et al. 2020](http://bib.iem.rwth-aachen.de/IEMpublications/2020FPLow.pdf)
- **Type II life testing.** Type II qualification applies "the inverse frequency rule" to scale power-frequency life data to converter frequencies — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)

### Inferences
- **Scaling rule (calculation).** Every operating stress is proportional to Udc for a given OF and a. Relative to 800 V:
  - a 1200 V bus multiplies P/P, P/G and T/T by 1.5;
  - a 1600 V bus multiplies them by 2.0.

  2-level operating peak-to-peak stresses, P/P = 2·OF·Udc, P/G = 1.4·OF·Udc, T/T = 0.7·OF·Udc (kVpp):

  | Udc | OF 1.2 (P/P / P/G / T/T) | OF 1.5 | OF 2.0 | OF 2.5 | T/T worst, 1.47 p.u. |
  |---|---|---|---|---|---|
  | 800 V | 1.92 / 1.34 / 0.67 | 2.40 / 1.68 / 0.84 | 3.20 / 2.24 / 1.12 | 4.00 / 2.80 / 1.40 | 1.18 |
  | 1200 V | 2.88 / 2.02 / 1.01 | 3.60 / 2.52 / 1.26 | 4.80 / 3.36 / 1.68 | 6.00 / 4.20 / 2.10 | 1.76 |
  | 1600 V | 3.84 / 2.69 / 1.34 | 4.80 / 3.36 / 1.68 | 6.40 / 4.48 / 2.24 | 8.00 / 5.60 / 2.80 | 2.35 |
- **Device and rise time (calculation; dv/dt taken over 10–90 % = 0.8·Udc/tr; critical length lc = v·tr/2 with v = 150–170 m/µs).**

  | Udc | tr = 30 ns (SiC) | tr = 150 ns (Si IGBT) | Fixed 20 V/ns (dv/dt-limited SiC) |
  |---|---|---|---|
  | 800 V | 21 V/ns, lc ≈ 2.3–2.6 m | 4.3 V/ns, lc ≈ 11–13 m | tr ≈ 32 ns, lc ≈ 2.4–2.7 m |
  | 1200 V | 32 V/ns, lc ≈ 2.3–2.6 m | 6.4 V/ns, lc ≈ 11–13 m | tr ≈ 48 ns, lc ≈ 3.6–4.1 m |
  | 1600 V | 43 V/ns, lc ≈ 2.3–2.6 m | 8.5 V/ns, lc ≈ 11–13 m | tr ≈ 64 ns, lc ≈ 4.8–5.4 m |

  At a fixed device rise time, dv/dt rises in proportion to Udc. If dv/dt is capped (EMI, bearing currents), the rise time grows and the critical length gets longer. The relative OF for a given cable can then be slightly lower at 1600 V, but the absolute overshoot (OF·Udc) still grows.
- **Integrated e-axle vs cabled drive.**
  - Integrated e-axle with busbar or terminal connections well below lc (tens of cm vs about 2–5 m): OF should stay near the 1.1–1.3 band. The earlier report's 1.2–1.5 assumption is reasonable but unverified, because no measured integrated-e-axle OF was found.
  - Cabled SiC drive with a cable of about 1.4–2.5 m or longer: OF = 2.0 must be assumed, plus margin for ringing or double pulses (3–4 p.u. are possible per CIGRE, GAMBICA and Taghia).
- **Surge-impedance sensitivity (calculation, OF_max ≈ 1 + Γ).**

  | Zc | Zm | Γ | OF_max |
  |---|---|---|---|
  | 50 Ω | 100 Ω | 0.33 | 1.33 |
  | 50 Ω | 200 Ω | 0.60 | 1.60 |
  | 50 Ω | 500 Ω | 0.82 | 1.82 |
  | 50 Ω | 1000 Ω | 0.90 | 1.90 |
  | 30 Ω | 2000 Ω | 0.97 | 1.97 |

  High-power, few-turn hairpin machines plausibly have lower Zm than small random-wound motors, consistent with the qualitative trend in CIGRE Fig. 7 of surge impedance versus rating. This would lower Γ, but I found no measured Zm for hairpin traction motors.
- **T/T in hairpin windings.**
  - Hairpin conductors sit in fixed, known positions, as in form-wound coils, so T/T stress is deterministic and computable (Dittmann, Berardi, Ju). It can be controlled by the winding plan, for example by where the line-end conductor sits and whether first and last conductors of a phase are adjacent.
  - Under the 18-41 schematic T/T = 2·a·Uj with Uj ≈ OF·Udc (my 2-level assumption), the default WF_TT = 0.7 corresponds to a ≈ 0.35.
  - GAMBICA's 30–90 % range would give 2a = 0.6–1.8. Part III's measured 1.47 p.u. corresponds to OF·2a ≈ 1.47.
  - The T/T requirement should therefore be bracketed between WF·OF = 0.7·OF (default) and 1.47 (measured worst case). The extreme bound a = 0.9 gives 2·0.9·OF.
- **3-level NPC/ANPC/T-type (calculation and assumption).**
  - Each switching event is a Udc/2 step, so the per-event jump voltage and, to first order, T/T stress halve: T/T ≈ 0.35·OF·Udc.
  - Overshoot acts only on the Udc/2 step, so P/P peak-to-peak ≈ (1 + OF)·Udc instead of 2·OF·Udc: for OF = 2, 3·Udc instead of 4·Udc.
  - The 1.4·Udc·OF-type P/G envelope is reduced less.
  - Consequence: a 1600 V 3-level drive presents roughly the T/T stress of an 800 V 2-level drive (≈ 0.67–0.84 kVpp at OF 1.2–1.5), but P/G and P/P remain about 1.5–2 times those of 800 V.
- **Switching frequency.** It does not change RPDIV or the PD-free requirement directly. It sets the impulse repetition rate (ageing per hour if PD occurs; 18-42's inverse-frequency acceleration) and the dielectric heating. With SiC at 1200/1600 V and 20–40 kHz, a Type II system would age much faster than at Si-IGBT frequencies of 5–10 kHz. This strengthens the case for a PD-free (Type I) design or a 3-level topology.

### Gaps
- The text of 18-41 Clause 4–5, Figure 4 (OF vs cable length) and Figure 7 (worst-case a vs rise time) was not readable, so a numeric "a(tr)" curve cannot be quoted.
- No measured OF for an integrated 800 V SiC e-axle (busbar-connected) was found. All SiC numbers above are simulations, a patent calculation, or a 540 V study.
- Abstracts or results of the hairpin-specific papers (Ju et al. 2022/2025; Berardi et al. 2020; e&i 2025) could not be read: IEEE Xplore and Springer were not accessible and the API rate limits were exhausted. No numeric "% of Udc on the first hairpin conductor" is therefore available.
- No published data were found on hairpin-motor surge impedance (Zm) or on 3-level-inverter-fed hairpin T/T measurements at 1200/1600 V.

---

## 2. What IEC 60034-18-41 (2014 + AMD1:2019; Ed. 2 status) and IEC 60034-18-42 specify, and what 1200 V / 1600 V buses imply

### Takeaway
IEC 60034-18-41 Ed. 1.1 (CSV 2014+AMD1:2019+COR1:2020) remains the current Type I document. A third-party standards database lists the Ed. 2 project as deleted at stage 30.98 on 2026-07-08, so no new edition is imminent.
- **Type I.** Requires PD-free operation, qualified by ageing sub-cycles followed by PD tests. Uses stress categories A–D (OF ≤ 1.1/1.5/2.0/2.5) and a total enhancement factor generally 1.25, multiplied by temperature and ageing factors in common practice. AMD1 adds IVIC classes, routine-test factors (TVF), and optional humidity and altitude factors without values.
- **The 700 V boundary.** It is descriptive ("generally ... 700 V r.m.s. or less"), not a scope limit.
- **1200 V and 1600 V buses.** These give fundamental line voltages of about 850 and 1130 V r.m.s. with SVPWM (calculation), above that boundary. A Type I claim is still possible but needs very high RPDIV (§5). Otherwise the machine falls under IEC 60034-18-42 Type II: PD-resistant, mica or inorganic-filled systems qualified by destructive life-curve testing of mainwall, turn and stress-control insulation.

### Cited Findings
- **Status of IEC 60034-18-41.** Ed. 1.1 combines Ed. 1 (2014-03; documents 2/1728/FDIS, 2/1738/RVD), AMD1 (2019-06; 2/1949/FDIS, 2/1957/RVD) and the 2020-12 corrigendum — [18-41 CSV preview](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf). The IEC webstore lists it with stability date 2029 (earlier notes) — [IEC webstore 32755](https://webstore.iec.ch/en/publication/32755)
- **Ed. 2 project.** The "IEC 60034-18-41 ED2" project (TC 2, same title) is shown at stage "30.98 Project deleted", dated 2026-07-08, under the "ABANDON" life-cycle heading. The listed previous publications are the 2014 edition, AMD1:2019 and COR1:2020 — [Genorma project page (third-party aggregator of IEC project data)](https://genorma.com/en/standards/iec-60034-18-41-ed2). This supersedes the earlier notes' unverified "PCC stage, forecast 2026-05-04" claim. No draft content was found.
- **Scope.** Applies to stator/rotor windings under voltage-source PWM drives. Excludes machines "only started by converters", machines "with rated voltage ≤ 300 V r.m.s." and rotor windings "operating at ≤ 200 V (peak)". No upper voltage limit appears in the scope — [18-41 CSV preview](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf)
- **Type I / Type II boundary wording.**
  - 18-41: Type I systems "are generally used in rotating machines rated at 700 V r.m.s. or less and tend to have random wound windings". Type II systems "tend to have form-wound coils, mostly rated above 700 V r.m.s." and their qualification "involves destructive ageing" — [18-41 CSV preview](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf)
  - 18-42: Type I systems are "generally used in rotating machines with rated voltage less than 700 V r.m.s.". For Type II, "the severity is additionally affected by the impulse voltage repetition rate and the fundamental voltage characteristics" — [18-42 Ed. 1.1 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf)
  - Stone & Lloyd describe random-wound stators as usually applying to motors "rated <1,000 V (Type I machines)" and form-wound machines as ">690 V" — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
- **Stress categories (Table 4, reproduced by third parties; standard text not readable).**
  - Pauli et al. give:

    | Category | OF band | Rise time tr |
    |---|---|---|
    | A benign | OF ≤ 1.1 | 1 µs < tr |
    | B moderate | 1.1 < OF ≤ 1.5 | 0.3 ≤ tr < 1 µs |
    | C severe | 1.5 < OF ≤ 2.0 | 0.1 ≤ tr < 0.3 µs |
    | D extreme | 2.0 < OF ≤ 2.5 | 0.05 ≤ tr < 0.1 µs |

    They also state that SiC (tr < 0.1 µs) must be treated as category D — [Pauli et al. 2020](http://bib.iem.rwth-aachen.de/IEMpublications/2020FPLow.pdf)
  - The CIGRE TB reproduces the same OF bands but a single rise-time entry "0,2 ± 0,1" µs. It notes the qualified category was to be marked on the plate as "IRV C" (Impulse Rated Voltage, an older TS-era label) — [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
  - **Conflict:** rise-time columns differ between the reproductions. The 2014 IS text gives a default of 0.3 µs.
- **Enhancement factors.**
  - AMD1 B.5: the P/P and P/G PD-test voltages for a 500 V machine are computed "without the additional factor of 1,1 (arising from line voltage variations) and multiplied by the relevant total enhancement factor shown in Table B.2 ... It is generally expected that the total enhancement factor will be 1,25."
  - AMD1 B.3: humidity and air density "may affect the PD inception voltage" and can shift it "in both directions", so "a further enhancement factor could be applied". Altitude "should be reflected by an additional enhancement factor".

  — [AMD1:2019](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
  - Common practice splits the total into EF_PD = 1.25, EF_T = 1.3 (T/T, P/P) or 1.1 (P/G), and EF_Aging = max(1; 1.2·Ts/Tc) for verification or 1 for qualification on aged specimens — [Lusuardi et al., Part III](https://zenodo.org/records/4562202)
  - The TS-era description required RPDIV after each ageing cycle to stay above the category levels "plus a 30% safety factor" — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
- **Published example levels (2-level converter).**
  - Stone & Lloyd Table 1, 480 V motor, RPDIV (Vpp), P/P / P/G / T/T:

    | Category | OF | P/P | P/G | T/T |
    |---|---|---|---|---|
    | Benign | 1.1 | 1853 | 1297 | 1297 |
    | Moderate | 1.5 | 2527 | 1769 | 1769 |
    | Severe | 2.0 | 3370 | 2359 | 2359 |
    | Extreme | 2.5 | 4212 | 2948 | 2948 |

    Table 2 gives a 460 V example measured zero-to-peak with a surge generator: P/P 1771–4027 V; P/G or T/T 1240–2818 V — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
  - AMD1 Table B.5, 500 V, EF 1.25: P/P 1857/2532/3375/4219 V and P/G 1300/1773/2364/2955 V for A–D (earlier notes).
  - **Note:** in the TS-era table T/T equals P/G (random-wound worst case). The Lusuardi defaults give T/T = 0.5 × P/G.
- **Qualification and type tests.**
  - Test objects go through IEC 60034-18-21 or 60034-18-31 sequences "with the addition of a high frequency voltage test and a partial discharge test", using impulse equipment per IEC/TS 61934 if needed. A system that is PD-free at the end is "qualified for the severity band that has been selected".
  - Type and optional routine tests on complete windings follow, and an IVIC is "assigned to the machine".

  — [18-41 CSV preview](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf)
  - Contents include 10.2.2 twisted pair, 10.2.3 motorette/formette, 10.2.4 complete windings, 10.3.2 "Turn/turn insulation samples", Table 5 "Allowable voltage waveforms for testing system components", and Table B.6 "Turn/turn PD test levels for special windings and twisted pairs" (values not readable) — [18-41 CSV sample](https://www.normsplash.com/Samples/IEC/165459798/IEC-60034-18-41-2014-AMD1-2019-CSV-en-fr-2.pdf)
- **IVIC and routine tests (AMD1).**
  - 3.19 IVIC = "peak to peak voltage classes A, B, C, D, S for reliable operation, assigned by the manufacturer". 3.26 U_IVIC = "maximum allowable peak to peak phase to ground voltage in service". 3.27 TVF = that P/G value in units of U_N "divided by 2√2".
  - 12.1: a PD routine test is "good practice".
  - 12.2: the mandatory withstand test of IEC 60034-1 "may be required at an increased voltage level for converter-fed machines, according to the specified IVIC". For machines ≤ 200 kW with U_N ≤ 1 kV, "the 1 min test may be replaced by a test of 1 s ... at 120 %". For < 1 kW with IVIC C/D, 100 % may be used.
  - Table C.1 limits are derived "using Formulae (1) and (2) together with the arbitrarily chosen stress category overshoot factors in Table 4"; intermediate steps and independent P/P and P/G limits may be needed (C.2).

  — [AMD1:2019](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- **Table D.1.**

  | IVIC | Enhancement ratio | TVF | Routine P/G test, U_N = 500 V |
  |---|---|---|---|
  | Line-fed | — | — | 2 kV r.m.s. |
  | A | 1.3 | 0.7 | 2.0 kV r.m.s. |
  | B | 1.7 | 1.0 | 2.0 kV r.m.s. |
  | C | 2.3 | 1.3 | 2.3 kV r.m.s. |
  | D | 2.9 | 1.7 | 2.7 kV r.m.s. |

  For IVIC S, X and Y are "chosen by the manufacturer" and the "equations in the line of IVIC 'S' apply to the other IVICs". The converter-fed routine test value may not be below the line-fed value — [normsplash sample, Annex D (FR)](https://www.normsplash.com/Samples/IEC/165459798/IEC-60034-18-41-2014-AMD1-2019-CSV-en-fr-2.pdf)
- **IEC 60034-18-42 (Type II).**
  - Current version: Ed. 1.1, 2020-08 (2017+AMD1:2020). It qualifies, by electrical endurance, the mainwall (life curve per IEC 60034-18-32; clause 9.3 "Use of 50 Hz or 60 Hz life data to predict the service life with a converter drive"), the turn insulation (clause 10) and the stress-control system (clause 11).
  - It includes an IVIC for Type II (Annex D, Table D.1 "IVIC- and test voltage factor definition"). Annex E derives an IVIC without a reference life line, including IVIC X/S "on the basis of satisfactory service experience".
  - It contains measured terminal-voltage characteristics for two converter-fed machines (Table 1), 3-level ageing contributions (Annex A), and impulse test circuits using semiconductor switches (Annex B).

  — [18-42 Ed. 1.1 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf)
- **Type II test approach (from the TS era).** Mainwall tests need only 50/60 Hz voltage. Turn and grading insulation need impulse ageing. Stress grading must survive a minimum life "at room temperature and at their thermal class limit minus 30°C". The acceptance (voltage endurance) test used 50/60 Hz at "2.5 times the rated peak-to-peak voltage", and any single early failure fails the set — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
- **Type II turn insulation (CIGRE).** It "is generally the weakest point". If the maximum turn voltage is unknown, "it should be assumed that the complete jump voltage may fall across the first coil". The basic test voltage is applied at 50/60 Hz for 60 s between two conductors. If PD incepts, an impulse (or higher-amplitude sinusoidal) voltage-endurance test follows, with frequency acceleration and inverse-power-law extrapolation — [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **What Type II insulation looks like.**
  - Inorganic filler and micaceous materials (VPI or resin-rich). Machines above 3 kV add semiconductive slot coatings and end-winding stress grading — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
  - "For stators operating above 700 volts, there may be slot corona protection present" — [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **Corona-resistant enamel does not raise PDIV.** In bipolar 20 kHz, 45 kV/µs tests, a PD-resistant enamel (PAI topcoat with inorganic nano/micro-fillers; Cr₂O₃ named) had a lower PDIV (mean 787 V) than standard enamel (975 V). The paper's grade label for this wire is inconsistent: grade 2 in Table 4, grade 3 in the Fig. 12 caption. Its lifetime advantage existed "only below a frequency threshold" — [Pauli et al. 2020](http://bib.iem.rwth-aachen.de/IEMpublications/2020FPLow.pdf)

### Inferences
- **Line voltages of the three buses (calculation, fundamental line-to-line r.m.s.).**

  | Udc | SPWM, m = 1 (0.612·Udc) | SVPWM linear limit (Udc/√2) | Six-step (0.78·Udc) | "Equivalent U_N" = Udc/1.35 |
  |---|---|---|---|---|
  | 800 V | 490 V | 566 V | 624 V | 593 V |
  | 1200 V | 735 V | 849 V | 936 V | 889 V |
  | 1600 V | 980 V | 1131 V | 1248 V | 1185 V |

  1200 V and 1600 V buses exceed the 700 V r.m.s. descriptor under any modulation. 800 V stays below it, consistent with the earlier report.
- **Type I remains admissible above 700 V r.m.s.** The 18-41 scope has no upper limit, and "Type I/II" is defined by whether PD is expected, not by voltage. A 1200 V or 1600 V hairpin machine can therefore be qualified Type I if every insulation path is shown PD-free at the §5 targets after ageing.
  - At 1600 V (2-level, OF 1.2–1.5) these targets are about 2.6–3.3 kVpp T/T, 4.4–5.5 kVpp P/G and 7.5–9.4 kVpp P/P.
  - If this cannot be shown, the system is Type II. It must then pass 18-42 life-curve qualification, i.e. PD-resistant (mica or inorganic-filled) materials, a different and destructive test programme.
- **Practical consequence for the oil-ageing study.** At 1600 V, the PD-free margin (RPDIV ÷ target) after oil ageing is the deciding metric. Corona-resistant enamels should be judged by endurance under PD, not by PDIV, because they do not raise PDIV.
- **Category D for SiC.** With SiC (tr < 0.1 µs), Pauli et al.'s reading puts any SiC drive in category D, whose OF upper bound is 2.5, unless the integrator measures and declares a lower OF. AMD1 C.2 / IVIC S allows the manufacturer to set independent P/P (X) and P/G (Y) limits matched to the measured terminal voltages, which suits a characterised integrated e-axle.

### Gaps
- The verbatim Table 4, Table B.2 (all enhancement factors), Table B.6 (twisted-pair T/T test levels) and Figure 7 (a vs tr) of 18-41 were not readable. The Table 4 rise-time columns conflict between reproductions.
- Ed. 2 deletion is reported only by a third-party aggregator (Genorma), not confirmed on the IEC project page. Whether a new project (e.g., a merged 18-41/18-42 or a TS on WBG drives) replaced it is unknown.
- No numerical values were obtained for 18-42 Table 1 (measured terminal voltages), Table A.1 (3-level ageing contributions) or Table D.1 (Type II IVIC/TVF).

---

## 3. Other documents that set insulation requirements or test levels for high-voltage traction drives (IEC TS 60034-25, IEC 61800-5-1, IEC 60664-1, IEC 60034-1, ISO 6469-3, ISO 21498, LV 123/124, GB/T 18488, SAE, IEC 60349), including hipot and insulation-resistance levels

### Takeaway
Most generic LV insulation-coordination standards stop at 1500 V DC: IEC 60664-1 (≤ AC 1000 V / DC 1500 V, ≤ 30 kHz) and IEC 61800-5-1 (LV PDS ≤ 1.5 kV DC). IEC 61800-5-1 also explicitly excludes traction and EV drive modules. A 1600 V bus is therefore outside "low voltage" in the IEC sense.
- **Motor hipot.** Comes from IEC 60034-1:2022 (Table 17, with new Table 18 IVIC test-voltage factors). Under IEC 60034-18-41 AMD1 Annex D, routine test ≈ 1 kV + 2·TVF·U_N, never below the line-fed 1 kV + 2·U_N value: 2 kV r.m.s. at U_N = 500 V.
- **Rail.** IEC 60349-2:2010 covers converter-fed AC traction motors for rail and road vehicles, but its dielectric levels were not readable.
- **Vehicle standards.** ISO 6469-3, ISO 21498-1/-2, GB/T 18488-2024 and SAE J3271 were identified but their numerical withstand and insulation-resistance clauses could not be read. LV 123/124 are not public.

### Cited Findings
- **IEC TS 60034-25 / 60034-17 (limit curves).**
  - GAMBICA (2016) lists IEC TS 60034-17 "currently edition 4 (2006)" (standard cage motors on converters) and IEC TS 60034-25 "currently edition 3 (2014)" (motors specially designed for converter supply).
  - It gives peak-voltage vs rise-time limit curves: Curve A for ≤ 500 V a.c. supplies (corresponding to IEC 60034-25), Curve B for > 500–690 V. Both exceed the IEC 60034-17 minimum capability.
  - It quotes NEMA's requirement "Vpeak = 3.1 * Vrated for NEMA rise times ≥ 0.1 µs and Vrated ≤ 600 V a.c.".

  — [GAMBICA/BEAMA 2016](https://www.gambica.org.uk/static/uploaded/e41820bb-886a-463b-829aaa07c6ec486c.pdf)
  - IEC 60034-18-41 normatively references "IEC/TS 60034-25:2007" and "IEC/TS 61800-8, ... Specification of voltage on the power interface" — [18-41 CSV preview](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf)
- **NEMA MG-1 Part 31 and IEEE 522.** Part 31 requires LV (< 600 V) inverter-duty windings to survive an impulse of "3.1 times the rated phase-to-phase voltage" and MV (> 600 V) motors "2.04 times". Form-wound coils per IEEE 522 are tested with an impulse crest of "3.5 times the peak line-to-ground voltage" — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
- **IEC 61800-5-1:2022 (Ed. 3.0, 2022-08).**
  - Scope: PDS "which include ... a motor or motors. Excluded are traction and electric vehicle BDM/CDM." It covers low-voltage PDS "up to and including 1,0 kV AC ... and up to and including 1,5 kV DC" and high-voltage PDS up to 35 kV AC / 52 kV DC.
  - Note 1: "the technical upper voltage limit for DC motors is 2,25 kV DC". "Motors for driven equipment ... are covered by IEC 60034".
  - Insulation coordination follows IEC 60664, with new 4.4.7.1.2 "Working voltage" and 4.4.7.8 "Solid insulation".
  - Contains Tables 6/7 "Impulse withstand voltage and temporary overvoltage versus system voltage" and Tables 31–33 "AC or DC test voltage" (values not readable).

  — [IEC 61800-5-1 Ed. 3.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec61800-5-1%7Bed3.0%7Db.pdf)
- **IEC 60664-1:2020 (Ed. 3.0, 2020-05).** Applies to equipment with "rated voltage up to AC 1 000 V or DC 1 500 V connected to low-voltage supply systems" and "to frequencies up to 30 kHz"; above 30 kHz, IEC 60664-4 applies. Change list: "addition of 1 500 V DC into tables in Annex B and F" — [IEC 60664-1 Ed. 3.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60664-1%7Bed3.0%7Db.pdf)
- **IEC 60034-1:2022 (Ed. 14.0, 2022-02).**
  - Contains Table 17 "Withstand voltage tests" and new Table 18 "Test voltage factors for machines with an assigned Impulse Voltage Insulation Class (IVIC) according to IEC 60034-18-41 and IEC 60034-18-42".
  - Changes: 9.2 "Test voltage for variable speed AC machines added", 9.13 new "measurement of insulation resistance and polarization index", 6.2 reduced arcing distance at altitudes > 1 000 m, and new definitions of "converter capable" and "converter duty" machine. Table values were not readable.

  — [IEC 60034-1 Ed. 14 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-1%7Bed14.0%7Db.pdf)
  - Footnote b of 18-41 Table D.1 states that the line-fed column (2 kV for U_N = 500 V) "is the test voltage specified in IEC 60034-1 for U_N = 500 V" — [AMD1:2019](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- **IEC 60349-2:2010 (Ed. 3.0, 2010-10, TC 9).** "applies to converter-fed alternating current motors forming part of the equipment of electrically propelled rail and road vehicles". It is "not intended" for "small road vehicles, such as battery-fed delivery vehicles, factory trucks". It stresses designer collaboration between motor and converter (5.1). Its dielectric-test clause was not in the preview — [IEC 60349-2 Ed. 3.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60349-2%7Bed3.0%7Db.pdf)
- **ISO 21498-1:2021** (published 2021-01-27). "Voltage sub-classes and characteristics": it specifies voltage sub-classes for DC circuits of voltage class B and design-relevant characteristics, and excludes electrical safety, which is left to ISO 17409 and ISO 6469 (scope via catalogue; sub-class table not readable) — [ISO 78209](https://www.iso.org/standard/78209.html); [SCC listing](https://scc-ccn.ca/standardsdb/standards/8175454)
- **ISO 6469-3 (search-result extracts; standard text not read).**
  - The 2018 edition introduced "new voltage classes B1 and B2" — [iTeh catalogue, ISO 6469-3:2018](https://standards.iteh.ai/catalog/standards/iso/2fc6b495-6e8e-439b-b9fc-ddd0c6c22ce9/iso-6469-3-2018)
  - Amendment 1:2020 is titled "Withstand voltage test for electric power sources" — [ANSI webstore, DS/ISO 6469-3:2018/Amd 1:2020](https://webstore.ansi.org/standards/ds/dsiso64692018amd2020)
  - **Conflict on the 100 Ω/V figure:** a secondary page says ISO 6469-3 requires "a minimum of 100 Ω/V" for DC systems — [batterydesign.net](https://www.batterydesign.net/legislation-rules-and-regulations/iso-6469-3/), page empty when fetched. Another attributes ≥ 100 Ω/V for DC to UN ECE R100 — [insulationtesting.com](https://insulationtesting.com/insulation-testing-ev-batteries/)
- **GB/T 18488-2024 (*Drive motor system for electric vehicles*).**
  - Issued 2024-05-28 and replaces GB/T 18488.1-2015 and GB/T 18488.2-2015. The listing shows implementation also on 2024-05-28, which was not cross-checked.
  - The nameplate must state the working voltage range and insulation level.
  - Systems "whose DC bus voltage is Class B voltage" must carry HV warnings.
  - The test clauses (6.3/6.4) were not visible.

  — [chinesestandard.net listing (partial English text)](https://www.chinesestandard.net/PDF.amp.aspx/GBT18488-2024)
- **SAE.** SAE J3271 (Megawatt Charging System) was issued March 2025 as a Technical Information Report (search-result extract) — [SAE Mobilus listing](https://saemobilus.sae.org/standards/j3271_202503-sae-megawatt-charging-system-electric-vehicles). No SAE document setting traction-motor winding insulation or PD levels was found.
- **Industry practice (weak, secondary sources; search-result extracts).**
  - AC hipot is often quoted as "(2 × rated voltage) + 1000V" (attributed to NEMA MG-1/IEEE). IEEE 43 recommends 500 V DC insulation-resistance testing for windings rated up to 1000 V — [industrialmonitordirect.com](https://industrialmonitordirect.com/blogs/knowledgebase/hipot-vs-baker-surge-test-motor-winding-voltage-testing)
  - A hairpin end-of-line plan comprises resistance/balance, insulation resistance, AC or DC withstand and surge comparison. Voltages "must be defined by the motor design and applicable standards" — [NIDE hairpin QC guide](https://www.nidegroup.com/newsInfo/hairpin-stator-manufacturing-quality-control.html)

### Inferences
- **Routine withstand (hipot) levels (calculation; my mapping U_N,eq = Udc/1.35, from 18-41's Udc = 1.35·U_N; 1-min, 50/60 Hz, r.m.s.).** Formula: U_test = max(1000 + 2·U_N,eq; 1000 + 2·TVF·U_N,eq), with TVF = Y/(2√2) from Table D.1. This formula reproduces the Table D.1 values (A 1.74 → 2.0 floor; B 1.99; C 2.34; D 2.66 kV at U_N = 500 V).

  | Udc | U_N,eq | Line-fed (1 kV + 2U_N) | IVIC A / B | IVIC C | IVIC D | U_IVIC P/G allowed, A / B / C / D (Vpp) |
  |---|---|---|---|---|---|---|
  | 800 V | 593 V | 2.19 kV | 2.19 kV | 2.59 kV | 2.97 kV | 1244 / 1659 / 2252 / 2785 |
  | 1200 V | 889 V | 2.78 kV | 2.78 kV | 3.39 kV | 3.95 kV | 1867 / 2489 / 3378 / 4178 |
  | 1600 V | 1185 V | 3.37 kV | 3.37 kV | 4.19 kV | 4.94 kV | 2489 / 3319 / 4504 / 5570 |

  A more conservative convention, 2·U + 1000 with U = the maximum DC working voltage (1.125·Udc), gives 2.8 / 3.7 / 4.6 kV r.m.s. This is an assumption; no automotive source was verified.
- **The 1 s shortcut does not apply at 1600 V.** At 1600 V, U_N,eq ≈ 1185 V exceeds 1 kV, so the AMD1 "1 s at 120 %" routine-test shortcut (≤ 200 kW, U_N ≤ 1 kV) no longer applies.
- **1600 V crosses the IEC "low voltage" boundary.** It exceeds the 1500 V DC limit of IEC 60664-1 and of IEC 61800-5-1's LV PDS category. Creepage/clearance and solid-insulation coordination for a 1600 V bus must therefore be taken from HV-equipment rules (IEC 61800-5-1 HV clauses, IEC 60204-11 as referenced there) or from rail practice (IEC 60349-2 / IEC 62497-1, not read).
- **Switching frequency vs IEC 60664-1's 30 kHz limit.** SiC switching at > 30 kHz moves the coordination basis to IEC 60664-4.
- **Plausible EV class B boundary.** If ISO 6469-3's voltage class B ends at 1500 V DC (widely cited, but not verified here), a 1600 V nominal bus would fall outside the ISO 6469 voltage classes. 1200 V would remain within class B.

### Gaps
- The numerical content of IEC 60034-1 Tables 17/18, IEC 61800-5-1 Tables 6/7/31–33, IEC 60349-2 dielectric tests, and IEC 62497-1 (rail insulation coordination) was not readable.
- ISO 6469-3 (current edition, class B limits, withstand-test formula and duration, Ω/V limits), ISO 21498-1 (voltage sub-class table, e.g. Umax of the "800 V" sub-class) and ISO 21498-2 test levels were not readable.
- GB/T 18488-2024 insulation-resistance, withstand and inter-turn impulse requirements were not readable.
- LV 123 / LV 124 are OEM documents, not publicly available. No verified content was obtained.
- Whether IEC TS 60034-25 has an edition newer than 2014 was not verified.
- No OEM-published hipot, surge or insulation-resistance limits for 800 V-class (or higher) traction motors were found.

---

## 4. Which applications use 800, 1200 and 1600 V buses (announced or in service), and their maximum bus voltages

### Takeaway
- **Passenger cars.** Already ship at "800 V class", and BYD's 2025 platform is a "full-domain 1000V" architecture with SiC chips rated up to 1500 V.
- **Heavy-duty charging.** The Megawatt Charging System is specified to about 1250 V DC (one source says 1500 V).
- **Rail and mining.** Rail DC-catenary traction is the established 1500–1950 V case: the 1500 V DC system runs 1000–1800 V permanently and 1950 V temporarily. Mining haul trucks are reported at 1800–2100 V DC.
- **Power devices.** 2300 V SiC modules are marketed for 1500 V DC buses.
- **Mapping to the study.** 800 V maps to current EVs (maximum ≈ 900–1000 V), 1200 V to MCS-class trucks/buses and next-generation cars, and 1600 V to rail/mining/industrial 1500 V-class drives. I found no verified product using exactly a 1200 V or 1600 V nominal traction bus in road vehicles.

### Cited Findings
- **BYD Super e-Platform.** Launched "On March 17, 2025", with a "full-domain 1000V high-voltage architecture" and SiC power chips rated "up to 1500V". It has the "world's first mass-produced 30,000 RPM motor" and a "single-module single-motor power of 580 kW". Charging current "reaches 1000A" (10C) and charging power is "1 megawatt (1000 kW)". First models: Han L and Tang L — [BYD press release](https://www.byd.com/en/news-list/BYD-Unveils-Super-e-Platform-Megawatt-Flash-Charging-Electric-Vehicles-Matching-Refueling-Speeds.html)
- **Megawatt Charging System (trucks and buses).**
  - SAE J3271 (MCS) was issued 2025-03 as a TIR — [SAE Mobilus](https://saemobilus.sae.org/standards/j3271_202503-sae-megawatt-charging-system-electric-vehicles)
  - **Conflict on the voltage ceiling (search-result extracts):** an Argonne FAQ describes MCS chargers from "440kW (350A/1250vdc non-cooled) up to 3.75MW (3000A/1250vdc actively cooled)" — [ANL MCS FAQ, 2023-03](https://sandbox4-www.anl.gov/sites/www/files/2023-03/MCS_FAQs_Final_3-13-23.pdf). A trade article cites "up to 1500 V/3000 A or 4.5 MW" — [eMobility Engineering](https://www.emobility-engineering.com/?p=16184).
- **Rail supply voltages (EN 50163 / IEC 60850:2007 values, as tabulated on Wikipedia).**

  | System | Min (temp./perm.) | Nominal | Max permanent | Max temporary |
  |---|---|---|---|---|
  | 600 V DC | 400 V | 600 V | 720 V | 800 V |
  | 750 V DC | 500 V | 750 V | 900 V | 1000 V |
  | 1500 V DC | 1000 V | 1500 V | 1800 V | 1950 V |
  | 3 kV DC | 2 kV | 3 kV | 3.6 kV | 3.9 kV |

  — [Wikipedia, "Railway electrification" (cites EN 50163:2007 and IEC 60850 3rd ed. 2007)](https://en.wikipedia.org/wiki/Railway_electrification). IEC 60850 Ed. 4.0 (2014-11) is current and "Table 1 modified" (values not in preview) — [IEC 60850 Ed. 4.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60850%7Bed4.0%7Db.pdf)
- **Rail/road traction motors.** Covered by IEC 60349-2 (converter-fed AC motors) — [IEC 60349-2 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60349-2%7Bed3.0%7Db.pdf)
- **Mining haul trucks (search-result extract; patent not opened).** A US patent on haul-truck drives gives a nominal DC-bus voltage of "about 1800-2100 VDC" — [USPTO 8847524](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8847524)
- **1500 V-class SiC (vendor; search-result extracts).** Wolfspeed markets 2300 V baseplate-less SiC modules for "1500V DC-bus applications" (renewables, energy storage, fast charging), with a 1500 V DC-bus three-phase inverter reference design (CRD1000DA23N-LM4) — [Wolfspeed article](https://www.wolfspeed.com/knowledge-center/article/maximizing-performance-of-1500-v-dc-bus-applications-with-the-2300-v-sic-modules/); [Wolfspeed reference design](https://www.wolfspeed.com/products/power/reference-designs/crd1000da23n-lm4/)
- **Industrial drives.** Low-voltage PDS go up to 1.5 kV DC; DC motors to a "technical upper voltage limit" of 2.25 kV DC — [IEC 61800-5-1:2022 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec61800-5-1%7Bed3.0%7Db.pdf)
- **E-aviation (search-result extracts; mostly qualitative).**
  - Reviews stress PD at reduced pressure and fast rise times. One architecture paper cites "a 2 kVac bus as close to the optimal voltage" for MEA/AEA — [Jiang et al., "A review on insulation challenges towards electrification of aircraft", *High Voltage* 2023, doi:10.1049/hve2.12304](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/hve2.12304); [MDPI *Eng. Proc.* 133(1):83](https://www.mdpi.com/2673-4591/133/1/83)
  - A vendor states air-gap breakdown voltage "may be roughly 40% lower" at 10,000 ft — [Ofil Systems](https://ofilsystems.com/higher-voltage-higher-stakes-the-emerging-partial-discharge-challenge-in-ev-and-electric-aircraft-motors/)
  - PDIV vs pressure has its minimum at 50–70 mbar (earlier notes) — [Elorza Azpiazu et al., *Appl. Sci.* 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)

### Inferences
- **Nominal vs maximum DC voltage for the test plan (assumptions).**

  | Bus | Maximum assumed | Basis |
  |---|---|---|
  | 800 V | 900–1000 V | Earlier report used 900 V; BYD's "1000 V" class shows the upper end |
  | 1200 V | ≈ 1250–1350 V | MCS's 1250 V and the 1.125 ratio used for 800 V |
  | 1600 V | ≈ 1800 V permanent, 1950 V transient | By analogy with the 1500 V DC rail class (Umax1/Umax2) |
- **What each voltage represents.**
  - 1200 V is a plausible next step for heavy-duty road vehicles (MCS-compatible) and is within reach of 1700 V-rated SiC.
  - 1600 V is effectively the "1500 V-class" bus used by rail (DC link up to 1.8–1.95 kV), mining and industrial/renewable converters, served by 2300 V SiC or 3-level topologies.
- **Altitude.** For e-aviation (and high-altitude road use), the AMD1 altitude enhancement factor would add to the §5 targets. No numeric factor is standardized.

### Gaps
- No verified announcement of a road-vehicle traction drive with a nominal 1200 V or 1600 V bus was found.
- No verified Umax values for 800 V-class packs (ISO 21498-1 sub-class table not read).
- No data on bus voltages for e-buses, off-highway machinery (other than the mining patent), marine DC grids, or e-aviation propulsion products were verified.
- The MCS voltage ceiling conflicts (1250 vs 1500 V). The SAE J3271 text was not read.

---

## 5. PD-free (RPDIV) targets for 800, 1200 and 1600 V from the IEC 60034-18-41 method, per insulation path (calculation)

### Takeaway
*(Calculation.)* With the same assumptions as the earlier 800 V calculation (2-level, OF 1.2–1.5, EF_PD 1.25, EF_T 1.3/1.1, EF_Aging 1.2), the PD-free verification targets are:

| Udc | T/T (default) | T/T (worst case) | P/G | P/P |
|---|---|---|---|---|
| 800 V | 1.31–1.64 kVpp | 2.29 kVpp | 2.22–2.77 kVpp | 3.74–4.68 kVpp |
| 1200 V | 1.97–2.46 kVpp | 3.44 kVpp | 3.33–4.16 kVpp | 5.62–7.02 kVpp |
| 1600 V | 2.62–3.28 kVpp | 4.59 kVpp | 4.44–5.54 kVpp | 7.49–9.36 kVpp |

A cabled SiC drive (OF 2.0) adds a further one-third, and the maximum-voltage case (×1.125) another 12.5 %. A 3-level inverter roughly halves the T/T target: 1600 V 3-level T/T ≈ 1.31–1.64 kVpp, the same as 800 V 2-level. As wire-pair AC-r.m.s. equivalents (÷ 2√2), the 1600 V T/T default target is about 0.93–1.16 kV r.m.s. at the operating temperature, if EF_T is retained.

### Cited Findings
- **Equation and factors.** Vc = Vdc·OF·WF·EF_PD·EF_T·EF_Aging, with WF = 2 / 1.4 / 0.7 (P/P, P/G, T/T); EF_PD = 1.25; EF_T = 1.3 (T/T, P/P) and 1.1 (P/G); EF_Aging = max(1; 1.2·Ts/Tc) in verification tests and 1 in qualification tests on aged specimens. OF = terminal peak ÷ DC-bus voltage — [Lusuardi et al., Part III, IEEE Access 2021](https://zenodo.org/records/4562202)
- **Measured worst-case T/T.** 1.47 p.u. of Vdc (adjacent first/last turns, 2 m cable, tr < 25 ns) — [Part III](https://zenodo.org/records/4562202)
- **Standard's own total EF.** "generally expected" to be 1.25. Humidity and altitude factors may be added — [AMD1:2019](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- **OF bands of the stress categories:** ≤ 1.1 / 1.5 / 2.0 / 2.5 — [Pauli et al. 2020](http://bib.iem.rwth-aachen.de/IEMpublications/2020FPLow.pdf); [CIGRE WG D1.43](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf)
- **Waveforms on twisted pairs.** AC PDIV testing on twisted pairs is acceptable because the potential difference between points is the same under AC or impulse. For sinusoidal tests PDIV is quoted r.m.s., for impulses peak-to-peak — [Part III](https://zenodo.org/records/4562202); [18-41 CSV preview, 3.2 Note 1](https://cdn.standards.iteh.ai/samples/18905/60c1ca4c89844c41a1b0b3ecfb9a2650/IEC-60034-18-41-2014.pdf)
- **Waveform strongly affects the measured value (grade-2 round wire).**

  | Waveform | Mean value |
  |---|---|
  | 50 Hz sinusoidal PDIV | 1192 V (standard), 1147 V (PD-resistant) |
  | Unipolar surge RPDIV | 2132 V / 2318 V |
  | Bipolar 20 kHz, 45 kV/µs PDIV | 975 V / 787 V |

  The standard sinusoidal and unipolar surge tests were judged "not a suitable means to identify the PDIV for inverter operated electrical machines" — [Pauli et al. 2020](http://bib.iem.rwth-aachen.de/IEMpublications/2020FPLow.pdf)
- **Unipolar surge testers.** Surge-generator values are "measured from zero to peak" — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf)
- **Temperature.** An 80 K temperature rise "may reduce the PD inception voltage by approximately 10%" — [GAMBICA/BEAMA 2016](https://www.gambica.org.uk/static/uploaded/e41820bb-886a-463b-829aaa07c6ec486c.pdf)
- **Reference PDIVs of rectangular wires (earlier notes, patent data).**
  - Essex PEEK-topcoat builds averaged 1.5–2.7 kV PDIV (conditions not stated) — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
  - Furukawa's acceptance criterion is ≥ 1 kVp at 25 °C — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)

### Inferences
**Assumptions (all stated; change any one and the results scale linearly):**
1. Topology: 2-level unless marked 3-level. The 3-level model: T/T WF halves (step Udc/2); P/P peak-to-peak = (1 + OF)·Udc; P/G = 0.7·(1 + OF)·Udc.
2. Udc nominal = 800 / 1200 / 1600 V. Maximum = 1.125 × nominal = 900 / 1350 / 1800 V.
3. OF cases:
   - 1.2 and 1.5: integrated e-axle or short connection, carried over from the earlier report;
   - 2.0: cabled SiC with full reflection, category C bound;
   - 2.5: category D bound.
4. WF = 2.0 (P/P), 1.4 (P/G), 0.7 (T/T default). T/T worst case uses the measured product OF·WF = 1.47.
5. EF_PD = 1.25; EF_T = 1.3 (T/T, P/P) and 1.1 (P/G). EF_Aging = 1.2 (verification on new specimens, Ts = Tc) or 1.0 (qualification on oil-aged specimens). Humidity and altitude EF = 1.
6. Targets are peak-to-peak RPDIV (bipolar). For unipolar surge testers apply them as 0-to-peak. For AC wire-pair tests divide by 2√2 to get r.m.s.

**Table 5.1 — Verification targets (EF_Aging = 1.2), kVpp, calculation**

| Udc | OF 1.2: T/T / P/G / P/P | OF 1.5 | OF 2.0 | OF 2.5 | T/T worst (1.47 p.u.) |
|---|---|---|---|---|---|
| 800 V | 1.31 / 2.22 / 3.74 | 1.64 / 2.77 / 4.68 | 2.18 / 3.70 / 6.24 | 2.73 / 4.62 / 7.80 | 2.29 |
| 1200 V | 1.97 / 3.33 / 5.62 | 2.46 / 4.16 / 7.02 | 3.28 / 5.54 / 9.36 | 4.09 / 6.93 / 11.70 | 3.44 |
| 1600 V | 2.62 / 4.44 / 7.49 | 3.28 / 5.54 / 9.36 | 4.37 / 7.39 / 12.48 | 5.46 / 9.24 / 15.60 | 4.59 |

Worked arithmetic for the 1600 V rows:
- T/T, OF 1.5: 1600 × 1.5 × 0.7 × 1.25 × 1.3 × 1.2 = 3276 V.
- P/G, OF 1.5: 1600 × 1.5 × 1.4 × 1.25 × 1.1 × 1.2 = 5544 V.
- P/P, OF 1.5: 1600 × 1.5 × 2 × 1.25 × 1.3 × 1.2 = 9360 V.
- T/T worst: 1600 × 1.47 × 1.25 × 1.3 × 1.2 = 4586 V.

The 800 V row reproduces the earlier report exactly: 1.31–1.64, 2.29, 2.22–2.77 and 3.74–4.68 kVpp.

**Table 5.2 — Qualification targets on aged specimens (EF_Aging = 1.0), kVpp, calculation**

| Udc | OF 1.2: T/T / P/G / P/P | OF 1.5 | OF 2.0 | T/T worst |
|---|---|---|---|---|
| 800 V | 1.09 / 1.85 / 3.12 | 1.36 / 2.31 / 3.90 | 1.82 / 3.08 / 5.20 | 1.91 |
| 1200 V | 1.64 / 2.77 / 4.68 | 2.05 / 3.47 / 5.85 | 2.73 / 4.62 / 7.80 | 2.87 |
| 1600 V | 2.18 / 3.70 / 6.24 | 2.73 / 4.62 / 7.80 | 3.64 / 6.16 / 10.40 | 3.82 |

This is the relevant table for "after oil ageing" measurements: the specimen is really aged, so EF_Aging = 1 per Part III.

**Table 5.3 — At maximum bus voltage (×1.125; verification), kVpp, calculation**

| Udc max | OF 1.2: T/T / P/G / P/P | OF 1.5 | OF 2.0 | T/T worst |
|---|---|---|---|---|
| 900 V | 1.47 / 2.49 / 4.21 | 1.84 / 3.12 / 5.26 | 2.46 / 4.16 / 7.02 | 2.58 |
| 1350 V | 2.21 / 3.74 / 6.32 | 2.76 / 4.68 / 7.90 | 3.69 / 6.24 / 10.53 | 3.87 |
| 1800 V | 2.95 / 4.99 / 8.42 | 3.69 / 6.24 / 10.53 | 4.91 / 8.32 / 14.04 | 5.16 |

**Table 5.4 — 3-level (NPC/ANPC/T-type) variant, verification, kVpp, calculation with the assumption in item 1**

| Udc | OF 1.2: T/T / P/G / P/P | OF 1.5 | OF 2.0 |
|---|---|---|---|
| 800 V | 0.66 / 2.03 / 3.43 | 0.82 / 2.31 / 3.90 | 1.09 / 2.77 / 4.68 |
| 1200 V | 0.98 / 3.05 / 5.15 | 1.23 / 3.47 / 5.85 | 1.64 / 4.16 / 7.02 |
| 1600 V | 1.31 / 4.07 / 6.86 | 1.64 / 4.62 / 7.80 | 2.18 / 5.54 / 9.36 |

**Table 5.5 — AC (50 Hz) wire-pair or plate test equivalents of Table 5.1, V r.m.s. = Vpp ÷ 2√2, calculation**

| Udc | OF 1.2: T/T / P/G / P/P | OF 1.5 | OF 2.0 | T/T worst |
|---|---|---|---|---|
| 800 V | 463 / 784 / 1324 | 579 / 980 / 1655 | 772 / 1307 / 2206 | 811 |
| 1200 V | 695 / 1176 / 1986 | 869 / 1470 / 2482 | 1158 / 1960 / 3309 | 1216 |
| 1600 V | 927 / 1568 / 2647 | 1158 / 1960 / 3309 | 1544 / 2613 / 4412 | 1622 |

**Interpretation for the oil-ageing study:**
- **Ratio of targets between buses.** At equal OF, the 1200 V and 1600 V targets are exactly 1.5× and 2× the 800 V targets. A test ladder of RPDIV thresholds can therefore be defined once and scaled.
- **Proposed pass levels for straight wire pairs (T/T, after oil ageing, qualification basis, OF 1.2–1.5).**

  | Bus | 2-level | 3-level |
  |---|---|---|
  | 800 V | ≥ 1.1–1.4 kVpp | — |
  | 1200 V | ≥ 1.6–2.1 kVpp | — |
  | 1600 V | ≥ 2.2–2.7 kVpp | ≈ 1.1–1.4 kVpp |

  Add ≈ +40 % (OF 2.0 / OF 1.5 ≈ 1.33, plus margin) if the motor will be cable-fed.
- **Conductor-to-plate or slot mock-up (P/G).** At 1600 V the level is about 3.7–4.6 kVpp, i.e. about 1.3–1.6 kV r.m.s. AC. This is a slot-liner-plus-wire system requirement, not a wire-only one.
- **Feasibility vs reported values.**
  - The highest rectangular-wire PDIV in the earlier notes is 2.7 kV (Essex, conditions not stated), and bipolar-pulse PDIV of thin enamel was only 0.8–1.0 kV (Pauli).
  - 800 V T/T targets look attainable with thick enamel or PEEK builds. 1200 V targets require thick builds (the PEEK/PI class).
  - The 1600 V 2-level targets (2.6–4.6 kVpp T/T) exceed every PDIV value found for enamel or extruded rectangular wire. They point to one of three routes:
    - (a) much thicker or lower-permittivity multilayer insulation;
    - (b) a 3-level topology;
    - (c) a Type II design (mica or inorganic-filled, life-tested per 18-41/42).
  - Glass-fibre-covered or porous builds will be PD-free only if fully impregnated.
- **Measurement temperature and EF_T.** EF_T exists because PDIV falls at service temperature. If RPDIV is measured at the maximum operating temperature (e.g., in the hot-oil condition), EF_T could arguably be set to 1, reducing the targets by 1.3 (T/T, P/P) or 1.1 (P/G). This is my inference; Part III's wording on testing at temperature was not re-checked.
- **Report the waveform with the result.** RPDIV must be reported together with waveform, polarity, rise time and pC threshold. Pauli shows sinusoidal, unipolar and bipolar values for the same wire differing by more than 2×, so a "pass" at 50 Hz does not prove PD-free operation under a 45 kV/µs bipolar SiC waveform.
- **Bound for hairpins with adjacent first/last conductors.** With a = 0.9 (GAMBICA's upper bound) and OF 1.2, the T/T verification target would reach 3.37 / 5.05 / 6.74 kVpp for 800 / 1200 / 1600 V. This shows why the winding plan (non-adjacent line-end conductors) matters as much as the insulation material.

### Gaps
- 18-41 Table B.6 (twisted-pair T/T test levels) could not be checked against these calculations.
- The OF of the intended drive (integrated vs cabled; SiC rise time at 1200/1600 V) is unmeasured. All targets hinge on the OF assumption.
- No quantitative humidity or altitude enhancement factor is available. Oil-wetted or oil-immersed PDIV (vs dry air) for the candidate insulations at 1200/1600 V-level targets was not found. Whether to measure in air after draining or in oil must be fixed by the study.
- No published RPDIV data at 1200/1600 V-level targets were found for the specific technologies in the study (PI tape, glass-fibre, epoxy powder, parylene on rectangular copper).
