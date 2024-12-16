FROM php:8.3-apache-bookworm
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
# Python packages should normally be installed in a virtualenv,
# but we can easily rebuild the image if we break system packages.
RUN pip install --break-system-packages pillow geopy
COPY --chown=www-data:www-data src/ /var/www/
