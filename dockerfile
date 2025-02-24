FROM python:3.12.9-alpine

COPY requirements.txt discord-bot/
COPY src/ discord-bot/src

RUN pip install -r discord-bot/requirements.txt

ENTRYPOINT ["python3", "discord-bot/src/main.py"]