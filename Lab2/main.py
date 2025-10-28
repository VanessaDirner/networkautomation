import os
from ping3 import ping, verbose_ping
import ifaddr
import ipaddress
from ipaddress import IPv4Network, ip_network
import time
import json
import scapy
import threading
import concurrent.futures
import subprocess
import nmap
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
            chosen_ip = adapters[adpt_choice].ips[0].ip
            chosen_prefix = adapters[adpt_choice].ips[0].network_prefix
            valid = True
        else:
            tries = tries + 1
            print("Sorry, that was outside the range of interfaces you have. Please double check the given list.", tries)

    except:
        tries = tries + 1
        print("Sorry that was not a number. ", tries)



## get ip details of the interface

## have address, format it
ip_address_combined = f"{chosen_ip}/{chosen_prefix}"
print(ip_address_combined)
print(type(ip_address_combined))
interface_ip_address = ipaddress.IPv4Address(chosen_ip)
print(interface_ip_address)
## get network address from ip address


range = ip_network(ip_address_combined, strict=False)
print(range)

## ping all addresses in space
##range = ip_network('192.168.7.0/24')
## turn network subnet into a actual list of the range
addresses = list(range.hosts())

## access a specific ip
print(addresses[0])

updevices = []
'''
nm = nmap.PortScanner()

#https://xael.org/pages/python-nmap-en.html
nm.scan(hosts='192.168.7.0/24')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print("scanning")
    print('{0}:{1}'.format(host, status))
    print("Sending to list")

exit()
nm.all_hosts()


for address in addresses:
    print("scanning", address)
    nm.scan(str(address))



exit()
## iterate, print IPs
for address in addresses:
    print(address)
    print(type(address))
    stringip = str(address)
    print(stringip)
    result = verbose_ping(stringip)
    
    ## add pingable devices to list
    if result != True:
        print("No device found at", stringip)
    elif result == False:
        print("Device found at ", stringip)
        updevices.append(stringip)



print("pinging")

a = ping(stringip)

print(a)

exit()


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