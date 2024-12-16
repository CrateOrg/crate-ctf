# Webb

### Osynlig text
På startsidan finns en flagga som HTML-kommentar.

### Huvudet på skaft
På olika HTTP-koder kan man hitta delar av flaggan i HTTP-headers som skickas från servern.
Del 1: http://web01.2020ctf.crate.foi.se:8080/hello.php (200)
Del 2: http://web01.2020ctf.crate.foi.se:8080/wp-login.php (301)
Del 3: http://web01.2020ctf.crate.foi.se:8080/404.php (404)

### The dogs web
Ledtråden syftar på att hundens enhet har User-Agent som identifierar hundens ras.
Om man ansluter med strängen "Spaniel" i User-Agent skickas man vidare till en bild på flaggan.

### Meddelande
På undersidan där man kan skicka meddelande körs kod som tar in indata och kör genom php system(). I filen drop_message.php finns flaggan som kommentar, så exekvera "cat drop_message.php" för att få flaggan.


# Kryptografi

### Rot13
Se https://sv.wikipedia.org/wiki/ROT13
Uppgiften skiljer sig dock lite från "vanlig ROT13", då den använder det svenska alfabetet med 29 bokstäver istället för det ordinarie med 26.

### Dubbelt publikt
Se https://sv.wikipedia.org/wiki/RSA
Om man återanvänder primtal för flera publika nycklar kan man faktorisera genom att hitta största gemensamma delare: https://sv.wikipedia.org/wiki/St%C3%B6rsta_gemensamma_delare

### Xor
Samma flagga som XOR-krypteras med olika slumpgenererade bitsekvenser varje gång man ansluter. Det står i ledtråden att "slumpbitsgeneratorn är skev", vilket syftar på att den oftast genererar nollor. Genom att ansluta många gånger kan man få statistik på vilka bitar som är vanligast på de olika platserna i meddelandet, vilket bygger upp flaggan.

### Ett hemligt, köttigt, gömt meddelande
På sidan om cookies finns det lite tecken som är i fetstil. Man kan tolka fet/icke-fet som ettor/nollor i ett Bacon's cipher: https://en.wikipedia.org/wiki/Bacon%27s_cipher


# Reversering

### Flaggkontrollerare
Programmet tar en sträng och kollar om det är flaggan. Men flaggan som kontrolleras ligger inbyggd i programmet, om man skriver ut innehållet med `strings chall` så kan man se flaggan.

### Uppgiften utan titel
Det finns en funktion som skriver ut flaggan men som aldrig anropas. Man kan modifiera programmet så att funktionen anropas.

### Slö
Uppgiften räknar (långtsamt) ut primtal nummer 160000005 och skriver ut 2020ctf{} runt det. Går snabbt att slå upp: https://www.wolframalpha.com/input/?i=160000005th+prime

### AndroidRev
Om man får strax över 31337 ("elit-klassen") poäng så skrivs flaggan ut. Patcha om programmet så att du får rätt antal poäng eller räkna ut logiken för hur flaggan skrivs ut. Flaggan är blowfish-krypterad med nyckel "00031340".


# Exploatering

### Miniräknare
Man kan identifiera att det är ett python-program som kör eval() runt datan man skickar in. Ge den exempelvis __import__('os').system('cat flag.txt') för att få det att skriva ut flaggan.

### Hoppsan
Programmet har en sårbarhet i form av en bufferöverskridning. Man kan med den peka om programmet att köra en funktion som skriver ut flaggan.

### EaaS
Uppgiften säger att flaggan finns på stacken. Programmet har en format string vulnerability, vilket gör att man kan läcka data från stacken. Om man ger exempelvis %5$lx som indata kommer man att få några bytes på stack från position 5 i hexadecimalt-format. Sök runt lite så hittar du flaggan.

### Pwned Editor
Räkna ut var returaddressen finns (relativt index 0 i texten man kan redigera) och skriv över den med addressen du vill hoppa till. När programmet startas så skrivs en ungefärlig address ut till var den redigeringsbara texten finns, så lägg in en NOP-släde och programdata där och hoppa dit.


# Övriga

### IRC -förnuftskontroll
Gå in i IRC-kanalen och se uppgiften i topic.

### Lager av zippar
Uppgiften är ganska välbeskriven, så skriv ett script som packar upp zipparna.

### Problemlösare 2000
Uppgiften är ganska välbeskriven, så skriv ett script som gör beräkningarna.

### Frågeformulär
Svara på frågorna.

### Dataläcka
"Ondingarna" har skickat ut data som ON/OFF-bitar i 104-protokollet (se https://en.wikipedia.org/wiki/IEC_60870-5). Filtrera ut rätt data i WireShark och översätt ON/OFF-bitarna till bitar i en sekvens av ascii-tecken.
