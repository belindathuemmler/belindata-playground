"""Card image for 'Easy Writing "Mathematisch"': left the scribbled chain x² = 4 = √4 = 2, right the same
solution written as a chain of equivalent statements. Large type, so it stays readable as a small card.
Usage: python math_writing_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

W, H = 1376, 768
IVORY, ROSE, TERRA, DARK, MUTED = '#FAF8F5', '#B77A8A', '#DF7654', '#1F1A1C', '#8A7F82'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
NL = chr(10)

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(IVORY)
ax.axis('off')
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# divider
ax.plot([W / 2, W / 2], [90, H - 90], color=ROSE, lw=2, alpha=0.6)

# headings
ax.text(W * 0.25, H - 95, 'scribbled', ha='center', va='center', fontsize=34, style='italic', family='serif', color=ROSE)
ax.text(W * 0.75, H - 95, 'written', ha='center', va='center', fontsize=34, style='italic', family='serif', color=TERRA)

# left: the chain of equals signs, line by line
left = [(r'$x^2 = 4$', 0.19), (r'$= \sqrt{4}$', 0.24), (r'$= 2$', 0.24)]
for i, (t, xf) in enumerate(left):
    ax.text(W * xf, H * 0.72 - i * 0.16 * H, t, ha='left', va='center', fontsize=40, color=MUTED, family='serif')
caption_left = NL.join(['so $4 = 2$?  And where is $-2$?', 'There is nothing to check,', 'only something to guess.'])
ax.text(W * 0.25, H * 0.145, caption_left, ha='center', va='center', fontsize=25,
        linespacing=1.3, style='italic', family='serif', color=ROSE)

# right: a chain of equivalent statements, one per line
lines = [r'Let $x \in \mathbb{R}$.',
         r'$x^2 = 4$',
         r'$\Leftrightarrow\; x^2 - 4 = 0$',
         r'$\Leftrightarrow\; (x-2)(x+2) = 0$',
         r'$\Leftrightarrow\; x = 2$ or $x = -2$']
x0 = W * 0.56
for i, s in enumerate(lines):
    ax.text(x0, H * 0.76 - i * 0.115 * H, s, ha='left', va='center', fontsize=40, color=DARK, family='serif')
caption_right = NL.join(['every line a statement', 'you can check'])
ax.text(W * 0.75, H * 0.145, caption_right, ha='center', va='center', fontsize=25,
        linespacing=1.3, style='italic', family='serif', color=TERRA)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
