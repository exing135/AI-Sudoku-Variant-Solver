
import copy
class Sandwich:
    def __init__(self):
        pass

    def apply(puzzle):
        val = 0
        for n in range(9):
            Sandwich.rowRemove19(puzzle, n)
            Sandwich.colRemove19(puzzle, n)
        
        # for row in range(9):
        #     sum = puzzle.sandwich[0][row]
        #     if not sum == -1:
        #         one, nine = Sandwich.rowFind19(puzzle, row)
        #         if len(one) == 1:
        #             if len(nine) == 1 and not sum == 0:
        #                 diff = abs(one[0] - nine[0])
                        



        return val

    def applyCell(puzzle, entryRow, entryCol, num):
        if not puzzle.sandwich:
            return
        if num == 1 or num == 9:
            rowSum = puzzle.sandwich[0][entryRow]
            colSum = puzzle.sandwich[1][entryCol]
            if not rowSum == -1:
                rowOne, rowNine = Sandwich.rowFind19(puzzle, entryRow)
                if len(rowOne) == 1 and len(rowNine) == 1:
                    if (not rowSum == 0) and (not rowSum == 35):
                        diff = abs(rowOne[0] - rowNine[0]) - 1
                        possibleRow = copy.deepcopy(puzzle.possibleSandwich[0][entryRow])
                        for possibleLength in possibleRow:
                            if not possibleLength == diff:
                                del puzzle.possibleSandwich[0][entryRow][possibleLength]

                        possibleRow = copy.deepcopy(puzzle.possibleSandwich[0][entryRow])
                        if not possibleRow:
                            return
                        cells = []
                        for n in range(min(rowOne[0] + 1, rowNine[0]), max(rowOne[0] + 1, rowNine[0])):
                            cells.append((entryRow, n))

                        possibleDigits = []
                        for n in possibleRow[diff]:
                            if not n in possibleDigits:
                                possibleDigits.append(n)
                        
                        for cell in cells:
                            if not puzzle.cellFilled(cell):
                                candidates = copy.deepcopy(puzzle.getCandidates(cell))
                                for cand in candidates:
                                    if not cand in possibleDigits:
                                        puzzle.removeCandidate(cell[0], cell[1], cand)
                else:
                    if rowSum == 0:
                        if entryCol > 1:
                            for n in range(entryCol - 1):
                                if num == 1:
                                    puzzle.removeCandidate(entryRow, n, 9)
                                elif num == 9:
                                    puzzle.removeCandidate(entryRow, n, 1)
                        if entryCol < 6:
                            for n in range(entryCol + 2, 9):
                                if num == 1:
                                    puzzle.removeCandidate(entryRow, n, 9)
                                elif num == 9:
                                    puzzle.removeCandidate(entryRow, n, 1)
                    else:
                        possibleLengths = []
                        possibleRow = copy.deepcopy(puzzle.possibleSandwich[0][entryRow])
                        for possibleLength in possibleRow:
                            possibleLengths.append(possibleLength)
                        possibleLengths.sort()
                        if not possibleLengths:
                            return
                        for n in range(possibleLengths[0]):
                            if num == 1:
                                if entryCol - n >= 0:
                                    puzzle.removeCandidate(entryRow, entryCol - n, 9)
                                if entryCol + n <= 8:
                                    puzzle.removeCandidate(entryRow, entryCol + n, 9)
                            if num == 9:
                                if entryCol - n >= 0:
                                    puzzle.removeCandidate(entryRow, entryCol - n, 1)
                                if entryCol + n <= 8:
                                    puzzle.removeCandidate(entryRow, entryCol + n, 1)
                        for n in range(possibleLengths[len(possibleLengths) - 1], 9):
                            if num == 1:
                                if entryCol - n - 2 >= 0:
                                    puzzle.removeCandidate(entryRow, entryCol - n, 9)
                                if entryCol + n + 2 <= 8:
                                    puzzle.removeCandidate(entryRow, entryCol + n, 9)
                            if num == 9:
                                if entryCol - n - 2 >= 0:
                                    puzzle.removeCandidate(entryRow, entryCol - n, 1)
                                if entryCol + n + 2 <= 8:
                                    puzzle.removeCandidate(entryRow, entryCol + n, 1)

            if not colSum == -1:
                colOne, colNine = Sandwich.colFind19(puzzle, entryCol)
                if len(colOne) == 1 and len(colNine) == 1:
                    if (not colSum == 0) and (not colSum == 35):
                        diff = abs(colOne[0] - colNine[0]) - 1
                        possibleCol = copy.deepcopy(puzzle.possibleSandwich[1][entryCol])
                        for possibleLength in possibleCol:
                            if not possibleLength == diff:
                                del puzzle.possibleSandwich[1][entryCol][possibleLength]

                        possibleCol = copy.deepcopy(puzzle.possibleSandwich[1][entryCol])
                        cells = []
                        for n in range(min(colOne[0] + 1, colNine[0]), max(colOne[0] + 1, colNine[0])):
                            cells.append((n, entryCol))

                        possibleDigits = []
                        if not possibleCol:
                            return
                        for n in possibleCol[diff]:
                            if not n in possibleDigits:
                                possibleDigits.append(n)
                        
                        for cell in cells:
                            if not puzzle.cellFilled(cell):
                                candidates = copy.deepcopy(puzzle.getCandidates(cell))
                                for cand in candidates:
                                    if not cand in possibleDigits:
                                        puzzle.removeCandidate(cell[0], cell[1], cand)
                else:
                    if colSum == 0:
                        if entryCol > 1:
                            for n in range(entryRow - 1):
                                if num == 1:
                                    puzzle.removeCandidate(n, entryCol, 9)
                                elif num == 9:
                                    puzzle.removeCandidate(n, entryCol, 1)
                        if entryCol < 6:
                            for n in range(entryRow + 2, 9):
                                if num == 1:
                                    puzzle.removeCandidate(n, entryCol, 9)
                                elif num == 9:
                                    puzzle.removeCandidate(n, entryCol, 1)
                    else:
                        possibleLengths = []
                        possibleCol = copy.deepcopy(puzzle.possibleSandwich[1][entryCol])
                        for possibleLength in possibleCol:
                            possibleLengths.append(possibleLength)
                        possibleLengths.sort()
                        if not possibleLengths:
                            return
                        for n in range(possibleLengths[0]):
                            if num == 1:
                                if entryRow - n >= 0:
                                    puzzle.removeCandidate(entryRow - n, entryCol, 9)
                                if entryRow + n <= 8:
                                    puzzle.removeCandidate(entryRow + n, entryCol, 9)
                            if num == 9:
                                if entryRow - n >= 0:
                                    puzzle.removeCandidate(entryRow - n, entryCol, 1)
                                if entryRow + n <= 8:
                                    puzzle.removeCandidate(entryRow + n, entryCol, 1)
                        for n in range(possibleLengths[len(possibleLengths) - 1], 9):
                            if num == 1:
                                if entryRow - n - 2 >= 0:
                                    puzzle.removeCandidate(entryRow - n, entryCol, 9)
                                if entryRow + n + 2 <= 8:
                                    puzzle.removeCandidate(entryRow + n, entryCol, 9)
                            if num == 9:
                                if entryRow - n - 2 >= 0:
                                    puzzle.removeCandidate(entryRow - n, entryCol, 1)
                                if entryRow + n + 2 <= 8:
                                    puzzle.removeCandidate(entryRow + n, entryCol, 1)
        else:
            rowOne, rowNine = Sandwich.rowFind19(puzzle, entryRow)
            if len(rowOne) == 1 and len(rowNine) == 1 and (not puzzle.possibleSandwich[0][entryRow] == -1):
                if entryCol > min(rowOne[0], rowNine[0]) and entryCol < max(rowOne[0], rowNine[0]):
                    if not puzzle.possibleSandwich[0][entryRow]:
                        return
                    elif not abs(rowNine[0] - rowOne[0]) in puzzle.possibleSandwich[0][entryRow]:
                        return
                    comboList = list(puzzle.possibleSandwich[0][entryRow][abs(rowNine[0] - rowOne[0])])
                    for combo in copy.deepcopy(comboList):
                        if not num in combo:
                            comboList.remove(combo)
                    puzzle.possibleSandwich[0][entryRow][abs(rowNine[0] - rowOne[0])] = tuple(comboList)

            colOne, colNine = Sandwich.colFind19(puzzle, entryCol)
            if len(colOne) == 1 and len(colNine) == 1 and (not puzzle.possibleSandwich[1][entryCol] == -1):
                if entryCol > min(colOne[0], colNine[0]) and entryCol < max(colOne[0], colNine[0]):
                    if not puzzle.possibleSandwich[1][entryCol]:
                        return
                    elif not abs(colNine[0] - colOne[0]) in puzzle.possibleSandwich[1][entryCol]:
                        return
                    comboList = list(puzzle.possibleSandwich[1][entryCol][abs(colNine[0] - colOne[0])])
                    for combo in copy.deepcopy(comboList):
                        if not num in combo:
                            comboList.remove(combo)
                    puzzle.possibleSandwich[1][entryCol][abs(colNine[0] - colOne[0])] = tuple(comboList)
        



    def applyCand(puzzle, entryRow, entryCol, candidates):
        val = 0
        return val

    def checkSolution(puzzle):
        for row in range(9):
            one, nine = Sandwich.rowFind19(puzzle, row)
            if (not len(one) == 1) or (not len(nine) == 1):
                return False
            sum = 0
            for n in range(min(one[0], nine[0]) + 1, max(one[0], nine[0])):
                sum += puzzle.getCandidates(row, n)

            if not sum == puzzle.sandwich[0][row]:
                return False
            
        for col in range(9):
            one, nine = Sandwich.colFind19(puzzle, col)
            if (not len(one) == 1) or (not len(nine) == 1):
                return False
            sum = 0
            for n in range(min(one[0], nine[0]) + 1, max(one[0], nine[0])):
                sum += puzzle.getCandidates(col, n)

            if not sum == puzzle.sandwich[1][col]:
                return False
        return True
        

    def rowFind19(puzzle, row):
        one = []
        nine = []
        for col in range(9):
            cands = puzzle.getCandidates([row, col])
            if puzzle.cellFilled([row, col]):
                if cands == 1:
                    one.append(col)
                elif cands == 9:
                    nine.append(col)
            else:
                if 1 in cands:
                    one.append(col)
                if 9 in cands:
                    nine.append(col)
        return one, nine
    
    def colFind19(puzzle, col):
        one = []
        nine = []
        for row in range(9):
            cands = puzzle.getCandidates([row, col])
            if puzzle.cellFilled([row, col]):
                if cands == 1:
                    one.append(row)
                elif cands == 9:
                    nine.append(row)
            else:
                if 1 in cands:
                    one.append(row)
                if 9 in cands:
                    nine.append(row)
        return one, nine

    def remove19(puzzle, row, col):
        if not puzzle.cellFilled([row, col]):
            candidates = puzzle.getCandidates([row, col])
            if 1 in candidates:
                puzzle.removeCandidate(row, col, 1)
            if 9 in candidates:
                puzzle.removeCandidate(row, col, 9)

    def rowRemove19(puzzle, row):
        if puzzle.sandwich[0][row] >= 22:
                Sandwich.remove19(row, 4)
                if puzzle.sandwich[0][row] >= 27:
                    Sandwich.remove19(row, 3)
                    Sandwich.remove19(row, 5)
                    if puzzle.sandwich[0][row] >= 31:
                        Sandwich.remove19(row, 2)
                        Sandwich.remove19(row, 6)
                        if puzzle.sandwich[0][row] == 35:
                            Sandwich.remove19(row, 1)
                            Sandwich.remove19(row, 7)
                            if not puzzle.cellFilled([row, 0]):
                                candidates = copy.deepcopy(puzzle.getCandidates([row, 0]))
                                for cand in candidates:
                                    if (not cand == 1) or (not cand == 9):
                                        puzzle.removeCandidate(row, 0, cand)
                            if not puzzle.cellFilled([row, 8]):
                                candidates = copy.deepcopy(puzzle.getCandidates([row, 8]))
                                for cand in candidates:
                                    if (not cand == 1) or (not cand == 9):
                                        puzzle.removeCandidate(row, 8, cand)

    def colRemove19(puzzle, col):
        if puzzle.sandwich[1][col] >= 22:
                Sandwich.remove19(4, col)
                if puzzle.sandwich[1][col] >= 27:
                    Sandwich.remove19(3, col)
                    Sandwich.remove19(5, col)
                    if puzzle.sandwich[1][col] >= 31:
                        Sandwich.remove19(2, col)
                        Sandwich.remove19(6, col)
                        if puzzle.sandwich[1][col] == 35:
                            Sandwich.remove19(1, col)
                            Sandwich.remove19(7, col)
                            if not puzzle.cellFilled([0, col]):
                                candidates = copy.deepcopy(puzzle.getCandidates([0, col]))
                                for cand in candidates:
                                    if (not cand == 1) or (not cand == 9):
                                        puzzle.removeCandidate(0, col, cand)
                            if not puzzle.cellFilled([8, col]):
                                candidates = copy.deepcopy(puzzle.getCandidates([8, col]))
                                for cand in candidates:
                                    if (not cand == 1) or (not cand == 9):
                                        puzzle.removeCandidate(8, col, cand)