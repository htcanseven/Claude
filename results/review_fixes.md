# Review-driven recomputes

## Honest significance (seed-level paired, n=5)
- optimal_vs_baseline: Δ=+23.1 pts; paired t(n=5) p=0.0001; Wilcoxon p=0.0625
- fs25_vs_fs100: Δ=+10.1 pts; paired t(n=5) p=0.0028; Wilcoxon p=0.0625

## Channel MI (raw vs gravity-compensated)
- full: raw=0.693, user=0.500, ratio=1.39
- no_mean: raw=0.695, user=0.530, ratio=1.31
- dc_invariant: raw=0.633, user=0.478, ratio=1.32

## Raw vs gravity-compensated AC content
- AC power ratio (raw/user): {'gX/gUserX': 0.9993647336959839, 'gY/gUserY': 1.0005632638931274, 'gZ/gUserZ': 1.0002989768981934}
- AC correlation (raw~user): {'gX~gUserX': 0.5785442284233455, 'gY~gUserY': 0.4568665294850057, 'gZ~gUserZ': 0.4570950067064737}
