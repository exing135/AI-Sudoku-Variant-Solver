
import copy
from puzzle import Puzzle
from sudokuRules import SudokuRules

class SudokuSolver:
    variants = [] # 0 classic, 1 arrow, 2 chess knight, 3 killer, 4 nonconsecutive, 5 palindrome, 6 sandwich, 7 thermo
    puzzle = None
    solution = []
    rules = None

    guesses = []

    trace = False

    def __init__(self):
        pass

    def solvePuzzle(self, filename):
        self.readPuzzle(filename)
        # return

        while not self.puzzle.isCorrect():
            val = 1
            while (val == 1):
                val = self.rules.apply(self.puzzle)
                if self.trace:
                    print('puzzle')
                    self.puzzle.printPuzzle()
                    print('\n')
                pass
            
            if val == -1:
                if self.guesses:
                    lastGuess = self.guesses.pop()
                    self.puzzle = lastGuess[0]
                    self.puzzle.removeCandidate(lastGuess[1], lastGuess[2], lastGuess[3])
                else:
                    print('error - no solution found')
                break
            
            # self.puzzle.printPuzzle()
            if not self.puzzle.isComplete():
                self.makeGuess()
                if self.trace:
                    print('guess')
                    lastGuess = self.guesses[len(self.guesses) - 1]
                    lastGuess[0].printPuzzle()
                    print(f'Guessed digit {lastGuess[3]} at row {lastGuess[1] + 1}, column {lastGuess[2] + 1}')
                    print('\n')
                pass

            elif not self.puzzle.isCorrect():
                if self.guesses:
                    lastGuess = self.guesses.pop()
                    if self.trace:
                        print('backtrack')
                        self.puzzle.printPuzzle()
                        print(f'Backtracked on last guess of digit {lastGuess[3]} at row {lastGuess[1] + 1}, column {lastGuess[2] + 1}, restored puzzle to:')
                        lastGuess[0].printPuzzle()
                        print('\n')

                    self.puzzle = lastGuess[0]
                    self.puzzle.removeCandidate(lastGuess[1], lastGuess[2], lastGuess[3])
                else: 
                    print('error - no solution found')
                    break
        if self.puzzle.isCorrect():
            print("Puzzle solved!")
            self.printSolution()

    def cellCorrect(self, numRow, numCol, num):
        if num == self.solution[numRow][numCol]:
            return True
        else:
            return False
                        


            

    def solveAll(self, filename):
        pass

    def readPuzzle(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()

        row = 0
        variantLines = 0
        variantData = []
        for line in lines:
            if row == 0:
                for num in line.strip():
                    self.variants.append(int(num))
                self.rules = SudokuRules(self.variants)
                self.puzzle = Puzzle(self.rules)

                if self.variants[1] == 1:
                    variantLines += 1
                if self.variants[3] == 1:
                    variantLines += 1
                if self.variants[5] == 1:
                    variantLines += 1
                if self.variants[6] == 1:
                    variantLines += 1
                if self.variants[7] == 1:
                    variantLines += 1

            elif row < 10:
                col = 0
                for num in line.strip():
                    if not int(num) == 0:
                        self.puzzle.fillCell(row - 1, col, int(num))
                    col += 1

            elif row < 10 + variantLines:
                variantData.append(line.strip())

            row += 1

        if not len(variantData) == 0:
            var = 1
            dataPos = 0
            while var < 8:
                if self.variants[var] == 1:
                    if var == 1: # arrow
                        dataStr = variantData[dataPos].strip()
                        self.parseArrow(dataStr)
                        dataPos += 1

                    if var == 3: # killer
                        dataStr = variantData[dataPos].strip()
                        self.parseKiller(dataStr)
                        dataPos += 1

                    if var == 5: # palindrome
                        dataStr = variantData[dataPos].strip()
                        self.parsePalindrome(dataStr)
                        dataPos += 1

                    if var == 6: # sandwich
                        dataStr = variantData[dataPos].strip()
                        self.parseSandwich(dataStr)
                        dataPos += 1

                    if var == 7: # thermo
                        dataStr = variantData[dataPos].strip()
                        self.parseThermo(dataStr)
                        dataPos += 1

                var += 1

    def readSolution(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()

        row = 0
        for line in lines:
            col = 0
            self.solution.append([])
            for num in line.strip():
                self.solution[row].append(int(num))
                col += 1

            row += 1
    
    def parseArrow(self, dataStr):
        dataStr = dataStr.replace(' ', '')

        data = []
        arrow = []
        arrowPos = ''
        for char in dataStr:
            if char == '[':
                arrowPos = ''
            elif char == ',':
                if not arrowPos == '':
                    arrow.append((int(arrowPos[0]) - 1, int(arrowPos[1]) - 1))
                    arrowPos = ''
            elif char == ']':
                arrow.append((int(arrowPos[0]) - 1, int(arrowPos[1]) - 1))
                data.append(tuple(arrow))
                arrow = []
                arrowPos = ''
            else:
                arrowPos += char

        self.puzzle.arrow = copy.deepcopy(data)

        self.puzzle.possibleArrow = {}
        for a in self.puzzle.arrow:
            self.puzzle.possibleArrow[tuple(a)] = copy.deepcopy(self.rules.arrowCombos[len(a) - 1])

    def parseKiller(self, dataStr):
        dataStr = dataStr.replace(' ', '')

        data = []
        killerCage = []
        killerCells = []
        killerSum = ''
        killerPos = ''
        for char in dataStr:
            if char == '[':
                if not killerCage:
                    killerSum = ''
                    killerPos = ''
            elif char == ',':
                if killerSum == '':
                    pass
                elif killerPos == '':
                    killerSum = int(killerSum)
                    killerCage.append(killerSum)
                else:
                    killerCells.append((int(killerPos[0]) - 1, int(killerPos[1]) - 1))
                    killerPos = ''
            elif char == ']':
                if not killerPos == '':
                    killerCells.append((int(killerPos[0]) - 1, int(killerPos[1]) - 1))
                    killerCage.append(tuple(killerCells))
                    data.append(tuple(killerCage))
                    killerCage = []
                    killerCells = []
                    killerSum = ''
                    killerPos = ''
            else:
                if type(killerSum) == str:
                    killerSum += char
                else:
                    killerPos += char

        self.puzzle.killer = copy.deepcopy(data)

        self.puzzle.possibleKiller = {}
        for cage in self.puzzle.killer:
            sum = cage[0]
            cells = cage[1]
            combos = self.rules.cageCombos[len(cells)][sum]
            self.puzzle.possibleKiller[tuple(cage)] = tuple(combos)

    def parsePalindrome(self, dataStr):
        dataStr = dataStr.replace(' ', '')

        data = []
        palindromeLine = []
        palindromePos = ''
        for char in dataStr:
            if char == '[':
                palindromeLine = []
                palindromePos = ''
            elif char == ',':
                if palindromePos == '':
                    pass
                else:
                    palindromeLine.append([int(palindromePos[0]) - 1, int(palindromePos[1]) - 1])
                    palindromePos = ''
            elif char == ']':
                palindromeLine.append([int(palindromePos[0]) - 1, int(palindromePos[1]) - 1])
                data.append(copy.deepcopy(palindromeLine))
                palindromeLine = []
                palindromePos = ''
            else:
                palindromePos += char

        self.puzzle.palindrome = copy.deepcopy(data)

    def parseSandwich(self, dataStr):
        dataStr = dataStr.replace(' ', '')
        self.puzzle.sandwich = []
        i = 0
        num = ''
        for char in dataStr:
            if char == '[':
                self.puzzle.sandwich.append([])
            elif char == ',':
                if not num == '':
                    self.puzzle.sandwich[i].append(int(num))
                    num = ''
            elif char == ']':
                if not num == '':
                    self.puzzle.sandwich[i].append(int(num))
                    num = ''
                i += 1
            elif char == '-':
                self.puzzle.sandwich[i].append(-1)
            else:
                num += char

        sumList0 = []
        for sum in self.puzzle.sandwich[0]:
            if sum == -1 or sum == 0:
                sumList0.append(sum)
            else:
                sumCombos = {}
                for sandwichLength in self.rules.sandwichCombos:
                    if sum in self.rules.sandwichCombos[sandwichLength]:
                        sumCombos[sandwichLength] = self.rules.sandwichCombos[sandwichLength][sum]
                sumList0.append(sumCombos)
        self.puzzle.possibleSandwich[0] = tuple(sumList0)

        sumList1 = []
        for sum in self.puzzle.sandwich[1]:
            if sum == -1 or sum == 0:
                sumList1.append(sum)
            else:
                sumCombos = {}
                for sandwichLength in self.rules.sandwichCombos:
                    if sum in self.rules.sandwichCombos[sandwichLength]:
                        sumCombos[sandwichLength] = self.rules.sandwichCombos[sandwichLength][sum]
                sumList1.append(sumCombos)
        self.puzzle.possibleSandwich[1] = tuple(sumList1)
        # print(self.puzzle.possibleSandwich)


    def parseThermo(self, dataStr):
        dataStr = dataStr.replace(' ', '')

        data = []
        thermoLine = []
        thermoPos = ''
        for char in dataStr:
            if char == '[':
                thermoLine = []
                thermoPos = ''
            elif char == ',':
                if thermoPos == '':
                    pass
                else:
                    thermoLine.append([int(thermoPos[0]) - 1, int(thermoPos[1]) - 1])
                    thermoPos = ''
            elif char == ']':
                thermoLine.append([int(thermoPos[0]) - 1, int(thermoPos[1]) - 1])
                data.append(copy.deepcopy(thermoLine))
                thermoLine = []
                thermoPos = ''
            else:
                thermoPos += char

        self.puzzle.thermo = copy.deepcopy(data)


    def makeGuess(self):
        minLen = 9
        for row in range(9):
            for col in range(9):
                if type(self.puzzle.grid[row][col]) is list:
                    minLen = min(minLen, len(self.puzzle.grid[row][col]))

        guess = None
        for row in range(9):
            for col in range(9):
                if type(self.puzzle.grid[row][col]) is list and len(self.puzzle.grid[row][col]) == minLen:
                    guess = [copy.deepcopy(self.puzzle), row, col, self.puzzle.grid[row][col][0]]
                    self.guesses.append(guess)
                    self.puzzle.fillCell(row, col, self.puzzle.grid[row][col][0])
                    break
            if not guess == None:
                break
    
    def printTrace(self, trace):
        self.trace = trace
    
    def printSolution(self):
        print('-------------------------------------')
        for row in range(9):
            rowStr = '|'
            for col in range(9):
                rowStr += ' ' + str(self.puzzle.grid[row][col]) + ' |'
            print(rowStr)
            print('-------------------------------------')