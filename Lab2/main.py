import os
from ping3 import ping
import ifaddr

## get all adapters
adapters = ifaddr.get_adapters()

## send to dictionary to choose from later
adapters_dict = {}
count = int(0)
print(type(count))

for adapter in adapters:
    print("ips of network adapter", adapter.nice_name)
    count = count + 1
    adapters_dict.update({count : adapter.nice_name})
    for ip in adapter.ips:
        print(ip.ip, ip.network_prefix)


print(adapters_dict)


print("choose an adapter to check devices on")

adpt_choice = int(input())
print("You chose 2")

try:
    if adpt_choice >= 0 and adpt_choice <= count:
        print("Will now attempt to enumerate network devices")
    else:
        print("Sorry, that was outside the range of interfaces you have. Please double check the given list.")
except:
    print("Sorry that was not a number. ")

'''
try:
    pings = ping('10.1.1.1')
    print("pinging", pings)
except:
    print("unknown error")

    '''