import random
import subprocess
  
flag_file = "flagga.txt"
current_number = str(random.randint(0,9999)).zfill(4)
zip_file_name = current_number + ".zip"
create_zip_command = f"zip {zip_file_name} {flag_file}"
subprocess.call(create_zip_command, shell=True)

for _ in range(222):
    next_number = str(random.randint(0,9999)).zfill(4)
    create_zip_command = f"zip -P {current_number} {next_number}.zip {current_number}.zip"
    subprocess.call(create_zip_command, shell=True)

    remove_previous_zip = f"rm {current_number}.zip"
    subprocess.call(remove_previous_zip, shell=True)

    current_number = next_number

