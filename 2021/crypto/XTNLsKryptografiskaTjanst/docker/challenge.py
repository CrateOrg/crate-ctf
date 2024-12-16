import base64
import itertools
import sys

flag = "cratectf{kan_man_ens_kalla_detta_kryptografi}"

def encrypt(data: str):
    retval = ""

    middle = int(len(data)/2)

    lower_half = data[:middle]
    upper_half = data[middle:]

    if len(lower_half)%2 == 1:
        lower_half += "?"
    if len(upper_half)%2 == 0:
        upper_half += "?"


    low_middle = int(len(lower_half)/2)
    lower_low_half = lower_half[:low_middle]
    upper_low_half = lower_half[low_middle:]
    for a, b in zip(lower_low_half, upper_low_half[::-1]):
        retval = retval + a + b

    high_middle = int(len(upper_half)/2)
    retval = retval + upper_half[high_middle]
    i = 1
    while high_middle+i < len(upper_half):
        retval = retval + upper_half[high_middle+i]
        retval = retval + upper_half[high_middle-i]
        i += 1

    return retval


def main():
    encrypted_flag = encrypt(flag)

    print("Välkommen till Xtnls Kryptografiska Tjänst!")
    print(f"Här är en flagga som jag har krypterat: {encrypted_flag}")
    print("Du får nu själv testa att kryptera lite grejer!")

    while True:
        line = input("=> ")
        encrypted_data = encrypt(line)
        print(f"Krypterad: {encrypted_data}")
        
def test():
    assert(encrypt("1") == "1")
    assert(encrypt("12") == "1?2")
    assert(encrypt("123") == "1?3?2")
    assert(encrypt("1234") == "124?3")
    assert(encrypt("12345") == "12453")
    assert(encrypt("123456") == "1?23564")
    assert(encrypt("1234567") == "1?23675?4")
    assert(encrypt("12345678") == "1423786?5")

if __name__ == "__main__":
    main()

