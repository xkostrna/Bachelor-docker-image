FROM alpine:latest

RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    g++ \
    cmake \
    make

COPY Prog /Program
RUN mkdir /Program/Share
WORKDIR /Program/Share
