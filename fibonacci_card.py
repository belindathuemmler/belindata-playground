"""Card image for 'The Golden Ratio Hides in a Pattern': the Fibonacci substitution a -> ab, b -> a,
drawn as rows of long (a, length φ) and short (b, length 1) tiles. Usage: python fibonacci_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654'
PHI = (1 + 5 ** 0.5) / 2

words = ['a']
for _ in range(7):
    words.append(''.join('ab' if c == 'a' else 'a' for c in words[-1]))

W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
total = sum(PHI if c == 'a' else 1 for c in words[-1])
ax.set_xlim(-0.04 * total, 1.32 * total); ax.set_ylim(-0.5, len(words) + 0.6)

h = 0.62
for row, w in enumerate(words):
    y = len(words) - row - 0.5
    x = 0.0
    for c in w:
        L = PHI if c == 'a' else 1.0
        col = TERRA if c == 'a' else PLUM
        ax.add_patch(FancyBboxPatch((x + 0.06, y - h / 2), L - 0.12, h, boxstyle='round,pad=0,rounding_size=0.12',
                                    fc=col, alpha=0.8 if c == 'a' else 0.55, ec='none'))
        x += L
    na, nb = w.count('a'), w.count('b')
    if nb:
        ax.text(1.03 * total, y, f'{na} : {nb} = {na / nb:.3f}', va='center', fontsize=16, color=ROSE, family='serif', style='italic')
ax.text(1.03 * total, -0.15, r'$\rightarrow\ \varphi \approx 1.618$', va='center', fontsize=21, color=TERRA, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok', [len(w) for w in words])
