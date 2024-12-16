#!/usr/bin/env python3

from pwn import remote, log

# I tried to implement this based on some C code that partially implemented the attack,
# but it didn't quite work. This was easier in the end and saves a lot of debugging work.
from randcrack import RandCrack


p = remote("challs.crate.nu", "16484")
rc = RandCrack()

state = log.progress("Fetching 624 values to determine state")
for i in range(624):
    p.recvuntil(b"guess?")
    p.sendline(b"1")
    p.recvuntil(b"Incorrect, I was thinking of the number")

    rc.submit(int(p.recvline().strip()))
    state.status(f"{i}/624")

state.success(f"Done, has_state = {rc.state}")

# Send another guess to ensure that recvline() has something to read
p.sendline(b"1")
rc.predict_getrandbits(32)

try:
    while "guess" in (returned_data := p.recvline().decode("utf-8")):
        predicted_number = rc.predict_getrandbits(32)
        log.info(f"Sending predicted number: {predicted_number}")
        p.sendline(str(predicted_number).encode("utf-8"))
except EOFError:
    print(returned_data)
