"""Card images for 'Open the Shell. Which Shell?' and 'What Is an API?'.
Usage: python shell_api_cards.py <output folder>"""
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SAGE = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#5B7D54'
W, H = 1376, 768


def canvas():
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    fig.patch.set_facecolor(IVORY)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor(IVORY); ax.axis('off')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10 * H / W); ax.set_aspect('equal')
    return fig, ax


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
    plt.close(fig)


# 1. Two shells: the system shell, and the Python shell started inside it
fig, ax = canvas()
ax.add_patch(FancyBboxPatch((0.6, 0.75), 7.0, 4.0, boxstyle='round,pad=0,rounding_size=0.25', fc='#241D20', ec='none'))
ax.add_patch(FancyBboxPatch((0.6, 4.35), 7.0, 0.4, boxstyle='round,pad=0,rounding_size=0.25', fc='#3A2F33', ec='none'))
for k, c in enumerate([TERRA, '#F4C98F', SAGE]):
    ax.add_patch(plt.Circle((0.95 + 0.3 * k, 4.55), 0.08, color=c))
mono = dict(family='monospace', fontsize=21)
lines = [
    ('C:\\Users\\me> ', CORAL, 'python', '#FFFFFF', 3.75),
    ('>>> ', '#9FD3A8', '2 + 3', '#FFFFFF', 2.85),
    ('', None, '5', '#FFFFFF', 2.25),
    ('>>> ', '#9FD3A8', 'exit()', '#FFFFFF', 1.65),
    ('C:\\Users\\me> ', CORAL, '', '#FFFFFF', 1.05),
]
for prompt, pc, cmd, cc, y in lines:
    t = ax.text(1.0, y, prompt, color=pc or '#FFFFFF', **mono)
    fig.canvas.draw()
    x1 = t.get_window_extent().transformed(ax.transData.inverted()).x1 if prompt else 1.0
    ax.text(x1, y, cmd, color=cc, **mono)
ax.text(7.95, 3.8, 'system shell', color=TERRA, fontsize=17, family='serif', style='italic')
ax.text(7.95, 2.3, 'Python shell', color=SAGE, fontsize=17, family='serif', style='italic')
ax.plot([7.8, 7.8], [1.55, 3.15], color=SAGE, lw=2)
ax.text(4.1, 5.05, 'Open the shell. Which one?', ha='center', fontsize=22, color=PLUM, family='serif', style='italic')
save(fig, 'card_shell.jpg')

# 2. API: the menu between you and the kitchen
fig, ax = canvas()
boxes = [(0.6, 'you', '(one program)', ROSE), (3.85, 'the menu', '= the API', TERRA), (7.1, 'the kitchen', '(another program)', PLUM)]
for x, title, sub, col in boxes:
    ax.add_patch(FancyBboxPatch((x, 2.0), 2.3, 1.6, boxstyle='round,pad=0,rounding_size=0.25', fc=col, alpha=0.15, ec=col, lw=2.4))
    ax.text(x + 1.15, 3.0, title, ha='center', fontsize=23, color=col, family='serif', style='italic', weight='bold')
    ax.text(x + 1.15, 2.45, sub, ha='center', fontsize=16, color=col, family='serif', style='italic')
for (x0, x1, y, label) in [(2.95, 3.8, 3.15, 'order'), (6.2, 7.05, 3.15, 'request'), (7.05, 6.2, 2.45, 'dish'), (3.8, 2.95, 2.45, 'response')]:
    ax.annotate('', xy=(x1, y), xytext=(x0, y), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.8, alpha=0.7))
ax.text(3.37, 3.3, 'order', ha='center', fontsize=14, color=DARK, alpha=0.7, family='serif', style='italic')
ax.text(6.62, 3.3, 'request', ha='center', fontsize=14, color=DARK, alpha=0.7, family='serif', style='italic')
ax.text(3.37, 2.1, 'dish', ha='center', fontsize=14, color=DARK, alpha=0.7, family='serif', style='italic')
ax.text(6.62, 2.1, 'response', ha='center', fontsize=14, color=DARK, alpha=0.7, family='serif', style='italic')
ax.text(5.0, 4.6, 'you never have to enter the kitchen', ha='center', fontsize=21, color=PLUM, family='serif', style='italic')
save(fig, 'card_api.jpg')
print('ok')
