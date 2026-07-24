"""Analysis E: communication link-budget + edge-node footprint (deterministic).

No hardware: this quantifies (a) telemetry bitrate of raw/feature/decision
streams vs typical IoT link capacities, and (b) serialized model footprint and
feature-vector cost for candidate edge classifiers. Cycle-accurate MCU latency
(Renode) is left as a labelled next step.
"""
from __future__ import annotations

import os, json, io
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.metrics import accuracy_score

from dataio import list_recordings
from features import build_feature_matrix, FEATURE_NAMES

RES = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")

# Typical *sustainable application-level* uplink capacities (bits/s).
LINKS = {
    "BLE 4.2":       300_000,
    "Zigbee 15.4":   100_000,
    "NB-IoT":         30_000,
    "LoRaWAN(1%DC)":      55,   # SF7 ~5.47 kbps PHY throttled by 1% duty cycle
}


def stream_bitrates(fs=100, n_ch=6, n_feat=84, hop_s=1.0):
    raw = fs * n_ch * 2 * 8                         # int16
    feat = n_feat * 4 * 8 / hop_s                   # float32 per hop
    feat_min = 6 * 1 * 4 * 8 / hop_s                # 6 feats, 1 channel
    dec = (1 + 4) * 8 / hop_s                       # 1B label + ~4B framing per hop
    return {"raw(6ch int16)": raw, "features(84·f32/s)": feat,
            "features(min 6/s)": feat_min, "decision(1/s)": dec}


def model_size_bytes(model) -> int:
    buf = io.BytesIO(); joblib.dump(model, buf, compress=3); return buf.getbuffer().nbytes


def main():
    recs = list_recordings()
    base = build_feature_matrix(recs)
    X, y, g = base["X"], base["y"], base["groups"]
    n_feat = X.shape[1]

    # ---------- link budget ----------
    br = stream_bitrates(n_feat=n_feat)
    lines = ["# Analysis E — Link budget & edge footprint", "",
             "## Telemetry bitrate vs sustainable IoT link capacity", "",
             "| stream | bitrate | " + " | ".join(LINKS) + " |",
             "|" + "---|" * (len(LINKS) + 2)]
    budget = {}
    for sname, bps in br.items():
        cells = []
        for lname, cap in LINKS.items():
            cells.append("✓" if bps <= cap else "✗")
        budget[sname] = bps
        rate = f"{bps/1000:.2f} kbps" if bps >= 1000 else f"{bps:.0f} bps"
        lines.append(f"| {sname} | {rate} | " + " | ".join(cells) + " |")
    lines += ["", "> LoRaWAN's 1% duty cycle (~55 bps sustained) admits **only the "
              "on-node decision stream** — raw or feature streaming at 100 Hz is "
              "infeasible, so classification must run on the node. BLE/Zigbee/NB-IoT "
              "can carry raw or feature streams.", ""]

    # ---------- edge-model footprint vs accuracy (GROUP) ----------
    def group_acc(make):
        sgkf = StratifiedGroupKFold(n_splits=6, shuffle=True, random_state=0)
        accs = []
        for tr, te in sgkf.split(X, y, g):
            m = make(); m.fit(X[tr], y[tr]); accs.append(accuracy_score(y[te], m.predict(X[te])))
        # size from a model trained on all data
        m = make(); m.fit(X, y)
        return 100*np.mean(accs), 100*np.std(accs), model_size_bytes(m)

    candidates = {
        "RF-200": lambda: RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=0),
        "RF-50-d8": lambda: RandomForestClassifier(n_estimators=50, max_depth=8, n_jobs=-1, random_state=0),
        "DecisionTree-d8": lambda: DecisionTreeClassifier(max_depth=8, random_state=0),
        "LogReg": lambda: make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
    }
    lines += ["## Edge-model footprint vs deployment-realistic accuracy", "",
              "| model | GROUP acc | ±std | serialized size |", "|---|---|---|---|"]
    foot = {}
    for name, mk in candidates.items():
        a, s, sz = group_acc(mk)
        foot[name] = dict(acc=a, acc_std=s, size_bytes=sz)
        sz_str = f"{sz/1024:.1f} KB" if sz < 1e6 else f"{sz/1e6:.2f} MB"
        lines.append(f"| {name} | {a:.1f} | {s:.1f} | {sz_str} |")
        print(f"{name:16s} acc={a:.1f}±{s:.1f}  size={sz_str}")

    # feature-vector cost
    fv_bytes = n_feat * 4
    lines += ["",
              f"Per-inference feature vector: {n_feat} floats = {fv_bytes} B. "
              "Feature extraction is O(W·C) time-domain statistics per 2 s window "
              "(W=200 samples, C=6) — no FFT, tractable on a Cortex-M-class MCU.",
              "",
              "> **Next step (labelled):** cycle-accurate latency/energy via Renode "
              "emulation of a Cortex-M4, plus `emlearn`/TFLite-Micro C-array sizes "
              "(the serialized sizes above are Python/joblib and only indicative)."]

    with open(os.path.join(RES, "analysis_E.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(RES, "analysis_E.json"), "w") as f:
        json.dump({"bitrates_bps": budget, "links_bps": LINKS, "footprint": foot}, f, indent=2)
    print("\n".join(lines[:14]))
    print("wrote analysis_E.md / .json")


if __name__ == "__main__":
    main()
