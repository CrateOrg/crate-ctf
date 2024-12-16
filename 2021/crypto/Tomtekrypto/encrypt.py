import random

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
original = [x for x in alphabet]
shuffled = [x for x in alphabet]
random.shuffle(shuffled)

encryption_dict = dict()
for a, b in zip(original, shuffled):
    encryption_dict[a] = b
    encryption_dict[a.upper()] = b.upper()

original = ""
with open("text.txt", "r") as f:
    original = f.read()

encrypted = ""
for c in original:
    if c in encryption_dict:
        encrypted += encryption_dict[c]
    else:
        encrypted += c

print(encrypted)
