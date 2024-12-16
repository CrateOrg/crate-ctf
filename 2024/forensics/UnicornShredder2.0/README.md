## UNICORN SHREDDER 2.0
Webapp för strimling av bildfiler.
Bild laddas upp till webserver, strimlas och placeras i hinken för strimlade filer.

Funktionen som strimlar delar upp bilden i strimlor a 1px breda och slumpar var de ska vara.
Algoritmen är dock dålig och kan bara strimlas på tio olika sätt.

Bild på flaggan är strimlad i "förväg" och finns tillgänglig för allmänhetens beskådan.

## Lösningsförslag
Gör en lika stor bild som flaggbilden man hittar i hinken. Gör någon slags identifiering i varje 1px kolumn som är lätt att identifera mha script.
Strimla ett gäng gånger, inse att det bara finns tio olika utfall och gör ett script som bygger ihop bilder utifrån en strimlad bild.

## Kuriosa
Baserad på 2023 års unicorn shredder, där 95% av all kod genererades av chat-gpt.
