import random

def get_random_bit():
    if random.randint(1,10) <= 3:
        return 1
    return 0

def generate_key(nbytes):
    retkey = b""
    
    for i in range(nbytes):
        intval = get_random_bit()
        for _ in range(7):
            intval <<= 1
            intval |= get_random_bit()
        retkey += bytes([intval])

    return retkey

def main():
    flag = "bruh"
    with open("flag.txt", "rb") as f:
        flag = f.readline().strip()

    print("Here is an XOR-encrypted flag for you:")

    encrypted = b""
    for a, b in zip(flag, generate_key(len(flag))):
        encrypted += bytes([a^b])
    hexdata = ''.join(format(x, '02x') for x in encrypted) + "\n"
    print(hexdata)

if __name__ == "__main__":
    main()
