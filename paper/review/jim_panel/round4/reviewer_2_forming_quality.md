# Referee report, fourth round: Reviewer 2

**Manuscript:** A production-referenced evaluation of design-stage decision rules in deep drawing: when can a prediction replace a physical trial?
**Journal:** Journal of Intelligent Manufacturing
**Round:** Fourth round (verification of the single-document, restyled version)
**Reviewer focus:** Sheet-metal forming practice (deep drawing, die tryout, finite-element process simulation) and quality engineering (statistical process control, process capability, measurement systems analysis)
**Date:** 25 October 2026

*Written by an AI agent acting as a fictional reviewer in a simulated review panel; it does not come from the journal or speak for any real person.*

Locations are page and margin line of `main_reviewed.pdf`. All checks were read-only pandas reads.

## 1. Summary

My round-3 points and D1–D10 survive the merge and the rewrite, and every number I checked reproduces.

The rewrite often helps, but it made two meaning slips, in the abstract and the conclusion. The merge left one file pointer wrong (the floor components) and the central simulation comparison without a named file.

Every fix fits on an existing line. The rewrite cost two pages: 31 became 33, and the declarations now end on p. 29 instead of p. 27. About 15 of the added lines are announcements and fillers, which can pay for any addition.

## 2. Regressions

| Item | Status | Where |
|---|---|---|
| My must-fix 1 (D4): three grid-wide comparisons; wall-angle trend dropped | Holds; the scope now reads as binding all three (4.1, item 3) | pp. 16–17, ll. 734–774 |
| My must-fix 2 (D8): "once runs differ by a floor"; "6 of the other 8" | Holds everywhere | p. 23, l. 1052; Table 8, ll. 1126–1127; p. 25, ll. 1142–1145; p. 28, ll. 1271–1273 |
| My optional 1: c_FR = 0.5 c_FA | Adopted | p. 10, ll. 458–459 |
| Assumed blank; blank and scale sensitivities; fitted line spacing; depth offset; extraction noise; A3; drift bound | Hold | p. 12, ll. 508–510, 548–550; p. 13, ll. 561–566; p. 16, ll. 709–719; p. 18, ll. 795–800 |
| Worked example; release as a decision on m̄ + 4σ; within-run trial | Hold | pp. 10–11, ll. 453–495; p. 23, ll. 1037–1052 |
| D1, D2, D5, D6, D7, D9, D10 | Hold | p. 21, ll. 939–942, 958–960; p. 8, ll. 339–346; p. 22, ll. 993–1012; p. 9, l. 382; Table 3; p. 14, l. 640; p. 29, l. 1314 |
| D3 | Holds in Sections 6.1 and 7; lost in the abstract (must-fix 1) | p. 24, ll. 1096–1097; p. 28, ll. 1270–1271; p. 1, l. 40 |

## 3. Support after the Online Resource was removed

**Simulation validation (old S3).**
- The levels point to `sim_validation` (p. 17, l. 775), which holds them: 11 of 42 cells; +1.84/+2.01 mm at 100 kN; 0.0111 mm at 300 kN; corner +2.59 to +3.48 mm and +1.26 to +3.31 mm; convex arms within 0.56°.
- The extraction noise points to `meas_sim` (1.82–2.32 and 2.44–9.76 floors).
- The rest of Section 5.2 reproduces, but the text names none of its files:
  - the grid-wide comparisons on which D4 rests (`sim_grid_comparisons`: 2.83–7.44; 0.894–1.000; 0.763);
  - Mc's 72 of 72 fits at 0.15 (`sim_mc_friction`, which the old S3 note named);
  - Mcd's maximum a posteriori at 0.05 in all 50 fits;
  - the oil mapping (0.77–3.13 against at most 0.091 and 0.388 mm per g/m²);
  - the depth offset (0.70–1.06 and 2.02–2.20 mm).
- The first two should be named (should-fix 1).

**Scan redundancy (old S4, upper half).** Table 3 carries the support itself. Its ranges match `meas_scan` and `meas_cut_walls`.

**Floor protocol (old S4, lower half).** Table 4 matches `panel_floor_protocol` and `meas_run_floors`, and Section 5.1's 15–33 %, 0.92–1.49 floors and 1.2–9.8 floors match `meas_floor`. The pointer for σb, σw and the drift ratio is wrong (must-fix 3).

**Trial and release (old S14).** These hold: `qual_trial` (1.35/0.90), `qual_between_run_trial` (2.10/3.55/5.10), `qual_release_capability` (3.35/10.55; 2.12–3.27/3.82–7.42) and `qual_trial_cost` (0.0171/0.0374). The nearest setting's 3.45/4.45/5.75 under τ are in `qual_between_run`, not in the file cited (should-fix 2).

**Guard bands.** `qual_guard_decision` (0.954; 0.748 of 139 decided; 0.92–1.00 per family), `qual_guard_oos` and `qual_between_run` hold.

## 4. The rewrite

### 4.1 Meaning changes and errors

**1. p. 1, l. 40.**
- "none closer than 30 floors" became "none within 30 floors".
- Mcd decides at 30.00 floors (`learn_source_floor`; Table 5), which is within 30. The abstract now contradicts Section 5.3 and loses D3's wording.
- *Fix:* restore "closer than".

**2. p. 28, ll. 1279–1282.**
- "the production record carried the decision within a family, which argues for indexing such records … rather than for a more elaborate model" became "Based on these findings, it is suggested to index production records … rather than to develop a more elaborate model".
- The within-family scope is lost: "these findings" include the cross-family one, where only simulation-based rules carried the geometry change. "Suggest … to index" is also ungrammatical.
- *Fix:* "Based on these findings, this study suggests indexing production records within a design family by their relation to the coming design rather than developing a more elaborate model; such a record is the baseline that a learned manufacturability check has to beat."

**3. pp. 16–17, ll. 734–735, 770–774.**
- "The comparisons … show it at every friction and thickness of the grid:" became "This is shown at every friction and thickness of the grid by the three comparisons … Firstly … Secondly … Thirdly".
- The qualifier holds only for the force effect. The arms bend downward in 89 % of the simulations at 100 kN, and the dome ranking is reversed in 76 %.
- The reach is inherited, but the enumeration makes each comparison read as grid-wide, which is the error my round-3 must-fix 1 corrected.
- *Fix (same length; names the file):* "Three comparisons that depend neither on the assumed blank nor on the scales of the scanner show this (`sim_grid_comparisons`). Firstly, at every friction and thickness of the grid, the simulated force effect …"

**4. p. 12, ll. 534–536.**
- A list of the documented features became "the blank is modeled by shell elements … with a scaled DP600 flow curve and constant Coulomb friction".
- This attaches friction, a contact property, to the model of the blank.
- *Fix:* "… and a scaled DP600 flow curve, and the contact uses constant Coulomb friction."

**Changes that check out.**
- "Under the same prior" (p. 22, l. 994) is correct: the values are release-like in `qual_guard_oos`.
- "200 draws of this component" (p. 24, l. 1065) is correct.
- "extrapolated verdicts" (p. 25, l. 1143) is correct.
- "Consequently" (p. 23, l. 1055) keeps the condition of l. 1052.
- The capability, PPAP, ISO 5725, MSA and forming terms are correct.

### 4.2 Clarity

Where it helps:
- definitions of P_FA, P_FR, P_T, d and s0;
- split clause chains (Sections 4.1, 4.3 and 5.1);
- enumerations;
- the prior named at l. 994.

Where it is padded, about 15 lines in all, which can pay for any addition:
- section openings (p. 5, ll. 223–225; p. 11, ll. 499–501; p. 16, ll. 693–696);
- "It should be noted that" (p. 7, l. 287; p. 12, l. 548) and "It is important to note that" (p. 18, l. 815);
- "The computational details are as follows" (p. 15, l. 679) and "According to the table" (p. 16, l. 699);
- a third statement of the floor definition (p. 28, ll. 1260–1262).

Where it is harder to follow:
- "On the other hand, … but they are safe" (p. 18, ll. 810–811), a double contrast;
- "the spread between teams of the share of wrong verdicts accepted" (p. 27, l. 1233).

## 5. Items

### Must fix

1. p. 1, l. 40: "none closer than 30 floors".
2. p. 28, ll. 1279–1282: restore the within-family scope and fix the grammar (4.1, item 2).
3. p. 7, l. 282 and the Table 4 note, p. 17, l. 750: "σb, σw and the drift ratio in `meas_floor`" is wrong.
   - The drift ratio (2.1–4.5, p. 16, l. 704) is `drift_inflation` in `sens_drift` (2.08–4.49); it is not in `meas_floor`.
   - The per-geometry σb and σw that reproduce each floor to within 12 % through Section 3.2's normal model are in `panel_floor_protocol` (old S4: σb/F 0.26–0.36, σw/F 0.46–1.39).
   - `meas_floor`'s σ_batch and five-part σ_st give only 0.52–0.86 of the floors, so they do not let the floor "be recomputed".
   - *Fix:* at l. 282, "(`panel_floor_protocol`)"; at l. 750, "σb and σw in `panel_floor_protocol`, the drift ratio in `sens_drift`". Both fit on existing short lines (ll. 292 and 750). The dictionary row should match.

### Should fix

1. Section 5.2 wording (4.1, item 3). Also add "(`sim_mc_friction`)" after "(0.15)" at p. 18, l. 783; the paragraph's last line (l. 792) has room for both changes.
2. p. 23, l. 1055: "(`qual_between_run_trial`, `qual_between_run`)".
3. The friction attribution (4.1, item 4).
4. "M5 and M7n decide only at 6.8–7.2 floors but are safe below one floor"; "the between-team spread in the share of wrong verdicts accepted".

### Optional

1. Table 3 note: "per series in `meas_scan`" (my round-3 optional 4).
2. Table 9, floor row: "(Table 4, Section 5.1)". Table 4 has no lag column.
3. p. 26, l. 1164 (this predates the rewrite): "the draw-ins" → "the mid-side draw-in". Against the force trend, the simulation does not help the corner draw-in (Table 6: 2.9 against 2.8).
4. `findings.md` still says "31 pages". If this round leads to changes, the paper should count eight simulated rounds.

## 6. Recommendation

**Accept with minor corrections.** The must-fix items can be checked against `learn_source_floor`, `sens_drift` and `panel_floor_protocol` without another round. None changes a finding or the length.

Confidence: high in my area. I verified every number quoted here against the archive.
