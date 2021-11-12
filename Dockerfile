FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt ./
RUN pip install -r requirements.txt
