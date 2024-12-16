#!/usr/bin/env python3

import random
import time

FLAG = "cratectf{wow_you_must_be_really_lucky}"

banner = r"""
  ██╗ ██╗     ██████╗ ██████╗ ███████╗ █████╗ ████████╗     ██████╗ ██████╗ ██████╗ ███████╗     ██████╗  █████╗ ███╗   ███╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗      ██████╗ ██████╗        ██╗ ██╗  
 ██╔╝██╔╝    ██╔════╝ ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝    ██╔═══██╗██╔══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔══██╗██║     ██║████╗  ██║██╔════╝     ██╔════╝██╔═══██╗       ╚██╗╚██╗ 
██╔╝██╔╝     ██║  ███╗██████╔╝█████╗  ███████║   ██║       ██║   ██║██║  ██║██║  ██║███████╗    ██║  ███╗███████║██╔████╔██║██████╔╝██║     ██║██╔██╗ ██║██║  ███╗    ██║     ██║   ██║        ╚██╗╚██╗
╚██╗╚██╗     ██║   ██║██╔══██╗██╔══╝  ██╔══██║   ██║       ██║   ██║██║  ██║██║  ██║╚════██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══██╗██║     ██║██║╚██╗██║██║   ██║    ██║     ██║   ██║        ██╔╝██╔╝
 ╚██╗╚██╗    ╚██████╔╝██║  ██║███████╗██║  ██║   ██║       ╚██████╔╝██████╔╝██████╔╝███████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║██████╔╝███████╗██║██║ ╚████║╚██████╔╝    ╚██████╗╚██████╔╝██╗    ██╔╝██╔╝ 
  ╚═╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═════╝ ╚═╝    ╚═╝ ╚═╝  
"""

print(banner)
print("*** Guess the number and win a prize! ***")
print("Model: MT19937")
print("=========================================")


print("Setting RNG seed", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(1)
random.seed()
print("done")

guess_count = 0
correct_answers = 0
required_answers = 3

while True:
    random_number = random.getrandbits(32)

    guess_count += 1
    if guess_count > 1000:
        print("I'm getting tired, try again later")
        break

    try:
        guess = int(input("What is your guess? "))
    except EOFError:
        print("Bye!")
        break
    except Exception:
        print("Invalid input, try again")
        continue

    if guess == random_number:
        correct_answers += 1
        if correct_answers >= required_answers - 1:
            print("Well done! Here is the flag:", FLAG)
            break
        else:
            print("Wow, that was correct! But can you guess the next number as well?")
    else:
        print("Incorrect, I was thinking of the number", random_number)
        correct_answers = 0
