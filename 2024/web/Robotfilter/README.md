# Robotfilter

## Lösning

Robotfiltret är antagligen inte möjligt att lösa, men alla nivåer är på olika
subdomäner och alla möjliga subdomäner syns i certifikatet som webbsidan
använder. Det går att hoppa direkt till den subdomänen som börjar på `flag`.

## ~~Att göra~~ Gjort:

Certifikatet i `docker/.lego` gäller bara till den 29 oktober, så det måste förnyas eller bytas ut.

För att skapa ett nytt certifikat kör t.ex.:
```sh
lego $(BASE_DOMAIN=robotfilter.challs.crate.nu go run . domains | sed 's/^/-d=/g') --accept-tos -m some@email.com --http run
```
på den server dit robotfilter.challs.crate.nu (port 80) pekar.

Uppdatera sedan `connection_info` i `challenge.yml` samt `BASE_DOMAIN`, `CERT_FILE` och `KEY_FILE` i `docker/docker-compose.yaml`.

## Att Göra

Certifikatet är uppdaterat, väl innan utmaningen börjar kan man skapa en droplet i digital ocean. Installera docker, samt docker-compose och köra.

```bash
docker compose up --build -d
```

DNS-uppslaget för robotfilter.challs.crate.nu måste då också pekas om till droppletten. 
