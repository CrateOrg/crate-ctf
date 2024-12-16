FROM alpine:3.20

RUN apk --no-cache add openssh-server

RUN : \
    && adduser -D ossian \
    && echo "ossian:$(head -c21 | base64)" | chpasswd \
    && echo -e "PasswordAuthentication no\nPermitRootLogin no" >> /etc/ssh/sshd_config \
    && rm /etc/motd \
    && echo "cratectf{den_där_guiden_funkade_ju_inte_alls}" > /home/ossian/flag.txt \
    && :

COPY ssh_host_ed25519_key ssh_host_ed25519_key.pub /etc/ssh/
RUN chmod 600 /etc/ssh/ssh_host_ed25519_key
RUN chmod 644 /etc/ssh/ssh_host_ed25519_key.pub
COPY ossian_ed25519.pub /home/ossian/.ssh/authorized_keys
COPY fake-docker.sh /bin/docker

CMD ["/usr/sbin/sshd", "-De"]
