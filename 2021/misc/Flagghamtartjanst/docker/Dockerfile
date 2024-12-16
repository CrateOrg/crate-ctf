FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

# Update
RUN apt-get update --fix-missing && apt-get -y upgrade

# Dependencies
RUN apt-get install -y python3 python3-pip locales thrift-compiler
RUN pip3 install thrift

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf

# Add Resources
ADD chall.sh /home/ctf/chall.sh
ADD server.py /home/ctf/server.py
ADD flag.txt /home/ctf/flag.txt
ADD gen-py /home/ctf/gen-py

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/chall.sh
RUN chmod 750 /home/ctf/server.py
RUN chmod 750 /home/ctf/flag.txt
RUN chmod -R 750 /home/ctf/gen-py

CMD ["/home/ctf/chall.sh"]
