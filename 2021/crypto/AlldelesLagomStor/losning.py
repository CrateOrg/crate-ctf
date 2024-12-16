from Crypto.Util import number
import math


def powinv3(x):
    high = x
    low = 0
    curr = x//2
    test = pow(curr, 3)
    while test != x:
        if test > x:
            high = curr
        if test < x:
            low = curr
        oldcurr = curr
        curr = low+((high-low)//2)
        test = pow(curr, 3)
        if curr == oldcurr:
            break
    return curr

assert( powinv3(pow(3213123, 3)) == 3213123 )
assert( powinv3(pow(5555555555, 3)) == 5555555555 )

with open("output.txt", "r") as f:
    c = int(f.readline().strip().split(" = ")[-1], 16)
    n = int(f.readline().strip().split(" = ")[-1], 16)

i = 0
while True:
    test = powinv3(c+i*n)
    if pow(test, 3, n) == c:
        print(bytes.fromhex(hex(test)[2:]))
        break
    i += 1
