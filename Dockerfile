FROM python:3

RUN apt-get update && apt-get install -y \
    postgresql-client

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
