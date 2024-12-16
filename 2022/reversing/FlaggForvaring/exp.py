#!/usr/bin/env python3

import sys

import z3

key = [z3.BitVec(f"{i:2}", 8) for i in range(29)]

s = z3.Solver()

# Dashes every 5 characters, else numbers
for index, i in enumerate(key):
    if index in [5, 11, 17, 23]:
        s.add(i == ord("-"))
    else:
        s.add(i >= 0x30, i <= 0x39)

# Sum equal to 0x5d1
s.add(sum(k for k in key) == 0x5d1)

# Other constraints from decompiled code
s.add(key[6] + key[7] + key[8] + key[9] + key[10] == 0x110)
s.add(key[0] == key[3], key[3] == key[10], key[10] == key[24])
s.add(key[0] == ord('9'))
s.add(key[0] + key[1] + key[2] + key[3] + key[4] == 0x10c)
s.add(key[12] + key[13] + key[14] + key[15] + key[16] == 0xfd)
s.add(key[13] == key[12] + 1)
s.add(key[14] == key[13] + 4)
s.add(key[13] == key[16], key[13] == key[18], key[13] == key[26])
s.add(key[4] == key[15], key[4] == key[21])
s.add((key[6] ^ key[7]) == 2)
s.add((key[6] ^ key[10]) == 0xe)
s.add(key[19] == key[20] + 1)

# Known substring from decompiled code
for k, char in zip(key[24:], "92127"):
    s.add(k == ord(char))

if s.check() != z3.sat:
    print("Z3 says constraints are not satisfiable, exiting.")
    sys.exit(1)

print("Valid license keys:")
while s.check() == z3.sat:
    m = s.model()
    model = sorted([(index, m[index]) for index in m], key=lambda x: str(x[0]))
    print("".join([chr(key_char[1].as_long()) for key_char in model]))

    s.add(z3.Or([f != s.model()[f] for f in key]))
