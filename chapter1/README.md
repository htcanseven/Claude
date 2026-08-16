# High-Speed Electrical Machines — Chapter 1

Draft material for the Wiley book proposal (Canseven, Petrov, Pyrhönen).

## Deliverables

| File | What it is |
|---|---|
| `Chapter_1_HighSpeed_FULL.docx` | Full version, ~18 pp. Restructured, with new scaling analysis. |
| `Chapter_1_HighSpeed_MINIMAL.docx` | Minimal version, ~14 pp. Original structure, repairs only. |
| `Chapter_1_Record_of_Changes.docx` | Every change against the original draft, with derivations. |

Both chapter versions contain the same technical corrections and the same six figures.
They differ in structure and depth only.

## Sources

- `ch1_full.md`, `ch1_minimal.md` — chapter text (edit these, then regenerate)
- `CHANGES.md` — change record
- `figures/` — six generated figures, 300 dpi PNG
- `src/verify_scaling.py` — numerical check of every scaling relation in §1.4 / §1.5
- `src/make_figures.py`, `src/fix_figures.py`, `src/fix_figures2.py` — figure generation
- `src/md2docx.py` — Word conversion

## Regenerating

```
pip install matplotlib numpy python-docx
python3 src/make_figures.py && python3 src/fix_figures.py && python3 src/fix_figures2.py
python3 src/md2docx.py
```

## Outstanding

Two figures to be drawn (geared vs direct-drive architecture; rotor bending modes),
citations to be filled in — both are listed in `CHANGES.md` §E.
