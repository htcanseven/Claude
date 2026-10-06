# High-Speed Electrical Machines — Chapter 1

Draft material for the Wiley book proposal (Canseven, Petrov, Pyrhönen).

## Deliverables

| File | What it is |
|---|---|
| `Chapter_1_HS_machines_TRACKED.docx` | **For the co-authors.** The author's own file with every edit as a Word tracked change (458 revisions). See `TRACKED_CHANGES.md`. |
| `Chapter_1_HS_machines_CLEAN.docx` | **For contributors and the publisher.** The same file with every change accepted and Track Changes off. Built by `src/accept_changes.py`; verified identical to accept-all of the tracked file. |
| `Annotated_TOC_for_contributors.docx` | The version that goes outside: no Status column, no title deliberation. Built by `src/make_circulation_toc.py`. **Circulate this one.** |
| `Chapter_Ownership.docx` / `.md` | Why every chapter has one owner, and what that means for each invitation. |
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
- `src/make_schematics.py` — the two schematic figures of the first revision (superseded by `src/ch1_figures.py`)
- `src/recover_original.py` — rebuilds original_draft_text.json from a redline
- `src/md2docx.py` — Word conversion
- `src/make_redline.py` — tracked-changes redline generation
- `src/verify_redline.py` — checks that Accept All reproduces the revised text and Reject All the original

## House style: the current figures and chapter

- `House_Style.md`, `House_Style.docx` — the rules for every chapter; the .docx is also the Word template
- `src/hsbook_style.py`, `src/hsbook_style.m` — the house style as code, for Python and MATLAB
- `src/ch1_figures.py` — all nine Chapter 1 figures, written to `figures/ch1/`
- `src/trace_fig_1_04.py` — the mode shapes of Figure 1.4, traced from the original picture into `data/fig_1_04_modes.csv`; replace that file with the model's own export
- `src/apply_house_style.py` — `incoming/Chapter_1_final.docx` to `Chapter_1_house_style.docx`; what it changed is in `Chapter_1_house_style_CHANGES.md`
- `src/add_confidentiality.py` — the stamped copies in `to_send/`
- `src/make_style_guide.py` — `House_Style.docx`
- `src/mpl_to_pptx.py`, `src/preview_pptx.py` — Figure 1.2 as editable PowerPoint, SVG and PDF in `figures/editable/`

```
pip install matplotlib numpy scipy pillow lxml python-docx python-pptx
python3 src/ch1_figures.py
python3 src/apply_house_style.py && python3 src/add_confidentiality.py chapter
python3 src/make_style_guide.py
python3 src/mpl_to_pptx.py
```

## Regenerating the first revision

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
