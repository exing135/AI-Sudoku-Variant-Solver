
import copy

class Killer:

    def __init__(self):
        pass

    def apply(puzzle):
        val = 0

        for cage in puzzle.killer:
            sum = cage[0]
            cells = cage[1]

            possibleDigits = []
            combos = copy.deepcopy(puzzle.possibleKiller[cage])
            for combo in combos:
                for n in range(len(cells)):
                    if not combo[n] in possibleDigits:
                        possibleDigits.append(combo[n])

            availableCands = []
            for cell in cells:
                if not puzzle.cellFilled(cell):
                    candidates = copy.deepcopy(puzzle.getCandidates(cell))
                    for cand in candidates:
                        if not cand in possibleDigits:
                            if puzzle.removeCandidate(cell[0], cell[1], cand) == 1:
                                val = 1
                        else:
                            availableCands.append(cand)
                    
                    for combo in combos:
                        validCombo = False
                        for n in combo:
                            if not puzzle.cellFilled(cell):
                                if n in puzzle.getCandidates(cell):
                                    validCombo = True
                        if not validCombo:
                            val = max(puzzle.removeKillerCombo(cage, combo), val)
                else:
                    availableCands.append(puzzle.getCandidates(cell))

            for combo in combos:
                for n in combo:
                    if not n in availableCands:
                        if combo in puzzle.possibleKiller[cage]:
                            val = max(puzzle.removeKillerCombo(cage, combo), val)

        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        for cage in puzzle.killer:
            if puzzle.cageFilled(cage):
                break
            sum = cage[0]
            cells = cage[1]

            hasCell = False
            for cell in cells:
                if cell[0] == entryRow and cell[1] == entryCol:
                    hasCell = True
            if hasCell:
                for cell in cells:
                    if not puzzle.cellFilled(cell):
                        puzzle.removeCandidate(cell[0], cell[1], num)
                for combo in copy.deepcopy(puzzle.possibleKiller[cage]):
                    if not num in combo:
                        puzzle.removeKillerCombo(cage, combo)
            
    def applyCand(puzzle, entryRow, entryCol, candidates):
        val = 0
        cages = puzzle.getCages([entryRow, entryCol])
        if cages: # if cell is in a cage
            for cage in cages: # for each cage the cell is in
                sum = cage[0]
                cells = cage[1] # cell coordinates
                combos = copy.deepcopy(puzzle.possibleKiller[cage]) # possible combos for cage

                # get available candidates in a cage
                availableCands = [] # candidate digits present in at least one cell in cage
                for cellCoord in cells: # for each cell
                    if puzzle.cellFilled(cellCoord):
                        availableCands.append(puzzle.grid[cellCoord[0]][cellCoord[1]])
                    else:
                        cell = puzzle.getCandidates(cellCoord)
                        for cand in cell: # for each candidate in cell
                            if not cand in availableCands:
                                availableCands.append(cand)

                # remove combos that include a candidate not found in any cells in cage
                for combo in combos:
                    for n in combo:
                        if not n in availableCands:
                            val = max(puzzle.removeKillerCombo(cage, combo), val)

        return val

    def checkSolution(puzzle):
        for cage in puzzle.killer:
            sum = cage[0]
            cells = cage[1]
            
            testSum = 0
            for cell in cells:
                testSum += puzzle.grid[cell[0]][cell[1]]
            if not testSum == sum:
                return False
        return True