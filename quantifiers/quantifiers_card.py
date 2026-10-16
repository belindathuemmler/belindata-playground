"""Card image for '∀ and ∃: A Quick Logic Lesson': left ∀ε ∃δ (every ε gets its own δ), right ∃δ ∀ε (one δ for all).
Usage: python quantifiers_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

W, H = 1376, 768
IVORY, ROSE, TERRA, DARK, PLUM = '#FAF8F5', '#B77A8A', '#DF7654', '#1F1A1C', '#874C62'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(IVORY)
ax.axis('off')
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.plot([W / 2, W / 2], [100, H - 100], color=ROSE, lw=2, alpha=0.6)
rows = [H * 0.72 - i * 0.105 * H for i in range(5)]


def arrow(x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=22, lw=2.4, color=TERRA))


# left: ∀ε ∃δ, a different δ for each ε
ax.text(W * 0.25, H - 90, r'$\forall\, \varepsilon\;\; \exists\, \delta$', ha='center', va='center', fontsize=46, color=DARK)
for i, y in enumerate(rows, 1):
    ax.text(W * 0.14, y, r'$\delta_%d$' % i, ha='center', va='center', fontsize=34, color=DARK)
    arrow(W * 0.18, y, W * 0.31, y)
    ax.text(W * 0.36, y, r'$\varepsilon_%d$' % i, ha='center', va='center', fontsize=34, color=DARK)
ax.text(W * 0.25, H * 0.13, 'a different δ for each ε', ha='center', va='center', fontsize=26, family='serif', color=PLUM)

# right: ∃δ ∀ε, one δ for all
ax.text(W * 0.75, H - 90, r'$\exists\, \delta\;\; \forall\, \varepsilon$', ha='center', va='center', fontsize=46, color=DARK)
ax.text(W * 0.64, rows[2], r'$\delta$', ha='center', va='center', fontsize=34, color=DARK)
for i, y in enumerate(rows, 1):
    arrow(W * 0.68, rows[2], W * 0.81, y)
    ax.text(W * 0.86, y, r'$\varepsilon_%d$' % i, ha='center', va='center', fontsize=34, color=DARK)
ax.text(W * 0.75, H * 0.13, 'one δ for all of them', ha='center', va='center', fontsize=26, family='serif', color=PLUM)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
