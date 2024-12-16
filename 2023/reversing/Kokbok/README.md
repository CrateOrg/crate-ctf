# Kokbok

SETUP
För att få fram recepten görs följande (finns i mappen script):
1. get_recept.sh	// Hämtar rcept från ICAs hemsida, kör dem genom cleanjson.py för att utvinna de relevanta fälten. Detta kommer köras 'while true' så programmet måste avslutas.
2. unique.py	// Filtrerar bort alla dubletter av recept och lägger in i unika_rena_recept.json

flag_doc.json är den json-filen som importeras till den andra kollektionen som innehåller flaggans parametrar i json-format.

I src finns det orginella C-programmet som kompileras innan det ges till användaren. Det kan kompileras med typ detta kommando.
```sh
gcc recept.c -o recept -I/usr/local/include/libmongoc-1.0 -I/usr/local/include/libbson-1.0 -L/usr/local/lib -lmongoc-1.0 -lbson-1.0
```

NOTE
Mappen Kokbok innehåller en kopia av databasen. Det borde gå att köra 'mongo restore' med filerna för att få upp databasen, men allt är automatiserat i docker samt tillhörande filer. Denna mappen används alltså inte!

Gamla grejer att installera från tidigare version av docker-filen
´´´
# RUN apt update &&\
#     apt install -y wget gcc make pkg-config libssl-dev libsasl2-dev &&\
#     wget https://github.com/mongodb/mongo-c-driver/releases/download/1.5.4/mongo-c-driver-1.5.4.tar.gz &&\
#     tar xzf mongo-c-driver-1.5.4.tar.gz &&\
#     cd mongo-c-driver-1.5.4 &&\
#     ./configure &&\
#     make install

# ENV LD_LIBRARY_PATH=/usr/local/lib
´´´
