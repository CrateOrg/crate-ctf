# Intern 2

Ossian är tillbaks. Typ. Uppgiften från förra året:
<https://git.crate.foi.se/capturetheflag/crate-ctf-2023/-/blob/master/challenges/Intern/solution.txt?ref_type=heads>

Inloggningsuppgifter:
(redacted for public publishing)

## Uppgiftsförklaring

Ossian har skaffat en webbsida på ossianwallengren.se. Dess källkod finns
[på github](https://github.com/ossianwallengren/ossianwallengren.se). Dessutom
finns en github action som automatisk deployar sidan från repot. Detta görs via
ssh med en nyckel som sparas i en github action secret. Men så var det inte
alltid! Tidigare var nyckeln sparad direkt i actionen (smidigt va?). Detta
fixades sedan genom en rebase och en force push. Dessutom lade Ossian upp ett
blogginlägg på sin webbsida om hur man tar bort hemligheter man lagt upp med
lite bilder på hur det ser ut på vägen.

Tyvärr för Ossian så sparar GitHub commits som inte (längre) går att nå från
någon branch i typ all evighet (eller åtminstone 14 år, se
[denna fråga på stackoverflow](https://stackoverflow.com/questions/4367977/how-to-remove-a-dangling-commit-from-github))
och dessa går att komma åt om man har commit-hashen (eller åtminstone början av
den). Otroligt nog läckte Ossian hashen av hans commit med hans ssh-nyckel i
en av de illustrativa bilderna i hans blogginlägg.

Jag missade först att man även skulle kunna se alla gamla commits som det körts
en deploy från på action-tabben. Det gick dock att lösa genom att stänga av
actions på repot (nu när det inte är några fler som måste köras). Då kan man
fortfarande se runs på commits ett givet commit, men inte se listan av alla
runs av en action (åtminstone inte från webbgränssnittet men om någon hittar
det via API:t tycker jag man förtjänar flaggan).

Sedan är det bara att logga in med ssh-nyckeln och hämta flaggan.

## Hosting

För att köra deployment-actionen och få loggar som ser rimliga ut (fast de
försvinner ju efter 90 dagar så den gröna checkboxen är allt som kommer finnas
kvar, vilket är lite synd) körde jag en podman-kontejner som i sin tur körde en
ssh-server och en "nestlad" podman-instans. Det gick då att bygga och starta
kontejnern via docker compose mot docker-instansen (fast det var ju podman men
det är nära nog för att mestadels funka) via ssh. Däremot verkade den inre
kontejnern med webbsidan stängas av efter någon minut men det kvittar. För att
minska risken att bli fett ägd av Nordkoreanska hackers gjorde jag så att
endast IP-addresserna github action runners kan få fick ansluta med nyckeln.
Imagen med tillhörande compose-fil som kördes finns i `ci.tar.gz` (jag lyckades
endast köra den i rootful podman och docker-compose (ej podman-compose!, podman
compose-kommandot kan exekvera docker-compose), men antagligen bör det inte
behövas igen).

Det som behövs köras på ossianwallengren.se under tävlingen är
[webbsidan](https://github.com/ossianwallengren/ossianwallengren.se/) och en
ssh-server som accepterar publika nyckeln i `ci.tar.gz:./ossian_ed25519.pub`
där man kan få flaggan. Docker compose-fil med båda finns i mappen ./docker.
Har nu lagt in en traefik-kontejner som svarar med 404 om hostnamnet inte är
ossianwallengren.se, så det bör inte gå att hitta någon intressant genom att
testa porter även om den körs på samma server som alla andra uppgifter, men den
måste lyssna på port 22 för ssh (dåligt planerat?) så den måste väl köra på en
server vars ordinarie ssh-server inte använder port 22. I
`docker/traefik-{static,dynamic}.yaml` finns även konfiguration för https
utkommenterad. Om man avkommenterar dessa och `ossianwallengren.se` pekar till
servern som kör kontejnrarna kanske det bara funkar™.
