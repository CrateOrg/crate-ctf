#!/usr/bin/env python3
import random
import socket
import struct
import time


def send_tlv_request(host, port, tlv_type):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Create and send the TLV request
    data = random.randbytes(random.randint(1, 500))
    length = len(data)
    client_socket.sendall(struct.pack("!BH", tlv_type, length) + data)

    # Receive the response (type and length first)
    response_header = client_socket.recv(3)
    response_type, response_length = struct.unpack("!BH", response_header)

    # Receive the response value
    response_value = client_socket.recv(response_length)

    print(
        f'Received response for type {response_type}: {response_value.decode("utf-8", errors="replace")}'
    )
    client_socket.close()


def main():
    host = "challs.crate.nu"
    port = 56412

    types = [i % 4 for i in range(10)]
    random.shuffle(types)

    for tlv_type in types:
        send_tlv_request(host, port, tlv_type)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
