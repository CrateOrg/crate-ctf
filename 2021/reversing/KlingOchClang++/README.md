# Kling och Clang++
Man får LLVM IR för ett program.

Tänkt lösning: kompilera färdigt (`clang++ main.ll`) och kör. Då kan man se att den skriver ut "Almost there...". Kör man det kompilerade programmet genom en dekompilator eller en disassemly så kan man se att den har en if-stats som skriver ut det meddelandet om den evalueras negativt. Ändra på ifsatsen för att köra den andra grenen, som skriver ut flaggan.

Utmaningar: Identifiera att det är LLVM IR det rör sig om, komma på hur man kompilerar den, komma på hur man kommer åt flaggan (det är ett stort program i och med C++, men det mesta är ju ointressant)
