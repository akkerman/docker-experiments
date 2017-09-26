FROM node:8.5-alpine
LABEL maintainer "Marcel Akkerman <ikbenMarcelAkkerman@hotmail.com>"
ADD . /app
WORKDIR /app
RUN npm install --silent
EXPOSE 3000
CMD ["/usr/local/bin/node", "/app/index.js"]

