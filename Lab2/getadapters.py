import os
from ping3 import ping, verbose_ping
import ifaddr
import ipaddress
from ipaddress import IPv4Network, ip_network
import traceback
from netmiko import ConnectHandler
from getpass import getpass


def adapterdetails():
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
    else:
        print("completed all validations. Continuing with inputted details...",     interface_ip_address)
    return ip_address_combined
