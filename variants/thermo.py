
class Thermo:
    def __init__(self):
        pass

    def apply(puzzle):
        val = 0
        for line in puzzle.thermo:
            lastMin = 0
            for n in range(0, len(line)):
                cell = line[n]
                if puzzle.cellFilled(cell):
                    lastMin = puzzle.grid[cell[0]][cell[1]]
                    lastMax = puzzle.grid[cell[0]][cell[1]]
                else:
                    for cand in puzzle.grid[cell[0]][cell[1]]:
                        if cand <= lastMin:
                            val = max(puzzle.removeCandidate(cell[0], cell[1], cand), val)
                        else:
                            lastMin = cand
                            break
            
            lastMax = 10
            for n in range(1, len(line) + 1):
                cell = line[len(line) - n]
                if puzzle.cellFilled(cell):
                    lastMax = puzzle.grid[cell[0]][cell[1]]
                else:
                    for cand in puzzle.grid[cell[0]][cell[1]]:
                        if cand >= lastMax:
                            val = max(puzzle.removeCandidate(cell[0], cell[1], cand), val)
                        else:
                            lastMax = max(cand, lastMax)
        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        for line in puzzle.thermo:
            hasCell = False
            listPos = 0
            for cell in line:
                if cell == entryRow and cell == entryCol:
                    hasCell = True
                    listPos = line.index(cell)
            
            if hasCell:
                lastMin = num
                for n in range(listPos + 1, len(line)):
                    cell = line[n]
                    if puzzle.cellFilled(cell):
                        lastMin = puzzle.grid[cell[0]][cell[1]]
                    else:
                        for cand in puzzle.grid[cell[0]][cell[1]]:
                            if cand <= lastMin:
                                puzzle.removeCandidate(cell[0], cell[1], cand)
                            else:
                                lastMin = cand
                                break
                
                lastMax = num
                for n in range(len(line) - listPos, len(line)):
                    cell = line[len(line) - n - 1]
                    if puzzle.cellFilled(cell):
                        lastMax = puzzle.grid[cell[0]][cell[1]]
                    else:
                        for cand in puzzle.grid[cell[0]][cell[1]]:
                            if cand >= lastMax:
                                puzzle.removeCandidate(cell[0], cell[1], cand)
                            else:
                                lastMax = max(cand, lastMax)

    def applyCand(puzzle, entryRow, entryCol, candidates):
        return 0



    def checkSolution(puzzle):
        for line in puzzle.thermo:
            lastMin = 0
            for n in range(0, len(line)):
                cell = line[n]
                if puzzle.grid[cell[0]][cell[1]] <= lastMin:
                    return False
                else:
                    lastMin = puzzle.grid[cell[0]][cell[1]]
                
            lastMax = 10
            for n in range(1, len(line) + 1):
                cell = line[len(line) - n]
                if puzzle.grid[cell[0]][cell[1]] >= lastMax:
                    return False
                else:
                    lastMax = puzzle.grid[cell[0]][cell[1]]
        return True