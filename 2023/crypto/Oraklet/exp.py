#!/usr/bin/env python3
# Adapted from https://github.com/flast101/padding-oracle-attack-explained

import base64

from pwn import *

##########################################
# Padding Oracle Attack Proof of Concept #
##########################################

BLOCK_SIZE = 128
BYTE_NB = BLOCK_SIZE//8
IV = '\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00' # Unknown

#p = process("./challenge.py")
p = remote("challs.crate.nu", 16621)
p.recvuntil(b"att dekryptera:")

def oracle(data):
    p.sendline(base64.b64encode(data))
    stdout = p.recvuntil(b"att dekryptera:")
    return b"Dekrypterat meddelande" in stdout or b"skulle kunna vara en flagga" in stdout


def decrypt(encrypted):
    # print(oracle(encrypted))
    # return ""
    block_number = len(encrypted)//BYTE_NB
    decrypted = bytes()
    # Go through each block
    for i in range(block_number, 0, -1):
        current_encrypted_block = encrypted[(i-1)*BYTE_NB:(i)*BYTE_NB]

        # At the first encrypted block, use the initialization vector if it is known
        if i == 1:
            previous_encrypted_block = bytearray(IV.encode("ascii"))
        else:
            previous_encrypted_block = encrypted[(i-2)*BYTE_NB:(i-1)*BYTE_NB]

        bruteforce_block = previous_encrypted_block
        current_decrypted_block = bytearray(IV.encode("ascii"))
        padding = 0

        # Go through each byte of the block
        for j in range(BYTE_NB, 0, -1):
            padding += 1

            # Bruteforce byte value
            for _ in range(0,256):
                bruteforce_block = bytearray(bruteforce_block)
                bruteforce_block[j-1] = (bruteforce_block[j-1] + 1) % 256
                joined_encrypted_block = bytes(bruteforce_block) + current_encrypted_block

                # Ask the oracle
                if oracle(joined_encrypted_block):
                    current_decrypted_block[-padding] = bruteforce_block[-padding] ^ previous_encrypted_block[-padding] ^ padding

                    # Prepare newly found byte values
                    for k in range(1, padding+1):
                        bruteforce_block[-k] = padding+1 ^ current_decrypted_block[-k] ^ previous_encrypted_block[-k]

                    break

        decrypted = bytes(current_decrypted_block) + bytes(decrypted)

    return decrypted[:-decrypted[-1]]  # Padding removal

ciphertext = input("Enter encrypted message as base64: ")
plaintext_bytes = decrypt(base64.b64decode(ciphertext))
print(plaintext_bytes.decode("utf-8", errors="replace"))
