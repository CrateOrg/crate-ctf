# ZKP
Utmaningen ar ett Zero knowledge proof som man kan ta sönder. Baserat på https://en.wikipedia.org/wiki/Zero-knowledge_proof och det diskreta log problemet. För att bestämma vilken typ av utmaning den ska fråga efter seedar den tiden när på millisekunden.
Pga klockdrift så läcker den sin interna tid i containern, och därefter väntar den på input från användaren och tar ut en ny tid.
Därför kommer klockan som seedas vara (läckt tid + rtt av ett tcp packet). Rtt:en lokalt är ca 1 ms, när Rtt har blivit testat mot andra hemsidor så driftar den med ca 3 ms.
Se Solve.py för full lösning.
