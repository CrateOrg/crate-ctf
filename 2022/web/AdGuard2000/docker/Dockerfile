FROM php:7.4-apache
RUN apt-get update && apt-get upgrade -y
RUN apt-get install sqlite3 -y
COPY html/ /var/www/html/
RUN sqlite3 /var/www/html/adguard.db < /var/www/html/adguard.sql
RUN rm /var/www/html/adguard.sql
RUN chown www-data.www-data /var/www/html/adguard.db
# TODO add php.ini?
