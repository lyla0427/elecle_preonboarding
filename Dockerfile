FROM python:3.8-slim-buster
#any data will be sent to the terminal
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get -y install libpq-dev gcc
RUN pip3 install -r requirements.txt
COPY . .
