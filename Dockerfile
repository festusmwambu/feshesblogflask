FROM python:slim

RUN useradd feshesblogflask

WORKDIR /home/feshesblogflask

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY feshesblog_flask feshesblog_flask
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP app.py

RUN chown -R feshesblogflask:feshesblogflask ./
USER feshesblogflask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
