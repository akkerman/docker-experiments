FROM node:9
LABEL maintainer "Marcel Akkerman <ikbenMarcelAkkerman@hotmail.com>"

RUN mkdir -p /app
WORKDIR /app

COPY package.json ./
RUN npm install

COPY src/ ./src/
COPY server.js ./


EXPOSE 3000
VOLUME /app/src


CMD ["node", "server.js"]
