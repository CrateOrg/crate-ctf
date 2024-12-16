import random

flag = "cratectf{var_det_en_IRriterande_uppgift?}"
key1 = [218, 225, 38, 71, 151, 157, 92, 9, 160, 177, 217, 167, 170, 23, 176, 184, 229, 42, 101, 222, 202, 108, 142, 232, 165, 181, 11, 152, 90, 6, 51, 35, 249, 94, 229, 94, 61, 143, 54, 13, 37]
print(key1)

encrypted_1 = []
for c, char in zip(key1, flag):
    encrypted_1.append(c^ord(char))

encrypted_2 = []
for c in encrypted_1:
    encrypted_2.append(c+423)

encrypted_3 = []
for c1, c2 in zip(encrypted_2, encrypted_2[1:]+[32]):
    encrypted_3.append(c1^c2)

print(encrypted_1)
print(encrypted_2)
print(encrypted_3)

