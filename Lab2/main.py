import os
from ping3 import ping
import ifaddr

## get all adapters
adapters = ifaddr.get_adapters()

## send to dictionary to choose from later
adapters_dict = {}
count = 0

for adapter in adapters:
    print("ips of network adapter", adapter.nice_name)
    count = count + 1
    adapters_dict.update({count : adapter.nice_name})
    for ip in adapter.ips:
        print(ip.ip, ip.network_prefix)


print(adapters_dict)

'''
print("choose an adapter to check devices on")

adpt_choice = input()




try:
    pings = ping('10.1.1.1')
    print("pinging", pings)
except:
    print("unknown error")

    '''