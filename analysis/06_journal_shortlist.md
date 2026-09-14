# Where to submit next — venue shortlist

## First, an honest framing

Scope fit was never the problem. **IEEE TEC was a good scope home for this paper** — salient-pole
synchronous generators are squarely "energy conversion," and the journal publishes rotor ITSC
diagnosis regularly (your own ref [2], Bai *et al.* 2025, is TEC). The rejection was about
contribution and validation, not about being in the wrong place.

So the question "which journal fits perfectly?" has to be answered as **"which journal fits
*which version* of this paper?"** Sending the current manuscript somewhere else, unchanged,
mostly relocates the same three objections. Three versions are realistic:

| Version | Work | What it is |
|---|---|---|
| **A** | 2–3 weeks | Presentation + reproducibility fixes only (WP1, WP2). Novelty problem intact. |
| **B** | 3–4 months | Physics-validated (WP0–WP5): measured `I_f`, Eq. (4) verified, confounding index, hardened benchmark. A genuinely different paper. |
| **C** | ~2 months + split | R1's suggestion: measurement/feature paper *and* generalisation paper, separately. |

---

## The most useful evidence: your own reference list

Your bibliography is an almost perfect venue map for this exact topic. Where comparable work
actually landed:

| Ref | Paper | Venue |
|---|---|---|
| **[4]** Ehya, Nysveen, Antonino-Daviu | **SG fault detection using stray magnetic field** | **IEEE Trans. Industrial Electronics** |
| **[6]** Bechara *et al.* | **Rotor ITSC in large hydrogenerators, stray flux + CVAE** | **IEEE Trans. Industry Applications** |
| [2] Bai *et al.* (2025) | SG rotor ITSC, leakage flux | IEEE Trans. Energy Conversion |
| [9] Cuevas, Romary, Lecointe, Jacq | SG rotor short-circuit, stray field + vibration | IEEE Trans. Magnetics |
| [17] Gurusamy *et al.* | PMSM ITSC, stray flux, localisation | IEEE Trans. Instrumentation & Measurement |
| [12] Frosini, Harlişca, Szabó | IM bearing faults, stray flux | IEEE Trans. Industrial Electronics |
| [14] Park, Choi, Lee, Gyftakis | Search-coil BRB detection | IEEE Trans. Industry Applications |
| [13] Biot-Monterde *et al.* | IM rotor failures, stray flux | Energies (MDPI) |
| [15] Irhoumah *et al.* | SM stator ITSC, two coils | Electronics (MDPI) |
| [18] Skowron *et al.* | PMSM demagnetisation, neural | IEEE Access |

The field stratifies cleanly:

- **Physics-grounded, rigorous** → TIE, TIA, TEC, TMAG
- **Sensing- and measurement-led** → TIM
- **Lighter ML applications** → Energies, Electronics, IEEE Access

**[4] and [6] are the two closest precedents to your paper that exist** — same machine class,
same fault, same sensing modality. They are in TIE and TIA. That is your answer for Version B.

---

## Ranked shortlist

Impact factors below are approximate and drawn from aggregators of varying reliability — treat
them as ballpark. (One source confidently reported TIE's acceptance rate as 100 %, which tells
you how much to trust that class of site.)

### Tier 1 — for Version B (the paper worth writing)

**1. IEEE Transactions on Industrial Electronics** — *first choice*
IF ≈ 7.4, Q1. First-revision report ≈ 69 days.
Ref [4] is literally "Advanced fault detection of synchronous generators using stray magnetic
field," published here. TIE reviewers will engage with the Eq. (4) validation and the
confounding index — that is exactly the kind of physics-plus-data contribution the journal
rewards. It will *not* accept the saturated benchmark as a contribution, so Version B only.

**2. IEEE Transactions on Industry Applications** — *strongest realistic alternative*
IF ≈ 5.4, Q1, bi-monthly.
Ref [6] is the closest precedent in the literature: rotor ITSC in hydrogenerators via stray flux
plus a learned model. TIA is somewhat more receptive to applied, laboratory-scale validation
than TIE, and more tolerant of a benchmark framing — so if you get through WP3 but not WP6
(no FEM, no new measurements), TIA is the better bet of the two.

**3. Mechanical Systems and Signal Processing** — *high risk, high reward*
IF ≈ 10.2, Q1.
Fits if you lead with the signal-processing and cross-domain-generalisation methodology rather
than the machine. MSSP is demanding about methodological rigour and would hit the saturation
problem hard — but it is precisely the venue where "here is why the benchmark had no resolving
power, and here is the protocol that restores it" is a *contribution* rather than an admission.
Only with WP4 fully done.

### Tier 2 — good fit, more achievable

**4. IEEE Transactions on Instrumentation and Measurement** — *best home for the split (Version C)*
IF ≈ 7, Q1.
R1 practically commissioned this paper: *"This topic could, in itself, constitute a separate
publication."* TIM wants exactly what R1 asked for — the measurement chain, descriptor
construction, worked examples, per-operating-point sensitivity. Ref [17] is the PMSM analogue,
published here. If you do only one thing beyond the fixes, this is the cleanest path to a
publication with a real contribution.

**5. ISA Transactions** — IF ≈ 6.6, Q1, Elsevier.
Scope explicitly names fault detection and soft sensing. Receptive to benchmark-and-method
papers with an instrumentation angle. Elsevier → OA covered by FinELib. A solid, less
competitive alternative to TIE/TIA for Version B.

**6. Measurement (Elsevier, IMEKO)** — IF ≈ 5.6, Q1.
Measurement-technique framing, similar role to TIM but a lower bar. Also FinELib-covered.

### Tier 3 — fast routes for Version A

**7. IEEE Open Journal of Industry Applications** — APC $1,950 (FinELib-funded), reportedly Q1.
IEEE-branded, fully OA, faster than TIA, same society. Reasonable if you want Version A out
with an IEEE stamp. The IF figure circulating (~7.9) is from a young journal and volatile.

**8. IEEE Access** — IF ≈ 3.4, very fast (weeks), APC funded via FinELib.
Ref [18] is here. Honest assessment: it will publish Version A, and it is a legitimate IEEE
venue, but it carries little prestige and does nothing for the novelty question. Use it only if
you need the publication banked quickly (contract, evaluation, thesis requirement).

### Not recommended right now

**IET Electric Power Applications** — IF ≈ 1.5 (Q2), fully OA at **$2,800**, *and* LUT's Wiley
free-OA quota is exhausted (see below). Low impact plus a real bill is the worst combination
here. Reconsider in 2027 if the Wiley agreement renews.

**MDPI (Energies, Machines, Sensors, Electronics)** — CHF 2,400–2,600, **not covered by any LUT
agreement**, so out of pocket. Refs [13], [15], [16] are here, so scope fit is genuine and
acceptance would be likely — but you would be paying ~€2,700 to publish a paper whose central
weakness nobody made you fix. If budget is not a constraint and speed is everything, *Machines*
or *Energies* would take Version A.

**IEEE Transactions on Magnetics** — IF has fallen to ≈ 1.9 (Q3). Ref [9] is here, and it would
suit a heavily FEM/electromagnetic version, but the impact no longer justifies it over TIE/TIA.

---

## Two practical constraints worth knowing

### LUT's open-access funding (checked against the LUT library guide)

| Publisher | Status for LUT corresponding authors |
|---|---|
| **Wiley** (incl. IET titles) | 2025–2026 agreement — but **full-OA quota ran out September 2026**, hybrid quota runs out **October 2026** |
| **Elsevier** | Covered for acceptances through **31 Dec 2026** — MSSP, ISA Trans., Measurement, EPSR all qualify |
| **IEEE** | FinELib funds APCs in IEEE hybrid and fully-OA journals |
| **Springer Nature** | Covered 2026–2027 |
| **MDPI** | **No agreement — full APC out of pocket** |

Net effect: Elsevier and IEEE are financially free to you right now; Wiley/IET is effectively not
(quota gone); MDPI costs ~€2,700. Verify current quota status with the LUT library before you
commit — these run out mid-year.

### A near-term conference worth taking seriously

**IEEE IEMDC 2027** — 17–20 May 2027, Milwaukee. **Digest deadline 1 November 2026** (~7 weeks
out). Topic list explicitly includes *"Condition Monitoring, Fault Diagnosis and Prognosis."*
Critically: papers presented at IEMDC **may be extended and submitted to TIA, TEC, TIE or TPEL**.

That makes it a genuinely good move. A digest is achievable from Version A within seven weeks,
you get expert feedback on the reframing from exactly the right audience before committing to a
journal round, and it opens a sanctioned path back into TIA or TIE later.

**IEEE SDEMPED 2027** is the single most on-topic venue in existence for this work (your ref [3]
is a SDEMPED paper). It runs biennially; the 2027 call is not yet published. Watch
<https://www.ieee-sdemped.org/> — worth targeting if the timing works.

ICEM 2026 (Funchal, 6–9 Sept 2026) and ECCE Europe 2026 have both passed.

---

## Recommendation

1. **Now:** WP1 + WP2 (presentation and reproducibility). Two to three weeks, needed for every
   route.
2. **By 1 Nov 2026:** submit an IEMDC 2027 digest. Cheap, fast, gets the reframing in front of
   the right people, and keeps the TIA/TIE door open.
3. **In parallel:** WP0 (email UFSC) and WP3 (validate Eq. (4)). This is what converts the paper
   from a benchmark into a contribution.
4. **Then choose:**
   - WP3 lands well → **IEEE TIE** (aim high; ref [4] is the precedent), fall back to **TIA**.
   - WP3 stalls or the data won't support it → split per R1 and send the measurement half to
     **IEEE TIM**.
   - You need something published quickly for external reasons → **IEEE Open Journal of Industry
     Applications** or **IEEE Access**, both APC-funded, and keep the good version for TIE/TIA.

**Do not** send the current manuscript to TIE, TIA or MSSP. All three will reject it on the same
grounds TEC did, and a second rejection on record makes the third submission harder.
