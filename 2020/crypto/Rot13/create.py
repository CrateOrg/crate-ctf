import string
import sys

word = "ETABLISSEMANG"
if len(sys.argv) > 1:
    word = sys.argv[1]

upper_letters = string.ascii_uppercase + "ÅÄÖ"
lower_letters = string.ascii_lowercase + "åäö"

output = ""
for c in word:
    if c in upper_letters:
        idx = (upper_letters.index(c)+13) % len(upper_letters)
        output += upper_letters[idx]
    if c in lower_letters:
        idx = (lower_letters.index(c)+13) % len(lower_letters)
        output += lower_letters[idx]
    else:
        output += c

print(output)
