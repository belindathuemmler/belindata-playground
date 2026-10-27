"""Card image for 'Who Induces Whom?': the chain inner product -> norm -> metric,
each with the formula by which it induces the next.
Usage: python who_induces_whom_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 13.76); ax.set_ylim(0, 7.68)

boxes = [  # (x centre, name, formula)
    (2.35, 'inner product', r'$\langle x, y\rangle$'),
    (6.88, 'norm', r'$\|x\| = \sqrt{\langle x, x\rangle}$'),
    (11.41, 'metric', r'$d(x, y) = \|x - y\|$'),
]
for cx, name, formula in boxes:
    ax.add_patch(FancyBboxPatch((cx - 1.85, 2.55), 3.7, 2.6, boxstyle='round,pad=0,rounding_size=0.3',
                                fc=CORAL, alpha=0.18, ec='none'))
    ax.add_patch(FancyBboxPatch((cx - 1.85, 2.55), 3.7, 2.6, boxstyle='round,pad=0,rounding_size=0.3',
                                fc='none', ec=PLUM, lw=2.5))
    ax.text(cx, 4.4, name, ha='center', va='center', fontsize=30, color=PLUM, family='serif', style='italic')
    ax.text(cx, 3.3, formula, ha='center', va='center', fontsize=27, color=DARK)
for x0, x1 in [(4.25, 4.98), (8.78, 9.51)]:
    ax.annotate('', xy=(x1, 3.85), xytext=(x0, 3.85), arrowprops=dict(arrowstyle='-|>', color=TERRA, lw=3, mutation_scale=28))
ax.text(6.88, 1.45, 'each one induces the next', ha='center', fontsize=22, color=ROSE, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
