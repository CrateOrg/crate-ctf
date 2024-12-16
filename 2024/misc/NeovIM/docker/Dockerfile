FROM gcc:bookworm

ENV DEBIAN_FRONTEND noninteractive

# Dependencies
RUN apt-get update --fix-missing && apt-get -y upgrade && rm -rf /var/lib/apt/lists/*

# Dependencies
RUN apt-get update && apt-get install -y python3 xinetd locales && rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf
# Add Resources
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./main.py /home/ctf/main.py
COPY run.sh /home/ctf/run.sh


# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/main.py
RUN chmod 755 /home/ctf/run.sh

RUN service xinetd restart
CMD ["/usr/sbin/xinetd", "-dontfork"]
