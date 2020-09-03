FROM node:12-alpine

WORKDIR /usr/app

COPY . .

RUN npm install 
RUN npm run build

EXPOSE 3000

CMD [ "node", "dist/server.js" ]