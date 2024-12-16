
import sys

# OTP key (i.e. random data)
overlay = [0x66, 0xf4, 0xfe, 0x33, 0xdf, 0xd3, 0x5c, 0xf1,
    0x31, 0xc5, 0x30, 0xd5, 0x1a, 0xf7, 0xb3, 0xab,
    0xf9, 0x8a, 0xeb, 0xd1, 0xc6, 0x1f, 0x55, 0x23,
    0x2b, 0x3d, 0x35, 0x60, 0x03, 0x81, 0x8d, 0x6a,
    0xa6, 0x8d, 0xe9, 0x7c, 0x8c, 0x34, 0x8f, 0x20,
    0x93, 0x40, 0xa1, 0x6c, 0x75, 0x68, 0xcd, 0x48,
    0x61, 0x30, 0x6d, 0x2b, 0x67, 0x67, 0xdf, 0xeb,
    0x74, 0xc8, 0x31, 0x5c, 0x03, 0x5f, 0x0d, 0xc5,
    0x83, 0x98, 0x22, 0xc1, 0xda, 0xed, 0x1a, 0x6e,
    0xe5, 0xd3, 0x0d, 0xb6, 0x51, 0x75, 0x37, 0x8a,
    0xcd, 0xcb, 0xa5, 0x34, 0x03, 0x3c, 0x3c, 0xa8,
    0x5a, 0x14, 0xb0, 0x5a, 0x47, 0x1c, 0x8b, 0x44,
    0x99, 0x10, 0xc5, 0xd7]

flag = "cratectf{OTP är oknäckbart, men bara om man gör rätt}"

if False:
    # use offset between within the ciphertexts
    hint = "The truth is in there. Seven and the Difference will prevail in dark times."
    padding = "padding"
else:
    # no offset between ciphertexts
    padding = ""
    hint = "The truth is in there. The Difference will prevail in dark times."

def do_xor(first, second):
    length = min(len(first), len(second))
    res = []

    for i in range(0, length):
        res = res + [first[i] ^ second[i]]

    return res

def do_otp(text, padding):
    clear_text = list(map(ord, padding + text))
    cipher = do_xor(overlay, clear_text)
    return cipher[len(padding):]

def printHex(bytes):
    for i in range(0, len(bytes)):
        if (i % 16 == 0) & (i > 0):
            sys.stdout.write("\n")
        sys.stdout.write("%02X " % bytes[i])
    sys.stdout.write("\n")

print(type(overlay))
hintCipher = do_otp(hint, "")
flagCipher = do_otp(flag, padding)

printHex(hintCipher)
sys.stdout.write("\n")
printHex(flagCipher)
sys.stdout.write("\n")
sys.stdout.write(hint)
sys.stdout.write("\n")
sys.stdout.write("\n")

#def testOTP(hintc, flagc, hint, startOffset, endOffset):
#    for i in range(startOffset, endOffset + 1):
#        xoredCiphers = do_xor(hintc[i:], flagc)
#        recovered = do_xor(xoredCiphers, hint[i:].encode('ascii'))
#        sys.stdout.write("%d: %s\n" % (i, ''.join(map(chr, recovered))))
         
#testOTP(hintCipher, flagCipher, hint, 0, 10)

