from pymodbus.server import StartAsyncTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import threading

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


special_display_id = 0x1f
matrices = {
    0x02: "EDDIE LEVER!",
    0x04: "Spola kröken",
    0x05: "Tuta om du gillar min bil",
    0x09: "Fkk Cancer",
    0x0d: "HELP! MOM FARTED AND WE CANT GET OUT!",
    0x13: "Full gas sparar tid!",
    0x19: "TotemPolarna",
    0x1c: "King Of The Road",
    special_display_id: "cratectf{vilken_forsakring_tacker_egentligen_detta}",
    0x29: "Touch and die!"
}

# global dict for all slaves
slaves = {}

injector_id = 0x33

SPEED_CHANGE_TIMEOUT = 10
DEFAULT_MAX_SPEED = 30
MAX_SPEED_ADDRESS = 0xb + 1    # internal addressing starts from 0


class InjectorBridgeBlock(ModbusSparseDataBlock):
    def __init__(self, values):
        super().__init__(values)
        self.timer = None
        self.inited = False

    @property
    def max_speed(self):
        return self.getValues(MAX_SPEED_ADDRESS)[0]

    def setValues(self, address, values, use_as_default=False):
        if not self.inited:
            self.setValuesInternal(address, values)
            self.inited = True
            return
        current_max_speed = self.max_speed
        self.setValuesInternal(address, values)
        log.info(f"set {values} to {address}")
        log.debug(f"current max: {current_max_speed}         max: {self.max_speed}")
        if current_max_speed != self.max_speed:
            # max speed changed, update timer
            if self.timer:
                self.timer.cancel()
            self.timer = threading.Timer(SPEED_CHANGE_TIMEOUT, self.speedChangeTimeout)
            self.timer.start()
            log.info(f"{SPEED_CHANGE_TIMEOUT} second timer started!")

    def setValuesInternal(self, address, values):
        # log.(f"internal set {address} to {values}")
        super(InjectorBridgeBlock, self).setValues(address, values)

    def speedChangeTimeout(self):
        log.info("timer triggered, reseting max speed")
        self.setValuesInternal(MAX_SPEED_ADDRESS, [DEFAULT_MAX_SPEED])


MIN_SPEED_FOR_DISPLAY = 90

class SpecialDisplayBlock(ModbusSequentialDataBlock):
    def getValues(self, address, count=1):
        # Get current max speed from the injector bridge
        injector = slaves[injector_id]
        current_max_speed = injector.getValues(3, 0xb, 1)[0]
        if current_max_speed >= MIN_SPEED_FOR_DISPLAY:
            log.info(f"speed ok ({current_max_speed}, showing display")
            vals = super(SpecialDisplayBlock, self).getValues(address, count)
            return vals
        else:
            log.info(f"speed too low ({current_max_speed}), returning zeroes")
            vals = [0 for _ in range(count)]
            return vals


async def run_async_server():
    for slave_id, msg in matrices.items():
        display = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*40),
            co=ModbusSequentialDataBlock(0, [0]*12),
            hr=ModbusSequentialDataBlock(0, [0]*800),
            ir=ModbusSequentialDataBlock(0, [0]*800) if slave_id != special_display_id else SpecialDisplayBlock(0, [0]*800))
        slaves[slave_id] = display
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
        display.setValues(4, 0, [height, width])
        display.setValues(4, 240, list(ba))

    injector_bridge = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0] * 40),
        co=ModbusSequentialDataBlock(0, [0] * 12),
        hr=InjectorBridgeBlock([0] * 120),
        ir=ModbusSequentialDataBlock(0, [0] * 120))
    slaves[injector_id] = injector_bridge
    injector_bridge.setValues(3, MAX_SPEED_ADDRESS, [DEFAULT_MAX_SPEED])

    context = ModbusServerContext(slaves=slaves, single=False)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'OlleWarez'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://aliexpress.com/'
    identity.ProductName = 'Matrix Multiplexer modded by Olle'
    identity.ModelName = 'AE928.1.haxx'
    identity.MajorMinorRevision = 4

    # TCP Server
    await StartAsyncTcpServer(context, identity=identity, address=("0.0.0.0", 5020))


if __name__ == "__main__":
    asyncio.run(run_async_server(), debug=True)

