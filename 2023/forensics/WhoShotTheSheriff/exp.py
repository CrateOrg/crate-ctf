#!/usr/bin/env python3

import hashlib
import zipfile

with open("WhoShotTheSheriff.txt", "r", encoding="utf-8") as f:
    target_hash = f.read().strip()

with zipfile.ZipFile("mugshots.zip", "r") as mugshots:
    for filename in mugshots.namelist():
        with mugshots.open(filename, "r") as f:
            f.seek(41 * 512)
            data = f.read(512)
            if hashlib.sha1(data, usedforsecurity=False).hexdigest() == target_hash:
                print(f"cratectf{{{filename}}}")
