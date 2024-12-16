#!/usr/bin/env python3

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import sys
# your gen-py dir
sys.path.append('docker/gen-py')

import time

# Example files
from description import *
from description.ttypes import *


transport = TSocket.TSocket("localhost", 13313)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = FlagGetter.Client(protocol)

transport.open()

key = client.get_key()
flag = client.get_flag(key)
print(flag)

transport.close()
