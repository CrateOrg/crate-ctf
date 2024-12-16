# Fallet om KÄRNkraftverket

## Installering på virtuell maskin
Kör ansible-boken deploy.yml mot dropplet, samt peka om DNS-uppslag.

## Beskrivning
Maskinen kör en xinetd som skickar data varje sekund (se talker.c).

Kärnmodulen upprätthåller en länkad lista av element, där varje element innehåller IP och den senaste porten som spelaren skickar data till. När man har skickat ett SYN-paket som innehåller rätt lösenord (data.bin), sparar den den porten.

För att vinna måste man slå de tre portarna definierade i koden i rad. Om man slår på fel port, eller börjar rätt och sen slår fel tas elementet i den länkade listan bort och man får börja om från början.

När man har gjort detta kommer kärnmodulen att ersätta tcp trafiken som kommer från xinetd med flaggan. 

## Lösning
I ett terminalfönster, kör
```
nc fok.challs.crate.nu 50014
```

```
sudo hping3 -S fok.challs.crate.nu -p 1288 -d 8 -E data.bin -c 1
sudo hping3 -S fok.challs.crate.nu -p 5134 -d 8 -E data.bin -c 1
sudo hping3 -S fok.challs.crate.nu -p 36112 -d 8 -E data.bin -c 1
```
Där data.bin är bytes från databinären. 
Flaggan kommer då att injiceras i trafiken i den ursprungliga netcat-sessionen. 
