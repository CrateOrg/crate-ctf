# Corduroy

Flaggan i ASCII-format är kodad enligt [Manchesterkodningen](https://en.wikipedia.org/wiki/Manchester_code) som används i äldre versioner av Ethernet och i äldre typer av hemautomationsutrustning, t.ex. fjärrströmbrytare och temperaturgivare. Varje bit i flaggan kodas så att 0 -> 10 och 1 -> 01 och den resulterande bitströmmen har sedan amplitudmodulerats till en ljudfil och blandats med lite bakgrundljud.

Med t.ex. brusreduceringen ifrån Audacity kan bakgrundljudet minskas så att signalen framträder tydligt. Sedan kan man med ett skript (eller manuellt med mycket tålamod) leta efter varje stigning och fall i signalen och återskapa bitarna i flaggan.
