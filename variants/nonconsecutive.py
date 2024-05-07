
class Nonconsecutive:
    def __init__(self):
        pass

    def apply(puzzle):
        val = 0
        for num in range(1, 10):
            for row in range(9):
                consecutive = []
                lastPos = -10
                for col in range(9):
                    if puzzle.cellFilled([row, col]):
                        continue
                    elif num in puzzle.getCandidates([row, col]):
                        if col == lastPos + 1:
                            consecutive[len(consecutive) - 1].append(col)
                            lastPos = col
                        else:
                            consecutive.append([col])
                            lastPos = col
                for c in consecutive:
                    if len(c) == 2:
                        val = max(Nonconsecutive.removeConsecutiveCells(puzzle, row, c[0], num), val)
                        val = max(Nonconsecutive.removeConsecutiveCells(puzzle, row, c[1], num), val)
                    elif len(c) == 3:
                        val = max(Nonconsecutive.removeConsecutiveCells(puzzle, row, c[1], num), val)

            for col in range(9):
                consecutive = []
                lastPos = -10
                for row in range(9):
                    if puzzle.cellFilled([row, col]):
                        continue
                    elif num in puzzle.getCandidates([row, col]):
                        if row == lastPos + 1:
                            consecutive[len(consecutive) - 1].append(row)
                            lastPos = row
                        else:
                            consecutive.append([row])
                            lastPos = row
                for c in consecutive:
                    if len(c) == 2:
                        val = max(Nonconsecutive.removeConsecutiveCells(puzzle, c[0], col, num), val)
                        val = max(Nonconsecutive.removeConsecutiveCells(puzzle, c[1], col, num), val)
                    elif len(c) == 3:
                        val = max(Nonconsecutive.removeConsecutiveCells(puzzle, c[1], col, num), val)

        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        if not num == 1:
            Nonconsecutive.removeConsecutiveCells(puzzle, entryRow, entryCol, num - 1)
        if not num == 9:
            Nonconsecutive.removeConsecutiveCells(puzzle, entryRow, entryCol, num + 1)

    def applyCand(puzzle, entryRow, entryCol, candidates):
        val = 0
        if len(candidates) == 2 and candidates[1] - candidates[0] == 1:
            val = max(Nonconsecutive.removeConsecutiveCells(puzzle, entryRow, entryCol, candidates[1]), val)
            val = max(Nonconsecutive.removeConsecutiveCells(puzzle, entryRow, entryCol, candidates[0]), val)
        elif len(candidates) == 3 and candidates[1] - candidates[0] == 1 and candidates[2] - candidates[1] == 1:
            val = max(Nonconsecutive.removeConsecutiveCells(puzzle, entryRow, entryCol, candidates[1]), val)
        return val

    def checkSolution(puzzle):
        for row in range(9):
            for col in range(9):
                num = puzzle.grid[row][col]
                if not row == 0:
                    if abs(puzzle.grid[row - 1][col] - num) == 1:
                        return False
                if not row == 8:
                    if abs(puzzle.grid[row + 1][col] - num) == 1:
                        return False
                if not col == 0:
                    if abs(puzzle.grid[row][col - 1] - num) == 1:
                        return False
                if not col == 8:
                    if abs(puzzle.grid[row][col + 1] - num) == 1:
                        return False
        return True

    def removeConsecutiveCells(puzzle, row, col, num):
        val = 0
        if not row == 0:
            val = max(puzzle.removeCandidate(row - 1, col, num), val)
        if not row == 8:
            val = max(puzzle.removeCandidate(row + 1, col, num), val)
        if not col == 0:
            val = max(puzzle.removeCandidate(row, col - 1, num), val)
        if not col == 8:
            val = max(puzzle.removeCandidate(row, col + 1, num), val)
        return val