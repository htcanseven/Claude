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

Fault detection and diagnosis for PMSM drives, trained on FEA-generated data and
validated against publicly available measurement datasets.

Chosen because it is the only candidate that (a) supports public-dataset validation,
(b) has a clean severity axis to split across two papers, and (c) sits in an active
line of work.

### Datasets

Selected after sweeping IEEE DataPort, Zenodo, Mendeley Data, Kaggle, PMC / Data in
Brief, the OpenWindSCADA index (26 datasets), awesome-industrial-datasets, and the
university repositories (Paderborn KAt, CWRU, NASA/FEMTO, XJTU-SY).

### Primary — PMSG condition-monitoring benchmark

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

### Secondary — three-PMSM stator fault dataset

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
