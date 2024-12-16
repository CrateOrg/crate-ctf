# Uppvärmning

Uppgiften är inspirerad av filförvaring från Crate-CTF 2022, på samma sätt så kan den lösas med en SMT-lösare, som z3. Inputen består av 32 knappar som är på eller av, efter varje gång man har lyckats så sparas det en historik av vinsten du använde. I och med att buffern av historik växer, så allokeras mer och mer minne. Efter att man förlorar frias detta minne. Flaggan printas inte när man vinner men den laddas in i en buffer. Genom att vinna tillräckligt många gånger och sen förlora med mening, kan man se till att flaggbuffern och historikbuffern är en del av samma chunk i heapens fast-bin. Flag kommer då få historikens gamla pekare och det leder till en use-after-free.

# Todo

Jag är osäker om man borde kompilera binären med eller utan symbol obfuskering. Eller bara ge ut C-filen ifall den är för svår. 
