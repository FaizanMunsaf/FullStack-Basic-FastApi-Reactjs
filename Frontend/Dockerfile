From node:16.20.0
WORKDIR /app
COPY package*.json /app

RUN npm i --silent
RUN npm i -g react-scripts@5.0.1

COPY . ./

CMD [ "npm", "start" ]
