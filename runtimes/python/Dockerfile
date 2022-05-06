FROM python:3.7-alpine

RUN mkdir runtime

RUN apk update

RUN apk add wget

RUN apk add bash

RUN apk add --upgrade unzip

RUN apk add python3

COPY runtimes/python /runtime

WORKDIR /runtime

RUN mkdir enigpy

COPY packages/enigpy /runtime/enigpy

RUN dos2unix fetch-and-setup.sh