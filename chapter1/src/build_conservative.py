"""Build the CONSERVATIVE version of Chapter 1.

Rule: the original draft's prose is reproduced verbatim.  Corrections are made
by ADDING text, tables and figures alongside the original wording wherever that
is possible.  Existing sentences are deleted or replaced only where an addition
cannot fix the problem, and every such case is listed in OPS below, so the edit
set is auditable and provably small.

Run:  python3 src/build_conservative.py
"""
import json, re, sys

SRC, OUT = 'original_draft_text.json', 'ch1_conservative.md'

# Paragraphs that carried a heading style in the draft (recovered by inspection).
HEADINGS = {
    40, 48, 50, 54, 66, 68, 72, 77, 80, 82, 85, 88, 93, 95, 100, 102, 104, 107,
    112, 116, 118, 120, 125, 131, 134, 139, 141, 142, 144, 147, 153, 156, 162,
    170, 172, 177, 185, 187, 194, 197, 210, 212, 218, 223, 229, 242, 246, 252,
    254, 256, 258, 260, 262, 264,
}
EQUATIONS = {43, 179, 220}
TABLE_CAPTIONS = {60, 203, 234}
SKIP = {70, 71, 155, 175, 176, 244, 245}          # figure placeholders, replaced below
TABLE_ROWS = set(range(61, 65)) | set(range(204, 210)) | set(range(235, 241))


# ─────────────────────────────────────────────────────────── the edit set
# Each entry is (kind, anchor-prefix, payload).  'after' inserts new material,
# 'drop' removes a paragraph, 'replace' substitutes one.
OPS = [
    # ---- unavoidable removals ------------------------------------------------
    ('drop', 'The fP product is discussed in the context of classifying machines',
     'Drafting artefact: the sentence apologises for its own missing citation '
     '("without external resources provided").'),

    ('replace', 'In summary, the definitions for high-speed machines remain varied',
     'In summary, the definitions for high-speed machines remain varied: tip speed, '
     'n√P, and now the fP product.'),

    # ---- additions -----------------------------------------------------------
    ('after', 'Conversely, solid rotors, often found in high-performance induction', """
The factor of two is exact for a thin disc. For a solid rotating disc of density ρ and Poisson ratio ν the maximum tangential stress occurs at the centre and is

    σmax = [(3 + ν)/8] · ρ · vtip²

while introducing a small central bore moves the maximum to the bore and doubles it:

    σmax = [(3 + ν)/4] · ρ · vtip²

Figure 1.3 evaluates both for electrical steel, taking ρ = 7650 kg/m³ and ν = 0.3. A bored lamination reaches about 252 MPa at 200 m/s and about 395 MPa at 250 m/s. Against a high-strength grade with a proof stress near 450 MPa and a safety factor of 1.5, the 250 m/s design is already outside the allowable envelope while the 200 m/s design is inside it. This is the quantitative form of the advantage that solid rotors hold over laminated ones.

**[Figure 1.3 near here]**
*Figure 1.3 Maximum tangential stress against peripheral speed for a solid disc, a disc with a central bore and a thin ring, for electrical steel (ρ = 7650 kg/m³, ν = 0.3). The central bore doubles the stress, which is the penalty paid by any shaft-mounted lamination stack.*
"""),

    ('after', 'If we consider that the two first definitions fulfil the definition', """
Two qualifications should be attached to this figure. The value is proposed here from a single design point, and the Voltcar machine is itself marginal by the tip-speed criterion, at 150.8 m/s against a 150 m/s threshold, so it is a weak anchor for a classification boundary. At this stage the fP product is therefore best read as a descriptive figure of merit for converter burden rather than as a validated threshold; Chapter 2 calibrates it against a population of published machines.

What the fP product does capture, and what neither vtip nor n√P can, is the pole number. The same 120 kW rotor wound as a two-pole machine would have an identical tip speed and an identical n√P, while its fundamental frequency, and with it the fP product, would fall by a factor of three. Figure 1.1 shows how the two criteria sit relative to one another in the power–speed plane.

**[Figure 1.1 near here]**
*Figure 1.1 The n√P and fP criteria in the power–speed plane. The fP contour is drawn for p = 3; changing the pole-pair number translates it vertically, which is the dependence that n√P cannot express. The marked point is the machine of Table 1.1.*
"""),

    ('after', 'This conflict is the primary reason why high-speed design requires a holistic', """
It is worth putting a number on this conflict for the machine of Table 1.1. At a fundamental frequency of 1500 Hz, maintaining mf = 21 requires a switching frequency of 31.5 kHz. A silicon IGBT stage of this rating operates practically at 8 to 16 kHz; at 16 kHz the modulation ratio would be 10.7, which is at the control-stability floor identified above and far below the synchronous-PWM threshold. This machine therefore cannot be supplied acceptably from a silicon converter, and the shortfall cannot be recovered at the machine end without changing the pole number. Figure 1.6 shows where the boundary falls.

**[Figure 1.6 near here]**
*Figure 1.6 Required switching frequency against fundamental frequency for two modulation ratios, with the practical ranges of silicon IGBT and wide-bandgap devices indicated. The machine of Table 1.1 falls outside the silicon region.*
"""),

    ('after', 'As we scale a machine down to reach higher speeds, the ratio of Loss/Surface Area', """
One qualification is worth adding here. The square–cube argument assumes that the machine is scaled isotropically, with every dimension changing in proportion. High-speed machines are not scaled that way. The tip-speed limit caps the diameter, so the rotor shrinks radially while growing axially in order to recover the rating, and along that path the rotor lateral surface area, which is proportional to Dr·l, is very nearly preserved. What does degrade is the loss density inside the stator, and the length of the conduction path out of the rotor, which is thermally isolated by an air gap whose conductance is poor and largely independent of the cooling effort spent on the stator.
"""),

    ('after', 'By understanding these scaling laws, the designer can identify the sweet spot', """
#### 1.5.5 Reading the scaling table: which path is being followed

Table 1.3 is best read one row at a time, because the rows are not all evaluated under the same condition. The power and stress rows state their condition explicitly, namely constant power as the diameter is reduced and constant stress as the tip speed is held fixed. The iron-loss and windage rows, by contrast, are evaluated at fixed rotor geometry, which is the overspeed case rather than the design case. The distinction matters, because a designer moving to a higher speed does not hold the geometry fixed: the tip-speed limit forces the diameter down, and the rating is then recovered by increasing the active length.

It is therefore useful to tabulate the same speed doubling along the path that a design actually follows, with rated power and peripheral speed both held constant, so that the rotor radius scales as Ω⁻¹ and the active length as Ω. Table 1.4 gives the result and Figure 1.7 compares the two paths.

**Table 1.4** The same doubling of speed evaluated along the tip-speed-limited design path, at constant rated power

| Quantity | Scaling | Factor on doubling Ω |
|---|---|---|
| Rotor diameter Dr | ∝ Ω⁻¹ | 0.50 |
| Active length l | ∝ Ω | 2.00 |
| l/Dr ratio | ∝ Ω² | 4.00 |
| Active volume | ∝ Ω⁻¹ | 0.50 |
| Centrifugal stress σmec | constant | 1.00 |
| Iron loss PFe | ∝ Ω | 2.00 |
| Windage loss Pwnd | constant | 1.00 |
| Rotor surface area | constant | 1.00 |
| First critical speed ncr | ∝ Ω⁻³ | 0.125 |

Two entries deserve comment. Windage is unchanged rather than increased eightfold, because windage power is the product of a shear stress set by the tip speed, which is fixed by definition along this path, and a rotor surface area proportional to Dr·l, which is preserved because the diameter reduction and the length increase cancel. Iron loss doubles rather than quadruples, because the loss per unit mass rises as f² while the iron mass falls with the halving active volume. The fourfold and eightfold figures of Table 1.3 are correct for overspeeding an existing machine; it is only their application to a redesign that would mislead.

**[Figure 1.7 near here]**
*Figure 1.7 The same doubling of speed evaluated along three design paths: fixed geometry, tip-speed limited at constant power, and tip-speed limited with the active length capped by rotordynamics.*

#### 1.5.6 Rotordynamic scaling: where the returns actually stop

The last row of Table 1.4 deserves a section of its own, because it identifies the constraint that in practice terminates the pursuit of higher speed.

Section 1.3.2 established that high-speed rotors become long and thin. Treating the rotor as a uniform beam, the first bending critical speed scales as

    ncr ∝ rr / l²

Substituting the tip-speed-limited path used for Table 1.4, with rr ∝ Ω⁻¹ and l ∝ Ω,

    ncr ∝ Ω⁻¹ / Ω² = Ω⁻³

so that the first critical speed falls as the cube of the design speed while the operating speed rises linearly with it. The ratio of the two therefore scales as

    nop / ncr ∝ Ω⁴

A doubling of the design speed degrades the rotordynamic margin by a factor of sixteen, as Figure 1.8 shows. This is why so many high-speed machines must be operated supercritically. It is not a design preference: along the only path that respects the material limit, the critical speed collapses far faster than the operating speed rises.

These exponents are idealised. A real rotor is not a uniform beam, the bearing span exceeds the active length, shaft extensions and couplings add mass outboard of the bearings, and a shrink-fitted sleeve or a solid rotor body stiffens the assembly. They should be read as indicating the severity of the trend rather than as design values. The trend is nevertheless what governs practice, and it is the reason that the rotor's mechanical and rotordynamic design cannot be left until the electromagnetic design is complete.

**[Figure 1.8 near here]**
*Figure 1.8 Divergence of the operating speed and the first bending critical speed along the tip-speed-limited design path. The rotordynamic margin degrades as the fourth power of the speed multiplier.*
"""),

    # ---- roadmap: must match the 12-chapter table of contents ----------------
    ('replace_block', 'This book is structured as a comprehensive journey', """
This book is structured as a journey through the multidisciplinary landscape of high-speed engineering. Following this introduction, the text is organised into four parts, each addressing a pillar of the high-speed trilemma.

#### Part I: The High-Speed Design Space

Chapter 2 surveys the applications, from gearless industrial compression through aerospace propulsion to electrically assisted turbocharging, and calibrates the classification criteria of Section 1.1.1 against a population of real machines. Chapter 3 compares the candidate topologies: solid-rotor and laminated induction machines, synchronous and permanent-magnet-assisted reluctance machines, and surface- and interior-magnet synchronous machines, together with the choice of winding at high fundamental frequency.

#### Part II: Electromagnetic Design

Chapter 4 develops the sizing procedure, working from the mechanical and rotordynamic limits inward to the electromagnetic design, with worked examples for both the industrial and the mobile paradigm. Chapter 5 addresses AC copper losses, comparing Litz wire and form-wound conductors and the mitigation of skin and proximity effects. Chapter 6 treats core and rotor losses in the kilohertz range, including the soft magnetic materials available, the manufacturing effects that degrade them, eddy currents in sleeves and magnets, and magnet segmentation.

#### Part III: Mechanical and Thermal Design

Chapter 7 develops rotor stress analysis and magnet retention, comparing carbon fibre and metallic sleeves against interior-magnet bridge designs, and addresses fatigue life and overspeed margin. Chapter 8 covers rotordynamics and bearing selection, from high-precision rolling elements through air foil systems to active magnetic bearings, together with the vibration and acoustic behaviour that follows from both. Chapter 9 treats air-gap flow, windage including Taylor–Couette effects, and the thermal design of the complete machine.

#### Part IV: System Integration and Delivery

Chapter 10 develops the power electronic interface, specifically the role of SiC and GaN devices, insulation stress under fast switching, and the mitigation of bearing currents. Chapter 11 addresses control at high fundamental frequency, including position sensing and sensorless operation at low pulse ratios. Chapter 12 presents complete design case studies drawn from both paradigms, together with test methods, loss segregation at high speed, and overspeed and endurance qualification.
"""),
]

# Figure placeholders in the draft, given real artwork and captions.
FIGURE_FILLS = {
    70: ('1.2', 'Geared and direct-drive architectures compared. Above, a mains-connected '
                'motor drives the load through a step-up gearbox, with the lubrication plant '
                'below floor level. Below, the impeller is mounted directly on the high-speed '
                'motor shaft and carried on active magnetic bearings, giving a single sealed '
                'unit with no oil system and no second storey.'),
    155: ('1.4', 'First and second bending modes of a slender high-speed rotor, shown as '
                 'deflected shapes against the undeflected axis. The second mode has an '
                 'interior node. Because the first bending critical speed scales as rr/l², '
                 'lengthening a rotor to recover the torque lost to a reduced diameter reduces '
                 'it quadratically.'),
    175: ('1.5', 'Flow regimes in the air gap. Below the critical Taylor number the flow is '
                 'laminar and the drag is modest; above it the flow breaks into counter-rotating '
                 'toroidal cells, and both the drag torque and the rotor heating rise sharply.'),
    244: ('1.9', 'The high-speed design space. The mechanical, electromagnetic and thermal '
                 'constraints bound the feasible region, and the converter acts as a gate that '
                 'renders part of that region unreachable regardless of how the three are '
                 'balanced.'),
}


def find(paras, prefix):
    for i, p in enumerate(paras):
        if p.startswith(prefix):
            return i
    sys.exit(f'ANCHOR NOT FOUND: {prefix!r}')


def main():
    paras = json.load(open(SRC, encoding='utf-8'))
    n_orig = len(paras)
    audit = {'verbatim': 0, 'dropped': 0, 'replaced': 0, 'added_blocks': 0, 'roadmap': 0}

    # emit the body first, then apply operations against paragraph indices
    drop_idx, replace_map, after_map = set(), {}, {}
    for kind, anchor, payload in OPS:
        i = find(paras, anchor)
        if kind == 'drop':
            drop_idx.add(i); audit['dropped'] += 1
        elif kind == 'replace':
            replace_map[i] = payload; audit['replaced'] += 1
        elif kind == 'after':
            after_map[i] = payload; audit['added_blocks'] += 1
        elif kind == 'replace_block':
            # replace this paragraph and everything up to the closing sentence
            j = find(paras, 'This roadmap ensures that whether the reader')
            for k in range(i, j):
                drop_idx.add(k)
            replace_map[i] = payload
            audit['replaced'] += 1
            audit['roadmap'] = (j - i)

    out = ['# 1 Introduction', '']
    i = 0
    while i < n_orig:
        if i < 40:                       # planning skeleton at the head of the draft
            i += 1; continue
        if i in SKIP and i not in FIGURE_FILLS:
            i += 1; continue
        if i in drop_idx and i not in replace_map:
            i += 1; continue

        if i in FIGURE_FILLS:
            num, cap = FIGURE_FILLS[i]
            out += [f'**[Figure {num} near here]**', f'*Figure {num} {cap}*', '']
            i += 1; continue

        if i in replace_map:
            out += [replace_map[i].strip(), '']
            i += 1; continue

        p = paras[i]

        if i in TABLE_ROWS:              # emit a contiguous run of table rows once
            rows = []
            while i < n_orig and i in TABLE_ROWS:
                cells = [c.strip() for c in paras[i].split('|')]
                rows.append(cells); i += 1
            width = max(len(r) for r in rows)
            rows = [r + [''] * (width - len(r)) for r in rows]
            out.append('| ' + ' | '.join(rows[0]) + ' |')
            out.append('|' + '---|' * width)
            for r in rows[1:]:
                out.append('| ' + ' | '.join(r) + ' |')
            out.append('')
            audit['verbatim'] += len(rows)
            continue

        if i in HEADINGS:
            if re.match(r'^\d+\.\d+\.\d+', p):
                out += [f'### {p}', '']
            elif re.match(r'^\d+\.\d+\.?\s', p):
                out += [f'## {p}', '']
            else:
                out += [f'#### {p}', '']
        elif i in EQUATIONS:
            out += [f'    {p}', '']
        elif i in TABLE_CAPTIONS:
            out += [f'**{p}**', '']
        else:
            out += [p, '']
        audit['verbatim'] += 1

        if i in after_map:
            out += [after_map[i].strip(), '']
        i += 1

    open(OUT, 'w', encoding='utf-8').write('\n'.join(out))

    body = n_orig - 40                   # paragraphs below the planning skeleton
    print(f'wrote {OUT}')
    print(f'  original paragraphs             {n_orig}')
    print(f'  planning skeleton removed       40  (head of draft, not prose)')
    print(f'  figure placeholders filled       {len(FIGURE_FILLS)}')
    print(f'  body paragraphs                 {body}')
    print(f'  reproduced verbatim             {audit["verbatim"]}')
    print()
    print('  edits to existing prose:')
    print(f'    sentences deleted              {audit["dropped"]}  (the drafting artefact)')
    print(f'    sentences trimmed              {audit["replaced"] - 1}')
    print(f'    roadmap paragraphs replaced   {audit["roadmap"]}  (19-chapter plan -> 12-chapter plan)')
    print(f'  new material added              {audit["added_blocks"] + 1} blocks, 5 figures, 1 table')
    touched = audit['dropped'] + (audit['replaced'] - 1) + audit['roadmap']
    print()
    print(f'  body paragraphs touched         {touched} of {body}')
    print(f'  => body prose left untouched:   {100*(body-touched)/body:.1f}%')
    print(f'  => excluding the roadmap:       {100*(body-touched+audit["roadmap"])/body:.1f}%')


if __name__ == '__main__':
    main()
