## Connect to 1 or all devices, push configuration
from ipaddress import IPv4Network, ip_network
from netmiko import ConnectHandler
from getpass import getpass

print("importing connectandrun")
import connectandrun
print("Importing getdevices")
import getdevices

### get templates, create association between IPs and their template

## generate correlation between Ips and templates
updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14']
number_of_devices = 6
IPs_and_templates = {}
counter = 0

for device in updevices:
    filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\{updevices[counter]}.json"
    IPs_and_templates.update({device: filename})
    counter = counter + 1


## keeping asking until they pick an option
quit = False
choice_selected = False
device_selected = False
get_devices = False
get_addresses = False


while (choice_selected == False) and (quit == False):
    print("What action would you like to complete? " \
    "Your options are: 0 - Push Configuration to Device : 1 - Save Running Configuration. 2 - Scan Network for devices" \
    " You can quit with -1")

    ## we are keeping track of which option they picked with outoption
    outoption = int()

    try:
        outoption = input()
        if outoption == '0':            
            print("You selected 0 succesfully.")
            action = outoption
            get_devices = True
            choice_selected = True
        elif outoption == '1':
            print("You selected 1 succesfully.")
            action = outoption
            choice_selected = True
            get_devices = True
        elif outoption == '2':
            print("You selected 2 succesfully.")
            action = outoption
            choice_selected = True
            get_addresses = True
        elif outoption == '-1':
            print("quitting")
            quit = True
            quit()
        else:
            print("Sorry, was looking for -1, 0, 1, 2 for selecting a cisco device output")
    except Exception as e:
        print("Ran into an issue: ", e)


all = int(number_of_devices + 1)

quit = False
index = int(0) 

# print("did we make it here - 1")

if (quit == False) and (get_addresses == True):
    print("Starting scan.")    
    # Scan the network to look for new network devices.
    getdevices.getallIPs('192.168.7.0/24')

# print("did we make it here - 2")print("choice selected = ", choice_selected, "get_devices = ", get_devices, "deviceselected = ", device_selected)
while (choice_selected == True) and (quit == False) and (get_devices == True) and (device_selected == False):
    ##Prompt a User to input an IP Address for a Network Device in the Rack
    print("Which device would you like to connect to. To select an individual device, your options are any of these files. ")
    ## for each template, print template and it's count
    ips = IPs_and_templates.keys()
    optionsindextoIPs = {}
    for ip in ips:
        print("Option", index, "is", ip)
        optionsindextoIPs.update({index : ip})
        index = index + 1
    print("Items list", optionsindextoIPs.items())
    print("To select all devices, enter", all)
    print("Enter the appropriate number for the device you'd like to select")
    print("Enter -1 to quit.")
    devicechoice = int(input())
    ##Validate the IP Address entered works for your Rack or series of devices
    try:
        ## quit value
        if (devicechoice == -1):
            print("You entered: ", devicechoice, ", to quit, succesfully")
            print("quit entered, quitting.")
            quit = True
            exit()
        elif(devicechoice == all):
            print("You selected all. Preparing devices")
            device_selected = True
        elif(devicechoice > -1 and devicechoice <= len(optionsindextoIPs)):
            print("Device choice was ", devicechoice)
            selectedip = optionsindextoIPs.get(devicechoice)
            print("Selected ip is " , selectedip)
            print("selected device is", IPs_and_templates.get(selectedip))
            device_selected = True
        else:
                device_selected = False
                print("Failed to get template based on IP. Please double check your entry")
            # print("You didn't select one of the options. Enter an option between 1 and ", len(Ips_and_templates) , "Try again")
    except Exception as e:
        print("Failed to get details about device choice.")
        print(e)
        print("Enter -1 to quit now. Enter anything else to continue")
        leave = input()
        if leave == '-1':
            print("-1 was entered, quitting.")
            exit()
        print("Continuing.")   
        failed = False


## put a blocker on this to make sure it's not run for scan, must have selected a choice and device
if (choice_selected == True) and (quit == False) and (get_devices == True) and (device_selected == True):
    ## if choice is all, for each IP acting as a key for my templates, + action
    if devicechoice == all:
        for ip in IPs_and_templates:
            print(action, ip, IPs_and_templates.get(ip))
            connectandrun.runaction(action, ip, IPs_and_templates.get(ip))
    ## otherwise, send the individual IP key along with template, + action
    else:
        print("action is", action, "ip is", selectedip, "template is", IPs_and_templates.get(selectedip))
        connectandrun.runaction(action, selectedip, IPs_and_templates.get(selectedip))