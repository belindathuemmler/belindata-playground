"""Card image for '= or ⇔?': the equals sign connects objects, the equivalence sign connects statements.
Usage: python equals_iff_card.py out.jpg"""
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
ax.plot([5, 5], [0.6, 5.0], color=ROSE, lw=1.5, alpha=0.6)

# left: = between objects
ax.text(2.5, 4.05, r'$=$', ha='center', fontsize=80, color=TERRA)
ax.text(2.5, 3.15, 'connects objects', ha='center', fontsize=24, color=TERRA, family='serif')
ax.text(2.5, 2.05, r'$(x-2)(x+2) = x^2 - 4$', ha='center', fontsize=25, color=DARK)
ax.text(2.5, 1.2, 'two expressions, the same value', ha='center', fontsize=17, color=ROSE, family='serif')

# right: ⇔ between statements
ax.text(7.5, 4.05, r'$\Leftrightarrow$', ha='center', fontsize=80, color=PLUM)
ax.text(7.5, 3.15, 'connects statements', ha='center', fontsize=24, color=PLUM, family='serif')
ax.text(7.5, 2.05, r'$x^2 = 4 \;\Leftrightarrow\; x = 2 \,\vee\, x = -2$', ha='center', fontsize=25, color=DARK)
ax.text(7.5, 1.2, 'two claims, the same truth', ha='center', fontsize=17, color=ROSE, family='serif')
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
