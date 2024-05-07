# AI-Sudoku-Variant-Solver

To solve a sudoku puzzle:
1. Enter a puzzle in solvePuzzle.txt
- Puzzle must be in the following format:
- Line 1 - variants used
  - variants must be entered as a series of eight 0's and 1's with 0 indicating a variant is not applied and 1 indicating that a variant is applied
  - variants are listed in the following order - classic, arrow, chess knight, killer, nonconsecutive, palindrome, sandwich, thermo
  - ex. 10000101 - puzzle variants are classic, palindrome, and thermo
- Lines 2-10 - starting digits on the sudoku grid (enter 0 if empty)
  - each line contains 9 digits to represent the digits of each row of the sudoku grid
- Lines 11+ - any additional information for variants (if applicable)
  - place each variant on a single line in the following order, omit if variant is not present in the puzzle
  - arrow - list all arrows in the format [circleCell, arrowCell, arrowCell, ...], [circleCell, arrowCell, arrowCell, ...], ...etc.
    - ex. [36, 25, 14] - circle at row 3 col 6, arrow along row 2 col 5 and row 1 col 4
  - killer - list all killer cages in the format [cageSum, [cageCell, cageCell, ...]], [cageSum, [cageCell, cageCell, ...], ...etc.
    - ex. [17, [11, 21]] - cage with sum 17 containing cells at row 1 col 1 and row 2 col 1
  - palindrome - list all palindrome lines in the format [lineCell, lineCell, ...], [lineCell, lineCell, ...], ...etc.
    - ex. [36, 25, 14] - palindrome line crossing through cells at row 3 col 6, row 2 col 5, and row 1 col 4 in order
  - sandwich - list all sandwich sums in the format [rowSum1, rowSum2, ..., rowSum9], [colSum1, colSum2, ..., colSum9] (enter - if no sum)
    - ex. [-, -, -, 17, 16, 6, -, 22, 5], [5, 16, 24, -, -, -, -, 6, 23] - row 4 sum 17, row 5 sum 16, ...etc., col 1 sum 5, col 2 sum 16, ...
  - thermo - list all thermometer lines in the format [thermoBulb, thermoLine, thermoLine, ..., thermoEnd], ...etc.
    - ex. [36, 25, 14] - bulb at row 3 col 6, thermo line through row 2 col 5 and row 1 col 4 in order
2. Run main.py

Several example puzzles are included in sudokuPuzzles.txt, simply copy and paste a puzzle from there into solvePuzzle.txt and run main.py to solve it. Solutions for the example puzzles are included in sudokuSolutions.txt (listed in the same order as in sudokuPuzzles.txt)  
