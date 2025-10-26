import os
from ping3 import ping, verbose_ping
import ifaddr
import ipaddress
from ipaddress import IPv4Network, ip_network
import time
import json
import scapy


'''
## get all adapters
adapters = ifaddr.get_adapters()

## print details nicely
for adapter in adapters:
    print(adapter.nice_name) 
    for ip in adapter.ips:
        print(ip.ip)
        print(ip.network_prefix)
        print(ip.nice_name)


valid = False
tries = 0
## double check their answer to see if we can select an interface based on it
while tries < 3 and valid == False:
    try:
        print("choose an adapter to check devices on")
        adpt_choice = int(input())
        print("You chose ", adpt_choice)
        if adpt_choice > 0 and adpt_choice <= len(adapters):
            print("Will now attempt to enumerate network devices for ", adapters[adpt_choice].nice_name)
            print("the details of that adapter are: ")
            print(adapters[adpt_choice].ips[0].ip)
            print(adapters[adpt_choice].ips[0].network_prefix)
            print(adapters[adpt_choice].ips[0].nice_name)
            valid = True
        else:
            tries = tries + 1
            print("Sorry, that was outside the range of interfaces you have. Please double check the given list.", tries)

    except:
        tries = tries + 1
        print("Sorry that was not a number. ", tries)



'''
## get ip details of the interface




## ping all addresses in space
#for address in addresses:
#        print(address)
#        time.sleep(15)
  


range = ip_network('192.168.7.0/24')

addresses = list(range.hosts())
print(addresses[0])

for address in addresses:
    print(address)
    print(type(address))
    
print("pinging")

a = ping('192.168.7.11')

print(a)

exit()
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


'''
print(type(adapters))
print(adapters[2])
print(adapters[2].ips)
print(adapters[2].ips[0])
print(adapters[2].ips[0].ip)
print(adapters[2].ips[0].network_prefix)
print(adapters[2].ips[0].nice_name)
while tries < 3 and valid == False:
    try:
        print("which network on that adapter would you like to choose?")
        print("your options are ", adapters[adpt_choice])
        print("Enter a number between ", len(adapters[adpt_choice]))
        input_net = input()
        if input_net > -1 and input_net <= len(adapters[adpt_choice].ips):
            print("you selected", adapters[adpt_choice].ips[input_net])
        valid = True
    except:
        print("Sorry that's not a valid network adapter")
        

'''