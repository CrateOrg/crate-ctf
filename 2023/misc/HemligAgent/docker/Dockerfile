FROM debian:12

ENV DEBIAN_FRONTEND noninteractive
ENV TZ "Europe/Stockholm"

RUN apt-get update && apt-get install -y --no-install-recommends locales sudo openssh-server sshpass vim && rm -rf /var/lib/apt/lists/*

RUN mkdir /chall
RUN chmod -R 770 /chall
RUN chmod 775 /chall
RUN adduser chall --disabled-password --gecos ""

ENV CHALLUSER=chall
ENV CHALLUSERHOME=/home/chall

COPY run.sh /chall/
RUN chmod +x /chall/run.sh

RUN sed -i '/ForwardAgent/s/.*/ForwardAgent yes/g' /etc/ssh/ssh_config
RUN sed -i '/AllowAgentForwarding/s/.*/AllowAgentForwarding yes/g' /etc/ssh/sshd_config

RUN adduser flagholder --disabled-password --gecos ""
COPY --chown=flagholder:flagholder flag.txt /home/flagholder/
RUN chmod 600 /home/flagholder/flag.txt

COPY --chown=chall:chall tip.txt /home/chall/valkommen.txt

USER flagholder
RUN ssh-keygen -t ed25519 -q -f /home/flagholder/.ssh/id_ed25519 -N ""

USER root

RUN mkdir /home/chall/.ssh
RUN cp /home/flagholder/.ssh/id_ed25519.pub /home/chall/.ssh/authorized_keys
RUN cp /home/flagholder/.ssh/id_ed25519.pub /home/flagholder/.ssh/authorized_keys
RUN chown -R chall:chall /home/chall/.ssh
COPY prepare.sh /home/chall/prepare.sh

CMD cd /home/chall/; /home/chall/prepare.sh > /dev/null 2>&1; rm /home/chall/prepare.sh; sudo --preserve-env=HOST,CONTAINER_ID,CHALLUSER,CHALLUSERHOME -u chall TERM=xterm-color /chall/run.sh
