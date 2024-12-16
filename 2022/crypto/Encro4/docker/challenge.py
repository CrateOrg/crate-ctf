#!/bin/env python3
import time

from Crypto.Cipher import ARC4
from Crypto.Hash import SHA

banner = r"""
 _____                       ___           ______           _ _         _____             _     ___   _   _            
|  ___|                     /   |          | ___ \         | | |       /  __ \           | |   /   | | | | |           
| |__ _ __   ___ _ __ ___  / /| |  ______  | |_/ /___  __ _| | |_   _  | /  \/ ___   ___ | |  / /| | | |_| | __ ___  __
|  __| '_ \ / __| '__/ _ \/ /_| | |______| |    // _ \/ _` | | | | | | | |    / _ \ / _ \| | / /_| | |  _  |/ _` \ \/ /
| |__| | | | (__| | | (_) \___  |          | |\ \  __/ (_| | | | |_| | | \__/\ (_) | (_) | | \___  | | | | | (_| |>  < 
\____/_| |_|\___|_|  \___/    |_/          \_| \_\___|\__,_|_|_|\__, |  \____/\___/ \___/|_|     |_/ \_| |_/\__,_/_/\_\
                                                                 __/ |                                                 
                                                                |___/                                                  
"""
print(banner)

key = bytes.fromhex('b37e50cedcd3e3f1ff64f4afc0422084ae694253cf399326868e07a35f4a45fb')
cipher = ARC4.new(SHA.new(key).digest())
print("Welcome to the RC4 encryption service")
print("=====================================")
print("Generating nonce", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(1)
print("error")
msg = input("Input data to be encrypted: ")

enc = cipher.encrypt(msg)
print(enc.hex())
