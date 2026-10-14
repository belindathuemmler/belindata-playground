"""Card image for 'AI vs. Me: A Data Analysis Duel': a dashboard in belindata colours, built with the real
numbers from my IBM Data Analyst capstone (Stack Overflow survey). Usage: python dashboard_card.py out.jpg"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = sys.argv[1]
IVORY, PLUM, ROSE, CORAL, TERRA, DARK, SAGE = '#FAF8F5', '#874C62', '#B77A8A', '#EE9779', '#DF7654', '#1F1A1C', '#5B7D54'
W, H = 1376, 768
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
fig.patch.set_facecolor(IVORY)

# frame with two tabs: Me | AI
bg = fig.add_axes([0, 0, 1, 1]); bg.axis('off'); bg.set_xlim(0, 1); bg.set_ylim(0, 1)
bg.add_patch(FancyBboxPatch((0.03, 0.04), 0.94, 0.84, boxstyle='round,pad=0,rounding_size=0.02', fc='white', ec='#E8DED8', lw=2))
bg.add_patch(FancyBboxPatch((0.05, 0.86), 0.09, 0.08, boxstyle='round,pad=0,rounding_size=0.015', fc=PLUM, ec='none'))
bg.text(0.095, 0.9, 'Me', ha='center', va='center', fontsize=20, color='white', weight='bold')
bg.add_patch(FancyBboxPatch((0.15, 0.86), 0.09, 0.08, boxstyle='round,pad=0,rounding_size=0.015', fc='white', ec=TERRA, lw=2))
bg.text(0.195, 0.9, 'AI', ha='center', va='center', fontsize=20, color=TERRA, weight='bold')
bg.text(0.95, 0.9, 'Stack Overflow survey', ha='right', va='center', fontsize=16, color=ROSE)

# KPI tiles (real counts from the capstone)
kpis = [('JavaScript', '8,687', TERRA), ('MySQL', '5,469', PLUM), ('Linux', '5,811', SAGE)]
for k, (label, val, col) in enumerate(kpis):
    x = 0.06 + k * 0.155
    bg.add_patch(FancyBboxPatch((x, 0.6), 0.14, 0.2, boxstyle='round,pad=0,rounding_size=0.015', fc=IVORY, ec='none'))
    bg.text(x + 0.07, 0.725, val, ha='center', fontsize=26, color=col, weight='bold')
    bg.text(x + 0.07, 0.645, label, ha='center', fontsize=14, color=DARK, alpha=0.7)

# bar chart: top languages
ax1 = fig.add_axes([0.12, 0.1, 0.36, 0.42])
langs = ['JavaScript', 'HTML/CSS', 'SQL', 'Shell', 'Python'][::-1]
vals = [8687, 7830, 7106, 4642, 4542][::-1]
ax1.barh(langs, vals, color=TERRA, alpha=0.85, height=0.62)
ax1.set_title('Top languages', fontsize=16, color=DARK, loc='left')
# bar chart: top databases
ax2 = fig.add_axes([0.6, 0.1, 0.33, 0.7])
dbs = ['MySQL', 'SQL Server', 'PostgreSQL', 'SQLite', 'MongoDB'][::-1]
dvals = [5469, 4110, 4097, 3248, 3016][::-1]
ax2.barh(dbs, dvals, color=PLUM, alpha=0.75, height=0.62)
ax2.set_title('Top databases', fontsize=16, color=DARK, loc='left')
for a in (ax1, ax2):
    a.set_facecolor('white')
    for side in ['top', 'right', 'bottom']:
        a.spines[side].set_visible(False)
    a.spines['left'].set_color('#E8DED8')
    a.tick_params(axis='y', labelsize=13, colors=DARK, length=0)
    a.set_xticks([])
fig.savefig(out, dpi=100, facecolor=IVORY, pil_kwargs={'quality': 92})
print('ok')
