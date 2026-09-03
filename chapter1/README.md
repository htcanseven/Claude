# High-Speed Electrical Machines — Chapter 1

Draft material for the Wiley book proposal (Canseven, Petrov, Pyrhönen).

## Deliverables

| File | What it is |
|---|---|
| `Chapter_1_HS_machines_TRACKED.docx` | **The deliverable.** The author's own file with every edit as a Word tracked change (458 revisions). See `TRACKED_CHANGES.md`. |
| `Annotated_TOC.docx` / `Annotated_TOC.md` | The annotated table of contents for the Wiley proposal: positioning, 12 chapter abstracts, budgets, contributors, schedule. |
| `Invitation_Emails.docx` / `Invitation_Emails.md` | Short invitation emails, one per invitee, in the author's own register. Use these to invite. |
| `Contributor_Invitation.docx` / `Contributor_Invitation.md` | Long form: terms sheet, one detailed "your contribution" block per invitee, letter-of-support template, pre-sending checklist. Use after the publisher approves. |
| `source/The_first_Ch_of_HS_machines_1.docx` | The author's original file, untouched. |
| `Chapter_1_HighSpeed_CONSERVATIVE.docx` | Earlier reconstruction: original prose verbatim, corrections added alongside. |
| `Chapter_1_Redline_CONSERVATIVE.docx` | Word-level tracked changes for the conservative version. |
| `Chapter_1_HighSpeed_FULL.docx` | Full version, ~18 pp. Restructured, with new scaling analysis. |
| `Chapter_1_HighSpeed_MINIMAL.docx` | Minimal version, ~14 pp. Original structure, repairs only. |
| `Chapter_1_Record_of_Changes.docx` | Every change against the original draft, with derivations. |
| `Chapter_1_Redline_FULL.docx` | Word tracked-changes redline: original draft → full version. |
| `Chapter_1_Redline_MINIMAL.docx` | Word tracked-changes redline: original draft → minimal version. |

Both chapter versions contain the same technical corrections and the same six figures.
They differ in structure and depth only.

## Sources

- `ch1_conservative.md`, `ch1_full.md`, `ch1_minimal.md` — chapter text
- `src/build_tracked.py` — applies the tracked edits directly to the author's .docx XML (run from `work/`)
- `src/verify_tracked.py` — checks reject-all reproduces the original and accept-all contains the new material
- `src/make_trilemma.py` — the new Figure 1.9
- `src/build_conservative.py` — generates the conservative chapter from the draft plus an auditable edit list
- `CHANGES.md` — change record
- `figures/` — all eight figures, 300 dpi PNG
- `original_draft_text.json` — the original draft's text, recovered from the redlines
- `src/verify_scaling.py` — numerical check of every scaling relation in §1.4 / §1.5
- `src/make_figures.py`, `src/fix_figures.py`, `src/fix_figures2.py` — analytical figures
- `src/make_schematics.py` — the two schematic figures
- `src/recover_original.py` — rebuilds original_draft_text.json from a redline
- `src/md2docx.py` — Word conversion
- `src/make_redline.py` — tracked-changes redline generation
- `src/verify_redline.py` — checks that Accept All reproduces the revised text and Reject All the original

## Regenerating

```
pip install matplotlib numpy python-docx
python3 src/make_figures.py && python3 src/fix_figures.py && python3 src/fix_figures2.py
python3 src/make_schematics.py
python3 src/md2docx.py
python3 src/make_redline.py && python3 src/verify_redline.py
```

## Outstanding

Citations to be filled in; every location is listed in `CHANGES.md` §E.
All figures are complete.
