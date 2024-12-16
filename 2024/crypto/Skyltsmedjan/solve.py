from pwn import *
from sympy.ntheory import factorint
from functools import reduce

# p = process(["python", "./docker/skyltsmedjan.py"], shell=False)
p = remote("localhost", 2456)

for _ in range(0,22):
    p.readline() 

userid = p.readline().split(b"nr. ")[1].split(b"!")[0].decode("utf-8")
n = int(p.readline().split(b" = ")[1])
e = int(p.readline().split(b" = ")[1])

msg = f"Kund nr. {userid} får hämta flaggan".encode("utf-8")
m = int.from_bytes(msg, "little")
f = factorint(m, multiple=True, limit=100_000)
print(f)
if len(f) == 1:
    print("prime? try again")
    raise SystemExit(1)
m1n = reduce(lambda x, y: x * y, f[0:-1])
m2n = f[-1]

m1 = m1n.to_bytes((m1n.bit_length() + 7) // 8, "little")
m2 = m2n.to_bytes((m2n.bit_length() + 7) // 8, "little")

if b"\n" in m1 or b"\n" in m2:
    print("uh oh, newline in message, try again")
    raise SystemExit(1)

print(m1)
print(m2)

p.sendlineafter(b"? ", b"s")
p.sendlineafter(b"> ", m1)
a = int(p.readline())
p.sendlineafter(b"? ", b"s")
p.sendlineafter(b"> ", m2)
b = int(p.readline())

assert pow(a, e, n) == m1n
assert pow(b, e, n) == m2n

s = (a * b) % n

p.sendlineafter(b"? ", b"f")
p.sendlineafter(b"> ", msg)
p.sendlineafter(b"> ", str(s).encode("utf-8"))
print(p.readline().decode("utf-8").strip())
