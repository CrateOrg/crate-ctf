#!/usr/bin/env python3

import base64
import binascii

import Crypto.Util.Padding
from Crypto.Cipher import AES

prompt_string = """*** Oraklet ***
=========================================
"""
key = b"AxaNBQ1duTGxy8nk"
iv = b"ntUuLm9w4xXfgk2K"

innocent_messages = [
    "BOwquzaj5VAuw+W243CFTPt+B6Lmg4y+8J0jCMw4MMk4z64Y12gIA+4fB6Tk8oBD",
    "I6gFIFq515l0MgmX5fRm6YOqHj+ZwBP50sSOqxbQizjjWqTKvmdAS9jlBEUUaXnIJtOXUbqlzxFO642SxbMUrA==",
]

def main():
    while True:
        try:
            try:
                user_data = input("Ge mig något att dekryptera: ")
            except EOFError:
                print("Hejdå!")
                break

            cipher = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
            try:
                padded_ciphertext = base64.b64decode(user_data)
            except (binascii.Error, ValueError) as e:
                if "Incorrect padding" in str(e) or "Data must be padded" in str(e):
                    print("* Fel vid avkodning med base64 *")
                continue
            padded_plaintext = cipher.decrypt(padded_ciphertext)
            try:
                plaintext = Crypto.Util.Padding.unpad(padded_plaintext, block_size=16, style="pkcs7")
            except (binascii.Error, ValueError) as e:
                print(f"* Fel vid dekryptering: {e} *")
                continue

            plaintext = plaintext.decode("utf-8", errors="replace")

            if "cratectf" in plaintext or user_data not in innocent_messages:
                print("* Det där meddelandet skulle kunna vara en flagga, det får du inte läsa! *")
            else:
                print("* Dekrypterat meddelande: *")
                print(plaintext)
        except Exception as e:
            print(f"* Något gick fel: {e} *")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
