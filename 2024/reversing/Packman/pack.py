base = 0x50
currentChar = ''
lastChar = []

def findDistance(target):
    # this code is spaghetti because im having a brainfreeze figuring out how to do this with clean math, without mixing up 0xff and 0x00
    count = 0
    current = base
    for i in range(0,256):
        if current == target:
            return count
        current += 1
        count += 1
        if current == 256:
            current = 0

with open('flag', 'rb') as f1:
    with open('flag.packed', 'wb') as f2:
        try:
            while True:
                currentByte = ord(f1.read(1))

                currentChar = findDistance(currentByte).to_bytes(1, 'big')
                
                print(currentChar)
                if len(lastChar) == 0:
                    lastChar = [currentChar, 1]

                elif currentChar == lastChar[0]:
                    lastChar[1] = lastChar[1] + 1
                else:

                    f2.write(lastChar[0])
                    f2.write((lastChar[1]).to_bytes(2, 'big'))
                    lastChar[0] = currentChar
                    lastChar[1] = 1
                #print("going to next round")
        except:
            try:
                f2.write(lastChar[0])
                f2.write((lastChar[1]).to_bytes(2, 'big'))
            except:
                pass
