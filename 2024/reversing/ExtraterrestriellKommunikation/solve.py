from PIL import Image
from math import lcm
import collections
import math

morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '{': '---...', '}': '...---'
}

def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st

ascii_to_coord = {}

for letter in morse_code_dict: 
    ascii_to_coord[letter] = morse_code_dict[letter].count('-'), morse_code_dict[letter].count('.')

coord_to_ascii = {}
for a in ascii_to_coord:
    coord_to_ascii[convertTuple(ascii_to_coord[a])] = []
    for b in ascii_to_coord:
        if ascii_to_coord[a] == ascii_to_coord[b]:
            if b not in coord_to_ascii:
                coord_to_ascii[convertTuple(ascii_to_coord[a])].append(b)

im = Image.open('./flag.png')
size = im.size[0]
order = {}
added = 0
for j in range(0,size):
    for i in range(0,size):
        
        p = im.getpixel((i,j))
        if p == (0,0,0):
            continue
        # if i == 0:
        #     print(p[0], p[2])
        pos = (p[2] - 1)/256
        inside = False
        for item in order:
            if str(pos) == item:
                inside = True
        if not inside:
            added += 1
            order[str(pos)] = ((i,j), p[0])

print(order, added)
pSize = size / 5
print("pSize: ", pSize)

flag = {}
for k in order:
    rChannel = order[k][1]
    x = order[k][0][0]
    y = order[k][0][1]
    xMod = x % pSize
    yMod = y % pSize
    indexY = (x - xMod) / pSize 
    indexX = (y - yMod) / pSize 
    print(x, y, xMod, yMod)
    print(indexY, indexX)
    c = coord_to_ascii[convertTuple((int(indexY), int(indexX)))]
    print(c, rChannel, (len(c)*(rChannel-1))/256)
    index = round((len(c)*(rChannel-1))/256)
    print(c[index])
    flag[k] = c[index]
    print('\n')

print(flag)
sortedFlag = collections.OrderedDict(sorted(flag.items()))
print(sortedFlag)
flag = ''
for ind in sortedFlag:
    flag += sortedFlag[ind]
print(flag)
        #(index/len(m)*256) + 1)
