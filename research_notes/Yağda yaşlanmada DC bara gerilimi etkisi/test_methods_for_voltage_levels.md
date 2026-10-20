# Test methods, equipment and test-matrix design for adding 800 V, 1200 V and 1600 V DC-bus classes to an oil-ageing study of hairpin/rectangular-conductor insulation

How to read these notes. They build on lines 340–385 of `reports/Hairpin izolasyon malzemeleri ve yöntemleri.md`. That report already lists AC PDIV on wire pairs, RPDIV after He et al. 2025, P/G on a plate or slot model, breakdown, the forming chain, ATF + water tests, V–t under PD and the electro-thermal formette example (PWM 1 kHz, 675–975 V, 20–210 °C, ≥250 h). Those items are not repeated here. These notes add the following:
- how voltage-class targets are derived;
- what changed in IEC TS 61934:2024 and what IEC TS 60034-27-5:2021 contains;
- equipment limits for the 1600 V class;
- how specimens are handled after oil ageing;
- matrix designs that keep the specimen count low;
- safety.

Each citation is tagged with how much of the source I read:
- **[full text]**: I read the whole document. Some of these were PDFs downloaded to the scratchpad; this is noted where it applies.
- **[preview]**: the official standard preview, which covers only the TOC, scope, definitions and first clauses.
- **[product page]**: a manufacturer's product page or brochure.
- **[abstract]**: the abstract only.
- **[search snippet]**: only the search-engine excerpt. The page was not opened or was blocked.

All values that I calculated are labelled as my own inference.

## 1. How are PDIV and RPDIV measured under repetitive impulse/PWM-like voltages (waveform, rise time, polarity, repetition rate, ramp, PD detection, noise filtering, thresholds, specimen numbers, statistics)?

### Takeaway
The governing documents are IEC TS 61934:2024 (generic, TC 112) and IEC TS 60034-27-5:2021 (windings, TC 2). Both define RPDIV as the minimum peak-to-peak impulse voltage at which more than 5 PD pulses occur on 10 impulses, which is in effect a 50 % PD-probability point. The voltage is raised and lowered as step-by-step trains of impulses.

The 2024 edition of IEC TS 61934 brings the generator specification in line with wide-bandgap devices, with rise times down to 20 ns, and prefers bipolar impulses. It drops charge-based (pC) measurement, so impulse-PD readings are now reported in mV after a mandatory sensitivity and noise check. Detection uses UHF antennas, HFCTs or coupling capacitors with high-order filters. Results depend strongly on temperature, humidity and pressure, so these must be fixed and reported.

The voltage a specimen must reach without PD comes from the IEC 60034-18-41 enhancement-factor chain, applied per insulation path. Only these targets change between 800, 1200 and 1600 V buses; the measurement method stays the same.

### Cited Findings
**Definitions and procedure**
- IEC TS 61934:2024 (Ed. 3.0, 2024-01, TC 112) defines RPDIV as the "minimum peak-to-peak impulse voltage at which more than five PD pulses occur on ten voltage impulses of the same polarity". RPDEV is the maximum peak-to-peak voltage at which fewer than five PD pulses occur on ten impulses, found while the voltage decreases. Both are mean values for a specified test time — [IEC TS 61934:2024 redline preview, iTeh](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- IEC TS 61934:2024 lists the significant changes from the 2011 edition:
  - added background on wide-bandgap devices;
  - impulse-waveform parameter values modified to reflect wide-bandgap devices;
  - charge-based measurements and source-controlled gating are no longer described;
  - the bibliography is deleted.
  — [IEC TS 61934:2024 redline preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]; webstore listing: [IEC TS 61934:2024](https://webstore.iec.ch/en/publication/91294)
- Clause 8 of IEC TS 61934:2024 is "Test procedure for increasing and decreasing the repetitive impulse voltage magnitude". Annex C holds RPDIV round-robin results and Annex D gives noise levels of practical PD detectors. Optical and ultrasonic PD detection are explicitly excluded from the scope — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview; clause 8 text not visible]
- IEC TS 60034-27-5:2021 gives off-line RPDIV/RPDEV practice for windings fed by voltage-source converters. Its contents include:
  - the step-by-step (SBS) method with parameters Us (start voltage), Um (maximum voltage), ΔU (step), Np (impulses per train) and tss (rest time between trains);
  - a conditioning procedure before RPDIV, defined as "pre-application of conditioning voltage before PD test for stable measurement condition" (Fig. 20);
  - calculation of RPDIV/RPDEV "using a 50 % PD probability" (Fig. 30);
  - Table 1, typical impulse parameters that must be reported at the test-object terminals;
  - clause 5.3, threshold level of PD detection (noise vs. disturbance vs. threshold);
  - a round-robin test in Annex A.
  — [IEC TS 60034-27-5:2021 preview, iTeh](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf) [preview: TOC, definitions, clause 4.1; numeric SBS values not visible]. The German adoption DIN IEC/TS 60034-27-5 (VDE V 0530-27-5) was published in 2024-07 — [VDE Verlag](https://www.vde-verlag.de/standards/0500280/din-iec-ts-60034-27-5-vde-v-0530-27-5-2024-07.html) [product page]
- IEC 60034-18-41:2014 defines RPDIV the same way.
  - Type I (PD-free) systems are "generally used in rotating machines rated at 700 V r.m.s. or less".
  - Testing is performed at the extreme value of the chosen overshoot band, with "a default value of 0,3 µs … attributed to the impulse rise time".
  - Converter output rise times "may be in the 0,05 µs – 2,0 µs range".
  - For a 2-level converter, U_dc = U_a (steady-state impulse magnitude).
  — [IEC 60034-18-41:2014 preview, iTeh](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf) [preview]
- Status of IEC 60034-18-41 as of October 2026: the current text is the 2014 edition with AMD1:2019. The IEC page shows Edition 2.0 at stage PCC with a forecast publication date of 2026-05-04, and the European draft prEN IEC 60034-18-41:2025 is listed as "project deleted" (13 Jul 2026) — [IEC webstore](https://webstore.iec.ch/en/publication/32755); [Genorma](https://genorma.com/en/standards/pren-iec-60034-18-41-2025) [search snippets]

**Waveform, rise time, polarity, repetition rate**
- IEC TS 61934:2024 Table 1 gives example impulse parameters without load:
  - rise time 0.02–1 µs (the redline shows 0.04 changed to 0.02);
  - repetition rate 1 Hz–10 kHz;
  - impulse width 0.08–25 µs;
  - shape square or triangular;
  - polarity unipolar or bipolar.

  The text says "rise times as short as 20 ns are exhibited by devices employing wide band gap semiconductor materials". It also says "to simulate the turn-to-turn voltage of a motor driven by a PWM phase voltage, a bipolar repetitive voltage impulse voltage is preferable", with unipolar allowed when bipolar is hard to obtain. A unipolar impulse must have an opposite-polarity oscillation below 20 %. Impulse and PD waveforms must be observed at the test object with an oscilloscope of at least 100 MHz bandwidth, and "PD can occur during the voltage oscillation following the first impulse" — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- The rise-time definition was revised in the 2024 redline. The extracted text contains both the 2011 wording ("0 % to 100 %", estimated as 1.25 × the 10–90 % time) and "10 % to 90 %". IEC TS 60034-27-5 and IEC 60034-18-41 both use 10–90 % — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf); [IEC TS 60034-27-5 preview](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf) [previews; the strike-through could not be resolved in extracted text]
- The waveform depends on the load. "As the capacitance of the sample increases, the rise time of the voltage impulse increases". Inductive and distributed objects add damped oscillations, as shown in IEC TS 60034-27-5 4.2.2 (Figs. 7–13: increased rise time, overshoot, ringing in bipolar tests, slow oscillating decay). IEC TS 60034-27-5 also defines k, the ratio of the distorted to the open-terminal peak-to-peak voltage — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf); [IEC TS 60034-27-5 preview](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf) [previews]
- Hu et al. (2021) studied a 2 kV form-wound coil (170 pF) driven by a 10 kV SiC platform.
  - Shortening the edge from 800 ns to 100 ns lowered PDIV by 6.5 % (3.95 → 3.71 kV at 10 µs pulse width).
  - Repetition rate (1–8 kHz) and duty ratio changed RPDIV by less than 90 V.
  - Bipolar RPDIV was close to unipolar but slightly higher.
  - Sine-PWM (10/60/400 Hz, modulation index 0.1/0.9) changed RPDIV by less than 75 V.
  — [Hu et al., IEEE OJPEL 2021, DOI 10.1109/OJPEL.2021.3069780](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/) [full text]
- He et al. (2025, hairpin-in-slot): RPDIV tends to increase with rise time, but the temperature effect is larger. Going from 70 to 120 ns had minimal effect on RPDIV decline or early breakdowns during ageing — [He, Tenbohlen, Beltle, Energies 18 (2025) 1376, DOI 10.3390/en18061376](https://d-nb.info/1376542846/34) [full text]
- Driendl et al. (2022) argue that IEC 60034-18-41 treats unipolar and bipolar waveforms with the same peak-to-peak value as equivalent. They state that the prescribed test pulse (tr = 0.3 µs ± 0.2 µs) "can not represent the fast switching operation of new generation semiconductors". They used bipolar pulses (800 V DC link, tr 80 ns, 60 kHz, peak 973 V, OF 1.22, 25 kV/µs, ΔU 1773 V) — [Driendl, Pauli, Hameyer, IEEE TIE 69(8) 2022, DOI 10.1109/TIE.2021.3108721](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]

**Ramp and step practice in published work**
- AC PDIV on twisted pairs used 50 Hz, a 1 nF coupling capacitor, an HFCT into a Techimp PDBase II, and 25 V steps of 30 s each at RT and 140 °C. The study notes that for twisted pairs AC and impulse give the same PDIV for a given peak-to-peak voltage, because the potential difference between any two points is the same, while RPDIV exceeds PDIV — [Lusuardi et al., "Part III: Preventing Partial Discharges", IEEE Access 2021, DOI 10.1109/ACCESS.2021.3058090](https://zenodo.org/records/4562202) [full text]
- Impulse RPDIV practice:
  - Hu et al. held each DC-bus level for at least 1 min, recorded RPDIV when PD triggered continuously, otherwise raised by 100–150 V, and repeated each condition 10 times with at least 5 min between conditions — [Hu et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/) [full text]
  - Driendl et al. raised or lowered the voltage manually at about 2 V/s — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]
  - He et al. repeated each RPDIV measurement 10 times — [He et al. 2025](https://d-nb.info/1376542846/34) [full text]

**PD detection and switching-noise suppression**
- Under impulses, the detection system must strongly suppress the residual voltage impulse and must not suppress the PD pulse. The suppression needed rises with test voltage and with shorter rise time, because the spectra overlap (Annex A). Options:
  - UHF (300 MHz–3 GHz) narrow-band detection;
  - ultra-wide-band detection with a high-pass filter;
  - integration of the PD current at very low frequency.

  Readings are in mV, consistent with IEC TS 62478, and "cannot be calibrated in relation to apparent charge in pC". A sensitivity check per clause 7 is mandatory: test diagram, PD detection sensitivity, background noise, detector + generator noise, and a sensitivity report. Coupling devices covered are coupling capacitor + multipole filter, HFCT + multipole filter, electromagnetic couplers and UHF antennas — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- IEC TS 60034-27-5 shows three arrangements: coupling capacitor + higher-order analogue filter, HFCT + higher-order analogue filter (between supply and object, or between object and earth), and an electromagnetic coupler or UHF antenna — [IEC TS 60034-27-5 preview](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf) [preview TOC/figure list]
- Published sensor choices:
  - Hu et al.: two antennas (136–960 MHz), each behind a 500 MHz high-pass filter, into an MDO4104, inside a grounded Faraday shield. A Pearson 2877 HFCT (200 MHz, 50 MHz high-pass) "showed severe oscillations at the rising edge" and missed a falling-edge PD, so it was dropped. Noise was about 2 mV, PD about 5 mV, trigger 2.5 mV — [Hu et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/) [full text]
  - Driendl et al.: Beehive 100-series EMC probe about 0.5 m from the specimen, Tektronix RSA306B spectrum analyser up to 3 GHz. MOSFET switching noise dominated 0–200 MHz and WLAN appeared at 2.4 GHz; PD was clearly separable between these bands. The antenna method gave "the best results in comparison to PD detection by measurement of the current" — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]
  - He et al.: HFCT (10 MHz–1 GHz), then a 290 MHz–3 GHz band-pass and denoising "following IEC 61934". PD appeared at rising and falling edges and also during the high level — [He et al. 2025](https://d-nb.info/1376542846/34) [full text]

**Thresholds**
- Because impulse PD is reported in mV, there is no standard pC threshold for RPDIV. The threshold is set above noise and disturbance (IEC TS 60034-27-5 5.3) after the IEC TS 61934 sensitivity check. AC tests per IEC 60270 still use pC, as summarised in the earlier report — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf); [IEC TS 60034-27-5 preview](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf) [previews]

**Target voltages (enhancement-factor chain)**
- Lusuardi et al.'s reading of IEC 60034-18-41:
  - critical voltage V_c = V_dc · OF · WF · EF_PD · EF_T · EF_Aging;
  - winding factors WF = 2 (P/P), 1.4 (P/G), 0.7 (T/T), "when experimental results or simulations are missing";
  - EF_PD = 1.25;
  - EF_T = 1.3 for T/T and P/P, 1.1 for P/G;
  - EF_Aging = max(1, 1.2·Ts/Tc) for verification tests on new stators, EF_Aging = 1 in qualification tests.

  Qualification tests use sub-cycles per IEC 60034-18-21 with a PD-proof test after each sub-cycle, on "not less than five samples" — [Lusuardi et al. 2021](https://zenodo.org/records/4562202) [full text]
- Driendl et al. give the turn-to-turn test voltage according to the standard as U_test,pk/pk = 2 · a · 0.7 · U_dc · OF · NF · PD · AF · TF. The terms are:
  - a: fraction of the jump voltage across the turn, 0.85 at 80 ns; "for a rise time below 50 ns almost the full jump voltage is stressing the interturn insulation";
  - 0.7: jump-voltage factor;
  - NF = 1.1 (±10 % supply);
  - PD = 1.25 ("PDEV … 25 % lower than the PDIV");
  - AF = 1.2·(1 − (Tclass − Tservice)/Tclass), at most 1.2, type tests only;
  - TF = 1.3 (P/P and T/T).

  For an 800 V system with OF 1.25 they compute 2134 V pk-pk per the standard (maximum EF 1.63). Their ambient-based proposal gives 2867 V pk-pk (EF_amb = 2.19), 34 % higher — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]
- The overshoot-factor (U_p/U_dc) stress categories of IEC 60034-18-41 are Benign 1.1, Moderate 1.5, Severe 2.0 and Extreme 2.5. Stone & Lloyd's example RPDIV targets for a 480 V motor on a 2-level inverter are P/P 1853/2527/3370/4212 V pk-pk and P/G = T/T 1297/1769/2359/2948 V pk-pk — [Stone & Lloyd, PCIC Middle-East 2014-08](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf) [full text; 2014, slightly older than the preferred window]. Driendl et al. add that category A (1.1) "is very hard to reach" with fast semiconductors, and they used OF 1.25 as category B — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]

**Ambient factors, specimens, statistics**
- Driendl et al. measured twisted pairs (Grade 2, 1 mm wire):
  - temperature, 10 specimens: PDIV fell from 982 to 829 V between 20 and 200 °C (−15 %), with the steepest drop between 150 and 200 °C;
  - pressure, 10 specimens: PDIV fell from 972 to 564 V between 1000 and 200 mbar (−42 %);
  - humidity, 5 specimens: largest drop (−24 %) between 60 % and 85 % RH;
  - PDIV/PDEV ratio: ranged 1.02–1.57, cluster near 1.3; mean 1.38 under temperature variation and 1.09 under humidity variation.

  They state that the standard's 1.25 "could underestimate" the PD safety factor — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]
- IEC TS 61934:2024 lists factors that affect PD quantities:
  - temperature, humidity, pressure, ambient gas, contamination;
  - voltage distribution and PD position;
  - previous voltage applications and the time between them;
  - time under stress and ageing.
  — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- Two published ways to turn PDIV distributions into a design value:
  - Weibull B10, the 10th percentile, on twisted pairs. For non-impregnated pairs the B10 PDIV at 140 °C was 10 % lower than at RT — [Lusuardi et al. 2021](https://zenodo.org/records/4562202) [full text]
  - "mean − 3·StdDev" margins against class-specific targets (see Q5) — [HEFT D2.4, 2024](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf) [full text]
- IEC 60034-18-42 lists IEC 62539 (statistical analysis of insulation breakdown data) as a normative reference — [IEC 60034-18-42 Ed. 1.1 preview, VDE](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf) [preview]

### Inferences
- *Inference.* One measurement protocol can serve all three DC-bus classes. Only the pass/fail targets and the voltage range of the source change. Fix the protocol once:
  - bipolar square impulses with 10–90 % rise time ≤100 ns (≈20–80 ns for SiC-like stress), measured at the specimen terminals;
  - repetition rate in the 1–10 kHz Table 1 range;
  - an SBS ramp with fixed ΔU, Np and tss;
  - UHF or band-passed HFCT detection with a threshold set from the sensitivity and noise check.

  Report the RPDIV as the 50 % probability point and the RPDEV on the way down.
- *Inference.* For turn-like capacitive models (back-to-back, twisted pair), AC 50 Hz PDIV reported in V pk-pk is a cheaper screening tool. Lusuardi et al. show that it equals the impulse PDIV for the same peak-to-peak voltage. Reserve impulse RPDIV for a confirmation subset and for formettes, where voltage distribution and impulse distortion matter.
- *Inference.* Because PDIV/PDEV ratios of 1.02–1.57 were measured, record RPDEV for every specimen. Then a class verdict can use either PDIV with EF_PD = 1.25 or PDEV directly.
- *Inference.* Temperature, RH and pressure are each worth 15–42 % of PDIV. Without controlling them, the class verdicts become noise. Use a climate chamber or oven with an RH log, and standardise a pre-measurement conditioning (see Q3).

### Gaps
- I could not read the numeric content of IEC TS 61934:2024 clause 8 (ramp, number of impulses per step) or IEC TS 60034-27-5 SBS values (Us, ΔU, Np, tss), Table 1 and the 5.3 threshold rule. They are paywalled; the previews stop before these clauses.
- I did not read the IEC 60034-18-41 Tables 4, B.2 and B.6 text directly. The stress-category OFs and EF values above come from secondary summaries (Stone & Lloyd 2014; Lusuardi 2021; Driendl 2022). The rise-time limit attached to each stress category was not found.
- No source gives a standard mV PD threshold for impulse RPDIV. Thresholds are laboratory-specific.
- I found no published RPDIV measurement on oil-wetted hairpin specimens under bipolar SiC-like impulses.

## 2. What equipment generates repetitive impulses with SiC-like rise times at amplitudes needed for 1600 V-class buses, and what AC/DC hipot and insulation-resistance equipment and levels are used for 800 V-class motors?

### Takeaway
Commercial impulse PD testers fall into two groups:
- Surge testers (6–15 kV, up to 40 kV with power packs) that report RPDIV/RPDEV but produce damped surges with typical rise times of about 100 ns or more.
- PWM-type "pulse" sources limited to about ±2.5 kV with 150/500 ns rise times.

Published laboratory SiC sources reach 70–100 ns at 3–7 kV, or about 48 ns at 5 kV. None of the verified sources gives ≥±4 kV bipolar with ≤50 ns, which is what IEC-style phase-to-phase targets for a 1600 V bus would need (about 4.6–7.8 kV pk-pk; see Q5). This makes AC PDIV the practical route for high-voltage P/P and P/G margin checks.

For hipot, the formulas in use are of the form 2·U + 1000 V for 1 min: IEC 60034-1 uses the rated rms voltage, and GB/T 18488-2015 uses the maximum working voltage. Insulation resistance limits of ≥20 MΩ appear in Chinese EV-motor documents. ISO 6469-3/UN R100 "high voltage"/class B ends at 1500 V DC, so a 1600 V bus falls outside it.

### Cited Findings
**Standard requirements for the generator**
- IEC TS 61934:2024 requires:
  - short rise time and repetitive impulses with low noise;
  - semiconductor switches allowed in place of sphere gaps;
  - "sufficient electromagnetic shielding" of the generator;
  - a generator designed to deliver the required wave shape to the load.

  Example ranges are 0.02–1 µs rise, 1 Hz–10 kHz, 0.08–25 µs width — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- IEC 60034-18-42 Annex B gives example impulse test circuits using a semiconducting switch, with typical waveforms — [IEC 60034-18-42 Ed. 1.1 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf) [preview TOC only]

**Commercial equipment**
- Schleich partial-discharge testers:
  - PD testing from 1,000 V up to 15,000 V; surge from 1,000 V to 50,000 V;
  - MTC2 R7 offered at 6/12/15/25 kV and MTC3 R2 at 6/15 kV;
  - measure PDIV, RPDIV, RPDEV and PDEV;
  - antenna (passive or active) or coupling module, plus a 3-channel HF voltage probe (VoltageAnalyzer).

  No rise-time or polarity figure is published — [Schleich product page](https://www.schleich.com/en/partial-discharge-test-devices/) [product page]
- Solfas STA Advanced series:
  - Sinus 5 kV, 100 mA, 500 VA;
  - Surge 6 kV, 1.8 J;
  - Pulse ±2.5 kV, unipolar or bipolar PWM, rise time 150 or 500 ns selectable;
  - PD via HFCT or HF antenna, 200–400 MHz;
  - cites IEC TS 60034-27-5, IEC TS 61934 and IEC 60034-18-41.
  — [Solfas STA product page](https://www.solfas.com/partial-discharge-sta-advanced-series/) [product page]
- Electrom iTIG IV:
  - 4 kV or 6–15 kV, up to 40 kV with an external power pack;
  - surge pulses at repetition rates up to 50 Hz;
  - PD screen shows RPDIV, RPDEV and maximum PD in mV "in compliance with IEC 61934";
  - also DC hipot, programmable step voltage and megohm/PI/DAR.

  No rise time is published — [Electrom iTIG IV brochure (ATEC)](https://www.atecorp.com/getmedia/9b2115e6-673c-4735-be9a-65b146496c7d/iTIG-IV-4-15kV-Electrom-Surge-Tester.pdf?ext=.pdf) [product brochure]
- Hioki ST4030A impulse winding tester: 100–4200 V, 200 MHz sampling, optional discharge detection. No rise time found — [Hioki ST4030A](https://www.hioki.com/us-en/products/electrical-safety-testers/impulse/id_6745) [search snippet]
- Megger Baker AWA-IV: 2/4/6/12 kV models. The listings found mention surge, megohm, PI, DAR, DC step-voltage and DC hipot, but no PD option or rise time — [Megger AWA-IV listing](https://www.directindustry.com/prod/megger/product-7346-2778055.html) [search snippet]
- Stone & Lloyd describe surge-generator targets "measured from zero to peak with a conventional surge generator" and inverter rise times of "50–2000 ns" — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf) [full text]

**Published laboratory SiC generators**
- Hu et al. (2021):
  - custom 10 kV SiC MOSFET module (Wolfspeed XHV-6);
  - DC bus up to 7 kV, giving 7 kV unipolar or ±3.5 kV bipolar (polarity set by moving the ground point);
  - edges 100–800 ns set by gate resistors (100 ns into 170 pF);
  - at most 10 kHz, "limited by the cooling system".
  — [Hu et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/) [full text]
- Driendl et al. (2022): H-bridge of CREE C2M0045170D (1700 V SiC MOSFETs) fed by a 0–1500 V HVDC source, giving bipolar pulses (80 ns, 60 kHz at 800 V). The specimen sat in an oven, climate chamber or vacuum chamber, reached through 1.5 m cables, the minimum length needed — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]
- He et al. (2025): PWM generator with 70–120 ns rise and up to 3 kV amplitude, 400 MHz oscilloscope with HV probe, oven 20–300 °C (±0.1 °C) — [He et al. 2025](https://d-nb.info/1376542846/34) [full text]
- A 5 kV generator built from series-connected 1700 V SiC MOSFETs reports 48 ns rise at 5 kV and 6.2 ns at 400 V (about 100 kV/µs) for insulation tests — [Rev. Sci. Instrum. 92 (2021) 114705](https://pubs.aip.org/aip/rsi/article-abstract/92/11/114705/596176/A-5-kV-pulse-generator-with-a-100-kV-s-slew-rate) [search snippet/abstract]
- An endurance bench used a bipolar square wave at 1.5 kV peak and 20 kHz with dv/dt up to 60 kV/µs — [EEPower technical article](https://eepower.com/technical-articles/modular-dv-dt-pulse-generator-testbench-for-insulation-endurance-assessment-part-1/) [search snippet; page blocked]

**Hipot and insulation-resistance levels**
- IEC 60034-1 withstand test: 2·U_N + 1000 V for 1 min; for example 2400 V for a 690 V machine. For routine tests of quantity-produced machines up to 200 kW, 1 s at 120 % may replace the 1 min test — [type-test programme citing IEC 60034-1](https://pdfcoffee.com/download/fat-lv-motor-pdf-free.html); [Slovak national annex](https://normy.normoff.gov.sk/norma/132702/nahlad) [search snippets; IEC 60034-1 text not read]
- GB/T 18488 (2015, as analysed in a Korean paper):
  - winding-to-case withstand 1000 V + 2 × maximum working voltage (≥1 kW, ≥100 V);
  - 1500 V winding-to-temperature-sensor;
  - IR meter 500 V or 1000 V depending on maximum working voltage.

  GB/T 18488.1-2001 required cold IR > 20 MΩ. GB/T 18488-2024 replaced the 2015 parts on 2024-05-28; its values were not checked — [Korean analysis](https://koreascience.kr/article/CFKO201632568241071.pdf); [GB/T 18488.1-2001](https://www.chinesestandard.net/PDF-EN/GBT18488.1-2001EN-P09P-H7128H-692484.pdf); [GB/T 18488-2024 listing](https://www.chinesestandard.net/Related.aspx/GBT18488-2024?Redirect) [search snippets]
- A June 2025 SEARI presentation on NEV drive-motor insulation under high-voltage platforms reported:
  - IR ≥ 20 MΩ, on model coils (W/G, P/P, T/T) and stators;
  - PDIV and RPDIV ≥ 50 % of the initial value after ageing;
  - AC/DC withstand values in a "Table 7" that was not reproduced.
  — [SMM news report of SEARI talk, 2025](https://news.metal.com/newscontent/103388153/Discussion-on-Detection-and-Evaluation-Technology-of-Drive-Motor-Insulation-under-High-voltage-Platform-[Electric-Drive-System-Conference]) [news article]
- IEEE 43-2013 (insulation resistance) has been "inactive-reserved" since 2024-03-21, and a successor P43 is in development — [IEEE SA](https://standards.ieee.org/ieee/43/4791) [search snippet]
- UN R100 defines "high voltage" as >60 V and ≤1500 V DC; ISO 6469-3 voltage class B covers this range — [GAOIS terminology (R100 wording)](https://www.gaois.ie/en/terminology/fiat/648045); [ANSI blog on ISO 6469-3:2021](https://blog.ansi.org/ansi/iso-6469-3-2021-safety-for-electric-road-vehicles/) [search snippets]
- End-of-line stator test sequences combine AC dielectric strength, surge, rotation and PD, with PDIV to EN 60034-18-41 — [Marposs stator testing](https://www.marposs.com/eng/application/stator-quality-control) [search snippet]. AC PD and surge (impulse) PD find different defects — [Hioki, 6 electrical tests](https://www.hioki.com/us-en/industries-solutions/manufacturing/6electrical_testing_of_motors.html) [search snippet]

### Inferences
- *Inference, own calculation.* Required source ranges, using the targets in Q5:
  - 800 V class: P/P targets of about 1.9–3.9 kV pk-pk, within ±2.5 kV PWM sources and all surge testers.
  - 1200 V class: about 2.9–5.9 kV pk-pk, beyond ±2.5 kV pulse sources.
  - 1600 V class: about 3.8–7.8 kV pk-pk, needing at least ±4 kV bipolar plus headroom to locate the actual RPDIV.

  Among the verified sources, only surge testers (non-SiC-like edges) or a custom generator of the Hu et al. class (≤7 kV pk-pk at ≥100 ns) reach this. A 5 kV rms AC PD source (≈14 kV pk-pk) covers every class for AC PDIV.
- *Inference.* A practical equipment set:
  - (a) an AC PD system (IEC 60270, pC) of about 5 kV rms with HFCT or coupling capacitor, for all P/P and P/G margin tests and for screening;
  - (b) a bipolar SiC impulse source of about ±1.5–2.5 kV, ≤100 ns, with a UHF antenna, for T/T RPDIV and for confirming 800 V-class P/P;
  - (c) for 1200/1600 V-class confirmation, either a higher-voltage custom SiC stack (series 1.7/3.3 kV devices or 10 kV modules) or a 6–15 kV surge tester, with the waveform at the specimen recorded;
  - (d) an oscilloscope of at least 100 MHz (≥400 MHz preferred) and an HV probe at the specimen terminals.
- *Inference, own calculation.* Hipot levels:
  - IEC 60034-1 style, with U_N ≈ U_dc/√2 (maximum linear-modulation line voltage): about 2.13 kV (800 V), 2.70 kV (1200 V) and 3.26 kV (1600 V) rms for 1 min.
  - GB/T 18488-2015 style, with maximum working voltage = bus voltage: 2.6, 3.4 and 4.2 kV.

  These apply to complete windings or formettes. They are not useful as ageing diagnostics, because they are pass/fail and potentially damaging.
- *Inference.* The 1600 V class is outside UN R100/ISO 6469-3 class B, outside the 1000 V DC scope of IEC TS 61857-42, and above the roughly 700 V rms "Type I" domain of IEC 60034-18-41. Its test levels therefore have no automotive standard basis and must be justified from the enhancement-factor chain.

### Gaps
- No verified datasheet for a commercial bipolar generator with ≥±4 kV and ≤50 ns rise into a pF–nF load was found. Rise times of Schleich, Electrom, Hioki and Megger surge testers are not published on the pages read.
- I did not read the ISO 6469-3:2021, LV 123 or GB/T 18488-2024 hipot and insulation-resistance clauses. The 800 V-class OEM hipot levels remain unverified.
- The IEEE 43 insulation-resistance test-voltage table could not be verified.

## 3. Which specimens best represent each insulation path in hairpin windings, and how should they be prepared and conditioned (temperature, humidity, oil-wetted vs drained) for PD testing?

### Takeaway
Each path needs its own model:
- **Turn-to-turn (T/T):** a back-to-back pair of rectangular conductors, the "gap 0" case.
- **Phase-to-phase (P/P) in the end winding:** parallel conductors with controlled air gaps (0–150 µm) in temperature-stable holders. This is the weakest path in full-pitch hairpin windings.
- **Phase-to-ground (P/G):** a conductor on a grounded plane, or a slot model with or without liner, wedge or over-mould.
- **System level:** a hairpin formette per IEC TS 61857-42 Annex B, or a 30 cm hairpin-in-slot emulation.

Twisted pairs remain the reference for round wire. After oil ageing, handling must be standardised and reported (blotting, draining or drying). IEC 60851-4 splits specimens "as removed" vs "dried at 125 °C/30 min" to separate reversible absorption from degradation. Oil films and oil vapours change PDIV in both directions.

### Cited Findings
**Standard test-object families**
- IEC TS 60034-27-5 clause 6.1 covers twisted pair or equivalent, motorette or formette, and complete winding and connection. It defines a "parallel winding" model in which T/T is simulated by two isolated conductors wound in parallel, one grounded and one energised — [IEC TS 60034-27-5 preview](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf) [preview]
- IEC 60034-18-41 qualification uses "twisted pair or equivalent arrangement" (10.2.2) and "motorette (random wound) or formette (form-wound)" (10.2.3). Table B.6 gives T/T PD test levels for special windings and twisted pairs — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf) [preview TOC]
- IEC TS 61934:2024 classifies test objects as:
  - capacitive: twisted pairs, main-wall models;
  - inductive: motorettes and formettes;
  - distributed: turn insulation of windings, busbars.

  The class determines waveform distortion at the object — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- IEC TS 61857-42:2025 (Ed. 1.0, 2025-08) provides:
  - Table 1, guidance for test-object selection (segmented and prototype stators);
  - Annex B, "GPM construction: Hairpin formette" (arrangement, components, assembly, test positions; Fig. B.1 shows a hairpin formette made with steel);
  - an initial impulse PD test (6.2) and impulse PD within diagnostic sub-cycles (8.2);
  - a dielectric diagnostic test;
  - Annex A, chemical compatibility with cooling fluids;
  - normative Annex C, derivation of peak-to-peak test voltages for the diagnostic impulse PD test, including the PD safety factor.

  Scope is EIS in road-vehicle drivetrains with battery DC voltage up to 1000 V. The EIS "will operate free from partial discharges over its whole lifetime" — [IEC TS 61857-42:2025 preview, VDE](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iects61857-42%7Bed1.0%7Den.pdf) [preview: TOC, introduction, scope]

**Hairpin-specific models in published work**
- HEFT D2.4 (Cavallini, UNIBO, 2024):
  - P/P end-winding models: rectangular PAI and CR-PAI conductors (80 and 110 µm enamel) separated by air gaps of 0, 50, 100 and 150 µm, held in MACOR holders (stable to 800 °C, low thermal expansion). They checked that "at least the minimum distance between the conductors was equal to the air gap length", because perfect parallelism is hard.
  - P/G: conductor in direct contact with a grounded plane, as the worst case without over-moulding and representing contact with the slot wedge.
  - T/T: back-to-back at gap 0.
  - Tests were at 20–210 °C in an oven.
  — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf) [full text]
- In end windings, "conductors of different phases can be positioned close to each other, separated by an air gap of a few tens of micrometers (typically ≥100 μm)". The P/P path in the end winding is "the most critical part". With a sequential hairpin layout, T/T stress is small: about 224 V pk-pk at 800 V, with 30 % of the jump voltage across the first two turns. Double-pulse superposition can raise the first-to-last turn voltage in interlayer-transposition hairpins (Ju et al., IEEE TIE 2022, DOI 10.1109/TIE.2021.3116577, cited therein) — [Martinez, Iannarelli, Seri, Cavallini, IEEE WEMDCD 2025, DOI 10.1109/WEMDCD61816.2025.11014120 (postprint)](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf) [full text]
- He et al. used a single hairpin in a slot, 30 cm long, PAI about 100 µm (Grade 3), as "hairpin-in-slot emulation". They note formettes represent the slot insulation system — [He et al. 2025](https://d-nb.info/1376542846/34) [full text]
- Chinese practice reported by SEARI (2025): rectangular wire tested back-to-back with a 150 mm straight section and binding tape rated ≥180 °C; round wire as twisted pairs; model coils for winding-to-ground, P/P and T/T — [SMM report of SEARI talk](https://news.metal.com/newscontent/103388153/Discussion-on-Detection-and-Evaluation-Technology-of-Drive-Motor-Insulation-under-High-voltage-Platform-[Electric-Drive-System-Conference]) [news article]
- Twisted pairs "should undergo the same processes of the stator" (e.g., dipping and baking) — [CIGRE WG D1.43 TB](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf) [full text; 2011, older]. Lusuardi et al. show that impregnated twisted pairs can have lower PDIV than bare pairs at high temperature, so the impregnation route must match the product — [Lusuardi et al. 2021](https://zenodo.org/records/4562202) [full text]

**Conditioning and handling after oil exposure**
- IEC 60851-4:2016 Test 20 (resistance to transformer oil), for round wire:
  - 10 twisted pairs are aged in a sealed stainless pressure vessel with dried, de-aerated oil and paper, at the class temperature or 150 °C, for 1000 h.
  - After cooling to room temperature, five pairs are tested for breakdown "with the specimens in air" at 105 °C as removed.
  - The other five are dried at 125 °C for 30 min first. The standard notes that if only absorption has occurred, this drying "will produce a recovery of the specimen".
  - Rectangular wire uses U-shaped and mandrel-bent specimens.
  — [IEC 60851-4:2016](https://webstore.iec.ch/en/publication/25335) [full text of the 2016 edition read from a copy retrieved in an earlier session]
- T/CAQI draft 2025 (oil-resistant insulation paper for NEV motors):
  - ATF is set to 2000 ± 100 ppm water;
  - 2 L SUS304 sealed tanks with PTFE gasket, 75 % filled, specimens fully immersed;
  - cycles RT → (155 °C/40 h → −40 °C/8 h) × 8;
  - after cycles 4 and 8, specimens are removed and the surface oil is blotted with oil-absorbent paper before testing;
  - unaged controls are conditioned 24 h at 23 °C/50 % RH and tested in air.
  — [T/CAQI draft 2025](https://www.ttbz.org.cn/upload/file/20251024/6389689969642652828990215.pdf) [full text of draft]
- HEFT D2.4: back-to-back conductors (about 4 cm) aged in Castrol ON BOT (BEV) G5 ATF at 160 °C for 2 weeks. PDIV was measured before and after at 20, 180 and 210 °C. The handling between oil and PD test is not described — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf) [full text]
- Spraying ATF at 60 °C on conductors at 180 °C, with a 50 µm gap, reduced PDIV. The abstract gives "about 10–15 %"; the text says "a reduction down to 10 %". Vapours were visible, and the authors suggest hydrocarbons in the gas phase raise the Townsend ionisation coefficient — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf) [full text]
- In contrast, oil-coated crossed PAI wires showed higher PDIV and corona resistance at ambient temperature, with the benefit decreasing at elevated temperature — ["Impact of Cooling Oil on PD and Insulation Reliability in Inverter-Fed EV Motors", Cognizance J. Multidiscip. Stud. 2025](https://www.academia.edu/130464924/Impact_of_Cooling_Oil_on_Partial_Discharge_and_Insulation_Reliability_in_Inverter_Fed_EV_Motors) [abstract only; low-profile journal]
- Twisted pairs fully immersed in silicone oil were used to *prevent* PD inception in intrinsic-ageing studies — [CIGRE WG D1.43 TB](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf) [full text; 2011]
- Peng et al. (RWTH/TotalEnergies) immersed twisted pairs (Damid PAI-overcoat and PEEK) and Nomex in two water-based lubricants in sealed heating pots at 70 and 100 °C. Sampling was at 1 day and 2, 4, 6 and 8 weeks, with 7 specimens per sampling point and type, and PDIV was measured with an impulse generator and a Stahl EW600.B. Damid enamel in WBL1 at 100 °C dissolved after 6 weeks — [Peng et al., IEEE IEMDC 2025, DOI 10.1109/IEMDC60492.2025.11060975](https://doi.org/10.1109/IEMDC60492.2025.11060975) [full text read from a copy retrieved in an earlier session]
- Climate conditioning matters. Qualification tests are "usually carried out at a controlled temperature and humidity (20 °C and 60 % relative humidity)", and the largest RH-induced PDIV drop occurred between 60 and 85 % RH — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]. The earlier report's protocol is three readings per specimen, 60 s apart, after 10 min at temperature.

### Inferences
- *Inference.* Use a four-model kit per insulation technology, all cut from the same coil and corner radius:
  - (i) T/T back-to-back, flatwise and edgewise, 150 mm contact;
  - (ii) P/P gap model at 0, 50 and 100 µm in ceramic holders, as the critical path for every bus class;
  - (iii) P/G conductor-on-plane, plus a slot model with liner if liners are part of the study;
  - (iv) hairpin formette or hairpin-in-slot only for a subset.

  Only (ii) and (iii) need the high-voltage range of the 1200/1600 V classes.
- *Inference.* Define three PD-test states for each oil-aged specimen and keep them separate in the results:
  - S1 "as removed + blotted", after IEC 60851-4 and T/CAQI;
  - S2 "drained + dried", for example 125 °C/30 min as in IEC 60851-4, or a fixed time at test temperature, to separate absorption from degradation;
  - S3 "solvent-cleaned", optional, using a solvent shown not to attack the enamel.

  These states cost measurement time, not extra specimens. Never measure fully immersed specimens for air-gap PDIV, because oil suppresses PD and the result describes a different gap.
- *Inference.* Measure every state at RT and at the oil-ageing temperature (for example 150–180 °C), at fixed RH (for example ≤50 % RH at RT), after a fixed soak. Record barometric pressure, because PDIV varied 42 % between 1000 and 200 mbar.

### Gaps
- No source compares PDIV of ATF-aged specimens after blotting, draining, drying and solvent cleaning. The effect of residual oil films on hairpin RPDIV is unquantified.
- The dimensions, materials and test positions of the IEC TS 61857-42 hairpin formette (Annex B) were not visible in the preview.
- No published P/P gap-model data were found for PEEK, PI/FEP tape or powder coatings. The HEFT data cover PAI and CR-PAI only.

## 4. How are voltage-endurance and multi-stress (electrical + thermal + environmental) ageing tests designed?

### Takeaway
There are two families of test:
- **Type I (PD-free) qualification** under IEC 60034-18-41 is a diagnostic test, not a life test. Specimens go through IEC 60034-18-21-style thermal, mechanical and environmental sub-cycles. A PD-proof test at the class-specific V_c follows each sub-cycle, and failure means PD below V_c or breakdown, with ≥5 samples.
- **Life tests** under IEC 60034-18-42 Type II, or research endurance tests, age specimens destructively at several voltage levels above service stress. They fit an inverse power law in voltage, use a frequency-acceleration rule (life ∝ 1/f) to shorten the test, and analyse Weibull lifetimes (IEC 62539).

For automotive EIS, IEC TS 61857-42 (2025) adapts thermal multifactor evaluation (8000 h passenger-car life, cooling-fluid compatibility, impulse PD diagnostics). It applies only up to 1000 V DC. Published multi-stress designs use 2-level factorial DoE (He et al.) or periodic immersion sampling (Peng et al.).

### Cited Findings
- IEC 60034-18-41: qualification test objects are "subjected to the range of tests described in IEC 60034-18-21 or IEC 60034-18-31 with the addition of a high frequency voltage test and a partial discharge test". If PD-free at the end of the sequence, the system "is qualified for the severity band" — [IEC 60034-18-41:2014 preview](https://cdn.standards.iteh.ai/samples/18905/b95c2f0bc77e4b658894b3e6629e3aa2/IEC-60034-18-41-2014.pdf) [preview]
- Sub-cycles apply thermal, mechanical and ambient stresses "sequentially (or simultaneously, if workable)", with a PD-proof test at the end of each. Failure time is noted when PD incepts below V_c or the system breaks down, at least five samples are needed, and EF_Aging = 1 in qualification because the ageing is actually applied — [Lusuardi et al. 2021](https://zenodo.org/records/4562202) [full text]
- IEC 60034-18-42 (Type II) contents:
  - qualification "involves destructive ageing of test objects under accelerated conditions" and yields a life curve, including one for turn insulation (Fig. 9);
  - Table 2 covers the influence of converter-voltage features on acceleration of ageing;
  - Annex A uses an "endurance coefficient of 10" example to compute 1 kHz impulse ageing relative to 50 Hz;
  - Annex E covers deriving an IVIC from endurance tests;
  - IEC 62539 is normative for statistics.
  — [IEC 60034-18-42 Ed. 1.1 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec60034-18-42%7Bed1.1%7Db.pdf) [preview]
- The CIGRE WG D1.43 technical brochure states:
  - the TS "supports the frequency acceleration rule to extrapolate test results to the operating frequency, and the inverse power law to evaluate the lifetime at the rated voltage";
  - pulse ageing of groundwall insulation is "much more severe" than 50/60 Hz;
  - groundwall temperature rose about 10 °C per ~1 kHz switching-frequency increase;
  - life dropped about 58 % without and about 31 % with forced cooling, showing the role of dielectric heating;
  - intrinsic (PD-free) ageing is faster at high frequency.
  — [CIGRE WG D1.43 TB](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf) [full text; 2011]
- Recent endurance studies (search-level only):
  - Under repetitive square waves, life is "mainly determined by the peak-peak magnitude" when other parameters are fixed — [Akram et al., High Voltage 2022](https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/hve2.12223) [search snippet; publisher page blocked]
  - Life lines keep a constant slope with an intercept that rises with voltage, i.e. inverse-power-law behaviour; dv/dt also acts as an inverse power; tests were held at 5 kHz to shorten ageing — [Yang et al., High Voltage 2024](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/hve2.12375) [search snippet]
  - Rise time and frequency "can influence lifetimes significantly", and square and sine waves of equal peak-to-peak value give different PD and life — [Wang et al., IEEE TDEI](https://www.researchgate.net/publication/263164673_The_Influence_of_Repetitive_Square_Wave_Voltage_Parameters_on_Enameled_Wire_Endurance) [search snippet]
- He et al. 2025 DoE for hairpin-in-slot:
  - 5 temperatures (20, 67.5, 115, 162.5, 210 °C), voltage levels 0, 675, 750, 825, 900, 975 V with rated 800 V, rise times 70/120 ns, 1 kHz, 500 µs width;
  - "20 test groups" with 4 DUTs each;
  - analysed as a 2³ full factorial with low/high codings (T ≤115 vs ≥162.5 °C; U ≤825 vs ≥900 V; 70 vs 120 ns);
  - ≥250 h; lifetime modelled with IEC 61858 regression.

  Electrical and thermal stress interact. "RPDIV alone" did not reliably indicate ageing degree, and failure rate was the most reliable response — [He et al. 2025](https://d-nb.info/1376542846/34) [full text]
- Mancinelli, Stagnitta and Cavallini proposed a multistress qualification model for hairpin motors including electrical, thermal, mechanical vibration and thermal cycling factors — [IEEE TIA 53 (2017), DOI 10.1109/TIA.2016.2619670](https://cris.unibo.it/handle/11585/598944) [abstract/search snippet only]
- IEC TS 61857-42:2025:
  - passenger-car drivetrain EIS "designed for a typical lifetime of 8 000 h", vs. 20 000 h for industrial motors;
  - multifactor evaluation for cooling-fluid compatibility and mechanical load profiles;
  - suggested ageing temperatures and periods (Table 3), with example cycles of 24 h at 235 °C, 96 h at 215 °C and 288 h at 195 °C;
  - test voltages (Table 4).
  — [IEC TS 61857-42 preview](https://www.vde-verlag.de/iec-normen/preview-pdf/info_iects61857-42%7Bed1.0%7Den.pdf) [preview]
- Chinese NEV practice reported by SEARI (2025), for thermal life:
  - lowest ageing temperature: average life ≥25 % of design life and ≥2500 h;
  - highest temperature: average life ≥100 h;
  - temperature steps ≥20 K, extrapolation ≤25 K, about 10 cycles per sub-cycle;
  - pass criterion after ageing: PDIV/RPDIV ≥50 % of initial.
  — [SMM report of SEARI talk](https://news.metal.com/newscontent/103388153/Discussion-on-Detection-and-Evaluation-Technology-of-Drive-Motor-Insulation-under-High-voltage-Platform-[Electric-Drive-System-Conference]) [news article]
- Oil plus thermal cycling: the T/CAQI draft uses (155 °C/40 h ↔ −40 °C/8 h) × 8 in ATF with 2000 ppm water — [T/CAQI draft 2025](https://www.ttbz.org.cn/upload/file/20251024/6389689969642652828990215.pdf) [full text of draft]

### Inferences
- *Inference.* For a PD-free (Type I) study across three bus classes, the energised-ageing voltage should sit below each specimen's measured RPDIV. It should equal the class's service peak-to-peak stress per path (for example HEFT P/P 1920/2880/3840 V pk-pk for 800/1200/1600 V at OF 1.2). The purpose is to see whether combined oil, thermal and voltage stress changes RPDIV or dielectric response faster than unenergised oil ageing (synergy). Above-RPDIV endurance (inverse power law) belongs to a separate Type II-style sub-study, because the Type I philosophy treats PD inception as end of life.
- *Inference.* Frequency acceleration is valid only while the failure mechanism does not change. Dielectric heating at tens of kHz, and oil heating, can shift it. Keep the specimen temperature under control (thermocouple on the conductor) and run one frequency-check pair (for example 1 kHz vs 10 kHz) before extrapolating.
- *Inference.* For step-stress designs, apply voltage in steps of fixed duration (for example 0.1 × target per step) to a small batch of oil-aged and unaged specimens. This ranks technologies quickly, but extrapolating to life requires an assumed inverse-power-law exponent. I found no recent hairpin-specific step-stress study, so treat it as a ranking tool only.

### Gaps
- No published combined voltage + oil (ATF/e-fluid) + temperature endurance study on hairpin insulation was found. Peng et al. and HEFT did oil ageing without voltage; He et al. did voltage + temperature without oil.
- Voltage-endurance coefficients (n) for PEEK, PI/FEP or CR-PAI under bipolar SiC impulses were not retrieved. The Yang 2024 and Akram 2022 full texts were blocked.
- The IEC 60034-18-42 sub-clauses on turn-insulation endurance (number of voltage levels, specimens per level, allowed frequency) were not visible in the preview.

## 5. How can three voltage classes be added economically to an oil-ageing matrix (margin analysis against class-specific PD-free targets, energised ageing for a subset), and what published matrix designs and specimen counts exist?

### Takeaway
The cheapest approach treats DC-bus class as an evaluation factor, not an ageing factor. Every specimen in the existing dry/oil-aged matrix is measured once per state (PDIV, RPDEV and RPDIV for a subset) at RT and at temperature. Its statistic (mean − 3σ or Weibull B10) is then compared with three class-specific targets per insulation path. This adds zero specimens.

HEFT D2.4 is a published template: it gives 800/1000/1200 V targets for P/P, P/G and T/T and margin tables. Energised ageing is then added only for the few best technologies, at 1–2 voltage levels, with 4–5 specimens per cell, following He et al.'s 2-level factorial design. Published counts are:
- He et al.: 4 DUTs per group;
- Peng et al.: 7 per sampling point;
- Driendl et al.: 5–10;
- IEC 60034-18-41: ≥5;
- IEC 60851-4: 10 pairs, split 5 + 5.

### Cited Findings
- HEFT D2.4 (2024) margin method, the closest published template:
  - assumes a 2-level drive, OF = 1.2 (measured by GKN) and a bipolar DC bus (±U_dc/2 to frame);
  - EF_T = 1.2 (range 1.0–1.3) for RT tests, or not applied when tests are at 180 °C;
  - EF_Aging = max(1.2·Ts/Tc, 1) = max(0.98, 1) = 1 for Tc 220 °C and Ts 180 °C;
  - PDIV/PDEV hysteresis = 1, because the maximum bus voltage is used;
  - U_os = (OF − 1)·U_des; P/P = 2·(U_des + U_os); P/G = U_des + 2·U_os; T/T = 2·(2/3)·ρ·(U_des + U_os), with ρ = 0.19 at 30 ns from FEA (ρ = 0.3 conservative).

  The resulting service and target values are:

  | Path | 800 V | 1000 V | 1200 V |
  |---|---|---|---|
  | P/P (V pk-pk) | 1920 | 2400 | 2880 |
  | P/G (V pk-pk) | 1120 | 1400 | 1680 |
  | T/T, ρ = 0.19 (V pk-pk) | 243 | 304 | 364 |
  | T/T, ρ = 0.3 (V pk-pk) | 384 | 480 | 576 |
  | RT type-test P/P (V pk-pk) | 2304 | 2880 | 3456 |
  | RT type-test P/G (V pk-pk) | 1344 | 1680 | 2016 |

  The equations "were agreed upon" with the IEC 60034-18-41 Ed. 2 project leader and TC 112 WG 6 members — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf) [full text]
- HEFT margins at 180 °C, defined as PDIV − 3·StdDev − target in V pk-pk:
  - PAI 110 µm back-to-back (PDIV 2215 ± 17): +242 / −238 / −718 for 800 / 1000 / 1200 V;
  - CR-PAI 110 µm: +47 / −433 / −913;
  - P/G PAI 110 µm (PDIV 1551): +431 / +151 / −129.

  The conclusions were:
  - 800 V: 80 µm "is never guaranteed" once the standard deviation is considered, while 110 µm always works;
  - 1000/1200 V: "none can be reliably used";
  - T/T limits of 384/480/576 V pk-pk (ρ = 0.3) are met even at 210 °C.

  Preliminary thickness estimates from RT PDIV data were 90/120/150 µm for 800/1000/1200 V — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf) [full text]. Martinez et al. (2025) state that 110 µm is adequate for P/G and P/P "up to 1000 V". This conflicts with the negative P/P margins at 1000 V in D2.4 and probably reflects mean-based vs mean − 3σ criteria — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf) [full text]
- Stone & Lloyd tabulate RPDIV targets by stress category (OF 1.1/1.5/2.0/2.5) for one motor rating. This is a precedent for evaluating one dataset against several severity targets — [Stone & Lloyd 2014](https://irispower.com/wp-content/uploads/2018/06/IEC-Standards-for-Variable-Speed-Drives-and-Motor-Winding-Insulation.pdf) [full text]
- He et al. (2025) matrix:
  - 20 groups × 4 DUTs;
  - each group split into Group A (RPDIV every 24–96 h) and Group B (RPDIV only at start and end) to check whether the measurements themselves cause ageing;
  - failure rates 29.5 % (13/44) vs 20.5 % (9/44), judged "largely unaffected";
  - a separate set of 5 hairpin-in-slot emulations used for RPDIV vs temperature (20–180 °C).

  The 44 + 44 counts in their Table 4 do not match 20 × 4 = 80; the inconsistency is in the paper — [He et al. 2025](https://d-nb.info/1376542846/34) [full text]
- Peng et al. (2025) matrix: 2 fluids × 2 temperatures (70 and 100 °C) × specimen types (Damid pairs, PEEK pairs, Nomex) × 5 sampling times × 7 specimens — [Peng et al. 2025](https://doi.org/10.1109/IEMDC60492.2025.11060975) [full text, earlier-session copy]
- Driendl et al.: 10 specimens for the temperature and pressure series and 5 for the humidity series — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]. IEC 60851-4 Test 20: 10 twisted pairs per oil test, split 5 as removed + 5 dried — [IEC 60851-4:2016](https://webstore.iec.ch/en/publication/25335) [full text, earlier-session copy]. IEC 60034-18-41 qualification: ≥5 samples — [Lusuardi et al. 2021](https://zenodo.org/records/4562202) [full text]

### Inferences
- *Inference, own calculation.* Class-specific targets in V pk-pk for 800 / 1200 / 1600 V buses. The 800 and 1200 V values of framework A are from HEFT; all 1600 V values and frameworks B–D are my extrapolations with the published formulas.
  - **A. HEFT style, OF 1.2, tested at operating temperature:**
    - P/P 1920 / 2880 / 3840;
    - P/G 1120 / 1680 / 2240;
    - T/T 243 / 365 / 486 (ρ 0.19) or 384 / 576 / 768 (ρ 0.3).
  - **A at RT (× EF_T 1.2):**
    - P/P 2304 / 3456 / 4608;
    - P/G 1344 / 2016 / 2688.
  - **B. IEC-style chain (Lusuardi), RT tests, EF_PD 1.25, EF_Aging 1, OF 1.2:**
    - P/P (WF 2, EF_T 1.3) 3120 / 4680 / 6240;
    - P/G (WF 1.4, EF_T 1.1) 1848 / 2772 / 3696;
    - T/T (WF 0.7, EF_T 1.3) 1092 / 1638 / 2184.
  - **C. Same as B with OF 1.5 (category B bound):**
    - P/P 3900 / 5850 / 7800;
    - P/G 2310 / 3465 / 4620;
    - T/T 1365 / 2048 / 2730.
  - **D. Driendl twisted-pair T/T (random-winding worst case, a 0.85, OF 1.25, NF 1.1, EF 1.625):** 2134 / 3201 / 4268. With the ambient EF of 2.19: 2867 / 4300 / 5733.

  Framework D is not appropriate for sequentially laid hairpins, where T/T sees only ρ ≈ 0.19–0.3 of the jump voltage. It is relevant only for round-wire or random-wound references. The report should state which framework is used and evaluate every specimen against all three classes.
- *Inference.* An economical matrix in three layers:
  - **Layer 1, existing study, no new specimens.** k technologies × {dry reference, oil-aged t1, t2 (t3)} × models {T/T back-to-back, P/P gap, P/G plate} × n = 5. Add an air-aged control at the same temperature and time to separate oil from thermal effects. Each specimen gets AC PDIV/PDEV at RT and at T_op in state S1 (blotted) and state S2 (dried). The output is a margin table per class, using mean − 3σ or B10 − target, plus the "PDIV ≥ 50 % of initial" retention criterion.
  - **Layer 2, impulse confirmation, measurement only.** Bipolar ≤100 ns RPDIV/RPDEV on 2 of the 5 specimens per cell (or all specimens at end of test), to verify the AC–impulse equivalence per technology.
  - **Layer 3, energised oil ageing, new specimens.** Top 2–3 technologies × 1 oil temperature × 2 voltage levels (800-class and 1600-class service peak-to-peak on the P/P gap model or a hairpin formette, both below RPDIV) × 5 specimens. Split into He-style A/B subgroups (periodic vs start/end measurement).
- *Inference, own calculation.* Example count with 8 technologies:
  - Layer 1: 8 × 4 conditions × 3 models × 5 = 480 specimens.
  - Making voltage class an ageing factor for oil-aged cells only would add 8 × 3 (oil conditions) × 3 models × 5 × 3 classes ≈ 1080 energised specimens and 72 energised oil vessels.
  - Layer 3 instead adds 3 × 2 × 5 = 30 specimens (60 if two models are energised).
  - A 2³ fractional or full factorial (temperature × voltage × oil/no-oil) for the energised subset follows He et al. and keeps interaction terms estimable.
- *Inference.* Use the same models for margin analysis across classes, but make sure the voltage source covers the 1600 V-class targets. In HEFT framework A at temperature, a P/P model needs PDIV ≥ 3840 V pk-pk plus 3σ. The HEFT PAI and CR-PAI data (≤2.6 kV pk-pk at 180 °C) imply that much thicker or lower-permittivity insulation (e.g. PEEK, multilayer) would be needed. This extrapolation is uncertain, because PDIV does not scale linearly with thickness.

### Gaps
- I found no published matrix that evaluates the same oil-aged specimens against several DC-bus classes. HEFT evaluates unaged and briefly ATF-aged PAI only, with no 1600 V class.
- No published specimen-count or power analysis for detecting PDIV changes of a given size in oil-ageing studies was found. The counts above (4–10) are precedents, not statistically derived.
- HEFT does not state the PD detector, voltage waveform or number of specimens behind each mean and standard deviation. The WEMDCD paper indicates AC measurements.

## 6. What safety and practical issues arise when applying high voltage to specimens in or wetted by oil at elevated temperature?

### Takeaway
The main constraints are:
- **Fire:** conventional ATFs have flash points of about 170–210 °C, and HEFT's ATF had a 180 °C fire point. Ageing at 150–180 °C is close to this.
- **Pressure and leaks:** sealed vessels cooled before opening are needed.
- **Hot oil vapour:** it lowers PDIV and could ignite.
- **Electrical hazards:** HV test-area interlocks and EMC shielding are needed.

Published practice ages oil-wetted specimens in sealed containers below the fire point (HEFT: 160 °C for an ATF with a 180 °C fire point) and does hot PD tests on handled specimens in an oven. The handling between oil and PD test must be defined, because both residual oil and vapours change PDIV.

### Cited Findings
- HEFT: "Considering the fire point of the oil (180 °C) and the maximum temperature in operation (210 °C), the tests were performed at a temperature of 160 °C". Specimens were in sealed aluminium containers in an oven for 2 weeks. A corrosive-sulfur check from transformer practice was added: bare Cu wrapped in kraft paper in the oil at 140 °C for 4 days, and at 160 °C. No Cu₂S or FTIR anomaly was found. Enamel–copper delamination was traced to the enamel, because it also occurred after 1 week at 220 °C in air without oil — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf) [full text]
- Conventional ATF flash points from technical data sheets, which may not apply to low-viscosity e-fluids:
  - Dexron III-H 210 °C (ASTM D92) — [PDS Power ATF D III H](https://apar.com/wp-content/uploads/2021/02/1-PDS-POWER-ATF-D-III-H.pdf);
  - Dexron II-D 180 °C — [PDS Power ATF D II D](https://apar.com/wp-content/uploads/2021/02/2-PDS-POWER-ATF-D-II-D.pdf);
  - Servo Transdex III min 170 °C (COC) — [IOCL](https://iocl.com/Downloads/Servo_Transdex_III.pdf);
  - Oryx MATIC ATF >180 °C — [Oryx TDS](https://lubes.oryxenergies.com/wp-content/Data-Sheets/EN/TDS/MATIC-ATF_online_TDS.pdf).

  [search snippets of TDS]
- Visible vapours appeared when ATF was sprayed on 180 °C conductors, with an accompanying PDIV reduction of about 10–15 % — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf) [full text]
- Vessel practice:
  - IEC 60851-4: stainless pressure vessel rated 6 × 10⁶ Pa, preferably unwelded, with controlled heating; oil and paper dried and de-aerated (2 kPa, 16 h at 90 °C or 4 h at 105 °C); vessel cooled to room temperature before discharging and opening — [IEC 60851-4:2016](https://webstore.iec.ch/en/publication/25335) [full text, earlier-session copy]
  - T/CAQI: 2 L SUS304 tank with PTFE gasket, 75 % fill — [T/CAQI draft 2025](https://www.ttbz.org.cn/upload/file/20251024/6389689969642652828990215.pdf) [full text of draft]
  - Chinese practice: bolt torque 60 or 100 N·m by container type — [SMM report of SEARI talk](https://news.metal.com/newscontent/103388153/Discussion-on-Detection-and-Evaluation-Technology-of-Drive-Motor-Insulation-under-High-voltage-Platform-[Electric-Drive-System-Conference]) [news article]
  - Peng et al.: sealed heating pots — [Peng et al. 2025](https://doi.org/10.1109/IEMDC60492.2025.11060975) [full text, earlier-session copy]
- IEC TS 60034-27-5 clause 6.2, "Safety and environment during PD test", covers grounding vs. floating of test objects and environment during the test. IEC TS 61934 requires EM shielding of the impulse generator — [IEC TS 60034-27-5 preview](https://cdn.standards.iteh.ai/samples/23255/adc22c15e39342919b4552a9e81aa3ea/IEC-TS-60034-27-5-2021.pdf); [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [previews; clause text not visible]. Hu et al. tested inside a grounded Faraday shield — [Hu et al. 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8152218/) [full text]
- EN 50191 (erection and operation of electrical test equipment): BS EN 50191:2010 is listed as under review. Vendors describe test hoods with safety switches that prevent opening during a test (Performance Level e per ISO 13849-1) and enclosures that disconnect HV when opened — [BSI listing](https://knowledge.bsigroup.com/products/erection-and-operation-of-electrical-test-equipment-1); [Metrel guide to EN 50191 workplaces](https://www.metrel.si/assets/Metrel/PDF_dokumentacija/Handbook/Ang/MI_3394_CE_MultiTesterXS/Guide%20working%20place%20acording%20to%20EN%2050191_Ang_2021.pdf) [search snippets]
- Long leads to an oven or chamber alter the waveform. Driendl et al. used the minimum length (1.5 m) and measured the voltage at the specimen terminals — [Driendl et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022NDInfluence.pdf) [full text]. IEC TS 61934 requires recording the waveform at the test object — [IEC TS 61934:2024 preview](https://cdn.standards.iteh.ai/samples/103347/2bb1cad446b6434e882415029f27724e/IEC-TS-61934-2024.pdf) [preview]
- Full immersion in oil suppresses PD, as in silicone-oil-immersed twisted pairs used in intrinsic-ageing tests — [CIGRE WG D1.43 TB](https://cigre.cz/dokumenty_komise/d1/WG%20D1.43_TB_Final.pdf) [full text; 2011]

### Inferences
- *Inference.* Keep three stations separate:
  - (1) a sealed-vessel ageing oven, at least 20 K below the fluid's flash or fire point, with over-temperature cut-out and ventilation;
  - (2) a handling bench (blot, drain, dry) with defined times;
  - (3) a clean PD oven or climate chamber in an interlocked, grounded Faraday cage.

  Do not energise oil-dripping specimens in a hot air oven. Oil vapour both reduces PDIV (biasing all subsequent specimens in that oven) and creates an ignition risk if PD or breakdown arcs occur. Clean or bake out the PD oven between oil-aged batches, and run a reference specimen to detect contamination drift.
- *Inference.* For any energised oil ageing (Layer 3 in Q5), use sealed or inerted (N₂) vessels with HV feedthroughs. Add pressure relief, current-limited sources with breakdown detection (so arcs cannot persist in oil), and temperature limits below the flash point. Discharge and ground specimens before opening vessels.
- *Inference.* Obtain the SDS of the specific e-fluid, which may differ from ATF. Measure the fluid's water content before and after ageing; the earlier report and T/CAQI use 2000 ppm or 0.2–0.5 %. Water both accelerates hydrolysis and changes PDIV.

### Gaps
- No source quantifies the fire or ignition risk of PD or breakdown in hot ATF-wetted specimens, or prescribes how to energise specimens in hot e-fluid.
- Flash and fire points of modern low-viscosity EV e-fluids were not found; only conventional ATF data sheets were.
- No validated cleaning procedure (solvent type, time) that removes ATF without altering enamel PDIV was found.
- EN 50191 clause content (interlock categories, clearances) was not read.
