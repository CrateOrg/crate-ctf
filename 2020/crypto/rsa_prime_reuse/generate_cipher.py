from Crypto.Util import number #pip3 install pycryptdome
import math

from secret import SECRET

prime1 = number.getPrime(1024)
prime2 = number.getPrime(1024)
prime3 = number.getPrime(1024)

n1 = prime1*prime2
n2 = prime2*prime3

m1 = int.from_bytes(SECRET, "big")

c1 = pow(m1, 65537, n1)

with open("output.txt", "w") as f:
    f.write("n1 = " + str(n1) + "\n")
    f.write("n2 = " + str(n2) + "\n")
    f.write("c1 = " + hex(c1) + "\n")
