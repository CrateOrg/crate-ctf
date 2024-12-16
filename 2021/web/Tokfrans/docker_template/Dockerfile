FROM php:8-apache-buster

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y unzip p7zip git

# TODO timezone / localtime?

RUN a2enmod rewrite

# Composer install
ADD composer_install.sh /tmp/
RUN sh /tmp/composer_install.sh
RUN ./composer.phar require adhocore/jwt
# ...and clean up
RUN apt-get remove -y git
RUN rm composer.phar

# Site
ADD *.php /var/www/html/
ADD *.png /var/www/html/

