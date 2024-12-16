import re

import gdb

gdb.execute("set sysroot libs")
gdb.execute("core-file check_flag_format.core")

backtrace = gdb.execute("bt", to_string=True)

frames = []

for frame in re.finditer(r"#(\d+).*in (.+) .*", backtrace):
    frame_no, function = frame.group(1, 2)
    if function == "F":
        frames.insert(0, int(frame_no))

flag = ""

for frame in sorted(frames, reverse=True):
    gdb.execute(f"frame {frame}")
    var_value = gdb.execute("x/c $rbp-4", to_string=True)
    if value := re.search(r"'(.+)'", var_value):
        flag += value.group(1)

print(f"cratectf{{{flag}")
