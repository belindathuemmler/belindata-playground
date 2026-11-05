# How Much Does a Flat Square Weigh?

Article: [https://belindata.com/projects/hausdorff.html](https://belindata.com/projects/hausdorff.html) (published)

- `covering_recipe.html`: interactive "Hausdorff’s Recipe, Step by Step" (2D): a curve in the plane covered by discs U_i of diameter δ; shrink δ and the discs multiply and hug the curve; the sum Σ (diam U_i)^s is shown for s = 1 and closes in on the length of the curve from below (coarse pieces cut corners); "another cover" cycles through a careful chord-centred cover, a wasteful one, a shifted one and one with pieces of different sizes (all ≤ δ), to show that the sum depends on the cover and Hausdorff takes the cheapest.
- `koch_curve.html`: interactive "Weighing the Koch Curve" as a standalone page.
- `koch_curve.py`: Card image: Koch curve (level 5) with its earlier construction steps faintly underneath.
- `three_fractals.py`: Figure for the article: the Cantor set (levels 0 to 5), the Sierpiński triangle (level 5) and a level-2 Menger sponge as voxels. Output `assets/three_fractals.jpg` on the site.
- `card_koch.jpg`: the image as used on the site

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
