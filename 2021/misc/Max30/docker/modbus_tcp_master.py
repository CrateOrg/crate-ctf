from pymodbus.server import StartAsyncTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

import asyncio

import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def char_to_pixels(text, path='arialbd.ttf', fontsize=14):
    """
    Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
    """
    font = ImageFont.truetype(path, fontsize)
    dummy1, dummy2, w, h = font.getbbox(text)
    h *= 2
    image = Image.new('L', (w, h), 1)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)
    arr = np.asarray(image)
    arr = np.where(arr, 0, 1)
    arr = arr[(arr != 0).any(axis=1)]
    return arr


matrices = {
    0x02: "EDDIE LEVER!",
    0x04: "Spola kröken",
    0x05: "Tuta om du gillar min bil",
    0x09: "Fkk Cancer",
    0x0d: "HELP! MOM FARTED AND WE CANT GET OUT!",
    0x13: "Full gas sparar tid!",
    0x19: "cratectf{dotmatrix_modbus_atraktorhaxx}",
    0x1c: "King Of The Road",
    0x1f: "MAMMA BETALAR :)",
    0x29: "Touch and die!"
}

async def run_async_server():
    slaves = {}
    for slave_id, msg in matrices.items():
        slave = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*40),
            co=ModbusSequentialDataBlock(0, [0]*12),
            hr=ModbusSequentialDataBlock(0, [0]*800),
            ir=ModbusSequentialDataBlock(0, [0]*800))
        slaves[slave_id] = slave
        # bit-array!
        arr = char_to_pixels(msg, "6x12-ISO8859-1.pcf.gz", fontsize=12)
        # pixel dimensions
        height, width = arr.shape
        # byte-array!
        ba = np.packbits(arr)
        # input register 0 = height
        # input register 1 = width
        # total pixels = height*width, bytes = pixels/8
        # data starts at register 240
        slave.setValues(4, 0, [height, width])
        slave.setValues(4, 240, list(ba))

    context = ModbusServerContext(slaves=slaves, single=False)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'AliExpress'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://aliexpress.com/'
    identity.ProductName = 'Matrix Multiplexer'
    identity.ModelName = 'AE928.1'
    identity.MajorMinorRevision = 4

    # TCP Server
    await StartAsyncTcpServer(context, identity=identity, address=("0.0.0.0", 5020))


if __name__ == "__main__":
    asyncio.run(run_async_server(), debug=True)

