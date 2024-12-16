# Web

## XML-kontroll

En webbsida som är sårbar för XML eXternal Entity (XXE)-injektion: https://en.wikipedia.org/wiki/XML_external_entity_attack. På Linux-system lagras användarkonton i `/etc/passwd`, så genom att läsa ut den filen hittar man flaggan.

## Robotfilter

En uppsättning CAPTCHA-aktiga sidor som till slut blir omöjliga att lösa. Varje nivå har en egen domän och alla möjliga subdomäner syns i certifikatet som webbsidan
använder. Det går att hoppa direkt till den subdomänen som börjar på `flag`.

## Fillagringstjänst

Från källkoden kan man se att filer läses ut via ``readFile(`./uploaded/${req.session}/${path}`)``. Detta är sårbart för path traversal för att läsa valfri fil på systemet, men sådana angrepp filtreras bort från `path`-variablen. Dock så går det att utnyttja `session`-kakan som saknar denna kontroll.

## Sök

En MongoDB-injection som låter en filtrera på användares lösenord (som sparas i
klartext). Det går dock inte att returnera lösenordet direkt, men med MongoDB-filter går det att gissa lösenordet tecken för tecken.

## KaKlickare

Variabeln som sparar hur många clicks som är genomförda styrs av klienten via en kaka samt via JavaScript.

# Exploatering

## Riscy Business 1

En buffer overflow på RISCV-arkitekturen, kan t.ex. köras via QEMU. En `win`-funktion skriver ut flaggan.

## Golf SM

Även fast programmet filtrerar bort negativa tal, så uppfattas tal större än `2**31` som negativa tal av resterande operationer i programmet, se [Two's compliment](https://en.wikipedia.org/wiki/Two%27s_complement). Sista hålet kan lösas med att göra:
`2**32-900 = 4294966396` armhävningar.

## Heapie

Ett Zig-program där är möjligt att få ett stycke och ett dokument som ligger på samma adress med sekvenser av allokeringar och deallokeringar. Det är sedan möjligt att skriva över metadata som pekar ut var dokumentet finns i minnet för att peka om det till flaggan och få utskrivningen av dokumentet att visa den.

## JSFS

Om man skriver ett kommando som inte finns så får man hela "minifierade" källkoden utskriven till sig som en del av felmeddelandet. Terminalen är implementerad som en state machine och om `"writeflag"` finns i state:t så sparas flaggan till `file` i state:t. Via JavaScript prototype pollution är det möjligt att få detta att hända utan att känna till lösenordet.

## Note

När JSON tolkas som en struct i Go så görs ingen skillnad på gemener/versaler, men om den tolkas som en `map[string]any` så blir det skillnad. Det går därför att sätta `"IS-ADMIN":true` (med versaler) för att kringgå kontrollen och samtidigt bli admin.

# Kryptografi

## Kassaskåpet 2 - "Bättre tur är skicklighet"

Eftersom random-funktionen i kontraktet nyttjar sig av blockhashen kan man beräkna i förhand vad den kommer att returnera. Kontrollen [tx.origin != msg.sender](https://ethereum.stackexchange.com/questions/1891/whats-the-difference-between-msg-sender-and-tx-origin) medger att man måste deploya ett proxykontrakt att agera genom.

## Zebran, Koordinatera och Piraterna
Se [Zero-Knowledge Proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof#Practical_examples). Programmet bestämmer vilket tal den frågar efter beroende på tiden, vilket gör det möjligt att förutsäga vilken fråga som kommer dyka upp och anpassa sina valda tal för att lösa uppgiften utan att känna till hemligheten.

## Skyltsmedjan 

Utmaningen bygger på https://en.wikipedia.org/wiki/Digital_signature_forgery.Kortfattat beskriver artikeln att om du kan signaturen till m1 och m2, kan du beräkna signaturen för m1*m2. Genom att faktorisera `Kund nr. {userid} får hämta flaggan` kan man få programmet att signera dessa m1 och m2, detta medger att man kan förfalska signaturen till det kompletta meddelandet.

## KrEncyclopedia
Genomför frekvensanalys på artiklarna, nyckeln som har använts för krypteringen kan då deriveras. 

# Forensik

## Protokollkoll

En server som implementerar ett litet TLV (type-length-value)-protokoll. Typ 5 ger flaggan som svar och övriga typer ger "Error". En PCAP-fil finns given där typ 0-3 skickas. Typ- och längdfälten kan då identifieras genom att kolla på konversationerna i PCAP:en. Genom att testa olika typer kan flaggan hittas.

## Stulen Konst

Datan är tagen från `/dev/input/mice`. När man har parsat [formatet av datan](https://stackoverflow.com/questions/11451618/how-do-you-read-the-mouse-button-state-from-dev-input-mice) kan det nyttjas ett visualiseringsbibliotek, t.ex. Pythons `turtle` för att rita en bild. Bilden innehåller flaggan.

## Red teaming?
Datan är infraröda signaler från en Samsung TV-fjärrkontroll. Modellen kan gissas utifrån från det repeterade mönstret som börjar med `0xe0e0`, vilket vid en sökning kan leda en till IR-protokoll. Med en [översättningstabell](https://github.com/lepiaf/IR-Remote-Code) kan man översätta datan till flaggan.

## Långtidsminne

Minnesdumpen kommer från en VM där programmet `C:\Users\Administrator\Downloads\metasploit_psexec_session_stager.exe` har körts vid 2024-08-23 14:12:29. Filen kan analyseras med t.ex. [Volatility](https://github.com/volatilityfoundation/volatility), och genom att testa processrelaterade kommandon från en [cheat sheet](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet#processes) går det att hitta programmet via modulen `windows.registry.userassist`.

# Reversering

## Autentiseringsknas
Autentisering sker via PAM med en modul som hittas i `/lib/security/pam_weird.so` (filen refereras till från `/etc/pam.d/sshd`). Genom att SSH:a in som games kan man få containern att hämta DNS-uppslag från spelaren ([ngrok](https://ngrok.com/) och [bind9](https://www.isc.org/bind/) kan vara till nytta). När man ssh:ar in som flagholder kommer PAM-modulen att få PAM_RHOST som ett argument. Den kontrollerar sedan lösenordet man stoppar in mot `chiffertext.end.flag.crate`. Där `chiffertet.end.flag.crate` är ditt DNS-uppslag. Om den dekrypterade chiffertexten (en privat och publik RSA-nyckel finns i binären) stämmer med lösenordet som stoppades in får man flaggan. 

## Extraterrestriell Kommunikation

Pythonprogrammet enkodar morse till en bild. Bilden ses som ett koordinatsystem, mängden `-` och `.` i en bokstav ses som en X- och Y-koordinat. Den blåa färgkanalen avgör vilken position i flaggan bokstaven har, den röda färgkanalen avgör vilken bokstav pixeln syftar på i händelse av kollision. Med kollision menas att bokstäverna `d,r och u` pekar på samma koordinat eftersom `['d', 'r', 'u']` i morse är `['-..', '.-.', '..-']`. 

## Fallet Om KÄRNkraftverket

Den öppna porten kör ett enkelt C-program som skickar data varje sekund. Kärnmodulen nyttjar två [netfilter](https://elixir.bootlin.com/linux/v6.11.6/source/include/linux/netfilter.h)-krokar. Den för inkommande trafik kontrollerar vilka portar som får SYN-paket. För att modulen ska parsa paketen du skickar måste du inkludera 8 bytes som återfinns i binären. För att skicka TCP-paket som har SYN-flaggan satt och samtidigt innehålla data kan programmet `hping3` nyttjas. Genom att slå på tre portar i rad: 1288, 5134 och 36112, så kommer den utåtgående kroken att ersätta trafik som kommer från port 50014 med flaggan.

## Uppvärmning

Den stora if-satsen kan lösas med en SMT-lösare, såsom `z3`. Även fast man vinner skrivs flaggan aldrig ut. Efter varje gång man har lyckats så sparas det en historik av vinsten du använde. I och med att buffern av historik växer, så allokeras mer och mer minne. Efter att man förlorar frias detta minne. Flaggan printas inte när man vinner men den laddas in i en buffer. Genom att vinna tillräckligt många gånger och sen förlora med mening, kan man se till att flaggbuffern och historik buffern är en del av samma chunck i heapens fast-bin. `flag` kommer då få historikens gamla pekare och det leder till en [use-after-free](https://heap-exploitation.dhavalkapil.com/attacks/first_fit) när spelaren ber programmet skriva ut historikbuffern.

## Packman

En tjänst där man laddar upp filer, och sedan packar dem. Formatet följer `byte`, `short`: Där det motsvarar offset (från ett fast värde), count. Offseten kan beräknas genom att ladda upp egna filer med känt innehåll och se hur de packas, vilket låter en reversera processen.

# Osint

## Intern 2 

Ossian har skaffat en webbsida på ossianwallengren.se. Dess källkod finns
[på GitHub](https://github.com/ossianwallengren/ossianwallengren.se). Dessutom
finns en GitHub action som automatiskt deployar sidan från repot. Detta görs via
SSH med en nyckel som sparas i en GitHub action secret. Tidigare var nyckeln sparad direkt i actionen, vilket fixades genom en rebase och en force push (enligt blogginlägget). Tyvärr för Ossian så sparar GitHub commits även om de har ersatts, så genom att plocka ut commithashen från bilden och gå till den på GitHub går det att hitta nyckeln och använda den för att logga in på servern.

## HittaHit 1
Leta med hjälp av karta, Google Streetview, eller något annat liknande verktyg.

## HittaHit 2
Via en sökning på adressen för huset i korsningen går det att hitta en nyhetsartikel om att huset har sålts med namn på nuvarande och föregående ägare. En sökning på "brastad bil" ger en bilfirma med samma namn som en av personerna i artikeln.

# Övriga

## Neovim

En simulering av spelet [Nim](https://en.wikipedia.org/wiki/Nim). Artikeln beskriver hur man spelar optimalt. Första spelet går att lösa för hand, men det andra är tillräckligt stort för att medföra att man behöver scripta det. 

## Hönan och Ägget

Genom att ladda upp filer som är konstiga kan man se i error-loggen att det är `make` som körs för att kompilera filerna. Genom att ladda upp en fil som heter `Makefile` som innehåller en regel för att göra `Makefile` kan man få tjänsten att köra kommandot `make Makefile`. I regeln för hur den ska göra `Makefile` kan man då exekvera kod. 

## Kassaskåpet 1 - "Den Berömda Bosse"

Python-biblioteket `web3` kan användas för att kommunicera med blockkedjan. Man skulle kunna tro att `string private password` inte går att komma åt, men detta kontrollerar endast att variabeln inte kan läsas genom kontraktets ABI. Funktionsanropet:
```python
web3.eth.get_storage_at(CONTRACT, 0)
```
läser minnet och lösenordet vid kontrakets address. 

## Buggigt

En GDB-session där ett program har fastnat i ett segmenteringsfel. Funktionen `print_flag()` ska skriva ut flaggan, men den kraschar på grund av att mode-argumentet till `fopen()` är "open" istället för "r" (för "read"). Genom att sätta en breakpoint på `print_flag()`, starta om programmet, stega fram till efter att argumenten skrivits men innan `fopen()` anropas och byta ut strängen går det att få programmet att skriva ut flaggan.

## Frågeformulär

Svara på frågorna och få en flagga.

