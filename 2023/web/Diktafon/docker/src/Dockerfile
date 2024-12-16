FROM golang:1.21-alpine3.18 AS builder

WORKDIR /src

COPY go.mod go.sum ./

RUN go mod download

COPY *.go ./
COPY components/ components/
COPY database/ database/
COPY method/ method/
COPY sessions/ sessions/
COPY files/ files/

RUN go build -ldflags="-X 'challs.crate.nu/diktafon/log/file.baseLocation=/data'" -o /app ./

FROM alpine:3.18

COPY --from=builder /app /

CMD ["/app"]
