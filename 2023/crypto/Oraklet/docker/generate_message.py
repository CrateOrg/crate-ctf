#!/usr/bin/env python3

import argparse
import base64
import sys

import Crypto.Util.Padding
from Crypto.Cipher import AES

import challenge


def main():
    parser = argparse.ArgumentParser(description="Generate encrypted message from stdin")
    parser.parse_args()

    cipher = AES.new(key=challenge.key, iv=challenge.iv, mode=AES.MODE_CBC)
    plaintext = input().encode("utf-8")
    padded_plaintext = Crypto.Util.Padding.pad(plaintext, block_size=16, style="pkcs7")
    sys.stdout.buffer.write(base64.b64encode(cipher.encrypt(padded_plaintext)) + b"\n")

if __name__ == "__main__":
    main()
