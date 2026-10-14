"""Card image for 'True Mathematicians by Heart': the tutor's implication and its contraposition.
Usage: python true_mathematicians_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, ROSE, DARK = '#FAF8F5', '#B77A8A', '#1F1A1C'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
ax.set_xlim(0, 10); ax.set_ylim(0, 10 * H / W)

ax.text(5, 4.45, 'the tutor', ha='center', fontsize=24, color=ROSE, family='serif', style='italic')
ax.text(5, 3.6, r'true mathematician  $\Rightarrow$  sees it by heart', ha='center', fontsize=36, color=DARK, family='serif')
ax.text(5, 2.4, 'contraposition', ha='center', fontsize=24, color=ROSE, family='serif', style='italic')
ax.text(5, 1.55, r'writes it out  $\Rightarrow$  no true mathematician', ha='center', fontsize=36, color=DARK, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
