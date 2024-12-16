## Frågeformulär
Svara på frågorna och bli belönad med en flagga.

## Rörigt
Webbservern som URL:en pekar till använder sig av en sorts timing-attack för att avgöra om curl pipe:as till bash eller inte. När bash används så skickas en felaktig flagga - den rätta flaggan dyker bara upp om man försöker se källkoden via en webbläsare eller genom att låta curl skicka skriptet till en fil eller till terminalen.

## Min 90
Modbus över TCP. Dotmatrix-displayer med displaydata (1 bit = 1 pixel) på input register 240 och framåt. Register 0 och 1 är höjd respektive bredd på pixeldatan. Flaggdisplayen har id 0x1f. "Injektorbryggan" med  id 0x33 har maxspeed i holding register 0xb. Sätt registret till t.ex. 100 och läs ut datat från flaggdisplayen inom 10 sekunder och visualisera pixeldatat på lämpligt vis.

## Kaffepaket
Serialiseringsbugg i en java-applikation som använder biblioteket apache commons-collections 3.1, vilket kan användas för kodexekvering vid deserialiering. Använd t.ex. ysoserial för att hitta en lämplig payload. Programmet har ett debuggkommando som skriver ut en loggfil till /tmp, så lämpliga kommandon att lägga i sin payload är att skriva över loggfilen med flaggfilen, och sedan dumpa loggen i programmet.

## Fetch
Inse att det är javascript som blockar vissa mönster i hämtningar, och gå runt det.

## GammalDiskett
Det finns en raderad GIF-bild i diskavbildningen som innehåller flaggan. Den kan återskapas med t.ex. verktyget testdisk.

## Sudda, sudda, sudda
Bilden visar ett bankkort där kortnumret har blurrats. Genom att modifiera det givna skriptet (som genererar en suddig bild) går det att gissa ett kortnummer och jämföra resultatet pixel för pixel mot den givna bilden. Utsuddningen sker med en relativt liten radie, så det går att lista ut varje tecken rätt så oberoende av dess grannar då den gissning som ger minst skillnad mot originalet borde vara korrekt.

## Antimodänerna
En webserver som har många vhosts, hitta misstänkt myndighet eller loopa igenom alla med anpassad Host-header satt i requesten.

## Odefinierat beteende
Uppgiften demonstrerar en form av odefinierat beteende i C/C++ där kompilatorn kan ta bort delar av koden som inte följer C/C++-standarderna. Målet är att få programmet att krascha, vilket leder till att flaggan skrivs ut. I uppgiften tar kompilatorn bort en oändlig loop som är tänkt att skydda mot för stora tal, så genom att skicka in maxvärdet för en 32-bitars unsigned int (4294967295) sker division med 0 när programmet lägger till en etta till det inmatade talet.

## Så går vi ner i vår anropsstack
Binärfilen implementerar en enkel recursive descent-parser som kontrollerar att en inmatad flagga följer rätt format. Det görs ett funktionsanrop per tecken i flaggan, så med den givna coredump-filens stacktrace går det att gå igenom anropsstacken och plocka ut ett tecken ur flaggan (vid $rbp-4) för varje anrop.

## Gekåds
Inse att protokollet används för bland annat 3D skrivare, visualisera filen i en lämpligt verktyg och hitta flaggan inuti kuben.

## AdGuard 2000
Password-fältet på loginsidan är sårbart för SQL-injections. Bli admin (user id 9, eller username `admin`), ännu en sql-injection i manageusers.php. Luska ut att det är sqlite som används, och dumpa vilka tabeller som finns. Se att det finns en tabell som heter `secrets`, dumpa den och leta efter något som inehåller cratectf.

## Pressrelease
Scan codes, svensk tangentbordsuppsättning. Vissa är press, vissa är release. Tolka och följ med manuellt, eller automatisera med t.ex. Virtualbox `vboxmanage controlvm keyboardputscancode` mot en VM och luta dig tillbaka.

## Nystart
De givna filerna är delar av en JPEG-bild som innehåller JPEG restart markers. Genom att sätta ihop filerna så att markörerna hamnar i stigande ordning efter deras ID:n så bör hela bilden bli läsbar.

## PassarBast
Filen innehåller ett antal fragment där ett tecken upprepas många gånger i rad. Tecknena har skrivits till filen med best fit-allokering (vilket "passar bäst" ifrån titeln och beskrivningen antyder till) så att det största tillgängliga fragmentet fylls först, sen det näst största, och så vidare. Genom att sortera fragmenten efter fallande storleksordning så fås flaggan.

## Encro4
Uppgiften krypterar indatan med RC4, men använder samma nyckel/nonce varje gång. Att XOR:a valfritt krypterat meddelande med dess klartext ger nyckelströmmen, som sedan kan användas för att avkoda det givna meddelandet som innehåller flaggan. 

## RetroReversering
Den givna filen är ett GameBoy-ROM där det går att använda knapparna A och B för att mata in en 1:a respektive en 0:a som sedan används för att avkoda flaggan. Genom reversering går det att hitta dekrypteringsfunktionen och bruteforce:a sig till rätt "lösenord", eller så kan dekrypteringsalgoritmen reverseras.

## Bôs-arp
Homage till Franz! Titeln hintar om ARP-protokollet. En ARP-broadcast får svar från 7 olika adresser som tillsammans formar flaggan.

## Corduroy
Flaggan i ASCII-format är Manchesterkodad (manchestertyg heter couduroy på engelska). Med ett skript (eller manuellt med tålamod) går det att leta efter varje stigande och fallande flank i signalen och få ut flaggan.

## Det var inte alltid bättre förr
`message.bin` innehåller flaggan krypterad med den publika RSA-nyckeln i `rsa.pub`. Nyckeln kommer från ett gammalt Debiansystem som är sårbart mot CVE-2008-0166 och genererar nycklar med dålig slump. Det finns kompletta förteckningar på internet över alla nycklar och med en sådan kan man söka efter den publika nyckeln och få ut den privata.

## Dåliga odds
Slumptalsgeneratorn använder "Mersenne Twister"-algoritmen, specifikt MT19937 som uppgiften tipsar om. Det går att avgöra generatorns interna tillstånd genom att observera 624 genererade slumptal, därefter kan man förutsäga alla kommande tal.

## Flaggförvaring
Programmet kräver en giltig licensnyckel för att det ska gå att hämta flaggan. Genom reversering går det att se alla krav som nyckeln måste uppfylla för att accepteras, t.ex. "nyckelns 9:e tecken är detsamma som det 11:e och 13:e". Verktyg som t.ex. Z3 kan användas för att hitta en licensnyckel som uppfyller alla krav.

## SnurrigaSiffror
Varje byte i flaggan har gjorts om till tresiffriga decimaltal som slås på en nummerskiva. Högre siffror tar längre tid att slå, så längden på varje ljudsekvens i filen kan användas för att få fram siffrorna.

