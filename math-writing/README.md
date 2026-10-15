# Easy Writing “Mathematisch”

Article: [https://belindata.com/projects/math-writing.html](https://belindata.com/projects/math-writing.html) (in progress)

- `moser_circle.html`: the “1, 2, 4, 8, 16, … ?” animation as a standalone page. Open it in any browser, no installation needed.
- `four_solutions.html`: the flip cards “Five Solutions, One Perfect” (five solutions of x² = 4, one passes both tests, one also has the full stop) as a standalone page.
- `math_writing_card.py`: two figures. `card`: the scribbled chain x² = 4, = √4, = 2 alone (card and header image); `compare`: the scribbled chain next to the same solution written as a chain of equivalent statements (`python math_writing_card.py out.jpg compare`)
- `math_writing_compare.jpg`: the comparison figure; `math_writing_scribbled.svg`, `math_writing_written.svg`: its two halves as vector graphics, as used in the article (`python math_writing_card.py out.jpg split`)
- `card_math_writing.jpg`: the image as used on the site

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
