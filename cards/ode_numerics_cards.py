"""Card images for 'The Needle in the ODE Haystack' and 'Two Answers I Owed My Examiner'.
Usage: python ode_numerics_cards.py <output folder>"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C'
W, H = 1376, 768


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
    plt.close(fig)


# 1. ODE: direction field (the haystack) and one solution curve (the needle)
f = lambda x, y: np.sin(x) - 0.4 * y          # y' = sin(x) - 0.4 y
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
ax.set_xlim(-6, 6); ax.set_ylim(-6 * H / W, 6 * H / W)
X, Y = np.meshgrid(np.linspace(-5.8, 5.8, 46), np.linspace(-3.2, 3.2, 25))
S = f(X, Y); L = 0.11 / np.sqrt(1 + S ** 2)
ax.plot(np.array([X - L, X + L]).reshape(2, -1), np.array([Y - L * S, Y + L * S]).reshape(2, -1),
        color=ROSE, lw=1.6, alpha=0.55, solid_capstyle='round')
# solution through (-5.4, 2.3), Runge-Kutta 4
xs = np.linspace(-5.4, 5.8, 1200); ys = [2.3]; h = xs[1] - xs[0]
for x in xs[:-1]:
    y = ys[-1]
    k1 = f(x, y); k2 = f(x + h / 2, y + h / 2 * k1); k3 = f(x + h / 2, y + h / 2 * k2); k4 = f(x + h, y + h * k3)
    ys.append(y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
ax.plot(xs, ys, color=TERRA, lw=4.5)
ax.plot(xs[0], ys[0], 'o', color=PLUM, ms=13)
ax.text(5.6, -3.0, "y' = sin x − 0.4 y", ha='right', fontsize=26, color=PLUM, family='serif',
        bbox=dict(boxstyle='round,pad=0.35', fc=IVORY, ec='none'))
save(fig, 'card_ode.jpg')

# 2. Numerics: operator norm (left) and gradient descent (right)
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
axl = fig.add_axes([0.03, 0.08, 0.44, 0.8]); axr = fig.add_axes([0.53, 0.08, 0.44, 0.8])
for a in (axl, axr):
    a.set_facecolor(IVORY); a.axis('off'); a.set_aspect('equal')
# operator norm: the unit circle and its image under A
A = np.array([[1.6, 0.7], [0.3, 0.9]])
t = np.linspace(0, 2 * np.pi, 300)
circ = np.stack([np.cos(t), np.sin(t)])
img = A @ circ
axl.plot(*circ, color=ROSE, lw=2.5, ls='--')
axl.fill(*img, color=CORAL, alpha=0.18); axl.plot(*img, color=TERRA, lw=3)
U, Sv, Vt = np.linalg.svd(A)
v = U[:, 0] * Sv[0]
if v[0] < 0:
    v = -v
axl.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=PLUM, lw=3))
axl.text(v[0] * 0.5 - 0.35, v[1] * 0.5 + 0.3, r'$\|A\|$', fontsize=30, color=PLUM)
axl.set_xlim(-2.2, 2.2); axl.set_ylim(-1.9, 2.0)
axl.text(0, -1.85, 'operator norm', ha='center', fontsize=24, color=PLUM, family='serif')
# gradient descent on an elongated bowl
F = lambda x, y: 0.5 * (x ** 2 + 6 * y ** 2)
gx, gy = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-1.6, 1.6, 200))
axr.contour(gx, gy, F(gx, gy), levels=8, colors=ROSE, linewidths=1.4, alpha=0.7)
p = np.array([-2.7, 1.2]); path = [p.copy()]
for _ in range(14):
    p = p - 0.28 * np.array([p[0], 6 * p[1]]); path.append(p.copy())
path = np.array(path)
axr.plot(path[:, 0], path[:, 1], '-o', color=TERRA, lw=2.6, ms=6)
axr.plot(0, 0, '*', color=PLUM, ms=20)
axr.set_xlim(-3, 3); axr.set_ylim(-1.7, 1.7)
axr.text(0, -1.95, 'gradient descent', ha='center', fontsize=24, color=PLUM, family='serif')
save(fig, 'card_numerics.jpg')
print('ok')
