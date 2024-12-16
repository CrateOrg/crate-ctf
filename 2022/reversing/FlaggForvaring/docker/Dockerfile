FROM gcc:12-bullseye as build-image

ADD challenge.c ./
RUN gcc -O0 -o chall challenge.c

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

# Update and install dependencies
RUN apt-get update --fix-missing && apt-get -y upgrade && apt-get install -y xinetd locales && rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf
# Add Resources
ADD ctf.xinetd /etc/xinetd.d/ctf
COPY --from=build-image chall /home/ctf/chall
ADD chall.sh /home/ctf/chall.sh
ADD flag.txt /home/ctf/flag.txt

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/chall.sh
RUN chmod 750 /home/ctf/chall

RUN service xinetd restart
CMD ["/usr/sbin/xinetd", "-dontfork"]
