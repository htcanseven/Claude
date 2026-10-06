# Specific speed: the Introduction only, and what that changes elsewhere

**Decision (6 October 2026).** Ahti Jaatinen-Värri's specific-speed material goes into the
Introduction, in full. Chapter 2 remains Juha Saari's entire, as agreed, and §2.2 no longer
derives specific speed — it applies the result. Ahti's own section in the book is Chapter 13,
which he holds jointly with Jonna Tiainen; the Introduction contribution is separate from it.

The book treats specific speed **once**. That is the point of writing it down here.

---

## 1. Where it goes in Chapter 1

A new **§1.1.2, "Where the speed requirement comes from"**, between the definitional material
of §1.1.1 and the history of the direct-drive transition. The present §1.1.2 becomes §1.1.3.

The chapter asserts the speed requirement four times before it is a third through — "required
for compressors, pumps, and fans"; "the necessary impeller tip speeds"; "the turbine's native
speed"; "a 2-pole machine at 30 000 r/min" — and never says who decides the number. "Native
speed" is specific speed under another name, used without definition. One subsection ahead of
all four closes the hole.

Renumbering is safe: nothing in the chapter cross-references §1.1.2 by number, and the one
numbered reference in that region is to §1.1.1, which is unaffected.

Chapter 1's equations are unnumbered. Six new ones need numbers, so either §1.1.2 numbers its
own (1.1)–(1.6) and the rest of the chapter stays as it is, or the whole chapter is numbered.
The first is less work and reads normally.

**Budget.** 26 → 28 pages, 4 → 5 tables, figures unchanged at 9. Book total 452 → 454, still
well inside the 500-page ceiling.

**Credit.** Ahti is named at the head of Chapter 1 as the contributor of §1.1.2. The owners
table now carries that row.

---

## 2. What changes in Chapter 2

§2.2 was "Why the driven machine sets the speed: specific speed and the turbomachinery
optimum". With the derivation in Chapter 1 that section would repeat two pages of a 500-page
book and put two contributors on the same ground. It is retitled and rescoped:

> **2.2 From duty to speed: where the industrial applications fall in the specific-speed
> bands** (the relation itself is derived in §1.1.2)

and the chapter abstract now reads, in its opening:

> It begins from the driven machine rather than the motor, because that is where the speed
> requirement originates. The specific-speed relation itself is derived once, in §1.1.2, and
> is not repeated here; this chapter takes it as given and asks where each industrial duty
> falls against it, so that the reader sees why one application lands at 30 000 r/min and
> another at 100 000.

This is a better section for Saari than the old one. Deriving *N*s is not what he brings;
knowing which duty lands where, and what that costs in machine terms, is.

The owner note also drops the clause asking him to recruit a co-author for §2.2. He no longer
needs one there — §2.2 rests on §1.1.2.

**He has the old wording.** The table of contents already sent to him carries the old §2.2
title. Nothing starts before a contract, so there is no risk of wasted writing, but the
detailed section structure he is waiting for must carry the new wording, and it is worth one
line in the covering note so he sees the change rather than discovers it.

---

## 3. Draft of §1.1.2

Ahti's draft 2 carried through, with the corrections from `incoming/ahti_specific_speed/`
applied: Ω restored inside equation (1.1), *R*u in the numerator of (1.3), densities
recomputed at the 15 °C the table states, ρ in kg/m³, and *T*in added as a column.

> ### 1.1.2 Where the speed requirement comes from
>
> The preceding section asked what counts as a high-speed machine. It did not ask why any
> machine should have to be one, and the answer is not an electrical one. In almost every
> application treated in this book the rotational speed reaches the electrical designer
> already fixed, decided by the machine being driven.
>
> Turbomachinery design begins from the specific speed,
>
> > *N*s = Ω √*q*v,in ⁄ Δ*h*s^(3/4)  (1.1)
>
> in which Ω [rad/s] is the angular velocity, *q*v,in [m³/s] the inlet volumetric flow rate
> and Δ*h*s [J/kg] the isentropic enthalpy difference the stage must produce. The group is
> dimensionless, and it applies to every class of turbomachine: axial and radial compressors,
> axial and radial turbines, pumps and fans. The inlet volume flow follows from the required
> mass flow and the inlet thermodynamic state; the isentropic enthalpy difference follows from
> the inlet state, the required pressure ratio and the working fluid itself.
>
> For each class of machine there is a band of *N*s within which good isentropic efficiency can
> be reached; for centrifugal compressors that band is roughly 0.6 to 0.9 [Rodgers, 1980].
> Once the designer has chosen a design specific speed, the corresponding rotational speed
> follows. The bands are semi-empirical guidelines rather than hard limits, and it is
> sometimes worth designing off-optimum and paying for it in efficiency, but they are narrow
> enough to settle the answer.
>
> For an ideal gas the quantities in (1.1) are available in closed form. The isentropic
> enthalpy rise is
>
> > Δ*h*s = *R*i (1 − 1/γ)⁻¹ (*T*out,s − *T*in)  (1.2)
>
> where *R*i [J/kg K] is the specific gas constant, γ the ratio of specific heat capacities and
> *T*out,s [K] the isentropic outlet temperature. The specific gas constant is
>
> > *R*i = *R*u ⁄ *M*  (1.3)
>
> with *R*u [J/mol K] the universal gas constant and *M* [kg/mol] the molar mass of the working
> fluid; the isentropic outlet temperature is
>
> > *T*out,s = *T*in (PR)^((γ−1)/γ)  (1.4)
>
> for a pressure ratio PR; the inlet volume flow is
>
> > *q*v,in = *q*m ⁄ ρin  (1.5)
>
> for a desired mass flow *q*m [kg/s]; and for a perfect gas the inlet density comes from the
> equation of state,
>
> > ρin = *p*in ⁄ (*R*i *T*in)  (1.6)
>
> For working fluids that are not well approximated as ideal — refrigerants, organic Rankine
> cycle fluids, steam, carbon dioxide near its critical point — the properties must be taken
> from a thermodynamic library such as CoolProp or REFPROP, and the structure of the
> calculation is unchanged.
>
> **Table 1.x** applies this to two compressors with identical duty and different working
> fluids. Both draw 3 kg/s at 1 bar and 15 °C and deliver a pressure ratio of 3, and both are
> designed at *N*s = 0.80, the middle of the centrifugal band.
>
> | | Fluid | *M* [kg/mol] | *R*i [J/kg K] | γ | *T*in [K] | ρin [kg/m³] | *q*v,in [m³/s] | Δ*h*s [J/kg] | *N* [r/min] |
> |---|---|---|---|---|---|---|---|---|---|
> | Compressor | air | 0.0290 | 287 | 1.40 | 288 | 1.209 | 2.481 | 106 700 | 28 640 |
> | Compressor | hydrogen | 0.0020 | 4157 | 1.41 | 288 | 0.0835 | 35.94 | 1 550 400 | 55 990 |
>
> Two things in that table carry the argument of this book. The first is that nothing
> electrical entered the calculation. The air machine is the industrial compressor drive used
> as a running example throughout these chapters: its duty alone gives close to 29 000 r/min,
> which is why 30 000 r/min recurs as the nominal figure, and some 320 kW of isentropic work,
> about 400 kW at the shaft. The speed was decided by aerodynamics, and the electrical machine
> is required to deliver it.
>
> The second is the effect of the working fluid. Δ*h*s rises as the molar mass falls — equations
> (1.2) and (1.3) — so the same duty in hydrogen demands an isentropic enthalpy rise about
> 14.5 times that in air, and, through (1.1), very nearly twice the shaft speed. That is why
> hydrogen compression is a driver of high-speed machine development rather than an
> application of the machines that already exist, and it is treated as such in §2.8.
>
> Equation (1.1) also says, for a fixed fluid, inlet state and design specific speed, that the
> larger the mass flow the lower the speed, and the higher the pressure ratio the higher the
> speed. Small machines run fast. This is the mechanism behind the e-turbocharger of §2.7,
> where a mass flow two orders of magnitude below the compressor above puts the design speed
> past 100 000 r/min.
>
> Two consequences organise the rest of the book. The speed is not among the quantities the
> machine designer may trade: pole number, rotor diameter, bearing type, cooling architecture
> and converter are all negotiable, the number on the nameplate is not, and a sizing procedure
> that treats it as an input rather than a boundary condition fails in the way described in
> Chapter 7. And the speed arrives before any electromagnetic decision has been taken, which
> is why this book runs the design sequence in the order it does.

Reference to add: Rodgers, C. (1980). *Specific speed and efficiency of centrifugal
impellers.* 25th Annual International Gas Turbine Conference, New Orleans.

---

## 4. Still needed from Ahti

- **The turbine convention.** Juha asked whether the volume flow in (1.1) is the inlet volume
  for a turbine as well as for a compressor. It is not answered in draft 2, and it cannot be
  guessed: a reader who assumes inlet for both will size a turbine wrong. One sentence settles
  it, and §1.1.2 should carry it, because the book uses (1.1) for ORC turbines and
  turbo-expanders as well as compressors.
- **Confirmation of the corrected table.** The 0 °C/15 °C inconsistency in his draft is
  corrected above; he should check the numbers before they are set.
- **The figure, if one is wanted.** The specific-speed-against-efficiency chart belongs in
  §2.2 with the application map, not in §1.1.2, and should be redrawn from Balje or Rodgers
  rather than from the company blog post he linked, which is not citable.

## 5. When to apply it

Chapter 1 is stamped and already with Wrobel, Saari and Jaatinen-Värri/Tiainen. Hold this and
issue one revised Chapter 1 before submission, together with the other pending items: the
missing §1.2 heading (the chapter runs §1.1.2 straight into §1.2.1 with no Heading 2 between),
the roadmap's pulse-ratio wording against "nine or eleven" in Juha's table of contents, and
"mechanical rpm value" in §1.1 against r/min everywhere else.
