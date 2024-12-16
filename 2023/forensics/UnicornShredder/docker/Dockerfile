FROM php:8.2-apache-bullseye
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN pip install pillow
COPY src/ /var/www/
RUN chmod 777 /var/www/html/shreds
