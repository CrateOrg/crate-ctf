FROM python:3.11

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py index.html ./
ENTRYPOINT [ "gunicorn", "-w", "4", "-b", "0.0.0.0", "--access-logfile", "-", "app:app" ]
