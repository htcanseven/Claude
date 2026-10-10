# Powder, Liquid, Electrodeposition, Vapour-Deposition and Inorganic Coatings for Bare Rectangular Copper Hairpin Conductors (EV traction motors, hairpin weld ends, EV busbars)

Research date: 2026-10-10. All URLs below were opened (web page fetched, or PDF downloaded and text-extracted). Document dates are given where the source shows them; older documents are flagged.

## Q1. Epoxy powder coatings (fluidized-bed dip / electrostatic spray): thickness, cure, Tg, thermal class, dielectric strength, edge coverage, flexibility, use on hairpin weld ends, slots and busbars

### Takeaway
Epoxy powder is the established series-production method for insulating hairpin weld ends. The stator is preheated, its weld tips are dipped into a fluidized powder bath, and this is done after trickle impregnation. Epoxy powder is also the dominant coating for EV busbars, where electrostatic spray is the norm. Documented builds are about 100–500 µm, and fluid-bed dipping can reach 200–2000 µm. Dielectric strength is about 30–85 kV/mm (depending on test thickness) with εr ≈ 4. Hairpin and slot grades carry UL 1446 Class F/H. The documented busbar grades show only about 5% elongation and Tg2 of about 100–112 °C. Powder is therefore a post-forming, post-welding process, not a pre-bending insulation.

### Cited Findings
**Industrial process and maturity on hairpin weld ends**
- Hairpin/I-pin stator welded zones "have to be protected" to achieve electrical insulation. The market methods are powder coating, gel coating, potting, and dipping of the welded joints. The welding pins are coated with epoxy powder, and heat can be reused when the coating step is combined with the impregnation system. — [bdtronic – Stator coating](https://bdtronic.com/en-en/impregnation-applications/stator-coating)
- bdtronic's powder coating machine (vendor figures) handles stator diameters of 60–450 mm and stator weights up to 70 kg, with pins on one or both sides. A line combined with trickle impregnation is claimed to save 40% floor space and up to 50% of heating cost and heating time. — [bdtronic – Powder coating machine](https://bdtronic.com/en-en/impregnation-machines/powder-coating-machine)
- Process description (20 Aug 2020): "the part is preheated and moved into a powder bath"; the stator's heat melts the epoxy on the surfaces, forming a protective layer over the welding tips. bdtronic's trickle impregnation machines run at 45 s per motor. No coating thickness was disclosed. — [Magnetics Magazine, 2020](https://magneticsmag.com/bdtronic-adds-powder-coating-process-for-hairpin-stators/)
- Gehring's hairpin line (brochure dated 11/2025) lists "8. Impregnation" followed by "9. Powder coating". Its Imflex P powder coater offers "robust powder bath fluidization for reproducible weld end coating" and optional automated masking/unmasking. Its Imflex TR impregnation uses induction heating. — [Gehring e-mobility brochure](https://gehring-group.com/wp-content/uploads/2025/11/gehring-emobility_WEB-EN.pdf)
- Braun Sondermaschinen says its hairpin pins are "reliably covered" with a "low risk of bridging between the individual pins", and claims >95% line availability. Its QC checks cover coating layer thickness, edge coverage, mechanical impact resistance, and electrical insulation. Because the product is not heated before coating, excess powder can be recycled, which suggests cold/electrostatic deposition followed by heating. — [Braun Sondermaschinen – epoxy coating & hairpin systems](https://www.braun-sondermaschinen.de/en/special-machine-construction-and-epoxy-coating-systems/epoxy-coating-and-hairpin-systems/)

**AkzoNobel Resicoat (EV and EL ranges)**
- Resicoat EVmotor epoxy powders are "specifically designed for the electrical insulation of hairpin stators". They are applied by fluidized bed for "a constant film build", and "special Resicoat EV grades for hairpins are recognized by UL 1446 Class F and Class H", with claimed resistance to heat, chemicals, moisture, and "different fluids hairpins are operating in". The slot-insulation powders list dielectric strength "≥ 30 - 45 kV/mm" and Class F (155 °C) or Class H (180 °C) operating temperature. — [AkzoNobel EV brochure, Issue 3, 04/2025](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf)
- The same brochure covers Resicoat EVbusbar grades for nickel-, silver- and tin-plated or plain copper and aluminium busbars, listed to UL 94 V-0 and UL 746B. Resicoat EVcooling grades are listed to UL 746B with a temperature index of 130 °C (Class B). — [AkzoNobel EV brochure, 04/2025](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf)
- Resicoat EL brochure (Issue 1, 09/2024), process data:
  - Fluidized bed: the object is heated above the powder's melting point and immersed for typically 1–5 s, giving 200–2000 µm, with post-cure sometimes required.
  - Electrostatic fluidized bed: cold, earthed parts pass through a cloud of charged powder and are cured by induction.
  - Thermal class: EL3 and e-lock are Class F (155 °C) and EL4 is Class H (180 °C), listed as UL 1446 system components.
  - Other claims: "high dimensional stability on the edge up to 300°C", adhesion to metal up to 25 MPa, and busbar systems from 25 A to 6300 A.
  — [Resicoat EL brochure](https://powdercoatings.brand.akzonobel.com/m/e90ff93aef69124f/original/FUNC-Resicoat-Electrical-Insulation-Brochure-EN.pdf)
- Resicoat EL HLG09R, an electrostatic-spray epoxy for cores, wire and busbars (TDS dated 16 Aug 2016, older):
  - Cure and build: 10–15 min at 160–180 °C object temperature; recommended film 100–300 µm.
  - Thermal: Tg2 > 100 °C (DSC, 20 K/min).
  - Electrical: dielectric strength > 30 kV/mm (IEC 60243-1); tan δ < 0.01 at 25 °C and at 105 °C; εr 4.0 (100 Hz–1 MHz); CTI 500 M.
  - Claimed "high level of flexibility and consistent edge coverage".
  — [HLG09R TDS](https://powdercoatings.brand.akzonobel.com/m/4cc5273cdc960aa3/original/NAM-TDS-Resicoat-EL-HLG09R_US.pdf)
- Resicoat EL HLF59R, an epoxy busbar powder (French TDS, rev. 17, 9 Sep 2019):
  - Application: preheat 190–235 °C object temperature, then 5–10 min post-cure; film 200–300 µm.
  - Mechanical: impact > 5 J; elongation > 5%.
  - Thermal: Tg1 65 ± 7 °C and Tg2 112 ± 5 °C; temperature index 130 °C (Class B, IEC 60216-1); thermal conductivity 0.4–0.5 W/(m·K).
  - Electrical: dielectric strength 45 kV/mm (IEC 60243-1); εr 4.0; tan δ < 0.01 at 25 °C and at 105 °C; CTI 600.
  - Listings: UL 94 V-0 and UL 746B 130 °C (file E214934).
  — [HLF59R TDS](https://powdercoatings.brand.akzonobel.com/m/41be4e412784d15e/original/TDS-Resicoat-EL-HLF59R-FR.pdf)

**3M Scotchcast**
- Scotchcast 5555 (datasheet © 2002, old) is a one-part epoxy powder for motor stators, armatures and transformers.
  - Application: cold electrostatic fluid bed (induction heat recommended), hot venturi spray, or hot fluid-bed dip. Preheat is 204–260 °C.
  - Cure: grade 10G at 177 °C/6 min, 204 °C/150 s or 232 °C/90 s; grade 22G at 177 °C/8 min, 204 °C/4 min or 232 °C/2 min. Gel time at 392 °F is 9–11 s (10G) and 21–23 s (22G).
  - Properties: dielectric strength 1300 V/mil on a 12–14 mil coating (ASTM D149); impact 100 in-lb; cut-through > 340 °C.
  - Edge coverage: 35–40% (10G) and 30–40% (22G) of a 12–15 mil flat coating.
  - Listing: UL 1446 EIS recognition at class 120(E), 130(B), 155(F) and 180(H) (file E163090).
  - Small articles "lose heat rapidly and may require a higher preheat temperature and/or additional oven-curing".
  — [3M Scotchcast 5555 datasheet](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)
- Scotchcast 265 (datasheet © 2007, old) is a low-melt-viscosity epoxy powder for coil impregnation and bonding.
  - Application: preheat 163–232 °C; cure from 149 °C/60 min to 232 °C/2 min; gel time 60 s at 193 °C.
  - Properties: dielectric strength 1300 V/mil at 12–15 mil; thermal shock 10 cycles 75–155 °C passed; impact 160 in-lb; thermal conductivity 0.18 W/(m·K).
  - Listing: UL 1446 thermal classification 200 °C (helical coil) and 180 °C (twisted pair with MW 35 wire), file E309208.
  - Resistance heating of the coil "allows for selective deposition of the powder on only the windings, as the steel is still relatively cool".
  — [3M Scotchcast 265 datasheet](https://multimedia.3m.com/mws/media/22591O/3m-tm-scotchcast-tm-electrical-resin-265.pdf)

**Axalta**
- Alesta dielectric powders (Axalta battery brochure; the file name says 2014 but the footer is dated 02/2024):
  - Dielectric strength 85 kV/mm at 70 ± 5 µm (IEC 60455-2 / IEC 60243-1); film build 200–300 µm.
  - Cure: 140 °C/10 min for Alesta EFH603P0 Bus Gray / ELH623S8, and 170 °C/10 min for Alesta EE80007368521 / EFH643S8.
  - UL 94 V-0; thermal conductivity 0.35 ± 0.05 W/(m·K); salt spray 1,440 h.
  — [Axalta Battery Solutions brochure](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf)
- Alesta e-PRO Dielectric Gray (article dated 10/08/2025) is an epoxy-based powder for high-voltage insulation in EV battery packs and stationary storage. It "passes 6-kV hipot" and is claimed to offer edge coverage, "high flexibility" and high lap-shear strength. It was tested to UL 94 V0 and IEC 60243-1, and OEMs/Tier 1s are running additional tests. The article gives no thickness and does not mention motors or hairpins. — [Products Finishing](https://www.pfonline.com/products/axalta-introduces-alesta-e-pro-coatings-for-ev-thermal-runaway-mitigation)

**Busbar practice**
- Electronic Design (2 Jun 2026, author from busbar maker CEI): epoxy is the preferred powder for electrical busbars, citing the "highest dielectric strength". Electrostatic spray is the industry standard, at "approximately 95% of modern busbar powder coating". Fluidized bed is "older, less common", can produce very thick layers, gives thickness that is hard to control, and is less suited to intricate geometries. Bolted joints are masked, and parts are checked with hi-pot and wet-sponge pinhole tests. — [Electronic Design](https://www.electronicdesign.com/55381411)
- A Dana TM4 patent (priority 2020-04-09, granted 2024-10-15) coats busbars with epoxy by electrostatic fluidized bed, using AkzoNobel Resicoat EL4 HNE01R ("dimensional stability above 300° C") as the example. It claims a thickness of 0.1–1 mm (example 0.3 mm; the process can reach 0.1–3 mm) and a dielectric-strength threshold of 3000–4000 V/mm. Connection portions are masked. — [US12119141B2 (Google Patents)](https://patents.google.com/patent/US12119141)
- PPG's EV brochure (dated 05/2023) offers ENVIROCRON Extreme Protection Dielectric Powder Coating as a "high-temperature process" for busbars and connectors, with "outstanding dielectric performance (2 coats)". It is used in place of films/tapes to eliminate gaps and bubbles and to enhance edge protection. — [PPG EV battery pack brochure](https://eventguides.informaengage.com/wp-content/uploads/2023/07/PPG-Solutions-for-EV-Battery-Packs.pdf)

### Inferences
- **Dielectric strength in common units.**
  - 1300 V/mil ≈ 51 kV/mm, measured on roughly 0.30–0.38 mm films (12–15 mil). That is consistent with AkzoNobel's 30–45 kV/mm.
  - Axalta's 85 kV/mm was measured on a much thinner 70 µm film, which fits the usual fall in kV/mm as thickness increases.
  - Measured breakdown therefore depends strongly on the tested thickness, and the test plan should fix it.
- **Edge coverage on cut hairpins.** Edge coverage of 30–40% (3M) means a 300 µm flat build leaves only about 90–120 µm on sharp edges. On cut, burred or laser-cut hairpin ends, the corners will be the weakest point. Samples should be deburred/radiused, and two coats or a higher-flow grade considered.
- **Tg versus thermal class.** The documented busbar grades show Tg2 of only ~100–112 °C, even though they carry thermal class ratings. For 180–220 °C hairpin weld ends with ATF exposure, only Class H (180 °C) grades are documented (AkzoNobel hairpin grades, EL4, 3M 5555/265). No opened source documents a 200/220 °C powder system for hairpins, though 3M 265 has a 200 °C helical-coil UL classification.
- **Coating must follow forming.** These are thermosets with roughly 5% elongation (HLF59R) and 200–500 µm builds, so a coated conductor should not be bent afterwards. Powder belongs after forming, welding and impregnation, as in the Gehring/bdtronic sequence.
- **Lab feasibility on short bare conductors: high.**
  - Heat the copper sample (oven, induction, or direct resistive heating as in 3M 265), dip it for 1–5 s in a small fluidized bed, then post-cure. Alternatively, spray electrostatically onto a cold sample and then oven- or induction-cure.
  - Short copper samples lose heat quickly, so use the upper preheat range and an oven post-cure (3M 5555 note).
  - Heating 160–260 °C bare copper in air will oxidize the surface. This may affect adhesion; see the Mitsubishi interface-oxide finding in Q3.
- **Thermal mismatch at the weld tip.** A powder-coated weld end combines enamel, weld bead and bare copper. Thermal cycling against impregnation resin and enamel is a likely failure locus. This is an inference; no opened source gives cycle data.

### Gaps
- No public TDS or grade code was found for AkzoNobel's "Resicoat EV" hairpin grades (Tg, thickness, CTI, PDIV). The brochure states UL 1446 F/H without file numbers.
- No peer-reviewed PDIV, thermal-cycling or ATF-ageing data for powder-coated hairpin weld ends were found.
- **3M "Scotchcast 5133"** could not be found in any search or 3M listing, and its existence or specification is unverified. No hairpin-specific powders from Huntsman, Elantas or Nippon Paint were found.
- Production coating thicknesses on weld tips are not disclosed by bdtronic, Gehring or Braun.
- No opened source documents powder-coated slot insulation in series hairpin stators. AkzoNobel describes slot-insulation powders generically, and slot liners are covered by other researchers.

## Q2. Liquid coatings: epoxy / epoxy-novolac (dip, spray, brush), silicone resin/rubber, UV-curable and dual-cure conformal coatings on hairpin welds

### Takeaway
The industrial liquid routes for weld ends are gel coating (resin trickled over the welds and oven-cured), 2K potting in a stator-specific mold, and dipping cured by heat or UV. The best-documented hairpin-specific liquid is a Hitachi patent: a CaCO3-filled anhydride epoxy dip on rectangular-conductor weld ends, 50–1000 µm thick, with 5–11 kV AC breakdown and ≥155 °C heat resistance. I could not confirm any commercial UV/dual-cure "hairpin weld" product from Elantas, Dymax, Henkel or Axalta in an opened source. Generic data show silicones reach 200–260 °C but have modest dielectric strength (≈16–80 kV/mm). Thick liquid epoxies in the opened sources are rated Class B–F.

### Cited Findings
- Gel coating: liquid resin is trickled over the welded joints soon after trickle impregnation, on the same machine, and cured in the machine's oven. Potting uses a resin that is "typically 2-components" and needs a mold designed for the stator. Dipping immerses the weld joints in liquid resin, cured "by means of temperature or UV light". — [bdtronic – Stator coating](https://bdtronic.com/en-en/impregnation-applications/stator-coating)
- **Hitachi patent US8735724B2** (priority 2010-10-20, lapsed 2018). It covers insulation of the welded ends of rectangular stator-coil conductors.
  - Material: anhydride-type epoxy (SOMAR E-530) filled with calcium carbonate (3–7 µm, 40–55 wt%; examples 45–50 wt%).
  - Application: the welding part is dipped downward for 1–10 min (3 min in Ex. 1) and cured upward, at 160 °C furnace / 150 °C surface temperature for 30 min.
  - Thickness: 50–1000 µm claimed (examples 220–730 µm and 75–550 µm).
  - Edge cover ratio: ≥20% required (examples 21–39%).
  - AC 50 Hz breakdown: 11 kV in Ex. 1 and 3, 5 kV in Ex. 4.
  - Heat resistance ≥155 °C (JIS C 4003). The patent avoids powder resin to reduce dust.
  — [US8735724B2](https://patents.google.com/patent/US8735724)
- **3M Scotchcast 10N** (datasheet Sept 2016): a two-part, room-curing, Class B (130 °C), filled, thixotropic epoxy paste. It is applied by spatula/"buttering", including "insulating by buttering end-turns of motor stator coils".
  - Cure: 24–48 h at 23 °C, 2 h at 60 °C, or 1 h at 95 °C.
  - Electrical: electric strength 350 V/mil (13.8 kV/mm) on a 3.175 mm sample; εr 5.3; tan δ 0.10; volume resistivity 1×10^12 Ω·cm.
  - Elongation 15%. Oil and fuel resistance is claimed.
  — [3M Scotchcast 10N datasheet](https://multimedia.3m.com/mws/media/1289663O)
- Generic conformal-coating comparison in an SCS datasheet (© 2016; values from 2002–2004 handbooks, so older generic data):

  | Coating family | Continuous service | Dielectric strength | εr at 60 Hz |
  |---|---|---|---|
  | Acrylic | 82 °C | 3,500 V/mil | not given (2.7–3.2 at 1 MHz) |
  | Epoxy | 177 °C | 2,200 V/mil | 3.3–4.6 |
  | Urethane | 121 °C | 3,500 V/mil | 4.1 |
  | Silicone | 260 °C | 2,000 V/mil | 3.1–4.2 |

  All four are applied by "spray or brush". — [SCS Parylene LED datasheet (properties table)](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf)
- **DOWSIL 3-1953 silicone conformal coating** (distributor data): one-part, solvent-free, RTV/heat cure (listed 30 min at room temperature or 1.5 min at 60 °C).
  - Service temperature −45 to 200 °C.
  - Dielectric strength 400 V/mil; volume resistivity 1.6×10^15 Ω·cm.
  - UL 94 V-0 and MIL-I-46058C; hardness 16 Shore A.
  — [Ellsworth – DOWSIL 3-1953](https://www.ellsworth.com/products/conformal-coatings/silicone/dow-3-1953-silicone-conformal-coating-18.1-kg-pail/)
- **PPG RAYCRON UV-Cure Dielectric Coating** (brochure 05/2023): a low-temperature process with 1–2 s takt time and "outstanding dielectric performance (2 coats)". It is a 100% solids, solvent-free sprayable liquid, aimed at prismatic cell cans and module separators. — [PPG EV battery pack brochure](https://eventguides.informaengage.com/wp-content/uploads/2023/07/PPG-Solutions-for-EV-Battery-Packs.pdf)
- **Axalta** (Energy Solutions brochure, footer 09/2023): impregnating resins go "up to thermal class 220°C (R)", are epoxy-modified with no anhydrides, and are partly offered with increased thermal conductivity and PD resistance. Its wire enamels claim "excellent resistance against ATF oils". No weld-end coating product is listed. — [Axalta Energy Solutions brochure](https://www.axalta.com/content/dam/general-industrial/segments/energy-solutions/Brochure_Energy_Solutions_2024.pdf)
- **Elantas**:
  - Its insulation is described as "tailored to hairpin and concentrated winding designs", across wire enamels, impregnating resins and casting/potting materials, for 400–1,200 V systems. No named weld-end, UV or dual-cure product appears. — [Elantas e-mobility](https://elantas.com/markets/emobility-solutions-elan-drive.html)
  - Its impregnating materials can be cured air-dry, heat-cure or "UV-assisted", using dip, hot-dip, roll-dip, trickle, spray, vacuum or VPI methods. — [Elantas impregnating materials](https://elantas.com/products/impregnating-materials.html)

### Inferences
- **Lab feasibility.** Liquid dip or brush is the easiest lab method. The Hitachi patent shows that edge coverage is the critical parameter: it needed a highly filled thixotropic resin (27.6 Pa·s at 25 °C), downward dip and upward cure just to reach 21–39% edge cover. Unfilled low-viscosity dips will thin even more at corners.
- **Silicones.** They reach 200 °C (DOWSIL, distributor data) to 260 °C (handbook), but their dielectric strength (2,000 V/mil handbook, 400 V/mil product, ≈16–79 kV/mm) is lower than epoxies'. ATF swelling is unknown.
- **UV-only cure.** On closely packed hairpin weld tips this risks uncured shadow zones. Dual-cure (UV plus heat or moisture) would be needed. This is an inference; no hairpin-specific source was opened.
- **Thermal headroom.** Liquid epoxies in the opened sources reach Class B (3M 10N) or ≥155 °C (Hitachi example). Axalta's 220 °C class refers to impregnating resins, not weld-end coatings.

### Gaps
- No opened source confirms a Dymax, Henkel, Elantas or Axalta UV- or dual-cure coating sold for hairpin welds. DELO's e-motor brochure, reportedly listing "hairpin sealing", returned HTTP 404 and could not be verified.
- No liquid epoxy-novolac dip product for hairpin weld ends was found. Novolak epoxy appears only as an electrodeposition resin option in the Hitachi Astemo patent (Q3).
- No ATF-compatibility or thermal-cycling data were found for silicone, UV or dual-cure coatings on copper weld ends.

## Q3. Electrodeposition: cathodic epoxy/acrylic e-coat (incl. PPG Powercron) and electrodeposited polyimide / polyamide-imide for rectangular wire and weld ends

### Takeaway
Electrodeposition (ED/EPD) gives the best corner coverage of any wet process, because field concentration builds film at edges. Toyochem reports >80% edge coverage on 2.5 mm square copper, and Mitsubishi corners come out thicker than flats unless chamfered. ED is documented in three hairpin-relevant settings:
- **Hairpin weld ends:** a Hitachi Astemo patent coats them by cathodic ED to 5–50 µm, with thickness chosen against PD inception.
- **Continuous flat wire:** Mitsubishi Materials patents describe PAI/PI flat wire at 10–100 µm, with 3.5–6.0 kV breakdown at 40 µm and 9.5 kV at 100 µm.
- **Busbars:** Axalta AquaEC epoxy e-coat (20–45 µm, 70–150 kV/mm) and Japanese polyimide e-coats rated about 200 to over 250 °C.

In the opened PPG material, Powercron is marketed for corrosion protection, not as a busbar dielectric. Maturity is mixed. Epoxy e-coat on battery parts and PI e-coat on busbars are commercial. ED flat magnet wire and ED on weld ends are at patent/pilot level in the sources found.

### Cited Findings
**Electrodeposition on hairpin weld ends**
- **Hitachi Astemo patent US10630129B2** (priority 2013-03-15, granted 2020-04-21).
  - The stripped conductor near the weld is coated "through electrodeposition", with the stator as the negative electrode (cathodic). The bath is at about 28 °C for 1–5 min, then the part is washed and baked.
  - Listed resins: novolak-type epoxy, polyamide-imide, polyimide, acrylic, polybutadiene, alkyd and polyester.
  - Average thickness is 5–50 µm (another passage gives 5–40 µm), "determined in consideration of a partial discharge-starting voltage". The coating also prevents dust in the ATF and improves moisture, insulation and heat resistance.
  - ED is said to give better throwing power and a more uniform film than powder. At higher voltage the film overlaps the enamel. No PDIV values are reported.
  — [US10630129B2](https://patents.google.com/patent/US10630129)

**ED polyamide-imide / polyimide flat (rectangular) wire, Mitsubishi Materials patents**
- **US10706992B2** (priority 2017-08-22).
  - Wire and film: PAI or PI electrodeposited on flat copper wire with aspect ratio ≥12 (12–60 in the embodiment). Film at the long-side centre is 10–100 µm, with centre-to-edge thickness ratio t1/t2 of 0.80–1.35.
  - Process: DC ≥150 V (lower voltage causes foaming at bake) for 5–60 s, followed by a two-step bake (150–220 °C, then ≥30 °C higher).
  - Example 1: 500 V, 30 s, 25 °C, then 210 °C/3 min + 300 °C/3 min.
  - Breakdown: 3.5–6.0 kV at 40 µm and 9.5 kV at 100 µm, versus 1.2 kV for a 10 µm comparative with t1/t2 1.55.
  — [US10706992B2](https://patents.google.com/patent/US10706992)
- **US9947436B2** (priority 2014; hexagonal copper core).
  - Dip/die coating "tends to be thin on the corner part", while electrodeposition makes the corner "a swelled shape".
  - Without a chamfer, flat/corner thickness was 10/18, 40/55 and 100/126 µm, with void ratios of 7–12%.
  - With a corner chamfer of R/L = 1/3–1/20, the difference fell to ≤5 µm and voids to ≤5%.
  - Bake profile: 200–500 °C gradient.
  — [US9947436B2](https://patents.google.com/patent/US9947436)
- **US12278025B2** (priority 2019, granted 2025-04-15).
  - Process: PAI particle ED on a rectangular 1.5 × 6.5 mm copper wire to 40 µm (preferred 10–50 µm). Bake 300 °C/5 min, then controlled-cooling post-heat at ≥180 °C (general range: bake 200–350 °C for 1–10 min).
  - Interface result: adhesion after a 90° edgewise bend around a 6.5 mm bar (3.25 mm radius) was grade A only when the Cu/film interface oxygen layer was 7–10 nm. At 0.5, 35 or 60 nm it was grade C (≥5 µm protrusions).
  — [US12278025B2](https://patents.google.com/patent/US12278025)

**Commercial polyimide e-coats (Japan)**
- **Toyochem (artience)** anionic, waterborne polyimide ED paint.
  - Builds thick film "of 100 μm", with edge coverage above 80% on 2.5 mm square copper.
  - Breakdown stays above 10 kV after 500 h at 220 °C (about 100% retention).
  - Thermal: Tg ≥ 200 °C; Td5 ≥ 400 °C (N2).
  - Thermal shock: 250 cycles from −40 to 180 °C with cross-cut class 0.
  - Cure schedule and εr are not given.
  — [artience / Toyochem polyimide electrodeposition](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html)
- **Honey Kasei** polyimide-based electrodeposition resin, "Supports over 250℃", with surface resistance >1×10^16 Ω. It is aimed at high-voltage EV busbars, on substrates including copper, aluminium, anodized aluminium and stainless steel. — [Honey Kasei (IPROS)](https://pr.mono.ipros.com/en/honny/product/detail/2001642863/)
- **Shimizu** (IPROS listings, auto-translated):
  - "Elecoat PI" cationic polyimide electrodeposition coating.
  - A heat-resistant insulating coating rated about 1000 V on flat surfaces at a 10 µm example.
  - Heat- and acid-resistant grades of 3–40 µm, around 200 °C.
  - E-coat heat-resistant/insulating technology for edgewise coils, busbars and EV motor coils.
  - Elecoat FEW at 5 µm, rated 180 °C for over 3000 h.
  — [IPROS – Electrochemical paint listings](https://mono.ipros.com/en/cg2/Electrochemical%20Paint)

**Research EPD**
- **KTH/Scania** (RSC Advances 2021): electrophoretic deposition of quaternized polyetherimide on copper, followed by drying and thermal re-imidization at 250 °C, giving 2–6 µm films.
  - The 17 h / 44 h durations are internally inconsistent. The body text assigns them to drying in a 60 °C oven, while the Fig. 4 caption assigns them to the 250 °C treatment.
  - Pulsed 20 V was best; constant 20 V caused H2 bubbles and copper etching.
  - A ~5 µm film withstood a 50 V test (~10 kV/mm), with insulation resistance >10^9 Ω.
  - The suspension stays stable for about 48 h. The work used flat coupons, with no hairpins and no PD testing.
  — [Zirignon et al., RSC Adv. 2021 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9042725/)

**Epoxy e-coat for busbars / battery parts**
- **Axalta AquaEC** (brochure footer 02/2024):
  - AquaEC 6100: epoxy, 140 kV/mm at 25 µm, film 20–30 µm, salt spray 504 h.
  - AquaEC 3500EP: epoxy, 70–150 kV/mm, breakdown voltage 2–5 kV, film 20–45 µm, salt spray 1,000 h.
  - Dielectric strength depends "on filmbuild and pretreatment".
  — [Axalta Battery Solutions brochure](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf)
- **PPG** (brochure 05/2023): POWERCRON electrocoats appear under "Corrosion & Impact Protection" ("uniform film build", "highly automated"), not under "Dielectric Isolation". The dielectric products listed for busbars are ENVIROCRON dielectric powder and RAYCRON UV-cure. — [PPG EV battery pack brochure](https://eventguides.informaengage.com/wp-content/uploads/2023/07/PPG-Solutions-for-EV-Battery-Packs.pdf)

### Inferences
- **Breakdown per thickness.** 40 µm ED PAI giving 3.5–6.0 kV equals about 88–150 kV/mm, comparable to Axalta's 140 kV/mm at 25 µm. ED films are electrically strong per µm. Their absolute breakdown and PDIV are limited by thinness (5–100 µm), so ED alone is unlikely to replace a 150–250 µm hairpin insulation for 800 V SiC drives. It is more plausible as a weld-end or corner-repair layer or a base coat. PDIV must be tested (inference).
- **Lab feasibility: medium.**
  - Needs the supplier's bath (Toyochem, Shimizu, Honey Kasei, Axalta or PPG), a DC supply (tens to hundreds of volts; the patents use ≥150–500 V for PAI), a counter-electrode, rinsing, and a bake oven (≈200–300 °C for PI/PAI).
  - Cut faces and corners are coated automatically. Burrs may swell or bubble (US9947436; KTH), so deburr or chamfer the samples.
- **Interface oxide.** The 7–10 nm optimum (US12278025) shows that Cu surface preparation and bake atmosphere are critical to bend adhesion. ED before forming is possible only with a tightly controlled interface, while ED after forming or welding (Hitachi Astemo) avoids bending loads.
- **Epoxy e-coat thermal class.** Standard epoxy e-coat (AquaEC) has no thermal class in the opened material. It should be treated as unproven at 180–220 °C, while the polyimide e-coats show 200–250 °C+ capability.

### Gaps
- No PDIV data were found for electrodeposited coatings on flat wire, busbars or weld ends.
- No full technical data sheet was found for Shimizu "Elecoat PI" (thickness range, breakdown voltage, thermal class), and the IPROS pages are machine-translated.
- No evidence was found that PPG Powercron is qualified or marketed as a busbar dielectric. The premise is unverified.
- The series-production status of Mitsubishi Materials' ED flat magnet wire is unknown, and no press release was found. These sources are patents only.
- No thermal-class or ATF data were found for epoxy or acrylic e-coat.

## Q4. Vapour deposition: Parylene N, C, D, HT/AF-4, F/VT-4 and plasma-polymer coatings

### Takeaway
Parylene gives pinhole-free films of a few hundred ångströms up to about 75 µm. It deposits at room temperature from vapour and is fully conformal, including corners and crevices. Short-time dielectric strength is very high (5,400–7,000 V/mil), εr is low (HT ≈ 2.2), and elongation is high (200–250%). Only Parylene HT/AF-4 (350 °C continuous) and F/VT-4 (200 °C long-term) meet class 180–220 °C needs in air; C (80 °C), N (60 °C) and D (100 °C) do not. Use on hairpins exists only at patent level (Essex: parylene over enamel on preformed hairpins, 1–40 µm). Thin films limit absolute breakdown and PDIV. Plasma-polymer insulation (<2 µm) is at research or early-industrial stage.

### Cited Findings
- **SCS properties table** (© 2016):

  | Property | HT | C | N |
  |---|---|---|---|
  | Dielectric strength (ASTM D149) | 5,400 V/mil | 5,600 V/mil | 7,000 V/mil |
  | εr at 60 Hz / 1 kHz / 1 MHz | 2.21 / 2.20 / 2.17 | 3.15 / 3.10 / 2.95 | 2.65 (all) |
  | Dissipation factor at 60 Hz | <0.0002 | 0.020 | 0.0002 |
  | Continuous / short-term service | 350 / 450 °C | 80 / 100 °C | 60 / 80 °C |
  | Water absorption (24 h) | <0.01% | <0.1% | <0.1% |
  | Tensile strength | 7,500 psi | 10,000 psi | 7,000 psi |
  | Penetration (crevices/tubing) | 50× diameter | 5× diameter | 40× diameter |

  Films range "from several hundred angstroms to 75 microns". The gas "uniformly grows on all surfaces and edges, including inside the smallest crevices". — [SCS Parylene LED datasheet](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf)
- SCS (2 Mar 2022) gives continuous/short-term service temperatures of C 80/100 °C, N 60/80 °C, D 100/120 °C and HT 350/450 °C.
  - C is rated at 80 °C for "100,000 hours (approximately 10 years)" in oxygen-dominated atmospheres. Without oxygen, parylenes work from about −270 °C to 450 °C.
  - Melting points: C 290 °C, N 420 °C, D 380 °C, HT >500 °C.
  - Thermal conductivity: C 0.084 W/(m·K); N 0.126 W/(m·K).
  — [SCS – A guide to Parylene service temperatures](https://scscoatings.com/newsroom/blog/a-guide-to-parylene-service-temperatures/)
- SCS (1 May 2022): Parylene N dielectric strength is 7000 V/mil "at 1 mil", higher than C; N has better crevice penetration than C. — [SCS – Parylene variant comparison](https://scscoatings.com/newsroom/blog/parylene-variant-comparison/)
- **HZO properties table**:
  - Parylene F (VT-4): long-term (~10+ years) 200 °C and short-term (~1 month) 250 °C; tan δ 0.0002 at 60 Hz/1 kHz and 0.0008 at 1 MHz; volume resistivity 1.1×10^17 Ω·cm; CTE 3.6×10^-5 /°C.
  - AF-4: 350 °C long-term and 450 °C short-term.
  - Short-term values for the other types (N 95 °C, C 115 °C, D 135 °C) differ from SCS's 80/100/120 °C, a conflict between sources.
  — [HZO – Parylene properties](https://hzo.com/coatings/parylene-coating/properties)
- **Wikipedia industry table**:
  - Elongation to break: N 250%, C 200%, D 200%, HT/AF-4 200%. Young's modulus: N 350,000 psi, C 400,000 psi, HT 370,000 psi. CTE: N 69 ppm, C 35 ppm, HT 36 ppm.
  - Process (Gorham): dimer pyrolysis at 450–700 °C and 0.01–1.0 Torr. AF-4 dimer cracks at 700–750 °C and deposits at 1–100 mTorr at room temperature. Post-deposition vacuum anneal is 300 °C for AF-4.
  - Trade names: AF-4 is sold as SF (KISCO) and HT (SCS); VT-4 as CF (KISCO).
  - It gives AF-4 dielectric constant as ~2.5, which conflicts with SCS's 2.17–2.21.
  — [Wikipedia – Parylene](https://en.wikipedia.org/wiki/Parylene)
- **Essex patent US10510459B2** (priority 2016-03-31; Essex Group, now Essex Solutions):
  - Process: parylene (N, C, D, HT/AF-4, F and others) is applied as a conformal layer over enameled magnet wire, including batch coating of preformed hairpins before insertion. The wire may be cut and shaped into hairpins before coating.
  - Thickness is preferably 1–40 µm, with a broader range up to about 75 µm. Underlying enamel layers are 0.001–0.010 in each.
  - A-174 silane (CAS 2530-85-0) or other promoters are named for adhesion.
  - Stated targets, not measurements: dielectric strength "in excess of approximately 7,000 volts/mil"; PDIV >1,000–2,500 V; continuous use up to about 200/220/240 °C for 1,000/5,000/20,000 h.
  — [US10510459B2](https://patents.google.com/patent/US10510459)
- **Fraunhofer IFAM plasma polymers.** Coatings are applied inline at atmospheric pressure or in low-pressure plasma, with no solvents and no VOCs, and are PFAS- and halogen-free. Typical thickness is "below 2 micrometers" (<2–5 µm cited for heat dissipation). They are described as "partial-discharge-resistant" (no numbers), for conductor tracks and as a replacement for insulating lacquers on boards and coils. — [Fraunhofer IFAM – electrical insulation coatings](https://www.ifam.fraunhofer.de/en/technologies/electrical-insulation-coatings.html)

### Inferences
- **Field strength.** 5,400–7,000 V/mil ≈ 213–276 kV/mm short-time at about 25 µm. At the maximum practical 50–75 µm, parylene alone would give a few kV of breakdown at room temperature. It is better suited as a conformal sealing layer over enamel, weld zones or cut ends than as standalone 800 V insulation. PDIV must be tested; the low εr (2.2) of HT/VT-4 helps (inference).
- **Grade choice.** For 180–220 °C in air, only HT/AF-4 (350 °C) or VT-4/F (200 °C) are candidates. Parylene C, the cheapest and most common, is limited to 80 °C continuous in air.
- **Before or after forming.** The 200–250% elongation suggests films can survive some forming. The Essex route applies parylene after forming, as a batch on hairpins or even on wound assemblies, which avoids the question.
- **Lab feasibility: high via coating services** (SCS, KISCO, Para Tech, Curtiss-Wright, HZO).
  - Samples are batch-coated at room temperature with A-174 primer. Contact ends need masking.
  - Deposition is slow and thickness scales with chamber time (Essex), so 25–75 µm builds are expensive.
- **Plasma polymers (<2 µm).** Too thin to be a primary 400–800 V insulation. They are plausible as adhesion or barrier interlayers, at research level.

### Gaps
- Parylene HT dielectric strength versus thickness and versus temperature was not obtained (the HAL/Univ. Toulouse paper was bot-blocked).
- No peer-reviewed PDIV or thermal-ageing data were found for parylene on hairpins or rectangular wire. All hairpin evidence is patent claims.
- No ATF-immersion data were found for parylene. The Essex patents only assert oil resistance.
- No dielectric constant, elongation or adhesion data were found for VT-4 on copper after 200 °C ageing.
- No dielectric data were found for plasma polymers on copper windings.

## Q5. Thermoplastic powder and dispersion coatings: PEEK (VICOTE), PPS (Ryton), PFA/FEP/ETFE (Daikin/Chemours), PA11 (Rilsan)

### Takeaway
PA11 (Rilsan) is commercial for EV busbars: up to 500 µm per fluid-bed dip, CTI >600 V, UL 94 V-0, and a pass on the 3.175 mm conical mandrel. It melts at 186 °C, so it is unsuitable for 180–220 °C windings. PEEK (VICOTE) has the thermal headroom: 260 °C continuous use and RTI, Tg 143 °C, builds from under 100 to 500 µm. So do PFA/FEP/ETFE powders (melting points 305/270/220 °C; 100–2,000 µm; elongation 250–400%). Both need very high processing temperatures (PEEK ovens up to 450 °C) and grit-blasted metal, which raises copper oxidation and annealing concerns. PPS powder is rated up to 200 °C. No opened source shows any of these on hairpin conductors, and dielectric data for the coatings are largely missing.

### Cited Findings
- **Victrex VICOTE 700 Series** (datasheet):
  - Application: electrostatic spray; hot flocking for films above 1 mm. Typical thickness is <100–500 µm; average particle size 10–50 µm.
  - Process: ovens to 450 °C; optional anneal at 250 °C for 30–60 min; powder drying at 150 °C/3 h.
  - Thermal: continuous use 260 °C; Tg 143 °C; Tm 343 °C; RTI elec/imp/str 260 °C (UL 746B).
  - Substrate: no primer; degrease and grit-blast. Phosphate-pretreated substrates "may delaminate".
  - No dielectric strength or εr is given. Supply only through Victrex or its preferred coater network.
  — [Victrex VICOTE 700 datasheet](https://www.victrex.com/en/downloads/datasheets/vicote-700-series)
- **Arkema Rilsan PA11 for busbars and battery parts.** Rilsan T Orange 7706 is a primerless fluid-bed grade reaching up to 500 µm in one dip. Rilsan ESY Orange 7705 is a primerless electrostatic grade for thinner insulation.
  - CTI >600 V and UL 94 V-0 for coated busbar; UL Yellow Card granted.
  - Passes ISO 6860 (3.175 mm conical mandrel) at >250 µm.
  - Adhesion to steel, aluminium, copper and nickel; cooling-plate insulation from 100 µm.
  - Resists 50% NaOH and 10% H2SO4.
  — [Arkema – electrical applications & battery components](https://hpp.arkema.com/en/markets-and-applications/powder-metal-coatings/electrical-applications-and-battery-components/)
- Rilsan PA11 T Blue 7444 MAC: fluidized-bed dipping grade with D50 115 µm, melting temperature 186 °C (DSC) and density 1.17 g/cm³. — [Arkema product page](https://hpp.arkema.com/en/products/product/f/spa_hpp_RilsanPowders/p/rilsan-pa11-t-blue-7444-mac/)
- **Daikin NEOFLON coating powders** (TDS dated Mar 2018). All three grades are electrostatic powders intended for chemical-industry linings, and none of the sheets gives electrical data:
  - PFA AC-5539: 100–1,000 µm; average particle size 40 µm; raw-material melting point 305 °C; elongation 250–350%. — [TDS AC-5539](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ac-5539-E_ver01_Mar_2018.pdf)
  - FEP NC-1539N: 100–2,000 µm; melting point 270 °C; elongation 310–360%. — [TDS NC-1539N](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-nc-1539n-E_ver01_Mar_2018.pdf)
  - ETFE EC-6510: 100–1,000 µm; melting point 220 °C; elongation 400%; LOI 50%. — [TDS EC-6510](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ec-6510-E_ver01_Mar_2018.pdf)
- Daikin lists 18 NEOFLON coating powder grades. FEP/PFA have "low melt viscosity", which gives pinhole-free coatings, and ETFE forms "thick" layers. — [Daikin NEOFLON coating powder](https://www.daikinchemicals.com/solutions/products/fluoro-coatings/neoflon-powder.html)
- Syensqo Ryton PPS M2000 FP powder coating (article 2 Apr 2025) is rated "up to 200°C", targets oil and gas, and is said to give "better deposition per pass" with minimal post-cure. No dielectric data. — [Interplas Insights](https://interplasinsights.com/plastics-materials/latest-plastics-materials-news/syensqo-ryton-polyphenylene-sulfide-coating-grade/)
- **Context, likely extruded rather than powder-coated wire** (blog, 6 Feb 2025): Daikin/Additive Drives NEOFLON PFA magnet wire with 50% thinner insulation than PAI enamel. It reportedly showed "superior PDIV" (no values) and >10% higher continuous power, aimed at 800+ V systems. — [Daikin blog](https://www.daikinchem.de/blog/boosting-electric-motor-performance/)

### Inferences
- **PA11.** Its 186 °C melting point rules it out for windings at 180–220 °C. It stays relevant for busbars and lower-temperature parts.
- **PEEK and PFA.** Fusing PEEK (ovens up to 450 °C) or PFA (melting point 305 °C, so fusing above it) on bare copper will grow thick copper oxide and anneal hard copper. Adhesion and mechanical properties after processing must be verified. The VICOTE note that aluminium's properties "are affected at processing temperatures" is analogous (inference).
- **Lab feasibility: medium (PA11) to low (PEEK, PFA/FEP/ETFE).**
  - PA11 fluid-bed dipping needs only preheat and a small fluid bed.
  - PEEK and fluoropolymers need grit blasting, high-temperature ovens and, in practice, approved coaters.
  - Thick builds (100–500 µm or more) on short conductors are feasible. Edge build on rectangular corners is unknown.
- **Forming.** Thermoplastics with 250–400% elongation (fluoropolymers) can in principle tolerate post-coat forming, unlike epoxy powders. Adhesion to copper during bending is unproven (inference).

### Gaps
- No dielectric strength, εr or PDIV data were found for VICOTE, Daikin PFA/FEP/ETFE or Ryton powder coatings.
- Bake schedules for PFA/FEP/ETFE powders are not in the TDS, and the Chemours Teflon PFA coatings page returned 403.
- The Solvay Ryton PPS coatings bulletin returned 403/404, so no primary PPS process data was obtained.
- No source shows thermoplastic powder coatings on hairpin conductors or weld ends.

## Q6. Inorganic coatings: ceramic/sol-gel and organic-inorganic hybrids, plasma/thermal-sprayed alumina, ceramic-insulated wire (Ceramawire), anodizing (aluminium conductors only)

### Takeaway
Inorganic coatings are lab or niche options for traction-motor hairpins.
- **Plasma-sprayed alumina on copper:** about 180–220 µm, with only 10.5–12.9 kV/mm AC breakdown, εr 11–16, 5–6% porosity and vertical microcracks. Copper's CTE is about 3× that of alumina.
- **Sol-gel organic-inorganic hybrids:** above 200 V/µm on fine copper wire, cured at 380–425 °C.
- **Commercial ceramic-insulated wires** (Ceramawire, Fujithermo M): characterized only for 20–400 °C niche use.
- **Anodizing:** applies only to aluminium. Oxide must be kept below about 15 µm (preferably below 10 µm) to survive coil forming, and it is studied mainly for windings above 280 °C.

None is shown to survive hairpin forming at the thicknesses needed for 400–800 V.

### Cited Findings
- **TU Berlin APS alumina on copper** (Coatings 2022, 12, 1847):
  - Substrate: oxygen-free copper, grit-blasted.
  - Thickness: 217 ± 11 µm at 70 mm spray distance down to 183 ± 14 µm at 130 mm; porosity 5.4–6.4%.
  - Breakdown: AC 2.2–2.05 kV, i.e. a mean dielectric strength of 10.5–12.9 kV/mm. The Weibull characteristic strength is 11–14 kV/mm.
  - Dielectric response: εr at 50 Hz is 15.6–10.8; tan δ at 50 Hz is 0.435–0.166; DC resistivity is 6.3×10^8–6.3×10^9 Ω·m.
  - CTE of Cu is 16.7×10^-6 K^-1 versus 5.2×10^-6 K^-1 for Al2O3, about a factor of 3, creating thermal-mismatch stresses. Vertical microcracks lower dielectric strength.
  — [Junge et al., Coatings 2022 (TU Berlin DepositOnce)](https://depositonce.tu-berlin.de/items/73969378-3419-4ab0-8285-59cd6d136bdb)
- **Pfeifer, Brendler, Veith, Kroke** (J. Sol-Gel Sci. Technol. 70, 191–202): sol-gel hybrid precursors from pyromellitic dianhydride and alkoxysilylalkylamines.
  - Applied with an industrial coating device to fine copper wires and cured at 380–425 °C.
  - The best coatings reached breakdown "well above 200 V/µm", were flexible without cracking, and had no pinholes.
  — [Hochschule Schmalkalden repository](https://opus4.kobv.de/opus4-w-hs/frontdoor/index/index/year/2018/docId/2832)
- **Strathclyde (IEEE ICSD 2007)**: dielectric study of the commercial ceramic-insulated wires "Ceramawire" and "Fujithermo M" from 20 to 400 °C, covering I–V and conduction mechanisms, leakage current versus temperature, and DC breakdown of twisted pairs versus temperature. The abstract gives no numeric values. This is older (2007) information. — [Timoshkin et al., Strathprints](https://strathprints.strath.ac.uk/37068/)
- **ABB patent US6261437B1** (priority 1996, expired; older): batch anodizing of Cu, Al or Al-coated Cu winding wire 0.1–6 mm in diameter. Oxide is kept below 15 µm (preferably below 10 µm) so coils can be formed without "cracks or flaking", for high-voltage machine windings. — [US6261437B1](https://patents.google.com/patent/US6261437)
- **Ait-Amar, Saoudi, Vélu** (Energies 15(15) 5362, Jul 2022): thermal ageing of an anodized aluminium strip wire for windings. The motivation is that organic insulation deteriorates where temperatures "exceed 280 °C". The aim is a temperature index and a thermal life model. — [IDEAS/RePEc abstract](https://ideas.repec.org/a/gam/jeners/v15y2022i15p5362-d870474.html)

### Inferences
- **Not a primary hairpin insulation.** APS alumina's 10–13 kV/mm on about 200 µm gives only about 2 kV breakdown, with high εr (unfavourable for PDIV) and porosity that needs sealing. Combined with brittleness and Cu/Al2O3 CTE mismatch, it is unsuitable as primary hairpin insulation. It could serve as a high-temperature barrier on non-flexed parts (inference).
- **Sol-gel hybrids.** These look promising per µm (above 200 V/µm). Curing at 380–425 °C on copper and the research-only maturity make them a lab curiosity for hairpins.
- **Anodizing.** It is irrelevant to copper hairpins. For aluminium hairpins, the <15 µm limit for formability leaves very little insulation thickness, so anodized aluminium would need an organic overcoat for 400–800 V (inference).
- **Lab feasibility on cut copper samples.** APS spraying can be outsourced to a thermal-spray shop (grit blast, then coat). Sol-gel needs in-house synthesis and a 380–425 °C cure. Anodizing does not apply to copper.

### Gaps
- No manufacturer datasheet was found for Ceramawire (temperature rating, thickness, breakdown), and the Strathclyde paper's numbers are not in the abstract.
- No research was found on anodized aluminium hairpins specifically. Aluminium hairpin forming studies (Windsor thesis, Unimore paper) were not opened.
- No PDIV data were found for any inorganic coating on rectangular conductors.
- No data were found on sealing APS alumina coatings on copper for automotive humidity or ATF exposure.

## Q7. Cross-cutting: lab feasibility on cut bare conductors, corner/edge vs flat coverage, flexibility (before vs after hairpin forming), and maturity for hairpins

### Takeaway
For a bare-conductor test plan, the realistic and industrially relevant candidates are:
1. Epoxy powder, by fluid-bed dip or electrostatic spray: in series production on weld ends and busbars, easy in the lab, thick, but thin at corners.
2. Filled liquid epoxy dip, plus silicone or UV/dual-cure coatings: easy, but the poorest edge coverage.
3. Electrodeposition (epoxy e-coat, or PI/PAI e-coat): the best corner coverage, but needs a supplier bath and gives thin films.
4. Parylene HT or VT-4 through a coating service: perfect conformality and low εr, but thin and costly.
5. Thermoplastic powders: PA11 (low temperature) or PEEK/fluoropolymers (very high process temperatures).

Inorganic coatings are research-only. Every thermoset method in the sources is applied after forming and welding. Only the thermoplastics, parylene and thin ED PAI with controlled interface oxide show elongation or bend data compatible with forming after coating.

### Cited Findings
- Industrial weld-end sequence: impregnation, then powder coating (Gehring). Powder coating is combined with trickle impregnation (bdtronic). — [Gehring brochure 11/2025](https://gehring-group.com/wp-content/uploads/2025/11/gehring-emobility_WEB-EN.pdf); [bdtronic](https://bdtronic.com/en-en/impregnation-applications/stator-coating)
- Edge coverage on record:
  - Epoxy powder 30–40% of flat thickness. — [3M 5555](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)
  - Filled liquid epoxy dip 21–39% edge cover ratio. — [US8735724B2](https://patents.google.com/patent/US8735724)
  - Electrodeposited polyimide above 80% on 2.5 mm square copper. — [artience/Toyochem](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html)
  - ED corners thicker than flats (40 µm flat / 55 µm corner) unless chamfered. — [US9947436B2](https://patents.google.com/patent/US9947436)
  - Parylene "uniformly grows on all surfaces and edges". — [SCS datasheet](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf)
- Flexibility on record:
  - Epoxy busbar powder elongation >5%. — [HLF59R TDS](https://powdercoatings.brand.akzonobel.com/m/41be4e412784d15e/original/TDS-Resicoat-EL-HLF59R-FR.pdf)
  - PA11 passes the 3.175 mm conical mandrel at >250 µm. — [Arkema](https://hpp.arkema.com/en/markets-and-applications/powder-metal-coatings/electrical-applications-and-battery-components/)
  - PFA 250–350%, FEP 310–360% and ETFE 400% elongation. — [Daikin TDS AC-5539](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ac-5539-E_ver01_Mar_2018.pdf), [NC-1539N](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-nc-1539n-E_ver01_Mar_2018.pdf), [EC-6510](https://www.daikinchemicals.com/library/pb_common/pdf/tds/Fluoropolymer_Coatings/NEOFLON_Coating_Powder/tds-ec-6510-E_ver01_Mar_2018.pdf)
  - Parylene 200–250% elongation. — [Wikipedia](https://en.wikipedia.org/wiki/Parylene)
  - ED PAI survives a 90° edgewise bend (r = 3.25 mm) only with a 7–10 nm interface oxide. — [US12278025B2](https://patents.google.com/patent/US12278025)
  - Anodic oxide <15 µm to avoid cracking in coil forming. — [US6261437B1](https://patents.google.com/patent/US6261437)

### Inferences
Comparison matrix, synthesized from the Cited Findings in Q1–Q6. Numbers are from the linked sources; the "lab feasibility" and "risk" columns are my inferences.

| Material / method | Typical thickness | Temperature capability | Dielectric data | Edge vs flat | Bend after coating? | Maturity for hairpins/busbars | Lab feasibility on cut bare Cu | Main risks for hairpin |
|---|---|---|---|---|---|---|---|---|
| Epoxy powder, fluid-bed dip (hot part) | 200–2000 µm per 1–5 s dip ([Resicoat EL](https://powdercoatings.brand.akzonobel.com/m/e90ff93aef69124f/original/FUNC-Resicoat-Electrical-Insulation-Brochure-EN.pdf)); 12–15 mil tests ([3M 5555](https://multimedia.3m.com/mws/media/22602O/3mtm-scotchcasttm-electrical-resin-5555.pdf)) | UL 1446 F/H hairpin grades ([AkzoNobel EV](https://powdercoatings.brand.akzonobel.com/m/28e49a6fd077c2f1/original/NAM-Electric-Vehicle-Brochure.pdf)); 200 °C helical coil ([3M 265](https://multimedia.3m.com/mws/media/22591O/3m-tm-scotchcast-tm-electrical-resin-265.pdf)) | 1300 V/mil ≈ 51 kV/mm; 30–45 kV/mm; εr ≈ 4 | Edge 30–40% of flat | No (thermoset, ~5% elongation) | Series on hairpin weld ends (bdtronic, Gehring, Braun) and busbars | High (preheat + small fluid bed + oven) | Thin corners on cut ends; Tg ~100–112 °C on documented busbar grades; bridging between pins; copper oxidation at preheat |
| Epoxy powder, electrostatic spray (cold part + cure) | 100–300 µm ([HLG09R](https://powdercoatings.brand.akzonobel.com/m/4cc5273cdc960aa3/original/NAM-TDS-Resicoat-EL-HLG09R_US.pdf)); 200–300 µm ([Axalta](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf)); 0.1–1 mm busbars ([Dana TM4](https://patents.google.com/patent/US12119141)) | Class B–H depending on grade | >30–85 kV/mm | "Consistent edge coverage" claimed (no %) | No | ~95% of busbar powder coating ([Electronic Design](https://www.electronicdesign.com/55381411)) | High (gun + oven) | Faraday-cage effects between pins (inference); multiple coats needed |
| Filled liquid epoxy dip on welds | 50–1000 µm ([US8735724](https://patents.google.com/patent/US8735724)) | ≥155 °C (patent example) | 5–11 kV AC breakdown | Edge cover 21–39% | No | Patent (Hitachi, 2010 priority) | Very high | Sagging, voids, poor edges |
| Brush/butter epoxy paste | thick, mm range | Class B 130 °C ([3M 10N](https://multimedia.3m.com/mws/media/1289663O)) | 13.8 kV/mm, εr 5.3 | Manual | No (15% elongation) | Repair/legacy | Very high | Too low thermal class |
| Silicone conformal coating | not stated | −45 to 200 °C ([DOWSIL 3-1953](https://www.ellsworth.com/products/conformal-coatings/silicone/dow-3-1953-silicone-conformal-coating-18.1-kg-pail/)); 260 °C generic ([SCS](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf)) | 400 V/mil ≈ 16 kV/mm | Poor (liquid) | Yes (elastomeric; inference) | No hairpin evidence found | Very high | Low strength; ATF swelling unknown |
| UV/dual-cure liquid | not stated | not stated | "2 coats" ([PPG RAYCRON](https://eventguides.informaengage.com/wp-content/uploads/2023/07/PPG-Solutions-for-EV-Battery-Packs.pdf)) | Poor | Unknown | Dipping with UV cure listed ([bdtronic](https://bdtronic.com/en-en/impregnation-applications/stator-coating)); no product confirmed | High (needs UV lamp) | Shadow zones; temperature class unproven |
| Cathodic ED on weld ends | 5–50 µm ([US10630129](https://patents.google.com/patent/US10630129)) | resin-dependent | PD-driven thickness | Good throwing power | n/a (post-forming) | Patent (Hitachi Astemo, 2013 priority) | Medium (bath + DC) | Thin; boundary with enamel |
| ED PAI/PI flat wire | 10–100 µm ([US10706992](https://patents.google.com/patent/US10706992)) | PI e-coat >10 kV after 500 h at 220 °C ([Toyochem](https://www.artiencegroup.com/en/products/metal-coatings/electrocoating/polyimide.html)); >250 °C ([Honey Kasei](https://pr.mono.ipros.com/en/honny/product/detail/2001642863/)) | 3.5–6.0 kV at 40 µm; 9.5 kV at 100 µm | Corners ≥ flats (swelling; chamfer) | Possible with controlled interface ([US12278025](https://patents.google.com/patent/US12278025)) | Patents; PI e-coat commercial for busbars in Japan | Medium (supplier bath, 200–300 °C bake) | Bubbling/foaming; interface oxide; thin |
| Epoxy e-coat (busbars) | 20–45 µm ([Axalta AquaEC](https://secure.axalta.com/content/dam/general-industrial/segments/battery-solutions/Axalta_Battery_Solutions_2014.pdf)) | not stated | 70–150 kV/mm; 2–5 kV breakdown | Good (inference) | Unknown | Commercial for battery parts | Medium | No thermal class; thin |
| Parylene HT (AF-4) / VT-4 (F) | ~0.1–75 µm (pref. 1–40 µm) ([SCS](https://nrf.aux.eng.ufl.edu/_files/documents/14389.pdf), [Essex](https://patents.google.com/patent/US10510459)) | HT 350 °C; VT-4 200 °C; C only 80 °C ([HZO](https://hzo.com/coatings/parylene-coating/properties)) | 5,400–7,000 V/mil; εr 2.2 (HT) | Uniform incl. edges and crevices | Yes (200–250% elongation) | Patent-level for hairpins | High via service (masking, A-174) | Thin, so limited breakdown/PDIV; cost; slow deposition |
| Plasma polymer | <2 µm ([IFAM](https://www.ifam.fraunhofer.de/en/technologies/electrical-insulation-coatings.html)) | not stated | not stated | Conformal (low-pressure process) | not stated | Research | Low | Far too thin as primary insulation |
| PA11 powder | up to 500 µm per dip ([Arkema](https://hpp.arkema.com/en/markets-and-applications/powder-metal-coatings/electrical-applications-and-battery-components/)) | Tm 186 °C | CTI >600 V | not stated | Mandrel pass | Commercial for busbars | High | Melts below class-H targets |
| PEEK powder (VICOTE) | <100–500 µm ([Victrex](https://www.victrex.com/en/downloads/datasheets/vicote-700-series)) | 260 °C; Tg 143 °C | not stated | not stated | Unknown | Industrial coatings, none on hairpins | Low–medium (ovens to 450 °C, grit blast) | Copper oxidation/annealing; adhesion |
| PFA/FEP/ETFE powder | 100–2,000 µm ([Daikin](https://www.daikinchemicals.com/solutions/products/fluoro-coatings/neoflon-powder.html)) | Tm 305/270/220 °C | not stated | not stated | Likely (250–400% elongation) | Chemical linings, none on hairpins | Low–medium | Primer/adhesion; bake temperature on copper |
| APS alumina | ~180–220 µm ([TU Berlin](https://depositonce.tu-berlin.de/items/73969378-3419-4ab0-8285-59cd6d136bdb)) | inorganic | 10.5–12.9 kV/mm AC; εr 11–16 | Line-of-sight spray (inference) | No (brittle; CTE mismatch) | Research | Medium (outsource) | Porosity, cracks, high εr |
| Sol-gel hybrid | not stated | cure 380–425 °C ([Pfeifer](https://opus4.kobv.de/opus4-w-hs/frontdoor/index/index/year/2018/docId/2832)) | >200 V/µm | not stated | Flexible on fine wire | Research | Low | Process temperature; no rectangular-wire data |
| Anodizing (Al only) | <15 µm ([ABB](https://patents.google.com/patent/US6261437)) | >280 °C context ([Energies](https://ideas.repec.org/a/gam/jeners/v15y2022i15p5362-d870474.html)) | not obtained | not stated | Only if <10–15 µm | Research (not for Cu) | n/a for Cu | Too thin for 400–800 V without overcoat |

- **Before vs after forming.** All thermoset powder, liquid and e-coat routes for hairpins in the sources are post-forming or post-welding steps. Parylene, ED PAI and the thermoplastics are the only families with elongation or bend evidence compatible with coat-then-form, and this is unproven at hairpin bend radii.
- **Test-plan implication.** On cut samples, the cut faces, corners and burrs dominate failure for liquid and powder methods. Specimen preparation (deburring, edge radius, masking for electrical contact) must be standardized across all coating methods so they can be compared.

### Gaps
- No single source compares these methods head-to-head on rectangular copper hairpin conductors for PDIV, breakdown, thermal ageing and ATF compatibility. A cross-method comparison will need the team's own testing.
- PDIV values are essentially absent for every method in my slice. Only patent targets (Essex: >1,000–2,500 V) and design statements (Hitachi Astemo: thickness chosen for PD inception) were found.
- Long-term ATF compatibility is not quantified for any coating here. There are only qualitative claims: AkzoNobel "fluids hairpins are operating in", the Essex oil-resistance claim, and the Hitachi Astemo ATF-dust remark.
