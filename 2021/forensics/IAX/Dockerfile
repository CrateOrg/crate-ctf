FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

# Typical devel stuff TODO move to own image
RUN apt-get install -y vim net-tools git cscope ctags build-essential colormake gdb cgdb
RUN apt-get install -y python3
RUN apt-get install -y tcpdump tshark
RUN apt-get install -y socat netcat curl wget
RUN apt-get install -y iproute2 inetutils-ping

WORKDIR /root
RUN wget https://github.com/pjsip/pjproject/archive/2.10.tar.gz
RUN tar zxvf 2.10.tar.gz; cd pjproject-2.10; ./configure; make dep; make
RUN cp /root/pjproject-2.10/pjsip-apps/bin/pjsua-x86_64-unknown-linux-gnu /usr/local/bin/
COPY *.wav /root/
