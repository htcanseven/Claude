#!/usr/bin/env python3
"""Resolve Reviewer 1's Figure 6 / Table IV question and produce the corrected table.

Reviewer 1 asked:

    "How can 48 errors correspond to a Macro-F1 score higher than that obtained with
     22 errors, while 12 errors and 4 errors result in the same Macro-F1 score?"

The reported values are correct; the presentation is not. Table IV reports classical
models over the 607 unique voltage-vector files, but CNN models pooled over three random
seeds (n = 1821 = 607 x 3). The error-count column therefore switches denominator between
rows, and Fig. 6 reproduces those counts as bar labels.

Run this to confirm the arithmetic and print the corrected, single-denominator table.
"""

N_FILES = 607   # unique voltage-vector files in the public dataset (P15..P21)
N_SEEDS = 3     # CNN runs are pooled over three random seeds

# (label, reported n, reported macro-F1, reported error count) exactly as in Table IV
TABLE_IV = [
    ("ExtraTrees", "All numeric",          607, 0.9951,  3),
    ("SVM-RBF",    "Norm. spectral profile", 607, 0.9935,  4),
    ("LR-L2",      "Band-energy ratios",   607, 0.9935,  4),
    ("SC-CNN",     "Raw + severity calib.", 1821, 0.9935, 12),
    ("Raw-CNN",    "Raw majority voting",  1821, 0.9737, 48),
    ("RF",         "Cross-channel ratios",  607, 0.9632, 22),
]


def on_file_basis(n, errors):
    """Express an error count on the 607-file basis, averaging over seeds if pooled."""
    return errors / N_SEEDS if n == N_FILES * N_SEEDS else float(errors)


def main():
    assert N_FILES * N_SEEDS == 1821, "pooled n should be 607 x 3"

    print("Corrected benchmark table (single denominator, n = 607 files)")
    print("CNN rows are means over the three seeds.\n")
    hdr = f"{'Model':<11}{'Representation':<24}{'Err (607)':>11}{'Err rate':>10}{'Macro-F1':>10}"
    print(hdr)
    print("-" * len(hdr))
    for model, repr_, n, f1, errors in TABLE_IV:
        per_file = on_file_basis(n, errors)
        rate = errors / n * 100.0
        shown = f"{per_file:.1f}{'*' if n != N_FILES else ''}"
        print(f"{model:<11}{repr_:<24}{shown:>11}{rate:>9.2f}%{f1:>10.4f}")
    print("\n* reported in the manuscript as a pooled count over 3 seeds")

    print("\n" + "=" * 62)
    print("Reviewer 1's two apparent contradictions")
    print("=" * 62)

    raw_cnn, rf = 48 / 1821 * 100, 22 / 607 * 100
    print(f"\n1. Raw-CNN 48 errors -> {raw_cnn:.2f}% error rate  (F1 = 0.9737)")
    print(f"   RF       22 errors -> {rf:.2f}% error rate  (F1 = 0.9632)")
    print(f"   => {raw_cnn:.2f}% < {rf:.2f}%, so the CNN is genuinely the better model.")
    print("      More raw errors, but over three times as many predictions.")

    sc_cnn, svm = 12 / 1821 * 100, 4 / 607 * 100
    print(f"\n2. SC-CNN 12 errors -> {sc_cnn:.4f}% error rate  (F1 = 0.9935)")
    print(f"   SVM-RBF  4 errors -> {svm:.4f}% error rate  (F1 = 0.9935)")
    print(f"   => identical rates (12 x 607 == 4 x 1821: {12 * 607 == 4 * 1821}),")
    print("      hence identical macro-F1. Not a coincidence.")

    print("\nFix: report error RATE as the primary column and put CNN results on the")
    print("607-file basis as mean +/- std over seeds. Apply the same correction to")
    print("Fig. 6 bar labels and to the Fig. 7 P18 confusion matrices, which currently")
    print(f"show 36 seed-level errors (= {36 // N_SEEDS} per seed).")


if __name__ == "__main__":
    main()
