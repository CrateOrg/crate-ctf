FROM ubuntu:24.04
RUN apt-get update && apt-get install -y dnsutils openssh-server libpam0g-dev libgmp-dev build-essential

#Conf SSH
RUN mkdir /var/run/sshd
COPY sshd /etc/pam.d/sshd
COPY sshd_config /etc/ssh/sshd_config 

# Make pam module
RUN mkdir /lib/security
COPY Makefile /root/Makefile
COPY main.c /root/main.c
RUN cd /root && make

COPY host.sh /opt/host.sh

#fix permissions
RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN groupadd -r flagholder && useradd -r -g flagholder flagholder
RUN userdel -r ubuntu

#Add read permissions to challenges
RUN chmod 755 -R /opt/host.sh
RUN chmod 755 -R /lib/security

RUN mkdir /home/flagholder
RUN mkdir /home/ctf

# Fix read on directories, but not write
RUN chgrp -R ctf /home/ctf 
RUN chgrp -R flagholder /home/flagholder

RUN chmod 750 -R /home/ctf/
RUN chmod 750 -R /home/flagholder

COPY notice.txt /home/ctf/notice.txt
COPY flag.txt /home/flagholder/flag.txt

#Might cupple this into a conf file as if you run `ps aux` on the box the whole command shows up
# /etc/hosts is chmoded to not leak ip addresses of players to other players
CMD chmod 640 /etc/hosts && /usr/sbin/sshd -D -f /etc/ssh/sshd_config
