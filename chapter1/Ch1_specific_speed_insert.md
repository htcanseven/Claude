# Integrating Ahti's specific-speed text into the Introduction

## Where

**A new §1.1.2, "Where the speed requirement comes from", between the definitions and the
history.** The current §1.1.2 becomes §1.1.3.

The chapter's own order asks for it there. §1.1.1 answers *what counts as high speed* —
tip speed, n√P, the fP product. The next question a reader has is *why does anything have
to be high speed*, and the chapter never answers it; it moves straight to how industry
delivered the speed, first with gearboxes and then without. The requirement is asserted
four times before the chapter is a third through:

- §1.1.2 ¶1: "the industrial standard for achieving high-speed rotation, **required for
  compressors, pumps, and fans**"
- §1.2.1: "Traditionally, these required a speed-increasing gearbox to reach **the
  necessary impeller tip speeds**"
- §1.2.1: "the ability to operate at **the turbine's native speed** (often 20 000 to
  50 000 r/min)"
- §1.2.1: "a 2-pole machine at **30 000 r/min** results in a 500 Hz fundamental frequency"

"Native speed" is specific speed under another name, used without ever being defined, and
30 000 r/min arrives from nowhere. One subsection ahead of all four of them closes the hole.

Putting it any later does not work. §1.2.1 is about topology and retention strategy, and by
then the unexplained numbers have already been used. §1.3 is the constraints, which is where
the chapter starts answering a different question.

### Renumbering is safe
Nothing in the chapter cross-references §1.1.2 by number. The one numbered forward
reference in that region is to §1.1.1 ("calibrates the classification criteria of Section
1.1.1"), which is unaffected. The chapter's equations are unnumbered, so a numbered (1.1)
either starts a scheme or stays unnumbered in the chapter's present style — the latter is
less work and consistent.

## How much

**Not all of it.** §2.2 of the table of contents is "Why the driven machine sets the speed:
specific speed and the turbomachinery optimum", and it belongs to Juha Saari's Chapter 2.
Ahti's draft 2 — six equations, the air-against-hydrogen table, non-ideal fluids — is a §2.2
in miniature. Printing it twice costs two pages of a 500-page ceiling and makes the two
chapters read as duplicates, which is the one thing the DREM-companion positioning promises
the book does not do.

The split that works:

| | Chapter 1, §1.1.2 | Chapter 2, §2.2 |
|---|---|---|
| the question, and that the answer is not electrical | ✓ | |
| equation (1), with units, and dimensionless | ✓ | ✓ restated |
| the good Ns band for centrifugal compressors | ✓ one line | ✓ per machine class, with the chart |
| one worked number, landing on the book's own compressor | ✓ | |
| equations (2)–(6), the ideal-gas apparatus | | ✓ |
| the air-against-hydrogen table | | ✓ |
| non-ideal fluids, CoolProp/Refprop | | ✓ |
| the turbine convention for volume flow | | ✓ |
| the Balje / Rodgers efficiency chart | | ✓ |

Chapter 1 needs about 420 words and one equation — three quarters of a page. **No figure**:
the chapter already carries nine in twenty-six pages, and the chart is §2.2's.

## Draft of the insert

> ### 1.1.2 Where the speed requirement comes from
>
> The preceding section asked what counts as a high-speed machine. It did not ask why any
> machine should have to be one, and the answer is not an electrical one. In almost every
> application treated in this book the rotational speed reaches the electrical designer
> already fixed, decided by the machine being driven.
>
> Turbomachinery design begins from the specific speed,
>
> > *N*s = Ω √*q*v,in ⁄ Δ*h*s^(3/4)
>
> in which Ω [rad/s] is the angular velocity, *q*v,in [m³/s] the inlet volumetric flow rate
> and Δ*h*s [J/kg] the isentropic enthalpy difference the stage must produce. The group is
> dimensionless, and it applies to every class of turbomachine: axial and radial
> compressors, axial and radial turbines, pumps and fans. For each class there is a band of
> *N*s within which good isentropic efficiency can be reached; for centrifugal compressors
> that band is roughly 0.6 to 0.9 [Rodgers, 1980]. The bands are semi-empirical guidelines
> rather than hard limits, and a designer may work off-optimum and pay for it in efficiency,
> but they are narrow enough to settle the answer.
>
> Since the duty of the stage fixes *q*v,in and Δ*h*s, the equation then fixes Ω. Take the
> centrifugal air compressor that recurs throughout this book: 3 kg/s at inlet conditions of
> 1 bar and 15 °C, with a pressure ratio of 3. The inlet density follows from the gas law
> and the isentropic enthalpy rise from the inlet state and the pressure ratio; with *N*s at
> the middle of the good band this gives a shaft speed close to 29 000 r/min — which is why
> 30 000 r/min recurs as the nominal figure in this book — and some 320 kW of isentropic
> work, about 400 kW at the shaft. No electrical quantity has entered the calculation. The
> speed was decided by aerodynamics, and the electrical machine is required to deliver it.
>
> Two consequences follow, and they organise the rest of the book. The first is that the
> speed is not among the quantities the machine designer may trade. Pole number, rotor
> diameter, bearing type, cooling architecture and converter are all negotiable; the number
> on the nameplate is not, and a design procedure that treats it as an input rather than a
> boundary condition will fail in the way described in Chapter 7. The second is that the
> number moves with the working fluid. Δ*h*s rises as the molar mass falls, so the same duty
> in hydrogen rather than air asks for roughly twice the shaft speed. That is why hydrogen
> compression is a driver of high-speed machine development rather than an application of
> the machines that already exist. Section 2.2 develops the argument in full, with the
> thermodynamic relations behind Δ*h*s, the behaviour of non-ideal working fluids, and the
> corresponding convention for turbines.

Reference to add: Rodgers, C. (1980). *Specific speed and efficiency of centrifugal
impellers.* 25th Annual International Gas Turbine Conference, New Orleans.

### The numbers in it are the corrected ones
"Close to 29 000 r/min" is deliberate: it is right whether Ahti's table is left as it stands
(29 405) or corrected for the 0 °C/15 °C inconsistency (28 640). It will not need revisiting
when he fixes the table.

## Practical order of operations

Chapter 1 is finished, stamped confidential and already with Wrobel, Saari and
Jaatinen-Värri/Tiainen. Adding a subsection means a new version, a re-stamp and a decision
about whether to resend.

Since the proposal has not gone to Wiley, **hold it**. Collect this with the other pending
Chapter 1 work and issue one revised version before submission rather than three. The other
items waiting:

- the missing §1.2 heading — the chapter runs §1.1.2 straight into §1.2.1 with no Heading 2
  for "The two paradigms" in between;
- the roadmap's pulse-ratio wording against Juha's "nine or eleven" in the table of
  contents;
- "mechanical rpm value" in §1.1, against r/min everywhere else.

## One thing to settle before it is written

Ahti is writing for Chapter 1 at Juha's request, but the material's home in the table of
contents is §2.2, which belongs to Juha Saari — who has accepted Chapter 2 and is waiting
for the detailed section structure. Two people are now working the same ground without
knowing it. Whichever way it falls, Saari needs to be told what §2.2 still contains before
he starts, and Ahti's name belongs in the contributor list against Chapter 1 as well as
Chapter 13.
