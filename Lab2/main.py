import os
from ping3 import ping, verbose_ping
import ping3
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
import traceback
from netmiko import ConnectHandler
from getpass import getpass

## get all adapters
adapters = ifaddr.get_adapters()
counter = int(-1)
counter2 = int(-1)

## print details nicely
for adapter in adapters:
    print("\n")
    counter = counter + 1
    print(counter, " - Adapter '", adapter.nice_name, "' number",  "has the following networks associated with it:")
    counter2 = -1
    for ip in adapter.ips:
        counter2 = counter2 + 1
        print(counter, ".", counter2, " Network",  ip.nice_name, "with IP address of ", ip.ip, "/", ip.network_prefix )


valid = False
tries = 0
adpt_choice = int()
net_choice = int()

## double check their answer to see if we can select an interface based on it
while tries < 3 and valid == False:
    try:
        print("choose an adapter to check devices on")
        adpt_choice = int(input())
        print("You chose ", adpt_choice, "which is ", adapters[adpt_choice].nice_name)
        if adpt_choice > -1 and adpt_choice <= len(adapters):
            print("Choose a network on that adapter: ")
            net_choice = int(input())
        else:
            tries = tries + 1
            print("Sorry, that was outside the range of interfaces you have. Please double check the given list. Tries:", tries)

        if net_choice > -1 and net_choice <= len(adapter.ips):
            print("You have selected", adapter.ips[net_choice].nice_name, "on ", adapters[adpt_choice].nice_name)
            print("the details of that adapter are: ")
            print(adapters[adpt_choice].ips[net_choice].ip)
            print(adapters[adpt_choice].ips[net_choice].network_prefix)
            print(adapters[adpt_choice].ips[net_choice].nice_name)
            chosen_ip = adapters[adpt_choice].ips[net_choice].ip
            chosen_prefix = adapters[adpt_choice].ips[net_choice].network_prefix
            valid = True
            print("Will now attempt to enumerate network devices on that network.")
        else:
            print("Sorry that was out of range of networks on that interface.  Tries:", tries)

    except Exception:
        tries = tries + 1
        print(traceback.print_exc())
        print("Sorry that was not a number. ", tries)


## get ip details of the interface

## have address, format it
ip_address_combined = f"{chosen_ip}/{chosen_prefix}"
print(ip_address_combined)
print(type(ip_address_combined))

try:
    interface_ip_address = ipaddress.IPv4Address(chosen_ip)
except:
    print("Sorry, it's likely you picked a non valid IP address range to ping from an adapter. Exiting...")
    exit()

if interface_ip_address.is_loopback:
    print("Sorry this is a loopback address. Cannot ping. Exiting...")
    exit()
elif interface_ip_address.is_unspecified:
    print("Sorry this is an unspecified address. Exiting...")
    exit()
elif interface_ip_address.is_link_local:
    print("Sorry this is a link local address. Exiting...")
    exit()
elif interface_ip_address in ipaddress.ip_network("169.254.0.0/16"):
    print("Sorry you picked an apipa address. Exiting...")
    exit()

print(interface_ip_address)
## get network address from ip address


range = ip_network(ip_address_combined, strict=False)
print(range)

## ping all addresses in space
## for testing only ##range = ip_network('192.168.7.0/24')
## turn network subnet into a actual list of the range
addresses = list(range.hosts())

## access a specific ip
print(addresses[0])

updevices = []

ping3.Exceptions = True
## iterate, print IPs
for address in addresses:
    print(address)
    print(type(address))
    stringip = str(address)
    result = ping(stringip, size=1, timeout=1) ## count=1 not recognized unless verbose
    print("result of ping for ", stringip, "is", result, "with a type of ", type(result))
    ## add pingable devices to list
    if result is None:
        print("No device found at", stringip, "Since output is ", result)
    elif result is False:
       print("Also a fail since output is ", result)
    else:
        print("Device found at ", stringip, "Since output is ", result)
        updevices.append(stringip)
        print('')

print("final list of devices up", updevices)

## temp for testing
updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.140']
##is ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.140']

host_address = updevices[1]

ciscoTemplate = {
    'device_type': 'cisco_ios',
    'host':  host_address,
    'username':'cisco',
    'password':'cisco'
}


'''
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

