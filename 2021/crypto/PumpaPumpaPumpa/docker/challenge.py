import hashlib
import base64
import os
import random
import sys

key = os.urandom(64)

def get_mac(message):
    global key
    return hashlib.sha256(key + message).hexdigest()

def is_valid(message, signature):
    try:
        message = message.encode()
    except:
        pass
    return get_mac(message) == signature

def menu():
    print()
    print("Enter command: ", end="")
    message = sys.stdin.buffer.readline().strip()
    signature = input("Enter signature: ")

    if not is_valid(message, signature):
        print(f"Invalid signature")
        return

    if b"print_flag" in message:
        with open("flag.txt", "r") as f:
            flag = f.readline().strip()
            print(flag)

    elif b"get_random_number" in message:
        print(random.randint(0,1000000))

    elif b"ping" in message:
        print("pong")

    else:
        print("Invalid command")

def main():
    print("Welcome to my service!")
    print("Some commands you can try:")

    pingmac = get_mac(b"ping")
    randmac = get_mac(b"get_random_number")

    print(f"ping                 signature={pingmac}")
    print(f"get_random_number    signature={randmac}")
    print("I'm not going to give you a signature for print_flag, figure it out yourself")
    print("-"*20)

    while True:
        menu()

if __name__ == "__main__":
    main()
