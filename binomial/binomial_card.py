"""Card image for 'The Binomial Formulas Are Pictures':
(a+b)^2 put together, (a-b)^2 cut out with the corner given back, (a+b)(a-b) rearranged.
Usage: python binomial_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SAGE, APRI = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#5B7D54', '#F4C98F'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
a, b = 2.0, 0.75


def panel(x):
    ax = fig.add_axes([x, 0.2, 0.3, 0.62]); ax.axis('off'); ax.set_aspect('equal')
    ax.set_xlim(-0.2, 3.1); ax.set_ylim(-0.35, 3.0)
    return ax


def box(ax, x, y, w, h, fc, alpha=0.85, label=None, fs=19, ec='white'):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=2.5, alpha=alpha))
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha='center', va='center', fontsize=fs, color=DARK)


# 1. (a+b)^2: put the square together
ax = panel(0.03)
box(ax, 0, 0, a, a, CORAL, label='$a^2$', fs=24)
box(ax, a, 0, b, a, APRI, label='$ab$')
box(ax, 0, a, a, b, APRI, label='$ab$')
box(ax, a, a, b, b, ROSE, label='$b^2$')
fig.text(0.18, 0.88, 'put together', ha='center', fontsize=20, color=PLUM, family='serif', style='italic')
fig.text(0.18, 0.08, '$(a+b)^2 = a^2 + 2ab + b^2$', ha='center', fontsize=22, color=DARK)

# 2. (a-b)^2: cut two strips of size a*b away; they overlap in the corner, which was cut twice
ax = panel(0.35)
c = a - b
ax.add_patch(Rectangle((0, 0), a, a, fc='none', ec=PLUM, lw=2, ls='--'))            # the big square a^2
box(ax, 0, 0, c, c, CORAL, label='$(a-b)^2$', fs=21)
ax.add_patch(Rectangle((0, c), a, b, fc=APRI, alpha=0.55, ec='none'))               # top strip  a*b
ax.add_patch(Rectangle((c, 0), b, a, fc=APRI, alpha=0.55, ec='none'))               # right strip a*b
ax.add_patch(Rectangle((c, c), b, b, fc=ROSE, alpha=0.9, ec='white', lw=2.5))      # overlap: cut twice
ax.text(a / 2, a + 0.12, '$-ab$', ha='center', fontsize=17, color=DARK)
ax.text(a + 0.12, a / 2, '$-ab$', va='center', fontsize=17, color=DARK)
ax.text(c + b / 2, c + b / 2, '$+b^2$', ha='center', va='center', fontsize=16, color=DARK)
ax.text(a + 0.12, a + 0.12, 'cut twice,\ngive back once', fontsize=14, color=PLUM, family='serif', style='italic', va='bottom')
fig.text(0.5, 0.88, 'cut away', ha='center', fontsize=20, color=PLUM, family='serif', style='italic')
fig.text(0.5, 0.08, '$(a-b)^2 = a^2 - 2ab + b^2$', ha='center', fontsize=22, color=DARK)

# 3. (a+b)(a-b): cut b^2 out of a^2, move the remaining strip, get a rectangle
ax = panel(0.67)
box(ax, 0, b, a - b, a - b, CORAL)                 # the part that stays
box(ax, a - b, b, b, a - b, APRI)                  # strip that stays in place
box(ax, 0, 0, a - b, b, SAGE, alpha=0.3)           # the strip that is moved ...
ax.add_patch(Rectangle((a - b, 0), b, b, fc='none', ec=ROSE, lw=2, ls='--'))   # the removed b^2
ax.text(a - b / 2, b / 2, '$b^2$', ha='center', va='center', fontsize=16, color=ROSE)
ax.add_patch(Polygon([[a + 0.05, b], [a + 0.05, a], [a + 0.05 + b, a], [a + 0.05 + b, b]], closed=True,
                     fc=SAGE, alpha=0.75, ec='white', lw=2.5))      # ... to here, rotated
ax.annotate('', xy=(a + 0.05 + b / 2, b + 0.05), xytext=(0.6, b / 2),
            arrowprops=dict(arrowstyle='->', color=SAGE, lw=2, connectionstyle='arc3,rad=0.35'))
ax.text((a + 0.05 + b) / 2, a + 0.1, '$a+b$', ha='center', fontsize=17, color=DARK, va='bottom')
fig.text(0.82, 0.88, 'rearranged', ha='center', fontsize=20, color=PLUM, family='serif', style='italic')
fig.text(0.82, 0.08, '$(a+b)(a-b) = a^2 - b^2$', ha='center', fontsize=22, color=DARK)
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
