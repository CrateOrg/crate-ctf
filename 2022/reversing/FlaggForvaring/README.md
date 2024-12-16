# Flaggförvaring

Flaggan ligger lagrad i en textfil som bara kan läsas genom att interagera med ett program som körs på challengeservern. Programmet skriver ut flaggan om man anger en giltig licensnyckel först, vilken deltagarna inte har. Genom att reversera licensnyckelkontrollen i det kompilerade programmet kan en serie regler fås fram som visar hur nyckeln är uppbyggd. T.ex. "nyckelns 9:e tecken är detsamma som det 11:e och 13:e", "summan av alla tecken i nyckeln är 0x51C", "tecknet på plats 8 är lika med: (värdet av tecknet på plats 18) + 5".

Med hjälp av en "satisfierbarhet modulo teorier (SMT)"-lösare, t.ex. [Z3](https://github.com/Z3Prover/z3), kan man mata in alla regler och få ut exempel på tilldelningar (licensnycklar) som uppfyller alla krav. Det finns 160 sådana nycklar som uppgiften kommer att acceptera som giltiga.
