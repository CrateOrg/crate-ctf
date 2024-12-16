FROM wordpress

# For the 404 redirect flag
RUN echo 'ErrorDocument 404 /404.php' >> /etc/apache2/apache2.conf

# Copy our own content. /var/www/html is a volume defined in the container itself (?)
# so the copy must take place after starting.
COPY wordpress-content-*.tar.gz /tmp
RUN cd /tmp && \
  mkdir -p wordpress && \
  cd wordpress && \
  tar zxf ../wordpress*.gz && \
  chown root.www-data * -R && \
  chmod 660 messages/messages

# Make sure the setup script copies from our path, not the default installation
RUN sed -i s,/usr/src/wordpress,/tmp/wordpress, /usr/local/bin/docker-entrypoint.sh
RUN sed -i '$ichown -R root:www-data /var/www/html/' /usr/local/bin/docker-entrypoint.sh
