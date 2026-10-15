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
    ax.text(W * 0.5, H * 0.17, 'So $4 = 2$?  And where is $-2$?', ha='center', va='center', fontsize=40,
            linespacing=1.3, family='serif', color='#874C62')
else:
    # compare: poster-sized type. split: one small type size for everything, matching the labels of the
    # small diagrams in the article (the halves are cropped to their content afterwards)
    if mode == 'split':
        fh = ff = fc = 18; step = 0.075 * H
    else:
        fh, ff, fc = 34, 40, 25; step = 0.16 * H
    ax.plot([W / 2, W / 2], [90, H - 90], color=ROSE, lw=2, alpha=0.6)
    ax.text(W * 0.25, H - 95, 'scribbled', ha='center', va='center', fontsize=fh, family='serif', color=ROSE)
    ax.text(W * 0.75, H - 95, 'written', ha='center', va='center', fontsize=fh, family='serif', color=TERRA)
    y0 = H - 95 - 1.6 * step
    left = [(r'$x^2 = 4$', 0.19), (r'$= \sqrt{4}$', 0.24), (r'$= 2$', 0.24)]
    for i, (t, xf) in enumerate(left):
        ax.text(W * xf, y0 - i * step, t, ha='left', va='center', fontsize=ff, color=MUTED, family='serif')
    lines = [r'Let $x \in \mathbb{R}$.',
             r'$x^2 = 4$',
             r'$\Leftrightarrow\; x^2 - 4 = 0$',
             r'$\Leftrightarrow\; (x-2)(x+2) = 0$',
             r'$\Leftrightarrow\; x = 2$ or $x = -2$']
    rstep = step   # same line spacing on both sides
    for i, t in enumerate(lines):
        ax.text(W * 0.56, y0 - i * rstep, t, ha='left', va='center', fontsize=ff, color=DARK, family='serif')
    ycap = y0 - 4 * rstep - 1.9 * step
    ax.text(W * 0.25, ycap, caption_left, ha='center', va='center', fontsize=fc, linespacing=1.3, family='serif', color=ROSE)
    ax.text(W * 0.75, ycap, caption_right, ha='center', va='center', fontsize=fc, linespacing=1.3, family='serif', color=TERRA)

fig.savefig(sys.argv[1], dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
if mode == 'split':
    from PIL import Image
    from PIL import ImageChops
    im = Image.open(sys.argv[1]).convert('RGB'); stem = sys.argv[1].rsplit('.', 1)[0]
    halves = [im.crop((0, 0, W // 2 - 20, H)), im.crop((W // 2 + 20, 0, W, H))]
    bg = Image.new('RGB', halves[0].size, IVORY)
    boxes = [ImageChops.difference(h, bg).convert('L').point(lambda v: 255 if v > 24 else 0).getbbox() for h in halves]  # ignore JPEG noise
    top, bottom = min(b[1] for b in boxes) - 36, max(b[3] for b in boxes) + 36   # same height for both
    for h, b, name in zip(halves, boxes, ('_scribbled.jpg', '_written.jpg')):
        cx = (b[0] + b[2]) // 2; half_w = max(b[2] - b[0], 420) // 2 + 36
        h.crop((max(0, cx - half_w), max(0, top), min(h.width, cx + half_w), min(h.height, bottom))).save(stem + name, quality=92)
