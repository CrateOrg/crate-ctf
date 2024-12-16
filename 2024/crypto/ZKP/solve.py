from pwn import *
import time
import subprocess
import math
from ctypes import CDLL
from ctypes.util import find_library
from Crypto.Util import number

libc = CDLL(find_library("c"))

host = "localhost"
port = 50008
#
# def run_command(command):
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     stderr = []
#
#     for line in iter(process.stderr.readline, ''):
#         stderr.append(line)
#     process.stderr.close()
#
#     process.wait()
#    
#     return ''.join(stderr)

def mod_inverse_fermat(a, m):
    return pow(a, m-2, m)


def requestRandom(p, g):
    r = number.getRandomRange(1, p-1)
    C = pow(g, r, p)
    return C, r

def requestMod(p, y, g):
    r = number.getRandomRange(1, p-1)

    t1 = pow(g, r, p)
    t2 = mod_inverse_fermat(y, p)
    C = (t1*t2) % p
    return C, r

def verifyMod(p, y, g, C, r):
    t1 = pow(g, r, p)
    t2 = (C*y) % p
    return t1 == t2
def getNext():
    res = libc.rand()
    return res % 2

won = 0
while not won:
    rem = remote(host, port)
    for i in range(0,13):
        rem.recvline()

    p = int(rem.recvline().decode().split(": ")[1][:-1])
    y = int(rem.recvline().decode().split(": ")[1][:-1])
    g = int(rem.recvline().decode().split(": ")[1][:-1])

    t = rem.recvuntil(b']')
    rem.sendline(b"")
    t = int(t.decode().split(' ')[3])
    print("Time received from server: ", t)

    # rtt = round(float(run_command("sudo hping3 -S -p {} {} -c 2".format(port, host).split(" ")).split("round-trip min/avg/max =")[-1].split("/")[1]), 0)
    seed = t #+ round((rtt), 0)
    print("Seed should be", seed)
    # print("RTT: ", rtt)

    #print("Debug, used seed on server: \n", rem.recvline())
    libc.srand(int(seed))
    for i in range(0,100):
        choice = getNext()

        if choice:
            C, r = requestRandom(p,g)
            print("Next is random")
        else:
            C, r = requestMod(p,y,g)
            print("next is mod")
        try:
            rem.recvuntil(b':')
            rem.sendline(str(C).encode())
            rem.recvuntil(b':')
            rem.sendline(str(r).encode())
        except:
            rem.close()
            break
    if i == 99:
        won = 1

rem.interactive()

