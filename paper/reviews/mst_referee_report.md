# Referee Report — *Measurement Science and Technology*

**Manuscript:** "Deployment-Realistic Performance Measurement of Low-Cost MEMS Sensing for IoT-Based Condition Monitoring of Induction Machines"

**Article type:** Paper

**Recommendation:** Major revision

---

## 1. Summary

The manuscript re-analyses a public 100 Hz smartphone-MEMS vibration dataset of a single 1.1 kW induction machine (six health states × three supply frequencies × two loads = 36 recordings) and reframes the problem as one of measurement rather than classification. It makes three claims: (i) the consumer accelerometer can be characterised "as a measurement instrument" (effective resolution ≈ 0.015 mg, noise floor −70.8 dB re 1 g²/Hz, usable band bounded by the 50 Hz Nyquist limit), and its raw channels carry more fault information than the on-device gravity-compensated channels; (ii) conventional random-split evaluation is a "measurement artefact" that overstates accuracy by ~40–45 points, whereas a leakage-free recording-wise protocol yields a deployment-honest ~50–75% baseline; and (iii) a resource-frugal configuration (25 Hz, three raw channels, 4 s window) is measured to outperform the full-rate configuration by ~23 points while cutting data volume ~8×, which the authors translate into IoT link-budget and edge-footprint operating points. No new data are collected; the contribution is methodological and analytical.

## 2. Fit to MST scope

This is the pivotal question, given the prior TIM desk-rejection on scope grounds, and my assessment is mixed and honest: **the reframing is defensible in principle but the executed measurement content is currently too thin to carry the paper on measurement-science merit.**

What is genuinely "measurement" here:

- The "how should diagnostic performance itself be measured?" framing (Section V, `subsec:protocols`; Section VI.A) is a legitimate measurement-methodology angle. MST does publish condition-monitoring and smart-sensor work of exactly this flavour — indeed the authors cite one such paper in the journal (Shukla *et al.* 2020, `shukla2020smartsensor`, MST 31 105104).
- The uncertainty framing (Type A expanded uncertainty, coverage factor, GUM citation `jcgm2008gum`) and the paired significance testing signal a measurement sensibility that is above the norm for this subfield.

Why the measurement contribution is nonetheless insufficient *as it stands*:

- **The "sensor-as-instrument" characterisation (Section IV) is metrologically thin.** "Effective resolution" is the quantisation LSB read off the exported data; "noise floor" is the median PSD above 30 Hz of a *running* machine; and "usable band" is simply the Nyquist frequency — a definition, not a measurement. There is no calibration, no traceability, no frequency-response or linearity measurement, no reference-accelerometer comparison, and no temperature characterisation. This is precisely the content that the metrology papers the authors themselves cite actually deliver (Prato *et al.* 2021 `prato2021mems`; Schiavi *et al.* 2023 `schiavi2023mems`; D'Emilia & Natale 2021 `demilia2021mems`). Against that backdrop, Section IV reads as descriptive statistics on a downloaded file, not as instrument characterisation in the sense an MST reader expects.
- **The "measurement methodology" is, at core, ML evaluation methodology that already exists.** Group-/recording-wise evaluation and the leakage critique are established (Kapoor & Narayanan 2023; Wheat *et al.* 2024; Hendriks *et al.* 2022 — all cited). The novelty is the *application* to a low-rate smartphone dataset, not the method.
- **The uncertainty analysis borrows GUM vocabulary for a quantity whose dominant uncertainty components are explicitly excluded** (see §4). This risks reading as metrological framing rather than metrological substance.

**Net:** the paper sits closer to MST scope than TIM's rejection implies, but its acceptance on those grounds should be conditional on *deepening the genuine measurement content* — either a real instrument characterisation (bench noise floor at rest, amplitude/frequency response over 0–50 Hz against a reference) or a properly constructed uncertainty/evaluation framework whose unit of analysis is defensible (§4). Without that, the "measurement science" is largely a veneer over an applied re-analysis, and the scope concern is real.

## 3. Significance and novelty

The significance of the *message* is real: for this class of data — one continuous recording per operating condition, heavy window overlap — random-split evaluation is badly optimistic, and demonstrating a 100% → ~50% collapse is a useful cautionary result for the smartphone/MEMS condition-monitoring community, which (as the authors correctly note, Section II.D) still routinely reports near-perfect accuracy.

The *novelty*, however, is modest:

- The leakage phenomenon and its remedy are known; the demonstration is a confirmation on a new (single) dataset rather than a methodological advance.
- The dataset is public and already carries its own baseline (`ertargin2026smartphone`); the classifiers (RF/KNN/SVM, logistic regression, shallow tree) and the 14 time-domain features are entirely standard.
- The most novel empirical claim — "ultra-low-bandwidth sensing is an asset" — is confounded and non-monotonic (§4, Concern 5), so it cannot yet be advanced as a finding.
- The channel-informativeness result is interesting but is partly contradicted by the authors' own data and is leakage-suspect (§4, Concern 7).

The self-assessment in Table `tab:positioning` (all six criteria checked for "This work," including "Sensor charact." and "Acc.–resource trade-off") overstates the differentiation, given how light the characterisation and how confounded the trade-off actually are.

## 4. Technical soundness and rigor

The evaluation architecture is sensible and the leakage demonstration is sound. But the inferential claims are weaker than presented, and I have concrete, verifiable objections.

**(a) The significance testing is overstated by pseudoreplication.** The paired *t*-test and Wilcoxon signed-rank test are reported at `p<10^-5` and `p<10^-4` (abstract; Table `tab:measured`; Section VI.B). The underlying analysis (`results/analysis_stats.md`) shows these are computed over **n = 30 = 5 seeds × 6 folds on a *fixed* recording-level partition**. Because the five seeds are re-runs on the *same* data and the *same* partition, they are not independent observations — they capture model-training stochasticity, not sampling variation. The independent unit is the fold (n = 6). With n = 6, a two-sided Wilcoxon signed-rank test *cannot* reach below ≈ 0.03 (its minimum attainable p is 2/2⁶ = 0.031), so a reported `Wilcoxon p<10^-4` is not attainable at the honest unit of analysis. The p-values are therefore inflated by treating pseudoreplicates as replicates. *What would address it:* use the fold (n = 6) as the experimental unit, or a clustered/mixed model with seed as a nested factor; report the honest (and much weaker) p-values; and reconcile the unit of analysis with the uncertainty computation, which uses n = 5 seeds (see (b)).

**(b) The uncertainty is mislabeled and captures only resampling variance.**
- *Coverage-factor inconsistency (a genuine reporting error, not a transient number):* Section V states the coverage factor is `k = t_{0.975,4} ≈ 2.78`; `analysis_stats.md` confirms 2.78; but the caption of Table `tab:measured` states `k = 2`. The tabulated intervals (e.g., baseline ±4.4 for s = 3.5, n = 5 ⇒ U = 2.78 × 3.5/√5 ≈ 4.4) were computed with 2.78, so the "k = 2" caption is simply wrong. Fix it.
- *Substance:* treating the five per-seed means as "repeated measurements" and applying GUM Type A machinery yields an expanded uncertainty that reflects only seed/fold reshuffling on **one machine and one fixed set of 36 recordings**. The authors acknowledge this ("does not capture the additional, unquantified uncertainty arising from the single-machine scope," Section V), but the abstract, Table `tab:measured`, and the term "expanded uncertainty" still present a GUM-grade figure whose dominant components (machine-to-machine, specimen-to-specimen, mounting, severity grading) are excluded. *What would address it:* state explicitly that the reported U is a *resampling* uncertainty only; avoid GUM "expanded uncertainty" phrasing unless the excluded Type B components are at least bounded; and quote it as a reproducibility interval.

**(c) External validity is limited by a specimen confound the paper does not confront.** All 36 recordings come from one machine, and each health *class* corresponds to a *single physical specimen* (one cracked-outer-ring bearing, one drilled rotor, one imbalance wiring). Under the GROUP protocol, holding out one recording of class B3 still trains on the same physical B3 bearing at other speeds/loads. The classifier can therefore key on *that specimen's* idiosyncratic signature (its particular imbalance, clearance, mounting) rather than a fault signature that would generalise to a different specimen of the same fault — the classic "specimen identification" confound that the very reference the authors cite for leakage (Hendriks *et al.* 2022) raises for CWRU. The "leakage-free" label is thus only relative: it removes window-overlap and exact-operating-point identity, not the specimen/mounting confound. *What would address it:* explicitly discuss this confound and its bearing on interpretation; ideally add repeated re-installations per fault, multiple specimens per class, or a second machine; and reframe "measuring machine health" accordingly.

**(d) The "low rate as an asset" result is confounded and non-monotonic.** In both the paper (Table `tab:sampling`) and `analysis_D.md`, the sampling sweep is erratic: 50 Hz is *worse* than 100 Hz (42.0 vs 53.7 in the paper; 43.7 vs 46.4 in `analysis_D`), yet 25 Hz peaks (64.9 / 66.7). `RESULTS.md` attributes the 25 Hz gain to the **anti-alias low-pass removing content "the model overfits"** — i.e., the effect is entangled with filtering and with overfitting on ~30 recordings, not with sample rate per se, and the 50 Hz dip is left unexplained. The single-seed spreads are ±(13–19) points, so the 25 Hz peak overlaps heavily with 100 Hz; the claimed significance rests on the pseudoreplicated paired test of (a). *What would address it:* separate sample rate from anti-alias filtering (e.g., low-pass at 100 Hz vs decimate to 25 Hz); explain the 50 Hz dip; show the sweep with honest CIs; and reframe the claim as "decimation/low-pass does not hurt, and may reduce overfitting on this dataset."

**(e) Deployment quantities are emulated, not measured.** Energy is never measured (only inferred from data volume); latency is proxied by window length; the "edge-model footprint" is a Python/joblib serialized size — which `analysis_E.md` itself flags as "only indicative" — not an embedded C/quantized footprint; and packet loss, bit-depth reduction, and mounting rotation are injected post hoc in software. The link-budget bitrates are correct arithmetic (6 ch × 100 Hz × 16 bit = 9.6 kbps, etc.) but are calculations, not measurements. These should be labeled as such throughout, and the deployment claims softened accordingly (see Concern 6).

**(f) The channel-informativeness claim is partly contradicted by the authors' own data.** The validation table (`validation.md`) shows that per axis the standard deviations of the raw and gravity-compensated channels are essentially identical (e.g., H_0_30Hz: gX σ = 0.066, gUserX σ = 0.066; gY σ = gUserY σ; gZ σ ≈ gUserZ σ). If gravity compensation "discards diagnostically useful low-frequency content" (abstract; Section IV.C), the AC power of the compensated channel should be visibly lower — it is not. The complementary filter appears to *reshape* rather than *remove* AC power. Moreover, the mutual information (Section IV.C, Fig. `fig:mi`) is computed pooled over windows without recording-wise separation; because the raw channels retain a per-recording DC/tilt offset (the "Mean" feature) that varies with condition, the raw-channel MI advantage may partly encode *recording identity* — the very leakage the paper otherwise condemns. This is an internal inconsistency in the application of the paper's own principle. *What would address it:* recompute MI under recording-wise separation; test whether removing the raw DC offset erases the advantage; and reconcile the "discards" claim with the near-equal AC standard deviations.

**(g) A characterisation over-simplification.** Section IV.B states the bearing defect frequencies "lie well above 50 Hz." This holds at 50 Hz supply (for 6205, BPFO ≈ 3.6·f_r ≈ 86 Hz at ~24 Hz shaft), but at 30 Hz supply (~14 Hz shaft) BPFO ≈ 50 Hz and BSF ≈ 33 Hz fall *within* the usable band. The categorical claim should be softened; this nuance may also partly explain the residual bearing-fault separability.

## 5. Strengths

- **A clear, honest, and useful central message.** The 100% → ~50% collapse under recording-wise evaluation (Table `tab:optimism`, Fig. `fig:gap`) is a striking and well-motivated cautionary result for a community that still reports near-perfect accuracy on this data class (Section II.D).
- **Reproducibility discipline.** The integrity check (Section III.E; `validation.md`) is thorough — 36/36 recordings, exactly 89,999 samples/channel, zero NaNs, negligible sample-and-hold duplication — and the pipeline reproduces the source article's window count (32,328) exactly. Fixed seeds and released code are promised.
- **Above-average methodological care for the subfield:** four contrasting evaluation protocols on identical features (Fig. `fig:pipeline`), multi-seed repetition, and paired testing on identical held-out recordings.
- **Honest reporting of failure modes:** the B1/B2 lubrication confusion (Fig. `fig:confusion`), the mounting-orientation sensitivity (30° → ~31%, `analysis_D.md` D7), and a candid Limitations section (VII.B).
- **Genuine practical value** in the accuracy–resource framing for IoT nodes, and a well-chosen, relevant figure set.
- The writing is clear and the structure logical.

## 6. Major concerns

**M1. The measurement/instrumentation contribution is too thin for MST as executed.** Section IV provides descriptive statistics (quantisation LSB, running-machine PSD, Nyquist band), not an instrument characterisation of the kind MST readers expect and that the cited metrology literature exemplifies. *Address by:* adding a genuine characterisation — a true noise floor from a *stationary* sensor (no excitation), and amplitude/frequency response and linearity over 0–50 Hz against a reference accelerometer — or, failing that, substantially reducing the metrological claims and reframing Section IV as a signal-content analysis rather than instrument characterisation.

**M2. Overstated statistical significance (pseudoreplication).** See §4(a). The reported `p<10^-5`/`p<10^-4` use n = 30 pseudoreplicates; the honest unit is n = 6 folds, at which the Wilcoxon cannot reach below ≈ 0.03. *Address by:* recomputing significance with the fold (or a clustered model) as the unit and reporting the honest p-values, then re-wording the abstract/results accordingly.

**M3. Uncertainty is mislabeled and underpowered.** See §4(b). Fix the k = 2 vs k = 2.78 contradiction (Table `tab:measured` caption vs Section V), and stop presenting a seed-resampling spread as GUM "expanded uncertainty" without at least bounding the excluded (single-machine, specimen, mounting, qualitative-severity) components. *Address by:* relabeling as reproducibility uncertainty, correcting k, and adding a qualitative Type B discussion.

**M4. Single-machine, single-specimen external validity; over-general claims.** See §4(c). Broad statements — "default operating point for this class of node" (Section VII), "a reproducible reference for assessing low-cost vibration-sensing instruments" (abstract) — are not supported by one machine with one physical specimen per fault. *Address by:* tempering to a single-machine feasibility study, confronting the specimen confound explicitly, and (ideally) adding a second machine or repeated installations.

**M5. "Low sampling rate is an asset" is not yet a supportable finding.** See §4(d). Non-monotonic sweep, anti-alias/overfitting confound, and CIs that overlap. *Address by:* disentangling rate from anti-alias filtering, explaining the 50 Hz dip, and reframing as "decimation does not hurt / reduces overfitting here."

**M6. Emulated vs measured deployment quantities.** See §4(e). Energy unmeasured, latency proxied, footprint from pickle sizes, robustness stresses simulated. *Address by:* labeling every such quantity as calculated/emulated; either delivering the promised cycle-accurate MCU measurement (Renode/emlearn are already named in `analysis_E.md`) with true C/quantized footprints, or removing the pickle-size "footprint" table and softening the energy/latency claims to conjecture.

**M7. Channel-informativeness claim is inconsistent with the authors' own data and is leakage-suspect.** See §4(f). *Address by:* recomputing MI recording-wise, testing sensitivity to the raw DC offset, and reconciling "discards low-frequency content" with the near-equal AC standard deviations (or restating it as "reshapes").

## 7. Minor concerns

1. **Internal numeric reconciliation.** The baseline 100 Hz/6 ch/2 s RF accuracy appears as 46.4 (Table `tab:footprint`; `analysis_D`), 52.8 (Table `tab:measured`), 53.7 (Tables `tab:sampling`, `tab:recipe`; text), and 54.3 (Table `tab:optimism`). I understand these are being reconciled; the final version must draw all headline numbers from a single, stated pipeline run.
2. **Classifier hyperparameters stated inconsistently.** Section V specifies "Random Forest … with 300 trees," but `analysis_stats.md`/`analysis_E.md` use RF-200, and Table `tab:footprint` reports "Random Forest (200 trees)." State the exact configuration used for each table and keep it consistent.
3. **Footprint-table RF (46.4%) is a different configuration** from the RF elsewhere (54.3 / 53.7); ensure the footprint accuracies are drawn from the same protocol and config as the main results, or note the difference.
4. **Optimism-gap magnitude is run-dependent** (39–46 pts multi-seed; 37–52 pts single-seed per `RESULTS.md`). Report it with its spread rather than a point range.
5. **Leftover IEEE artefacts.** The section files carry "IEEE TIM / IEEEtran" header comments, and the (non-submitted) top-level `main.tex` is IEEEtran. The actual MST submission (`manuscript.tex`) is correctly `iopjournal`, but it uses `\bibliographystyle{unsrt}`; please adopt the IOP reference style (e.g., `iopart-num`) and purge the IEEE comments to avoid confusion.
6. **Fig. 1 callouts.** Eight components are labeled (including oscilloscope, resistive load bank, digital multimeter) but several are not referenced or motivated in the text; confirm the resistive load bank is consistent with the DC-generator loading described in Section III.A.
7. **Per-class performance should be in the main text.** The macro-F1 and per-class recall (e.g., B2 recall ≈ 0.16, `RESULTS.md`) materially qualify "measuring machine health" and should not be relegated to a figure only.
8. **Terminology.** "Measures machine health significantly more reliably" conflates classification accuracy with health measurement; prefer "classifies health state." Define BPFO/BPFI/BSF at first use (Section II.A).
9. **Units.** Define "−70.8 dB re 1 g²/Hz" (PSD level) once and use consistently.
10. **Reference balance.** Consider adding archival condition-monitoring/uncertainty references (including from MST) to strengthen the metrological framing; several current entries are Data-in-Brief data descriptors.
11. Citing Nyquist (1924) and Shannon (1948) for "100 Hz ⇒ 50 Hz band" is heavy; a standard DSP text suffices.

## 8. Overall recommendation

**Major revision.** The paper has an honest, reproducible core (leakage inflates low-rate smartphone-MEMS condition-monitoring accuracy; frugal configurations remain viable) that is worth bringing to publication, and the measurement-methodology framing is a defensible fit for MST — more so than the TIM scope rejection suggests. But it is not yet acceptable: (i) the genuine measurement/instrumentation contribution, on which MST scope depends, is currently thin and partly superficial (M1); (ii) the headline statistics overstate significance through pseudoreplication and the uncertainty is mislabeled and underpowered (M2, M3); (iii) central deployment quantities are emulated rather than measured (M6); and (iv) several flagship claims — low-rate-as-asset, channel informativeness, and generalizable "operating points" — outrun a single-machine, single-specimen, confounded, non-monotonic evidence base (M4, M5, M7), with one claim (channel informativeness) partly contradicted by the authors' own validation data. These are substantial but, in most cases, addressable through re-analysis and re-framing rather than new data collection; hence major revision rather than reject. I would want to see M1–M3 and M7 resolved convincingly, and M4–M6 either resolved or honestly de-scoped, before acceptance. If, on revision, the authors cannot deepen the measurement contribution beyond descriptive statistics and cannot repair the statistical inference, the scope concern (Section 2) would in my view justify rejection.

## 9. Specific questions to the authors

1. In the paired significance tests, what is the experimental unit? If n = 30 pools 5 seeds × 6 folds on a *fixed* partition, how do you justify treating seed re-runs as independent, and what are the p-values with the fold as the unit (n = 6)?
2. Which coverage factor was actually used for Table `tab:measured` — k = 2 (caption) or k = t₀.₉₇₅,₄ = 2.78 (Section V and `analysis_stats.md`)? Please reconcile.
3. Does the decimation in the sampling-rate sweep apply an anti-alias filter? If so, can you separate the effect of sample rate from that of low-pass filtering (e.g., low-pass-only at 100 Hz vs decimate-to-25 Hz)? What explains the non-monotonic dip at 50 Hz?
4. Was the channel mutual information estimated with recording-wise separation? Given that the raw channels carry per-recording DC/tilt offsets that vary with condition, could the raw-channel MI advantage partly reflect recording identity? What happens if the DC offset (the "Mean" feature) is removed?
5. How do you reconcile the claim that gravity compensation "discards" low-frequency content with the near-equal per-axis standard deviations of the raw and compensated channels in `validation.md` (e.g., 0.066 vs 0.066)?
6. Each fault class corresponds to a single physical specimen recorded at 3 speeds × 2 loads, and the GROUP protocol trains and tests on that same specimen. How do you exclude the possibility that the classifier identifies the specific specimen/mounting rather than a generalizable fault signature?
7. How was the noise floor isolated from genuine machine vibration, given that it was computed above 30 Hz from a *running* (healthy) recording rather than from a stationary sensor?
8. What is the embedded (C/quantized) model footprint as opposed to the Python/joblib serialized size, and do the footprint-table accuracies use the same RF configuration (200 vs 300 trees) as the rest of the paper?
9. Can you provide any direct or bounded estimate of on-node energy and latency, or should those claims be qualified as conjecture pending the promised MCU measurement?
10. Given the single-machine, single-specimen scope, on what basis is 25 Hz / raw-3ch / 4 s recommended as a "default operating point" for this class of node in general?
