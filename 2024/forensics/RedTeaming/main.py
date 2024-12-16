flag = "cratectf{infra-redteamingftw}"
ir_codes = {'onoroff': 0xE0E040BF,
            '1': 0xE0E020DF,
            '2': 0xE0E0A05F,
            '3': 0xE0E0609F,
            '4': 0xE0E010EF,
            '5': 0xE0E0906F,
            '6': 0xE0E050AF,
            '7': 0xE0E030CF,
            '8': 0xE0E0B04F,
            '9':  0xE0E0708F,
            '0':  0xE0E08877,
            'mute': 0xE0E0F00F,
            }
crypted = list(map(lambda c: str(ord(c)).zfill(3), flag))
with open('data.bin', 'bw') as f:
    f.write(bytes.fromhex(hex(ir_codes['onoroff'])[2:]))
    for c in crypted:
        for d in c:
            f.write(bytes.fromhex(hex(ir_codes[d])[2:]))

        f.write(bytes.fromhex(hex(ir_codes['mute'])[2:]))
    f.write(bytes.fromhex(hex(ir_codes['onoroff'])[2:]))
print(crypted)
