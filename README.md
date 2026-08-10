# Low-cost MEMS condition monitoring of induction motors — IEEE TIM paper

Research project: a **measurement methodology + accuracy–resource trade-off
characterization** for ultra-low-bandwidth (100 Hz) smartphone-grade MEMS
vibration sensing in induction-motor condition monitoring, targeting **edge/IoT**
deployment. Built entirely in software on an existing public dataset — no new
hardware, no new measurements.

**Target venue:** IEEE Transactions on Instrumentation and Measurement (TIM).

## Dataset

Ertargın et al., *A smartphone-based vibration dataset for induction motor fault
diagnosis under different speed and load conditions*, Data in Brief 67 (2026)
112916. Mendeley Data DOI `10.17632/rs4vz8n3t5.1` (CC BY-NC 4.0).

> **Upload the raw data into [`data/raw/`](data/raw/)** — see that folder's
> README for the file list and naming convention. Data is git-ignored (kept local).

## Layout

```
data/raw/         <- UPLOAD the 36 dataset files here (git-ignored)
data/processed/   <- generated windows/features (git-ignored)
data/external/    <- optional public datasets for cross-validation (git-ignored)
src/              <- pipeline & experiment code (to be built)
results/          <- figures & tables (git-ignored)
paper/            <- outline.md (TIM structure) + analysis_plan.md
```

## Planning docs

- [`paper/outline.md`](paper/outline.md) — TIM paper structure, contributions, figures.
- [`paper/analysis_plan.md`](paper/analysis_plan.md) — every analysis, tagged to a section.
