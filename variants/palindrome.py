
import copy
class Palindrome:
    def __init__(self):
        pass

    def apply(puzzle):
        val = 0
        for line in puzzle.palindrome:
            for n in range(int(len(line) / 2)):
                cell1 = line[n]
                cell2 = line[len(line) - n - 1]
                cand1 = copy.deepcopy(puzzle.getCandidates(cell1))
                cand2 = copy.deepcopy(puzzle.getCandidates(cell2))
                if not cand1 == cand2:
                    if puzzle.cellFilled(cell1):
                        puzzle.fillCell(cell2[0], cell2[1], puzzle.getCandidates(cell1))
                    elif puzzle.cellFilled(cell2):
                        puzzle.fillCell(cell1[0], cell1[1], puzzle.getCandidates(cell2))
                    else:
                        for cand in cand1:
                            if not cand in cand2:
                                val = max(puzzle.removeCandidate(cell1[0], cell1[1], cand), val)
                        for cand in cand2:
                            if not cand in cand1:
                                val = max(puzzle.removeCandidate(cell2[0], cell2[1], cand), val)
        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        for line in puzzle.palindrome:
            hasCell = False
            listPos = 0
            for cell in line:
                if cell == entryRow and cell == entryCol:
                    hasCell = True
                    listPos = line.index(cell)
            
            if hasCell:
                cell2 = line[len(line) - listPos - 1]
                puzzle.fillCell(cell2[0], cell2[1], num)


    def applyCand(puzzle, entryRow, entryCol, candidates):
        val = 0
        for line in puzzle.palindrome:
            hasCell = False
            listPos = 0
            for cell in line:
                if cell == entryRow and cell == entryCol:
                    hasCell = True
                    listPos = line.index(cell)
            
            if hasCell:
                cell2 = line[len(line) - listPos - 1]
                cand2 = copy.deepcopy(puzzle.getCandidates(cell2))
                if not candidates == puzzle.getCandidates(cell2):
                    for cand in cand2:
                        if not cand in candidates:
                            val = max(puzzle.removeCandidate(cell2[0], cell2[1], cand), val)
        return val

    def checkSolution(puzzle):
        for line in puzzle.palindrome:
            for n in range(int(len(line) / 2)):
                cell1 = line[n]
                cell2 = line[len(line) - n - 1]
                if not puzzle.getCandidates(cell1) == puzzle.getCandidates(cell2):
                    return False
        return True