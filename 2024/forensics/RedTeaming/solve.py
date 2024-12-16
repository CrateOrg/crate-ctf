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

code_to_button = {hex(v)[2:]: k for k, v in ir_codes.items()}
print(code_to_button)
mess = ''
with open('data.bin', 'rb') as f:
    code = 'foo'
    while code != b'':
        try:
            code = f.read(4)
            mess += code_to_button[code.hex()]
        except:
            continue
    mess = mess[7:-7].split("mute")[0:-1]
    print(mess)
    flag = ''.join(list(map(lambda c: chr(int(c)), mess)))
    print(flag)