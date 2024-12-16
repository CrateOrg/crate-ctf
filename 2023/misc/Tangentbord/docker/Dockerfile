FROM debian:bookworm

ENV DEBIAN_FRONTEND noninteractive

# Dependencies
RUN apt-get update && apt-get install -y openssh-server locales && rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/sv_SE.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG sv_SE.UTF-8
ENV LANGUAGE sv_SE:sv
ENV LC_ALL sv_SE.UTF-8

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN echo "ctf:Vhbmhkbk91o6wams" | chpasswd
ADD sshd_config /etc/ssh/sshd_config

# Add Resources
ADD flag.txt /home/ctf/flag.txt
ADD inputrc /home/ctf/.inputrc
RUN echo "bind 'set enable-bracketed-paste off'" >> /home/ctf/.bashrc

ADD step1.txt /home/ctf/flag.txt
ADD step2.txt /etc/.flag.txt
ADD step3.txt /var/mail/flag.txt
ADD flag.txt /etc/X11/.Xauthority

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/.inputrc

RUN mkdir /run/sshd
CMD ["/usr/sbin/sshd", "-D"]
