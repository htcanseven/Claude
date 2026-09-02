# 1 Introduction

## 1.1 The High-Speed Landscape

High-speed electrical machine design is the balancing of four demands that pull against one another: mechanical integrity, electromagnetic performance, thermal management and power-electronic feasibility. A standard 50 or 60 Hz machine can be designed from established rules of thumb, with comfortable margins in every domain. A high-speed machine sits at the edge of several material and switching limits at once, and the margins are gone. A one per cent change in rotor diameter can move a design from safe to failed; a small increase in pole count to save stator mass can push the converter past its stable switching limit.

The design sequence itself changes as a result. Conventional practice proceeds outward from an electromagnetic specification: choose the loadings, size the bore, then verify mechanically and thermally. High-speed design runs the other way. The mechanical and rotordynamic limits fix the rotor geometry first, the converter fixes the admissible pole number, and the electromagnetic design is fitted into the space that remains.

Speed in this context is an electrical problem as much as a mechanical one. The fundamental frequency follows from the mechanical speed n in r/min and the pole-pair number p as

    f₁ = p · n / 60                                                      (1.1)

Traditional industrial high-speed machines favour a low pole count, which keeps f₁ below roughly 600 Hz and within reach of silicon IGBT converters. Machines designed for specific power invert this choice, and in doing so encounter a chain of conflicts: reducing mass requires thinning the stator yoke, which requires raising the pole count, which raises f₁ into the kilohertz range, which raises the switching frequency needed for acceptable current quality, which silicon devices cannot deliver without severe thermal derating.

### 1.1.1 Defining "High Speed"

There is no universally accepted definition of what "high speed" means for an electrical machine. Certain physical limits nevertheless mark the boundary, and when a design approaches them it can reasonably be called high speed. Mechanical, thermal and power-electronic constraints all enter.

#### The r/min fallacy

Revolutions per minute is a deceptive metric, because it conceals the physical intensity of the machine. Fifty thousand r/min sounds impressive, but its engineering significance depends entirely on the physical scale of the rotor. A dental drill spinning at 400 000 r/min is a trivial mechanical task compared with a multi-megawatt industrial compressor at 15 000 r/min.

The reason is that no significant physical mechanism depends on angular velocity alone. Centrifugal stress depends on peripheral speed, v_tip = Ω·r_r. Rotor losses and converter burden depend on electrical frequency, which is angular velocity multiplied by pole-pair number. Windage depends on surface velocity and rotor area. In every case the geometry enters, and r/min discards it. A larger rotor at lower r/min may face far more severe structural loading — bursting of laminations, or loss of magnet retention — than a small rotor turning much faster.

Speed is also relative to electromagnetic frequency. A two-pole machine at 30 000 r/min produces a 500 Hz fundamental; an eight-pole traction machine at the same speed demands 2 kHz. "High speed" is therefore not a single number but a combination of mechanical limit, thermal dissipation and frequency-dependent loss.

#### The established criteria

Two definitions dominate the literature. The first is based on peripheral speed, with v_tip exceeding 150 m/s, and reflects mechanical strength. The second uses the product of rated speed and the square root of rated power, n√P > 100 000 with n in r/min and P in kW (El Hajji et al., 2024). Neither is universally adopted, which is a substantial part of the confusion in the field.

Peripheral speed is the natural mechanical measure because centrifugal stress is a function of tip speed alone. For a rotating solid disc of density ρ and Poisson ratio ν the maximum tangential stress is

    σ_max = [(3 + ν)/8] · ρ · v_tip²                                     (1.2)

and for the same disc with a small central bore — the geometry of any lamination stack mounted on a shaft — the maximum stress moves to the bore and doubles:

    σ_max = [(3 + ν)/4] · ρ · v_tip²                                     (1.3)

Taking ρ = 7650 kg/m³ and ν = 0.3, a bored lamination at 200 m/s carries about 252 MPa and at 250 m/s about 395 MPa. Against a high-strength electrical steel with a proof stress near 450 MPa and a safety factor of 1.5, the 250 m/s design is already outside the allowable envelope. The factor of two between equations (1.2) and (1.3) is the quantitative reason why solid rotors reach higher peripheral speeds than laminated ones.

**[Figure 1.1 near here]**
*Figure 1.1 Maximum tangential stress against peripheral speed for a solid disc, a disc with a central bore and a thin ring, for electrical steel. The central bore doubles the stress.*

#### A third, drive-system criterion

Neither established criterion contains the pole number, and therefore neither contains the electrical frequency. This is a real omission. Two machines of identical rating, size and tip speed but different pole count present very different problems to the converter that must supply them: a two-pole 120 kW machine at 30 000 r/min has a 500 Hz fundamental, while a six-pole machine of the same rotor diameter has 1500 Hz. Their tip speeds and n√P values are identical.

We therefore propose a third measure, the product of fundamental frequency and rated power, f₁P. Rated power sets the current and voltage the converter must handle; fundamental frequency sets the rate at which it must handle them. Their product is a measure of converter burden, and it rises both when a machine is made faster and when it is made lighter by increasing pole count. It is a *drive-system* criterion rather than a machine criterion: it describes the difficulty of supplying the machine rather than of building it.

The fP product is introduced here as a descriptive figure of merit, not as a validated threshold. Assigning a numerical boundary requires a population of machines rather than a single design point, and that calibration is carried out in Chapter 2, where a survey of published high-speed machines is mapped onto all three criteria.

**[Figure 1.2 near here]**
*Figure 1.2 The n√P and fP criteria in the power–speed plane. The fP contour is drawn for p = 3; changing the pole-pair number translates it vertically, which is the dependence n√P cannot express.*

#### Worked example

The high-speed traction machine designed in the EU Voltcar project is characterised in Table 1.1 and is used as a running example through this chapter.

**Table 1.1** Voltcar six-pole radial-flux traction machine, inner rotor

| Quantity | Symbol | Value |
|---|---|---|
| Rated power | P | 120 kW |
| Maximum speed | n | 30 000 r/min |
| Rotor diameter | D_r | 96 mm |
| Pole pairs | p | 3 |

Applying the three criteria:

    v_tip = π × 0.096 × 30 000 / 60 = 150.8 m/s
    n√P   = 30 000 × √120 = 3.29 × 10⁵
    f₁    = 3 × 30 000 / 60 = 1500 Hz,   f₁P = 1.8 × 10⁵ kW/s

The machine only just exceeds the 150 m/s mechanical threshold while clearing the n√P threshold by a factor of 3.3. The disagreement is instructive, and its source is the pole count: wound as a two-pole machine, the same rotor would have identical tip speed and n√P while its fundamental frequency, and with it the fP product, would fall by a factor of three. The consequences of that choice are pursued in Section 1.4.

### 1.1.2 Historical Context and the Direct-Drive Transition

For decades the industrial route to high-speed rotation for compressors, pumps and fans was the geared solution: a four-pole mains-connected induction motor at 1500 or 1800 r/min driving a mechanical speed increaser. The arrangement is mature but is increasingly a bottleneck for both efficiency and power density, and it is being displaced by integrated direct drive, in which the machine is designed to match the load speed natively.

The driver is the drivetrain rather than the motor. Gearboxes are maintenance-intensive, requiring dedicated lubrication systems, oil cooling and periodic seal replacement, and they dissipate typically 2 to 5 per cent of throughput. The physical footprint of a motor–gearbox–load assembly is substantial: in the worst case a geared high-speed unit occupies two storeys, because the lubrication-oil tank must sit below the drive.

Eliminating the gearbox yields several transformative benefits. Removing the gear stages and high-speed couplings raises wire-to-shaft efficiency directly, and over a twenty-year life the energy saving is large. Integrated units frequently use active magnetic or foil bearings, removing oil lubrication entirely — critical in food, pharmaceutical and semiconductor processes, and in subsea installations where an oil leak is an environmental incident. With fewer moving parts, mean time between failures rises, and the machine can be built as a hermetically sealed unit.

The transition is not free. Moving from 1800 to 60 000 r/min shifts the burden from mechanical engineering to multidisciplinary physics: the rotor must survive extreme centrifugal stress, the stator must tolerate high-frequency core loss, and the full thermal load must be removed from a much smaller volume.

**[Figure 1.3 near here]**
*Figure 1.3 Geared and direct-drive architectures compared. Above: a mains-connected motor drives the load through a step-up gearbox, with the lubrication plant below floor level. Below: the impeller is mounted directly on the high-speed motor shaft and carried on active magnetic bearings, giving a single sealed unit with no oil system and no second storey.*

## 1.2 Two Design Paradigms

The constraints described in this chapter apply to every high-speed machine, but they do not produce a single kind of machine, because different applications weight them differently. Two families result, and their design conventions are close to opposite. This division organises the whole book.

### 1.2.1 The gearless industrial machine

Centrifugal compressors, aeration blowers, turbo-expanders and organic Rankine cycle generators share an economic structure: continuous operation for years, judgement on total cost of ownership, and near-irrelevance of mass because the machine is bolted to a foundation. Such a machine is often expected to run for 100 000 hours with minimal intervention.

The design conventions follow. Pole counts are low — two-pole induction machines, or two- and four-pole rotor-surface-magnet synchronous machines — which keeps the fundamental below about 1 kHz and within reach of standard IGBT converters. The two-pole configuration gives the lowest fundamental frequency for a given speed and the highest power factor, and it permits relatively thick laminations of 0.2 to 0.35 mm, keeping manufacturing cost under control.

The high-speed induction machine remains a workhorse because of its ruggedness. Its rotor may be a solid steel body or a high-strength lamination stack, and the absence of magnets simplifies retention entirely. Where efficiency governs, the surface-magnet synchronous machine is preferred; rotor copper loss disappears, but the magnets cannot withstand centrifugal tension unaided and require thick carbon-fibre or Inconel sleeves applied with sufficient pre-stress to keep them in compression at maximum overspeed.

Because mass is not constrained, the industrial strategy is generous everywhere. Rotor diameters are large, pushing peripheral speeds to 200 to 250 m/s, and sleeves are wound with high tension to match. Air gaps of several millimetres reduce windage and accommodate thermal growth, at the cost of magnetising current — unlike traction machines, which use small gaps to maximise torque density. Rotor thermal management often uses a conductive shield, or the sleeve itself as a barrier, paired with forced-air or liquid jacket cooling.

The principal advantage of the low pole count is converter compatibility. With the fundamental below 1 kHz, a switching frequency of 8 to 16 kHz gives a modulation ratio comfortably above 10 without specialised hardware, and standard sine-wave or LC filters can be used to protect insulation from du/dt stress and to suppress bearing currents.

### 1.2.2 The mass-limited mobile machine

Traction, aerospace propulsion and turbomachinery for internal combustion engines invert the priorities. Mass is the objective, because the machine is carried and every kilogram costs range, payload or fuel. Automotive motor speeds have climbed from 10 000 to beyond 20 000 r/min; hybrid-electric aircraft demand power densities above 10 to 15 kW/kg; e-turbochargers and turbo-compounding units operate beyond 100 000 r/min.

The dominant relation is that stator yoke thickness varies inversely with pole number, because flux per pole falls as poles are added. Going from two poles to eight quarters the flux per pole and permits a corresponding reduction in yoke thickness — a large saving in the heaviest single component of the machine. This is why mobile machines use six, eight or twelve poles where industrial machines use two.

The cost is frequency. An eight-pole machine at 15 000 r/min has a 1000 Hz fundamental; at 30 000 r/min it has 2000 Hz. Core loss must then be controlled with thin, high-grade laminations of 0.1 to 0.2 mm, and the resulting loss density demands direct liquid cooling, frequently using the transmission oil to cool the windings and rotor.

Interior-magnet rotors dominate this family. The lamination bridges provide retention without a sleeve, keeping the effective air gap small; the resulting saliency contributes reluctance torque, supporting the wide constant-power speed range that traction requires; and field weakening is effective, which matters when the DC-link voltage is fixed by a battery.

The bearing choice also inverts. Where the industrial machine adopts magnetic or foil bearings to eliminate maintenance, the mobile machine uses oil-lubricated hybrid ceramic rolling-element bearings, which are cheaper, more compact and tolerant of road and airframe shock loading. The gearbox is likewise retained rather than eliminated: since P = T·Ω, generating a given power at high speed and low torque produces a far smaller and cheaper machine, and a fixed-ratio reduction gear is a cheaper route to wheel torque than a larger machine would be.

The mobile approach is not possible without wide-bandgap semiconductors, for reasons developed in Section 1.4.

### 1.2.3 The same physics, opposite conclusions

Table 1.2 summarises the two families. The point of the comparison is not that one is superior but that both are correct. An industrial designer who adopted eight poles and a SiC converter would have raised cost and reduced reliability for a mass saving of no value; a traction designer who adopted a two-pole rotor with a thick sleeve would have produced a machine too heavy to use.

**Table 1.2** Design conventions of the two paradigms

| Feature | Gearless industrial | Mass-limited mobile |
|---|---|---|
| Governing objective | total cost of ownership, availability | specific power |
| Typical pole count | 2 (IM), 2 or 4 (SPM) | 6, 8 or 12 (IPM) |
| Fundamental frequency | below ~1 kHz | 1 to 3 kHz |
| Rotor retention | thick carbon-fibre or Inconel sleeve | lamination bridges, thin sleeve |
| Stator yoke | generous, for flux and stiffness | minimised |
| Lamination thickness | 0.20 to 0.35 mm | 0.10 to 0.20 mm |
| Air gap | large, several mm | small |
| Bearings | active magnetic or air foil | hybrid ceramic rolling element |
| Converter | silicon IGBT | SiC or GaN |
| Transmission | none, direct drive | fixed-ratio reduction gear |

## 1.3 Fundamental Physical Constraints

### 1.3.1 Mechanical limits

Equations (1.2) and (1.3) fix a maximum tip speed for any rotor material, and that limit is hard in a way that thermal and electromagnetic limits are not. A machine running slightly too hot loses insulation life; a rotor turning too fast fails, and the failure is not graceful.

Stress distribution depends strongly on construction. In laminated rotors, common in induction and interior-magnet machines, stress concentrates around the shaft bore and in the bridges that retain magnets or cage bars. Laminations have negligible axial strength, so radial load must be carried entirely by the planar geometry of the steel, and the central bore required for shaft mounting doubles the peak stress relative to a solid disc. Solid rotors behave as a monolithic cylinder with a more uniform distribution and can reach 250 to 300 m/s, but they introduce large eddy-current losses and typically require a large air gap, a low-harmonic winding and an LC filter in the supply.

Surviving a single run is not sufficient. Industrial and traction rotors accumulate very large numbers of load cycles, and repeated expansion and contraction under centrifugal loading drives crack propagation at stress concentrations — particularly the corners of magnet pockets. Fatigue must be assessed separately from static strength.

Two retention strategies are used. In surface-magnet machines the magnets are held in compression by a high-strength sleeve of carbon fibre, where specific strength governs, or Inconel, where temperature and corrosion govern. The sleeve is applied by shrink fit or filament winding with controlled pre-stress so that the magnets remain in compression at maximum overspeed and maximum temperature, the two conditions being additive because the thermal expansion of sleeve and magnet differ. The design penalty is magnetic: a 3 mm sleeve added to a 1 mm mechanical clearance quadruples the effective air gap and forces a corresponding increase in magnet volume.

In interior-magnet machines the lamination itself provides retention, eliminating the sleeve and keeping the effective gap small, but placing the load on thin steel bridges that are simultaneously a magnetic short circuit. The bridge must be thin enough to limit leakage and thick enough to survive; the optimum is narrow and moves with speed, temperature and duty.

### 1.3.2 Rotordynamics and critical speeds

The tip-speed limit caps rotor diameter, and since torque scales with the square of diameter and with active length, a capped diameter must be compensated by length. High-speed rotors are therefore slender, and slenderness is the enemy of rotordynamic stability. The first bending critical speed of a rotor behaving as a uniform beam scales as

    n_cr ∝ r_r / l²                                                      (1.4)

so lengthening the rotor reduces the critical speed quadratically while the diameter reduction that forced the lengthening reduces it further. Section 1.5 quantifies how severely the two compound.

The practical consequence is that many high-speed machines cannot operate below their first critical speed and must run supercritically, passing through one or more resonances on every run-up and coast-down. The electromagnetic design, which wants a large diameter, is thus continually pushed back by the rotordynamic analysis, which demands a short stiff rotor.

**[Figure 1.4 near here]**
*Figure 1.4 First and second bending modes of a slender high-speed rotor, shown as deflected shapes against the undeflected axis. The rotor is supported at the two bearings; the second mode has an interior node. The first bending critical speed scales as r_r/l², so lengthening a rotor to recover the torque lost to a reduced diameter reduces it quadratically.*

The bearing is therefore a first-order design decision rather than a component selection. Hybrid ceramic rolling-element bearings, with silicon nitride balls and oil-mist or jet lubrication, are compact and inexpensive and dominate traction and smaller industrial units, but they impose a finite Dn limit and remain a wearing part; combined with squeeze-film damping they are rugged and economical at lower powers. Fluid-film and air-foil bearings support the rotor on a gas or oil film, are oil-free and self-acting, and are increasingly used in micro-turbines and blowers, but have limited load capacity and can suffer sub-synchronous whirl. Active magnetic bearings levitate the rotor entirely, eliminating contact and wear; uniquely, their stiffness and damping can be varied during operation, so a rotor can be actively steered through a resonance that would destroy a passively supported machine, and they provide continuous position and vibration diagnostics. Their cost, sensor count and control complexity make them difficult to justify at low power.

### 1.3.3 Aerodynamic and windage losses

In conventional machines friction against the air is a rounding error. Above roughly 100 m/s peripheral speed it becomes a principal loss mechanism and in some designs the dominant one.

Flow in the annular gap is governed by the Taylor number. Below a critical value the flow is laminar and drag is modest; above it the flow breaks into Taylor vortices, counter-rotating toroidal cells stacked along the axis, and drag rises sharply. Higher still, the vortices themselves become turbulent. Each transition raises the friction coefficient, and a machine may cross more than one between standstill and rated speed.

The dissipated power on the cylindrical rotor surface follows

    P_w = k · C_f · ρ_air · Ω³ · r_r⁴ · l                                (1.5)

where C_f depends on Taylor and Reynolds numbers and on surface roughness. The cubic dependence on angular velocity is the relation usually quoted, and it is the origin of the common claim that windage is what ultimately halts the pursuit of speed. Section 1.5 shows that this claim, though widely repeated, does not describe the design path engineers actually follow.

Two features make windage more troublesome than its magnitude suggests. It is deposited in the air gap, the least thermally accessible part of the machine and immediately adjacent to the magnets, so the heat reaches the most temperature-sensitive component by the shortest path. And it appears as a braking torque, reducing shaft output directly rather than merely adding a thermal burden. Where it becomes limiting, the responses are to reduce gas density — operating in a partial vacuum or in helium — or to attack C_f through surface finish and gap geometry.

## 1.4 The Converter as Gatekeeper

The converter is often listed as a fourth constraint alongside the mechanical, electromagnetic and thermal ones. That framing is convenient but inaccurate: the converter does not trade against the other three, it determines which regions of the space they define can be reached at all. It is a gate, not an axis.

### 1.4.1 Switching frequency and fundamental frequency

The relationship between switching frequency f_sw and fundamental frequency f₁ is expressed by the frequency modulation ratio

    m_f = f_sw / f₁                                                      (1.6)

In a mains-frequency drive m_f exceeds 100 and the current is very nearly sinusoidal. At high speed it falls, and two thresholds matter. Below about m_f = 21, asynchronous PWM produces subharmonic current components and synchronous PWM becomes necessary. Below roughly m_f = 10 the sampling delay becomes comparable with the fundamental period, the current regulator loses its ability to reject disturbances, and torque ripple and instability follow.

For the machine of Table 1.1, with f₁ = 1500 Hz, maintaining m_f = 21 requires

    f_sw = 21 × 1500 = 31.5 kHz

A silicon IGBT stage of this rating operates practically at 8 to 16 kHz. At 16 kHz the modulation ratio would be 10.7 — at the stability floor, well below the synchronous-PWM threshold, and with substantial harmonic content. This machine cannot be acceptably supplied by a silicon converter, and the shortfall cannot be engineered around at the machine end without changing the pole count.

**[Figure 1.5 near here]**
*Figure 1.5 Required switching frequency against fundamental frequency for two modulation ratios, with the practical ranges of silicon IGBT and wide-bandgap devices indicated. The worked example of Table 1.1 falls outside the silicon region.*

Poor current quality is undesirable in any drive; in a high-speed machine it is dangerous. Current harmonics produce air-gap field components asynchronous with the rotor, contributing no average torque but inducing eddy currents in every conducting body they reach — the magnets, a metallic retaining sleeve, and the rotor body in solid-rotor machines. This loss is deposited in a component thermally isolated by the air gap and cooled by the same air that is generating windage heat. In a permanent-magnet rotor the result is a magnet temperature rise, and the demagnetisation limit is frequently the binding thermal constraint of the whole machine.

The designer is therefore caught between two failure modes. Lowering the switching frequency to protect the converter heats the rotor; raising it to protect the rotor derates the converter. In conventional drives the trade-off is comfortable. At high speed the acceptable window may be empty for a given semiconductor technology, which is what "gate" means here.

### 1.4.2 What wide-bandgap devices changed

Silicon carbide and gallium nitride devices switch several times faster than silicon at comparable ratings and with substantially lower switching energy. Their significance is not that they improve converter efficiency, though they do, but that they moved the gate.

Before wide-bandgap devices, the achievable switching frequency capped the fundamental frequency, which capped the pole number, which set a floor under stator yoke thickness and therefore under machine mass. High-pole-count, mass-critical high-speed machines were not merely difficult to supply; they were pointless to design, because no converter could exploit them. Practical SiC devices removed that block and opened the design region described in Section 1.2.2.

They did not remove the gate; they raised it. A designer contemplating a twelve-pole machine at 40 000 r/min — 4 kHz fundamental, 84 kHz switching at m_f = 21 — is against the limit once more, now with a different semiconductor. The structure of the problem is unchanged.

## 1.5 Scaling Laws

Scaling arguments are the natural way to reason about a machine class, and the high-speed literature contains a standard set: power density rises linearly with speed, iron loss with the square, windage with the cube, and the combination eventually overwhelms the gains. The conclusion — that a speed exists beyond which further increase is self-defeating — is correct. The reasoning usually given for it is not, and the difference matters, because it changes which constraint the designer should be working against.

### 1.5.1 Three design paths

A scaling exponent is meaningless until one states what is held constant. "Windage scales with the cube of speed" is true at fixed geometry and false along the path a designer actually takes. Three paths must be distinguished:

**Path (a), fixed geometry.** An existing machine is run faster with no dimensional change. This is the overspeed case, and it is the path implicitly assumed by most quoted scaling exponents.

**Path (b), tip-speed limited at constant power.** The rating is fixed and the rotor is redesigned at each speed to sit exactly at the material limit, so v_tip is constant. This is the idealised design path.

**Path (c), rotordynamically constrained.** Path (b), but with active length capped because the rotor cannot be made arbitrarily slender. This is what real designs do.

### 1.5.2 Path (a): fixed geometry

With D_r and l constant and Ω doubled, the familiar exponents apply. Centrifugal stress rises fourfold, iron loss fourfold, windage eightfold, and output power doubles. For the overspeed question these are correct. As a description of what happens when a machine is *designed* for higher speed they are not, because no designer doubles the speed of a rotor while leaving its diameter alone — the fourfold stress increase would destroy it.

### 1.5.3 Path (b): the tip-speed-limited design path

Hold rated power and tip speed constant. Since v_tip = Ω·r_r is fixed, doubling Ω halves r_r. The sizing relation

    P ∝ D_r² · l · Ω · B̂ · A                                            (1.7)

with peak air-gap flux density B̂ and linear current density A constant, then requires active length to double to preserve the rating. Rotor volume halves — the power-density gain is real — but the machine becomes four times as slender, since l/D_r rises by a factor of four.

The loss consequences are not what the fixed-geometry exponents suggest. **Windage is unchanged:** substituting r_r ∝ Ω⁻¹ and l ∝ Ω into equation (1.5) gives P_w ∝ Ω⁻⁴·Ω·Ω³ = Ω⁰. The physical reading is more transparent than the algebra — windage is the product of a shear stress set by tip speed, a rotor surface area proportional to D_r·l, and the tip speed itself; along this path the tip speed is fixed by definition and the surface area is preserved, because the diameter reduction and length increase cancel exactly. **Iron loss doubles rather than quadruples,** because loss per unit mass rises as f₁² while iron mass falls with the halving active volume. **Direct-current copper loss is unchanged,** since at constant electric loading and current density the copper volume scales with D_r·l. Alternating-current effects do grow with frequency, but the ohmic baseline does not move.

Total loss therefore grows only through the iron, and grows sub-linearly. On this path a speed doubling buys a halving of volume for a modest efficiency penalty. If this were the whole story there would be no upper limit worth discussing.

### 1.5.4 What actually stops the process

The limit is rotordynamic, and it is severe. Substituting r_r ∝ Ω⁻¹ and l ∝ Ω into equation (1.4) gives

    n_cr ∝ Ω⁻¹ / Ω² = Ω⁻³                                               (1.8)

The first bending critical speed falls as the cube of the design speed while the operating speed rises linearly, so the ratio scales as

    n_op / n_cr ∝ Ω⁴                                                     (1.9)

A doubling of design speed degrades the rotordynamic margin by a factor of sixteen. This is why high-speed machines run supercritically: not by choice, but because along the only path that respects the material limit, the critical speed collapses far faster than the operating speed rises.

Equations (1.8) and (1.9) are idealised — a real rotor is not a uniform beam, bearing span exceeds active length, and shaft extensions add outboard mass — and the exponents should be read as indicating the severity of the trend rather than as design values. But the trend governs practice, and it is the reason rotor mechanical design cannot be left until the electromagnetic design is complete.

**[Figure 1.6 near here]**
*Figure 1.6 Divergence of operating speed and first bending critical speed along the tip-speed-limited path. The rotordynamic margin degrades as the fourth power of the speed multiplier.*

### 1.5.5 Path (c) and the corrected scaling table

Because equation (1.9) forbids unlimited slenderness, real designs cap the active length and accept a compromise elsewhere. If length may grow by only 50 per cent when speed doubles, preserving the rating through equation (1.7) requires a rotor diameter of 0.58 rather than 0.50 times the original, and tip speed rises by 32 per cent — the machine is pushed a third past its previous stress level, which must be recovered by a stronger material, a thicker sleeve or a reduced rating. Every quantity then lands between the two extremes, as Table 1.3 shows.

**Table 1.3** Factor change in principal design quantities for a doubling of rotational speed, along three design paths. Rated power is constant on paths (b) and (c) and doubles on path (a).

| Quantity | (a) fixed geometry | (b) tip-speed limited | (c) length capped |
|---|---|---|---|
| Rotor diameter | 1.00 | 0.50 | 0.58 |
| Active length | 1.00 | 2.00 | 1.50 |
| l/D_r ratio | 1.00 | 4.00 | 2.60 |
| Active volume | 1.00 | 0.50 | 0.58 |
| Centrifugal stress | 4.00 | 1.00 | 1.33 |
| Fundamental frequency | 2.00 | 2.00 | 2.00 |
| DC copper loss | 1.00 | 1.00 | 0.87 |
| Iron loss | 4.00 | 2.00 | 2.00 |
| Windage loss | 8.00 | 1.00 | 1.33 |
| Rotor surface area | 1.00 | 1.00 | 0.87 |
| First critical speed | 1.00 | 0.125 | 0.257 |
| n_op / n_cr | 2.00 | 16.00 | 7.79 |

**[Figure 1.7 near here]**
*Figure 1.7 The same speed doubling evaluated along the three design paths of Table 1.3.*

Three conclusions follow. The loss penalty of high speed is smaller than commonly claimed, provided the machine is genuinely redesigned rather than overspeed. The rotordynamic penalty is far larger than commonly claimed, and it is the mechanism that actually terminates the pursuit of speed. And the exponent one should quote depends entirely on the question being asked — a table of exponents with no stated path is not a design tool, which is why the path is explicit in every column of Table 1.3.

A note on thermal scaling is warranted here, because the square–cube law is frequently invoked in this context. That argument — losses scale with volume, cooling with surface area, so the ratio degrades as the machine shrinks — is correct only for a machine scaled isotropically. High-speed machines are not scaled isotropically: the tip-speed limit forces the rotor to shrink radially while growing axially, and under that anisotropic scaling the rotor surface area is very nearly preserved, as Table 1.3 shows. The thermal problem at high speed is real, but it is not the square–cube law. What does degrade is stator loss density and the length of the conduction path from rotor to coolant, the rotor being thermally isolated by an air gap whose conductance is poor and largely independent of stator cooling effort.

## 1.6 Framing the Design Challenges Ahead

### 1.6.1 Three constraints and a gate

High-speed machine design is not an extension of conventional design to higher frequency. It is a distinct discipline, defined by the collapse of safety margins and the strong coupling of physical domains that are normally treated separately.

The mechanical, electromagnetic and thermal constraints bound a design space in which every edge is a trade-off. Mechanical reinforcement of a surface-magnet rotor adds effective air gap and degrades electromagnetic performance. Raising pole count to reduce mass raises frequency and loss density, degrading the thermal position. Adding cooling geometry to relieve the thermal position complicates the stator structure and lengthens the machine, degrading rotordynamic behaviour.

Cutting across the space is the converter gate. As Section 1.4 established, it does not trade against the three constraints; it makes part of the space unreachable. Wide-bandgap semiconductors have raised the gate substantially and continue to, but they have not removed it.

**[Figure 1.8 near here]**
*Figure 1.8 The high-speed design space. Three mutually competing constraints bound the feasible region; the converter gate renders part of it unreachable regardless of how the three are balanced.*

### 1.6.2 Relationship to conventional machine design

This book assumes familiarity with conventional electrical machine design and does not repeat it. The reader is expected to know how a winding is laid out, how a magnetic circuit is dimensioned, how loadings are chosen and how a thermal network is assembled; these are treated comprehensively in the standard texts, to which reference is made throughout.

What is treated here is the regime in which conventional practice stops being sufficient. In every chapter the question is the same: which familiar assumption fails at high speed, why, and what replaces it. Loss models fitted below 400 Hz do not extrapolate to 2 kHz. A slot conductor sized on direct-current resistance is wrong once the skin depth approaches its dimensions. A rotor designed to a static stress limit is not qualified against fatigue. A thermal network that ignores the air gap as a heat source misses one of the largest terms. And a design sequence that begins with electromagnetic sizing begins in the wrong place.

### 1.6.3 Plan of the chapters

**Part I — The high-speed design space.** Chapter 2 surveys the applications, from gearless industrial compression to aerospace propulsion and e-turbocharging, and calibrates the classification criteria of Section 1.1.1 against a population of real machines. Chapter 3 compares the candidate topologies — solid-rotor and laminated induction machines, synchronous and PM-assisted reluctance machines, and surface- and interior-magnet synchronous machines — and treats the choice of winding at high fundamental frequency.

**Part II — Electromagnetic design.** Chapter 4 develops the inverted sizing procedure, working from the mechanical and rotordynamic limits inward to the electromagnetic design, with worked examples for both paradigms. Chapter 5 addresses alternating-current losses in the windings, comparing litz and form-wound conductors. Chapter 6 treats core and rotor losses in the kilohertz range, including the available soft magnetic materials and the manufacturing effects that degrade them.

**Part III — Mechanical and thermal design.** Chapter 7 develops rotor stress analysis and magnet retention, comparing carbon-fibre and metallic sleeves against interior-magnet bridge designs. Chapter 8 covers rotordynamics and bearing selection, and the vibration and acoustic behaviour that follows from both. Chapter 9 treats air-gap flow, windage and the thermal design of the complete machine.

**Part IV — Drive integration and delivery.** Chapter 10 develops the converter interface, including insulation stress under fast switching and bearing currents. Chapter 11 addresses control at low modulation ratios, including position sensing and sensorless operation. Chapter 12 presents complete design case studies from both paradigms, together with test methods, loss segregation at high speed, and qualification practice.

---

## References

*[To be completed. Confirmed citation from the present draft:]*

El Hajji, T., et al. (2024). Optimal design of high specific power electric machines for fully electric regional aircraft: a case study of 1 MW S-PMSM. *Aerospace*, 11(10), 820.

*[Citations still required, by location:]*

- §1.1.1 — primary source for the 150 m/s and n√P > 100 000 thresholds, if a source earlier than El Hajji et al. is preferred.
- §1.1.1 — Voltcar project reference for the machine data in Table 1.1.
- §1.3.1 — solid-rotor peripheral speed capability; sleeve pre-stress design.
- §1.3.2 — rotordynamic penalty of high l/D; bearing technology review.
- §1.3.3 — Taylor–Couette friction coefficient correlations.
- §1.5.3 — equation (1.7), the machine sizing relation. *Standard text reference.*
- §1.4.1 — m_f = 21 synchronous PWM threshold. *Standard power electronics text.*
- §1.2.1 — industrial direct-drive efficiency and TCO data.
