# Analysis E — Link budget & edge footprint

## Telemetry bitrate vs sustainable IoT link capacity

| stream | bitrate | BLE 4.2 | Zigbee 15.4 | NB-IoT | LoRaWAN(1%DC) |
|---|---|---|---|---|---|
| raw(6ch int16) | 9.60 kbps | ✓ | ✓ | ✓ | ✗ |
| features(84·f32/s) | 2.69 kbps | ✓ | ✓ | ✓ | ✗ |
| features(min 6/s) | 192 bps | ✓ | ✓ | ✓ | ✗ |
| decision(1/s) | 40 bps | ✓ | ✓ | ✓ | ✓ |

> LoRaWAN's 1% duty cycle (~55 bps sustained) admits **only the on-node decision stream** — raw or feature streaming at 100 Hz is infeasible, so classification must run on the node. BLE/Zigbee/NB-IoT can carry raw or feature streams.

## Edge-model footprint vs deployment-realistic accuracy

| model | GROUP acc | ±std | serialized size |
|---|---|---|---|
| RF-200 | 46.4 | 10.9 | 1.09 MB |
| RF-50-d8 | 51.2 | 8.9 | 214.4 KB |
| DecisionTree-d8 | 43.7 | 10.7 | 4.3 KB |
| LogReg | 52.2 | 14.8 | 4.7 KB |

Per-inference feature vector: 84 floats = 336 B. Feature extraction is O(W·C) time-domain statistics per 2 s window (W=200 samples, C=6) — no FFT, tractable on a Cortex-M-class MCU.

> **Next step (labelled):** cycle-accurate latency/energy via Renode emulation of a Cortex-M4, plus `emlearn`/TFLite-Micro C-array sizes (the serialized sizes above are Python/joblib and only indicative).
