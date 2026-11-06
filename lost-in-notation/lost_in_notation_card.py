"""Card image for 'Lost in Notation: A Mathematician Reads Physics': one vector written twice, as the column vector (0, 1) the way I write it and as the qubit state |1> the way physicists do. Needs the Windows font Segoe Script for the handwritten remark (any script font will do).
Usage: python lost_in_notation_card.py out.jpg"""
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

# one example only: the second basis vector of C^2, which physicists call the qubit state |1>
XL, XM, XR = 2.7, 5.0, 7.3
Y = 3.2   # no column headings: left my way of writing it, right the physicists'
ax.text(XL, Y, r'$\binom{0}{1}$', ha='center', va='center', fontsize=150, color=DARK, family='serif')   # binom draws the column vector (0, 1); it sets its entries small, hence the larger size
ax.text(XM, Y, r'$\leftrightarrow$', ha='center', va='center', fontsize=70, color=ROSE, family='serif')
ax.text(XR, Y, r'$|1\rangle$', ha='center', va='center', fontsize=110, color=DARK, family='serif')
ax.text(XM, 0.62, 'the same thing?!', ha='center', fontsize=46, color=ROSE, family='Segoe Script')   # handwriting, like a note in the margin
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
