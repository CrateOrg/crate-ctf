FROM python:3.10-alpine

# CTF user account
RUN addgroup -S ctf && adduser -S -D -G ctf ctf

RUN apk --no-cache add curl py3-numpy
ENV PYTHONPATH=/usr/lib/python3.10/site-packages

WORKDIR /home/ctf

COPY --chown=ctf:ctf *.sh server.py ./

RUN chmod +x *.sh server.py

ENTRYPOINT [ "./server.py", "38994" ]
EXPOSE 38994
HEALTHCHECK CMD curl -f http://localhost:38994/ctf.sh || exit 1
