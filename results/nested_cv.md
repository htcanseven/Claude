# A4 - nested recording-wise cross-validation

- nested (unbiased) estimate: **71.0%** over 18 outer folds
- best configuration judged on the outer folds themselves: fs25_raw3_w4 at 76.9%
- selection bias: **+6.0 points**

## Configurations selected by the inner loop

- fs25_raw3_w4: chosen in 13/18 outer folds
- fs100_all6_w4: chosen in 2/18 outer folds
- fs12.5_raw3_w4: chosen in 2/18 outer folds
- fs12.5_all6_w2: chosen in 1/18 outer folds

## Naive ranking (biased, for reference)

- fs25_raw3_w4: 76.9%
- fs25_all6_w4: 69.7%
- fs12.5_raw3_w4: 67.3%
- fs12.5_all6_w4: 66.7%
- fs25_raw3_w2: 66.2%
- fs100_raw3_w4: 65.8%
- fs25_all6_w2: 63.7%
- fs100_raw3_w2: 62.6%
- fs12.5_all6_w2: 62.3%
- fs12.5_raw3_w2: 61.2%
- fs100_all6_w4: 60.8%
- fs100_all6_w2: 55.2%
