# Why the Circle Wins

Article: [https://belindata.com/projects/isoperimetric.html](https://belindata.com/projects/isoperimetric.html) (in progress)

- `fence_off_a_field.html`: stage 1 of the article, 18 pieces of fence on a big field; fence off a rectangle, make it wider or narrower, and count the patches inside. Standalone page, open it in any browser.
- `fence_off_a_field_rope.html`: stage 2, the same fence as a rope: a slider for the width, the graph of the area and its tangent; stop when the tangent is flat.
- `fence_off_a_field_corners.html`: stage 3, regular polygons with the same fence compared with the circle.
- `steiner_symmetrization.html`: stage 3, the proof idea: an odd-shaped field, draw an axis by hand, symmetrize and watch the fence shrink while the area stays; a "keep going" mode rotates the axis until the field is a circle. Standalone page.
- `steiner_symmetrization.py`: Steiner symmetrization of a planar shape: every vertical chord is slid until its midpoint lies on the horizontal axis. Area stays the same, the boundary gets shorter.
- `isoperimetric_card.py`: Card image for 'Why the Circle Wins': dark like the interactives: one rope of length L = 18 unrolled at the top, and below it, side by side and to scale, three fields fenced with that rope: rectangle 8 × 1 < square 4.5 × 4.5 < circle.
- `steiner.jpg`: the image as used on the site
- `card_isoperimetric.jpg`: the image as used on the site

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
