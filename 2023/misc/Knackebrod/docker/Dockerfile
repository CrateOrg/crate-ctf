FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# Update
RUN apt-get update --fix-missing && apt-get -y upgrade && rm -rf /var/lib/apt/lists/*

# Dependencies
RUN apt-get update && apt-get install -y python3 xinetd locales && rm -rf /var/lib/apt/lists/*

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf

# Add Resources
ADD ctf.xinetd /etc/xinetd.d/ctf
ADD chall.sh /home/ctf/chall.sh
ADD challenge.py /home/ctf/challenge.py
ADD hashes /home/ctf/hashes

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/chall.sh
RUN chmod 750 /home/ctf/challenge.py
RUN chmod 750 /home/ctf/hashes

RUN service xinetd restart
CMD ["/usr/sbin/xinetd", "-dontfork"]
