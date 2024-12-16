#!/usr/bin/env python3
from pwn import *
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

        if countOnes + countZeroes + 1 == len(self.boardState) and countOnes % 2 == 1:
            return 1
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

        print("nimsum", nimsum)
        maxValue = max(self.boardState)
        biggestRow = self.boardState.index(maxValue)

        winnibleRes = self.winnable()
        if winnibleRes == 1:
            print("winnible: ", winnibleRes)
            return biggestRow, maxValue
        if winnibleRes == 2:
            return biggestRow, maxValue - 1

        if nimsum == 0:
            return biggestRow, 1
        for i, row in enumerate(self.boardState):
            if row & nimsum == nimsum:
                #print("moves 2")
                return i, nimsum
            else:
                toBeremoved = row ^ nimsum
                if toBeremoved <= row:
                    print("To be removed: ", toBeremoved, nimsum, row) 
                    return i, row - toBeremoved

    def checkWin(self):
        if max(self.boardState) == 0:
            return True
        return False

r = remote("localhost", 50002)

nim = Nim(5)

while True:
    res = r.recvuntil(":")
    turnRow, turnN = nim.optimalTurn()
    r.sendline("{} {}".format(turnRow, turnN))
    print("making turn: ", turnRow, turnN)
    nim.turn(turnRow, turnN)
    

    r.recvuntil("drag ")
    enemyMove = r.recvuntil("\n").split(b" ")
    print("enemy move captured: ", enemyMove)
    nim.turn(int(enemyMove[0]), int(enemyMove[1]))
    nim.render()
    if nim.checkWin():
        r.recvuntil("runda 2")
        print("Game won, exiting")
        break
print("game 2 started\n")
nim = Nim(51)
while True:
    r.recvuntil(":")
    turnRow, turnN = nim.optimalTurn()
    r.sendline("{} {}".format(turnRow, turnN))
    print("making turn: ", turnRow, turnN)
    nim.turn(turnRow, turnN)
    if nim.checkWin():
        break

    r.recvuntil("drag ")
    enemyMove = r.recvuntil("\n").split(b" ")
    print("enemy move captured: ", enemyMove)
    nim.turn(int(enemyMove[0]), int(enemyMove[1]))
    nim.render()
    if nim.checkWin():
        print("Game won, exiting")
        break
r.interactive()

