from Crypto.Util import number #pip3 install pycryptdome
import math

from secret import SECRET

p = number.getPrime(2048)
q = number.getPrime(2048)
n = p*q
m = int.from_bytes(SECRET, "big")
while pow(m, 3) == pow(m, 3, n):
    SECRET += b"X"
    m = int.from_bytes(SECRET, "big")

c = pow(m, 3, n)

with open("output.txt", "w") as f:
    f.write("c = " + hex(c) + "\n")
    f.write("n = " + hex(n) + "\n")
