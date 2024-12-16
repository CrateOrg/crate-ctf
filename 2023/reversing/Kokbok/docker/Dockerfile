FROM mongo:latest
EXPOSE 27017

ENV MONGO_INITDB_ROOT_USERNAME=dev
ENV MONGO_INITDB_ROOT_PASSWORD=a-top-secret-developer-password
ENV MONGO_INITDB_DATABASE=Kokbok

COPY flag_doc.json unika_rena_recept.json /
COPY mongo-init.js /docker-entrypoint-initdb.d

RUN chmod +x /docker-entrypoint-initdb.d/mongo-init.js
