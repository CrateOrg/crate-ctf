#!/usr/bin/env python3

import io
import base64
import pickle
import hashlib
import sys

def check_hash(hashed, plain, all_targets):
    if hashed not in all_targets:
        return False

    sha1 = hashlib.sha1(plain.encode()).hexdigest()
    return sha1 == hashed

def main():
    print("Please enter the cracked passwords on the format [hash]:[plain]. One entry per line! Example:")
    print("f58cf5e7e10f195e21b553096d092c763ed18b0e:asdf1234")
    print("=================================================")

    filename = "hashes"
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    all_targets = []
    with open(filename, "r") as f:
        all_targets = [line.strip() for line in f.readlines()]

    accepted_pairs = set()

    for line in sys.stdin:
        if not line.strip():
            break
        tokens = line.strip().split(":")

        if len(tokens) != 2:
            print(f"\"{line}\" is not on the format [hash]:[plain], skipping")

        hashed = tokens[0].strip()
        plain = tokens[1].strip()
        pair = f"{hashed}:{plain}"

        if check_hash(hashed, plain, all_targets):
            if pair not in accepted_pairs:
                accepted_pairs.add(pair)
            else:
                print(f"You have already sent the line \"{pair}\", skipping")
        else:
            print(f"\"{pair}\" does not appear to be valid... Are you sure that the the plain text hashes to the provided hexstring, and that the hexstring is present in the given file?")

    num_cracked = len(accepted_pairs)
    num_targets = len(all_targets)
    percentage = (num_cracked/num_targets)*100
    print(f"You correctly cracked {num_cracked} out of {num_targets} targets! This corresponds to {percentage}%")
    if percentage >= 60:
        print("Amazing! You cracked more than 60% of the hashes! Here is a flag for you:")
        print("cratectf{snyggt_gissat_bra_jobbat}")
    else:
        print("Sadly, you did not crack more than 60% of the given hashes, so you're not getting the flag this time")


if __name__ == "__main__":
    main()

