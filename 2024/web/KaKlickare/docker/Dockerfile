FROM php:bookworm

ENV DEBIAN_FRONTEND noninteractive

# Set the locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf
# Add Resources
COPY src /home/ctf/src

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod -R 555 /home/ctf/src

WORKDIR /home/ctf/src
USER ctf
CMD ["php", "-S", "0.0.0.0:8000"]
