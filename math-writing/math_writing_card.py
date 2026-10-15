"""Two figures for 'Easy Writing "Mathematisch"'.
  card:    only the scribbled chain x² = 4, = √4, = 2 (card and header image)
  compare: the scribbled chain next to the same solution written as a chain of equivalent statements
  split:   the two halves of 'compare' as separate images out_scribbled.jpg and out_written.jpg
Usage: python math_writing_card.py out.jpg [card|compare|split]"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

W, H = 1376, 768
IVORY, ROSE, TERRA, DARK, MUTED = '#FAF8F5', '#B77A8A', '#DF7654', '#1F1A1C', '#8A7F82'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
NL = chr(10)
mode = sys.argv[2] if len(sys.argv) > 2 else 'card'

fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(IVORY)
ax.axis('off')
ax.set_xlim(0, W)
ax.set_ylim(0, H)

caption_left = NL.join(['so $4 = 2$?  And where is $-2$?', 'There is nothing to check,', 'only something to guess.'])
caption_right = NL.join(['every line a statement', 'you can check'])

if mode == 'card':
    # the scribbled side alone, across the whole image
    left = [(r'$x^2 = 4$', 0.40), (r'$= \sqrt{4}$', 0.47), (r'$= 2$', 0.47)]
    for i, (t, xf) in enumerate(left):
        ax.text(W * xf, H * 0.76 - i * 0.17 * H, t, ha='left', va='center', fontsize=56, color=MUTED, family='serif')
    ax.text(W * 0.5, H * 0.17, 'So $4 = 2$?  And where is $-2$?', ha='center', va='center', fontsize=30,
            linespacing=1.3, family='serif', color=ROSE)
else:
    ax.plot([W / 2, W / 2], [90, H - 90], color=ROSE, lw=2, alpha=0.6)
    ax.text(W * 0.25, H - 95, 'scribbled', ha='center', va='center', fontsize=34, family='serif', color=ROSE)
    ax.text(W * 0.75, H - 95, 'written', ha='center', va='center', fontsize=34, family='serif', color=TERRA)
    left = [(r'$x^2 = 4$', 0.19), (r'$= \sqrt{4}$', 0.24), (r'$= 2$', 0.24)]
    for i, (t, xf) in enumerate(left):
        ax.text(W * xf, H * 0.72 - i * 0.16 * H, t, ha='left', va='center', fontsize=40, color=MUTED, family='serif')
    ax.text(W * 0.25, H * 0.145, caption_left, ha='center', va='center', fontsize=25,
            linespacing=1.3, family='serif', color=ROSE)
    lines = [r'Let $x \in \mathbb{R}$.',
             r'$x^2 = 4$',
             r'$\Leftrightarrow\; x^2 - 4 = 0$',
             r'$\Leftrightarrow\; (x-2)(x+2) = 0$',
             r'$\Leftrightarrow\; x = 2$ or $x = -2$']
    for i, t in enumerate(lines):
        ax.text(W * 0.56, H * 0.76 - i * 0.115 * H, t, ha='left', va='center', fontsize=40, color=DARK, family='serif')
    ax.text(W * 0.75, H * 0.145, caption_right, ha='center', va='center', fontsize=25,
            linespacing=1.3, family='serif', color=TERRA)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
if mode == 'split':
    from PIL import Image
    im = Image.open(sys.argv[1]); stem = sys.argv[1].rsplit('.', 1)[0]
    im.crop((0, 40, W // 2 - 20, H - 20)).save(stem + '_scribbled.jpg', quality=92)
    im.crop((W // 2 + 20, 40, W, H - 20)).save(stem + '_written.jpg', quality=92)
