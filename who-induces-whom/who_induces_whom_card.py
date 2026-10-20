"""Card image for 'Who Induces Whom?':
the chain inner product -> norm -> metric -> topology -> measure, and the unit balls of the
1-, 2- and max-norm; only the circle comes from an inner product.
Usage: python who_induces_whom_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, APRI = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#F4C98F'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)

# The chain along the top: each structure induces the next one
chain = ['inner product', 'norm', 'metric', 'topology', 'measure']
fig.text(0.5, 0.87, '   →   '.join(chain), ha='center', va='center', fontsize=23, color=PLUM, family='serif', style='italic')


def shape(ax, patch_cls, *args, fc, ec, lw=3):
    ax.add_patch(patch_cls(*args, fc=fc, alpha=0.45, ec='none'))   # transparent fill
    ax.add_patch(patch_cls(*args, fc='none', ec=ec, lw=lw))         # solid outline


def panel(x):
    ax = fig.add_axes([x, 0.2, 0.28, 0.52]); ax.axis('off'); ax.set_aspect('equal')
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35)
    ax.axhline(0, color=ROSE, lw=1, alpha=0.5); ax.axvline(0, color=ROSE, lw=1, alpha=0.5)
    return ax


# Unit balls: diamond (1-norm), circle (2-norm), square (max-norm)
ax = panel(0.04)
shape(ax, Polygon, [[1, 0], [0, 1], [-1, 0], [0, -1]], fc=APRI, ec=TERRA)
fig.text(0.18, 0.1, r'$\|x\|_1 = |x_1| + |x_2|$', ha='center', fontsize=21, color=DARK)

ax = panel(0.36)
shape(ax, Circle, (0, 0), 1, fc=CORAL, ec=PLUM, lw=4)
ax.text(0, 0.42, r'$\langle x, y\rangle$', ha='center', va='center', fontsize=24, color=PLUM)
fig.text(0.5, 0.1, r'$\|x\|_2 = \sqrt{\langle x, x\rangle}$', ha='center', fontsize=21, color=DARK)

ax = panel(0.68)
shape(ax, Polygon, [[1, 1], [-1, 1], [-1, -1], [1, -1]], fc=APRI, ec=TERRA)
fig.text(0.82, 0.1, r'$\|x\|_\infty = \max\{|x_1|, |x_2|\}$', ha='center', fontsize=21, color=DARK)

fig.text(0.5, 0.76, 'only the circle comes from an inner product', ha='center', fontsize=17, color=ROSE, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
