# Diktafon
(bättre namn efterlyses)

En webbtjänst där man kan skapa konton, logga in och läsa dikter.

Luckan är aningen tidskänslig och borde nog rensas och startas om någon/några
timmar innan tävlingen startar.

## Lösning

`/poem` tillåter att man läser dikter som har `../` i namnet och validerar inte
att filsökvägen är i diktmappen `data/poems`, endast att den är i datamappen.
(Det är alltså en local file inclusion). I datamappen finns även filen där alla
loggar hamnar, alltså kan man se serverns loggar på `/poem?name=../log.json`.
När någon försöker logga in loggas användarnamnet.

I bakgrunden simuleras lite trafik, bland annat att någon försöker logga in som
`admin`, men först råkar byta plats på användarnamnet och lösenordet (som är
lite knasigt placerade på inloggningssidan), innan den sedan byter plats på dem
och lyckas logga in.

Alltså går det att hitta lösenordet till kontot `admin` i loggarna. Loggar man
in som admin så syns flaggan på sidan.
