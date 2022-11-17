FROM python:3.8-slim-buster
#any data will be sent to the terminal
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY . .
RUN apt-get update && apt-get -y install libpq-dev gcc && pip3 install -r requirements.txt

