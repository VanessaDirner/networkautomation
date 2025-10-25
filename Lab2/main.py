import os
from ping3 import ping
import ifaddr

## get all adapters
adapters = ifaddr.get_adapters()

## send to dictionaries to choose from later
adapters_dict = {}
ips_dict = {}
slash_dict = {}

adptcount = int(0)
ipcount = int(0)

#adapters_dict.update({count : adapter.nice_name})
#        ips_dict.update({count : ip.ip}, {count: ip.network_prefix})
#    print("ips of network adapter", adapter.nice_name)
#        print(ip.ip, ip.network_prefix)

## print out adapter details and format it so we can get an answer and select one
for adapter in adapters:
    adptcount = adptcount + 1
    ipcount = 0 ## reset
    adapters_dict[adptcount] = adapter.nice_name
    for ip in adapter.ips:
        ipcount = ipcount + 1
        ips_dict[adptcount, ipcount, "ip"] = ip.ip
        slash_dict[adptcount, ipcount, "slash"] = ip.network_prefix


print(adapters_dict)
print(ips_dict)

print("choose an adapter to check devices on")
exit()
adpt_choice = int(input())
print("You chose 2")

## double check their answer to see if we can select an interface based on it
try:
    if adpt_choice >= 0 and adpt_choice <= count:
        print("Will now attempt to enumerate network devices")
    else:
        print("Sorry, that was outside the range of interfaces you have. Please double check the given list.")
except:
    print("Sorry that was not a number. ")

## get ip details of the interface


'''
try:
    pings = ping('10.1.1.1')
    print("pinging", pings)
except:
    print("unknown error")

    '''