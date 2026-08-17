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

| Dataset | Role |
|---|---|
| Three-phase PMSM ITSC, IEEE DataPort — 12 torque-speed points × 9 shorted-turn levels × 3 SC resistances | **Primary.** The severity axis is what makes the two-paper split possible. |
| Paderborn KAt bearing (PMSM drivetrain, current + vibration, real + artificial damage) | Cross-dataset generalization in the journal paper |
| Paderborn electric motor temperature (~185 h) | Optional bridge to the cooling work |
| CWRU bearing | Legacy baseline only — CWRU-only validation is penalized by reviewers |

## 4. Work split

| | EPEi (6 pp) | TIA extension |
|---|---|---|
| Task | Fault **detection** — binary / few-class | Severity **estimation** — regression on shorted-turn % |
| Conditions | 1–2 operating points | All 12 torque-speed points; unseen-condition generalization |
| Data | FEA-generated training + one public dataset | + cross-machine domain adaptation + **own-rig measurement** |
| Baselines | 2 classical (MCSA/FFT features + shallow classifier) | Full ablation, repeated runs, significance testing |
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
