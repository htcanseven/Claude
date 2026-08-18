# EPEi 2026 → IEEE TIA: two-paper plan

Conference paper at EPEi 2026, extended to a post-conference IEEE Transactions on
Industry Applications submission via the IAS invitation route.

## 1. Venue facts

**EPEi 2026** — 14th IEEE International Conference and Exposition on Electrical and
Power Engineering, Iași, Romania, 22–24 October 2026.

| Item | Value |
|---|---|
| Full paper deadline | 18 July 2026 — **passed, must confirm with chairs** |
| Acceptance notification | 31 August 2026 |
| Camera-ready + registration | 30 September 2026 |
| Length | 4–6 pages; shorter is auto-rejected |
| Template | IEEE conference template, strict compliance required for Xplore |
| Submission | Microsoft CMT — https://cmt3.research.microsoft.com/EPEi2026/ |
| Indexing | IEEE Xplore, Web of Science Core Collection |
| Fees (early, by 7 Oct) | €450 non-member / €390 IEEE / €300 student / €250 IEEE student |
| Registration coverage | One registration covers at most 2 papers by the same author |
| AI disclosure | Mandatory — state which sections used generative AI and which tool |

**IAS status.** EPEi appears on the IAS conference schedule as **Co-sponsored** — a
tier above "Technical Co-sponsored", alongside ECCE, IEMDC, APEC, PEMC and ICEMS.
The conference page carries the IAS logo (with PES, Education Society, IMS).

## 2. The TIA route

TIA policy: except for special issues, all TIA papers are improved versions of papers
presented at an IAS sponsored or co-sponsored conference.

- The **invitation is issued by the conference organizers**, not requested by authors.
- It is **capped**: the annual MOU sets the quota. For technical co-sponsorship this is
  typically up to ~20% of papers. EPEi is a tier above, but the slice is still selective.
- Presentation must be within the previous **12 months**.
- The Transactions version must **not** be a verbatim copy; **≥20% change** expected.
- The conference paper must be **cited** in the Transactions version.
- Typically **~4 weeks** to submit after the invitation is issued.

**Implication:** write for the invited slice. A minimum-length paper is the wrong play.
Target a strong 6 pages that visibly reads as the seed of a Transactions paper.

## 3. Topic

> **Constraint added.** The MitDev-Eletrica PMSG dataset (Zenodo 15741561) is already
> used in another TIA paper currently under review and is therefore unavailable.
>
> **The conflict may be wider than the dataset.** MitDev-Eletrica is an inter-turn /
> inter-winding short-circuit dataset. If the under-review paper is ITSC diagnosis,
> swapping datasets does not clear the overlap: a second ITSC paper reaches the same
> TIA committee, likely draws overlapping reviewers, and can be read by an editor as
> one contribution split across two submissions. **Open question — what does the
> under-review paper cover?** If it is ITSC diagnosis, move off the fault mode
> entirely, not just the data.

### Recommended: pivot to thermal

Equally supported by existing work (*Applied Thermal Engineering* 2025, direct liquid
cooling; *IEEE Access* 2025, hairpin cooling arrangements) and clear of all three fault
papers — *Machines* 2026, IET Power Electronics 2026, and the TIA paper under review.

**Dataset — Electric Motor Temperature (Paderborn LEA)**
https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature

185 h, 69 measurement profiles, ~1.33 M samples, 13 columns: ambient, coolant, u_d,
u_q, motor_speed, torque, i_d, i_q, and targets `pm` (rotor magnet), `stator_yoke`,
`stator_tooth`, `stator_winding`. German OEM prototype PMSM, mildly anonymized.

2 Hz sampling is adequate here — thermal time constants are seconds to minutes. The
resolution objection that rules out SCADA data does not apply to a thermal problem.

**Warning: this dataset is crowded.** Kirchgässner's benchmark (IEEE TEC 2021),
Thermal Neural Networks (LPTN in recurrent state-space form), LPTN-informed neural
networks, OLTEM 2025, and assorted LSTM/BiLSTM work. Plain "physics-informed thermal
estimation on the Paderborn set" is already done and will be rejected.

**The open angle — cross-cooling-topology transfer.** Every published model on this
dataset trains and tests on the same machine with the same cooling arrangement. Whether
a thermal model learned on one cooling topology survives transfer to another is
unstudied.

It should not survive, for a statable reason: direct liquid cooling bypasses the
winding → tooth → yoke → housing path that a conventionally-cooled model has
internalized as its dominant thermal resistance. Failure is physically predictable.

This gives:
- **Public data as source domain**, with TNN et al. as benchmarks to beat on their turf
- **Own rig + FEA as target domain**, forcing the hardware anchor TIA expects rather
  than bolting it on afterwards
- A contribution requiring knowledge of the cooling physics, not only the time series

### Alternative, if staying in fault diagnosis

**Mendeley 10.17632/rgn5brrgrn.5** — https://data.mendeley.com/datasets/rgn5brrgrn/5
CC BY. Three PMSMs (1.0 / 1.5 / 3.0 kW, 4-pole, 3000 rpm, Higen), inter-turn and
inter-coil short circuits, 8 severity levels each (to 21.69% and 37.66% fault ratio),
current at 100 kHz, vibration at 25.6 kHz.

Weakness: **a single operating condition** (3000 rpm, 1.5 Nm). No load/speed robustness
story, which is the first thing a TIA reviewer asks for. Own-rig data would be needed
to fill that gap.

Viable only if the under-review TIA paper is *not* about ITSC.

### Evaluated: the Brno (CEITEC BUT) ISC datasets

Both are companion datasets to papers by Zezula, Kozovský, Buchta and Blaha at CEITEC,
Brno University of Technology. Both CC BY.

| | Zenodo 15233529 (Apr 2025) | Zenodo 21717722 (Jul 2026) |
|---|---|---|
| Companion paper | *Discrete-Time Modeling of ISCs in Interior PMSMs*, IEEE TIE 73(1), Jan 2026 | Mitigation paper — not clearly indexed yet |
| Machine | Interior PMSM, concentrated winding, 21 pole pairs, 253 W nom, 3.78 Nm, 638 rpm | Three-phase PMSM drive |
| Severities | 3/25, 6/25, 10/25 turns | 3/25, 6/25, 9/25 turns |
| SC resistance | 4 levels: R_FIU {442, 47.0, 5.62, 1.74} mΩ + R_wire 14.4 mΩ | Progressive levels |
| Conditions | 1200–1900 rad/s, 1–3 Nm | 1400 and 2000 rad/s, 0.5/1.0/1.5 Nm |
| Regimes | Steady, velocity transient (10 000 rad/s²), load transient (50 Nm/s) | With and without mitigation |
| Signals | dq currents/voltages, fault current, torque, sin/cos θe, ωe | + electrical power in/out, resistive losses, severity estimates |
| Extras | Simulink models (.slx), continuous + discrete-time, forward Euler | .mlx live scripts, PDF reports |
| Size | 144.6 MB (6.2 GB total) | 601 MB (4.8 GB total) |

Machine parameters (15233529): Rs 727 mΩ, Rc 362 mΩ, Ld 3.29 mH, Lq 3.12 mH,
L0 2.74 mH, λpm,1 18.4 mWb, λpm,3 200 µWb, np 1, ns 6, 6 segments × 25 turns per phase.

**Strengths.** The severity × short-circuit-resistance grid in 15233529 is unique —
fault current depends on the combination of x_f and R_f, so their separate
identifiability is a genuine open question and this is the only dataset found that is
built to interrogate it. Transients present in a drive-controlled context. Signals are
control-structure only, no extra hardware — the industrial framing TIA prefers.
Shipping the Simulink models allows matched synthetic data and direct model-vs-measurement
comparison.

**Problems.**

1. **Still ITSC.** Does not resolve the overlap with the TIA paper under review.
2. **The incumbents own this ground and will likely review any submission.** Zezula
   et al. have TIE 2024 (diagnostics), TIE Jan 2026 (IPMSM discrete-time modeling),
   IECON 2024 (online SC current monitoring), plus the mitigation work — detection,
   location, severity estimation, transient operation, embedded implementation and
   mitigation are all done.
3. **An ML approach would be a downgrade.** Their model-based method detects in 3 ms
   and resolves location and severity within 6 ms of detection, on one AURIX TC277 core
   at 55–88% load in single precision. A learned classifier needing windowed transforms
   and a network forward pass would be slower, heavier and no more accurate.
4. **Known rig artifacts.** Segment-linking resistance reaches 11.8 mΩ (9.7% of segment
   resistance), which the paper states is unlike industrial motors; the fault insertion
   unit adds L_wire = 3.81 µH, disproportionately distorting low shorted-turn counts.
   Not clean ground truth.

**The opening — machine-side physics, not estimation.** The Brno group is a control and
estimation group; their model is a lumped circuit model parameterised by winding-topology
constants (np, ns, x_f, λpm,1, λpm,3) with no link back to the electromagnetic design.
Open questions that FEA can answer and their open data can validate:

- **Does x_f actually equal shorted-turns / total-turns?** The model assumes so, but
  flux linked by shorted turns depends on radial position in the slot, where leakage
  varies strongly.
- **Saturation under fault.** Ld and Lq are estimated by locked-rotor test averaged
  across current levels. Local saturation around the shorted coil changes effective
  inductances non-uniformly — invisible to the lumped model, visible in FEA. The
  1–3 Nm range and 4 R_sc levels give the operating spread to test it.
- **The np > 1 edge they flagged themselves.** The motor has 6 individually accessible
  coil segments allowing various series-parallel configurations, but validation used only
  np = 1, ns = 6 — and the paper states that non-negligible segment-linking resistance
  violates the model assumption when np > 1. An acknowledged open gap, and parallel-branch
  machines are in scope for LUT.

**Check before committing:** 21717722 was published 31 July 2026 and its companion
mitigation paper is not clearly indexed. Establish what it claims before building on it.

### Final ranked assessment (all repositories, TIA-odds criterion)

Constraint updated: **ITSC as a topic is fine** — only dataset reuse across independent
papers is excluded. MitDev-Eletrica remains out; everything else is back in play.
Extended sweep covered induction machines, SynRM and DFIG/wound-rotor in addition to PM
machines. Note: a conference→journal extension properly reuses its own dataset; the
no-reuse rule applies to independent papers only.

| Rank | Dataset | Machine | Assessment |
|---|---|---|---|
| **1** | **Brno pair** — Zenodo 15233529 + 21717722 | 253 W IPMSM, concentrated winding | Only severity × R_sc grid available; transients; TIE-published baselines; FEA angle orthogonal to incumbents; 21717722 adds mitigation on/off axis |
| **2** | **Korean industrial fleet** — Mendeley 10.17632/9r82jppsn7.1 (2025) | 4 induction motors, 1/3/5/7.5 HP (Hyundai Electric) | ITSC 10/40/60% + winding, misalignment, bearing faults; VFD with randomized ±4%/±16% speed; loads 0–90%; current @ 100 kHz, vibration/torque @ 25.6 kHz; CC BY. Fresh, unsaturated; cross-power-rating transfer is an open axis |
| **3** | **BRB database** — IEEE DataPort (open access) | 1 hp IM, 34-bar cage | 1–4 broken bars × 8 load levels × 10 reps; 3V + 3I + 5 vibration; elec. 50 kHz, vib. 7.6 kHz. Classic IAS lineage but heavily mined; line-fed; drilled bars |
| 4 | Mendeley 3-PMSM (rgn5brrgrn) | 1.0/1.5/3.0 kW PMSM | Single operating point — support role only |

**Closed after search:** SynRM — no public experimental dataset exists (2.2 kW rig work
published, data not released); DFIG/wound-rotor — no public dataset; 0.2 kW SciData
2025 set (figshare 27216219) — trivial faults (phase removal, misalignment), not TIA
material.

### Decision: Brno pair primary, FEA methodology

The winning combination on the data + methodology test:

- **Physics, not ML.** FEA-based interrogation of the lumped ITSC model: does
  x_f = shorted/total turns hold when slot leakage varies with turn position; how does
  local saturation around the shorted coil move Ld, Lq across 1–3 Nm; does the severity
  indicator survive np > 1 (the gap Zezula et al. explicitly left open).
- **Their measurements are the validation set** — experimental anchor without rig
  dependency; dataset authors tend to review favorably work that builds on their data
  rather than competing with their algorithms.
- **Risk to state openly:** full lamination geometry unpublished. Build a
  representative FEA model matched to the published structure (6 segments × 25 turns,
  21 pole pairs) and calibrate to the measured parameter table (Rs 727 mΩ, Ld 3.29 mH,
  Lq 3.12 mH, λpm,1 18.4 mWb, λpm,3 200 µWb).

**Strategic alternative (#2)** if the methodology is to stay ML: cross-rating ITSC
transfer (train 1 HP → test 7.5 HP) under randomized VFD speeds. Open question, fresh
data, induction machines (continuity with the 2021 eccentricity paper, clear of all
three PMSM papers). On the Brno data an ML method would be a downgrade against the
3 ms embedded model-based baseline; on the Korean fleet ML is the natural tool.

### Ruled out

- **WT ITSC benchmark**, Zenodo 11511321 — **simulated** (MATLAB/Simulink wind turbine
  example), 75 scenarios, fault ratios {0.05, 0.1, 0.2, 0.3, 0.5}, 4 kHz. Simulation-only
  data invites the "no experimental validation" rejection at TIA.
- **MitDev-Eletrica PMSG**, Zenodo 15741561 — in use by the paper under review.

### Earlier sweep (retained for reference)

Selected after sweeping IEEE DataPort, Zenodo, Mendeley Data, Kaggle, PMC / Data in
Brief, the OpenWindSCADA index (26 datasets), awesome-industrial-datasets, and the
university repositories (Paderborn KAt, CWRU, NASA/FEMTO, XJTU-SY).

#### PMSG condition-monitoring benchmark — UNAVAILABLE (in use by paper under review)

Zenodo 10.5281/zenodo.15741561 · https://github.com/InnovaPower/MitDev-Eletrica
CC BY · ~1.2 GB · 225 `.mat` files

| Property | Value |
|---|---|
| Machine | PMSG, Equacional, 2.5 kVA, 230 V, 4-pole, three-phase double-star (YY), 24 winding derivations |
| Faults | Inter-turn and inter-winding short circuits, 2.6 Ω, 24 fault cases + healthy |
| Operating points | 3 speeds (1200/1500/1800 rpm) × 3 torques (5.2/6.4/8.0 Nm) |
| Signals | 32 variables — abc currents/voltages, dq components, converter signals, DC-link voltage, controller outputs, torque, speed, encoder position, fault relay status |
| Sampling | 20 kHz; 3 s per record |

Chosen because:

1. It is a **generator**, and its operating points were scaled to reflect typical points
   of a 15 MW offshore wind turbine (the machine itself is a 2.5 kVA lab unit).
   Directly in the PMSG / offshore WECS line.
2. The **double-star YY** winding connects to the IECON 2021 dual three-phase PMSM
   ITSC fault-tolerant control work — an existing theoretical companion.
3. It captures **fault inception**, not only steady faulted state: each record covers
   pre-fault → 400 ms insertion → steady faulted → removal. Nearly all published ITSC
   diagnosis uses steady-state data. This enables a **detection-latency** contribution,
   where FEA explains the transient signature — the physics-informed edge a pure-ML
   group cannot replicate.
4. Converter and controller signals make it a **drive-systems** paper, reaching TIA's
   Industrial Drives Committee as well as RSECS.

#### Three-PMSM stator fault dataset (see Alternative above)

Mendeley 10.17632/rgn5brrgrn.5 · https://data.mendeley.com/datasets/rgn5brrgrn/5 · CC BY

Three PMSMs (1.0 / 1.5 / 3.0 kW, 4-pole, 3000 rpm, Higen). Inter-turn and inter-coil
short circuits, 8 severity levels each (to 21.69% and 37.66% fault ratio). Current at
100 kHz, vibration at 25.6 kHz. Single operating condition (3000 rpm, 1.5 Nm).

**The two are complementary:** PMSG gives cross-*condition* generalization (9 operating
points, one machine); Mendeley gives cross-*machine* generalization (three ratings, one
condition). Both CC BY, no subscription — fully reproducible.

### Optional

| Dataset | Role | Caveat |
|---|---|---|
| PMSM ITSC, IEEE DataPort (12 torque-speed × 9 severities × 3 SC resistances) | Richest grid | 67 GB; **requires a DataPort subscription** — check LUT access. Paywalled data weakens reproducibility with reviewers. |
| Paderborn KAt (425 W PMSM, 64 kHz current + vibration, 32 states) | Cross-fault-type check | **CC BY-NC** — academic use only |

### Rejected

- **All wind SCADA datasets** (Kelmarsh, Penmanshiel, Ørsted Anholt and Westermost
  Rough, CARE to Compare, EDP, Hill of Towie): 10-minute averaged data cannot resolve
  electrical fault signatures. They support system-level anomaly detection — a pure
  data-science problem where machine-design expertise gives no edge.
- **Zenodo 13974503** (inverter-driven PMSM): 10 Hz sampling, 1.4 MB, derived features
  rather than raw signals. Unusable for fault physics.
- **CWRU / NASA / FEMTO / XJTU-SY**: bearing vibration only, no electrical content,
  heavily saturated in the literature.

## 4. Work split

Structure the TIA paper first, then carve the conference paper out of it.

| | EPEi (6 pp) | TIA extension |
|---|---|---|
| Data | PMSG benchmark, subset of operating points | + all 9 operating points, + Mendeley cross-machine, + **own-rig measurement** |
| Task | Fault **detection** — ITSC vs. healthy | Severity **estimation** and fault-type discrimination (inter-turn vs. inter-winding) |
| Regime | Steady-state faulted operation | **Fault inception transient** — detection latency in electrical periods |
| FEA role | Signature explanation for one case | Full physics-informed feature justification across conditions |
| Baselines | 2 classical (MCSA/FFT + shallow classifier) | Full ablation, repeated runs, significance testing |
| Extra axis | — | Real-time / embedded inference cost and latency |

Estimated new content in the journal version: 60%+, well clear of the 20% floor.

## 5. Risks

- **Public-data-only validation is weak for TIA.** It is an industry applications
  transaction; reviewers expect hardware. Public datasets establish generality, the
  rig measurement establishes reality. Book rig time in advance, not in November.
- **Three-way novelty split.** The TIA paper must be distinct from *Machines* 2026
  (FEA + deep transfer learning, PM faults) and IET Power Electronics 2026 (hybrid ML,
  multi-fault PMSM drives), not only from the EPEi paper. Sim-to-real domain adaptation
  with severity regression clears this; a generic ML classifier on PMSM data does not.
- **Late submission.** The full-paper deadline passed on 18 July 2026. Unconfirmed.
- **Invitation is not guaranteed** even with an accepted paper.

## 6. Immediate action

Email the EPEi chairs (https://www.epe.tuiasi.ro/contact/) with both questions:

1. Are late full papers still being assigned reviewers via CMT?
2. How does EPEi handle IAS post-conference invitations to submit an extended
   version to IEEE Transactions on Industry Applications?

The second question also signals the paper is being written for the invited tier.

## 7. Timeline

| When | What |
|---|---|
| Now | Email chairs; begin drafting; request rig time for the journal measurements |
| By 31 Aug | Submit to CMT if late submission is accepted |
| 30 Sep | Camera-ready + registration |
| 22–24 Oct | Present at EPEi |
| ~Late Nov | TIA submission due, if invited (~4 weeks from invitation) |
| Nov 26 – Jan 27 | Journal work: severity regression, cross-dataset transfer, rig validation |

## Sources

- EPEi 2026 — https://www.epe.tuiasi.ro/ , /authors/ , /conference/
- IAS conference schedule — https://ias.ieee.org/conferences/conference-schedule/
- IAS Information for Authors of Transactions and Magazine Papers
- IEEE DataPort — https://ieee-dataport.org/documents/three-phase-pmsm-itsc-faults-stator-winding-dataset
