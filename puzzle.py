
class Puzzle:
    grid = [[], [], [], [], [], [], [], [], []]
    rules = None

    arrow = []
    killer = []
    palindrome = []
    sandwich = []
    thermo = []

    possibleArrow = {}
    possibleKiller = {} # key cage val combos
    possibleSandwich = {}

    stop = False

    def __init__(self, rules):
        self.grid = [[], [], [], [], [], [], [], [], []]
        self.rules = rules
        for row in range(9):
            for col in range(9):
                self.grid[row].append([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def printPuzzle(self):
        for row in range(9):
            print(self.grid[row])
                    
    def fillCell(self, entryRow, entryCol, num):
        self.grid[entryRow][entryCol] = num
        self.rules.applyCell(self, entryRow, entryCol, num)
    
    def removeCandidate(self, entryRow, entryCol, num):
        if not self.cellFilled([entryRow, entryCol]) and self.cellContains([entryRow, entryCol], num):
            self.grid[entryRow][entryCol].remove(num)
            if len(self.grid[entryRow][entryCol]) == 1:
                self.fillCell(entryRow, entryCol, self.grid[entryRow][entryCol][0])
            else:
                self.rules.applyCand(self, entryRow, entryCol, self.grid[entryRow][entryCol])
            return 1
        else:
            return 0
        
    def removeArrowSum(self, arrow, sum):
        arrow = tuple(arrow)

        if sum in self.possibleArrow[arrow]:
            del self.possibleArrow[arrow][sum]
            return 1
        return 0
        
    # count = 0
    def removeArrowCombo(self, arrow, sum, combo):
        arrow = tuple(arrow)
        # if arrow == ((1, 5), (2, 4), (1, 3)) and sum == 8 and combo == [3, 5]:
        #     pass
        # if self.count == 0:
        #     self.count += 1
        if sum in self.possibleArrow[arrow]:
            combos = list(self.possibleArrow[arrow][sum])
            if combo in combos:
                combos.remove(combo)
                if combos:
                    self.possibleArrow[arrow][sum] = tuple(combos)
                else:
                    del self.possibleArrow[arrow][sum]
                return 1
        return 0
        
    def removeKillerCombo(self, cage, combo):
        cage = tuple(cage)
        if len(self.possibleKiller[cage]) > 1:
            combos = list(self.possibleKiller[cage])
            if combo in combos:
                combos.remove(combo)
                self.possibleKiller[cage] = tuple(combos)
                return 1
        return 0
        
    def isComplete(self):
        for row in range(9):
            for col in range(9):
                if not self.cellFilled([row, col]):
                    return False
        return True
    
    def isCorrect(self):
        if not self.isComplete():
            return False
        return self.rules.checkSolution(self)
    
    def cellContains(self, cell, num):
        if not self.cellFilled(cell) and num in self.getCandidates(cell):
            return True
        else:
            return False
        
    def cellFilled(self, cell):
        if type(self.grid[cell[0]][cell[1]]) is int:
            return True
        else:
            return False
        
    def cageFilled(self, cage):
        for cell in cage[1]:
            if not self.cellFilled(cell):
                return False
        return True
    
    def arrowFilled(self, arrow):
        for cell in arrow:
            if not self.cellFilled(cell):
                return False
        return True
        
    # return candidates of a certain cell
    def getCandidates(self, cellCoords):
        return self.grid[cellCoords[0]][cellCoords[1]]
    
    # return first row/column of a box
    def getBox(self, rowCol):
        return rowCol - (rowCol % 3)
    
    def getArrows(self, findCell):
        arrows = []
        for arrow in self.arrow:
            for cell in arrow:
                if cell == tuple(findCell):
                    arrows.append(arrow)
                    break
        return arrows
    
    # return list of cages that include a particular cell
    def getCages(self, findCell):
        cages = []
        for cage in self.killer:
            for cell in cage[1]:
                if cell == tuple(findCell):
                    cages.append(cage)
                    break
        return cages
    
    