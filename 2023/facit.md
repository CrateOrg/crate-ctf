## Pin 3
PIN-koden består av 5 siffror. Skriv ett script som testar kombinationerna och hittar rätt kod.

## Pin 4
PIN-koden består av 22 siffror, så det är inte bruteforce. Back-end kontrollerar PIN via ett otvättat system()-anrop så injicera kommandon för kunna ta reda på flaggan.

## Source Control
Använd t.ex. `netcat` för att sätta source port, och undvik sitta bakom elak NAT som skyfflar runt portar.

## Lagom är bäst
Servern ger olika svar beroende på om filen är för stor eller för liten. Med t.ex. binärsökning går det att komma fram till den lagom stora storleken för att få servern att ge ut flaggan.

## Generisk buffertöverskridning #125772 v1.0
Via en blandning av C++ och C går det att skriva oändligt med data i en 256-byte buffert. Binären har kompilerats utan ASLR, NX, RELRO och stack canaries så det går att injicera shellcode och en returadress som pekar på bufferten (adressen ges i en utskrift).

## Generisk buffertöverskridning #125772 v1.1
Jämfört med v1.0 så skrivs inte längre adressen till bufferten ut, men det finns en funktion som innehåller en "jmp rax"-instruktion. Eftersom strcpy returnerar buffertens adress kommer denna finnas i RAX när `get_input()` returnerar. Att skriva över returadressen med adressen för "jmp rax" kommer omdirigera exekveringen till bufferten med shellcode.

## Unicorn Shredder
Den första tuggade bilden (längst ner på bucket-sidan) innehåller flaggan. Tugga lika stora bilder med identifierbara fyrkanter och inse att algoritmen bara tuggar på ett tiotal olika vis. Skriv ett script som pusslar ihop flaggbilden givet platserna på dina fyrkanter och se vilken bild som visar flaggan.

## Hemlig agent
Kontot "flagholder" har en SSH-session som "chall"-kontot. SSH-sessionen har agent forwarding aktiverat vilket gör det möjligt att återanvända sina SSH-nycklar för att ansluta till en annan maskin. För att det ska fungera skapas en SSH-agent-socket i `/tmp` som ägs av "flagholder". Det kontot (eller root) kan använda socketen för att skapa nya sessioner med SSH-nycklarna som agenten har inladdade, se "Security Issues With Key Agents" på http://unixwiz.net/techtips/ssh-agent-forwarding.html.

## Mikrokontrollerad
En AVR-binär som XOR-avkodar flaggan med fel nyckel och skriver ut den via USART. Med `file`, `objdump` och `strings` syns det att det är en ELF-binär för "Atmel AVR 8-bit", specifikt en ATmega328P. Att köra programmet med t.ex. simavr leder till att en sträng med skräptecken skrivs ut via serieporten (USART).

Att reversera programmet med t.ex. Ghidra bör leda till att man upptäcker att en sekvens med data XOR:as med 0x42 innan den skrivs till UDR0-registret för att skickas ut på serieporten. Att använda 0x42 som XOR-nyckel för att avkoda sekvensen ger samma utdata som skrivs ut om man kör programmet. Ledtråden i beskrivningen tyder på att den här nyckeln kan vara fel. Med t.ex. CyberChefs "XOR brute force"-modul kan rätt nyckel hittas som ger en sträng som börjar med "cratectf{".

## Moment 22
Kontrollen av den inmatade datan mot flaggan kan göras via strcmp som tar olika tid på sig att jämföra två strängar beroende på hur många tecken från början av strängarna som är lika. Genom att avaktivera "optimizations" och aktivera "debug mode" i inställningsmenyn tar strcmp längre tid på sig för varje korrekt tecken i flaggan.

Om flaggan består av 36 tecken med ett alfabet på 65 tecken tar det då max 65\*36=2340 gissningar att hitta flaggan istället för 65^36 gissningar som med vanlig brute force.

## Oraklet
En dekrypteringstjänst som använder AES-CBC för att avkoda några meddelanden som ges i uppgiften. Tjänster låter en inte läsa meddelandet som innehåller flaggan, men berättar ifall meddelandet dekrypterades korrekt (den PKCS #7 padding som mottogs var korrekt) eller inte. En [padding oracle attack](https://en.wikipedia.org/wiki/Padding_oracle_attack) kan användas för att dekryptera meddelandet och få ut flaggan.

## Tangentbord
En SSH-session där alla inmatade tecken översätts som om de hade skrivits på ett DVORAK-tangentbord. Med en bild på ett DVORAK-tangentbord som referens går det att skriva in Bash-kommandon för att läsa `~/flag.txt` och följa ledtrådarna till filen som innehåller flaggan.

## Kokbok
Reversera binären för att hitta credentials till en MongoDB. I binären finns även ett krypterat meddelande, och fungerande nyckel går att hitta i databasen.

## Terminator
Hitta kompilator för arnoldc, finns på github. Kompilera koden till något som är lättare att reversera, och gör det.

## Färgteori
Ta hexkoden för bakgrundsfärgerna på sidorna i presentationen och gör om till ascii.

## WhoShotTheSheriff
Inse att det handlar om SHA1, hasha sektorerna (512 bytes) och hitta den som matchar den givna hashen. Flaggan är det matchande filnamnet inom cratectf{}.

## (G)örfil
Bokstäverna i flaggan görs om till tal i form av olika antal a:n. Med kombinationer av dessa utförs lite matematiska operationer och svaren av dessa står i filen. Reversera operationerna för att få flaggan.

## Testbild 
De minst signifikanta bitarna i någon av färgkanalerna resulterar i en QR-kod som innehåller flaggan.

## Discode 
Hex-värdena för respektive R, G, B i varje bild ger flaggan i ascii.

## Poletten
One-time-pad som använts flera gånger. Använd detta faktum för att få ut nyckeln.

## Signalanalys
DTMF-toner avkodas till siffror. Tre siffror tillsammans tolkas som ascii (base 10). Base64-avkoda strängen för att få flaggan.

## Knäckebröd
Hitta diverse läcka lösenordslistor och knäck hasharna (SHA1) mot dessa.

## Diktafon
Local file inclusion ger tillgång till loggarna i `../log.json`, som innehåller lösenordet till admin. Loggar man in som admin får man flaggan.

## Intern
Flaggan finns i beskrivningen av Ossians spotifylista som heter flaggor. En websökning leder till LinkedIn, men man får fortsätta leta på andra tjänster för att hitta länken till spotify.

## Frågeformulär
Svara på frågorna och få en flagga.
