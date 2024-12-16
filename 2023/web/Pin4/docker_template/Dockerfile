FROM alpine:3.18

# make sure you can use HTTPS
RUN apk --update add ca-certificates

# Install packages
RUN apk --no-cache add php82 php82-fpm php82-json php82-opcache php82-openssl php82-curl \
    nginx supervisor curl

# Configure nginx
COPY config/nginx.conf /etc/nginx/nginx.conf

# Remove default server definition
#RUN rm /etc/nginx/conf.d/default.conf

# Configure PHP-FPM
COPY config/fpm-pool.conf /etc/php82/php-fpm.d/www.conf
COPY config/php.ini /etc/php82/conf.d/custom.ini

# Configure supervisord
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setup document root
RUN mkdir -p /var/www/html

# Make sure files/folders needed by the processes are accessable when they run under the nobody user
RUN chown -R nobody.nobody /var/www/html && \
  chown -R nobody.nobody /run && \
  chown -R nobody.nobody /var/lib/nginx && \
  chown -R nobody.nobody /var/log/nginx && \
  chown -R nobody.nobody /var/log/php*

# Switch to use a non-root user from here on
USER nobody

# Add application
WORKDIR /var/www/html
COPY --chown=nobody src/ /var/www/html/

# Expose the port nginx is reachable on
#EXPOSE 8080

# Let supervisord start nginx & php-fpm
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

# Configure a healthcheck to validate that everything is up&running
#HEALTHCHECK --timeout=10s CMD curl --silent --fail http://127.0.0.1:8080/fpm-ping
