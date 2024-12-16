# Autentiseringsknas
Containern har en PAM-fil som körs vid SSH-inloggningar. I början får man göra lite detektivarbete och gräva fram den, man vet redan att CTF-användaren inte har någon hash, så man kan läsa i /etc/pam.d/sshd och hitta filen i pam filen i /lib/security.
Det finns tre användare:
| Användare  | Beskrivning |
|------------|-------------|
| ctf        | Logga in med Matrixgreen |
| games      | Genom att reversera koden kan man se att den kör /opt/host.sh med parametrar. Den gör en reverse lookup på specifierad ip address och lägger in den i /etc/hosts. |
| flagholder | SSH kommer att passa PAM_RHOST till scriptet, som resolvas till ditt hostnamn. Efter det kontrollerar den chiffertext.end.flag.crate, där chiffertext är krypterade versionen av lösenordet man stoppar in. |

Ett sätt att lösa den på är att sätta upp en bind-server, serva den med ngrok och sätta upp ett uppslag: 
```
$TTL 86400
@   IN  SOA flag.crate. root (
            2024073001 ; Serial
            3600       ; Refresh
            1800       ; Retry
            1209600    ; Expire
            86400      ; Minimum TTL
        )

    IN  NS  192.36.220.1.

1 IN PTR 35828307353437292958606111775.08669273865736267133044981921162307357.9949940315847485879922810321696134827535375828485523447404414.8966047440172650938462759177979388832311989.377540883593614906429561642765064546321789290527295502447009.end.flag.crate.
```
och skriva in lösenordet "a" efter att man fått games att hämta uppslaget från den. 
