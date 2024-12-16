#!/usr/bin/env python3

import argparse

from pwn import *


def string_to_hex(string: str):
    for char in string:
        byte = char.encode('ascii')
        byte = xor(byte, b"\x71")
        yield hex(int.from_bytes(byte))

def main():
    parser = argparse.ArgumentParser(
        description="Convert flag to bytes and obfuscate it"
    )
    parser.add_argument("flag", help="Flag as string")

    args = parser.parse_args()

    print(", ".join(string_to_hex(args.flag)))


if __name__ == "__main__":
    main()
