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


print("starting")
ip_address_combined = getadapters.adapterdetails()
print("done first module", ip_address_combined)
updevices = getdevices.getallIPs(ip_address_combined)
print("done second module, onto next...", updevices)
# ##updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.140', '192.168.7.1', '192.168.7.101', '192.168.7.110', '192.168.7.140']
result = savetemplates.saving(updevices)
# print(result)
a = connecttodevice.gettemplates(updevices)
# print(a)
b = connecttodevice.connecting(updevices)
# print("Done last module", b)

