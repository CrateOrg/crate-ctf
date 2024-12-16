#!/usr/bin/env python3
class Nim:
    def __init__(self, n):
        self.boardState = [2*i+1 for i in range(n)]
    def render(self):
        m = max(self.boardState)
        for i, row in enumerate(self.boardState):
            isDoubleDigit = 1
            if i >= 10:
                isDoubleDigit = 0
            print(i, " "*(m-row+isDoubleDigit), "| "*row)
        print("\n")
    def turn(self, row, n):
        if(row >= 0 and row <= len(self.boardState) and n > 0 and n <= self.boardState[row]):
            self.boardState[row] -= n
            return 0
        else:
            return 1
    def winnable(self):
        countOnes = self.boardState.count(1)
        countZeroes = self.boardState.count(0)

        if countOnes + countZeroes + 1 == len(self.boardState):
            if countOnes % 2 == 1:
                return 1
            return 2 
        if countZeroes + 1 == len(self.boardState) and countOnes != 1: 
            return 2
        
        return 0
    def optimalTurn(self):
        nimsum = 0
        for i, row in enumerate(self.boardState):
            if i == 0:
                nimsum = row
                continue
            else:
                nimsum ^= row

        maxValue = max(self.boardState)
        biggestRow = self.boardState.index(maxValue)

        winnibleRes = self.winnable()
        if winnibleRes == 1:
            return biggestRow, maxValue
        if winnibleRes == 2:
            return biggestRow, maxValue - 1

        if nimsum == 0:
            return biggestRow, 1
        for i, row in enumerate(self.boardState):

            if row & nimsum == nimsum:
                return i, nimsum
            else:
                toBeremoved = row ^ nimsum
                if toBeremoved <= row:
                    return i, row - toBeremoved

    def checkWin(self):
        if max(self.boardState) == 0:
            return True
        return False
def nimLoop(game):
    while True:
        game.render()
        inp = input("Skriv in rad och hur många tändstickor som skall plockas ([rad] [n], exempel \"3 2\"): ").split(" ")
        if (len(inp) != 2):
            print("Fel format")
            continue
        try:
            row = int(inp[0])
            n = int(inp[1])
            res = game.turn(row, n)
            if res:
                print("Ogiltigt drag")
                continue
            nim.render()
            if game.checkWin():
                return 1
            machineRow, machineN = game.optimalTurn()
            print("Motståndardrag {} {}\n".format(machineRow, machineN))
            
            game.turn(machineRow, machineN)
            if game.checkWin():
                return 0

        except: 
            print("Skriv in två tal")
print("\n", "*-"*8, "NIM", "*-"*8, "\n")
print("Varje runda väljer spelaren en rad, från denna rad måste spelaren välja att ta minst 1 sticka men får ta fler.")
print("Spelaren som tar sista stickan förlorar.\n")
nim = Nim(5)
nimres = nimLoop(nim)
if nimres:
    print("Vilken otur, jag slog dig denna gång.")
    exit()
print("Snyggt vinst, nu när du kan reglerna är det dags för runda 2.")
nim = Nim(51)
nimres = nimLoop(nim)
if nimres: 
    print("Vilken otur, jag slog dig denna gång.")
    exit()
print("Grattis. cratectf{Write_:wq_to_exit_neovim}")
