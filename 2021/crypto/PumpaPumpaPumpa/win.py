import pwn
import subprocess

p = pwn.remote("localhost", 13411)
p.readline()
p.readline()
pingline = p.readline().decode("ascii").strip()
sig = pingline.split("=")[1]
cmd = f"hashpump -s {sig} --data 'ping' -a 'print_flag' -k 64"
output = subprocess.check_output(cmd, shell=True).decode("ascii")
forged_signature = output.split("\n")[0]
forged_data = output.split("\n")[1]
forged_data = eval(f"b\"{forged_data}\"") + b"\n"

p.send_raw(forged_data)
p.sendline(forged_signature)

p.interactive()
