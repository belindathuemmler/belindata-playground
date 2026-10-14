"""Steiner symmetrization of a planar shape: every vertical chord is slid until its midpoint
lies on the horizontal axis. Area stays the same, the boundary gets shorter.
Usage: python steiner_symmetrization.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654'

# An irregular, vertically convex blob
th = np.linspace(0, 2 * np.pi, 2000)
r = 1 + 0.22 * np.cos(2 * th + 0.6) + 0.12 * np.sin(3 * th) + 0.06 * np.cos(5 * th)
X, Y = r * np.cos(th), 0.75 * r * np.sin(th) + 0.25 * np.cos(th) ** 2

def chord(x):
    """Lower and upper end of the vertical chord at position x."""
    ys = []
    for i in range(len(X) - 1):
        x0, x1 = X[i], X[i + 1]
        if (x0 - x) * (x1 - x) <= 0 and x0 != x1:
            ys.append(Y[i] + (x - x0) / (x1 - x0) * (Y[i + 1] - Y[i]))
    return (min(ys), max(ys)) if len(ys) >= 2 else None

xs = np.linspace(X.min() + 1e-3, X.max() - 1e-3, 400)
chords = [(x, chord(x)) for x in xs]
chords = [(x, c) for x, c in chords if c]
half = np.array([(c[1] - c[0]) / 2 for _, c in chords])
xc = np.array([x for x, _ in chords])

def length(px, py):
    return np.sum(np.hypot(np.diff(px), np.diff(py)))

W, H = 1376, 640
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
ax.set_aspect('equal')
shift = 3.7
ax.set_xlim(-1.7, shift + 1.7); ax.set_ylim(-1.45, 1.35)

# left: original shape with some of its chords
ax.fill(X, Y, color=ROSE, alpha=0.18); ax.plot(X, Y, color=ROSE, lw=2.6)
# right: symmetrized shape
sx = np.concatenate([xc, xc[::-1]]) + shift
sy = np.concatenate([half, -half[::-1]])
ax.fill(sx, sy, color=TERRA, alpha=0.2); ax.plot(np.append(sx, sx[0]), np.append(sy, sy[0]), color=TERRA, lw=2.6)
ax.plot([shift - 1.45, shift + 1.45], [0, 0], color=PLUM, lw=1.2, ls='--', alpha=0.6)
for k in range(12, len(chords), 30):
    x, (lo, hi) = chords[k]
    ax.plot([x, x], [lo, hi], color=PLUM, lw=1.6, alpha=0.75)
    ax.plot([x + shift, x + shift], [-half[k], half[k]], color=PLUM, lw=1.6, alpha=0.75)
ax.annotate('', xy=(shift - 1.5, 0.95), xytext=(1.25, 0.95), arrowprops=dict(arrowstyle='->', color=TERRA, lw=2.4))
ax.text((shift) / 2, 1.1, 'slide every chord to the middle', ha='center', fontsize=17, color=TERRA, family='serif', style='italic')
L0, L1 = length(np.append(X, X[0]), np.append(Y, Y[0])), length(np.append(sx, sx[0]), np.append(sy, sy[0]))
ax.text(0, -1.32, f'boundary {L0:.2f}', ha='center', fontsize=17, color=ROSE, family='serif', style='italic')
ax.text(shift, -1.32, f'boundary {L1:.2f}, same area', ha='center', fontsize=17, color=TERRA, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('boundary', round(L0, 3), '->', round(L1, 3))
