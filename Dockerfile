FROM alpine:latest

RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    gcc \
    g++ \
    cmake \
    make \
    libc-dev

COPY Prog /Program
RUN mkdir /Program/Share
WORKDIR /Program/Share
