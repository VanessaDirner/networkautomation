from ping3 import ping, verbose_ping
from ipaddress import IPv4Network, ip_network
from netmiko import ConnectHandler
from getpass import getpass

import getadapters
import getdevices
##import connecttodevice

print("starting")
ip_address_combined = getadapters.adapterdetails()
print("done first module")
listofIPs = getdevices.getallIPs(ip_address_combined)

#b = connecttodevice