FROM oven/bun:1-alpine AS base
WORKDIR /app

COPY package.json bun.lockb ./
RUN bun install --frozen-lockfile --production
COPY main.tsx tsconfig.json ./

USER bun
CMD [ "bun", "run", "main.tsx" ]
