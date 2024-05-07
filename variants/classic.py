
class Classic:
    def __init__(self):
        pass

    # checks entire puzzle and identifies all possibilities that fulfill the rule
    def apply(puzzle):
        val = 0
        for num in range(1, 10):
            newVal = Classic.checkRowCount(puzzle, num)
            if (newVal == -1):
                break
            else:
                val = max(newVal, val)

            newVal = Classic.checkColCount(puzzle, num)
            if (newVal == -1):
                break
            else:
                val = max(newVal, val)

            newVal = Classic.checkBoxCount(puzzle, num)
            if (newVal == -1):
                break
            else:
                val = max(newVal, val)

        return val

    # applies rules given value for a singular cell
    def applyCell(puzzle, entryRow, entryCol, num):
        for row in range(9):
            puzzle.removeCandidate(row, entryCol, num)

        for col in range(9):
            puzzle.removeCandidate(entryRow, col, num)
        
        boxRow = entryRow - (entryRow % 3)
        boxCol = entryCol - (entryCol % 3)
        for row in range(boxRow, boxRow + 3):
            for col in range (boxCol, boxCol + 3):
                puzzle.removeCandidate(row, col, num)

    # applies rules given candidates of a singular cell
    def applyCand(puzzle, entryRow, entryCol, candidates):
        if len(candidates) > 1:
            if len(candidates) < 5:
                val = 0
                matches = []
                for col in range(9):
                    if not col == entryCol:
                        if not puzzle.cellFilled([entryRow, col]) and len(puzzle.grid[entryRow][col]) <= len(candidates):
                            isIncluded = True
                            for cand in puzzle.grid[entryRow][col]:
                                if not cand in candidates:
                                    isIncluded = False
                            if isIncluded:
                                matches.append(col)
                if len(matches) + 1 == len(candidates):
                    for col in range(9):
                        if not col in matches and not col == entryCol:
                            for cand in candidates:
                                if puzzle.removeCandidate(entryRow, col, cand) == 1:
                                    val = 1

                matches = []
                for row in range(9):
                    if not row == entryRow:
                        if not puzzle.cellFilled([row, entryCol]) and len(puzzle.grid[row][entryCol]) <= len(candidates):
                            isIncluded = True
                            for cand in puzzle.grid[row][entryCol]:
                                if not cand in candidates:
                                    isIncluded = False
                            if isIncluded:
                                matches.append(row)
                if len(matches) + 1 == len(candidates):
                    for row in range(9):
                        if not row in matches and not row == entryRow:
                            for cand in candidates:
                                if puzzle.removeCandidate(row, entryCol, cand) == 1:
                                    val = 1

                boxRow = puzzle.getBox(entryRow)
                boxCol = puzzle.getBox(entryCol)
                matches = []
                for row in range(boxRow, boxRow + 3):
                    for col in range(boxCol, boxCol + 3):
                        if not (row == entryRow and col == entryCol):
                            if not puzzle.cellFilled([row, col]) and len(puzzle.grid[row][col]) <= len(candidates):
                                isIncluded = True
                                for cand in puzzle.grid[row][col]:
                                    if not cand in candidates:
                                        isIncluded = False
                                if isIncluded:
                                    matches.append((row, col))
                if len(matches) + 1 == len(candidates):
                    for row in range(boxRow, boxRow + 3):
                        for col in range(boxCol, boxCol + 3):
                            if not (row, col) in matches and not (row == entryRow and col == entryCol):
                                for cand in candidates:
                                    if puzzle.removeCandidate(row, col, cand) == 1:
                                        val = 1
                return val
            else:
                return 0
        elif len(candidates) == 1:
            puzzle.fillCell(entryRow, entryCol, candidates[0])
            return 1
        elif len(candidates) == 0:
            return -1



    def checkRowCount(puzzle, num):
        val = 0
        doubles = {}
        for row in range(9):
            count = 0
            cols = []
            entryCol = 0
            entryBox = 0
            boxExclusive = True
            for col in range(9):
                if puzzle.cellFilled([row, col]):
                    if puzzle.grid[row][col] == num:
                        count = 10
                        break
                    pass
                elif puzzle.cellContains([row, col], num):
                    count += 1
                    if count == 1:
                        entryCol = col
                        entryBox = puzzle.getBox(col)
                        cols.append(col)
                    else:
                        if not entryBox == puzzle.getBox(col):
                            boxExclusive = False
                        if count == 2:
                            cols.append(col)

            if count > 1:
                if not count == 10 and boxExclusive:
                    for i in range(3):
                        if not puzzle.getBox(row) + i == row:
                            for j in range(3):
                                if puzzle.removeCandidate(puzzle.getBox(row) + i, entryBox + j, num) == 1:
                                    val = 1
                if count == 2:
                    if cols in doubles.values():
                        for col in cols:
                            for r in range(9):
                                if not r == row:
                                    if puzzle.removeCandidate(r, col, num) == 1:
                                        val = 1
                    doubles[row] = tuple(cols)

            elif count == 1:
                puzzle.fillCell(row, entryCol, num)
                val = 1
            elif count == 0:
                return -1
        return val
    
    def checkColCount(puzzle, num):
        val = 0
        doubles = {}
        for col in range(9):
            count = 0
            rows = []
            entryRow = 0
            entryBox = 0
            boxExclusive = True
            for row in range(9):
                if puzzle.cellFilled([row, col]):
                    if puzzle.grid[row][col] == num:
                        count = 10
                        break
                elif puzzle.cellContains([row, col], num):
                    count += 1
                    if count == 1:
                        entryRow = row
                        entryBox = puzzle.getBox(row)
                        rows.append(row)
                    else:
                        if not entryBox == puzzle.getBox(row):
                            boxExclusive = False
                        if count == 2:
                            rows.append(row)
            if count > 1:
                if not count == 10 and boxExclusive:
                    for j in range(3):
                        if not puzzle.getBox(col) + j == col:
                            for i in range(3):
                                if puzzle.removeCandidate(entryBox + i, puzzle.getBox(col) + j, num) == 1:
                                    val = 1
                if count == 2:
                    if rows in doubles.values():
                        for row in rows:
                            for c in range(9):
                                if not c == col:
                                    if puzzle.removeCandidate(row, c, num) == 1:
                                        val = 1
                    doubles[col] = tuple(rows)
            elif count == 1:
                puzzle.fillCell(entryRow, col, num)
                val = 1
            elif count == 0:
                return -1
        return val
    
    def checkBoxCount(puzzle, num):
        val = 0
        doubles = {}
        for boxRow in range(3):
            for boxCol in range(3):
                count = 0
                rows = []
                cols = []
                entryRow = 0
                entryCol = 0
                rowExclusive = True
                colExclusive = True
                for i in range(3):
                    for j in range(3):
                        if puzzle.cellFilled([(boxRow * 3) + i, (boxCol * 3) + j]) and puzzle.grid[(boxRow * 3) + i][(boxCol * 3) + j] == num:
                            count = 10
                            break
                        elif puzzle.cellContains([(boxRow * 3) + i, (boxCol * 3) + j], num):
                            count += 1

                            if count == 1:
                                entryRow = (boxRow * 3) + i
                                entryCol = (boxCol * 3) + j
                                rows.append(entryRow)
                                cols.append(entryCol)
                            else:
                                if not entryRow == (boxRow * 3) + i:
                                    rowExclusive = False
                                if not entryCol == (boxCol * 3) + j:
                                    colExclusive = False
                                if count == 2:
                                    rows.append((boxRow * 3) + i)
                                    cols.append((boxCol * 3) + j)

                    if count == 10:
                        break
                if count > 1:
                    if not count == 10:
                        if rowExclusive:
                            for col in range(9):
                                if not puzzle.getBox(col) / 3 == boxCol:
                                    if puzzle.removeCandidate(entryRow, col, num) == 1:
                                        val = 1

                        if colExclusive:
                            for row in range(9):
                                if not puzzle.getBox(row) / 3 == boxRow:
                                    if puzzle.removeCandidate(row, entryCol, num) == 1:
                                        val = 1

                elif count == 1:
                    puzzle.fillCell(entryRow, entryCol, num)
                    val = 1
                elif count == 0:
                    return -1

        return val
    
    def checkSolution(puzzle):
        for row in range(9):
            for col in range(9):
                num = puzzle.grid[row][col]
                for i in range(9):
                    if not i == row and puzzle.grid[i][col] == num:
                        return False
                for j in range(9):
                    if not j == col and puzzle.grid[row][j] == num:
                        return False
                
                boxRow = puzzle.getBox(row)
                boxCol = puzzle.getBox(col)
                for i in range(3):
                    if not boxRow + i == row and puzzle.grid[boxRow + i][col] == num:
                        return False
                for j in range(3):
                    if not boxCol + j == col and puzzle.grid[row][boxCol + j] == num:
                        return False
        return True

    
