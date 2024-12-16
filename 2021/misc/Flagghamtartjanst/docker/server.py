#!/usr/bin/env python3

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import sys
sys.path.append('gen-py')

# Example files
from description import *
from description.ttypes import *

import time

import logging
logging.basicConfig(level=logging.DEBUG)

flag = ""
with open("flag.txt", "r") as f:
    flag = f.readline().strip()

class FlagGetterHandler:
    def get_key(self):
        return "amFnIGRldHRhIMOkciBqdSBlbiBueWNrZWwgaGVsdCBrbGFydCEK"

    def get_flag(self, key):
        if key == "amFnIGRldHRhIMOkciBqdSBlbiBueWNrZWwgaGVsdCBrbGFydCEK":
            return flag
        else:
            return "That's not the right key"


# set handler to our implementation
handler = FlagGetterHandler()

processor = FlagGetter.Processor(handler)
transport = TSocket.TServerSocket("0.0.0.0", 31337)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print("Starting server...")
server.serve()
