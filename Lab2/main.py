import os
from ping3 import ping
import ifaddr

adapters = ifaddr.get_adapters()

for adapter in adapters:
    print("ips of network adapter", adapter.nice_name)
    for ip in adapter.ips:
        print(ip.ip, ip.network_prefix)

print("why isn't this printing")

try:
    pings = ping('10.1.1.1')
    print("pinging", pings)
except:
    print("unknown error")