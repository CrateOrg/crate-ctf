from Crypto.Util import number
import math

with open("output.txt", "r") as f:
    n1 = int(f.readline().strip().split(" = ")[-1])
    n2 = int(f.readline().strip().split(" = ")[-1])
    c1 = int(f.readline().strip().split(" = ")[-1], 16)

p = math.gcd(n1, n2)
q = n1//p

d = number.inverse(65537, (p-1)*(q-1))

m = pow(c1, d, n1)

print(bytes.fromhex(hex(m)[2:]))
