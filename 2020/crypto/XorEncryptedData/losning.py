import pwn

# get some data (50 samples)
data = []
for _ in range(50):
    #p = pwn.remote("127.0.0.1", 13337)
    p = pwn.process(["python3", "./randnumservice.py"])
    p.readline()
    hexstring = p.readline().decode("ascii").strip()
    data.append(hexstring)

def get_bit_number(hexstr, n):
    index = n//4
    offset = n%4
    as_int = int(hexstr[index], 16)
    return (as_int >> (3-offset)) & 1

answer_bits = ""

# for each position, check which bit is most commonly on that position in the data
for i in range(len(data[0])*4):
    m = 0
    for s in data:
        info = get_bit_number(s, i)
        if info == 0:
            m -= 1
        else:
            m += 1

    if m > 0:
        answer_bits += "1"
    else:
        answer_bits += "0"

# print out the answer (this is a mess)
print( int(answer_bits, 2).to_bytes(len(data[0])//2, byteorder="big") )
