# 1 Introduction

## 1.1 What Changes at High Speed

A high-speed electrical machine is not a conventional machine turning faster. It is a machine in which the ordinary design margins have been consumed, and in which the constraints that a 50 Hz designer treats as background — rotor strength, shaft dynamics, air friction, the switching capability of the supply — have moved into the foreground and started to compete with one another.

That shift is what this book is about. In a mains-frequency induction motor, the designer chooses the bore diameter from a torque requirement, checks the tooth flux density, and moves on; the rotor will not burst, the first bending critical speed is an order of magnitude above the operating point, windage is a rounding error in the loss balance, and any commercial drive can supply the machine. In a machine running at 30 000 r/min none of these statements survives. The bore diameter is set by the strength of the rotor material before any electromagnetic consideration enters. The first bending mode may lie below the operating speed, so that the rotor must be accelerated through resonance on every start. Air friction in the gap may dissipate more power than the rotor conductors do. And the converter that supplies the machine may be physically unable to produce a current waveform clean enough to keep the rotor cool.

The consequence is that the design sequence itself changes. Conventional machine design proceeds outward from an electromagnetic specification: choose the loadings, size the bore, then verify mechanically and thermally. High-speed design runs the other way. The mechanical and rotordynamic limits fix the rotor geometry first, the converter fixes the admissible pole number, and the electromagnetic design is then fitted into whatever space those constraints leave. A designer who applies the conventional sequence to a high-speed specification will produce a machine that is electromagnetically elegant and mechanically impossible.

This chapter establishes the vocabulary and the physical boundaries that the rest of the book works within. Section 1.2 addresses a question that the literature still answers inconsistently — what "high speed" actually means, and which of the competing criteria is worth using. Section 1.3 sets out the four physical constraints. Section 1.4 examines how the machine behaves when speed is increased, and shows that the widely quoted scaling exponents are misleading because they describe a design path that no engineer actually follows. Section 1.5 treats the power converter as what it is: not a fourth design constraint but a gate that admits some designs and refuses others. Section 1.6 introduces the two design paradigms — the gearless industrial machine and the mass-limited mobile machine — that organise the whole book. Section 1.7 closes with the design space as a whole and the plan of the chapters that follow.

## 1.2 Defining High Speed

There is no agreed definition of a high-speed electrical machine. This is more than a terminological nuisance: without a criterion, published performance claims cannot be compared, and a designer cannot tell whether a given specification requires the methods in this book or whether conventional practice will do.

Three criteria are in circulation. Two are established and one is proposed here. All three are useful, and they are useful for different reasons, because each is sensitive to a different limiting physical mechanism.

### 1.2.1 The r/min fallacy

Rotational speed alone is a poor descriptor, and relying on it is the most common error in the field.

A dental handpiece turning at 400 000 r/min is, mechanically, an unremarkable object. Its rotor is a few millimetres in diameter, the centrifugal stresses in it are modest, and its rotordynamic behaviour is benign. A multi-megawatt process compressor turning at 15 000 r/min — a twenty-seventh of the speed — operates far closer to the limits of what its materials can survive. Judged on r/min the handpiece is the more extreme machine by a wide margin. Judged on any measure that reflects the actual physical loading, it is not close.

The reason is that no significant physical mechanism in a rotating machine depends on angular velocity alone. Centrifugal stress depends on the product of angular velocity and radius. Rotor losses and converter burden depend on electrical frequency, which is angular velocity multiplied by pole-pair number. Windage depends on surface velocity and rotor area. In each case the geometry enters, and the geometry is precisely what r/min discards.

A useful criterion must therefore combine speed with at least one other quantity. The three criteria below do this in three different ways.

### 1.2.2 Peripheral speed: the mechanical criterion

The peripheral, or tip, speed of the rotor

    v_tip = Ω · r_r = π · D_r · n / 60                                    (1.1)

where Ω is the mechanical angular velocity in rad/s, r_r the rotor radius, D_r the rotor diameter and n the rotational speed in r/min, is the natural mechanical measure, because centrifugal stress is a function of tip speed and of nothing else.

For a rotating solid disc of density ρ and Poisson ratio ν, the maximum tangential stress occurs at the centre and is

    σ_max = [(3 + ν)/8] · ρ · v_tip²                                     (1.2)

For the same disc with a small central bore — the geometry of any lamination stack mounted on a shaft — the maximum stress moves to the bore and doubles:

    σ_max = [(3 + ν)/4] · ρ · v_tip²                                     (1.3)

and for a thin rotating ring, which approximates a retaining sleeve, it is simply ρ·v_tip².

Nothing in equations (1.2) and (1.3) contains r_r or Ω separately. A large rotor turning slowly and a small rotor turning quickly, at the same tip speed, carry the same stress. This is the precise sense in which the dental handpiece is not a high-speed machine.

Figure 1.1 plots these three relations for electrical steel. Taking ρ = 7650 kg/m³ and ν = 0.3, a bored lamination at 200 m/s carries a peak stress of about 252 MPa, and at 250 m/s about 395 MPa. Against a high-strength electrical steel with a proof stress of roughly 450 MPa, and applying a safety factor of 1.5, the 250 m/s design is already outside the allowable envelope while the 200 m/s design is inside it. The factor-of-two penalty in equation (1.3) relative to (1.2) is the quantitative reason why solid rotors reach higher tip speeds than laminated ones, and why the shaft-mounting arrangement is a first-order design decision rather than a detail.

A threshold of v_tip > 150 m/s is commonly used to mark the onset of high-speed design (El Hajji et al., 2024). The value is conventional rather than physical — there is no discontinuity at 150 m/s — but it corresponds reasonably to the speed above which standard rotor constructions begin to require deliberate retention measures.

**[Figure 1.1 near here]**
*Figure 1.1 Maximum tangential stress against peripheral speed for a solid disc, a disc with a central bore and a thin ring, computed from equations (1.2) and (1.3) for electrical steel (ρ = 7650 kg/m³, ν = 0.3). The central bore doubles the stress; this is the penalty paid by any shaft-mounted lamination stack.*

### 1.2.3 The n√P criterion

Tip speed captures the mechanical loading but says nothing about rating. A 500 W machine and a 5 MW machine at the same tip speed present entirely different engineering problems, because the difficulty of building a high-speed machine grows with power at fixed speed as well as with speed at fixed power.

The empirical criterion

    n · √P > 100 000                                                     (1.4)

with n in r/min and P in kW, has been widely used for this reason (El Hajji et al., 2024). It has no derivation behind it; it is a correlation that happens to separate machines requiring specialist treatment from those that do not, across several decades of power. Its practical value is that it is computed from two numbers that appear on every nameplate.

### 1.2.4 The fP product: a drive-system criterion

Neither of the preceding criteria contains the pole number, and therefore neither contains the electrical frequency. This is a genuine omission, because two machines identical in rating, size and tip speed but differing in pole count present very different problems to the designer — and, more to the point, to the converter that must supply them.

Consider two machines, both 120 kW at 30 000 r/min. A two-pole design has a fundamental frequency of 500 Hz. A six-pole design of the same rotor diameter has 1500 Hz. Their tip speeds are identical, their n√P values are identical, and by both established criteria they are the same machine. They are not. The six-pole design has three times the core loss frequency, requires roughly three times the converter switching frequency to achieve the same current quality, and will very likely require wide-bandgap semiconductors where the two-pole design will not. The established criteria are blind to the difference.

We therefore propose a third measure, the product of fundamental frequency and rated power:

    f₁ · P    where    f₁ = p · n / 60                                   (1.5)

with p the number of pole pairs. Since f₁ is proportional to the product of speed and pole-pair number, the fP product differs from a simple speed–power product by exactly the factor that the other criteria omit.

The quantity has a straightforward interpretation. Rated power sets the current and voltage the converter must handle; fundamental frequency sets the rate at which it must handle them. Their product is therefore a measure of converter burden, and it rises both when a machine is made faster and when it is made lighter by increasing pole count. It is, in the terms used throughout this book, a *drive-system* criterion rather than a machine criterion: it describes the difficulty of supplying the machine rather than the difficulty of building it.

Two cautions are necessary. First, the fP product is introduced here as a descriptive figure of merit, not as a validated classification threshold. Assigning a numerical boundary requires a population of machines rather than a single design point, and that calibration is carried out in Chapter 2, where a survey of published and commercial high-speed machines is mapped onto all three criteria. Second, fP is a system measure and should not be read as a statement about the machine in isolation; a design with a high fP product is not necessarily harder to build, only harder to supply.

Figure 1.2 shows how the n√P and fP criteria sit relative to one another in the power–speed plane. They are not parallel, and the region between them is occupied by machines that one criterion admits and the other does not. Those machines — typically moderate-power, high-pole-count designs — are exactly the population for which the classification question is not academic.

**[Figure 1.2 near here]**
*Figure 1.2 The n√P and fP criteria in the power–speed plane. The fP contour is drawn for p = 3; changing the pole-pair number translates it vertically, which is the dependence the n√P criterion cannot express. The marked point is the worked example of Section 1.2.5.*

### 1.2.5 Worked example: classifying a traction machine

The high-speed traction machine designed in the EU Voltcar project provides a convenient reference point, and it is used as a running example through the remainder of this chapter. Its principal data are given in Table 1.1.

**Table 1.1** Voltcar six-pole radial-flux traction machine, inner rotor

| Quantity | Symbol | Value |
|---|---|---|
| Rated power | P | 120 kW |
| Maximum speed | n | 30 000 r/min |
| Rotor diameter | D_r | 96 mm |
| Pole pairs | p | 3 |

Applying the three criteria in turn:

*Peripheral speed.* From equation (1.1),

    v_tip = π × 0.096 m × 30 000 / 60 = 150.8 m/s

which exceeds the conventional 150 m/s threshold, but only just. Mechanically this machine sits at the boundary of the high-speed regime rather than deep inside it.

*The n√P criterion.* From equation (1.4),

    n√P = 30 000 × √120 = 3.29 × 10⁵

which exceeds the 10⁵ threshold by a factor of 3.3. By this measure the machine is comfortably in the high-speed class.

*The fP product.* From equation (1.5),

    f₁ = 3 × 30 000 / 60 = 1500 Hz,    f₁P = 1500 × 120 = 1.8 × 10⁵ kW/s

The disagreement between the first two criteria is itself instructive: a machine can be marginal mechanically and unambiguous electromagnetically, and the reason is the pole count. Had the same rotor been wound as a two-pole machine, the tip speed and the n√P value would have been unchanged while the fundamental frequency, and with it the fP product, would have fallen by a factor of three. The consequences of that choice are pursued in Section 1.5, where the converter requirement for this machine is derived.

## 1.3 The Four Physical Constraints

Four mechanisms limit what can be built. They are introduced here in the order in which they bind as speed is increased, which is also the order in which they should be checked in a design.

### 1.3.1 Mechanical: the tip-speed wall

Equations (1.2) and (1.3) fix a maximum tip speed for any rotor material, and that limit is hard in a way that thermal and electromagnetic limits are not. A machine running slightly too hot loses insulation life; a rotor turning slightly too fast fails, and the failure is not graceful.

The design responses fall into two families, and the choice between them is the principal topology decision in a permanent-magnet high-speed machine.

*Surface retention.* Rotor-surface magnets have negligible tensile strength and must be held in compression by an external sleeve, of carbon fibre where specific strength governs, or of Inconel or titanium where temperature and conductivity govern. The sleeve is applied with an interference fit or filament-wound with controlled tension so that the magnets remain in compression at maximum overspeed and at maximum temperature, the two conditions being additive because thermal expansion of the magnets and of the sleeve differ. The design penalty is that the sleeve occupies magnetic air gap: a 3 mm carbon-fibre sleeve added to a 1 mm mechanical clearance quadruples the effective gap and forces a corresponding increase in magnet volume to recover the air-gap flux density. This coupling — mechanical reinforcement paid for in magnet material — is the first of the trade-offs that make high-speed design a multi-domain problem, and it is treated in detail in Chapter 7.

*Internal retention.* Interior-magnet rotors hold the magnets in pockets within the lamination, so that the steel bridges and ribs carry the centrifugal load. No sleeve is required and the effective air gap stays small, but the bridges are simultaneously a magnetic short circuit. Thickening a bridge for strength increases leakage flux and reduces the useful magnet flux; thinning it for magnetic performance moves it towards its yield point. The optimum is narrow and it moves with speed, temperature and duty cycle.

Fatigue must be assessed separately from static strength. A traction rotor accumulates hundreds of thousands of load cycles over its life, and the stress concentrations at magnet-pocket corners are precisely where crack initiation occurs. A rotor that survives a single overspeed test is not thereby qualified.

### 1.3.2 Rotordynamics and the slenderness conflict

The tip-speed limit caps rotor diameter. Torque, however, scales with the square of diameter and with active length, so a diameter that has been capped must be compensated by length if the rating is to be maintained. High-speed rotors are therefore slender, and slenderness is the enemy of rotordynamic stability.

The first bending critical speed of a rotor behaving as a uniform beam scales as

    n_cr ∝ r_r / l²                                                      (1.6)

so that lengthening the rotor reduces the critical speed quadratically while the diameter reduction that forced the lengthening reduces it further. Section 1.4 quantifies how severely these two effects compound; the result is the single most important scaling relation in high-speed design.

The practical consequence is that many high-speed machines cannot be operated below their first critical speed and must instead run supercritically, passing through one or more resonances during every run-up and coast-down. This is routine engineering, but it is engineering that a conventional machine designer never has to do, and it makes the choice of bearing a first-order design decision rather than a component selection.

The available options span three orders of magnitude in cost and capability. Hybrid ceramic rolling-element bearings, with silicon nitride balls and oil-mist or jet lubrication, are compact and inexpensive and dominate traction applications, but they impose a finite Dn limit and remain a wearing part. Fluid-film and air-foil bearings remove the wear mechanism and permit oil-free operation, at the cost of limited load capacity and a susceptibility to sub-synchronous whirl. Active magnetic bearings eliminate contact altogether and, uniquely, allow stiffness and damping to be varied during operation, so that a rotor can be actively steered through a resonance that would destroy a passively supported machine; the price is a sensor and power-electronic system that is often comparable in complexity to the drive itself. Chapter 8 treats the selection and the analysis together, because at high speed the rotor and its bearings cannot be designed separately.

**[Figure 1.3 near here]**
*Figure 1.3 First and second bending modes of a slender high-speed rotor, shown as deflected shapes against the undeflected axis. The rotor is supported at the two bearings; the second mode has an interior node. The first bending critical speed scales as r_r/l², so lengthening a rotor to recover the torque lost to a reduced diameter reduces it quadratically.*

### 1.3.3 Aerodynamic drag and windage

In a mains-frequency machine the air in the gap is a passive medium and friction against it is a rounding error. Above roughly 100 m/s it becomes a principal loss mechanism, and in some designs the dominant one.

Flow in the annular gap between two concentric cylinders is governed by the Taylor number. Below a critical value the flow is laminar and the drag is modest. Above it the flow breaks into Taylor vortices — counter-rotating toroidal cells stacked along the axis — and the drag rises sharply. Higher still, the vortices themselves become turbulent. Each transition increases the friction coefficient, and a machine may cross more than one of them between standstill and rated speed.

The dissipated power on the cylindrical rotor surface follows

    P_w = k · C_f · ρ_air · Ω³ · r_r⁴ · l                                (1.7)

where C_f is a friction coefficient depending on Taylor and Reynolds numbers and on surface roughness. The cubic dependence on angular velocity is the relation usually quoted, and it is the origin of the common assertion that windage is the mechanism that ultimately halts the pursuit of higher speed. Section 1.4.4 shows that this assertion, though widely repeated, is wrong for the design path that engineers actually follow — the exponent is correct but it is being applied to the wrong variable.

Two features of windage make it more troublesome than its magnitude alone suggests. It is deposited in the air gap, which is the least accessible part of the machine thermally and is immediately adjacent to the magnets, so windage heat reaches the most temperature-sensitive component by the shortest path. And it is a braking torque, so it appears directly as a reduction in shaft output rather than merely as a thermal burden. Where it becomes limiting, the responses are to reduce the gas density — operating the rotor in a partial vacuum or in helium — or to attack C_f through surface finish and gap geometry. Chapter 9 develops both.

### 1.3.4 Thermal: loss density in a shrinking volume

The purpose of running fast is to make the machine smaller for a given rating. That is also the thermal problem: the same losses, or nearly the same, must be removed from a smaller object.

It is often argued that this follows from the square–cube law — losses scale with volume, cooling with surface area, so the ratio degrades as the machine shrinks. The argument is correct for a machine scaled isotropically, and it is worth stating clearly that high-speed machines are *not* scaled isotropically. As Section 1.4 shows, the tip-speed limit forces the rotor to shrink radially while growing axially, and under that anisotropic scaling the rotor surface area is very nearly preserved. The thermal problem at high speed is real, but it is not the square–cube law, and designing against the wrong mechanism leads to the wrong countermeasures.

What does degrade is the loss *density* in the stator, and the length of the conduction path from the rotor to any cooling surface. A stator carrying the same total loss in half the volume must reject twice the heat flux through a jacket of unchanged area, and the temperature gradient through the lamination stack and the slot insulation rises accordingly. This is why direct in-slot cooling, in which coolant is brought into contact with the conductors rather than with the frame, appears in high-speed machines at power levels where a conventional design would be comfortably jacket-cooled.

Rotor losses are the acute case. A rotor is thermally isolated by the air gap, whose conductance is poor and — importantly — largely independent of the cooling effort spent on the stator. Increasing the coolant flow in a water jacket does very little for a rotor that is radiating and convecting into a thin annulus of turbulent air. Rotor loss must therefore be either prevented at source, through magnet segmentation, sleeve material choice, harmonic reduction in the winding and clean converter current, or removed axially through the shaft. Both routes are expensive, which is why rotor loss estimation at high speed deserves the accuracy that Chapter 6 attempts and rarely receives in practice.

In permanent-magnet machines the constraint is sharpened further by the magnets themselves. Remanence falls with temperature, and above a limit that depends on the operating point the demagnetisation is irreversible: the machine does not recover when it cools. Because that limit sits well below the temperature the winding insulation could tolerate, the magnet temperature and not the winding temperature is frequently the binding thermal constraint in a high-speed PM machine. This is an inversion of conventional practice, where the winding is almost always the hot spot of interest, and it changes what a thermal model must resolve: an average rotor temperature is not sufficient when the quantity of interest is the peak temperature at the magnet corner nearest the air gap. Chapter 9 develops the models accordingly.

## 1.4 Scaling: What Actually Happens When Speed Is Doubled

Scaling arguments are the natural way to reason about a machine class, and the high-speed literature contains a standard set of them: power density rises linearly with speed, iron loss rises with the square, windage with the cube, and the combination eventually overwhelms the gains. The conclusion drawn is that there exists a speed beyond which further increase is self-defeating.

The conclusion is right. The reasoning usually given for it is not, and the difference matters, because it changes which constraint the designer should be working against.

### 1.4.1 Three design paths

The difficulty with a scaling exponent is that it is meaningless until one states what is being held constant. "Windage scales with the cube of speed" is true at fixed geometry and false along the path that a designer actually takes. Three paths must be distinguished.

**Path (a): fixed geometry.** An existing machine is run faster with no dimensional change. This is the overspeed case, relevant to qualification testing and to field weakening, and it is the path implicitly assumed by most quoted scaling exponents.

**Path (b): tip-speed-limited at constant power.** The rating is fixed and the rotor is redesigned at each speed to sit exactly at the material limit, so that v_tip is constant. This is the idealised design path and it is the one that a scaling argument about *machine design* ought to describe.

**Path (c): rotordynamically constrained.** Path (b), but with active length capped because the rotor cannot be made arbitrarily slender. This is what real designs do.

The three give sharply different answers, and Figure 1.5 compares them for a doubling of speed.

### 1.4.2 Path (a): fixed geometry

With D_r and l held constant and Ω doubled, the exponents are the familiar ones. Centrifugal stress, from equation (1.2), rises fourfold. Iron loss, scaling as f₁² at constant flux density and constant iron mass, rises fourfold. Windage, from equation (1.7), rises eightfold. Output power doubles, since torque is unchanged.

These are the numbers usually tabulated, and for the overspeed question they are correct. As a description of what happens when a machine is *designed* for a higher speed, they are not, because no designer doubles the speed of a rotor while leaving its diameter alone — the fourfold stress increase would destroy it.

### 1.4.3 Path (b): the tip-speed-limited design path

Now hold rated power and tip speed constant. Since v_tip = Ω·r_r is fixed, doubling Ω requires halving r_r. The sizing relation

    P ∝ D_r² · l · Ω · B̂ · A                                            (1.8)

with peak air-gap flux density B̂ and linear current density A held constant, then requires that active length double in order to preserve the rating. Rotor volume therefore halves — the expected power-density gain is real — but the machine becomes *four times* as slender, since l/D_r rises by a factor of four.

The loss consequences are not what the fixed-geometry exponents suggest.

*Windage is unchanged.* Substituting r_r ∝ Ω⁻¹ and l ∝ Ω into equation (1.7) gives P_w ∝ Ω⁻⁴ · Ω · Ω³ = Ω⁰. The physical reading is more transparent than the algebra: windage power is the product of a shear stress that depends on tip speed, a rotor surface area proportional to D_r·l, and the tip speed itself. Along this path the tip speed is fixed by definition and the surface area is preserved, because the diameter reduction and length increase cancel exactly. Constant tip speed and constant area give constant windage.

*Iron loss doubles rather than quadruples.* Loss per unit mass rises as f₁², but the iron mass falls in proportion to the active volume, which halves. The net is a factor of two.

*Direct-current copper loss is unchanged*, since at constant electric loading and current density the copper volume scales with D_r·l, which is preserved. Alternating-current effects in the conductors do grow with frequency and are the subject of Chapter 5, but the ohmic baseline does not move.

*Rotor surface area is unchanged*, which is the correction to the square–cube argument noted in Section 1.3.4.

Total loss therefore grows only through the iron, and grows sub-linearly. On this path a speed doubling buys a halving of volume for a modest efficiency penalty. If this were the whole story, there would be no upper limit worth discussing.

### 1.4.4 What actually stops the process

The limit is rotordynamic, and it is severe.

Substituting r_r ∝ Ω⁻¹ and l ∝ Ω into equation (1.6) gives, for a rotor treated as a uniform beam,

    n_cr ∝ Ω⁻¹ / Ω² = Ω⁻³                                               (1.9)

The first bending critical speed falls as the cube of the design speed while the operating speed rises linearly with it. The ratio of operating speed to first critical speed therefore scales as

    n_op / n_cr ∝ Ω⁴                                                     (1.10)

A doubling of design speed degrades the rotordynamic margin by a factor of sixteen. This is why high-speed machines run supercritically: not because designers choose to, but because along the only path that respects the material limit, the critical speed collapses far faster than the operating speed rises. Figure 1.4 shows the divergence.

Equations (1.9) and (1.10) are idealised. A real rotor is not a uniform beam; bearing span exceeds active length, shaft extensions and couplings add mass outboard of the bearings, and the stiffening effect of a shrink-fitted sleeve or a solid rotor body is not captured. The exponents should be read as indicating the severity of the trend rather than as design values. But the trend is what governs practice: it is the reason that a chapter of this book is devoted to rotordynamics and bearings, and the reason that rotor mechanical design cannot be left until after the electromagnetic design is complete.

**[Figure 1.4 near here]**
*Figure 1.4 Divergence of operating speed and first bending critical speed along the tip-speed-limited design path, from equations (1.9) and (1.10). The rotordynamic margin degrades as the fourth power of the speed multiplier.*

### 1.4.5 Path (c): the constrained design

Because equation (1.10) forbids the unlimited slenderness that path (b) assumes, real designs cap the active length and accept a compromise elsewhere. Suppose length is permitted to grow by only 50 per cent when speed is doubled. Preserving the rating through equation (1.8) then requires a rotor diameter of 0.58 rather than 0.50 times the original, and tip speed rises by 32 per cent — the machine is pushed 33 per cent past its previous stress level, which must be recovered by a stronger material, a thicker sleeve, or a reduction in rating.

Every quantity now lands between the two extremes. Windage rises by a third rather than staying flat; the rotordynamic margin degrades by a factor of about eight rather than sixteen; centrifugal stress rises by a third rather than staying constant. Table 1.2 collects the three paths.

**Table 1.2** Factor change in principal design quantities for a doubling of rotational speed, along three design paths. Path (a) holds geometry fixed; path (b) holds rated power and tip speed constant; path (c) additionally caps active length at 1.5 times its original value.

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

Rated power is constant on paths (b) and (c) and doubles on path (a).

**[Figure 1.5 near here]**
*Figure 1.5 The same speed doubling evaluated along the three design paths of Table 1.2. The fixed-geometry exponents commonly quoted in the literature describe path (a) and overstate the loss penalty of a genuine high-speed redesign, while understating the rotordynamic penalty by an order of magnitude.*

### 1.4.6 Reading the table

Three conclusions follow, and they set the priorities for the rest of the book.

The loss penalty of high speed is smaller than commonly claimed, provided the machine is genuinely redesigned rather than overspeed. The eightfold windage increase that appears throughout the literature belongs to path (a) and does not describe a design exercise.

The rotordynamic penalty is far larger than commonly claimed, and it is the mechanism that actually terminates the pursuit of speed. A designer who tabulates stress, iron loss and windage but not the critical-speed margin has omitted the binding constraint.

And the scaling exponent one should quote depends entirely on the question being asked. This is not pedantry: a table of exponents with no stated path is not a design tool, and Table 1.2 is arranged as it is so that the path is explicit in every column.

## 1.5 The Converter as Gatekeeper

The power converter is often listed as a fourth constraint alongside the mechanical, electromagnetic and thermal ones. That framing is convenient but inaccurate. The converter does not trade against the other three; it determines which regions of the space they define can be reached at all. It is a gate, not an axis.

### 1.5.1 Fundamental and switching frequency

The relationship between the converter switching frequency f_sw and the machine fundamental frequency f₁ is expressed by the frequency modulation ratio

    m_f = f_sw / f₁                                                      (1.11)

In a mains-frequency drive m_f exceeds 100 and the current waveform is very nearly sinusoidal. At high speed it falls, and two thresholds matter. Below about m_f = 21 asynchronous pulse-width modulation produces subharmonic current components and synchronous PWM becomes necessary. Below roughly m_f = 10 the sampling delay becomes comparable with the fundamental period, the current regulator loses the ability to reject disturbances, and torque ripple and instability follow.

For the Voltcar machine of Table 1.1, with f₁ = 1500 Hz, maintaining m_f = 21 requires

    f_sw = 21 × 1500 Hz = 31.5 kHz

A silicon IGBT stage of this rating operates practically at 8 to 16 kHz. At 16 kHz the modulation ratio would be 10.7 — at the stability floor, well below the synchronous-PWM threshold, and with substantial harmonic content. This machine cannot be supplied acceptably by a silicon converter. The requirement is not marginal and it cannot be engineered around at the machine end without changing the pole count.

**[Figure 1.6 near here]**
*Figure 1.6 Required switching frequency against fundamental frequency for two modulation ratios, with the practical ranges of silicon IGBT and wide-bandgap devices indicated. The worked example of Table 1.1 falls outside the silicon region.*

### 1.5.2 Why current harmonics matter more at high speed

Poor current quality is undesirable in any drive. In a high-speed machine it is dangerous, for reasons specific to the rotor.

Current harmonics produce air-gap field components that are asynchronous with the rotor. These contribute no average torque but induce eddy currents in every conducting body they reach: the magnets, the retaining sleeve if it is metallic, and the rotor body itself in solid-rotor machines. The resulting loss is deposited in a component that is thermally isolated by the air gap and cooled principally by the same air whose motion is generating windage heat. In a permanent-magnet rotor the consequence is a temperature rise in the magnets, whose demagnetisation limit is frequently the binding thermal constraint of the whole machine.

The designer is therefore caught between two failure modes. Reducing the switching frequency to protect the converter increases harmonic content and heats the rotor. Raising it to protect the rotor increases switching loss and derates the converter. In conventional drives this trade-off is comfortable; at high speed the acceptable window may be empty for a given semiconductor technology, which is precisely what "gate" means here.

### 1.5.3 What wide-bandgap devices changed

Silicon carbide and gallium nitride devices switch several times faster than silicon at comparable ratings and with substantially lower switching energy. Their significance for this book is not that they improve converter efficiency, though they do, but that they moved the gate.

Before wide-bandgap devices, the achievable switching frequency capped the fundamental frequency, which capped the pole number, which set a floor under stator yoke thickness and therefore under machine mass. High-pole-count, high-speed, mass-critical machines were not merely difficult to supply; they were pointless to design, because no converter could exploit them. The arrival of practical SiC devices removed that block and opened the design region that Section 1.6.2 describes.

It did not remove the gate. It raised it. A designer contemplating a twelve-pole machine at 40 000 r/min — 4 kHz fundamental, 84 kHz switching frequency at m_f = 21 — is once again against the limit, now with a different semiconductor. The structure of the problem is unchanged.

## 1.6 Two Design Paradigms

The constraints of Sections 1.3 to 1.5 apply to every high-speed machine. They do not produce a single kind of machine, because different applications weight them differently. Two families result, and their design conventions are close to opposite. This division organises the whole book: subsequent chapters address both, and the differences between them are usually more instructive than the common ground.

Before describing them it is worth recording why high-speed machines became common at all, because the answer is different in the two families and it explains their divergence.

For most of the twentieth century, industrial processes requiring high rotational speed obtained it mechanically. A four-pole mains-connected induction motor at 1500 or 1800 r/min drove a step-up gearbox, and the gearbox drove the compressor, blower or pump. The motor was a commodity, the speed conversion was a solved mechanical problem, and there was no alternative: without a variable-frequency supply, the machine ran at the speed the grid dictated. The arrangement survives in large numbers and it works.

What changed was the availability of the converter. Once a machine could be supplied at an arbitrary frequency, the speed conversion could be moved from the gearbox into the electrical domain, and the gearbox could be deleted. That single substitution is the origin of the industrial high-speed machine, and its consequences are more far-reaching than the efficiency arithmetic suggests. Gearboxes are maintenance-intensive: they require lubrication systems, oil coolers and periodic seal replacement, and they dissipate typically 2 to 5 per cent of the power passing through them. In large installations the lubrication plant dictates the layout of the building, because the oil reservoir must sit below the drive — which is why geared high-speed units are frequently housed over two storeys, with the tank in a basement. Removing the gearbox removes all of it.

The mobile high-speed machine has a different origin. There, the converter was necessary anyway, because the load demands variable speed regardless. What high speed offered instead was mass: as Section 1.6.2 sets out, the same power produced at higher speed and lower torque requires a smaller and lighter machine. The gearbox was consequently not deleted but retained, because a fixed-ratio reduction gear turned out to be a cheaper way of obtaining wheel torque than a larger machine.

The two families therefore arrive at high speed by opposite routes and for opposite reasons — one to eliminate a gearbox, the other to justify keeping one — and the design conventions that follow diverge accordingly.

### 1.6.1 The gearless industrial machine

Centrifugal compressors, aeration blowers for wastewater treatment, turbo-expanders and organic Rankine cycle generators share an economic structure. They run continuously for years — an availability target of 100 000 hours between interventions is not unusual — they are judged on total cost of ownership over a twenty-year life, and mass is nearly irrelevant because the machine is bolted to a foundation.

Mounting the impeller directly on the motor shaft and supporting it on magnetic or foil bearings yields a hermetically sealed, oil-free unit. This is a decisive advantage in food, pharmaceutical and semiconductor processes, where oil contamination of the process stream is unacceptable, and in subsea installations where a leak is an environmental incident rather than a maintenance item. With no gear teeth to wear and, in the magnetic-bearing case, no contacting parts at all, the mean time between failures rises substantially.

The design conventions follow from the economics rather than from any physical necessity.

Pole counts are low: two-pole induction machines, or two- and four-pole rotor-surface-magnet synchronous machines. This keeps the fundamental below about 1 kHz and the drive within reach of standard IGBT converters, and it has two further benefits that are easy to overlook. A two-pole machine has the lowest core-loss frequency available at a given speed, and it has the highest attainable power factor, which reduces converter current rating for the same shaft power. It also permits relatively thick laminations of 0.2 to 0.35 mm, avoiding both the material cost and the handling difficulty of thin foil.

The induction machine remains a workhorse in this family because of its ruggedness. Its rotor may be a solid steel body, slitted or copper-coated to improve the loss and torque characteristics, or a high-strength lamination stack with a cage. The absence of magnets removes the retention problem altogether and removes any concern about demagnetisation, and the rotor tolerates temperatures that would destroy a PM machine. Where efficiency governs, the surface-magnet synchronous machine displaces it, since rotor cage loss disappears — but the magnets then require sleeves.

Rotor retention is generous, because a thick carbon-fibre or Inconel sleeve costs little in a machine whose mass is unconstrained. Rotor diameters are correspondingly large, since torque is cheaper to obtain from diameter than from length, and peripheral speeds of 200 to 250 m/s are routine. Air gaps are large, at several millimetres, which reduces windage, accommodates thermal growth and eases manufacturing tolerance, at the cost of magnetising current — the opposite of the traction convention, where the gap is minimised to maximise torque density. Rotor thermal management typically relies on a conductive shield, or on the sleeve itself acting as a barrier to harmonic fields, combined with forced-air or liquid jacket cooling of the stator.

Every one of these choices trades performance for robustness. In this application that is the correct trade, and a designer who optimised the same machine for specific power would have produced something worse.

### 1.6.2 The mass-limited mobile machine

Traction, aerospace propulsion and turbomachinery for internal combustion engines invert the priorities. Mass is the objective; the machine is carried, and every kilogram costs range, payload or fuel. The applications span a wide speed range: automotive traction has moved from 10 000 r/min towards and beyond 20 000 r/min over roughly a decade; hybrid-electric aircraft propulsion and generation demand specific powers above 10 to 15 kW/kg, which conventional topologies cannot approach; and electrically assisted turbochargers and turbo-compounding units operate beyond 100 000 r/min, where the machine must be nearly invisible in mass and volume so as not to disturb the balance of the engine it serves.

The dominant relation is that stator yoke thickness varies inversely with pole number, because the flux per pole falls as poles are added. Going from two poles to eight quarters the flux per pole and permits a corresponding reduction in yoke thickness, with a large saving in the heaviest single component of the machine. This is why mobile machines use six, eight or twelve poles where industrial machines use two. It is worth being precise about what is being traded here: the pole count is not chosen for any electromagnetic virtue, but purchased as a mass reduction, and paid for in frequency.

The cost is frequency, and it is charged in three places. An eight-pole machine at 15 000 r/min has a 1000 Hz fundamental; at 30 000 r/min it has 2000 Hz. Core loss per unit mass rises with frequency, and must be recovered through thin, high-grade laminations of 0.1 to 0.2 mm, which are more expensive per kilogram and considerably more difficult to stack and handle without degrading their magnetic properties. The resulting loss density exceeds what a jacket can remove, so direct liquid cooling becomes necessary; in automotive practice the transmission oil is frequently used, cooling the windings and rotor as well as lubricating the gears. And, as Section 1.5 established, the switching frequency required to supply such a machine is out of reach for silicon. The mass saving is real, but it is bought with material cost, cooling complexity and a wide-bandgap converter.

Interior-magnet rotors dominate this family, for three reasons that compound. The lamination bridges provide retention without a sleeve, keeping the effective air gap small and so preserving torque density — the opposite resolution of the same trade-off the industrial machine makes with a thick sleeve. The buried geometry creates saliency, a difference between direct- and quadrature-axis inductance, which contributes reluctance torque in addition to magnet torque and supports the wide constant-power speed range that vehicle traction requires. And field weakening is effective, which matters greatly when the available DC-link voltage is fixed by a battery whose state of charge varies.

The bearing choice also inverts. Where the industrial machine adopts magnetic or foil bearings to eliminate maintenance, the mobile machine uses high-precision oil-lubricated hybrid ceramic rolling-element bearings, because they are cheaper, more compact, and tolerant of the shock and vibration of road or airframe service. An active magnetic bearing system on a vehicle would add sensors, power electronics and a control loop whose failure modes are safety-relevant, in exchange for a maintenance benefit that a ten-year vehicle life does not need.

And the gearbox that the industrial machine eliminated is retained. Since P = T·Ω, generating a given power at high speed and low torque produces a far smaller and cheaper machine than generating it at low speed and high torque. A direct-drive traction machine sized for wheel torque would be large, heavy and expensive in both copper and magnet material. It is economically and physically superior to generate the power at high speed in a small machine and trade speed for torque through a robust fixed-ratio reduction gear. This is the economic paradox of the mobile paradigm: adding components makes the system cheaper and lighter, and it is the exact inverse of the industrial conclusion.

### 1.6.3 The same physics, opposite conclusions

The two paradigms are summarised in Table 1.3. The point of the comparison is not that one is superior but that both are correct: an industrial designer who adopted eight poles and a SiC converter would have raised cost and reduced reliability for a mass saving of no value, and a traction designer who adopted a two-pole rotor with a thick sleeve would have produced a machine too heavy to use.

**Table 1.3** Design conventions of the two paradigms

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

**[Figure 1.7 near here]**
*Figure 1.7 Geared and direct-drive architectures compared. Above: a mains-connected motor drives the load through a step-up gearbox, with the lubrication plant below floor level. Below: the impeller is mounted directly on the high-speed motor shaft and carried on active magnetic bearings, giving a single sealed unit with no oil system and no second storey.*

## 1.7 The Design Space and the Plan of This Book

### 1.7.1 Three constraints and a gate

Figure 1.8 assembles the argument. The mechanical, electromagnetic and thermal constraints bound a design space, and every edge of that space is a trade-off in which improving one constraint degrades another. Mechanical reinforcement of a surface-magnet rotor adds effective air gap and degrades electromagnetic performance. Raising pole count to reduce mass raises frequency and therefore loss density, degrading the thermal position. Adding cooling geometry to relieve the thermal position complicates the stator structure and lengthens the machine, degrading rotordynamic behaviour.

Cutting across the space is the converter gate. It does not trade against the three constraints; it makes part of the space unreachable. Wide-bandgap semiconductors have raised the gate substantially, and continue to, but they have not removed it and there is no reason to expect that they will.

**[Figure 1.8 near here]**
*Figure 1.8 The high-speed design space. Three mutually competing constraints bound the feasible region; the converter gate renders part of it unreachable regardless of how the three are balanced.*

### 1.7.2 Relationship to conventional machine design

This book assumes familiarity with conventional electrical machine design and does not repeat it. The reader is expected to know how a winding is laid out, how a magnetic circuit is dimensioned, how loadings are chosen and how a thermal network is assembled; these are treated comprehensively in the standard texts, to which reference is made throughout rather than reproducing their content here.

What is treated here is the regime in which that conventional practice stops being sufficient. In each chapter the question is the same: which of the familiar assumptions fails at high speed, why it fails, and what replaces it. Loss separation models fitted below 400 Hz do not extrapolate to 2 kHz. A slot conductor sized on direct-current resistance is wrong once the skin depth approaches its dimensions. A rotor designed to a static stress limit is not qualified against fatigue. A thermal network that ignores the air gap as a heat source misses one of the largest terms. And a design sequence that begins with electromagnetic sizing begins in the wrong place.

Notation follows established convention throughout, so that a reader moving between this book and the standard design texts is not obliged to relearn symbols. Rotational speed n is in r/min and mechanical angular velocity Ω in rad/s; p denotes pole pairs rather than poles, so that f₁ = pn/60; B̂ is the peak fundamental air-gap flux density and A the linear current density, both defined at the air gap. Where a quantity is specific to high-speed work and has no settled symbol — the frequency modulation ratio m_f, the peripheral speed v_tip — it is defined at first use and listed in Appendix B.

### 1.7.3 Plan of the chapters

**Part I — The high-speed design space.** Chapter 2 surveys the applications, from gearless industrial compression to aerospace propulsion and e-turbocharging, and calibrates the classification criteria of Section 1.2 against a population of real machines. Chapter 3 compares the candidate topologies — solid-rotor and laminated induction machines, synchronous and PM-assisted reluctance machines, and surface- and interior-magnet synchronous machines — and treats the choice of winding at high fundamental frequency.

**Part II — Electromagnetic design.** Chapter 4 develops the inverted sizing procedure indicated in Section 1.1, working from the mechanical and rotordynamic limits inward to the electromagnetic design, with worked examples for both paradigms. Chapter 5 addresses alternating-current losses in the windings, comparing litz and form-wound conductors. Chapter 6 treats core and rotor losses in the kilohertz range, including the soft magnetic materials available and the manufacturing effects that degrade them.

**Part III — Mechanical and thermal design.** Chapter 7 develops rotor stress analysis and magnet retention, comparing carbon-fibre and metallic sleeves against interior-magnet bridge designs. Chapter 8 covers rotordynamics and bearing selection, and the vibration and acoustic behaviour that follows from both. Chapter 9 treats air-gap flow, windage and the thermal design of the complete machine.

**Part IV — Drive integration and delivery.** Chapter 10 develops the converter interface, including insulation stress under fast switching and bearing currents. Chapter 11 addresses control at low modulation ratios, including position sensing and sensorless operation. Chapter 12 presents complete design case studies drawn from both paradigms, together with test methods, loss segregation at high speed, and qualification practice.

---

## References

*[To be completed. Confirmed citation from the present draft:]*

El Hajji, T., et al. (2024). Optimal design of high specific power electric machines for fully electric regional aircraft: a case study of 1 MW S-PMSM. *Aerospace*, 11(10), 820.

*[Citations still required, by location:]*

- §1.2.2, §1.2.3 — primary source for the 150 m/s and n√P > 100 000 thresholds, if a source earlier than El Hajji et al. is preferred.
- §1.2.5 — Voltcar project reference for the machine data in Table 1.1.
- §1.3.1 — solid-rotor peripheral speed capability; sleeve pre-stress design.
- §1.3.2 — rotordynamic penalty of high l/D; bearing technology review.
- §1.3.3 — Taylor–Couette friction coefficient correlations.
- §1.4.3 — equation (1.8), the machine sizing relation. *Standard text reference.*
- §1.5.1 — m_f = 21 synchronous PWM threshold. *Standard power electronics text.*
- §1.6.1 — industrial direct-drive efficiency and TCO data.
- §1.7.2 — the conventional design texts this book builds on.
