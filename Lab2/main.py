import os
from ping3 import ping, verbose_ping
import ifaddr
import ipaddress
from ipaddress import IPv4Network, ip_network
import time
import json

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

range = ip_network('192.168.7.0/24')

addresses = list(range.hosts())
print(addresses)


## ping all addresses in space
#for address in addresses:
#        print(address)
#        time.sleep(15)

for addr in IPv4Network('192.168.7.0/24'):
    ip = print(addr)
    ping(ip)


ip = ipaddress.IPv4Address('192.168.1.1')
print(ip - 1)

#ip_list = [str(ip) for ip in IPv4Network('192.168.8.0/24')]
#print(ip_list[:5])