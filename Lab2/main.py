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


## get all adapters
adapters = ifaddr.get_adapters()
count = int(0)
count2 = int(0)

## print details nicely
for adapter in adapters:
    print("\n")
    count = count + 1
    count2 = 0
    print("Adapter '", adapter.nice_name, "' number", count, "has the following networks associated with it:")
    for ip in adapter.ips:
        count2 = count2 + 1
        print( ip.nice_name, "with IP address of ", ip.ip, "/", ip.network_prefix, "for network number", count2, "of adapter number", count)


exit()

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
        
            ## Read details of show interface brief
    try:
        with open("./showipconfig.txt") as file:
            ## parse the file
            ## separate out the lines
            ## read specific parts of lines
            ## skip the first line and assign each line the name of the first string in the line "vlan1"
            
            ## https://www.youtube.com/watch?v=ZLCZkMk69y0 how to read a line
        
            lines = file.readlines()
            file.close

    except:
        print("failed to read file. Please check if the showipconfix.txt file is in the Lab1pythonfolder. If it is, change your running directory to Lab1pythonfolder. Thanks! :)")
        return False
    else:
        print("Read of file succesful.")
  
    ipconfigArray = []
    total_lines = len(lines)
    ## append to an easier to handle data object to read to later
    for line in lines:
        print(line)
        ipconfigArray.append(line)

            ## Tell the user the details of the saved configuration
    print("your final configuration details are: \n",
          fullconfiguration)
    
    ## save all details to a file
    filename = "CiscoRouterConfig.txt"

    print("saving configuration to ", filename)

    ## overwrite existing content - we don't need more than 1 set of config
    with open(filename, "w") as f:
        f.write(fullconfiguration)
'''

