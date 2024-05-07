
from variants.classic import Classic
from variants.arrow import Arrow
from variants.knight import Knight
from variants.killer import Killer
from variants.nonconsecutive import Nonconsecutive
from variants.palindrome import Palindrome
from variants.sandwich import Sandwich
from variants.thermo import Thermo
import copy

class SudokuRules:
    variants = [] # 0 classic, 1 arrow, 2 chess knight, 3 killer, 4 nonconsecutive, 5 palindrome, 6 sandwich, 7 thermo
    arrowCombos = {}
    cageCombos = {}
    sandwichCombos = {}

    def __init__(self, vars):
        self.variants = vars
        if vars[1] == 1:
            self.setArrowCombos()
            # print(self.arrowCombos)
        if vars[3] == 1:
            self.setCageCombos()
            # print(self.cageCombos)
        if vars[6] == 1:
            self.setSandwichCombos()
            # print(self.sandwichCombos)

    def setCageCombos(self):
        file = open('variants/killerSums.txt', 'r')
        lines = file.readlines()

        cellCount = 0
        sumDict = {}
        for line in lines:

            if 'Cell Cage' in line:
                cellCount += 1
                if cellCount > 9:
                    break
                if cellCount > 1:
                    self.cageCombos[cellCount - 1] = sumDict
                    sumDict = {}
            elif not line.strip() == '':
                sum = ''
                comboStr = ''
                comboList = []
                for char in line.strip():
                    if char == '—':
                        sum = int(sum)
                    elif char == ' ':
                        if comboStr == '':
                            pass
                        else:
                            combo = []
                            for num in comboStr:
                                combo.append(int(num))
                            comboList.append(combo)
                            comboStr = ''
                    else:
                        if type(sum) == str:
                            sum += char
                        else:
                            comboStr += char
                    
                if not comboStr == '':
                    combo = []
                    for num in comboStr:
                        combo.append(int(num))
                    comboList.append(combo)
                    comboStr = ''
                sumDict[sum] = tuple(comboList)

    def setArrowCombos(self):
        self.arrowCombos[1] = {1: ([1],), 2: ([2],), 3: ([3],), 4: ([4],), 5: ([5],), 6: ([6],), 7: ([7],), 8: ([8],), 9: ([9],)}
        for arrowLength in range(2, 10):
            sumDict = {}
            for arrowSum in range(arrowLength, 10):
                combos = self.combination(arrowLength, arrowSum - arrowLength + 1, 0)
                uniqueCombos = []
                for combo in combos:
                    combo.sort()
                    if not combo in uniqueCombos:
                        sum = 0
                        for n in combo:
                            sum += n
                            if sum > arrowSum:
                                sum = 0
                                break
                        if not sum == 0 and sum == arrowSum:
                            uniqueCombos.append(combo)
                sumDict[arrowSum] = tuple(uniqueCombos)
            self.arrowCombos[arrowLength] = sumDict
    
    def setSandwichCombos(self):
        self.setCageCombos()
        self.sandwichCombos = copy.deepcopy(self.cageCombos)
        self.sandwichCombos[1] = {2: (2,), 3: (3,), 4: (4,), 5: (5,), 6: (6,), 7: (7,), 8: (8,)}
        for sandwichLength in copy.deepcopy(self.sandwichCombos):
            if sandwichLength > 7:
                del self.sandwichCombos[sandwichLength]
            else:
                for sandwichSum in copy.deepcopy(self.sandwichCombos[sandwichLength]):
                    if sandwichSum > 35:
                        del self.sandwichCombos[sandwichLength][sandwichSum]
                    elif not sandwichLength == 1:
                        combos = list(copy.deepcopy(self.sandwichCombos[sandwichLength][sandwichSum]))
                        for combo in copy.deepcopy(combos):
                            if 1 in combo or 9 in combo:
                                combos.remove(combo)
                        if not combos:
                            del self.sandwichCombos[sandwichLength][sandwichSum]
                        else:
                            self.sandwichCombos[sandwichLength][sandwichSum] = tuple(combos)
                            



    def combination(self, maxDepth, maxVal, currentDepth):
        currentDepth += 1
        combos = []
        newCombos = []
        if currentDepth < maxDepth - 1:
            combos = self.combination(maxDepth, maxVal, currentDepth)
        else:
            for n in range(1, maxVal + 1):
                combos.append([n])
        
        for c in combos:
            for n in range(maxVal):
                newC = copy.deepcopy(c)
                newC.append(n + 1)
                newCombos.append(newC)
        
        return newCombos
            




    def apply(self, puzzle):
        val = 0
        if self.variants[0] == 1:
            newVal = Classic.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)
            
        if self.variants[1] == 1:
            newVal = Arrow.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        if self.variants[2] == 1:
            newVal = Knight.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        if self.variants[3] == 1:
            newVal = Killer.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        if self.variants[4] == 1:
            newVal = Nonconsecutive.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        if self.variants[5] == 1:
            newVal = Palindrome.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        if self.variants[6] == 1:
            newVal = Sandwich.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        if self.variants[7] == 1:
            newVal = Thermo.apply(puzzle)
            if (newVal == -1):
                return newVal
            else:
                val = max(newVal, val)

        return val
            
    def applyCell(self, puzzle, entryRow, entryCol, num):
        if self.variants[0] == 1:
            Classic.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[1] == 1:
            Arrow.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[2] == 1:
            Knight.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[3] == 1:
            Killer.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[4] == 1:
            Nonconsecutive.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[5] == 1:
            Palindrome.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[6] == 1:
            Sandwich.applyCell(puzzle, entryRow, entryCol, num)
        if self.variants[7] == 1:
            Thermo.applyCell(puzzle, entryRow, entryCol, num)

    def applyCand(self, puzzle, entryRow, entryCol, candidates):
        val = 0
        if self.variants[0] == 1:
            newVal = Classic.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[1] == 1:
            newVal = Arrow.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[2] == 1:
            newVal = Knight.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[3] == 1:
            newVal = Killer.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[4] == 1:
            newVal = Nonconsecutive.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[5] == 1:
            newVal = Palindrome.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[6] == 1:
            newVal = Sandwich.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        if self.variants[7] == 1:
            newVal = Thermo.applyCand(puzzle, entryRow, entryCol, candidates)
            if newVal == -1:
                return newVal
            else:
                val = max(newVal, val)
        return newVal

    def checkSolution(self, puzzle):
        if self.variants[0] == 1:
            if (not Classic.checkSolution(puzzle)):
                return False
        if self.variants[1] == 1:
            if (not Arrow.checkSolution(puzzle)):
                return False
        if self.variants[2] == 1:
            if (not Knight.checkSolution(puzzle)):
                return False
        if self.variants[3] == 1:
            if (not Killer.checkSolution(puzzle)):
                return False
        if self.variants[4] == 1:
            if (not Nonconsecutive.checkSolution(puzzle)):
                return False
        if self.variants[5] == 1:
            if (not Palindrome.checkSolution(puzzle)):
                return False
        if self.variants[6] == 1:
            if (not Sandwich.checkSolution(puzzle)):
                return False
        if self.variants[7] == 1:
            if (not Thermo.checkSolution(puzzle)):
                return False
            
        return True