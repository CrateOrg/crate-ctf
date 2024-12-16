#!/bin/env python3

def byte_xor(b1, b2):
    return bytes([_a ^ _b for _a, _b in zip(b1, b2)])

flag = 'd157f6d302de10d8e1634fea9dbafe08913dea6741511d10725ce1fcd119dbb4040806c40e7aba0c30d63cfb5709e0ed9fe8'
chosen_msg = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
chosen_msg_enc = 'd344f6c606dc05dffb714fe691bac007893fe0634c6f09057253dff3df16d9b03a0206cb306dba1f30e83bfb4404e8eb8af43c273bd40a924fd6'

a = bytes.fromhex(chosen_msg_enc)
b = bytes(chosen_msg, 'utf-8')

ks = byte_xor(a, b)

msg = byte_xor(bytes.fromhex(flag), ks)
print(msg)
