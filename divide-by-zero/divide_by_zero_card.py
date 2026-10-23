"""Card image for 'Never Divide by Zero!': the classic 'proof' that 2 = 1, with the hidden division by zero.
Usage: python divide_by_zero_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, TERRA, DARK = '#FAF8F5', '#874C62', '#B77A8A', '#DF7654', '#1F1A1C'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
ax.set_xlim(0, 10); ax.set_ylim(0, 10 * H / W)

steps = [r'$a = b$', r'$a^2 = ab$', r'$a^2 - b^2 = ab - b^2$', r'$(a+b)(a-b) = b(a-b)$', r'$a + b = b$', r'$2b = b$', r'$2 = 1$']
y0, dy = 4.45, 0.62
ax.text(3.6, y0 + 0.72, r'Let $a, b \in \mathbb{R}$ with', ha='center', fontsize=22, color=DARK, family='serif')
for k, st in enumerate(steps):
    col = TERRA if k == len(steps) - 1 else DARK
    ax.text(3.6, y0 - k * dy, st, ha='center', fontsize=25, color=col, family='serif')
    if k < len(steps) - 1:   # the sign sits on the line it introduces: equivalences, all but one
        ax.text(1.5, y0 - (k + 1) * dy, r'$\Leftrightarrow$', ha='center', fontsize=32, color=TERRA if k == 3 else DARK, family='serif')
# the forbidden step
ax.annotate('', xy=(5.55, y0 - 4 * dy + 0.18), xytext=(5.55, y0 - 3 * dy + 0.05),
            arrowprops=dict(arrowstyle='->', color=TERRA, lw=2.4))
ax.text(5.8, y0 - 3.55 * dy + 0.1, r'$\div\,(a-b)$', fontsize=24, color=TERRA, family='serif')
ax.text(5.8, y0 - 4.25 * dy + 0.1, r'but $a - b = 0$ !', fontsize=22, color=TERRA, family='serif', style='italic')
ax.text(4.75, y0 - 6 * dy + 0.05, '→  zero points', ha='left', fontsize=22, color=ROSE, family='serif', style='italic')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
