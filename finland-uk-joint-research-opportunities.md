# Finland–UK Joint Research Programme — Deep Research Report

**For:** Dr. Hüseyin T. Canseven (LUT University, Finland) & Dr. Nur Sarma (Durham University, UK)
**Date of research:** 27 July 2026. All deadlines, budgets and eligibility rules were verified against official sources on this date; items that could not be fully confirmed are marked **UNVERIFIED**. Re-check every deadline on the official page before committing effort.

---

## 1. Executive summary

Your two profiles are almost perfectly complementary — machine design, thermal management and fault-tolerant drives (LUT) meets condition monitoring, fiber-optic sensing and diagnostics (Durham) — and you already have a joint publication (June 2026, *Machines*) on exactly the convergence topic: **fault detection in offshore direct-drive permanent-magnet wind generators**. That is the natural flagship theme, with a second theme (embedded fiber-optic sensing for thermally-pushed machines) as a fast personal-fellowship vehicle.

A detailed topic-by-topic reading of the Horizon Europe Cluster 5 Work Programme 2026-2027 is in the companion document [`horizon-cluster5-wp2026-2027-analysis.md`](./horizon-cluster5-wp2026-2027-analysis.md).

The five highest-value moves, in order of deadline:

| # | Action | Deadline | Instrument | Money |
|---|--------|----------|------------|-------|
| 1 | Hüseyin applies for an **MSCA Postdoctoral Fellowship** hosted at Durham (supervisor: Nur) | **9 Sep 2026** | HORIZON-MSCA-2026-PF-01 | ~€230k, 12–24 months |
| 2 | Parallel/backup: Hüseyin applies to the **Foundations' Post Doc Pool** (autumn call) for a Durham research period | **15 Aug – 15 Sep 2026** | Säätiöiden post doc -pooli | ~€30–60k, 6–24 months |
| 3 | Both **join COST Action CA25138 "SAFEWIND"** (offshore wind, starts 18 Sep 2026) and CA23155 "OTC" WG4 (condition monitoring) | join anytime, from Sep 2026 | COST | funded travel, STSMs, training schools |
| 4 | LUT-side 4-year grant: **Research Council of Finland winter call** — Academy Project (senior PI) and/or Academy Research Fellowship (Hüseyin, if PhD window fits), with Durham as international partner | **14 Oct – 11 Nov 2026** | RCF, funding starts Sep 2027 | €600k–700k / 4 yrs |
| 5 | Durham-side grant: **EPSRC standard responsive-mode grant** led by Nur with LUT as project partner + funded researcher visits | anytime | EPSRC responsive mode | no limit, 80% FEC |

Structural finding that shapes everything: **no bilateral Finland–UK funding instrument exists** (no RCF–UKRI lead-agency or money-follows-cooperation agreement; EPSRC does not fund Finnish co-investigators; UKRI's ISPF excludes Finland; Innovate UK has no Eureka Network Projects budget). The proven model for a Finland–UK pair is therefore: **(a)** personal mobility funding to embed the collaboration, **(b)** *parallel* national grants written around a shared work plan, and **(c)** EU instruments — where the UK is a fully associated Horizon Europe country through the 2027 calls, so LUT+Durham can sit in the same consortium as equals.

---

## 2. Why this collaboration works

### 2.1 Complementarity map

| Dimension | Hüseyin T. Canseven (LUT) | Nur Sarma (Durham) | Joint edge |
|---|---|---|---|
| Machine design | PMSM/PMSG electromagnetic design; high-specific-power machines; tooth-coil/modular topologies; dual-port PMSG with reduced converter size | — | **Design-for-reliability**: fault behaviour engineered at the design stage |
| Thermal | Direct liquid cooling; hairpin windings | — | Hotspot-critical designs that *need* embedded sensing |
| Sensing | — | Fiber-optic FBG sensing (strain, thermal) of electric machines; sensorless estimation | Embed FBG into hairpin/liquid-cooled machines at design time |
| Diagnostics | ML fault detection (decision trees, hybrid ML, deep transfer learning); PM demagnetization, eccentricity | Wide-band controller-signal diagnostics; DFIG stator/rotor fault detection; spectral methods | **Physics-informed ML**: design models generate fault signatures, monitoring validates them |
| Fault tolerance | Dual three-phase and five-phase PMSM fault-tolerant control | Fault detection triggers | Closed loop: detect → reconfigure → **"self-healing drivetrain"** |
| Systems | MW-class drive design; switching-frequency trade-offs; direct-grid PMSG | Power system modelling; interharmonics; load forecasting | Grid-side signatures of machine faults; drivetrain–grid interaction |
| Reliability engineering | — | Wind fleet failure-mode and downtime analysis | Field-data-driven prioritisation of which faults matter |
| Test capability | LUT machine prototyping & drives labs (30+ yrs of machine testing; WBG converters; thermal/cooling) | Durham wind turbine condition-monitoring test rig (~30 kW instrumented DFIG drivetrain); Tavner/Crabtree CM lineage | Two-site validation: prototype in Lappeenranta, monitor/diagnose in Durham |

### 2.2 You are not starting cold

- **Joint paper already published:** Canseven, Ercire, Cömert, Ünsal, **Sarma**, "Advanced Fault Detection of Permanent Magnet Faults in Offshore Wind Turbine Generators Using Finite Element Analysis and Deep Transfer Learning," *Machines* 2026, 14(6), 665 ([doi:10.3390/machines14060665](https://www.mdpi.com/2075-1702/14/6/665)) — FEA-generated fault signatures on the IEA 15 MW reference direct-drive PMSG, classified by deep transfer learning. In proposals, present the partnership as an **established, productive collaboration** — this materially strengthens MSCA, RCF and consortium bids. (One exception: the Royal Society International Exchanges scheme funds *new* collaborations only — see §4.1.)
- **Institutional hinterland, Durham:** one of the historic homes of wind turbine condition monitoring (Prof. Peter Tavner → Prof. Christopher Crabtree lineage); Durham Energy Institute wind theme; strategic partnership with Ørsted; member of the Aura cluster (with Siemens Gamesa, ORE Catapult, Hull, Sheffield); 2024 MoU with **ORE Catapult, Blyth (~40 km away), which operates 15 MW-class powertrain test facilities**; Nur supervises in the Aura CDT (EPSRC offshore wind doctoral training centre).
- **Institutional hinterland, LUT:** the Pyrhönen school of PM machine design; Laboratory of Electrical Drives Technology (high-fundamental-frequency WBG converters, machine-integrated power electronics, cooling of high-specific-power machines); and **Yaskawa Environmental Energy / The Switch in Lappeenranta** — serial manufacturer of MW-class offshore PM generators with an **18 MW drivetrain test bench** and an established LUT cooperation. Between The Switch and ORE Catapult, the pair sits next to two of Europe's largest drivetrain test facilities.
- **Market/policy tailwind (use in every motivation section):** UK offshore wind: ~16.1 GW operational, ~11.5 GW under construction, and a record **8.4 GW awarded in CfD Allocation Round 7 (Jan 2026)**. Finland: Tahkoluoto (world pioneer of icing-condition offshore wind) plus its ~600–840 MW extension, Vattenfall's ~1.3 GW Korsnäs project, and **Energiavirasto's first EEZ offshore auctions running in 2026** (four areas in the Gulf of Bothnia). Both states need exactly what you do: reliable, maintainable MW-scale PM drivetrains — Finland with the extra niche of **icing/cold-climate operation**.

---

## 3. What to propose: four project concepts

Each concept below is sized to a specific funding vehicle. They share one storyline, so work on any of them reinforces the others.

### Concept 1 — flagship: "Self-aware, fault-tolerant PM drivetrains for 15–25 MW offshore wind"

Offshore turbines have reached 15–25 MW with direct-drive PMSGs; O&M is roughly a third of offshore LCOE and access is weather-limited, so undetected generator faults are disproportionately costly.

- **WP1 (LUT):** design-for-reliability of multiphase/tooth-coil PMSG; fault-signature modelling (demagnetization, inter-turn, eccentricity) directly from electromagnetic design models.
- **WP2 (Durham):** embedded FBG sensing (strain/thermal in windings) plus converter-signal wide-band diagnostics — i.e., no additional offshore hardware.
- **WP3 (joint):** physics-informed ML fusing model-based signatures with monitoring data → health index and remaining-useful-life estimation (direct continuation of your 2026 *Machines* paper).
- **WP4 (LUT):** fault-tolerant reconfiguration of the multiphase drive after detection — the "self-healing" closed loop.
- **WP5 (joint + industry):** validation — scaled prototype at LUT, monitoring campaigns on the Durham rig, pathway to The Switch (18 MW) / ORE Catapult (15 MW) benches.

**Vehicles:** the €93M Horizon Europe wind topic's **cascade-funding calls from 2027** (up to €1M per grant — ideal size, see §4.3); a future CETPartnership call with better FI/UK funder coverage; and, immediately, the *parallel* RCF Academy Project + EPSRC standard grant pair (§4.2, §4.4).

### Concept 2 — fellowship-scale: "Embedded fiber-optic sensing for thermally-pushed electric machines"

Direct-liquid-cooled and hairpin-wound machines run deliberately close to thermal limits; the binding constraint is knowing the hotspot. FBG sensors are EMI-immune, multiplexable and embeddable in slots and end-windings — but nobody co-designs them into high-specific-power machines from the start. Hüseyin has the machines and cooling; Nur has the FBG instrumentation track record. Applications run from offshore wind through aerospace-grade high-specific-power machines to EV traction.

**Vehicle:** this is the ideal **MSCA Postdoctoral Fellowship** project (Hüseyin at Durham, deadline 9 Sep 2026), with an optional non-academic placement (e.g., ORE Catapult or an OEM) bolted on. Also a natural Post Doc Pool project (§4.1).

### Concept 3 — paper-first: "Converter-embedded, sensor-minimal diagnostics for offshore PMSG"

Extend Nur's wide-band controller-signal fault-detection methods (proven on DFIG) to direct-drive PMSGs, including PM demagnetization faults from Hüseyin's models. Reduced-converter and dual-port topologies (Hüseyin's line) change fault observability from the converter — a genuinely open scientific question. **Costs nothing to start now**: simulation studies plus Durham-rig experiments, producing the joint-publication record that all the grant applications cite.

### Concept 4 — network-scale: doctoral training network on reliable electric drivetrains for the offshore energy transition

An 8–12 beneficiary **MSCA Doctoral Network** anchored by LUT + Durham (e.g., + Strathclyde, Aalborg, KU Leuven, Politecnico di Torino, NTNU, and industry: The Switch/Yaskawa, ORE Catapult, Flender/Moventas, an operator such as Ørsted or OX2). Deadline 24 Nov 2026 is tight for a first-time consortium; **23 Nov 2027** is the realistic edition, with the 2026-27 period used to assemble the partnership via the COST actions.

---

## 4. Funding landscape (verified July 2026)

### 4.1 Act now — deadlines August–September 2026

**MSCA Postdoctoral Fellowship 2026** (HORIZON-MSCA-2026-PF-01) — **deadline 9 Sep 2026, 17:00 Brussels**
- 12–24 months at Durham; optional +6-month non-academic placement. Written jointly by fellow + supervisor.
- Rates (per month): €6,350 living (× UK country coefficient) + €710 mobility + €660 family if applicable; institution receives €1,000 research/training/networking + €650 management.
- Eligibility: PhD in hand by deadline; ≤8 years FTE post-PhD research experience; **mobility rule: ≤12 months in the UK during 9 Sep 2023 – 9 Sep 2026**; one proposal per researcher; proposals scoring <80% in 2025 may not be resubmitted.
- Reality check: 2025 saw a record 17,066 proposals and ~9.6% success. Apply, but run backups in parallel. Next edition: 8 Sep 2027.
- Sources: [call news](https://marie-sklodowska-curie-actions.ec.europa.eu/node/1575), [REA PF page](https://rea.ec.europa.eu/funding-and-grants/horizon-europe-marie-sklodowska-curie-actions/msca-postdoctoral-fellowships_en), [UKRO note](https://www.ukro.ac.uk/funding-and-opportunities/msca-postdoctoral-fellowships-2026-call-now-open/).

**Foundations' Post Doc Pool, autumn call** — **15 Aug – 15 Sep 2026** ([postdocpooli.fi](https://postdocpooli.fi/en/))
- The main Finnish vehicle for postdoc research periods abroad: 6–24 months, all expenses, ~€49k average, €1.6M pot this round. A 12-month research period in Nur's group fits exactly. Check the pool's ties-to-Finland/residence criteria against Hüseyin's situation before writing.

**Royal Society International Exchanges, Global Round 3** — **opens 30 Jul 2026, deadline 24 Sep 2026, 15:00 UK**
- Up to £12,000 over 2 years for mutual visits; Durham applicant leads, LUT co-applicant needs PhD + a contract covering the **full award duration** (i.e. to ~March 2029 for a 2-year award).
- **Two caveats, both examined in detail in the companion review [`royal-society-international-exchanges-review.md`](./royal-society-international-exchanges-review.md):** (1) durations are limited to 3 months, 1 year or 2 years — **there is no 36-month option**, though a 2-year award can take a one-year *no-cost* extension; (2) the scheme funds **new collaborations only** ("Applications must be new collaborations"), and your June 2026 joint paper is a recent collaboration. Email the Grants team for a ruling before investing effort.
- Source: [scheme page](https://royalsociety.org/grants/international-exchanges/).

**COST Actions — join two immediately** (lightweight: e-COST profile + working-group application; Management Committee membership via national COST coordinators)
- **CA25138 SAFEWIND** — Secure and Adaptive Frameworks for Environmentally sustainable Offshore WIND expansion; runs **18 Sep 2026 – 17 Sep 2030**; brand new, so early joiners can take WG roles. Direct hit for you both. ([cost.eu/actions/CA25138](https://www.cost.eu/actions/CA25138/))
- **CA23155 OTC** — ocean tribology network, running to Oct 2028, whose **WG4 is "Condition monitoring & diagnostics for operational systems in ocean environments."** ([cost.eu/actions/CA23155](https://www.cost.eu/actions/CA23155/))
- COST pays for exactly what a young collaboration needs: meetings, **Short-Term Scientific Missions between LUT and Durham**, training schools. Optionally, your own COST Action proposal is possible (**Open Call collection date 28 Oct 2026**, min 7 COST countries, ≥50% Inclusiveness Target Countries, ≥40% young researchers) — high effort, consider for 2027.

**RISEnergy transnational access** — free access (including travel/subsistence for up to 2 researchers, up to ~3 months) to 120+ renewable-energy research infrastructures across Europe; **5th call expected September 2026**, then every ~6 months to Sep 2027. Check the catalogue's offshore-wind filter for drivetrain/nacelle rigs (Strathclyde's offshore labs and Chalmers' research turbine are listed; availability of multi-MW drivetrain rigs UNVERIFIED). ([risenergy-project.eu/open-calls](https://risenergy-project.eu/open-calls/))

**For awareness only (probably not actionable this round):**
- **HORIZON-CL5-2026-09-D3-03** — the single €93M wind-energy Innovation Action of the 2026-27 Work Programme, **deadline 15 Sep 2026**, one project expected. Its scope reads like your CV (O&M digitalisation with new sensor technologies; lifetime extension; floating wind including integrated design of the "generation part"). Joining the core consortium at this stage is only realistic through an invitation — worth a few emails through Durham's Ørsted/Aura/ORE Catapult channels — but the real entry point is its **mandatory cascade funding** (§4.3). A full read of the work programme text for this topic — including the cascade-funding rules that make it enterable later — is in the companion document [`horizon-cluster5-wp2026-2027-analysis.md`](./horizon-cluster5-wp2026-2027-analysis.md). ([topic page](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl5-2026-09-d3-03))
- **Eurostars Call 11, deadline 10 Sep 2026** — SME-led; only relevant if a Finnish SME/midcap leads (then LUT is funded at 80%; Durham could only join self-funded since Innovate UK funds UK SMEs only). Next call ~March 2027.

### 4.2 Autumn 2026 — the Finnish anchor grant

**Research Council of Finland winter call — open 14 Oct – 11 Nov 2026** (funding starts Sep 2027). Note: RCF's traditional "September call" no longer exists; this is the current schedule. ([aka.fi calls](https://www.aka.fi/en/research-funding/apply-for-funding/calls-for-applications/))
- **Academy Project (akatemiahanke):** up to €600k / 4 years (consortium up to €1M). International collaboration and mobility are explicitly fundable — research visits to Durham, and even hiring foreign researchers into the Finnish team. The PI must meet RCF's experience requirements (docent-level or equivalent) — so this is typically led by a senior LUT professor with Hüseyin as a core named researcher and Nur as the named international collaborator (a support letter from Durham strengthens it).
- **Academy Research Fellowship (akatemiatutkija):** ~€700k / 4 years covering own salary + team + research costs, with working periods abroad encouraged — arguably the **single best Finland-side instrument for Hüseyin**, with Durham written in as the mobility destination. Eligibility window: PhD completed roughly 2–7 years before the call year — **verify Hüseyin's PhD date against the 2026 call text as soon as it is published (24 Sep 2026)**.
- No RCF–UK bilateral scheme exists; frame the UK link as international collaboration within these national instruments.

**MSCA Doctoral Networks 2026 — deadline 24 Nov 2026** (€593M; average grant ≈ €4.5M; min 3 beneficiaries in 3 MS/AC countries, realistically 8–12 partners; UK beneficiaries fully eligible). Only attempt this round if a coordinator-experienced partner joins; otherwise target **23 Nov 2027** with the consortium built through SAFEWIND. ([call news](https://marie-sklodowska-curie-actions.ec.europa.eu/node/1591))

**Marginal but noted:** HORIZON-CL5-2026-11-D3-23 (data sharing for AI foundation models in energy; IA ~€10M; opens 4 Aug 2026, deadline 1 Dec 2026) — only if a wind-data consortium invites you.

### 4.3 2027 — the scaling year

| Instrument | Key dates | Size | Why it fits |
|---|---|---|---|
| **MSCA Staff Exchanges 2027** | opens ~15 Dec 2026, **deadline 15 Apr 2027** | €5,170 per seconded person-month, up to 360 pm | The best structural instrument for institutionalised two-way LUT↔Durham mobility. Needs ≥3 legal entities in 3 countries **including a non-academic partner** — The Switch or ORE Catapult solves both constraints at once. |
| **Cascade calls of the €93M wind project (D3-03 FSTP)** | first "breakthrough" call in the winning project's year 1 (realistically late 2027–2028); €8M, then €16M of "validation" calls | **up to €1M per third-party project, 12–18 months** | Sized exactly for a two-university team. The work programme states these calls target "research organizations, academia… entities that do[…] not necessarily have the capacity to apply directly for EU grants", anticipates one entity winning **more than one** grant, and lets the validation calls mature technology "developed previously and separately in **other European and national projects**" — i.e. a direct pipeline from your RCF/EPSRC work into EU money. Watch for the winning consortium from early 2027. |
| **EPSRC standard grant (responsive mode)** | anytime | no limit, 80% FEC | Nur leads; LUT joins as (unfunded) project partner; **visiting-researcher travel/subsistence for Hüseyin can be costed on the UK grant**. EPSRC does not fund Finnish co-investigators (only Norway via MFC), so parallel-grant architecture is the way. |
| **2ZERO: HORIZON-CL5-2027-03-D5-03** — *best-fit Cluster 5 topic for this pair* | opens 15 Dec 2026, **deadline 14 Apr 2027** | IA, **€5–7M/project, 4 projects funded** | "Data-driven circular economy for e-mobility ecosystem". The scope names "**rotors, stators of electric motors**" and "power electronic converters", and asks for "**predictive maintenance**" and monitoring of "fatigue and thermal stress" to extend component lifespan, plus reduced critical-raw-material dependency. Nur's FBG strain/thermal sensing and Hüseyin's machine design map onto it almost line by line, at a realistic project size. Route in: an automotive OEM/Tier-1-led consortium needing a monitoring/lifetime work package. |
| **2ZERO: HORIZON-CL5-2027-03-D5-05** | opens 15 Dec 2026, **deadline 14 Apr 2027** | IA, ~€8M/project, 2 projects | Post-800V modular heavy-duty-vehicle powertrain — direct fit for LUT's fault-tolerant multiphase drives + direct liquid cooling, with Durham monitoring angle; diversifies you beyond wind. |
| **HORIZON-CL5-2027-02-D3-09** (ocean energy) | opens 3 Dec 2026, **deadline 31 Mar 2027** | IA, €43M, **1 project** | Explicitly invites your expertise: "Apply recent advances in **condition and structural health monitoring from other sectors** to ocean energy." Consortium-joining only, given the single-project format. |
| **Clean Aviation Call 5** | expected early 2027 | topics TBD (~€930M WP envelope; ≥15% of funding reserved for SMEs/RTOs/universities) | Entry for the high-specific-power machine + embedded-FBG line (Concept 2 at scale). |
| **CETPartnership Joint Call 2027** | expected ~mid-2027 (pattern) | €1–5M/project | **Skip the 2026 call**: the relevant module has no UK funder (only Invest NI, wrong modules) and Business Finland requires ≥2 Finnish export companies with ≥40% of Finnish costs. Revisit in 2027 if funder coverage improves. |
| **Supergen ORE Hub Flexible Fund Call 7** | pattern suggests a July call — UNVERIFIED, watch [supergen-ore.net](https://supergen-ore.net/flexible-funding) | ~£100k, 12 months | UK-only applicants; themes (sensing/electro-mechanics; reliability; O&M) fit Nur exactly; LUT could join as unfunded partner (confirm with the hub). |
| MSCA PF 2027 / DN 2027 | 8 Sep 2027 / 23 Nov 2027 | as 2026 | Second bites at both cherries. |

### 4.4 Structural notes for planning

- **No Finland–UK bilateral instrument exists.** Confirmed absences: RCF–UKRI agreements (none), EPSRC international co-lead for Finland (not accepted; Norway/IIASA only), UKRI ISPF (Finland not covered), Innovate UK Eureka Network Projects budget (none). NordForsk's one live UK-inclusive programme (NFRF "Disruptive Technologies", with UKRI and RCF-via-NordForsk) is already past its entry gate for this round — a LUT+Durham axis fits its geometry well if it repeats.
- **UK is a full Horizon Europe associated country for every call through 2027** — Durham participates and is funded exactly like an EU beneficiary, including MSCA hosting. **FP10 (2028–34) UK association is undecided**, so treat calls with 2026-27 deadlines as the safe window and don't build plans that assume UK eligibility from 2028.
- **Visiting-fellowship options for later career stages:** Royal Society Wolfson Visiting Fellowship (up to £125k, 12-month sabbatical for overseas-based mid/senior researchers, ~2 rounds/year) — relevant either for a senior LUT colleague now or for Hüseyin later; Royal Academy of Engineering Distinguished International Associates currently closed between rounds; RAEng Research Fellowships (~£800k/5 yrs, next round ~mid-2027) if Hüseyin ever considers a UK-based early-career route.
- **Finnish foundation calls to diary for early 2027** (all closed for 2026): Tekniikan edistämissäätiö TES (Jan–Feb), Walter Ahlström Foundation (early year; under-35 rule — check), Tutkijat maailmalle (Mar–Apr; up to €50k for 6–12 months abroad), Jenny & Antti Wihuri (May; note: long foreign postdoc periods excluded — points to the Post Doc Pool instead).

---

## 5. Consortium building and networks

**Industry to approach first (in likely order of accessibility):**
1. **Yaskawa Environmental Energy / The Switch** (Lappeenranta) — MW-class offshore PM generators, 18 MW test bench, existing LUT relationship. Solves the "non-academic partner" requirement for MSCA SE/DN and anchors CETP/Eurostars-type bids.
2. **ORE Catapult** (Blyth) — 15 MW powertrain testing, 2024 MoU with Durham; natural UK validation partner and MSCA placement host.
3. **Ørsted** (Durham strategic partner) — operator data and offshore relevance.
4. **Flender / Moventas Finland** (Jyväskylä, wind gearboxes), **ABB Motion**, **Danfoss Drives** (Vaasa) — Finnish drivetrain supply chain for larger consortia.

**Academic partners for a 3rd-country leg (needed for most EU instruments):** Strathclyde (offshore labs, in RISEnergy), Aalborg, KU Leuven/EnergyVille (drivetrain testing heritage from INNTERESTING), Politecnico di Torino, NTNU, Fraunhofer IWES (DTWO digital twins).

**Competitive/adjacent EU projects worth knowing (CORDIS):** WILLOW (offshore lifetime extension via AI health monitoring — closest overlap), SUDOCO, DTWO (federated digital twins), TWINVEST, AEROSUB (robotic O&M), CIRCWIND (circularity), INNTERESTING (hybrid accelerated drivetrain testing, H2020). Their consortia are also your future partner pool.

**Networks (cheap, high-leverage):**
- **EAWE:** Durham is a member; **LUT is not** (Finland is represented by Aalto) — LUT joining is a concrete, low-cost visibility action.
- **IEA Wind TCP Task 43** (digitalisation; gearbox/drivetrain reliability work now lives here) and **Task 42** (lifetime extension) — participation runs through national representatives.
- **Aura CDT** (Nur supervises): a co-supervised PhD project between Durham and LUT is a zero-grant way to make the collaboration durable now.

**Zero-cost immediate scientific actions:** (1) follow-up paper to the *Machines* article extending detection to converter-embedded signals (Concept 3); (2) a joint review/position paper on design-integrated condition monitoring of MW PM drivetrains; (3) a jointly organised special session at the next ICEM/IEMDC edition; (4) reciprocal seminars + drafting of the shared work-package structure that all applications will reuse.

---

## 6. 24-month roadmap

```
2026
Jul–Aug   | Decide MSCA PF go/no-go (check mobility rule + PhD date) — start writing
          | Post Doc Pool application drafted (window 15 Aug – 15 Sep)
          | Email SAFEWIND proposers; apply to OTC WG4
          | (Optional) Royal Society IE eligibility query re: existing collaboration
Sep       | 9 Sep: MSCA PF submission | 15 Sep: Post Doc Pool closes
          | 18 Sep: SAFEWIND launches — attend kick-off if possible
          | RISEnergy call ~Sep: request Durham↔LUT-relevant test access
Oct–Nov   | 14 Oct–11 Nov: RCF winter call — Academy Project (senior LUT PI)
          |   ± Academy Research Fellowship (Hüseyin)
          | 28 Oct: COST own-Action deadline (only if SAFEWIND roles insufficient)
          | 24 Nov: MSCA DN 2026 (only if an experienced coordinator adopts the idea)
Dec       | MSCA SE 2027 consortium assembly (LUT + Durham + The Switch/ORE Catapult + 3rd country)

2027
Jan–Apr   | 15 Apr: MSCA SE 2027 submission
          | 14 Apr: 2ZERO D5-03 e-mobility circularity (best-fit CL5 topic) and/or D5-05 HDV powertrain
          | 31 Mar: D3-09 ocean energy (consortium-joining; CM explicitly invited)
          | EPSRC standard grant (Nur) drafted with LUT project-partner letter
          | Watch: D3-03 cascade-funding (FSTP) first call; Clean Aviation Call 5;
          |   Supergen Flexible Fund Call 7; Eurostars Call 12; foundation calls (TES, Tutkijat maailmalle)
Feb       | ~9 Feb: MSCA PF results → if funded, fellowship starts ~mid-2027
Sep–Nov   | 8 Sep: MSCA PF 2027 (backup) | RCF winter call round 2 | 23 Nov: MSCA DN 2027 (main attempt)
```

---

## 7. Personal checklists

**Hüseyin (LUT):**
- [ ] Confirm PhD award date → MSCA PF 8-year rule and RCF Research Fellowship 2–7-year window
- [ ] Confirm UK residence history 2023–2026 → MSCA mobility rule
- [ ] Check Post Doc Pool residence/ties-to-Finland criteria
- [ ] Talk to LUT professors (electrical drives) about leading an Academy Project with Durham collaboration; engage LUT research services for the Oct–Nov call
- [ ] Approach The Switch contacts about partnership letters for 2027 instruments
- [ ] Register on e-COST; apply to SAFEWIND + OTC WG4; propose LUT joins EAWE

**Nur (Durham):**
- [ ] Agree to act as MSCA PF supervisor; engage Durham's EU/research office early (internal deadlines usually ~2 weeks before the call)
- [ ] Scope an EPSRC responsive-mode proposal with LUT as project partner + costed visiting-researcher line
- [ ] Ask Supergen ORE hub about Call 7 timing and non-UK project-partner rules; watch DEI/Ørsted/Aura channels for the D3-03 consortium and its later cascade calls
- [ ] Explore an Aura CDT studentship co-supervised with LUT
- [ ] If pursuing Royal Society IE: confirm with the Royal Society whether the 2026 joint paper counts as an "existing collaboration"

---

## 8. Caveats

- All facts current as of **27 July 2026**; deadlines shift and work programmes get amended — always re-verify on the official call page before writing.
- MSCA PF success ≈ 9.6% (2025): treat it as one shot in a portfolio, never the plan.
- The Cluster 5 2027 topics and Clean Aviation Call 5 details can change until formally opened (UNVERIFIED until then); Supergen Call 7 and RAEng DIA Round 6 are pattern-based expectations, not announcements.
- CETPartnership 2026 funder lists were marked "TBC" in places; Business Finland's own call page is authoritative for the Finnish rules.
- Dr. Sarma's current grant portfolio could not be verified externally (staff page blocks automated access) — factor her existing commitments into the plan directly.
- FP10 (2028–34): UK association undecided; the €175bn Commission proposal is still in negotiation. Keep flagship EU ambitions inside the 2026–27 call window or design them UK-optional.

## 9. Key sources

- MSCA PF/SE/DN: [MSCA Work Programme 2026–2027](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-2-marie-sklodowska-curie-actions_horizon-2026-2027_en.pdf) · [PF 2026 call](https://marie-sklodowska-curie-actions.ec.europa.eu/node/1575) · [DN 2026 call](https://marie-sklodowska-curie-actions.ec.europa.eu/node/1591) · [SE 2027](https://marie-sklodowska-curie-actions.ec.europa.eu/funding/msca-staff-exchanges-2027)
- **Companion documents in this repo:** [`royal-society-international-exchanges-review.md`](./royal-society-international-exchanges-review.md) — review of the Global Round 3 scheme notes (AKB/07/2026) for this pair
- **Companion analysis in this repo:** [`horizon-cluster5-wp2026-2027-analysis.md`](./horizon-cluster5-wp2026-2027-analysis.md) — full read of the Cluster 5 work programme (Decision C(2025) 8493), topic-by-topic
- Cluster 5: [Work Programme 2026–2027 PDF](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2026-2027/wp-8-climate-energy-and-mobility_horizon-2026-2027_en.pdf) · [HORIZON-CL5-2026-09-D3-03 topic](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/topic-details/horizon-cl5-2026-09-d3-03)
- CETPartnership: [Joint Call 2026](https://cetpartnership.eu/calls/joint-call-2026/) · [call text (final)](https://cetpartnership.eu/wp-content/uploads/2026/06/CETP_Joint-Call-2026-CallText_v20260612_FINAL.pdf) · [Business Finland page](https://www.businessfinland.fi/en/services/funding/calls/2026/cetp-funding-call-2026/)
- COST: [Open Call 2026 announcement](https://www.cost.eu/uploads/2026/03/2026-1-COST_Open_Call_Announcement.pdf) · [CA25138 SAFEWIND](https://www.cost.eu/actions/CA25138/) · [CA23155 OTC](https://www.cost.eu/actions/CA23155/)
- UK: [Royal Society International Exchanges](https://royalsociety.org/grants/international-exchanges/) · [EPSRC standard grant](https://www.ukri.org/opportunity/epsrc-standard-research-grant-nov-2023-responsive-mode/) · [EPSRC international agreements](https://www.ukri.org/who-we-are/epsrc/relationships/international-agreements/) · [Supergen ORE flexible funding](https://supergen-ore.net/flexible-funding) · [Wolfson Visiting Fellowship](https://royalsociety.org/grants/royal-society-wolfson-visiting-fellowship/)
- Finland: [RCF calls](https://www.aka.fi/en/research-funding/apply-for-funding/calls-for-applications/) · [Post Doc Pool](https://postdocpooli.fi/en/) · [Tutkijat maailmalle](https://tutkijatmaailmalle.fi/apurahat/) · [Eureka/Eurostars](https://www.eurekanetwork.org/programmes-and-calls/eurostars/eurostars-call-for-projects-september-2026/)
- Infrastructure/access: [RISEnergy](https://risenergy-project.eu/) · [MARINERG-i](https://www.marinerg-i.eu/)
- Context: [joint paper, Machines 2026](https://www.mdpi.com/2075-1702/14/6/665) · [Durham–ORE Catapult MoU](https://www.durham.ac.uk/news-events/latest-news/2024/10/new-partnership-to-tackle-offshore-wind-challenges/) · [The Switch](https://theswitch.com/2021/10/18/15-years-of-permanent-performance/) · [Korsnäs](https://www.metsa.fi/en/responsible-business/wind-power/korsnas-offshore-wind-farm/) · [UK AR7 results](https://www.energy-uk.org.uk/publications/energy-uk-explains-allocation-round-7-offshore-wind-results/) · [UKRI on Horizon association](https://www.ukri.org/publications/uk-association-to-horizon-europe-and-the-uk-horizon-europe-guarantee/uk-association-to-horizon-europe-and-the-uk-horizon-europe-guarantee/)
