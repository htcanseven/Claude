# HANDOVER — Conference/Journal Paper Project

**Read this first.** This document transfers a completed planning session (claude.ai/code
web, Aug 2026) to a local Claude Code session on the researcher's own computer. It is
self-contained: everything decided, derived, and built so far is summarized here, with
pointers to the repo files that carry the details.

---

## 1. Who and what

- **Researcher:** Hüseyin Canseven, post-doctoral researcher, LUT University (Finland).
  Electrical machines: PMSM design, FEA, high-specific-power machines, fault diagnosis.
  Relevant prior work: TIA 2022 & 2024 papers (via APEC/ICEM invited route), IECON 2021
  dual three-phase PMSM ITSC fault-tolerant control, *Machines* 2026 (FEA + deep
  transfer learning, PM faults), IET Power Electronics 2026 (hybrid ML, PMSM
  multi-fault), and **one TIA paper currently under review** that uses the
  MitDev-Eletrica PMSG dataset (Zenodo 15741561) — that dataset is therefore OFF LIMITS.

- **Goal:** a 4–6 page conference paper for **EPEi 2026** (Iași, Romania, 22–24 Oct 2026),
  written deliberately as the seed of an invited extension to **IEEE Transactions on
  Industry Applications (TIA)**.

- **Local environment:** researcher's own computer with **ANSYS Maxwell** and
  **MATLAB (needs ≥ R2024b for the dataset's Simulink models)**. The cloud session could
  not touch these; the local session can — that is why the work moved here.

## 2. Venue facts (verified from the conference site)

| Item | Value |
|---|---|
| Conference | EPEi 2026, 14th IEEE Int. Conf. & Expo on Electrical and Power Engineering |
| **Full-paper deadline** | **18 July 2026 — ALREADY PASSED.** CMT portal still open. **Nobody has emailed the chairs yet — this is the gating action.** |
| Notification | 31 Aug 2026 |
| Camera-ready + registration | 30 Sep 2026 |
| Format | IEEE template, 4–6 pages (shorter auto-rejected), CMT: cmt3.research.microsoft.com/EPEi2026/ |
| AI disclosure | Mandatory — declare which sections used generative AI and which tool |
| Indexing | IEEE Xplore + Web of Science |
| IAS status | **Co-sponsored** by IEEE IAS (same tier as ECCE/APEC/IEMDC) → eligible for post-conference TIA invitation. Invitations are capped and issued by the organizers to strong papers — write for the invited slice. TIA version: presented ≤12 months prior, ≥20% changed, cites the conference paper, ~4-week window after invitation. |
| Fallbacks if chairs say no | RTUCON 2026 (Riga, 29–31 Oct, IAS Co-sponsored), IEMDC 2027, IAS Annual Meeting. Nothing in this plan is EPEi-specific. |

## 3. The chosen dataset (verified live, downloaded, inspected)

**Brno CEITEC pair** (Zezula, Kozovský, Buchta, Blaha — Brno University of Technology):

- **Zenodo 10.5281/zenodo.15233529** (144.6 MB) — companion to Zezula et al., IEEE TIE
  73(1) Jan 2026, "Discrete-Time Modeling of Interturn Short Circuits in Interior
  PMSMs". Contains:
  - `Models/` — 3 Simulink models (R2024b, all native blocks, no protection):
    `models_comparison.slx` (continuous + derived DTM + forward-Euler side by side,
    fault subsystems cleanly isolated), `codegen_mod_new.slx`, `codegen_mod_eul.slx`.
  - `Data_diverse_FI/` — Rsc sweeps {442, 47.0, 5.62, 1.74} mΩ (+14.4 mΩ wire) at
    1900 rad/s for {3,6} shorted turns × {1,3} Nm.
  - `Data_diverse_OC/` — steady state (1400 rad/s, 1 Nm), velocity transient
    (1200→1600 rad/s @ 10⁴ rad/s²), load transient (1→3 Nm @ 50 Nm/s), all 10/25 turns.
  - **Critical property:** every .mat contains measured signals AND both models'
    predictions, time-aligned (`idq/if/Te` × `meas/new/eul`, plus `udq, we, SinCos,
    Rsc, sgm`) — so model-vs-measurement residuals are computable with zero simulation.
  - .mat files are MATLAB `timeseries` objects (MCOS) — unreadable by scipy; export via
    `matlab/export_brno_data.m` (in this repo) first.
- **Zenodo 10.5281/zenodo.21717722** (601 MB) — mitigation on/off datasets, severities
  {3,6,9}/25, speeds {1400, 2000} rad/s, loads {0.5, 1.0, 1.5} Nm. **Not yet downloaded
  or inspected.** Companion mitigation paper not yet found indexed — read the PDF
  reports inside the zip before using.

**Benchmark machine** (TIE 2026 Tables I–II): IPMSM, concentrated winding, 42 poles
(PP=21), np=1, ns=6 coil segments × 25 turns per phase (150 turns/phase), Rs 727 mΩ,
Rc 362 mΩ, Ld 3.29 mH, Lq 3.12 mH, L0 2.74 mH, λpm,1 18.4 mWb, λpm,3 200 µWb.
Nominal: 6.89 A, 3.78 Nm, 638 rpm, 253 W, max 3500 rpm. FIU parasitic: Rwire 14.4 mΩ,
**Lwire 3.81 µH (scales as ns/r — confounds low turn counts; must be separated in the
analysis)**. Known rig artifact: segment-linking resistance up to 11.8 mΩ.

## 4. The paper idea (full version: `conference-paper-idea.md`)

State-of-the-art model-based ISC diagnostics (the Brno TIE papers: 3 ms detection on
one AURIX core) define fault severity as x_f = shorted turns / total turns — a turn
COUNT. That assumes all turns are electromagnetically identical. They are not: slot
leakage links turns very unevenly (flux crossing the slot at height h links only
conductors below h), so the electromagnetic size of a "3-turn fault" depends on WHICH
turns are shorted.

**Three steps:**
1. **Residual analysis (no FEA):** from the shipped data, compute if_meas − if_new
   across the 2 severities × 2 loads × 4 Rsc grid → the state of the art's unexplained
   error. Days of work.
2. **FEA explanation (the contribution):** turn-level Maxwell model → effective severity
   x_f,eff and fault-loop inductance L_f vs turn position.
3. **Close the loop:** inject corrected parameters into the authors' own Simulink model,
   re-run against their own measurements, show the residual shrink. That figure is the
   paper.

**Physics support (derived, in `fea-model-notes.md`):** L0 = 2.74 mH vs
(Ld+Lq)/2 = 3.21 mH ⇒ **~85% of this machine's inductance is leakage** (42-pole
tooth-coil ⇒ weak magnetizing path). Turn position enters through L_f, and this machine
is leakage-dominated — best possible case for the effect. EMF per turn is roughly
position-independent (all turns encircle the same tooth); it is the INDUCTANCE that
carries the effect.

**Falsifiable gate (run before any FEA):** fault current is resistance-limited at high
Rsc, inductance-limited at low Rsc. The 442→1.74 mΩ sweep crosses that transition.
**If L_f carries a position error, the residual must GROW as Rsc falls.** Flat residual
⇒ hypothesis dead, pivot (saturation angle: 1 vs 3 Nm residual difference) or drop.

**Quantitative preview (synthetic slot-leakage model, `fea/lf_from_matrix.py`, tested):**
- Orderly-wound coil, r=3: L_f ranges 0.13×–2.76× the turn-ratio value (22× spread).
- Random-wound coil: unbiased on average (median k≈1.1) but irreducible ±2× spread for
  r=3, narrowing to ±40% at r=10.
- **Fork in the paper:** orderly winding ⇒ deterministic correction paper; random-wound
  ⇒ "fundamental precision limit of severity estimation" paper (arguably stronger, and
  robust to geometry uncertainty). Determine which from Fig. 3 of TIE 2026 / the
  terminal-box tap arrangement; if indeterminate, report both bounds.

## 5. FEA plan (full version: `fea-model-notes.md`, script: `fea/build_maxwell_model.py`)

- **Method:** assign each of the 25 turns of one coil as a separate winding in a
  **magnetostatic** solution; request the 25×25 inductance matrix; **solve once**.
  L_f of any shorted set S = Σᵢⱼ∈S L_ij (superposition; exact in the linear regime).
  `fea/lf_from_matrix.py` (tested — validates against the textbook N²h/3w slot
  permeance to 0.1%) does all post-processing: swap `synthetic_slot_matrix()` for
  `load_maxwell_matrix('turn_matrix.csv')`.
- **Two designs:** (a) calibration = 60° sector, ANTI-periodic boundary (GCD(36,42)=6,
  7 poles/sector = odd), to match λpm/Ld/Lq/L0 — weight **L0 most** (it is the leakage
  handle); (b) fault matrix = **full 360°** (single-turn excitation breaks sector
  symmetry — periodic boundaries invalid there).
- **Inferred geometry** (NOT published — confirm slot count against TIE 2026 Fig. 3):
  36s/42p single-layer tooth-coil (ns=6 ⇒ 18 coils ⇒ 36 slots; 6s/7p base unit).
  Sizing from λpm: D_bore·L_stk ≈ 3.1e-3 m² → suggested 110 mm bore / 30 mm stack.
  Starting slot: depth 14 mm, width 4.4 mm, opening 2 mm. Magnets: interior, tune depth/
  bridge for Ld/Lq ≈ 1.05.
- **Demagnetize magnets (Br=0) for inductance extraction** (or frozen permeability).
  Saturation study (1 vs 3 Nm axis) = separate frozen-permeability runs — that is the
  journal extension's axis, keep it out of the conference critical path.
- `fea/build_maxwell_model.py` is a **PyAEDT skeleton — UNTESTED** (written without
  AEDT access). Geometry construction is a commented sequence, not working code. First
  local task: `pip install ansys-aedt-core`, verify against the installed AEDT version,
  fill in the geometry steps.

## 6. Repo map

| File | Status |
|---|---|
| `epei-2026-plan.md` | Venue facts, TIA route, full dataset search log (what was ranked, rejected, and why — incl. eliminated: MitDev-Eletrica = in use; Korean Mendeley fleet = data removed; SynRM/DFIG = no public data; SCADA = wrong resolution) |
| `tia-paper-structure.md` | Journal paper: contributions C1–C5, section skeleton, figure/table plan, experiment matrix, risks, timeline, EPEi carve-out (§10) |
| `conference-paper-idea.md` | Plain-language explanation of the paper idea |
| `fea-model-notes.md` | Leakage-dominance derivation, falsifiable gate, geometry inference, calibration targets, build procedure |
| `fea/lf_from_matrix.py` | **Tested.** Submatrix-sum L_f method + synthetic slot model + random-wound Monte Carlo |
| `fea/build_maxwell_model.py` | **Untested** PyAEDT skeleton |
| `matlab/export_brno_data.m` | One-time .mat (timeseries) → CSV exporter; ready to run |

Branch: `claude/conference-paper-plan-yg504k` on github.com/htcanseven/Claude.

## 7. Next actions, in order

1. **Email the EPEi chairs** (epe.tuiasi.ro/contact/): (a) are late full papers still
   being reviewed via CMT? (b) how does EPEi handle IAS post-conference TIA
   invitations? Everything else proceeds in parallel, but this decides the venue.
2. **Download Zenodo 15233529**, run `matlab/export_brno_data.m` in MATLAB → CSVs.
3. **The gate:** residual analysis, especially residual vs Rsc from the
   `Rsc_changes_*` files (script does not exist yet — write it: align if_meas vs
   if_new, compute amplitude/phase residuals per Rsc step, check growth as Rsc falls;
   subtract the Lwire = 3.81 µH contribution before attributing anything to turn
   position). Also check the 1 vs 3 Nm difference (saturation backup axis).
4. **Confirm the winding** (orderly vs random-wound; slot count) from TIE 2026 Fig. 3 —
   decides which paper (correction vs precision-limit) gets written.
5. **Maxwell:** verify/complete `fea/build_maxwell_model.py`, calibrate the sector
   model to the five targets, run the full-360° turn-matrix solve, export 25×25 CSV,
   run `lf_from_matrix.py` on it.
6. **Write** the 6-pager per `tia-paper-structure.md` §10 (IEEE template + mandatory AI
   disclosure + cite both Zenodo DOIs and both TIE papers). Target: submitted by
   ~31 Aug if the chairs say yes.
7. Later, for the journal: download/inspect 21717722, read its PDF reports.

## 8. Standing constraints

- MitDev-Eletrica (Zenodo 15741561) must not be used — under-review TIA paper uses it.
- Same-topic ITSC is fine; same-dataset across independent papers is not.
  (Conference → journal extension reusing its own dataset is normal and expected.)
- The paper calibrates/extends the Brno model — never competes with their estimator
  (their 3 ms embedded baseline beats any ML replacement; they are likely reviewers).
- Model identity, AI tools etc. must not appear in commits/PRs; EPEi requires an AI
  disclosure section in the manuscript itself.
