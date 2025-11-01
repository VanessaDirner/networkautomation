from ping3 import ping, verbose_ping
from ipaddress import IPv4Network, ip_network
from netmiko import ConnectHandler
from getpass import getpass

print("import getadapters")
import getadapters
print("Import getdevices")
import getdevices
print("import connecttodevice")
import connecttodevice
print("import savetemplates")
import savetemplates



print("starting third part to create templates... ")
updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15']
result = savetemplates.saving(updevices)
print("starting fourth part to get templates")
a = connecttodevice.gettemplates()
print("starting fifth part to connect to devices")
b = connecttodevice.connecting(updevices)
print("Done last module")


exit()
print("starting first module to get network adapters...")
ip_address_combined = getadapters.adapterdetails()
print("starting second module to get IP addreseses")
updevices = getdevices.getallIPs(ip_address_combined)
