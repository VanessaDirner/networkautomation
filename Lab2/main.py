import os
from ping3 import ping, verbose_ping
import ifaddr
import ipaddress
from ipaddress import IPv4Network, ip_network
import time
import json
import scapy

## get all adapters
adapters = ifaddr.get_adapters()
print(adapters)
print(type(adapters))
print(adapters[2])
print(adapters[2].ips)
print(adapters[2].ips[0])
print(adapters[2].ips[0].ip)
print(adapters[2].ips[0].network_prefix)
print(adapters[2].ips[0].nice_name)
exit()
## send to dictionaries to choose from later
adapters_dict = {}
ips_dict = {}
slash_dict = {}
full_dictionary = {}
adapter_details_dict = {}

adptcount = int(0)
ipcount = int(0)
fullcount = int(0)
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
        full_dictionary = {adapter.nice_name : {{ipcount : ip.ip}, {ipcount :ip.network_prefix}}}
        fullcount = fullcount + 1
        adapter_details_dict.update({fullcount : full_dictionary})
        print(full_dictionary)
      

print("Printing completed dict: \n")
print(adapter_details_dict)

for x, obj in adapter_details_dict.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])





valid = False
tries = 0
## double check their answer to see if we can select an interface based on it
while tries < 3 and valid == False:
    try:
        print("choose an adapter to check devices on")
        adpt_choice = int(input())
        print("You chose ", adpt_choice)
        if adpt_choice > 0 and adpt_choice <= len(adapter_details_dict):
            print("Will now attempt to enumerate network devices for ", adapter_details_dict.get(adpt_choice))
            valid = True
        else:
            print("Sorry, that was outside the range of interfaces you have. Please double check the given list.")
            tries = tries + 1
    except:
        print("Sorry that was not a number. ")
        tries = tries + 1



## get ip details of the interface


print(adapter_details_dict.get(adpt_choice))



exit()

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



print("pinging")

a = ping('192.168.7.11')

b = ping('192.168.7.12')

c = ping('192.168.7.13')

d = ping('192.168.7.15')

print(a,b,c,d)

exit()
