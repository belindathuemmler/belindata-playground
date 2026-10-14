"""Card image for 'Eigenvalues, Finally Explained': left, a matrix bends most directions but only stretches
its eigenvectors; right, what the eigenvalue does to the solution e^(λt) of an ODE. Usage: python eigenvalues_card.py out.jpg"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SAGE = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#5B7D54'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
axl = fig.add_axes([0.03, 0.06, 0.44, 0.86]); axr = fig.add_axes([0.52, 0.16, 0.27, 0.7])
for a in (axl, axr):
    a.set_facecolor(IVORY)

# left: vectors v (grey) and Av (coloured); eigenvectors stay on their line
A = np.array([[2.0, 1.0], [1.0, 2.0]])          # eigenvalues 3 and 1, eigenvectors (1,1), (1,-1)
axl.axis('off'); axl.set_aspect('equal'); axl.set_xlim(-3.4, 3.4); axl.set_ylim(-3.2, 3.6)
# a few ordinary vectors: v (light) and Av (coral) both drawn from the origin, Av points somewhere else
for ang in np.radians([15, 75, 120, 160, 200, 255, 290, 340]):
    v = np.array([np.cos(ang), np.sin(ang)])
    axl.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=ROSE, lw=1.6, alpha=0.7))
    axl.annotate('', xy=A @ v, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=CORAL, lw=1.4, alpha=0.4))
for d, lam, col in [(np.array([1, 1]) / np.sqrt(2), 3, TERRA), (np.array([1, -1]) / np.sqrt(2), 1, PLUM)]:
    axl.plot([-3.3 * d[0], 3.3 * d[0]], [-3.3 * d[1], 3.3 * d[1]], color=col, lw=1.2, ls='--', alpha=0.6)
    axl.annotate('', xy=lam * d, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=col, lw=3.4))
axl.text(2.25, 2.55, r'$\lambda = 3$', fontsize=26, color=TERRA)
axl.text(0.85, -1.15, r'$\lambda = 1$', fontsize=26, color=PLUM)
axl.text(0, 3.25, r'$Av = \lambda v$', ha='center', fontsize=30, color=DARK)

# right: what λ does to a solution x(t) = e^{λt}
t = np.linspace(0, 6, 400)
axr.plot(t, np.exp(0.35 * t), color=TERRA, lw=3.4)
axr.plot(t, 3 * np.exp(-0.7 * t), color=PLUM, lw=3.4)
axr.plot(t, 2.2 * np.exp(-0.15 * t) * np.cos(2.6 * t), color=SAGE, lw=3.0)
axr.axhline(0, color=ROSE, lw=1, alpha=0.6)
axr.text(6.15, np.exp(0.35 * 6) - 0.4, r'$\lambda > 0$: grows', fontsize=19, color=TERRA, va='center')
axr.text(6.15, 0.55, r'$\lambda < 0$: fades', fontsize=19, color=PLUM, va='center')
axr.text(6.15, -1.2, r'complex $\lambda$: swings', fontsize=19, color=SAGE, va='center')
axr.set_xlim(0, 6); axr.set_ylim(-2.4, 8.4)
for side in ['top', 'right', 'bottom', 'left']:
    axr.spines[side].set_visible(False)
axr.set_xticks([]); axr.set_yticks([])
axr.set_title(r"$x' = \lambda x \;\Rightarrow\; x(t) = e^{\lambda t}$", fontsize=24, color=DARK, pad=14)
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
