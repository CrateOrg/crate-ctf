FROM node:20-alpine3.20

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY index.js ./

RUN echo "cratectf{mamma_sa_att_det_är_taskigt_att_hacka_och_jag_tror_att_du_nyss_gjorde_det}" > /flag.txt

EXPOSE 2580

CMD ["npm", "run", "run"]
