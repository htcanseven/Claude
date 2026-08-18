# Project: EPEi 2026 conference paper → IEEE TIA extension

This repo is a research-planning workspace, not a codebase. A prior Claude session
(claude.ai/code web) completed the planning phase; the full state transfer lives in
**`HANDOVER.md` — read it before doing anything else.**

Quick orientation:
- Topic: FEA-based assessment of the turn-count fault-severity assumption in lumped
  interturn-short-circuit models of PMSMs, validated on the open Brno CEITEC benchmark
  (Zenodo 15233529 / 21717722).
- This machine has ANSYS Maxwell and MATLAB — the reason the work moved here. FEA work
  goes through PyAEDT (`fea/build_maxwell_model.py`, untested skeleton) and the tested
  post-processor `fea/lf_from_matrix.py`.
- Deadlines are live (EPEi notification 31 Aug 2026; the full-paper deadline already
  passed — emailing the chairs is the gating action). See HANDOVER.md §7 for the
  ordered next steps.
- Constraint: never use the MitDev-Eletrica dataset (Zenodo 15741561) — it belongs to a
  separate under-review TIA paper.
