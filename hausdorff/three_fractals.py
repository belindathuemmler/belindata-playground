"""Three fractals between the dimensions, side by side: the Cantor set (dim log 2 / log 3), the Menger sponge
(dim log 20 / log 3) and the Sierpinski triangle (dim log 3 / log 2). Usage: python three_fractals.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

out = sys.argv[1]
IVORY, DARK, PLUM, TERRA, APRICOT, SAGE, CORAL = '#FAF8F5', '#1F1A1C', '#874C62', '#DF7654', '#F4C98F', '#ACAA91', '#EE9779'

fig = plt.figure(figsize=(13.76, 5.2), dpi=100)
fig.patch.set_facecolor(IVORY)

# ---------- 1. Cantor set: levels 0..5 as bars
ax = fig.add_axes([0.03, 0.16, 0.28, 0.76]); ax.set_facecolor(IVORY); ax.axis('off')
intervals = [(0.0, 1.0)]
for level in range(6):
    for a, b in intervals:
        ax.add_patch(Rectangle((a, 5 - level), b - a, 0.55, color=PLUM))
    ax.text(-0.03, 5 - level + 0.27, f'{level}', ha='right', va='center', fontsize=9, color=DARK, family='monospace')
    intervals = [iv for a, b in intervals for iv in ((a, a + (b - a) / 3), (b - (b - a) / 3, b))]
ax.set_xlim(-0.12, 1.02); ax.set_ylim(-0.6, 5.9)

# ---------- 2. Menger sponge, level 2, as voxels
def menger(level):
    n = 3 ** level
    keep = np.ones((n, n, n), dtype=bool)
    for lv in range(level):
        s = 3 ** lv                      # size of the block removed at this level, in voxels... iterate over coordinates
    idx = np.indices((n, n, n))
    for lv in range(1, level + 1):
        d = 3 ** (level - lv)            # voxel size of a level-lv cell
        c = (idx // d) % 3               # position of the cell inside its parent, per axis
        middle = (c == 1).sum(axis=0)    # number of axes in which the cell is the middle one
        keep &= middle < 2
    return keep

vox = menger(2)
ax = fig.add_axes([0.68, 0.10, 0.31, 0.88], projection='3d'); ax.set_facecolor(IVORY)
ax.voxels(vox, facecolors=TERRA, edgecolor=DARK, linewidth=0.25, alpha=0.95)
ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=24, azim=-55); ax.set_axis_off()

# ---------- 3. Sierpinski triangle, level 6
def sierpinski(level):
    tris = [np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3) / 2]])]
    for _ in range(level):
        nxt = []
        for t in tris:
            a, b, c = t
            ab, bc, ca = (a + b) / 2, (b + c) / 2, (c + a) / 2
            nxt += [np.array([a, ab, ca]), np.array([ab, b, bc]), np.array([ca, bc, c])]
        tris = nxt
    return tris

ax = fig.add_axes([0.36, 0.16, 0.29, 0.76]); ax.set_facecolor(IVORY); ax.axis('off'); ax.set_aspect('equal')
for t in sierpinski(5):
    ax.add_patch(Polygon(t, closed=True, color='#5B7D54', lw=0))
ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.12, 0.95)

for x, label in ((0.17, 'Cantor set'), (0.505, 'Sierpiński triangle'), (0.835, 'Menger sponge')):
    fig.text(x, 0.07, label, ha='center', va='center', fontsize=14, color=DARK, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
