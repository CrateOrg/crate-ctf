# Requires pymodbus and numpy
import time

from pymodbus.client import ModbusTcpClient as ModbusClient
import numpy as np
import math
import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.INFO)

ALL_UNITS = [ 0x02, 0x04, 0x05, 0x09, 0x0d, 0x13, 0x19, 0x1c, 0x1f, 0x29 ]
INJECTOR_BRIDGE = 0x33
MAX_SPEED_REGISTER = 0xb

def get_matrix_data(slave_id, client):
    print(f"Get pixel dimensions for slave {hex(slave_id)} at input registers 0+1")
    rr = client.read_input_registers(0, 2, slave=slave_id)
    assert(not rr.isError())
    height = rr.registers[0]
    width = rr.registers[1]
    numbytes = int(math.ceil(height * width / 8))
    print(f"Get {height}*{width} = {height*width/8} ({numbytes}) bytes of pixel data at register 240")
    data = []
    bytes_read = 0
    # Make sure to fit in the PDU
    while bytes_read < numbytes:
        bytes_to_read = min(100, numbytes - bytes_read)
        print(f"reading {bytes_to_read} bytes")
        rr = client.read_input_registers(240+bytes_read, bytes_to_read, slave=slave_id)
        assert (not rr.isError())
        data += rr.registers
        bytes_read += bytes_to_read
    bya = np.fromiter(data, dtype=np.uint8)
    bia = np.unpackbits(bya)
    result = np.where(bia, '#', ' ')
    for row in range(height):
        pixels = result[row * width : (row + 1) * width]
        print("".join(pixels))
    client.close()


if __name__ == "__main__":
    client = ModbusClient('kananga', port=42143)
    client.connect()
    print("Reading default displays")
    for slave in ALL_UNITS:
        get_matrix_data(slave, client)
    print("\n...Enabling high-speed display and reading again")
    time.sleep(2)
    client.write_register(MAX_SPEED_REGISTER, 165, slave=INJECTOR_BRIDGE)
    for slave in ALL_UNITS:
        get_matrix_data(slave, client)

