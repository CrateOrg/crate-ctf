# Webb

## Pin1
Korrekt pinkod går att hitta i källkoden.

## Pin2
Loopa igenom alla pinkodskandidater och testa dem mot verifyPin-funktionen.

## Switched
XSS i ett meddelande till Admin. Skriv javascript som skickar document.cookie till en extern tjänst, och använd sedan den stulna kakan för att logga in som admin.

## Tokfrans
Använd rockyou-ordlistan för att forcera fram rätt lösenord till JWT-token. Skapa sedan en ny JWT-token med admin-rättigheter.


# Exploatering

## En liten gurkburk
Pickle-serialiseringsbugg. Skicka in ett pickle-objekt som evaluerar flag-variabeln eller som ger ett skal.

## Högst Oklart Program
Use-after-free-bugg. Om man kör först `befria` och sedan `allokera` så kan man skriva över funktionspekaren som finns i objekten. Räkna ut addressen till `system` med hjälp av information i den givna `libc`-filen + addressen till `malloc` som skrivs ut i början. Kör sedan `anrop` med `/bin/bash` i strängvariablen (genom fixahemlis) för att få ett skal.

## Man kan väl ändra sig?
En bufferöverskridning som gör att man kan modifiera changeme-variabeln om man ger mer än 44 tecken som indata.

## Staketstolpe
Format string-bugg. Som beställningstext kan man exempelvis ange "%n" för att skriva data och "%x" för att läsa data, om man har ett namn som fyller ut hela name-buffern.


# Kryptografi

## Tomtekrypto
Substitutionskrypto, där varje bokstav har bytits ut mot en annan. Gör en frekvensanalys eller använd något onlineverktyg för att lösa. Var noggran med versaler och gemener i flaggan!

## Xtnls Kryptografiska Tjänst
Skriver man in lite data så inser man att tjänsten endast kastar om bokstäverna (och lägger in lite padding vid behov). Skicka unika bokstäver i en sträng med lika lång längd som den krypterade flaggan för att enkelt avgöra vart en bokstav hamnar vid krypteringen.

## Alldeles lagom stor
Loopen i `generate_cipher.py` gör att datan som krypteras blir precis större än `n`, vilket gör att en del blir "bortkapad" av modulo-operationen. Detta innebär det går att lägga på `n` multiplicerat med någon heltalskonstant för att återfå datan innan modulo-operationen kapar bort delen. Testa med ett par stycken (och ta tredjeroten) för att hitta flaggan.

## 🎃🎃🎃
Se https://en.wikipedia.org/wiki/Length_extension_attack


# Forensik

## Åttahundratvå punkt elva
chall.pcapng innehåller en paketdump av trafiken från ett WPA2-krypterat trådlöst nätverk med lösenordet "password123". Genom att använda t.ex. aircrack-ng borde lösenordet gå att hitta inom några sekunder även med en liten ordlista. Wireshark kan sedan användas för att dekryptera trafiken med hjälp av lösenordet. Ett ICMP-paket har skickats från 192.168.1.3 till 192.168.1.2, detta innehåller flaggan.

## Sofia
En minnesdump från en körande Windows XP. I minnet för notepadprocessen återfinns en flagga i form av ASCII-art, vilket kan hittas med exempelvis volatility eller strings och en del scrollande.

## Metaception
Wave-fil innehållande en PNG som metadata. PNG-filen har den base64-kodadade flaggan som metadata.

## IAX
Nätverksdump. Filtrera bort SSH och TLS, kvar finns ospecad UDP och RTCP vilket hintar om att UDP-paketen antagligen är RTP. Tagga i wireshark och analysera RTP-strömmar. Lyssna på samtalet till helpdesk och snappa upp flaggan.

## Konstigt ljud
Utmaningen består av en bild som har kodats i [APT-format](https://en.wikipedia.org/wiki/Automatic_picture_transmission), vilket sedan 1964 har använts för att skicka bilder från vädersatelliter. Idag används nyare metoder, men det finns fortfarande satelliter som sänder i detta format och mjukvara för avkodning finns fritt tillgänglig.


# Reversering

## FutureFlag
Modifiera (via LD_PRELOAD eller annan mekanism) att tiden blir rätt när du kör programmet.

## Ett väldigt jamande
Identifiera att det är ett Scratch-program (https://scratch.mit.edu/projects/editor/) och öppna filen i Scratch. Läs sedan igenom koden och försök komma på hur den verifierar indata och skriv ett program som genererar indata som accepteras.

## COSMAC-spel?
Identifiera att det är ett CHIP8-program (https://en.wikipedia.org/wiki/CHIP-8).

## Kling och Clang++
Det är IR för LLVM det rör sig om. Kompilera färdigt med `clang++ main.ll` och kör. Då kommer den att skriva ut "Almost there...". Genom att öppna med något lämpligt verktyg (gdb eller radare2, exempelvis) kan man identifiera vart programmet måste hoppa för att 


# Övriga

## Bösarp
GPS-track i XML-format. Identifiera att punkterna är i form av en cirkel runt kyrkan i Bösarp. Punkterna är antingen lite längre (etta) eller lite kortare (nolla) från centrumpunkten. Tolka bitarna som ASCII och få fram flaggan.

## Flagghämtartjänst
"Någon Apache-grej" hintar om att det rör sig något som Apache utvecklar. Om man kollar på listan på https://en.wikipedia.org/wiki/List_of_Apache_Software_Foundation_projects så kan man se att Thrift är ett ett verktyg för att skapa tjänsteservrar utifrån en definitionsfil. Kompilera description-filen med thrift och gör anrop till servern.

## Max 30
Servern kör modbus, och har tio anslutna dotmatrix-displayer som slavar. Varje slav lagrar följande information i sina input register (IR): Pixelhöjd på position 0, pixellängd på position 1 och pixeldata på position 240 och framåt. Hämta datat från respektive slav och plotta upp pixlarna rad för rad enligt dimensionerna. Flaggan återfinns på displayen med id 0x19.

