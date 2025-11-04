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

'''
print("starting first module to get network adapters...")
ip_address_combined = getadapters.adapterdetails()
print("starting second module to get IP addreseses")
updevices = getdevices.getallIPs(ip_address_combined)
'''

### get templates, create association between IPs and their template

## testing only
updevices = ['192.168.7.1', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.2', '192.168.7.3']
print("starting save templates")
print("starting third part to create templates... ")
Ips_and_templates  = savetemplates.saving(updevices)



#Prompt user to save the following information to appropriately named files
#Reload device
#Running configuration file (show running-config)

## keeping asking until they pick an option
quit = False
choice_selected = False

while (choice_selected == False) and (quit == False):
    print("What action would you like to complete? " \
    "Your options are: 0 - Reload Device : 1 - Show Running Configuration. You can quit with -1")
    ## we are keeping track of which option they picked with outoption
    outoption = int()

    try:
        outoption = input()
        if outoption == '0':            
            print("You selected 0 succesfully.")
            action = outoption
            choice_selected = True
        elif outoption == '1':
            print("You selected 1 succesfully.")
            action = outoption
            choice_selected = True
        elif outoption == '-1':
            print("quitting")
            quit = True
            quit()
        else:
            print("Sorry, was looking for -1, 0 or 1 for selecting a cisco device output")
    except Exception as e:
        print("Ran into an issue: ", e)


all = len(Ips_and_templates) + 1

quit = False
choice_selected = False
index = int(0) 

while (choice_selected == False) and (quit == False):
    ##Prompt a User to input an IP Address for a Network Device in the Rack
    print("Which device would you like to connect to. To select an individual device, your options are any of these files. ")
    ## for each template, print template and it's count
    ips = Ips_and_templates.keys()
    for ip in ips:
        print("Option", index, "is", ip)
        index = index + 1
    print("To select all devices, enter", all)
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
        elif(devicechoice >= 0 and devicechoice <= len(Ips_and_templates)):
            print("You selected ", devicechoice)
            print("loading configuration..", Ips_and_templates.get(ip), "succesfully")
            selected_template = Ips_and_templates.get(ip)
            choice_selected = True
        elif(devicechoice == all):
            print("You selected all. Preparing devices")
            choice_selected = True
        else:
            print("You didn't select one of the options. Enter an option between 1 and ", len(Ips_and_templates) , "Try again")
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


## if choice is all, for each IP acting as a key for my templates, + action
if devicechoice == all:
    for ip in Ips_and_templates:
        print(action, ip, Ips_and_templates.get(ip))
        connecttodevice.runaction(action, ip, Ips_and_templates.get(ip))
## otherwise, send the individual IP key along with template, + action
else:
    print(action, ip, Ips_and_templates.get(ip))
    connecttodevice.runaction(action, ip, Ips_and_templates.get(ip))





exit()


# get device choice (x)
# get action choice (y)

## if device choice is 1 of them
## run action + connect using x+y

## if device choice all
## foreach device
# ## run action + connect using x+y