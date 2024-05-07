
import copy

class Arrow:
    def __init__(self):
        pass

    def apply(puzzle):
        val = 0
        for arrow in puzzle.arrow:
            sumCandidates = copy.deepcopy(puzzle.getCandidates(arrow[0]))
            if not puzzle.cellFilled(arrow[0]):
                sumCandidates = copy.deepcopy(puzzle.getCandidates(arrow[0]))
                for cand in sumCandidates:
                    if not cand in puzzle.possibleArrow[arrow]:
                        val = max(puzzle.removeCandidate(arrow[0][0], arrow[0][1], cand), val)
            val = max(Arrow.checkPossibleCellCandidates(puzzle, arrow), val)
            val = max(Arrow.checkPossibleCombos(puzzle, arrow), val)
        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        arrows = puzzle.getArrows([entryRow, entryCol])
        if not arrows:
            return
        for arrow in arrows:
            if arrow[0] == (entryRow, entryCol):
                combos = copy.deepcopy(puzzle.possibleArrow[arrow])
                for possibleSum in combos:
                    if not possibleSum == num:
                        puzzle.removeArrowCombo(arrow, possibleSum, combos[possibleSum][0])
            Arrow.checkPossibleCellCandidates(puzzle, arrow)
            Arrow.checkPossibleCombos(puzzle, arrow)

    def applyCand(puzzle, entryRow, entryCol, candidates):
        val = 0
        arrows = puzzle.getArrows([entryRow, entryCol])
        if not arrows:
            return val
        for arrow in arrows:
            if arrow[0] == (entryRow, entryCol):
                combos = copy.deepcopy(puzzle.possibleArrow[arrow])
                for possibleSum in combos:
                    if not possibleSum in candidates:
                        val = max(puzzle.removeArrowSum(arrow, possibleSum), val)
            val = max(Arrow.checkPossibleCellCandidates(puzzle, arrow), val)
        return val

    def checkSolution(puzzle):
        for arrow in puzzle.arrow:
            sum = puzzle.getCandidates(arrow[0])
            cells = list(copy.deepcopy(arrow))
            cells.remove(arrow[0])

            newSum = 0
            for cell in cells:
                newSum += puzzle.getCandidates(cell)
                if newSum > sum:
                    return False
            if not sum == newSum:
                return False
        return True
    
    # given legal candidates in cells, remove impossible combos for those cells
    def checkPossibleCellCandidates(puzzle, arrow):
        val = 0
        combos = copy.deepcopy(puzzle.possibleArrow[arrow])
        sumCell = arrow[0]
        cells = list(copy.deepcopy(arrow))
        cells.remove(sumCell)

        availableCands = []
        for cell in cells:
            if puzzle.cellFilled(cell):
                if not puzzle.getCandidates(cell)in availableCands:
                    availableCands.append(puzzle.getCandidates(cell))
            else:
                for cand in puzzle.getCandidates(cell):
                    if not cand in availableCands:
                        availableCands.append(cand)

        for possibleSum in combos:
            for combo in combos[possibleSum]:
                newVal = 0
                for n in combo:
                    if not n in availableCands:
                        newVal = puzzle.removeArrowCombo(arrow, possibleSum, combo)
                        break
                if newVal == 0:
                    if not Arrow.findValidConfig(puzzle, combo, cells):
                        val = max(puzzle.removeArrowCombo(arrow, possibleSum, combo), val)
                else:
                    val = newVal
                    
        return val
    
    # given legal combos, remove impossible candidates for those combos
    def checkPossibleCombos(puzzle, arrow):
        val = 0
        sumCell = arrow[0]
        cells = list(copy.deepcopy(arrow))
        cells.remove(sumCell)
        combos = copy.deepcopy(puzzle.possibleArrow[arrow])

        if len(cells) == 1:
            sumCand = copy.deepcopy(puzzle.getCandidates(sumCell))
            candidates = copy.deepcopy(puzzle.getCandidates(cells[0]))
            if not sumCand == candidates:
                if puzzle.cellFilled(sumCell) and puzzle.cellFilled(cells[0]):
                    return -1
                if puzzle.cellFilled(sumCell):
                    puzzle.fillCell(cells[0][0], cells[0][1], sumCand)
                    val = 1
                elif puzzle.cellFilled(cells[0]):
                    puzzle.fillCell(sumCell[0], sumCell[1], sumCand)
                    val = 1
                else:
                    for cand in sumCand:
                        if not cand in candidates:
                            val = max(puzzle.removeCandidate(sumCell[0], sumCell[1], cand), val)
                    for cand in candidates:
                        if not cand in sumCand:
                            val = max(puzzle.removeCandidate(cells[0][0], cells[0][1], cand), val)
            return val

        possibleDigits = []
        for possibleSum in combos:
            for combo in combos[possibleSum]:
                for n in combo:
                    if not n in possibleDigits:
                        possibleDigits.append(n)

        for cell in cells:
            if puzzle.cellFilled(cell):
                continue
            candidates = copy.deepcopy(puzzle.getCandidates(cell))
            for cand in candidates:
                if not cand in possibleDigits:
                    val = max(puzzle.removeCandidate(cell[0], cell[1], cand), val)
        
        for cell in cells:
            newCells = copy.deepcopy(cells)
            newCells.remove(cell)
            candidates = copy.deepcopy(puzzle.getCandidates(cell))
            if puzzle.cellFilled(cell):
                candidates = [copy.deepcopy(puzzle.getCandidates(cell))]
            for cand in candidates:
                hasValidConfig = False
                for possibleSum in combos:
                    for combo in combos[possibleSum]:
                        if cand in combo:
                            hasValidConfig = Arrow.findValidConfig(puzzle, combo, newCells)
                            if hasValidConfig:
                                break
                    if hasValidConfig:
                        break
                if not hasValidConfig:
                    val = max(puzzle.removeCandidate(cell[0], cell[1], cand), val)
        return val
        
    # attempt to assign each digit in combo to a cell
    def findValidConfig(puzzle, combo, cells):
        for cell in cells:
            newCells = copy.deepcopy(cells)
            newCells.remove(cell)
            for n in combo:
                if puzzle.cellFilled(cell):
                    if n == puzzle.getCandidates(cell):
                        if newCells:
                            newCombo = copy.deepcopy(combo)
                            newCombo.remove(n)
                            if (Arrow.findValidConfig(puzzle, newCombo, newCells)):
                                return True
                        else:
                            return True

                elif n in puzzle.getCandidates(cell):
                    if newCells:
                        newCombo = copy.deepcopy(combo)
                        newCombo.remove(n)
                        if (Arrow.findValidConfig(puzzle, newCombo, newCells)):
                            return True
                    else:
                        return True   
        return False