# Turning Pieces and Cubes

Article: [https://belindata.com/projects/two-pieces.html](https://belindata.com/projects/two-pieces.html)

My son's maths homework (fourth grade, "Kopfgeometrie"): which two pieces build the rectangle? Turning shapes in your head is hard, so the article is a little playground for the step in between, with four games. Each one is here as a standalone page; open it in any browser.

- `turning_pieces_2d.html`: **Which Two Build the Rectangle?** An 8 × 6 rectangle and four pieces on squared paper, at their real size. Drag a piece onto the rectangle, turn it with the buttons or a two-finger twist; it snaps to the grid. Puzzles are generated: a random cut (one step, or a 45-degree line that misses the corner by a cell or two), each piece between 30 % and 70 % of the rectangle; the traps are the same piece one row too big and the mirror image of a true piece. The check samples nine points per cell: covered exactly once means solved, overlaps and pieces sticking out turn the rectangle red.
- `turning_pieces_3d.html`: **Which Two Build the Block?** The same game with cubes and a 3 × 2 × 2 block, built with [three.js](https://github.com/mrdoob/three.js) (MIT) and its OrbitControls. A random split of the block into two connected pieces; traps: one cube more, and the mirror image; every puzzle is re-dealt until exactly one pair of the four builds the block. Drag a piece onto the block (a see-through copy shows where it will land), turn it about three axes, swipe the floor to look around.
- `folding_the_die.html`: **Which Die Is It?** The net of a real die (one of the 11 nets of the cube, turned or flipped) and four dice, only one of which is the folded net. The net folds and unfolds on its hinges and can be turned like a die. Traps: two neighbouring numbers swapped (breaks "opposite faces add up to 7"), one opposite pair swapped (the mirror image, which keeps the 7-rule), and a 2, 3 or 6 turned by a quarter.
- `falling_blocks.html`: **Falling Blocks**, my own little version of the game I played as a child: seven pieces, turning, rows that disappear, levels, a landing shadow. Keyboard, swiping and buttons.
- `two_pieces_card.py`, `card_two_pieces.jpg`: a redrawn card image in the style of the worksheet (our own pieces). The site itself uses a photo of exercise 2 from the workbook (Denken und Rechnen 4, Arbeitsheft, Westermann, p. 9), quoted with source on the page; that photo is not part of this repository.

Python scripts need `numpy` and `matplotlib` (`pip install -r ../requirements.txt`).
