FROM python:3.13-bullseye

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install build-essential

RUN pip install pymodbus==3.7.4
RUN pip install numpy==2.1.2
RUN pip install twisted==24.10.0
RUN pip install pillow==11.0.0
RUN mkdir /chall

ADD 6x12-ISO8859-1.pcf.gz /chall/
ADD modbus_tcp_master.py /chall/

USER nobody:nogroup
WORKDIR /chall/

CMD [ "python3", "modbus_tcp_master.py" ]
