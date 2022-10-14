# FROM cosmtrek/air
FROM golang:1.19.2

WORKDIR /app 

COPY main.go /app
COPY go.mod /app
COPY .air.toml /app

RUN curl -fLo install.sh https://raw.githubusercontent.com/cosmtrek/air/master/install.sh \  
    && chmod +x install.sh && sh install.sh && cp ./bin/air /bin/air

CMD go run main.go