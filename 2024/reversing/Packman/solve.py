import struct
base = 0x50

def findDistance(start):
    # this code is spaghetti because im having a brainfreeze figuring out how to do this with math
    print("in find distance", start)
    current = base
    for i in range(0,start):        
        current += 1
        if current == 256:
            current = 0

    print("final current: ", current, chr(current))
    return current

with open('flag.packed', 'rb') as f1:
    with open('flagrecvoered', 'wb') as f2:
        #while True:
        print(0xff-base)
        while True:
            byte, count = ord(f1.read(1)), f1.read(2)
            actualByte = findDistance(byte)
            #print(hex(byte), actualByte, chr(actualByte), count)
            c = struct.unpack('>H', count)[0]
            for i in range(0,c):
                print("wrote")
                f2.write(actualByte.to_bytes(1, 'big'))
