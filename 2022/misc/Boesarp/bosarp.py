# Bôs-arp challenge pcap creator :D

from scapy.all import *

hw_broadcast = "ff:ff:ff:ff:ff:ff"
hw_src = "42:d6:53:41:52:50"
hw_replies = [
        "40:40:40:63:72:61",
        "74:65:63:74:66:7b",
        "66:72:61:6e:7a:24",
        "74:68:65:24:63:69",
        "72:63:75:6c:61:72",
        "24:68:65:72:6f:7d"
]

q_ip = "8.8.8.8"
d_ip = "55.41.13.26"

# Send the ARP broadcast
a = ARP(pdst=q_ip, psrc=d_ip, hwsrc=hw_src) 
e = Ether(dst=hw_broadcast, src=hw_src)

sendp(e/a)

import time
for responder in hw_replies:
    time.sleep(7)
    e = Ether(dst=hw_src, src=responder)
    a = ARP(op=2, pdst=d_ip, psrc=q_ip, hwdst=hw_src, hwsrc=responder)
    sendp(e/a)


