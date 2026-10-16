"""Card image for 'One for All, All for One: ∀, ∃ and Friends': the four quantifiers as four musketeers,
each with a hat; ∄ stands a little apart, like d'Artagnan. Usage: python quantifiers_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

W, H = 1376, 768
IVORY, ROSE, TERRA, DARK, PLUM, CORAL = '#FAF8F5', '#B77A8A', '#DF7654', '#1F1A1C', '#874C62', '#EE9779'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(IVORY)
ax.axis('off')
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect('equal')


def hat(x, y, scale=1.0, color=PLUM):
    """A musketeer hat: wide brim, soft crown, a feather."""
    ax.add_patch(Ellipse((x, y), 210 * scale, 34 * scale, color=color, zorder=3))
    ax.add_patch(Polygon([(x - 70 * scale, y), (x - 50 * scale, y + 62 * scale), (x + 55 * scale, y + 66 * scale), (x + 72 * scale, y)],
                         closed=True, color=color, zorder=3))
    t = np.linspace(0, 1, 60)
    fx = x + 40 * scale + 120 * scale * t
    fy = y + 60 * scale + 55 * scale * np.sin(np.pi * t) * (1 - 0.3 * t)
    ax.plot(fx, fy, color=CORAL, lw=5 * scale, solid_capstyle='round', zorder=4)


symbols = [(r'$\forall$', 'for all'), (r'$\exists$', 'there is'), (r'$\exists!$', 'exactly one'), (r'$\nexists$', 'none')]
xs = [W * 0.17, W * 0.39, W * 0.61, W * 0.87]       # the fourth stands a little apart
for (sym, word), x in zip(symbols, xs):
    ax.text(x, H * 0.47, sym, ha='center', va='center', fontsize=150, color=DARK)
    hat(x, H * 0.615, 0.9)
    ax.text(x, H * 0.22, word, ha='center', va='center', fontsize=26, family='serif', color=PLUM)

ax.text(W * 0.5, H * 0.09, 'one for all, all for one, exactly one, none', ha='center', va='center', fontsize=24, family='serif', style='italic', color=ROSE)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
