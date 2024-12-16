#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

MIN_BLOCKSIZE = 16

@dataclass
class Block:
    start: int
    end: int
    char: bytes

    @property
    def length(self):
        return self.end - self.start

blocks: List[Block] = []
last_byte = b"\0"
counter = 0
index = 0
block_start = 0

with open("PB.img", "rb") as f:
    while b := f.read(1):
        if b == last_byte:
            counter += 1
        else:
            if counter >= MIN_BLOCKSIZE:
                block = Block(block_start, index, last_byte)
                print(f"Block at 0x{block.start:x}-0x{block.end:x}, size = 0x{block.length:x}, char = {repr(block.char)}")
                blocks.append(block)
            counter = 0

        if counter == MIN_BLOCKSIZE:
            block_start = index - MIN_BLOCKSIZE

        last_byte = b
        index += 1

blocks.sort(key=lambda block: block.length, reverse=True)

print("cratectf{", end="")
for block in blocks:
    print(block.char.decode("utf-8"), end="")
print("}")
