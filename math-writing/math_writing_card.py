"""Figures for 'Easy Writing "Mathematisch"'.
  card:    only the scribbled chain x² = 4, = √4, = 2 (card and header image, JPEG)
  compare: the scribbled chain next to the same solution written as a chain of equivalent statements (JPEG)
  split:   the two halves of 'compare' as separate vector graphics out_scribbled.svg and out_written.svg,
           small type (matching the diagrams in the article) and cropped to the content
Usage: python math_writing_card.py out.jpg [card|compare|split] [svg|png]   (last argument: file type of the split halves)"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

W, H = 1376, 768
IVORY, ROSE, TERRA, DARK, MUTED, PLUM = '#FAF8F5', '#B77A8A', '#DF7654', '#1F1A1C', '#8A7F82', '#874C62'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams['svg.fonttype'] = 'path'      # text as outlines: looks the same in every browser
NL = chr(10)
mode = sys.argv[2] if len(sys.argv) > 2 else 'card'
out = sys.argv[1]

CAPTION_LEFT = NL.join(['So $4 = 2$?  And what is $x$?', 'There is nothing to check,', 'only something to guess.'])
CAPTION_RIGHT = NL.join(['Every line is a statement', 'you can check.'])
SCRIBBLED = [(r'$x^2 = 4$', 0.19), (r'$= \sqrt{4}$', 0.24), (r'$= 2$', 0.24)]
WRITTEN = [r'Let $x \in \mathbb{R}$. Then:',
           r'$x^2 = 4$',
           r'$\Leftrightarrow\; x^2 - 4 = 0$',
           r'$\Leftrightarrow\; (x-2)(x+2) = 0$',
           r'$\Leftrightarrow\; x = 2$ or $x = -2$.']


def canvas(x0, x1, y0, y1):
    """An axes whose data coordinates are pixels of the full W x H design, showing only the window given."""
    fig = plt.figure(figsize=((x1 - x0) / 100, (y1 - y0) / 100), dpi=100)
    fig.patch.set_facecolor(IVORY)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(IVORY)
    ax.axis('off')
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    return fig, ax


def draw_compare(ax, sides=('left', 'right'), fh=34, ff=40, fc=25, step=0.16 * H, divider=True):
    """The comparison figure; returns the y of the captions so callers can crop."""
    y0 = H - 95 - 1.6 * step
    ycap = y0 - 4 * step - 1.9 * step
    if divider:
        ax.plot([W / 2, W / 2], [90, H - 90], color=ROSE, lw=2, alpha=0.6)
    if 'left' in sides:
        ax.text(W * 0.25, H - 95, 'scribbled', ha='center', va='center', fontsize=fh, family='serif', color=ROSE)
        for i, (t, xf) in enumerate(SCRIBBLED):
            ax.text(W * xf, y0 - i * step, t, ha='left', va='center', fontsize=ff, color=MUTED, family='serif')
        ax.text(W * 0.25, ycap, CAPTION_LEFT, ha='center', va='center', fontsize=fc, linespacing=1.3, family='serif', color=ROSE)
    if 'right' in sides:
        ax.text(W * 0.75, H - 95, 'written', ha='center', va='center', fontsize=fh, family='serif', color=TERRA)
        for i, t in enumerate(WRITTEN):
            ax.text(W * 0.56, y0 - i * step, t, ha='left', va='center', fontsize=ff, color=DARK, family='serif')
        ax.text(W * 0.75, ycap, CAPTION_RIGHT, ha='center', va='center', fontsize=fc, linespacing=1.3, family='serif', color=TERRA)
    return ycap


if mode == 'card':
    fig, ax = canvas(0, W, 0, H)
    left = [(r'$x^2 = 4$', 0.40), (r'$= \sqrt{4}$', 0.47), (r'$= 2$', 0.47)]
    for i, (t, xf) in enumerate(left):
        ax.text(W * xf, H * 0.76 - i * 0.17 * H, t, ha='left', va='center', fontsize=56, color=MUTED, family='serif')
    # the remark in handwriting, like the corrections on the page (Segoe Print on Windows; serif fallback)
    import os
    from matplotlib.font_manager import FontProperties
    hand = FontProperties(fname=r'C:\Windows\Fonts\segoepr.ttf') if os.path.exists(r'C:\Windows\Fonts\segoepr.ttf') else FontProperties(family='serif', style='italic')
    ax.text(W * 0.5, H * 0.17, 'So 4 = 2?  And what is x?', ha='center', va='center', fontsize=40, fontproperties=hand, color=PLUM)
    fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})

elif mode == 'compare':
    fig, ax = canvas(0, W, 0, H)
    draw_compare(ax)
    fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})

else:  # split
    stem = out.rsplit('.', 1)[0]
    ext = '.' + (sys.argv[3] if len(sys.argv) > 3 else 'svg')
    small = dict(fh=18, ff=18, fc=18, step=0.075 * H, divider=False)
    step = small['step']
    ycap = H - 95 - 1.6 * step - 4 * step - 1.9 * step
    y_lo, y_hi = ycap - 65, H - 95 + 40           # window around headings and captions, same for both
    half_w = 300                                  # same width for both, so the type is the same size
    for side, cx, name in (('left', W * 0.25, '_scribbled' + ext), ('right', W * 0.75, '_written' + ext)):
        fig, ax = canvas(cx - half_w, cx + half_w, y_lo, y_hi)
        draw_compare(ax, sides=(side,), **small)
        fig.savefig(stem + name, facecolor=IVORY, dpi=200)
        plt.close(fig)
