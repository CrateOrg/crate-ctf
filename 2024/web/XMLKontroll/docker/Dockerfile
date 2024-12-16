FROM python:3.12

WORKDIR /app
RUN useradd -r "cratectf{xml_xxe_xploit_xpert}"
RUN groupadd -r ctf && useradd -r -g ctf ctf
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py ./
COPY templates/ /app/templates
USER ctf
ENTRYPOINT [ "gunicorn", "-w", "4", "-b", "0.0.0.0", "--access-logfile", "-", "app:app" ]
