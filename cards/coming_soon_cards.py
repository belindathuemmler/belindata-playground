"""Card images for the coming-soon projects on belindata.com (isoperimetry, mathematical writing,
text embeddings, me vs. AI). Usage: python coming_soon_cards.py <output folder>"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = sys.argv[1]
W, H = 1376, 768
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SAGE = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#5B7D54'


def canvas(xlim, ylim=None):
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    fig.patch.set_facecolor(IVORY)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(IVORY)
    ax.axis('off')
    ax.set_xlim(*xlim)
    if ylim is None:
        half = (xlim[1] - xlim[0]) * H / W / 2
        ylim = (-half, half)
    ax.set_ylim(*ylim)
    ax.set_aspect('equal')
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=100, facecolor=fig.get_facecolor(), pil_kwargs={'quality': 92})
    plt.close(fig)


# 1. Isoperimetry: three fences of the same length 2π; the circle encloses the most area
fig, ax = canvas((-5.4, 5.4))
L = 2 * np.pi
w_thin = 2.9
rgba = lambda c, a: (*matplotlib.colors.to_rgb(c), a)
shapes = [(-3.4, w_thin, L / 2 - w_thin, ROSE), (0.0, L / 4, L / 4, CORAL)]
for cx, w, h, col in shapes:
    ax.add_patch(plt.Rectangle((cx - w / 2, -h / 2), w, h, fc=rgba(col, 0.3), ec=col, lw=3.5))
    ax.text(cx, -1.65, f'area {w * h:.2f}', ha='center', fontsize=30, color=col, family='serif')
ax.add_patch(plt.Circle((3.4, 0), 1.0, fc=rgba(TERRA, 0.3), ec=TERRA, lw=4))
ax.text(3.4, -1.65, f'area {np.pi:.2f}', ha='center', fontsize=30, color=TERRA, family='serif', weight='bold')
ax.text(0, 1.7, r'every fence has length $2\pi$', ha='center', fontsize=30, color=PLUM, family='serif')
save(fig, 'card_isoperimetric.jpg')

# 2. Mathematical writing: a typical first-semester answer next to the same answer written as mathematics
fig, ax = canvas((0, 10), (0, 10 * H / W))
ax.plot([5, 5], [0.6, 5.0], color=ROSE, lw=1.5, alpha=0.6)
# left: a chain of equals signs that claims 4 = 2 and forgets -2
ax.text(2.5, 4.55, 'scribbled', ha='center', fontsize=21, color=ROSE, family='serif', style='italic')
for k, line in enumerate([r'$x^2 = 4$', r'$\ \ \ \ \ = \sqrt{4}$', r'$\ \ \ \ \ = 2$']):
    ax.text(1.3, 3.55 - 0.85 * k, line, fontsize=30, color='#8A7F84', family='serif')
ax.plot([0.9, 4.2], [1.05, 4.0], color=ROSE, lw=3, alpha=0.75)
ax.text(2.5, 0.85, r'so $4 = 2$ ?  and $-2$ ?', ha='center', fontsize=19, color=ROSE, family='serif', style='italic')
# right: a sentence that states something you can check
ax.text(7.5, 4.55, 'written', ha='center', fontsize=21, color=TERRA, family='serif', style='italic')
ax.text(5.5, 3.55, r'Let $x \in \mathbb{R}$ with $x^2 = 4$.', fontsize=26, color=DARK, family='serif')
ax.text(5.5, 2.7, r'Then $(x-2)(x+2) = 0$,', fontsize=26, color=DARK, family='serif')
ax.text(5.5, 1.85, r'so $x = 2$ or $x = -2$.', fontsize=26, color=DARK, family='serif')
ax.text(7.5, 0.85, 'a statement you can check', ha='center', fontsize=19, color=TERRA, family='serif', style='italic')
save(fig, 'card_math_writing.jpg')

# 3. Text embeddings: questions as points; similar meanings lie close together
fig, ax = canvas((-5, 5))
points = [((-3.3, 1.2), PLUM, 'refund?'), ((-2.2, 1.75), PLUM, 'money back'), ((-3.5, 0.3), PLUM, 'return an item'),
          ((2.0, 1.6), SAGE, 'opening hours'), ((2.6, 0.9), SAGE, 'when are you open'),
          ((2.0, -0.9), ROSE, 'delivery time'), ((2.6, -1.7), ROSE, 'how long is shipping')]
for (x, y), col, wd in points:
    ax.plot(x, y, 'o', ms=13, color=col, alpha=0.9)
    ax.text(x + 0.22, y + 0.1, wd, fontsize=18, color=col, family='serif', style='italic')
q = np.array([-2.5, -0.6])
ax.plot(*q, '*', ms=26, color=TERRA)
ax.text(q[0] + 0.3, q[1] - 0.5, '"can I get my money returned?"', fontsize=18, color=TERRA, family='serif', style='italic')
ax.add_patch(plt.Circle((-2.9, 0.7), 1.65, fc='none', ec=TERRA, lw=1.6, ls='--', alpha=0.7))
save(fig, 'card_embeddings.jpg')

# 4. Me vs. AI: the same analysis, two curves of quality over time
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0.12, 0.16, 0.78, 0.72])
ax.set_facecolor(IVORY)
t = np.linspace(0, 10, 300)
me = 1 - np.exp(-0.32 * t)
ai = 0.78 * (1 - np.exp(-2.2 * t)) + 0.04 * np.sin(1.4 * t) * np.exp(-0.15 * t)
ax.plot(t, me, color=PLUM, lw=3.4)
ax.plot(t, ai, color=TERRA, lw=3.4)
ax.text(8.6, me[-1] + 0.05, 'me', color=PLUM, fontsize=22, family='serif', style='italic')
ax.text(8.6, ai[-1] - 0.12, 'AI', color=TERRA, fontsize=22, family='serif', style='italic')
for side in ['top', 'right']:
    ax.spines[side].set_visible(False)
for side in ['left', 'bottom']:
    ax.spines[side].set_color(ROSE)
    ax.spines[side].set_linewidth(1.5)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('time', fontsize=19, color=PLUM, family='serif', style='italic')
ax.set_ylabel('insight', fontsize=19, color=PLUM, family='serif', style='italic')
ax.text(5, 1.12, '?', fontsize=34, color=TERRA, ha='center', family='serif')
ax.set_ylim(0, 1.2)
save(fig, 'card_me_vs_ai.jpg')
print('ok')
