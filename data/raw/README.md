# Upload the dataset here (`data/raw/`)

Place the **36 raw dataset files** from the smartphone-MEMS induction-motor
vibration dataset into this folder.

- **Source (Data in Brief 2026):** Ertargın et al., *A smartphone-based vibration
  dataset for induction motor fault diagnosis under different speed and load
  conditions*, Data in Brief 67 (2026) 112916.
- **Data repository (Mendeley Data):** DOI `10.17632/rs4vz8n3t5.1`
  — https://data.mendeley.com/datasets/rs4vz8n3t5/1
- **License:** CC BY-NC 4.0 — kept local, **not** committed to git (see `.gitignore`).

## What to upload

Either the `.csv` or `.mat` files (or both). You can drop them directly in this
folder, or keep the repository's `csv/` and `mat/` split if you prefer — the
loader will search recursively.

Expected: **36 files** = 6 health classes × 2 load states × 3 speeds.

### File-naming convention: `Class_Load_SpeedHz`

| Field | Values |
|-------|--------|
| **Class** | `H` (healthy), `B1` (insufficient lubrication), `B2` (severe insufficient lubrication), `B3` (cracked outer ring), `V` (voltage imbalance), `R` (broken rotor bar) |
| **Load** | `1` = loaded, `0` = unloaded |
| **Speed** | `30Hz`, `40Hz`, `50Hz` |

Examples: `B1_1_40Hz` (insufficient lubrication, loaded, 40 Hz), `H_0_30Hz`
(healthy, unloaded, 30 Hz).

### Signal format (per file)

- **6 channels:** `gx, gy, gz` (raw tri-axial acceleration) and
  `guserx, gusery, guserz` (gravity-compensated linear acceleration).
- **Sampling rate:** 100 Hz. **Duration:** 15 min (~90,000 samples/channel).

## After uploading

Tell me it's uploaded and I'll run a validation pass (file count, channel names,
sample counts, NaNs) before building the pipeline.

> Alternatively, I can attempt to download the dataset directly from Mendeley
> into this folder if outbound access is available — just say the word.
