from zipfile import ZipFile
import os

filename = "6007.zip"

while True:
    oldname = filename
    with ZipFile(filename, "r") as z:
        filename = z.namelist()[0]
        password = filename[:-4]
        z.extractall(pwd=bytes(password, "ascii"))
        print(filename, password)
        z.close()
    os.remove(oldname)
