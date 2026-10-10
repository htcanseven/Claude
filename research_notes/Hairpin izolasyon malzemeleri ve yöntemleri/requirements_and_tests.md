# Requirements and Test Methods for Insulated Rectangular (Hairpin) Copper Conductors – EV Traction Motors, 400–800 V, SiC Inverters

*Conventions: Vp = peak; Vpk/pk = peak-to-peak; P/P = phase-to-phase, P/G = phase-to-ground, T/T = turn-to-turn (conductor-to-conductor). Every source below was opened (fetched or downloaded and text-extracted) on 2026-10-10. Standards previews (VDE-Verlag, iTeh) show the table of contents, foreword, scope and first clauses only, so clause-level numbers deeper in the standards could not be read; these are listed under Gaps. The web-search budget for this session ran out before the end of the research. Some items below could not be checked for that reason, and each one is flagged where it appears.*

---

## 1. Electrical requirements for 400 V / 800 V SiC-fed hairpin motors: IEC 60034-18-41 (Type I), IEC 60034-18-42 (Type II), IEC TS 61934, IEC 60270, PDIV targets, published PDIV values, environment effects and impulse endurance

### Takeaway
IEC 60034-18-41 (current valid version: Ed. 1.1 CSV 2014+AMD1:2019) is the governing framework. It requires a PD-free design. The critical voltage each insulation sub-system must exceed is Vc = Vdc·OF·WF·EF_PD·EF_T·EF_Aging, with EF_PD = 1.25, EF_T = 1.3 (T/T, P/P) or 1.1 (P/G), and EF_Aging = max(1; 1.2·Ts/Tc). AMD1 adds humidity and altitude as further possible enhancement factors.

No OEM-published "800 V hairpin PDIV target" was found. Supplier patents use these PDIV acceptance thresholds for rectangular wire:
- at least 0.7–1.0 kVp at 25 °C;
- preferred values of 1.3–2.5 kV;
- at least 50 % retention at 250 °C.

Applying the 18-41 equation to an 800 V DC link gives T/T targets of roughly 1.3–2.3 kV (peak-to-peak) and P/G targets of roughly 2.2–2.8 kV (my calculation; see Inferences).

PDIV falls with temperature (about 10 % from RT to 140 °C for bare twisted pairs) and with lower pressure (minimum at 50–70 mbar). Humidity can shift PDIV in both directions, and fast rise times can lower impulse PDIV by roughly 20–40 %. These effects are why PDIV must be measured at the maximum service temperature and with a defined RH, waveform and pC threshold.

### Cited Findings

#### 1.1 Standards framework and status (as of Oct 2026)
- **IEC 60034-18-41 status.** The IEC webstore lists IEC 60034-18-41:2014/AMD1:2019 as a consolidated version (CSV), Edition 1.0, published 2019-06-25. The December 2020 corrigendum is included and the listed stability date is 2029 — [IEC webstore 32755](https://webstore.iec.ch/en/publication/32755)
- **Scope.** The standard covers stator/rotor windings fed by voltage-source PWM drives and defines qualification tests and type/routine tests. It does not apply to:
  - machines rated ≤ 300 V r.m.s.;
  - rotor windings operating at ≤ 200 V peak;
  - machines that are only started by converters.

  — [IEC 60034-18-41:2014 preview (iTeh)](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Type I vs Type II.** Type I insulation systems are "not expected to experience partial discharge activity within specified conditions in their service lives". Type II systems are expected to withstand PD throughout service life. Type I systems "are generally used in rotating machines rated at 700 V r.m.s. or less and tend to have random wound windings" — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Severity selection.** The drive-system integrator must tell the machine manufacturer what voltage will appear at the machine terminals. Severity is based on impulse rise time and peak-to-peak voltage, plus repetition rate for Type II. The expected overshoot range is divided into bands and testing is done at the extreme value of each band. The default rise time is 0.3 µs; other rise times or overshoots are treated as special cases — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Converter rise times.** "Modern converter output voltage rise times may be in the 0,05 µs – 2,0 µs range" — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf). This 2014 text predates wide-bandgap devices. A 2024 review shows overshoot curves down to 10 ns rise time and cites OF determination at 6.5 ns. It also notes that per IEC 60034-18-41 the terminal voltage "may double" the inverter voltage because of impedance mismatch — [Zhou et al., Energies 2024, 17, 1987 (PDF)](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)
- **Qualification route.** Representative test objects go through the IEC 60034-18-21 (random-wound) or IEC 60034-18-31 (form-wound) test sequences, "with the addition of a high frequency voltage test and a partial discharge test". The PD test may need impulse equipment per IEC/TS 61934. If the object is PD-free at the end of the sequence, the system is qualified for the selected severity band. Type tests and optional routine tests are done on complete windings — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Qualification test objects.** The table of contents lists:
  - 10.2.2 "Twisted pair or equivalent arrangement";
  - 10.2.3 "Motorette (random wound) or formette (form-wound)";
  - Table 4 "Stress categories for Type I insulation systems based on a 2-level converter";
  - Table B.2 "Summary of enhancement factors";
  - Table B.6 "Turn/turn PD test levels for special windings and twisted pairs".

  — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Key definitions** — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf):
  - RPDIV = "minimum peak-to-peak impulse voltage at which more than five PD pulses occur on ten voltage impulses of the same polarity".
  - PDIV is given as r.m.s. for sinusoidal voltage and as peak-to-peak for impulses.
  - Impulse rise time is measured from 10 % to 90 %.
  - Overshoot factor = ratio of the machine-terminal voltage to the converter voltage for each converter level.
  - Jump voltage Uj is defined in 3.22.
- **AMD1:2019 impulse voltage insulation classes (IVIC A/B/C/D/S).** Table D.1 gives the maximum allowable peak-to-peak operating voltage in units of U_N:

  | IVIC | P/P (× U_N) | P/G (× U_N) | Enhancement ratio (P/G) | TVF | Routine P/G test, U_N = 500 V |
  |---|---|---|---|---|---|
  | A | 3.0 | 2.1 | 1.3 | 0.7 | 2.0 kV r.m.s. |
  | B | 4.1 | 2.8 | 1.7 | 1.0 | 2.0 kV r.m.s. |
  | C | 5.4 | 3.8 | 2.3 | 1.3 | 2.3 kV r.m.s. |
  | D | 6.7 | 4.7 | 2.9 | 1.7 | 2.7 kV r.m.s. |
  | Line-fed | 2.8 | 1.6 | — | — | 2 kV r.m.s. |

  For machines ≤ 200 kW with U_N ≤ 1 kV, the 1 min routine withstand test may be replaced by a 1 s test at 120 % — [IEC 60034-18-41 AMD1:2019 preview (full amendment text)](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- **AMD1 Table B.5 (worked example, 500 V winding, 2-level converter, EF = 1.25, without the 1.1 line-variation factor).** Maximum peak-to-peak PD-test voltages:

  | Stress category | P/P | P/G |
  |---|---|---|
  | A (Benign) | 1 857 V | 1 300 V |
  | B (Moderate) | 2 532 V | 1 773 V |
  | C (Severe) | 3 375 V | 2 364 V |
  | D (Extreme) | 4 219 V | 2 955 V |

  "It is generally expected that the total enhancement factor will be 1,25" — [IEC 60034-18-41 AMD1:2019 preview](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- **AMD1 on humidity and altitude.** Relative humidity and air density (altitude) may affect PDIV "to a similar extent as the temperature", and humidity can move PDIV/RPDIV "in both directions", so a further enhancement factor could be applied. For altitude, "an additional enhancement factor" should reflect the expected maximum altitude in service — [IEC 60034-18-41 AMD1:2019 preview](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf)
- **IEC 60034-18-42 (Type II, PD-resistant).** Current version is Edition 1.1, 2020-08 (CSV of 2017+AMD1:2020). It qualifies the mainwall, turn insulation and stress-control system through life curves and voltage-endurance tests. Annex B gives impulse test circuits and Annex E covers IVIC derivation. Type II systems are "generally used in rotating machines which have form-wound windings, mostly rated above 700 V r.m.s.", and qualification "involves destructive ageing of test objects". The same introduction places Type I in machines "with rated voltage less than 700 V r.m.s." — [IEC 60034-18-42 Ed.1.1 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf)
- **IEC TS 61934:2024 (Edition 3.0, 2024-01-26, TC 42).** Covers off-line electrical PD measurement under repetitive impulses from power electronics (motors, inductive reactors, wind-turbine generators, power modules). It excludes optical/ultrasonic methods and non-repetitive impulses. Changes from 2011:
  - background on wide-bandgap devices added;
  - impulse-generator waveform parameters changed to suit WBG devices;
  - charge-based measurements and source-controlled gating removed;
  - bibliography deleted.

  Listed stability date is 2026 — [IEC webstore 91294](https://webstore.iec.ch/en/publication/91294)
- **IEC 60270 Edition 4.0 (2025-06).** Retitled "High-voltage test techniques – Charge-based measurement of partial discharges". It now applies to AC up to 500 Hz or DC, with a "clear focus on charge-based partial discharge measurements", streamlined performance checks and an improved normative Annex A for calibrators. It replaces the third edition (2000) and its Amendment 1 (2015) — [IEC 60270 Ed.4.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60270%7Bed4.0%7Db.pdf)

#### 1.2 How the PD-free target is derived (enhancement factors)
- **Critical voltage equation.** Lusuardi et al. (IEEE Access 2021) restate the IEC 60034-18-41 empirical equation as Vc = Vdc·OF·WF·EF_PD·EF_T·EF_Aging — [Lusuardi, Rumi, Cavallini et al., "PD in electrical machines for the MEA, Part III", IEEE Access 2021 (Zenodo record)](https://zenodo.org/records/4562202); [PDF](https://zenodo.org/records/4562202/files/access%20part%20III.pdf?download=1)
  - OF = peak voltage at motor terminals ÷ DC-bus voltage.
  - WF (winding factor) = 2 for P/P, 1.4 for P/G and 0.7 for T/T, "when experimental results or simulations are missing".
  - EF_PD = 1.25, to cover PD extinction occurring below PDIV.
  - EF_T = 1.3 for T/T and P/P, and 1.1 for P/G because the P/G insulation runs cooler.
  - EF_Aging = max(1; 1.2·Ts/Tc), where Ts = service temperature and Tc = class temperature.
- **Verification vs qualification tests** — [Part III, IEEE Access 2021](https://zenodo.org/records/4562202):
  - Verification tests on new stators use EF_Aging > 1.
  - In qualification tests EF_Aging = 1, because the specimens are actually aged in sub-cycles per IEC 60034-18-21 (thermal, mechanical, ambient), each followed by a PD-proof test.
  - Failure is PD inception below Vc, or breakdown.
  - At least 5 samples are required; twisted pairs or motorettes are customary.
- **Meaning of EF_Aging.** EF_Aging = 1.2 implies the PDIV is allowed to fall to 1/1.2 = 83 % over life. In thermal ageing of class-200 wires at 230 °C, PDIV and insulation thickness fell together because volatile by-products leave the enamel — [Part III](https://zenodo.org/records/4562202)
- **Choice of waveform** — [Part III](https://zenodo.org/records/4562202):
  - On complete stators, AC (sinusoidal) testing of P/G and P/P is allowed and "more conservative".
  - T/T on complete stators needs surge generators.
  - RPDIV from surge generators exceeds the true PDIV, because interference masks PD and unipolar, low-repetition impulses have a low inception probability.
  - On twisted pairs, AC PDIV tests are acceptable because the potential difference between points is the same under AC or impulse.
- **Worked example of in-service stress (random-wound motor, not hairpin).** The worst T/T stress was 1.47 p.u. of Vdc (2 m cable, rise time < 25 ns, first and last turns adjacent). The maximum P/G overvoltage was 1.2 p.u. (15 m cable). The reflection coefficient was limited to 1.85 by cable/machine impedance mismatch — [Part III](https://zenodo.org/records/4562202)

#### 1.3 Published PDIV / RPDIV reference values for rectangular and hairpin conductors
- **Essex Group patent US9324476B2 (priority 2014; flag: older).** Table 1 averages for PEEK-topcoat constructions:

  | Construction | Avg dielectric strength | Avg PDIV |
  |---|---|---|
  | PEEK only | 9.0 kV | 1.5 kV |
  | PI + PEEK | 10.0 kV | 1.6 kV |
  | PAI + PEEK | 11.1 kV | 1.8 kV |
  | PI + PEEK (another build) | 11.7 kV | 2.7 kV |
  | tape/PAI/PI build | 11.5 kV | 1.5 kV |
  | PAI/PI/PAI + PEEK | 11.1 kV | 1.7 kV |

  - Stated targets: PDIV > ~1 000 V, with preferred levels > 1 300, 1 500, 2 000 and 2 500 V; dielectric strength > ~10 kV (some embodiments > 15 kV).
  - Thicknesses: enamel 25–254 µm (preferred 76–127 µm), extruded PEEK/PAEK 25–610 µm (preferred 76–178 µm), total typically 85–240 µm.
  - Per-sample thickness and PDIV test temperature are not given in the table.

  — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- **Furukawa "inverter surge-resistant" patent US9224523B2 (priority 2013; flag: older).**
  - Rectangular Cu conductor 1.8 × 3.4 mm with 0.3 mm corner chamfer.
  - PDIV acceptance: ≥ 1 kVp at 25 °C, and ≥ 50 % of that value retained at 250 °C (AC 50 Hz, 10 pC).
  - Results:

    | Construction | Total thickness | Result |
    |---|---|---|
    | PAI 25 µm + PEEK 26 µm | 51 µm | pass |
    | PAI 40 µm + PEEK 103–160 µm | 143–200 µm | pass |
    | PI 40 µm + PEEK 108 µm | 148 µm | pass |
    | PAI 25 µm + PEEK 20 µm | 45 µm | fail (PDIV) |
    | PAI 25 µm + PA66 28 µm | 53 µm | fail (PDIV) |
    | PEEK only, 52 µm | 52 µm | PDIV pass, but 250 °C breakdown fail |
    | PAI 40 µm + PEEK 185–212 µm | 225–252 µm | fail (wind-and-heat test) |
    | PPS 146–185 µm | — | fail (breakdown) |

  - The text states that PDIV at 25 °C falls below 1 kVp when the total thickness is under 50 µm.
  - Relative permittivity (100 Hz), 25 °C → 250 °C: PAI 3.9 → 4.4; PI 3.5 → 4.0; PEEK 3.1 → 4.7.

  — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)
- **Essex Furukawa patent US11232885B2 (priority 2015).**
  - Preferred PDIV ≥ 700 Vp, more preferably ≥ 800 Vp and ≥ 1 000 Vp; preferred upper limit about 2 500 Vp.
  - Thermoset stack 30–130 µm (preferred 80–120 µm); optional thermoplastic outer layer 30–130 µm (PEEK, PPS).
  - Conductor width 1–5 mm, thickness 0.4–3.0 mm, corner radius ≤ 0.6 mm.

  — [US11232885B2](https://patents.google.com/patent/US11232885B2/en)
- **Univ. Stuttgart hairpin study (Energies 2025).** Specimen: hairpin-in-slot emulations, PAI Grade 3 ≈ 100 µm, 300 × 4 × 2 mm, rated 800 V, temperature index ≥ 220 °C, heat shock ≥ 240 °C.
  - RPDIV was measured at 20–180 °C with PWM rise times of 70–120 ns.
  - RPDIV rises with rise time, but temperature has the larger effect.
  - The spread across rise times was about 200 V at RT and more than 400 V at 80 °C and 180 °C.
  - Ageing excitation levels (675–975 V) were chosen below RPDIV.

  — [He, Tenbohlen, Beltle, Energies 2025, 18, 1376 (DNB copy)](https://d-nb.info/1376542846/34)
- **Nagoya Univ. / Nippon Soken (IEEE TDEI 2016; flag: older).** AIW (polyamide-imide) rectangular wires were tested: 2.3 × 1.5 mm with a 40 µm coating and 2.8 × 2.1 mm with a 160 µm coating, a range "decided from the range of variation in the actual motor used in the commercial product". In a field model of the same geometry, surface moisture changed the computed PDIV from 840 V to 680 V in one case and from 840 V to 950 V in another — [Wakimoto, Kojima, Hayakawa, IEEE TDEI 23(6) 2016 (repository PDF)](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf)
- **Phase-to-ground (slot liner) context.**
  - A slot-liner supplier offers 0.13 mm and 0.19 mm NKN/NMN spiral tubes with "dielectric strength up to 12 kV" and UL system integration up to 220 °C. For 800 V it recommends special Nomex grades 818–864 and Kapton MT+ (vendor claim; no test basis given) — [Electric Motor Engineering](https://www.electricmotorengineering.com/e-motor-400-800v-insulation-thermal-management-for-hairpin-stator-slot-liner/)
  - Hairpin windings reach fill factors up to 70 % with a limited number (8–10) of conductors per slot — [Zhou et al., Energies 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)

#### 1.4 Effects of temperature, pressure, humidity and waveform on PDIV
- **Temperature, twisted pairs.** At 140 °C the B10 PDIV of non-impregnated twisted pairs was 10 % lower than at RT, and 19 % lower for impregnated twisted pairs. An air-number-density model predicts a 9 % drop from RT to 140 °C. Some impregnating resins can make impregnated pairs fall below bare pairs at high temperature. Test procedure: AC 50 Hz, 1 nF coupling capacitor, HFCT into a Techimp PDBase II, 25 V steps of 30 s each — [Part III](https://zenodo.org/records/4562202)
- **Temperature, wire permittivity.** Higher temperature lowers PDIV mainly through lower air density. Enamel permittivity also matters: Muto et al. compared PAI and PEEK over 25–230 °C. A permittivity-only (Dakin) model fits within about 10 % below 60 °C, but its error grows to about 27 % at 180 °C. Air-density models (Lusuardi) stay within about 10–12 %. Windings "can reach 180 °C" in operation — [Elorza Azpiazu et al., Appl. Sci. 2023, 13, 2417 (PDF)](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)
- **Temperature, hairpin specimens.** On hairpin-in-slot specimens, temperature had a larger effect on RPDIV than rise time (70 vs 120 ns) — [He et al., Energies 2025](https://d-nb.info/1376542846/34)
- **Pressure / altitude.**
  - PDIV versus pressure is U-shaped, with the minimum at 50–70 mbar (Lusuardi, 50 Hz, twisted pairs). PDIV rises from 100 to 1 013 mbar — [Elorza Azpiazu et al. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)
  - For 0.56 mm round wire, insulation is 12.5/23.5/35.5 µm for grades 1/2/3. Going from grade 2 to grade 3 raises PDIV by 16 % at 1 000 mbar but only 8.7 % at 150 mbar (438 V → 476 V), so thicker enamel helps less at altitude — [Part III](https://zenodo.org/records/4562202)
- **Humidity.**
  - On rectangular AIW wire pairs at 25 °C, PDIV was stable at 20 % RH. At 90 % RH, pre-discharge made PDIV first fall and then rise. The authors attribute this to moisture adhering to the coating surface, which raises surface conductivity. At 20 % RH, PDs sat close to the contact point of the wires; at 90 % RH their location shifted with pre-discharge time. PDIV could be measured stably at higher frequency (1 kHz) in high humidity — [Wakimoto et al. 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf)
  - In the literature PDIV first rises with RH up to a peak and then falls. Below about 3 450 V the surface-conductivity/permittivity mechanism dominates, so PDIV falls with RH. Samples washed with pure water showed no humidity effect (Muto) — [Elorza Azpiazu et al. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)
- **Rise time / waveform (conflicting evidence).**
  - Wei et al.: PDIV (peak) was 28 % lower under 150 ns unipolar square pulses than under 60 Hz sine, and a further 21 % lower when rise time went from 150 to 60 ns. Another study found DC PDIV 23–38 % lower when rise time went from 1 000 ns to 150 ns. Other authors conclude that PDIV depends on the overshoot rather than the rise time itself — [Elorza Azpiazu et al. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)
  - In contrast, Part III states that the waveform changes the voltage distribution "but not the physics of the discharge, leading to the same PDIV" — [Part III](https://zenodo.org/records/4562202)

#### 1.5 Voltage endurance under repetitive impulses
- **Electro-thermal ageing of hairpin-in-slot specimens.** Conditions:
  - PWM at 1 kHz, 500 µs pulse width, 70 ns fall time and 70/120 ns rise time;
  - excitation of 0/675/750/825/900/975 V;
  - 20/67.5/115/162.5/210 °C;
  - 20 groups × 4 DUTs, at least 250 h.

  Detection used an HFCT (10 MHz–1 GHz) with a 290 MHz–3 GHz band-pass filter. Failure rate was 29.5 % (13/44) in Group A, where RPDIV was measured every 24–96 h, and 20.5 % (9/44) in Group B. The authors conclude that RPDIV alone cannot predict the degree of ageing, that electrical and thermal stress interact strongly, and that failure rate was the most reliable indicator. The lifetime regression follows IEC 61858 — [He et al., Energies 2025](https://d-nb.info/1376542846/34)
- **Diagnostic sessions in ageing tests.** These are run every 24/48 h. One example is an AC hipot at 500 Vrms, 50 Hz for 1 min. End of life is breakdown, and setting the diagnostic voltage at the wire's PDIV gives a more conservative life estimate — [Zhou et al., Energies 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)

#### 1.6 Test-matrix rows (requirement → method/standard → specimen → conditions → reference/acceptance values)

| Requirement | Method / standard | Specimen | Typical conditions | Reference / acceptance values | Source |
|---|---|---|---|---|---|
| PD-free T/T, P/G, P/P (Type I) | IEC 60034-18-41 qualification PD test; AC via IEC 60270, impulse via IEC TS 61934 | Twisted pair or equivalent; motorette/formette; complete winding | After IEC 60034-18-21 ageing sub-cycles; PD-proof after each sub-cycle; ≥ 5 samples | PD-free at Vc = Vdc·OF·WF·1.25·EF_T·EF_Aging (EF_T 1.3/1.1; EF_Aging 1 in qualification, max(1; 1.2·Ts/Tc) in verification) | [18-41 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf); [Part III](https://zenodo.org/records/4562202) |
| Wire-pair PDIV screening | AC 50 Hz, ramp 50 V/s, 10 pC threshold | Two rectangular wires, flat faces in contact over 150 mm | 25 °C and 250 °C | ≥ 1 kVp at 25 °C; ≥ 50 % retained at 250 °C | [US9224523B2](https://patents.google.com/patent/US9224523B2/en) |
| PDIV humidity sensitivity | AC 5 Hz / 50 Hz / 1 kHz, ramp 20 V/s, first pulse > 5 pC, 5 repeats | One bent wire clipped to a second wire at 7.8 N | 25 °C; 20 % and 90 % RH; pre-discharge 1.2 × PDIV at 1 kHz for 5–60 s | PDIV unstable at 90 % RH after pre-discharge; stable at 1 kHz | [Wakimoto 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf) |
| RPDIV and impulse endurance of hairpin | PWM 1 kHz, 70–120 ns rise, HFCT detection (paper cites IEC 60034-18-42) | Hairpin-in-slot, 300 mm, PAI ≈ 100 µm | 20–210 °C; 675–975 V; ≥ 250 h | Failure rate 20.5–29.5 %; RPDIV not a stand-alone ageing indicator | [He 2025](https://d-nb.info/1376542846/34) |
| Wire dielectric breakdown | AC 50 Hz, 500 V/s, 5 mA trip | Rectangular wire wrapped in metal foil | 25 °C and 250 °C | 250 °C value ≥ 50 % of 25 °C value | [US9224523B2](https://patents.google.com/patent/US9224523B2/en) |
| Machine routine withstand | IEC 60034-18-41 AMD1 Annex D / IEC 60034-1 | Complete winding | 50/60 Hz, 1 min (or 1 s at 120 % for ≤ 200 kW, U_N ≤ 1 kV) | 2.0/2.0/2.3/2.7 kV r.m.s. for IVIC A/B/C/D at U_N = 500 V | [AMD1 preview](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf) |

### Inferences
- **Stress-category overshoot factors are recoverable from AMD1 tables.** Using Upk/pk(P/P) = 2·OF·Udc and Udc = 1.35·U_N (no 1.1 line factor):
  - OF = 1.1 / 1.5 / 2.0 / 2.5 for categories A / B / C / D gives 2.97 / 4.05 / 5.4 / 6.75 × U_N, which matches Table D.1 (3.0 / 4.1 / 5.4 / 6.7).
  - Multiplying by 1.25 × 675 V reproduces Table B.5: 1 856 / 2 531 / 3 375 / 4 219 V P/P.
  - P/G = 0.7 × P/P in both tables, which is consistent with the WF ratio 1.4 / 2.
  - The Table 4 text itself was not accessible, so these OF bands are inferred, not quoted.
- **800 V worked example (my calculation, not a published target).** Inputs: Vdc = 800 V, OF = 1.2–1.5 (an assumption for short EV inverter-to-motor connections; it must be measured), EF_PD = 1.25 and EF_Aging = 1.2 (Ts = Tc).
  - T/T (WF 0.7, EF_T 1.3): 1.31–1.64 kV.
  - T/T with the worst-case 1.47 p.u. stress from Part III (adjacent first/last conductors): ≈ 2.3 kV.
  - P/G (WF 1.4, EF_T 1.1): 2.2–2.8 kV.
  - P/P (WF 2, EF_T 1.3): 3.7–4.7 kV.
  - All values are peak-to-peak RPDIV levels and scale linearly with Vdc. A 900 V maximum battery voltage adds about 12.5 %; a 400 V system roughly halves them.
  - This is consistent with the ">1.5–2 kVp" PDIV figures commonly quoted for 800 V hairpin wire and with the 1.3–2.5 kV preferred levels in the Essex patent.
- **Why the patent thresholds look sufficient for 400 V only.** The 1 kVp at 25 °C and 50 % retention at 250 °C criteria (Furukawa) look adequate for 400 V T/T stress. For 800 V T/T, at least about 1.6–2.3 kV at the maximum service temperature appears necessary, which favours total insulation well above 100 µm. This fits the Stuttgart observation that Grade 3 PAI ≈ 100 µm hairpins rated 800 V were aged at 675–975 V below their RPDIV.
- **Material permittivity matters for PEEK at temperature.** PEEK's permittivity rises more steeply with temperature than PAI's (3.1 → 4.7 vs 3.9 → 4.4 from 25 to 250 °C). Its room-temperature PDIV advantage should therefore shrink at operating temperature. PDIV acceptance should be defined at the maximum winding temperature (180 °C or more), not only at RT.
- **The PD threshold must be specified.** The cited methods use 5 pC (Nagoya), 10 pC (Furukawa), 50 pC (Elorza Azpiazu 2023) and "50 pC occurring 50 times" (Proterial; see §3). Results are not comparable unless the threshold, ramp rate, waveform, RH and temperature are fixed in the test plan.
- **Hairpin stators fall under Type I.** An 800 V-DC SiC traction motor normally has a line-to-line fundamental below 700 V r.m.s., so it falls within the Type I (PD-free) domain. IEC 60034-18-42 life-curve testing would apply only if PD is allowed by design.

### Gaps
- The text of Table 4 (stress categories) and Table B.2 (enhancement factors) of IEC 60034-18-41 was not accessible. The OF bands above are inferred. The Table B.6 turn/turn PD test levels for twisted pairs were not accessible either.
- The status of IEC 60034-18-41 Edition 2 is unverified. A search-engine summary claimed an Ed. 2.0 project at PCC stage with a forecast date of 2026-05-04, but the IEC webstore page I opened showed only the 2019 CSV with a 2029 stability date.
- I could not verify that IEC TS 60034-27-5 (off-line PDIV under repetitive impulses on windings) exists or what its edition is, because the search budget was exhausted.
- No OEM-published PDIV target for 800 V hairpin motors was found.
- No independent, peer-reviewed side-by-side PDIV dataset for enamelled vs extruded-PEEK rectangular wire at stated thickness and temperature was retrievable. An IEEE abstract reporting PDIV of 781 V vs 668 V for enamelled-extruded vs conventional wire could not be opened.
- The Von Roll/ELANTAS ISEIM 2020 paper "Electrical Insulation at 800 V Electric Vehicles" could not be retrieved (redirected).
- No quantitative humidity enhancement factor for rectangular wire was found. The Ji/Giangrande et al. (IEEE TTE 2024) ambient-EF paper was not accessible.

---

## 2. Winding-wire test standards: IEC 60851 series, IEC 60317-0-2, IEC 60172, IEC 60216, NEMA MW 1000, JIS C 3216 and newer documents

### Takeaway
The IEC toolkit for enamelled rectangular wire is current. The key editions are:
- IEC 60317-0-2:2020 (general requirements);
- IEC 60851-3:2023 (mechanical);
- IEC 60851-5:2026 (electrical);
- IEC 60851-4:2016 (chemical);
- IEC 60851-6:2012 (thermal);
- IEC 60172:2020 (temperature index at 20 000 h).

None of these contains a partial-discharge test or an abrasion test for rectangular wire. No IEC specification for extruded PEEK rectangular wire was found. Industry practice (Essex, Furukawa, Proterial patents) fills these gaps with NEMA MW 1000, ASTM D1676/D2307, JIS C 3216 and JIS C 3003 procedures.

### Cited Findings
- **IEC 60317-0-2:2020 (Edition 4.0, 2020-06)** — [IEC 60317-0-2 Ed.4.0 preview (VDE)](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-2%7Bed4.0%7Db.pdf)
  - General requirements for enamelled rectangular copper winding wire; replaces the 2013 edition and is read with IEC 60851. Clause numbers equal the IEC 60851 test numbers, and IEC 60317 prevails over IEC 60851 if they are inconsistent.
  - Clauses: 4 dimensions; 5 resistance; 6 elongation; 7 springiness (only for nominal proof strength ≤ 80 N·mm⁻²); 8 flexibility and adherence (8.1 mandrel winding, Table 7); 9 heat shock; 10 cut-through; 11 abrasion; 12 solvents; 13 breakdown voltage (Table 8); 14 continuity; 15 temperature index (to IEC 60172); 16 refrigerants; 17 solderability; 18 heat/solvent bonding; 19 dielectric dissipation factor; 20 resistance to transformer oil; 21 loss of mass; 23 pin-hole test; 30 packaging.
  - Changes vs 2013: a bonding-layer definition and dimensions; Clause 6 now accounts for proof strength; revised adherence test (8.2); references for copper rod (EN 1977, ASTM B49, ISO 6892-1:2016).
- **IEC 60851-2 (Edition 3.2, 2019-05 CSV).** Test 4, dimensions, including the procedure for "rounding of corners of rectangular wire" and overall dimension — [IEC 60851-2 Ed.3.2 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-2%7Bed3.2%7Db.pdf)
- **IEC 60851-3:2023 (Edition 4.0, 2023-08)** — [IEC 60851-3 Ed.4.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-3%7Bed4.0%7Db.pdf)
  - Replaces the 2009 edition with AMD1:2013 and AMD2:2019.
  - Test 6, elongation: rate (5 ± 1) mm/s, free length 200–250 mm, plus tensile strength.
  - Test 7, springiness: a separate procedure covers round wire > 1.6 mm and rectangular wire.
  - Test 8, flexibility and adherence:
    - mandrel winding, with a separate rectangular-wire subclause;
    - stretching (round > 1.6 mm);
    - jerk (round ≤ 1.0 mm);
    - peel (round > 1.0 mm);
    - an adherence test for enamelled rectangular wire.
  - Test 11, abrasion, applies to enamelled round wire only.
  - Test 18, heat bonding, includes enamelled rectangular wire. Annex B covers friction.
  - The only listed change is a clarification of the loss-of-adhesion distance measurement.
- **IEC 60851-5 (Edition 4.2, 2019-09 CSV = 2008+AMD1:2011+AMD2:2019)** — [IEC 60851-5 Ed.4.2 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-5%7Bed4.2%7Db.pdf)
  - Tests: 5 resistance; 13 breakdown voltage; 14 continuity; 19 dielectric dissipation factor; 23 pin-hole.
  - Test 13 has a dedicated subclause 4.7 "Rectangular wire", with 4.7.1 at room temperature and 4.7.2 at elevated temperature.
  - Specimen arrangements in the figure list: cylinder, twisted specimen, U-bend specimen in metal shot, coil-wound specimen. Table 1 gives rates of voltage increase.
- **IEC 60851-5:2026 (Edition 5.0, published 2026-08-13)** — [technickenormy listing of IEC 60851-5:2026 RLV](https://www.technickenormy.cz/en/iec-60851-5-2026-rlv-winding-wires-test-methods-part-5-electrical-properties/)
  - Replaces 2008+AMD1+AMD2.
  - Cylinder-method loads now cover a wider conductor size range (5.3.1/5.3.2).
  - New 6.5: inline continuity testing for rectangular wire, marked "under consideration".
  - No PD test is listed.
- **IEC 60851-6 (Edition 3.0, 2012-05; flag: older).**
  - Test 9, heat shock: "the potential of the wire to withstand temperature exposure after the wire has been stretched and/or wound or bent around a mandrel", with a specific rectangular-wire specimen (3.2.2).
  - Test 10, cut-through: enamelled round wire only.
  - Test 15: temperature index.
  - Test 21: loss of mass (round).

  — [IEC 60851-6 Ed.3.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-6%7Bed3.0%7Db.pdf)
- **IEC 60851-4 (Edition 3.0, 2016-07).**
  - Test 12, solvents: pencil-hardness method.
  - Test 16, refrigerants: revised, with Annex A on alternatives to R22.
  - Test 17: solderability.
  - Test 20, resistance to hydrolysis and to transformer oil: has a separate rectangular-wire procedure (6.3).

  — [IEC 60851-4 Ed.3.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-4%7Bed3.0%7Db.pdf)
- **IEC 60172:2020 (Edition 5.0, 2020-11).**
  - Temperature index = temperature from the Arrhenius life-vs-temperature plot extrapolated "to a lifetime of 20 000 h".
  - Follows IEC 60216-1 and covers enamelled wire (varnished or not) and tape-wrapped round and rectangular wire, in air at atmospheric pressure, using periodic AC proof-voltage tests.
  - 5.1.2 gives specimen preparation for enamelled or tape-wrapped rectangular wire; Table 4 gives proof voltages for rectangular wire.
  - Replaces the 2015 edition.

  — [IEC 60172 Ed.5.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60172%7Bed5.0%7Db.pdf)
- **IEC 60216-1 (Edition 6.0, 2013-03; flag: older).** Defines the temperature-index concept (usually 20 000 h) and the halving interval (HIC) — [IEC 60216-1 Ed.6.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60216-1%7Bed6.0%7Db.pdf)
- **Industry use of non-IEC procedures (Essex patent, priority 2014):**
  - NEMA MW 1000-2012 procedure 3.3.6 flexibility: 1 m sample bent at least about 90° around a 4.0 mm mandrel, inspected for cracks, then retested.
  - ASTM D1676-03 "oil bomb", typically at 150 °C for about 2 000 h, followed by dielectric, PDIV and visual crack checks.
  - ASTM 2307 thermal endurance at 1 000 / 5 000 / 20 000 h; continuous use up to about 220 °C, possibly 230–240 °C.
  - JIS C 3216-6:2011 softening/cut-through: about 300–400 °C before a short.

  — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- **JIS C 3216-3 §5.4 twist delamination test.** 50 cm specimen, one end fixed, twisted under a constant 100 N load; ratings are ≥ 30 twists (A) and 10 to < 30 twists (B) — [US11232885B2](https://patents.google.com/patent/US11232885B2/en)
- **JIS C 3003.** §7 flexibility and §8.1 b) torsion adhesion, with ≥ 15 torsion rounds rated good — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)
- **Example hairpin-wire specification (Stuttgart).** PAI, Grade 3, about 100 µm, temperature index ≥ 220 °C, heat shock ≥ 240 °C, rated 800 V — [He et al., Energies 2025](https://d-nb.info/1376542846/34)

### Inferences
- **Use IEC 60317-0-2 as the template.** Its clause structure (Tests 4–23) can serve as the backbone of a coating-agnostic test list for all candidate coatings. Five items must be added from other sources:
  - PDIV/RPDIV (from IEC 60034-18-41, IEC 60270 and IEC TS 61934);
  - abrasion/scrape for rectangular wire (IEC 60851-3 Test 11 is round-wire only);
  - cut-through for rectangular wire (IEC 60851-6 Test 10 is round-wire only; JIS C 3216-6 is the industry route);
  - ATF/oil compatibility;
  - post-forming electrical tests.
- **Extruded and non-enamel coatings need agreed requirements.** Extruded PEEK, PEEK tube or heat-shrink, Kapton tape, epoxy powder and parylene are not "enamelled" wire under IEC 60317-0-2. The team should state that the IEC 60851 test methods are applied "by analogy", and agree test levels such as breakdown voltage per thickness, since the Table 8 grade limits do not apply.
- **Track the new 60851-5 edition.** IEC 60851-5:2026 is brand new. Any contract or test plan should state which edition (2019 CSV or 2026) is used for breakdown and continuity.

### Gaps
- The numerical tables of IEC 60317-0-2 were not accessible: Table 7 (mandrel diameters for flatwise/edgewise winding), Table 8 (minimum breakdown voltages by grade) and the heat-shock and solvent requirements.
- The exact IEC 60851-5 §4.7 rectangular-wire breakdown procedure (electrode type and bending) was not accessible.
- The current edition of NEMA MW 1000 could not be verified (the NEMA page redirected to a store). Only MW 1000-2012 is cited (in a 2014 patent).
- The current editions of JIS C 3216 parts could not be verified; the patents cite JIS C 3216-6:2011.
- No IEC/IEEE document specific to extruded or "inverter-duty" rectangular wire was found. This could not be checked further after the search budget ran out.
- Whether IEC 60851-6 has amendments after 2012 was not verified; VDE has no Ed. 3.1 preview.

---

## 3. Specimen geometries for PDIV and breakdown of rectangular / hairpin wire, and how geometry affects PDIV

### Takeaway
Four specimen families are documented:
- **Wire-pair specimens.** Two rectangular wires with flat faces pressed together (150 mm contact), or one bent wire clipped to a second at a controlled force (7.8 N). Used for material PDIV screening.
- **Wire-to-ground specimens.** Metal foil, metal shot (U-bend) or cylinder electrodes. Used for breakdown.
- **Twisted pairs.** Round wire, IEC 60851-5 / IEC 60034-18-41.
- **Hairpin-in-slot formettes and motorettes.** Used for RPDIV and ageing.

PDIV is set by the air wedge next to the contact line (Paschen/streamer inception). It is therefore sensitive to:
- contact geometry and pressing force;
- corner radius;
- surface moisture;
- air density.

Contact length and force must therefore be fixed in the test plan.

### Cited Findings
- **Qualification test objects in IEC 60034-18-41.** "twisted pair or equivalent arrangement", "motorette" (special test model for random-wound windings) and "formette" (for form-wound windings), as well as complete windings — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
- **Rectangular wire pair for PDIV (Furukawa).** "Two insulated wires with their long flat faces in close contact over 150 mm, with no gap". AC 50 Hz, ramp 50 V/s, PDIV read at 10 pC, measured at 25 °C and 250 °C with a Kikusui KPD2050 — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)
- **Breakdown specimen for rectangular wire (Furukawa).** Metal foil wrapped on the wire; 50 Hz AC at 500 V/s with a 5 mA trip, reported as r.m.s., at 25 °C and 250 °C — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)
- **Bent-wire clip specimen (Nagoya).** One rectangular wire bent and held against a second with a plastic clip at 7.8 N, "low enough to avoid deformation of coatings". Test setup:
  - 200 pF coupling capacitor and CR detection, calibrated with a charge pulse generator;
  - specimens cleaned with alcohol and conditioned in a thermo-hygrostat;
  - PD location observed with a high-sensitivity camera; at 20 % RH PDs sat near the contact point of the wires.

  — [Wakimoto et al. 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf)
- **IEC 60851-5 breakdown electrodes.** Cylinder, twisted specimen, U-bend specimen in metal shot, coil-wound specimen; rectangular wire has its own subclause (4.7) — [IEC 60851-5 Ed.4.2 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-5%7Bed4.2%7Db.pdf)
- **Hairpin-in-slot emulation (formette).** One 300 mm hairpin (4 × 2 mm, PAI ≈ 100 µm) in a slot. It is "the most economical option" for statistically significant ageing, but "does not fully replicate the complex electromagnetic, thermal, and mechanical conditions of real motors" — [He et al., Energies 2025](https://d-nb.info/1376542846/34)
- **Specimen types in the 2024 review.**
  - The twisted pair, following IEC 60851-5, is the most common specimen in electrical ageing tests, and specimens are usually preconditioned.
  - Thermal-ageing specimens include a formette for hairpin windings and a motorette for double-layer windings.
  - "Compared to specimens, such as motorettes and twisted pairs, coils exhibit a shorter lifetime."

  — [Zhou et al., Energies 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)
- **Physics of inception.** "The PDIV corresponds to the minimum voltage to break the air gap in a twisted pair". FEM with a streamer criterion (K = 6) was calibrated on twisted pairs of different diameters and insulation thicknesses. The enamel-thickness benefit falls at low pressure (16 % → 8.7 %) — [Part III](https://zenodo.org/records/4562202)
- **PDIV models.** Using the straight-line gap distance instead of field-line paths gives PDIV errors of about 2–5 % in the literature. A permittivity-only (Dakin) model reaches about 27 % error at 180 °C, while an air-density (Lusuardi) model stays within about 10–12 %.

  The measurement template in that study:
  - AC 50 Hz, ramp 10 V/s;
  - PD threshold 0.05 nC (= 50 pC), set at ≥ 2 × background noise per UNE-EN 60270;
  - 5 fresh samples × 3 measurements, 60 s apart to avoid memory effects;
  - 10 min soak at temperature;
  - lab RH 45–60 %.

  — [Elorza Azpiazu et al. 2023](https://mdpi-res.com/d_attachment/applsci/applsci-13-02417/article_deploy/applsci-13-02417.pdf)
- **Round-wire industry variant (Proterial).** Twisted-pair PDIV at 23 °C and 50 % RH, 50 Hz, ramp 10–30 V/s; PDIV is the voltage at which a 50 pC discharge occurs 50 times. Breakdown voltage is measured on twisted pairs at 50 Hz up to 20 kV in air — [US12100532B2](https://patents.google.com/patent/US12100532B2/en)

### Inferences
- **Two complementary rectangular-wire PDIV specimens.**
  - Flatwise "back-to-back" pairs (broad faces in contact over a fixed length such as 150 mm, under a defined clamp force): these represent conductors stacked radially in a hairpin slot.
  - Edgewise pairs (narrow faces in contact): these involve the corner radii.

  The air wedge at the contact line, and therefore PDIV, depends on corner radius, flatness and clamp force. Specify force (for example in N, as Nagoya's 7.8 N), contact length, cleaning and RH conditioning. Report both orientations, because a hairpin slot presents both.
- **Conductor-to-ground arrangements.** Foil, metal shot or a grounded slot-steel mock-up can be used. The PDIV of a single-coated conductor against ground has one air wedge and one insulation layer. A wire pair has two layers in series, so a wire-pair PDIV is not directly comparable with conductor-to-ground PDIV. The test plan should use the geometry that matches the stress being qualified: wire pair for T/T, conductor-to-plate or slot mock-up for P/G.
- **Bent and processed specimens.** U-bend crown, twisted leg and the weld-adjacent end should be tested as formettes. Forming strains and laser-stripping edges are where coatings are most likely to crack (see §4 and §6). A straight-pair PDIV alone would overestimate in-stator performance.

### Gaps
- No published systematic comparison of edgewise vs flatwise contact PDIV for hairpin wire was retrievable. The Naderiallaf et al. fillet-radius study (IEEE) appeared only as a search result and could not be opened.
- No standardized clamp force or contact length for rectangular wire pairs exists in the IEC documents examined.
- No data were found on PDIV at the U-bend crown, twist zone or weld zone of real hairpins.

---

## 4. Mechanical / forming tests relevant to hairpin manufacturing (edgewise/flatwise bending, twisting, pre-elongation then breakdown, scrape/abrasion, adhesion, springback, slot insertion)

### Takeaway
IEC 60851-3:2023 provides elongation, springiness, mandrel winding and adherence tests for rectangular wire, but no abrasion test for it. Hairpin-relevant severities come from wire-maker practice:
- 180° bend around a 1.0 mm core with a deliberate 5 µm scratch;
- 90° bend over a 4.0 mm mandrel (NEMA);
- twist delamination under 100 N (JIS C 3216-3), with ≥ 30 twists rated best;
- torsion adhesion ≥ 15 rounds (JIS C 3003);
- pre-strain of 1 % (for heat ageing) or 20–30 % before electrical or crack checks.

Overly thick extruded layers (PEEK 185–212 µm) can fail a wind-and-heat test.

### Cited Findings
- **IEC 60851-3:2023 tests.**
  - Test 6, elongation: (5 ± 1) mm/s, 200–250 mm free length.
  - Test 7, springiness: separate method for round > 1.6 mm and rectangular wire.
  - Test 8, flexibility and adherence: mandrel winding with a rectangular-wire subclause; adherence test for enamelled rectangular wire; peel only for round wire > 1.0 mm.
  - Test 11, abrasion (unidirectional scrape): enamelled round wire only.
  - Test 18, heat bonding: includes rectangular.

  — [IEC 60851-3 Ed.4.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-3%7Bed4.0%7Db.pdf)
- **IEC 60317-0-2 requirements.** Springiness applies only to wire with nominal proof strength ≤ 80 N·mm⁻². Flexibility and adherence use mandrel winding (Table 7) and a revised adherence test (8.2) — [IEC 60317-0-2 Ed.4.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-2%7Bed4.0%7Db.pdf)
- **Heat shock in IEC 60851-6.** Tests the wire's ability to withstand temperature exposure "after the wire has been stretched and/or wound or bent around a mandrel", with a rectangular-wire specimen (3.2.2) — [IEC 60851-6 Ed.3.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-6%7Bed3.0%7Db.pdf)
- **Essex Furukawa bending and twist tests** — [US11232885B2](https://patents.google.com/patent/US11232885B2/en)
  - Bending (conductor adhesion): a 300 mm straight specimen gets a scratch about 5 µm deep and 2 µm long on the edge surface. It is bent 180° around a 1.0 mm iron core and held 5 min, repeated 5 times, and delamination is checked by eye. Ranking runs from no delamination (best) to delamination in 1, 2 or ≥ 3 of 5 trials.
  - Twist (interlayer adhesion): JIS C 3216-3 §5.4, 50 cm, 100 N load; A ≥ 30 twists, B 10 to < 30 twists.
  - A wire passes only if rated B or better on every item.
  - Comparative examples with a 2 µm innermost imide layer failed conductor adhesion (rank D). The preferred innermost layer is 5–10 µm, about 5–10 % of the thermoset stack.
- **NEMA MW 1000-2012 §3.3.6 flexibility.** 1 m sample, bent at least about 90° around a 4.0 mm mandrel, inspected for cracks and retested (flag: 2012 edition) — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- **Furukawa forming-related tests.**
  - JIS C 3003 §7 flexibility; torsion adhesion per JIS C 3003 §8.1 b), with ≥ 15 rounds rated good.
  - A "dielectric breakdown test after winding on iron core and heating": PAI 40 µm + PEEK 185–212 µm (225–252 µm total) failed it, while totals of 51–206 µm passed.

  — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)
- **Pre-elongation checks.**
  - Essex Furukawa: heat ageing at 220 °C for 1 000 h under 1 % extension; no surface cracks allowed — [US11232885B2](https://patents.google.com/patent/US11232885B2/en)
  - Proterial (round wire): 30 % elongation, then wound around its own diameter for 50 turns; no film cracks allowed — [US12100532B2](https://patents.google.com/patent/US12100532B2/en)
- **Vendor claim (Victrex).** XPI PEEK has "at least 2x tighter bending radius capability vs enamel"; coating is typically 80–300 µm vs 5–100 µm for enamel (no absolute radii or test conditions given) — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions)
- **Process context.**
  - Hairpin cross-sections typically have edge lengths of 2–4 mm. Hairpins are inserted into the slots with compressed air, and protruding ends are twisted together ("necking") or fixed before welding — [TRUMPF hairpin white paper (undated)](https://www.apricon.fi/wp-content/uploads/trumpf-whitepaper-hairpin-welding-e-motors-en.pdf)
  - A hairpin qualification study used a vibration shaker on specimens inside a ventilated oven, so that mechanical and thermal stress acted simultaneously — [Zhou et al., Energies 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)

### Inferences
- **Proposed "forming-then-electrical" chain for every coating.** No single standard defines this; it is assembled from the cited elements.
  1. Pre-elongation of 1–30 % (IEC 60851-3 Test 6 rig).
  2. Flatwise and edgewise 180° bends over a set of mandrels, for example down to 1.0 mm as in the patent, plus the actual crown radius of the hairpin design.
  3. Twist delamination under 100 N (JIS C 3216-3).
  4. Heat shock at ≥ 240 °C (as in the Stuttgart specification).
  5. Then breakdown voltage (foil or metal shot) and PDIV (wire pair) on the deformed zone.

  Pass/fail is no visible crack at the specified magnification, plus retention of breakdown voltage and PDIV against the straight reference.
- **Thickness has an upper limit for formability.** The Furukawa results suggest that very thick extruded layers are not automatically better: more than about 200 µm total failed wind-and-heat. Coatings applied as tube or heat-shrink should be bent after application to check for wrinkling and lift-off at the crown.

### Gaps
- No standardized edgewise/flatwise mandrel diameters for hairpin wire were found: IEC 60317-0-2 Table 7 was not accessible, and no public OEM forming specification was found.
- No published slot-insertion simulation test (insertion force, abrasion against slot liner, PDIV after insertion) was found.
- No IEC scrape/abrasion test for rectangular wire exists in IEC 60851-3:2023. The NEMA unilateral scrape applicability to rectangular wire was not verified.
- Springback values or acceptance limits for rectangular wire were not obtained.

---

## 5. Thermal, environmental and chemical tests (thermal endurance 200–240 °C, thermal shock/cycling, damp heat, ATF/oil and hydrolysis) and multi-stress ageing

### Takeaway
- **Thermal endurance.** Assessed by IEC 60172:2020 / IEC 60216-1, giving a temperature index at 20 000 h. Hairpin wires are specified around TI ≥ 220 °C and heat shock ≥ 240 °C. Accelerated ageing at 220–230 °C reduces both PDIV and insulation thickness.
- **ATF compatibility.** Industry tests are sealed-vessel immersions:
  - 150 °C for 500 h with 0.5 mass% water;
  - 150 °C for 1 000 h with 0.2 wt% water;
  - 200 °C for 1 000 h;
  - an oil bomb at 150 °C for about 2 000 h.

  Each is followed by a tight bend (180° around 1.0 mm), crack inspection, permittivity, PDIV or dielectric checks.
- **Multi-stress qualification.** Follows IEC 60034-18-21 sub-cycles (thermal, mechanical, ambient), each followed by a PD-proof test per IEC 60034-18-41.
- **Not found.** No source was found for specific thermal-shock (−40/+180 °C) or damp-heat (85 °C / 85 % RH) protocols for hairpin insulation.

### Cited Findings
- **Temperature index.** IEC 60172:2020 defines TI by extrapolation to 20 000 h under periodic AC proof-voltage tests, with specimen preparation for rectangular wire (5.1.2) and proof voltages for rectangular wire (Table 4) — [IEC 60172 Ed.5.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60172%7Bed5.0%7Db.pdf); [IEC 60216-1 Ed.6.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60216-1%7Bed6.0%7Db.pdf)
- **Thermal class references (with conflict).**
  - A Grade 3 PAI hairpin wire (≈ 100 µm) is specified with TI ≥ 220 °C and heat shock ≥ 240 °C — [He et al., Energies 2025](https://d-nb.info/1376542846/34)
  - Victrex claims XPI PEEK is "Class 220°C (vs. 180°C for PAI enamel)" and operates "from -40°C up to 260°C" — [Victrex](https://www.victrex.com/en/emotor-solutions)
  - These conflict on the class of PAI hairpin enamel: ≥ 220 °C in the Stuttgart specification vs 180 °C in the vendor comparison.
- **Ageing at 220–230 °C.**
  - Class-200 winding wires aged at 230 °C showed a simultaneous reduction of PDIV and insulation thickness — [Part III](https://zenodo.org/records/4562202)
  - Essex Furukawa: 220 °C for 1 000 h at 1 % extension, no surface cracks allowed — [US11232885B2](https://patents.google.com/patent/US11232885B2/en)
  - Furukawa: wound specimen at 190 °C for 1 000 h, checked for cracks in enamel or extruded layer — [US9224523B2](https://patents.google.com/patent/US9224523B2/en)
  - Essex: thermal-endurance durations of 1 000 / 5 000 / 20 000 h per ASTM 2307, and continuous use up to about 220 °C — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- **Operating-temperature envelope.** Winding insulation typically sees 40–160 °C in normal operation "and can exceed 180 °C in extreme scenarios" — [He et al., Energies 2025](https://d-nb.info/1376542846/34)
- **ATF test, Essex Furukawa (rectangular wire).**
  - A 300 mm straight specimen is placed in a closed stainless-steel (SUS) vessel with 1 300 g ATF and 6.5 ml water (0.5 mass%), at 150 °C for 500 h.
  - After cooling to 25 °C it is bent 180° around a 1.0 mm iron core and inspected by eye for cracks.
  - The PEI 9 µm + thermoset 90 µm + PEEK 60 µm example rated A; all-thermoset examples rated B.

  — [US11232885B2](https://patents.google.com/patent/US11232885B2/en)
- **ATF test, Proterial (round wire).**
  - Specimen 25 cm, fully immersed in ATF with 0.2 wt% water, at 150 °C for 1 000 h. Further examples were immersed, wiped and then held at 200 °C for 1 000 h.
  - Checks: surface cracks under about 5× magnification, and relative permittivity at 1 kHz after a 150 °C / 1 h dry-out, using silver-paste electrodes (100 mm main and 10 mm guards).
  - Pass: no crack and no change in permittivity.

  — [US12100532B2](https://patents.google.com/patent/US12100532B2/en)
- **Oil bomb, Essex.** ASTM D1676-03 "oil bomb", typically 150 °C for about 2 000 h, followed by dielectric, PDIV and visual crack checks (flag: 2014 patent) — [US9324476B2](https://patents.google.com/patent/US9324476B2/en)
- **Vendor ATF claim.** Victrex says XPI PEEK "withstands a wide range of ATFs and dielectric fluids at 180°C for up to 2,000 hours" with electrical properties retained. It also says PDIV stays stable after thermal cycling but gives no figures — [Victrex](https://www.victrex.com/en/emotor-solutions)
- **ATF compatibility of non-wire materials (elastomers).** ASTM D7216-15 ageing at 100 °C for 168 h, extended to 336/504/672 h, measuring volume, hardness, tensile strength and elongation at break. Limits come from Ford Mercon V, Allison TES 439/389 and GM Dexron VI. FKM and silicone showed high or medium compatibility; EPDM showed low compatibility — [García-Tuero et al., Appl. Sci. 2022, 12, 6213 (PDF)](https://mdpi-res.com/d_attachment/applsci/applsci-12-06213/article_deploy/applsci-12-06213.pdf)
- **Hydrolysis / oil.** IEC 60851-4 Test 20 "Resistance to hydrolysis and to transformer oil" has a separate rectangular-wire procedure (6.3), and Test 16 covers refrigerants — [IEC 60851-4 Ed.3.0 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60851-4%7Bed3.0%7Db.pdf). IEC 60317-0-2 also lists "Resistance to transformer oil" (Clause 20) — [IEC 60317-0-2 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60317-0-2%7Bed4.0%7Db.pdf)
- **Humidity in the PD framework.** IEC 60034-18-41 AMD1 states that humidity can shift PDIV/RPDIV "in both directions" and that a further enhancement factor could be applied — [AMD1 preview](https://cdn.standards.iteh.ai/samples/23527/a1d9bbea464c4242a53f644c696783a0/IEC-60034-18-41-2014-AMD1-2019.pdf). PDIV instability at 90 % RH on rectangular wire is described in §1.4 — [Wakimoto 2016](https://nagoya.repo.nii.ac.jp/record/24052/files/IEEE-TDEI-2015-proofread.pdf)
- **Multi-stress qualification.**
  - Qualification "comprise[s] sub-cycles where aging factors (thermal, mechanical, ambient) are applied sequentially (or simultaneously, if workable)". IEC 60034-18-21 is the reference, and a PD-proof test follows each sub-cycle — [Part III](https://zenodo.org/records/4562202)
  - IEC 60034-18-41 qualification uses IEC 60034-18-21/-31 sequences plus a high-frequency voltage test and a PD test — [18-41 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf)
  - Ovens hold ±3 °C; IEC 60505 allows mechanical stress to be combined with thermal stress; a hairpin qualification combined vibration (shaker) with oven ageing; diagnostics every 24/48 h — [Zhou et al., Energies 2024](https://mdpi-res.com/d_attachment/energies/energies-17-01987/article_deploy/energies-17-01987.pdf)
  - An electro-thermal design-of-experiments study on hairpin-in-slot specimens (PWM, 20–210 °C, 675–975 V, ≥ 250 h) found a significant interaction between electrical and thermal stress — [He et al., Energies 2025](https://d-nb.info/1376542846/34)

### Inferences
- **Thermal ageing for comparison.** A practical comparative programme uses at least three ageing temperatures, for example 220 / 240 / 260 °C for PEEK and PI-class coatings. This is consistent with IEC 60172's 20 000 h extrapolation and the 220–230 °C ageing points used above. At each ageing step, the diagnostic should be PDIV (wire pair, at RT and at maximum temperature) and thickness, not only AC proof voltage, because PDIV and thickness both decline with thermal ageing.
- **ATF test conditions.** For oil-cooled e-axles, the literature supports a sealed-vessel ATF test at 150 °C for 500–2 000 h with controlled water content (0.2–0.5 mass%). Severity can be raised to 180–200 °C for PEEK-class coatings. Post-exposure checks should include: a 180° bend over a small core with crack inspection, permittivity at 1 kHz, PDIV and breakdown, and adhesion. The specific ATF and its water content should match the customer's e-axle fluid.
- **Damp heat and thermal shock.** These were not found in hairpin-specific sources. The team will need OEM or component-level specifications, for example automotive environmental standards for e-drive components. Report them in the test plan as "OEM-defined" rather than literature-backed values.

### Gaps
- No public source found for hairpin-insulation thermal-shock or thermal-cycling profiles (e.g., −40/+180 °C, number of cycles) or for damp heat (85 °C / 85 % RH, hours) with acceptance criteria.
- No peer-reviewed study was retrieved that reports PDIV or breakdown of enamelled vs PEEK rectangular wire after ATF ageing with water content and temperature stated. Only patents and vendor claims were available.
- IEC 60851-4 Test 20 conditions (water content, temperature, duration for rectangular wire) were not accessible.
- No hairpin-specific TEAM (thermal–electrical–ambient–mechanical) sequence with numerical sub-cycle parameters was obtained. The Mancinelli/Stagnitta/Cavallini "Qualification of Hairpin Motors Insulation for Automotive Applications" (IEEE TIA 2017) full text was not accessible.

---

## 6. Weld and stripping zone: laser/mechanical stripping quality and heat-affected-zone damage after laser/TIG welding

### Takeaway
Laser stripping (CO2 for bulk removal, plus a ns fibre, UV or fs pass) is the dominant process. Documented quality issues are:
- residual polymer or carbon (even a 1–2 µm layer weakens welds);
- carbonised or burred coating edges, especially for PEEK;
- copper discoloration (which does not affect processing).

Reported quality metrics:
- fluorescence below 9 RFU (vendor benchmark);
- residual-carbon analysis;
- weld peel strength (315 N bare-copper reference; 262–409 N depending on stripping laser).

On the heat-affected zone, one patent states that a PI coating's characteristics may change at ≥ 500 °C while welding runs at ≥ 950 °C. It recommends a stripped length of 4–7 mm. No peer-reviewed measurements of insulation damage next to hairpin welds were found.

### Cited Findings
- **Common coatings and process (TRUMPF, undated white paper; flag: date unknown).**
  - Common hairpin coatings: PAI, PEEK and "PAI+FEP"; PAI still has "the largest share by far", with a trend toward PEEK and PAI+FEP.
  - Laser stripping is up to 80 % more productive than planing or milling, and 40–80 % faster than mechanical processes.
  - PEEK behaves as a volume absorber; for PAI, the first pass should carbonise the material to increase absorption.
  - Copper discolours from process heat, but this "is not relevant for the further processing" because the copper structure does not change.
  - Burrs form at the boundary with the coated copper.
  - PEEK ablation shows carbonisation at the boundary of the process window; reworking with a femtosecond laser improves edge quality.
  - Removal rates: PAI up to 13 cm²/s (average 7 cm²/s); PEEK 4 cm²/s.
  - Tilted (60°) optics risk leaving residues on the sides not facing the optics.
  - Maximum ablation lengths quoted for the different laser set-ups: 56 mm, 110 mm and 50 mm.
  - Welding depth is 2–3 mm, and residues should be cleaned off (e.g., by suction) before welding.

  — [TRUMPF white paper](https://www.apricon.fi/wp-content/uploads/trumpf-whitepaper-hairpin-welding-e-motors-en.pdf)
- **Residue limits (Novanta, 2023-09-03; vendor).**
  - A 400 W CO2 laser (10.6 µm, or 9.3 µm depending on chemistry) removes the bulk; a 200 W ns fibre laser removes the residual "1-2 µm layer".
  - "A single micron of insulation residue on the copper produces weak welds."
  - Benchmark of fewer than 9 RFU fluorescence on four hairpin designs.
  - ATR-IR spectroscopy is used to select the wavelength.
  - Cycle time under 1.0 s.

  — [Novanta white paper summary](https://novanta.com/precision-manufacturing/resources/whitepapers/unlocking-efficiency-in-electric-motors-the-power-of-hairpin-stripping/)
- **Comparative laser-stripping study (Politecnico di Milano / IMA Automation, reported 2025-07-03).**
  - Specimen: Cu-ETP hairpin 3.87 × 2.66 mm with 95 µm PAI enamel.
  - Seven stripping set-ups were compared: CO2 at 10.6 and 9.36 µm, ns fibre at 1.064 µm, disk at 1.03 µm, green at 0.532 µm, UV at 0.355 µm, and CO2 followed by NIR. Welding used a 6 kW fibre laser at 1.07 µm.
  - Residual carbon: the 10.6 µm CO2 laser left about 8× more carbon than UV; CO2 + NIR left the least.
  - Weld peel strength: bare copper 315 N average; CO2 at 10.6 µm 262 N; CO2 + NIR 409 N; overall range 150–600 N.
  - Small pores came from trapped polymer gases.
  - Inspection used optical/SEM microscopy, surface chemistry (residual carbon), peel tests and fracture analysis.
  - The article does not address heat-affected-zone effects on adjacent insulation.

  — [ASSEMBLY magazine](https://www.assemblymag.com/articles/99369-laser-stripping-of-magnet-wire)
- **Heat near the weld (LG Magna e-Powertrain patent US12068636B2, priority 2020).**
  - The PI coating's characteristics "may change at a high temperature of 500 °C or higher"; welding is done at ≥ 950 °C.
  - Recommended stripping length is 4–6 mm at ≥ 900 °C welding and 5–7 mm at ≥ 950 °C, kept as short as possible but balanced against damage to the adjacent coating.
  - The patent describes no test of coating damage.

  — [US12068636B2](https://patents.google.com/patent/US12068636B2/en)

### Inferences
- **Weld- and strip-zone test items for the campaign.** Assembled from the cited elements:
  1. Stripped-surface cleanliness: fluorescence (RFU), FTIR/ATR or residual-carbon analysis, and SEM.
  2. Coating-edge quality at the strip boundary: carbonisation width, burrs, delamination or lift-off, checked by cross-section microscopy.
  3. Stripped-length tolerance, for example within the 4–7 mm window above.
  4. Thermal exposure of the coating during welding: thermocouple or IR measurement at defined distances from the weld, judged against the coating's degradation onset (≥ 500 °C cited for PI).
  5. Electrical checks on welded formette ends: PDIV between adjacent welded pairs, and breakdown or PDIV of the coating within the first few mm from the strip edge.
  6. Weld peel/tensile strength as a process check.
- **Coating-dependent behaviour.** Thermoplastic coatings such as PEEK (volume absorber, carbonising edges) and heat-shrink or tube coatings may melt-back or retract near the weld differently from thermoset PAI/PI. Coating retraction or edge-lift length after welding is therefore a useful comparative metric. This is my inference; no source measured it.

### Gaps
- No peer-reviewed data were found on heat-affected-zone damage to hairpin insulation (PAI, PEEK, tapes, powder or parylene) after laser or TIG welding. This includes coating temperature vs distance and post-weld PDIV.
- No standard acceptance criteria for stripping residue or edge quality were found. Fluorescence < 9 RFU and the "1 µm residue" statement are vendor-reported.
- No data were found on mechanical stripping (milling, scraping) quality checks, or on how stripping method affects PDIV at the strip edge.
- TIG-welding-specific information was not found; all sources concern laser welding.
