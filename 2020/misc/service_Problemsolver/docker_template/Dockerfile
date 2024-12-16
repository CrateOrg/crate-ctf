FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive

# Update
RUN apt-get update --fix-missing && apt-get -y upgrade

# Dependencies
RUN apt-get install -y python3 xinetd

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf

# Add Resources
ADD ctf.xinetd /etc/xinetd.d/ctf
ADD chall_init.sh /etc/chall_init.sh
ADD chall /home/ctf/chall
ADD problemsolver.py /home/ctf/problemsolver.py
ADD redir.sh /home/ctf/redir.sh

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/chall
RUN chmod 750 /home/ctf/problemsolver.py
RUN chmod 750 /home/ctf/redir.sh
RUN chmod 700 /etc/chall_init.sh
