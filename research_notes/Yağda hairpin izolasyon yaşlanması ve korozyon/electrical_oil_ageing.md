# Electrical and dielectric effects of oil ageing on e-machine winding insulation (ATF, e-fluids, other oils)

Source-type tags used below: [PR] = peer-reviewed journal or magazine; [CONF] = conference paper; [THESIS]; [REPORT] = public project deliverable or government report; [PATENT]; [VENDOR] = company or trade-press material (not independently verified). "Abstract only" means only the abstract or landing page could be opened. All numbers come from the opened source cited on the same line. Research cut-off: October 2026.

## 1. Which studies aged winding insulation in ATF, e-fluids or other oils and measured electrical or dielectric properties? (study catalogue)

### Takeaway
The literature is small. Only about six academic sources age winding insulation in oil and then make electrical measurements: four from RWTH Aachen IEM (Yang, Pauli and Hameyer, 2022–2024, funded by TotalEnergies), and from Bologna/Mondragon the HEFT deliverable and its 2025 conference paper (Cavallini group). One IEEE EI Magazine article (Tre Tau, 2024) adds to these, and industry evidence comes from Afton (SAE paper and patents), Castrol (CEEIA 415-2019 protocol), Suzhou Jufeng and Essex (patents), and Honda (SAE). Specimens are almost always straight wires, twisted pairs or back-to-back rectangular conductors. No source found aged a hairpin stator, formette or full motor in oil and re-measured PDIV, BDV or tan δ.

### Cited Findings

#### Quick comparison of protocols (details and sources in C1–C15 below)

| # | Study (type, year) | Specimen / insulation | Fluid (water) | Vessel | T / duration | Electrical & dielectric measurements | Headline electrical result |
|---|---|---|---|---|---|---|---|
| C1 | Yang et al., ICEM 2022 [CONF] | Straight Damid 200 PEI/PAI round wire, 1 mm (twisted after ageing); Aramid-PI-Aramid paper | Commercial ATF, mineral e-fluid, synthetic e-fluid (water not reported) | Not reported; dry kiln | 180 °C, 1008 h (24/336/772/1008 h samples) + air reference | C at 10 kHz; PDIV under bipolar 10 kHz voltage | PDIV slightly ↓ and C slightly ↑ in all groups including air; no oil-specific electrical change before mechanical cracking |
| C2 | Yang et al., AEE 2022 [PR] | Damid 200 twisted pairs, 20 per group | Commercial ATF film + 0–1.2 g/L Cu particles | n/a (wetted, not aged) | Not aged | C, tan δ (1 and 10 kHz); PDIV (sine); RPDIV (surge) | ATF film raises PDIV and RPDIV about 3×; Cu particles cut PDIV α from 3677 to 2364 V |
| C3 | Yang et al., IEMDC 2023 [CONF] | Damid 200 wire; twisted pairs; 2 motorettes | Water-based lubricant (WBL) | Sealed heating pot | 90 °C, 1008 h | PDIV, C, εr, electrical lifetime (1200 V DC link, 10 kHz), IR (1000 V DC) | εr +~20 %; PDIV hardly changed; motorette IR fell to 0.9 MΩ when fully wetted |
| C5 | HEFT D2.4, UNIBO 2024 [REPORT] | Ederfil Becker PAI rectangular conductors, back-to-back with slot-moulding resins | Castrol ON BOT (BEV) G5 ATF | Sealed aluminium containers, plus no-oil controls | 160 °C, 2 weeks | PDIV at 20/180/210 °C; dielectric spectroscopy (tan δ, ε′) | No appreciable PDIV drop; new tan δ loss peaks; enamel delamination |
| C6 | Martinez et al., WEMDCD 2025 [CONF] | PAI rectangular conductors, 50 µm gap | ATF spray at 60 °C on 180 °C conductors; ester and mineral ATF ageing | n/a | 160 °C, 2 weeks (ageing) | PDIV with spray on vs off | Spray lowers PDIV by ~10–15 %; PAI delamination signs |
| C7 | Zeynalova et al., IEEE EI Mag 2024 [PR, vendor-affiliated] | Rectangular PAI enamel (4×1.5 mm, 100 µm) vs PFA coating (3.3×1.5 mm, 100 µm) | Shell Spirax S6 ATF D971 (water not reported) | "Oil tester" (IEC 60851-4 hydrolysis/transformer-oil method) | 150 °C, 2000 h | BDV (IEC 60851-5) | BDV retention: PAI 30 %, PFA ~50 % |
| C8 | Kwak et al. (Afton), SAE 2023 [CONF/PR; abstract only] | Round and rectangular polyester, polyamide and polyimide coatings | Several ETFs, varied water | Not accessible | Not accessible | BDV, PD, adhesion | Additive package drives large differences |
| C9 | Afton patents US 11,814,599 B2 / US 12,227,716 B2 [PATENT] | 15 AWG PEsI-type/PAI (200 °C) and polyester (180 °C) twisted pairs | Ester/PAO test fluids + ~1500 ppm water | Glass containers | 150 °C, 5 days | AC BDV per ASTM D1676-17 | PEsI/PAI 4.8–15.2 kV depending on fluid; polyester <1 kV |
| C10 | Castrol / Gasgoo 2022 [VENDOR] | Round and flat enamelled wires; complete insulation system | Conventional ATF vs Castrol e-fluid; 0, 0.2, 0.5 % water | Sealed | 8 × (155 °C 40 h / −45 °C 8 h) | BDV retention; withstand test | Retention falls with water; ATF worse than e-fluid (numbers only in charts) |
| C11 | Suzhou Jufeng US 12,159,731 B2 [PATENT] | Corona-resistant (CR) enamel constructions, 0.8 mm | ATF | Sealed tubes | 8 × (155 °C 40 h / −45 °C 8 h) | BDV; corona-resistance life (155 °C, 20 kHz square wave) | Market CR composite wire: 5.53 kV and 3 h 18 min life after ageing |
| C12 | Essex US 10,199,138 B2 [PATENT] | Enamel + extruded polymer magnet wire | Petroleum-based ATF | Sealed; air may be removed | 150 °C, 6–2000 h | BDV, PDIV, cracking | Claims ≥75–98 % retention |
| C7b/C14/C15 | Victrex, Solvay/Epic Resins, Proterial, Honda [VENDOR / CONF] | PEEK; enamel series | ATF; water (hydrolysis); refrigerant | Various | Various | Mostly qualitative | See entries below |

#### C1. Yang, Zhang, Pauli, Charrin, Hameyer: "Material Compatibility of Cooling Oil and Winding Insulation System of Electrical Machines", 2022 International Conference on Electrical Machines (ICEM), pp. 1334–1340 [CONF] (DOI not verified)
- Bibliographic: RWTH Aachen IEM and TotalEnergies One Tech; the project was funded by TotalEnergies One Tech, Fuel & Lubricant Division — [Yang et al. 2022 PDF](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf); venue and pages confirmed in the reference list of [Yang et al. 2023](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).
- Insulation: Damid 200 grade 2 enamelled round wire, 1 mm nominal, thermal class 200 °C, with a polyester-imide (PEI) base coat and polyamide-imide (PAI) overcoat. The study also tested Myoflex AHA slot paper (aramid–polyimide–aramid, 0.3 mm, class 180 °C) — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Oils: a commercial ATF (mineral base, classic ATF additives; viscosity 31.29/6.242 mm²/s at 40/100 °C); "E-fluid M" (mineral base, sulphur-free additives designed for e-motors; 15.02/3.618 mm²/s); and "E-fluid S" (synthetic base, the same type of additives; 7.814/2.402 mm²/s). Water content is not reported — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Ageing: the raw materials were immersed in each oil, with an air-stored reference group, and conditioned in a dry kiln at 180 °C for 1008 h. Samples were taken at 24, 336, 772 and 1008 h, then cleaned with n-heptane and wiped dry before twisted pairs were made per IEC 60172:2015. The text does not say whether the vessels were sealed or whether air could get in — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Measurements: capacitance at 10 kHz; PDIV under a bipolar voltage at 10 kHz switching frequency; peel test (25 N, 100 rpm); XPS. For the paper: PDIV under unipolar and sinusoidal voltage, and tensile strength — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Electrical results: capacitance rose slightly and PDIV fell slightly and continuously in every group, including the air reference. The oil groups' PDIV did not change significantly until mechanical cracking, and there was "no obvious difference between the oil groups and the Reference" — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Mechanical and chemical results: the coating became brittle and came off while twisting the pairs at 772 h (ATF) and 1008 h (both e-fluids); the air reference stayed intact. Peel strength fell significantly in all groups and fastest in ATF. XPS found 0.4–0.5 at% sulphur only in the ATF group, which shows additive penetration. In the air reference, oxygen content rose 25.5 % at 336 h, while in oil it stayed stable, so oil temporarily shielded the enamel from oxidation — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- AHA paper in e-fluids: capacitance fell continuously while PDIV stayed stable, and tensile strength fell slightly. The authors judged the paper more compatible than the enamelled wire — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Authors' conclusion: commercial ATFs "are not necessarily suitable" for combined use in e-drives, and additives matter more than the base oil — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).

#### C2. Yang, Pauli, Zhang, Hambrecht, Hameyer: "Influence of conductive particle contamination on the insulation system of rotating electrical machines with direct oil cooling", Archives of Electrical Engineering 71(3):789–804, 2022, DOI 10.24425/aee.2022.141685 [PR]
- Field oils: a commercial "e-motive" oil was sampled from an electric motorbike after 10,000 km. Particle sizes in the motor oil shifted to 10–100 nm, and iron reached 186 mg/kg — [AEE 2022 PDF](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- Specimens: Damid 200 grade 2 twisted pairs per IEC 60172, 20 per group, wetted with one commercial ATF containing 0, 0.4, 0.8 or 1.2 g/L of 5 µm copper particles. These were wetted, not thermally aged — [AEE 2022 PDF](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- Measurements: capacitance and tan δ at 1 and 10 kHz; PDIV under sinusoidal voltage (printed as "50 kHz"); RPDIV under surge voltage. The paper also measured surface resistance and surface breakdown of AHA paper, after 10 min at 95 % RH and 25 °C for the humidity case — [AEE 2022 PDF](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- Result, oil effect: wetting the twisted pair with ATF raised both PDIV and RPDIV "by about three times". At RPDIV the wetted samples drew much larger currents, which indicates breakdown rather than PD. The authors conclude that for an oil-wetted winding the voltage threshold is the breakdown voltage, not the RPDIV — [AEE 2022 PDF](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- Result, particles: as copper content rose from 0 to 0.4, 0.8 and 1.2 g/L, the Weibull scale parameter (63.2 %) fell from 3677 to 2705, 2429 and 2364 V (sinusoidal PDIV) and from 6608 to 4986, 4674 and 3578 V (surge RPDIV). Capacitance rose slightly — [AEE 2022 PDF](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).

#### C3. Yang, Cao, Zhang, El Bahi, Hameyer: "Preliminary Study on the Applicability of Water-Based Lubricant as a Direct Cooling Medium in Rotating Electrical Machines", IEEE IEMDC 2023, DOI 10.1109/IEMDC55163.2023.10238889 [CONF]
- Fluid: a water-based lubricant (WBL) made of synthetic base oil, distilled water and additives. Damid 200 grade 2 (PEI/PAI) wires were immersed "in a sealed heating pot" at 90 °C, a limit set to avoid boiling, for 1008 h with samples at 24, 336, 772 and 1008 h. Wires conditioned without fluid served as reference — [Yang et al. 2023 PDF](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).
- Results: PDIV hardly decreased and capacitance rose slightly. Relative permittivity rose about 20 % after 1008 h, attributed to water absorption. Peel strength halved within 336 h and then stayed stable — [Yang et al. 2023 PDF](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).
- Fluid films: PDIV rose slightly with a water film and significantly with a WBL film. Electrical lifetime of twisted pairs at a 1200 V DC link and 10 kHz showed "similar resistance against PDs with different fluids". The FEA permittivities were PAI 4.0, PEI 3.5, air 1.0 and e-fluid 2.1 — [Yang et al. 2023 PDF](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).
- Insulation resistance on motorette M1, phase-to-phase at 1000 V DC (R60s/R10s): dry >260/>260 GΩ; end-winding wetted 70/27 GΩ; whole winding wetted 12.5/4.9 GΩ; fully wetted for 48 h 0.0009/0.0006 GΩ (≈0.9/0.6 MΩ), below the 5 MΩ minimum the paper cites from IEC 60034-27-4. A local defect in motorette M2 gave 0.9/0.05 GΩ phase-to-ground with only the end winding wetted — [Yang et al. 2023 PDF](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).

#### C4. Liguo Yang: "E-fluid oil as coolant in low-voltage rotating electrical machines: impact on the insulation system", PhD thesis, RWTH Aachen (accepted 2023; Shaker 2024, ISBN 978-3-8440-9418-3) [THESIS; abstract only]
- Oil in the winding reduces PD risk. In FEA of twisted pairs, oil between adjacent conductors raises PDIV. In electrical ageing tests, PD activity disappeared once oil penetrated inter-turn gaps and voids — [RWTH record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1).
- Oil had no significant effect on mechanical ageing. The e-fluid penetrates the enamel and degrades its mechanical properties, but PDIV and capacitance measurements "fail to detect this". Conductive particles and humidity lower PDIV and cause surface creepage — [RWTH record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1).

#### C5. HEFT project Deliverable D2.4: "Analysis and validation of machine insulation for 800V DC bus" (written by A. Cavallini, Univ. Bologna; v2.0 dated 2024-06-21; Horizon Europe GA 101096306; partners include GKN Driveline) [REPORT]
- Specimens: insulated conductors about 4 cm long, Ederfil Becker polyamide-imide (220 °C class) rectangular wire, placed back-to-back with slot-moulding resin G720E or XQ8763 — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).
- Fluid and vessel: Castrol ON BOT (BEV) G5, the ATF used to cool the end windings by spray, was poured into sealed aluminium containers to cover all solid insulation. Containers with conductors and resin but no oil served as controls — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).
- Conditions: 160 °C in an oven for two weeks. The temperature was chosen because the oil's fire point is 180 °C, against a maximum operating temperature of 210 °C — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).
- Measurements before and after: dielectric spectroscopy (one electrode on the copper, silver-paint outer electrode) and PDIV of the back-to-back samples at 20, 180 and 210 °C — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).
- Results:
  - PDIV: no appreciable reduction.
  - Dielectric spectroscopy: G720E gave a tan δ peak at about 10 Hz and XQ8763 a loss peak at a few hundred kHz. The rise in dissipation factor at 10 kHz with XQ8763 was flagged as a risk of overheating and, at worst, thermal runaway.
  - Visual: the enamel separated from the conductor.
  - Delamination cause: a corrosive-sulphur test (kraft-paper-wrapped copper, 140 °C for 4 days and also at 160 °C) found no Cu₂S, and FTIR found no anomaly. Conductors aged in air at 220 °C for one week, without ATF or resin, also delaminated massively. The authors therefore blame enamel adhesion or a thermal-expansion mismatch, not the oil, and plan to re-test with new conductors — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).

#### C6. Martinez (Mondragon), Iannarelli, Seri, Cavallini (Bologna): "Insulation Technologies for State-of-the-Art Electrical Machines Used in Transport Electrification", IEEE WEMDCD 2025, DOI 10.1109/WEMDCD61816.2025.11014120 [CONF; open postprint]
- Spray test: ATF at 60 °C was sprayed onto hot (180 °C) rectangular conductors with a 50 µm gap. The abstract says spray "can decrease the PDIV by about 10–15 %"; the body says "a reduction down to 10 % of the PDIV" (Fig. 5, per-unit), so the exact magnitude is ambiguous. Vapours were seen, and the authors tentatively attribute the drop to hydrocarbons in the gas raising the Townsend ionisation coefficient — [Martinez et al. 2025 postprint](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf).
- Ageing: tests with one ester-based and one mineral ATF showed "possible signs of delamination for PAI after two weeks at the maximum operating temperature of 160 °C" — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf).
- Context: ATF conductivity is relatively high compared with air, so insulation resistance of a healthy system "can be unexpectedly low" compared with air-cooled machines, especially at operating temperature. The PAI-copper interface can have adhesion problems when exposed to ATFs. PEEK's permittivity and conductivity rise sharply above 160 °C, which lowers PDIV. Dry PDIV at 180 °C: CR-PAI is slightly lower than PAI at 80 and 110 µm build — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf).

#### C7. Zeynalova, Cepparrone, Roffino, Barbero (Tre Tau Engineering, Turin): "Effect of Thermal Aging on Electrical Performance of Perfluoroalkoxy- and Polyamide-Imide-Coated Magnet Wire", IEEE Electrical Insulation Magazine 40(3), May/June 2024 [PR magazine; authors make the PFA wire]
- Specimens:
  - Commercial PAI enamelled rectangular wire, 4 × 1.5 mm, 100 µm coating.
  - Tre Tau PFA-coated wire, 3.3 × 1.5 mm, 100 µm, "DryCycle" process (EP 3518255B1) — [IEEE EI Mag issue PDF](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).
- Oil ageing: run according to IEC 60851-4 "Resistance to hydrolysis and transformer oil" in Shell Spirax S6 ATF D971, 2000 h at 150 °C, 10 samples of 30 cm per wire, in an "oil tester". BDV was measured per IEC 60851-5 (steel-ball electrode, 5–20 tests per wire) — [IEEE EI Mag issue PDF](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).
- Results:
  - BDV retention: PAI 30 %; PFA about 50 %.
  - PAI: cracks, voids and partial loss of coating; colour changed from burgundy to black.
  - PFA: changed from orange to grey with uneven colour, but no cracks.
  - Hot BDV (dry): from room temperature to 240 °C it fell 13 % (PAI) and 10 % (PFA).
  - In 3 % NaCl water at 25 °C for 2000 h, PAI BDV fell 19 % while PFA rose 12 % — [IEEE EI Mag issue PDF](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).

#### C8. Kwak, Grzyska, Cleveland (Afton Chemical, USA), Tsuneo (Afton Japan): "Magnet Wire Compatibility Test for Electric Drivetrain Fluid Development", SAE 2023-32-0145 (JSAE/SAE PFL 2023); SAE Int. J. Adv. & Curr. Prac. in Mobility 6(3):1468–1478, 2024; DOI 10.4271/2023-32-0145 [CONF/PR, industry; abstract only]
- The paper evaluates adhesion, breakdown voltage and partial discharge of round and rectangular magnet wires with polyester, polyamide and polyimide coatings aged in electric transmission fluids (ETFs). It also studies how water concentration in the ETF affects ageing, and reports that the additive package or formulation "leads to significant MW performance differences". Fluids, temperatures, durations and numbers were not accessible — [SAE abstract](https://saemobilus.sae.org/articles/magnet-wire-compatibility-test-electric-drivetrain-fluid-development-2023-32-0145).

#### C9. Afton Chemical patents "Durable magnet wires and lubricating fluids for electric and hybrid vehicle applications": US 12,227,716 B2 (inventors Grzyska and Kwak; priority 2022-03-31; same family as US 11,814,599 B2) [PATENT]
- Protocol: twisted pairs prepared per NEMA MW 1000-2018 §3.8.4 were placed in glass containers with about 75 g of fluid plus about 1500 ppm water ("to increase the severity"). They were aged at about 150 °C for 5 days, cooled, washed four times with heptane and air-dried. AC dielectric breakdown was then measured per ASTM D1676-17 §§70–76 with 6 twists — [Google Patents US12227716B2](https://patents.google.com/patent/US12227716B2/en).
- Wires: A is 15 AWG, 200 °C rated, polyester(amide)(imide) base with PAI overcoat; B is 15 AWG, 180 °C, single-layer polyester — [Google Patents US12227716B2](https://patents.google.com/patent/US12227716B2/en).
- Results:
  - Wire A after ageing: 4,805 V to 15,246 V depending on fluid formulation.
  - Formulation driver: fluids with a ratio of detergent metal (ppm) to ester-group content (mol %) of about 70 or less gave ≥10,000 V. For example, ester base-oil fraction 10 % gave 9,330 V and 80 % gave 15,246 V.
  - Wire B: under 1,000 V.
  - Unaged baseline BDVs were not given in the text reviewed — [Google Patents US12227716B2](https://patents.google.com/patent/US12227716B2/en).

#### C10. Castrol-contributed article (author Xin Wen), "油冷电机绝缘系统与变速箱油兼容性能探究" ("Study on compatibility between oil-cooled motor insulation systems and transmission fluid"), Gasgoo, 6 Dec 2022 [VENDOR / trade press]
- Protocol per the Chinese group standard CEEIA 415-2019: insulation and oil are sealed together with 0.5 % water pre-added, then given 8 thermal-shock cycles of 40 h at 155 °C followed by 8 h at −45 °C. The water accelerates hydrolysis and simulates moisture or water ingress — [Gasgoo article](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml).
- Variables: a conventional ATF vs Castrol's e-drive fluid; water at 0, 0.2 and 0.5 %; a round enamelled wire, several flat wires, and one complete insulation system — [Gasgoo article](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml).
- Results (shown in charts only, no numbers in text):
  - Breakdown-voltage retention fell as water rose, and was lower after ATF than after the e-fluid.
  - SEM of ATF-aged enamel: darkened, slightly cracked, porous surface, which the author links to hydrolysis.
  - SEM-EDS of the copper under ATF-aged enamel: corroded, with sulphur detected.
  - The complete system aged in the e-fluid passed the withstand test — [Gasgoo article](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml).

#### C11. Suzhou Jufeng Electrical Insulation System Co.: US 12,159,731 B2, "ATF oil and corona-resistant enameled wire for electric vehicle motor" (priority CN 2020-04-14) [PATENT]
- Protocol: samples in sealed tubes filled with ATF, 8 cycles of 155 °C/40 h then −45 °C/8 h with 5–10 min shock transfers. Afterwards: BDV, corona-resistance life (square wave, 155 °C, 20 kHz), jerk and elongation tests. No water addition is mentioned — [Google Patents US12159731B2](https://patents.google.com/patent/US12159731B2/en).
- Results after the ATF test:
  - Conventional market corona-resistant composite wire: BDV 5.53 kV, corona life 3 h 18 min, peeling and cracking.
  - Single-layer imported corona-resistant PAI wire: BDV 10.82 kV, corona life 59 h 12 min, against 109 h 36 min unaged.
  - The patented wire (multilayer polyethersulfone-based protective films with nano-SiO₂ CR-PAI) claims >80 % retention, from 15.36–15.69 kV unaged BDV — [Google Patents US12159731B2](https://patents.google.com/patent/US12159731B2/en).
- Background claim: 200-class corona-resistant PEsI/PAI composite wires are "getting limited" in oil-cooled motors "because of the tested poor ATF oil-resistant performance" — [Google Patents US12159731B2](https://patents.google.com/patent/US12159731B2/en).

#### C12. Essex Group: US 10,199,138 B2, "Insulated winding wire" [PATENT]
- It describes the ASTM D1676 oil test (e.g., 150 °C for about 2000 h), after which the wire is retested for dielectric breakdown and PDIV and inspected for cracking. It also describes an ATF test: wire in a sealed container filled or partly filled with transmission fluid, from which "air may be removed", heated to e.g. 150 °C for about 6, 720, 1000 or 2000 h. Electrical performance should be at least 75–98 % of the pre-test value — [Google Patents US10199138B2](https://patents.google.com/patent/US10199138B2/en).

#### C13. Ito, Shibata, Kawasaki (Honda R&D): "Development of High Voltage Wire for New Structure Motor in Full Hybrid Vehicle", SAE 2016-01-1221; SAE Int. J. Alt. Powertrains 5(2):272–277, 2016 [CONF/PR; abstract only]
- A PEEK-based thermoplastic layer over enamel ("HVW") for motors of 650 V and above. It reportedly "secures durability" in the ATF and high-temperature environment and maintains high-voltage characteristics. No ATF test conditions or PDIV/BDV data appear in the abstract — [SAE abstract](https://saemobilus.sae.org/content/2016-01-1221).

#### C14. PEEK vendor evidence [VENDOR]
- Victrex says its PEEK magnet wire "withstands a wide range of ATFs and dielectric fluids at 180 °C for up to 2,000 hours with retention of electrical properties", "validated by OEM oil experts". No fluid names, method or retention values are given — [Victrex e-motor page](https://www.victrex.com/en/emotor-solutions).
- In a Solvay/Epic Resins trade article, PEEK-coated wire bonded with ProPreg E240 epoxy kept its adhesion after up to 1500 h of ATF exposure (data being built toward 2000 h at 150 °C). Failure was at the polymer–copper interface, not at the epoxy bond. This is mechanical data only; the test method is printed as "IEC 60133" by Eltek labs — [Kunststoffe Int. 2/2022](https://res.cloudinary.com/sternwald-systems/raw/upload/v1/hugoprd/ARTIKEL_ATTACH/002E9ADD_C9FA4B214D64/d124670c4b1ba66a64ab0bfbd6a44033a79ea62c/PEEK%20and%20Epoxy%20Provide%20Efficient%20Insulation%20for%20High%20Voltage%20E-Motor%20-%20KUint%2002%202022.pdf).

#### C15. Proterial (formerly Hitachi Metals/Hitachi Cable), "マグネットワイヤの選択とその使用方法" (magnet-wire selection guide; undated) [VENDOR]
- On oil: "there is almost no difference in oil resistance among enamel films" (耐油性は、絶縁皮膜による耐油性の差はほとんどありません) — [Proterial guide](https://www.proterial.com/products/electrical_wire/pdf/magnet_wire.pdf).
- Hydrolysis test: enamelled wire and water sealed together and heated above 100 °C, judged by BDV retention. The example uses twisted pairs, 1.0 mm grade 1, 0.4 vol % water, at 120 °C for up to about 30 days. PEW (polyester) degrades fastest, followed by IMW; AIW and KMK-22A are "far superior". PEW needs caution in sealed equipment — [Proterial guide](https://www.proterial.com/products/electrical_wire/pdf/magnet_wire.pdf).

### Inferences
- The planned study would be the first to compare insulation types and application methods on one oil-ageing protocol, using hairpin-relevant specimens and a full electrical test set (PDIV/RPDIV, BDV, C/tan δ spectroscopy, IR). Existing work covers either one insulation family (PEI/PAI or PAI) across several fluids, or two wire types (PAI vs PFA) in one fluid.
- In sources with comparable data, enamel PDIV and capacitance hardly change after oil ageing even when mechanical failure is imminent (C1, C4, C5). BDV and adhesion react much more (C7, C9, C10, C11). A study relying mainly on PDIV and capacitance risks reporting "no effect".
- The protocols cluster around three families: (a) static immersion near 150–180 °C for 120 h to 2000 h (C1, C7, C9, C12); (b) CEEIA-style sealed thermal-shock cycling with 0.5 % water (C10, C11); (c) sealed-container ageing with dry controls and hot PDIV (C5).

### Gaps
- I could not open "Impact of Cooling Oil on Partial Discharge and Insulation Reliability in Inverter-Fed EV Motors" (2025). ResearchGate and Academia returned 403. Search snippets only say it used crossed-wire PAI samples under repetitive square-wave voltage, oil-coated vs oil-free, and that oil raised PDIV and corona resistance at ambient temperature but less at high temperature. The venue appears to be the "Cognizance Journal of Multidisciplinary Studies" (low-tier, unverified). Treat it as unverified.
- Full texts not accessible: the Yang thesis (quantitative electrical-ageing results in oil), SAE 2023-32-0145, SAE 2016-01-1221 and the CEEIA 415-2019 standard. The Castrol article gives no numbers.
- I found no peer-reviewed Chinese or Japanese journal papers on ATF ageing of enamelled wire with electrical measurements; CNKI and J-STAGE are not reachable through web search here. Such papers likely exist (the Chinese patent and industry articles refer to routine "ATF oil resistance" testing).
- No accessible study measured insulation resistance or tan δ of an oil-cooled stator over long-term oil ageing. A paper on electrical conductivity of new and used ATFs (McFadden et al., SAE), cited by Yang et al. 2023, was not opened.

## 2. Patterns: does oil raise or lower PDIV, how does water drive hydrolysis, how much does temperature matter, do properties recover, and which insulation types degrade most?

### Takeaway
How oil affects PDIV depends on its state. A liquid film filling the air wedge raises PDIV strongly (≈3× at RWTH), while cooler oil sprayed onto hot conductors lowered it by about 10–15 % (Bologna). Conductive wear particles cut PDIV by up to ~36–46 %. After long ageing in oil and draining, PDIV and capacitance barely move. BDV, tan δ spectra and adhesion are what degrade: PAI BDV retention was 30 % after 2000 h at 150 °C in ATF. Water (0.15–0.5 %) and sulphur-bearing ATF additives speed degradation. ATF is consistently worse than dedicated e-fluids. Polyester and polyester-based enamels are the most vulnerable; PAI shows adhesion and delamination problems; PFA fared better than PAI. Independent PEEK electrical data in oil were not found.

### Cited Findings
**2a. Direction of the PDIV change**
- A fresh ATF film on twisted pairs raised PDIV and RPDIV "by about three times", and the failure mode shifted from PD to breakdown — [AEE 2022](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- Mechanism: oil (εr ≈ 2.1 in the authors' model) replaces air at the minimum gap and weakens the field concentration there — [Yang et al. 2023](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf). Oil bridging conductors "push[es] the crucial field lines outward", and PD vanished when oil penetrated voids during electrical ageing — [Yang thesis record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1).
- Opposite effect: ATF at 60 °C sprayed on 180 °C conductors lowered PDIV by about 10–15 %, possibly because hydrocarbon vapour raises gas ionisation. The authors say this "should be investigated further" for phase-to-phase end-winding insulation — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf).
- Contamination: 1.2 g/L of 5 µm copper particles in the ATF film cut the Weibull PDIV from 3677 to 2364 V (−36 %) and RPDIV from 6608 to 3578 V (−46 %), through field distortion and conductive "bridges" — [AEE 2022](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- After ageing and draining (heptane-cleaned): in 180 °C/1008 h oil ageing, PDIV fell only slightly and equally in oil and air groups — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf). After 160 °C/2 weeks in Castrol ATF, PAI showed "no appreciable reduction" of PDIV measured at 20, 180 and 210 °C — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).

**2b. Water and hydrolysis**
- CEEIA 415-2019 deliberately adds 0.5 % water to the sealed oil. Castrol's results show breakdown-voltage retention falling stepwise from 0 to 0.2 to 0.5 % water, with ATF-aged enamel turning porous, which was attributed to hydrolysis — [Gasgoo/Castrol](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml).
- Afton adds about 1500 ppm water to its 150 °C, 5-day twisted-pair test "to increase the severity" — [US12227716B2](https://patents.google.com/patent/US12227716B2/en). Afton's SAE paper investigates "the effect of water concentration in ETF on MW performance" (results not accessible) — [SAE abstract](https://saemobilus.sae.org/articles/magnet-wire-compatibility-test-electric-drivetrain-fluid-development-2023-32-0145).
- In sealed humid-heat tests (120 °C, 0.4 vol % water), polyester degrades fastest, then IMW, while AIW and KMK-22A are far more hydrolysis-resistant — [Proterial guide](https://www.proterial.com/products/electrical_wire/pdf/magnet_wire.pdf).
- In a water-containing fluid at 90 °C, PEI/PAI permittivity rose about 20 % in 1008 h (water absorption) while PDIV hardly changed — [Yang et al. 2023](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).

**2c. Temperature**
- Ageing temperatures used: 90 °C (WBL, boiling limit) — [Yang et al. 2023](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf); 150 °C — [Zeynalova et al. 2024](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf), [US12227716B2](https://patents.google.com/patent/US12227716B2/en), [US10199138B2](https://patents.google.com/patent/US10199138B2/en); 155 °C cycles — [Gasgoo/Castrol](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml); 160 °C, limited by the 180 °C oil fire point — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf); 180 °C — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Measurement temperature matters in its own right. HEFT measured PDIV at 20, 180 and 210 °C. Bologna designs to hot-spot conductor temperatures of 180 °C and 200–220 °C in the slots — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf). Dry hot BDV fell 13 % (PAI) and 10 % (PFA) from room temperature to 240 °C — [Zeynalova et al. 2024](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).
- Oxidation in air at 180 °C showed up as +25.5 % surface oxygen after 336 h, which oil suppressed initially. A thermal-only air or inert control is therefore essential to separate oil effects from thermal ones — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).

**2d. Recovery after draining or drying**
- All academic and patent protocols measured after draining plus solvent washing (n-heptane) and drying: wiped with tissue — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf); washed 4× and air-dried — [US12227716B2](https://patents.google.com/patent/US12227716B2/en). None compared "in-oil", "drained" and "re-dried" states on the same specimen.
- Analogue warning from hermetic motors: a 24 h air bake at 150 °C after 500 h of refrigerant exposure produced further dielectric-strength losses up to −70 % (Iso-800 varnish, HCFC-22) — [Doerr & Kujak 1992, DOE/CE/23810-3D](https://www.osti.gov/servlets/purl/7048840). Rapid desorption after absorption caused blisters, cracking and delamination — [OSTI 6837374 summary](https://www.osti.gov/biblio/6837374).

**2e. Which insulation types degrade most**
- **ATF vs e-fluids:** ATF embrittled PEI/PAI sooner (772 h vs 1008 h at 180 °C) and penetrated it with sulphur — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf). Castrol reports sulphur on copper under ATF-aged enamel — [Gasgoo/Castrol](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml).
- **PAI:** delamination after 2 weeks at 160 °C in ester and mineral ATFs — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf). Delamination also occurred in air at 220 °C, so it is partly an enamel adhesion issue — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf). BDV retention was 30 % after 2000 h at 150 °C in ATF, with cracks and voids — [Zeynalova et al. 2024](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).
- **Corona-resistant composite enamel:** a market CR composite wire fell to 5.53 kV BDV and 3 h 18 min corona life after CEEIA-type ATF cycling. A single-layer CR-PAI kept 10.82 kV and lost about 46 % of its corona life (109.6 h → 59.2 h) — [US12159731B2](https://patents.google.com/patent/US12159731B2/en).
- **Polyester:** under 1 kV BDV after 5 days at 150 °C in a fluid with water, against 4.8–15.2 kV for PEsI/PAI — [US12227716B2](https://patents.google.com/patent/US12227716B2/en).
- **PFA vs PAI:** about 50 % vs 30 % BDV retention after 2000 h at 150 °C in ATF — [Zeynalova et al. 2024](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).
- **PEEK:** only vendor or OEM claims of ATF durability exist — [Victrex](https://www.victrex.com/en/emotor-solutions); [Honda SAE 2016-01-1221](https://saemobilus.sae.org/content/2016-01-1221). A Bologna review notes PEEK's PDIV-reducing rise in permittivity and conductivity above 160 °C and its softening under overload — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf).

**2f. Sensitivity of each diagnostic**
- PDIV and capacitance "fail to detect" oil penetration that degrades mechanical properties — [Yang thesis record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1). The authors recommend a combined, multi-method evaluation and note that no end-of-life criterion is recognised for oil-compatibility testing — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Dielectric spectroscopy picked up resin- and oil-related loss peaks (10 Hz; hundreds of kHz) where PDIV did not — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).

### Inferences
- The PDIV "contradiction" is probably about state rather than chemistry. With liquid filling the wedge (fully wetted, near room temperature), PDIV rises. With hot conductors, partial or transient wetting and vapour, PDIV falls. A test that measures PDIV only on drained, cleaned, room-temperature specimens will miss both effects. Measuring PDIV dry, wetted and hot (≥150–180 °C) would capture them.
- Water content is a first-order variable but is rarely measured (none of the academic studies report Karl-Fischer water). The CEEIA and Afton practice of fixed water spiking (0.5 % or about 1500 ppm) plus a dry-oil arm would make results comparable with industry.
- Because ATF additives (sulphur) penetrate the enamel, the fluid choice (ATF vs e-fluid) may matter as much as the insulation choice. Testing at least one ATF and one e-fluid would separate the two.

### Gaps
- I found no oil-ageing dataset at multiple temperatures (Arrhenius or lifetime-line) for any winding insulation, so how strongly ageing depends on temperature in oil remains unquantified.
- I found no study measuring PDIV recovery after re-drying, or IR/tan δ of wetted vs dried specimens after ageing. The only recovery-type evidence is the hermetic-motor bake data (Section 5).
- I found no independent electrical data in oil for extruded PEEK, PEEK tube, heat-shrink, polyimide tape (Kapton), epoxy powder or parylene.

## 3. Studies specific to direct oil-cooled e-motors (spray/jet cooling, oil-flooded stators, oil-immersed end windings)

### Takeaway
The research addressing direct oil-cooled e-motor insulation explicitly is RWTH IEM (direct oil cooling with e-fluids and ATF; motorette wetting; field-oil particles), Bologna/HEFT (ATF sprayed on hairpin end windings of an 800 V machine; spray-induced PDIV reduction), and industry work on oil-cooled-motor wire (Castrol/CEEIA, Suzhou Jufeng, Honda, Afton). No study tested a complete hairpin stator under real spray or flooding with long-term electrical tracking.

### Cited Findings
- RWTH's work explicitly targets integrated drives where one oil lubricates the gearbox and cools the machine. It cites a LUT study (Montonen, Nerg, Polikarpova, Pyrhönen, IEEE Access 2019) that found conductive particles during experiments with direct oil cooling — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- Field evidence: in an e-motorbike after 10,000 km the motor oil carried 10–100 nm particles and up to 186 mg/kg iron — [AEE 2022](https://journals.pan.pl//Content/124108/PDF/art16_i.pdf).
- Motorette wetting tests are a model for spray and flood scenarios. Insulation resistance fell with wetted area: end-winding wetting 70 GΩ, whole-winding wetting 12.5 GΩ, complete 48 h immersion about 0.9 MΩ (water-based lubricant). A single local defect became a short-circuit path once wetted — [Yang et al. 2023](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).
- HEFT 800 V hairpin machine (GKN): the end windings are cooled by spraying Castrol ON BOT (BEV) G5. Phase-to-phase end-winding insulation is the weakest point. The design assumed a temperature enhancement factor of 1.2 despite oil cooling — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).
- Spray onto hot conductors lowers PDIV (Section 2a). The authors recommend considering this "in the design phase" — [Martinez et al. 2025](https://cris.unibo.it/retrieve/c037e7e3-7f76-4690-a5cf-b13fdf36a5ab/unpaywall-bitstream-1951351576.pdf).
- Industry wire development for oil-cooled EV motors: CEEIA 415-2019 compatibility testing — [Gasgoo/Castrol](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml); ATF- and corona-resistant enamel for loose-wound coils of oil-cooled motors — [US12159731B2](https://patents.google.com/patent/US12159731B2/en); Honda's PEEK-based wire for an ATF environment — [SAE 2016-01-1221](https://saemobilus.sae.org/content/2016-01-1221).
- SAE J3200 (draft at the time of the article) recommends bench tests for e-fluids, including material compatibility and "testing the fluid after it has been aged with materials" — [STLE TLT Aug 2021](https://www.stle.org/files/TLTArchives/2021/08_August/Cover_Story.aspx).

### Inferences
- For a spray-cooled hairpin motor, the critical electrical scenario is hot end-winding phase-to-phase gaps under intermittent spray, not fully immersed turns. Ageing specimens should include gap geometries (back-to-back and spaced conductors), as Bologna used.

### Gaps
- I found no study of PD or PDIV on a full oil-flooded or spray-cooled hairpin stator after long-term oil ageing, and none on oil-jet impact (erosion or charging) on insulation.

## 4. Multi-stress ageing that includes oil (thermal + oil + electrical + mechanical/vibration)

### Takeaway
Protocols that combine oil with other stresses are limited to thermal shock in oil plus water (CEEIA 415-2019), separate thermal, mechanical and electrical ageing with oil present (RWTH), and electrical endurance of oil- or fluid-wetted twisted pairs. I found no combined TEAM test (thermal + PWM electrical + oil + vibration) on hairpins or motorettes. The nearest combined-stress precedent with oil comes from transformers.

### Cited Findings
- CEEIA 415-2019 is thermal shock in oil with water: 8 × (155 °C/40 h → −45 °C/8 h), sealed, 0.5 % water — [Gasgoo/Castrol](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml). The same cycling (5–10 min shock transfer) is followed by BDV and 155 °C/20 kHz corona-life tests — [US12159731B2](https://patents.google.com/patent/US12159731B2/en).
- The RWTH thesis analyses thermal, mechanical and electrical ageing of the insulation system in an oil environment. Oil had no significant effect on mechanical ageing, and PD disappeared in electrical ageing when oil filled the voids — [Yang thesis record](https://www.iem.rwth-aachen.de/cms/iem/forschung/publikationen/publikationen1/~povh/details/?file=981658&lidx=1).
- Electrical endurance with fluid films: twisted-pair lifetime at 1200 V DC link and 10 kHz switching showed similar PD resistance across fluids — [Yang et al. 2023](http://bib.iem.rwth-aachen.de/IEMpublications/2023LYPreliminary.pdf).
- Transformer analogue: insulating paper in a sealed tank of 25# transformer oil at 113.7 °C with 3.39 kV AC, with 8.71 MPa mechanical stress for the ETM group, for up to 192 h. Results: tan δ +141 % (electro-thermal) vs +245 % (electro-thermal-mechanical); BDV −5.7 % vs −8.5 %; degree of polymerisation −43 % vs −47 %. Mechanical stress accelerated ageing — [Yuan et al., Polymers 2023, 15(21):4239](https://pmc.ncbi.nlm.nih.gov/articles/PMC10647747/).

### Inferences
- A practical multi-stress extension of the planned study: age in oil (thermal + chemical), then apply thermal shock (CEEIA-style) and a PWM endurance test of the aged specimens, both oil-wetted and dry. This mirrors what exists separately in the sources above.

### Gaps
- I found no accessible study combining vibration or mechanical stress with oil immersion and PWM electrical stress on magnet wire or hairpins.

## 5. Methodological analogues: hermetic compressor motors and oil-immersed transformers (precedent for protocols)

### Takeaway
Hermetic-motor research (ARTI/DOE MCLR, Trane, 1990s) set the precedent for sealed exposure of magnet wire and varnish to refrigerant and lubricant. It used inert-gas thermal controls, a post-exposure bake to reveal desorption damage, and dielectric-strength retention as the electrical end-point. Transformer research supplies sealed-tank combined-stress designs.

### Cited Findings
- Doerr & Kujak (Trane) for ARTI MCLR / US DOE, 1992 quarterly report:
  - Exposure: 500 h at 90 °C in HCFC-123, HCFC-22 and HFC-134a, with 500 h in nitrogen at 127 °C as a thermal-only control.
  - Properties measured: magnet-wire weight change, dielectric strength, burnout, flexibility and appearance; varnish bond strength; dielectric strength of sheet insulation.
  - Wire A (ester base, amide-imide overcoat) dielectric-strength changes ranged from −44.3 % to +16.5 % depending on varnish and refrigerant. After an extra 24 h air bake at 150 °C, losses reached −70.0 % (Iso-800, HCFC-22), −44.8 % (Y-390PG) and −42.0 % (ER-610).
  - [DOE/CE/23810-3D PDF](https://www.osti.gov/servlets/purl/7048840)
- Summary report (10 refrigerants × 24 motor materials): the greatest damage came from refrigerant absorption followed by rapid desorption, giving blisters, cracking, internal bubbles and delamination with lower bond and dielectric strength. HCFC-22 was the most severe — [OSTI 6837374](https://www.osti.gov/biblio/6837374).
- Vendor refrigerant test: R-134a and refrigeration oil 1:1 for 7 days at room temperature and 125 °C, BDV measured after a 130 °C/1 h bake. Polyester (PEW) fell from 16.5 kV to 14.6 and 14.4 kV, while the other enamels stayed within about ±10 % — [Proterial guide](https://www.proterial.com/products/electrical_wire/pdf/magnet_wire.pdf).
- Wire makers developed dedicated refrigerant-resistant windings: an R134a-compatible winding in 1992, and self-bonding wire SSB-41 for motors running immersed in refrigerant and refrigeration oil — [SEI Technical Review 190, 2017](https://sei.co.jp/technology/tr/bn190/pdf/190-19.pdf).
- Transformer analogue: sealed oil tank in a humid-heat chamber with combined electrical, thermal and mechanical stress (see Section 4) — [Yuan et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10647747/).

### Inferences
- Three hermetic-motor practices transfer directly to the oil study. An inert or air thermal control separates thermal from chemical effects (RWTH and HEFT did the same). A deliberate post-exposure bake tests whether drying "recovers" or damages the insulation. Results reported as % change from unexposed control specimens are comparable across materials.

### Gaps
- The IEEE paper "Sealed tube test method for evaluation of hermetic motor insulation performance with refrigerant systems" (IEEE Xplore 482399) could not be opened. ASHRAE/AHRI sealed-tube procedural details were not checked; the standards researcher covers these.

## 6. Has any study compared different insulation TYPES or APPLICATION METHODS under the same oil-ageing protocol?

### Takeaway
Only partially. One peer-reviewed comparison spans two application technologies: PFA coating vs conventional PAI enamel in ATF (Tre Tau, 2024). Others compare enamel chemistries or constructions (Afton, Suzhou Jufeng, Proterial, SAE Afton), or enamelled wire vs slot paper (RWTH), within one protocol. I found no study comparing enamel vs extruded PEEK vs PEEK tube vs heat-shrink vs polyimide tape vs epoxy powder vs parylene under one oil protocol with electrical end-points.

### Cited Findings
- PFA coating vs PAI enamel, same ATF protocol (Shell Spirax S6 ATF D971, 150 °C, 2000 h): BDV retention about 50 % vs 30 %; no defects in PFA vs cracks and voids in PAI — [Zeynalova et al. 2024](https://www.doble.com/wp-content/uploads/DEIS-magazine-MayJune2024.pdf).
- PEsI-type/PAI vs single polyester, same 150 °C/5-day fluid protocol with water: 4.8–15.2 kV vs <1 kV — [US12227716B2](https://patents.google.com/patent/US12227716B2/en).
- Corona-resistant enamel constructions (market composite CR, single-layer CR-PAI, multilayer PES-protected CR-PAI), same CEEIA-type ATF cycling. Post-test BDV ranged from 5.53 kV upward, and corona life from 3 h 18 min upward — [US12159731B2](https://patents.google.com/patent/US12159731B2/en).
- Enamelled wire vs aramid–polyimide–aramid slot paper, with ATF and two e-fluids at 180 °C for 1008 h: the paper's dielectric and electrical properties stayed stable while the wire embrittled — [Yang et al. 2022](http://bib.iem.rwth-aachen.de/IEMpublications/2022LYMaterial.pdf).
- PAI conductors with two slot-moulding resins, with and without ATF, at 160 °C for 2 weeks: the resins differed in dielectric-spectroscopy loss peaks — [HEFT D2.4](https://site.unibo.it/heftproject/en/publications/d2-4-analysis-and-validation-of-machine-insulation-for-800v-dc-bus.pdf/@@download/file/D2.4%20Analysis%20and%20validation%20of%20machine%20insulation%20for%20800V%20DC%20bus.pdf).
- Round vs flat enamelled wires and a complete insulation system under the CEEIA protocol, ATF vs e-fluid: numbers given only in charts — [Gasgoo/Castrol](https://auto.gasgoo.com/news/202212/6I70323978C501.shtml).
- Polyester, polyamide and polyimide coatings on round and rectangular wire in ETFs (abstract only) — [SAE 2023-32-0145](https://saemobilus.sae.org/articles/magnet-wire-compatibility-test-electric-drivetrain-fluid-development-2023-32-0145).
- Seven enamel types under one hydrolysis protocol and one refrigerant protocol — [Proterial guide](https://www.proterial.com/products/electrical_wire/pdf/magnet_wire.pdf).
- PEEK-coated wire + epoxy adhesion after ATF (mechanical only; PEEK vs standard polyester secondary insulation) — [Kunststoffe Int. 2/2022](https://res.cloudinary.com/sternwald-systems/raw/upload/v1/hugoprd/ARTIKEL_ATTACH/002E9ADD_C9FA4B214D64/d124670c4b1ba66a64ab0bfbd6a44033a79ea62c/PEEK%20and%20Epoxy%20Provide%20Efficient%20Insulation%20for%20High%20Voltage%20E-Motor%20-%20KUint%2002%202022.pdf).

### Inferences
- The planned study can claim novelty in comparing application methods side by side (enamel vs extruded vs tube vs heat-shrink vs tape vs powder vs CVD coating) under one oil protocol on rectangular hairpin conductors. Reporting % retention against an air or inert control, as Doerr & Kujak and Yang did, would make the comparison robust.
- Thermoplastic coatings (PFA here, and probably PEEK) appear to resist ATF better than thermoset PAI. However, the only peer-reviewed evidence is a single vendor-affiliated study, and PEEK's high-temperature dielectric behaviour (above 160 °C) is a counter-risk.

### Gaps
- I found no electrical oil-ageing data for parylene, epoxy powder coating, PEEK heat-shrink or PEEK tube on conductors, or Kapton-taped conductors in ATF or e-fluid, from peer-reviewed or vendor sources.
- SAE 2023-32-0145 may contain a polyimide vs polyamide vs polyester comparison, but its numbers were not accessible.
