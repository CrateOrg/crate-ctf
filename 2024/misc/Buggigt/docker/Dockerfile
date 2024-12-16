FROM debian:12 AS gdb-build

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /build

RUN apt-get update && apt-get install -y gcc g++ make wget libgmp-dev libmpfr-dev file patch && rm -rf /var/lib/apt/lists/*
RUN wget https://ftp.gnu.org/gnu/gdb/gdb-15.1.tar.gz && tar xvf gdb* && rm gdb-15.1.tar.gz && mv gdb* gdb
WORKDIR /build/gdb
# Build unmodified GDB for Docker cache, enables faster iterations when developing patch
RUN ./configure --with-python=no; make -j 8
# Add patch and rebuild necessary components
COPY remove-source-command.patch ./
RUN patch -p1 < remove-source-command.patch && make

FROM debian:12

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ="Europe/Stockholm"

RUN apt-get update && apt-get install -y locales gcc make libgmp-dev libmpfr-dev file gcc g++ && rm -rf /var/lib/apt/lists/*

COPY --from=gdb-build /build/gdb /gdb
RUN cd /gdb && make install

RUN adduser ctf --disabled-password --gecos ""

ENV CHALLUSER=ctf
ENV CHALLUSERHOME=/home/ctf

ADD main.c Makefile gdbinit /home/ctf/
RUN cd /home/ctf/ && chmod 644 * && make && rm main.c

COPY flag.txt /flag.txt
RUN chmod 644 /flag.txt

# Spawning a shell from GDB would be too easy
#RUN rm /bin/bash /bin/sh
# Remove all other programs except for GDB to prevent switching program to /bin/cat
RUN find /usr/bin/ -type f ! -name gdb | xargs rm

USER ctf
CMD [ "/usr/local/bin/gdb", "-x", "/home/ctf/gdbinit" ]
