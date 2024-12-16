FROM gcc:bookworm

ENV DEBIAN_FRONTEND noninteractive

# Dependencies
RUN apt-get update --fix-missing && apt-get -y upgrade && rm -rf /var/lib/apt/lists/*

# Dependencies
RUN apt-get update && apt-get install -y python3 python3-pip make locales && rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf
# Add Resources
COPY src /home/ctf/src
COPY flag.txt /flag.txt

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod -R 555 /home/ctf/src

RUN mkdir -p /home/ctf/src/app/compiled/
RUN chown -R ctf:ctf /home/ctf/src/app/compiled/
RUN chmod -R 766 /home/ctf/src/app/compiled/

RUN chmod 744 /flag.txt

RUN pip install --break-system-packages -r /home/ctf/src/requirements.txt

WORKDIR /home/ctf/src
USER ctf
CMD ["python3", "run.py"]
