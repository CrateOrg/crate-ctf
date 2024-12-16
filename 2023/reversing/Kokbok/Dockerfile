FROM ubuntu:22.04

# Ha filen `recept` och denna fil i samma mapp. Bygg sedan med `docker build . -t cratectf/kokbok`
# och kör med `docker run --init --rm -it cratectf/kokbok`

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y libmongoc-1.0-0 && rm -rf /var/lib/apt/lists/*

COPY recept /recept

RUN chmod +x /recept

CMD ["/recept"]
