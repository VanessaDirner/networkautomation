from ping3 import ping, verbose_ping
import ping3
from ipaddress import IPv4Network, ip_network
from netmiko import ConnectHandler
from getpass import getpass

def getallIPs(ip_address_combined):

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

