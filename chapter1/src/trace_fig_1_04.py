"""Trace the four mode shapes of the original Figure 1.4 from its picture.

The original is a MATLAB plot of the authors' rotor model; its data are not in
the repository, only the picture embedded in incoming/Chapter_1_final.docx.
This script recovers the curves from that picture so the figure can be redrawn
in the house style. Replace data/fig_1_04_modes.csv with the model's own output
when it is available; nothing else needs to change.

The rotor is drawn in translucent patches over the curves. A curve seen
through a patch is p = a*C + (1-a)*L, the patch alone is a*C + (1-a)*W, so the
difference from the local background is always parallel to L - W, whatever
the patch. Each pixel is given to the mode colour that explains it best, and
each curve is then followed column by column from a seed point.

usage:  python3 src/trace_fig_1_04.py      (run from chapter1/)
"""
import io
import zipfile

import numpy as np
from PIL import Image
from scipy.interpolate import UnivariateSpline
from scipy.ndimage import label, median_filter

SRC, MEDIA = 'incoming/Chapter_1_final.docx', 'word/media/image4.png'
OUT = 'data/fig_1_04_modes.csv'
X0, PXM, YC = 8.0, 640.0, 257.5            # px of 0 m, px per metre (ticks 0 to 2 m), rotor axis
L_ROTOR = 2.1406                           # m, the right edge of the plot
MODES = {1: (0, 114, 189), 2: (217, 83, 25), 3: (237, 177, 32), 4: (126, 47, 142)}
FREQ = {1: 55.9, 2: 293.0, 3: 590.1, 4: 905.8}   # Hz, from the original legend
SEEDS = {1: (60, 349), 2: (30, 80), 3: (30, 50), 4: (60, 420)}   # px, clear of crossings
# Columns where the model's own drawing lies over the curves and pulls the trace
# off them: the red bearing discs with their crossed lines, and the AMB sensor
# and actuator lines (m). The curves are bridged across these by the spline.
SKIP = [(0.168, 0.195), (1.408, 1.437), (2.004, 2.034)] + \
       [(z - 0.007, z + 0.007) for z in (0.197, 0.290, 1.225, 1.313, 1.820, 1.930)]


def scores(im):
    bg = np.stack([median_filter(im[..., k], size=11) for k in range(3)], -1)
    d = im - bg
    dn = np.linalg.norm(d, axis=-1)
    res, ts = [], []
    for c in MODES.values():
        v = np.array(c, float) - 255.0
        t = np.clip((d @ v) / (v @ v), 0, None)          # fraction of the full line colour
        res.append(np.linalg.norm(d - t[..., None] * v, axis=-1))
        ts.append(t)
    res, ts = np.array(res), np.array(ts)
    best, second = np.argmin(res, axis=0), np.sort(res, axis=0)[1]
    out = {}
    for i, k in enumerate(MODES):
        ok = (best == i) & (res[i] < 18 + 0.12 * dn) & (res[i] < 0.6 * second)
        out[k] = np.where(ok, ts[i], 0)
    return out


def trace(score, seed):
    H, W = score.shape
    mask = np.zeros((H, W), bool)
    mask[365:505, 530:840] = True                       # the legend box
    mask[140:175, 10:80] = mask[140:175, 1285:1345] = True   # 'NDE', 'DE'

    def candidates(x):
        col = np.where(mask[:, x], 0, score[:, x])
        lab, n = label(col > 0.30)
        found = []
        for i in range(1, n + 1):
            ys = np.nonzero(lab == i)[0]
            if len(ys) <= 14:                           # longer runs are vertical strokes
                found.append(float((ys * col[ys]).sum() / col[ys].sum()))
        return found

    x0 = seed[0]
    y0 = min(candidates(x0), key=lambda y: abs(y - seed[1]))
    pts = {x0: y0}
    for step in (1, -1):
        hist, x, miss = [(x0, y0)], x0, 0
        while 0 <= x + step < W and miss <= 40:
            x += step
            if len(hist) >= 12:                         # extrapolate the last dozen points
                hx = np.array([h[0] for h in hist[-12:]], float) - x
                hy = np.array([h[1] for h in hist[-12:]])
                pred = np.polyfit(hx, hy, 2 if miss < 8 else 1)[-1]
            else:
                pred = hist[-1][1]
            near = [y for y in candidates(x) if abs(y - pred) < 6 + 3 * miss]
            if near:
                y = min(near, key=lambda y: abs(y - pred))
                pts[x] = y; hist.append((x, y)); miss = 0
            else:
                miss += 1
    xs = np.array(sorted(pts), float)
    return (xs - X0) / PXM, (YC - np.array([pts[x] for x in sorted(pts)])) / PXM


def main():
    raw = zipfile.ZipFile(SRC).read(MEDIA)
    im = np.asarray(Image.open(io.BytesIO(raw)).convert('RGB')).astype(float)
    sc = scores(im)
    grid = np.round(np.arange(0, L_ROTOR + 1e-9, 0.0025), 4)
    cols = [grid]
    for k in MODES:
        x, y = trace(sc[k], SEEDS[k])
        keep = (x >= 0) & (x <= L_ROTOR)                # drop strays beyond the plot
        for a, b in SKIP:
            keep &= ~((x > a) & (x < b))
        x, y = x[keep], y[keep]
        med = np.array([np.median(y[max(0, i - 6):i + 7]) for i in range(len(y))])
        ok = np.abs(y - med) < 1.5 / PXM                 # a crossing that pulled a point off
        x, y = x[ok], y[ok]
        # a smoothing spline at the pixel noise level: it keeps the kinks of the
        # original polyline sharp to within a pixel or two
        spl = UnivariateSpline(x, y, k=3, s=len(x) * (0.45 / PXM) ** 2)
        rms = np.sqrt(np.mean((spl(x) - y) ** 2)) * PXM
        y = spl(grid)
        cols.append(y / np.abs(y).max())               # unit maximum deflection
        print(f'mode {k}: {len(x)} columns used, spline within {rms:.2f} px rms')
    head = ('# Lateral bending mode shapes of the rotor of Figure 1.4, each normalised to '
            'unit maximum deflection.\n'
            '# TRACED from the picture of the original MATLAB figure by '
            'src/trace_fig_1_04.py, not exported from the model.\n'
            '# Natural frequencies (Hz): ' + ', '.join(f'mode {k} {f:g}' for k, f in FREQ.items())
            + '\nz_m,mode1,mode2,mode3,mode4')
    np.savetxt(OUT, np.column_stack(cols), delimiter=',', fmt='%.5f', header=head, comments='')
    print(f'wrote {OUT}')


if __name__ == '__main__':
    main()
