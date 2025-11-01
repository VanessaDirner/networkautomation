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


updevices = ['192.168.7.1.json', '192.168.7.101.json', '192.168.7.11.json', '192.168.7.110.json', '192.168.7.12.json', '192.168.7.13.json', '192.168.7.14.json', '192.168.7.140.json', '192.168.7.15.json', '192.168.7.2.json', '192.168.7.3.json']
print("starting fourth part to get templates")
a = connecttodevice.gettemplates()
print("starting fifth part to select action")
b = connecttodevice.action()
print("get device choice")
devicechoice, ciscotemplates = connecttodevice.devicechoice(updevices)
print("sending device choice to get connected...")
connecttodevice.connecting()
print("now actioning on connection...")
connecttodevice.runaction(devices)
exit()

print("starting first module to get network adapters...")
ip_address_combined = getadapters.adapterdetails()
print("starting second module to get IP addreseses")
updevices = getdevices.getallIPs(ip_address_combined)
print("starting third part to create templates... ")
result = savetemplates.saving(updevices)