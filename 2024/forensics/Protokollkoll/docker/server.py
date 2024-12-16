#!/usr/bin/env python3
import struct
import sys
import hashlib
import signal


def timeout_handler(_signum, _frame):
    sys.exit(1)

def main():
    # Set timeout to 5 seconds
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)

    # Read the type (1 byte) and length (2 bytes)
    header = sys.stdin.buffer.read(3)
    if len(header) < 3:
        sys.exit(0)

    tlv_type, length = struct.unpack("!BH", header)

    # Read the value
    value = sys.stdin.buffer.read(length)
    if len(value) < length:
        sys.exit(0)

    # Handle the request
    if tlv_type == 0:
        response = hashlib.md5(value, usedforsecurity=False).digest()[2:5]
    elif tlv_type == 1:
        response = hashlib.sha1(value, usedforsecurity=False).digest()[0:8]
    elif tlv_type == 2:
        response = hashlib.sha256(value, usedforsecurity=False).digest()[6:10]
    elif tlv_type == 5:
        response = "cratectf{ingen_autentisering_här_inte}".encode("utf-8")
    else:
        response = b"Error"

    # Send the response
    response_data = response
    response_length = len(response_data)
    sys.stdout.buffer.write(
        struct.pack("!BH", tlv_type, response_length) + response_data
    )


if __name__ == "__main__":
    main()
