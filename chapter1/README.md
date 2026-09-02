# High-Speed Electrical Machines — Chapter 1

Draft material for the Wiley book proposal (Canseven, Petrov, Pyrhönen).

## Deliverables

| File | What it is |
|---|---|
| `Chapter_1_HighSpeed_FULL.docx` | Full version, ~18 pp. Restructured, with new scaling analysis. |
| `Chapter_1_HighSpeed_MINIMAL.docx` | Minimal version, ~14 pp. Original structure, repairs only. |
| `Chapter_1_Record_of_Changes.docx` | Every change against the original draft, with derivations. |
| `Chapter_1_Redline_FULL.docx` | Word tracked-changes redline: original draft → full version. |
| `Chapter_1_Redline_MINIMAL.docx` | Word tracked-changes redline: original draft → minimal version. |

Both chapter versions contain the same technical corrections and the same six figures.
They differ in structure and depth only.

## Sources

- `ch1_full.md`, `ch1_minimal.md` — chapter text (edit these, then regenerate)
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
