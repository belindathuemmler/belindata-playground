"""Card image for the Reidemeister moves: twist (I), poke (II) and slide (III), each shown as
'before <-> after'. Over-strands get an ivory halo so that the under-strand appears broken.
Usage: python reidemeister_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, TERRA, DARK = '#FAF8F5', '#874C62', '#B77A8A', '#DF7654', '#1F1A1C'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
LW = 4.2


def strand(ax, x, y, col=TERRA, over=False):
    if over:
        ax.plot(x, y, color=IVORY, lw=LW + 9, solid_capstyle='butt', zorder=3)
    ax.plot(x, y, color=col, lw=LW, solid_capstyle='round', zorder=4 if over else 2)


def panel(rect):
    ax = fig.add_axes(rect); ax.axis('off'); ax.set_aspect('equal')
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
    return ax


cols_x = [0.03, 0.36, 0.69]
for k, (name, roman) in enumerate([('twist', 'I'), ('poke', 'II'), ('slide', 'III')]):
    top = panel([cols_x[k], 0.5, 0.28, 0.38])
    bot = panel([cols_x[k], 0.06, 0.28, 0.38])
    fig.text(cols_x[k] + 0.14, 0.9, f'{roman}  ·  {name}', ha='center', fontsize=24, color=PLUM, family='serif')
    fig.text(cols_x[k] + 0.14, 0.465, '⇅', ha='center', va='center', fontsize=26, color=ROSE)

    if k == 0:   # I: a loop in a strand <-> a straight strand
        t = np.linspace(-np.pi, np.pi, 400)
        x, y = 0.38 * (t - 2 * np.sin(t)), 0.45 * (1 - 2 * np.cos(t)) - 0.5
        strand(top, x, y)
        m = (t > 1.55) & (t < 2.25)
        strand(top, x[m], y[m], over=True)
        s = np.linspace(-1.5, 1.5, 50)
        strand(bot, s, np.zeros_like(s))
    elif k == 1:  # II: one strand pushed over another <-> two separate strands
        s = np.linspace(-1.5, 1.5, 300)
        strand(top, np.full_like(s, 0.35), s, col=PLUM)
        strand(top, -0.55 + 1.5 * np.exp(-2.2 * s ** 2), s, over=True)
        strand(bot, np.full_like(s, 0.55), s, col=PLUM)
        strand(bot, -0.55 + 0.2 * np.exp(-2.2 * s ** 2), s)
    else:         # III: a strand slides across a crossing
        s = np.linspace(-1.4, 1.4, 200)
        for ax, hy in [(top, -0.75), (bot, 0.75)]:
            strand(ax, s, s, col=PLUM)
            strand(ax, s, -s, col=ROSE, over=True)
            strand(ax, s, np.full_like(s, hy), over=True)
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
