from sudokuSolver import SudokuSolver

def main():
    solver = SudokuSolver()
    solver.printTrace(False)
    solver.solvePuzzle('solvePuzzle.txt')

main()