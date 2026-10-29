# Response to the final consistency comments (third round of the external reviews)

Manuscript: single-column review version `paper/main.pdf` (42 pages), double-column CAS version `paper/main_dc.pdf`
(24 pages). The decision and held-out tables of the common bench were rerun (`scripts/revision_round4.py`,
`results/tables/R_decision_table_5c*.csv`, `R4_*.csv`); no verdict changed.

## What was corrected

| Item | Raised by | Change |
|---|---|---|
| At-level decision against the all-higher-level summary | E.2 §2 | Option 1. Section 3.3 now defines adequacy as the step-5 condition at `e_req` itself, a local decision; `e90^B` summarises from which level that decision holds at every higher tested level, so `e90^B ≤ e_req` implies adequacy but not conversely; on these data the two coincide because no suite meets a level and fails a higher one (every row of Table 7 is monotone). The implementation is the at-level rule, as the reviewer favours. |
| Table 6 against Table 8, SCIG inter-winding drive suites | E.4 must-fix 1 | Root cause: the suite table used the PMSG/SCIG suite definition with the PI-output features, the decision and held-out tables the three-machine definition without them. The common-bench decision tables (both units, three α, 1000 and 10 000 resamples), the held-out run and the selection-rule variant were rerun with the PI outputs included. All three tables now name the d-axis PI ripple for those suites; no support value and no verdict changed. Section 5.5 states that the PI ripple, the d-axis current ripple and the duty-cycle residual tie on extent and share for that suite and that the folds choose among the three; the 3 of 9 held-out false alarms belong to the in-sample fixed feature (1 of 9 in sample). |
| SCIG no-added-sensor recommendation conditional | E.2 §3, E.4 should-fix 9 | Section 6.2: the drive-internal suite meets the empirical detection-power criterion with a false-alarm performance that the held-out run leaves to be validated, so it is a candidate specification, not a validated one. |
| Highlight 4 | E.2 §3 | "A decision table selects the cheapest suite meeting an empirical 0.9 power target" (81 characters). |
| Orphaned borderline footnote | E.2 §4, E.3 item 1, E.4 must-fix 3 | The footnote is printed only when a cell carries the marker; at 10 000 resamples none does, so it is gone. The inheritance marker likewise appears only where it changes a cell, which removes the vacuous marker on a 0.00 cell (E.4 item 11). |
| "a single failure-mode class" | E.2 §4, E.4 must-fix 5 | "resistor-limited stator-winding short-circuits in two classes". |
| §4.4 resample count | E.4 must-fix 2 | 10 000 at α = 0.95 on the common bench, 1000 otherwise. |
| Fig. 8 cited before Figs. 2–7 | E.4 must-fix 4 | Section 3.2 cites Section 5.4 instead; Fig. 8 is first cited in Section 5.4. The same check found Fig. 7 and Table 7 cited early in Section 3.3; both now cite the section, and figures and tables are first cited in numerical order. |
| Log-logistic a90 against e90^B | E.4 should-fix 7 | The POD-fit paragraph moved from the limitations to Section 5.5 with a reconciliation: a90 is the crossing of a fitted curve between the smallest level (78 % detected for the PMSG's duty-cycle residual) and the next (100 %), borrowing the saturated upper levels' strength through the assumed shape; e90 reads the first tested level with a share of 0.9 (10.1 %) and e90^B the first from which the whole procedure meets it in 95 % of resamples (14.6 %). |
| Table 9 row at a boundary | E.4 should-fix 8 | The row's pooled support is 0.0503, uncertain by the unrounded rule; the caption now reads "… or lies at a boundary", the cells at a boundary print three decimals, and the note says the class is taken on the unrounded fraction. |
| False-alarm count as a tie-break | E.4 should-fix 10 | Stated as a choice in Section 3.2: the count enters only through the screen; a design team may prefer the quieter of two tied features. The rule itself is unchanged so that every table stays on one rule. |
| Small items | E.4 item 11, E.3 items 3–4 | "nuisance-alarm" → "false-alarm"; "is the slope" → "reflects the slope"; abstract "is met by drive-internal quantities alone"; Table 7 header without the percent sign; Section 5.4 states why the denominator is 30 on the SCIG (shaft-torque features with an unbounded null). |

## Checked and left as they are

* Highlights: 82, 80, 85, 81 and 73 characters, no acronyms beyond the ones MSSP tolerates (none).
* Data-availability DOIs: the link targets are the full DOIs; only the printed text breaks at the line (xurl).
* Reference list complete in both compiled files (46 entries); all cross-references resolve; abstract 250 words.
* Reference 41 stays, cited neutrally.

## Not done

* Code repository and a code-availability statement: the author's decision; raised again by E.2 and E.4, and it will
  come up at the journal.
* A generative-AI declaration: removed at the author's request in an earlier round; MSSP asks for one where
  applicable.
