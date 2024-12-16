# NeovIM

Flaggan är en simulering av spelet nim.<br>
https://en.wikipedia.org/wiki/Nim<br>
Spelet är löst, vilket betyder att spelaren som börjar vinner om den spelar optimalt. Minsta fel drag resulterar i att maskinen vinner. Man vinner genom att beräkna summan av varje rad, och därefter xora varje rad.<br>
Nimsumman som är kvar måste tas bort från en rad. Målet är att lämna motståndaren med en nimsumma av 0. När man når en vinnande position, som definieras med:<br>
```python
        countOnes = self.boardState.count(1)
        countZeroes = self.boardState.count(0)

        if countOnes + countZeroes + 1 == len(self.boardState):
           if countOnes % 2 == 1:
                return 1
            return 2
        if countZeroes + 1 == len(self.boardState) and countOnes != 1:
            return 2
        ...
        
        if winnibleRes == 1:
            return biggestRow, maxValue
        if winnibleRes == 2:
            return biggestRow, maxValue - 1
```
Följer man den för att vinna. <br>
Spel ett är för att testa så att spelaren har koll på reglerna och vet hur man spelar optimalt.<br>
Spel två är mycket större och hade varit svårt att spela för hand och medför att man behöver ett program om man inte vill spela för länge.<br>
(Jag är osäker om man ska sätta en tidsgräns på drag för att göra att man behöver scripta det, men det kan vara roligt om nån löser det by hand).<br>
Solve.py löser ut flaggan. <br>
