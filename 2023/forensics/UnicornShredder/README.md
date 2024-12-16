## UNICORN SHREDDER
Webapp för strimling av bildfiler.
Bild laddas upp till webserver, strimlas och placeras i hinken för strimlade filer.

Funktionen som strimlar delar upp bilden i 30x30px rutor och slumpar var de ska vara.
Algoritmen är dock dålig och kan bara strimlas på tio olika sätt.

Bild på flaggan är strimlad i "förväg" och finns tillgänglig för allmänhetens beskådan.

### TODO?
Implementera flera algoritmer?
  - 1px breda faktiska STRIMLOR? då slipper man göra resize på bilden.
  - 5x5px breda microfyrkanter?
  - lägg till i POST/API/dropdownmeny

## Lösningsförslag
Gör en lika stor bild som flaggbilden man hittar i hinken. Gör någon slags identifiering i varje 30x30px ruta som är lätt att identifera mha script.
Strimla ett gäng gånger, inse att det bara finns tio olika utfall och gör ett script som bygger ihop bilder utifrån en strimlad bild.

## Kuriosa
95% av all kod är genererad av chat-gpt.
Loggan är genererad av stable diffusion.
