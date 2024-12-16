FROM golang:1.22-alpine3.20 AS build

WORKDIR /src

COPY go.mod main.go index.html mirror.png ./

RUN go build -o /bin/robotfilter .

FROM alpine:3.20

WORKDIR /app

RUN apk add --no-cache imagemagick

COPY .lego .lego
COPY Caveat-VariableFont_wght.ttf ./

COPY --from=build /bin/robotfilter /bin/robotfilter

CMD ["/bin/robotfilter"]
