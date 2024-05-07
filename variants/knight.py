

class Knight:
    def __init__(self):
        pass

    def apply(puzzle):
        val = 0
        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        if entryRow - 2 >= 0:
            if entryCol - 1 >= 0:
                puzzle.removeCandidate(entryRow - 2, entryCol - 1, num)
            if entryCol + 1 <= 8:
                puzzle.removeCandidate(entryRow - 2, entryCol + 1, num)
        if entryRow + 2 <= 8:
            if entryCol - 1 >= 0:
                puzzle.removeCandidate(entryRow + 2, entryCol - 1, num)
            if entryCol + 1 <= 8:
                puzzle.removeCandidate(entryRow + 2, entryCol + 1, num)

        if entryCol - 2 >= 0:
            if entryRow - 1 >= 0:
                puzzle.removeCandidate(entryRow - 1, entryCol - 2, num)
            if entryRow + 1 <= 8:
                puzzle.removeCandidate(entryRow + 1, entryCol - 2, num)
        if entryCol + 2 <= 8:
            if entryRow - 1 >= 0:
                puzzle.removeCandidate(entryRow - 1, entryCol + 2, num)
            if entryRow + 1 <= 8:
                puzzle.removeCandidate(entryRow + 1, entryCol + 2, num)


    def applyCand(puzzle, entryRow, entryCol, candidates):
        val = 0
        return val

    def checkSolution(puzzle):
        for row in range(9):
            for col in range(9):
                if row - 2 >= 0:
                    if col - 1 >= 0:
                        if puzzle.getCandidates([row - 2, col - 1]) == puzzle.getCandidates([row, col]):
                            return False
                    if col + 1 <= 8:
                        if puzzle.getCandidates([row - 2, col + 1]) == puzzle.getCandidates([row, col]):
                            return False
                if row + 2 <= 8:
                    if col - 1 >= 0:
                        if puzzle.getCandidates([row + 2, col - 1]) == puzzle.getCandidates([row, col]):
                            return False
                    if col + 1 <= 8:
                        if puzzle.getCandidates([row + 2, col + 1]) == puzzle.getCandidates([row, col]):
                            return False

                if col - 2 >= 0:
                    if row - 1 >= 0:
                        if puzzle.getCandidates([row - 1, col - 2]) == puzzle.getCandidates([row, col]):
                            return False
                    if row + 1 <= 8:
                        if puzzle.getCandidates([row + 1, col - 2]) == puzzle.getCandidates([row, col]):
                            return False
                if col + 2 <= 8:
                    if row - 1 >= 0:
                        if puzzle.getCandidates([row - 1, col + 2]) == puzzle.getCandidates([row, col]):
                            return False
                    if row + 1 <= 8:
                        if puzzle.getCandidates([row + 1, col + 2]) == puzzle.getCandidates([row, col]):
                            return False
        return True