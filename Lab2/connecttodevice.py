from netmiko import ConnectHandler
from getpass import getpass
import os
import json

def gettemplates(updevices):
    
    ciscotemplates = []

    files = os.listdir("./templates")
    print(files)
    counter = 0

    ## get all templates
    for file in files:
        print("file is ",file)
        filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\{file}"
        print("filename is ", filename)
        f = open(filename)
        data = json.load(f)
        ciscotemplates.append(data)
        print(ciscotemplates[counter])
        counter = counter + 1

    print("HIIIIIII")

    return ciscotemplates



def choice(updevices):
    ciscotemplates = gettemplates(updevices)
    print("Started connecting module...")
    ## temp for testing
    ##updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.140']

    all = len(updevices) + 1

    ##Prompt a User to input an IP Address for a Network Device in the Rack
    print("Which device would you like to connect to. To select an individual device, your options are between 0 and ", len(updevices))
    print("To select all devices, enter", all)
    print("Enter -1 to quit.")

    devicechoice = int(input())
    ##Validate the IP Address entered works for your Rack or series of devices
    try:
        ## quit value
        if (devicechoice == "-1"):
            print("You entered: ", devicechoice , ", to quit, succesfully")
            print("quit entered, quitting.")
            quit = True
            exit()
        elif(devicechoice >= 0 and devicechoice <= len(updevices)):
            print("You selected ", devicechoice)
            print("loading configuration..", updevices[devicechoice], "succesfully")
        elif(devicechoice == all):
            print("You selected all. Preparing devices")
        else:
            print("You didn't select one of the options. Enter an option between 1 and ", len(updevices) , "Try again")
    except Exception as e:
        print("Failed to get details about device choice.")
        print(e)
    
        print("Enter -1 to quit now. Enter anything else to continue")
        leave = input()
        if leave == '-1':
            print("-1 was entered, quitting.")
            quit = True
            exit()
        print("Continuing.")   
        failed = False
    return False

def connecting(updevice):
    # selected_template = ciscotemplates[countdevice]
    tmp_template = {
    "device_type": "cisco_ios",
    "host": "192.168.7.14",
    "username": "cisco",
    "password": "cisco"
                    }

    debug_a = net_connect = ConnectHandler(**tmp_template)
    print(debug_a)

    try:
        net_connect.enable() 
        print(net_connect.find_prompt())
    except:
        print("device did not connect, moving on.")

    countdevice = 0
    if devicechoice == all:
        for device in updevices:
            print("todo")
            countdevice = countdevice + 1


updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.140', '192.168.7.1', '192.168.7.101', '192.168.7.110', '192.168.7.140']
 
connecting(updevices)


'''
            if failed == False:
                print("displayed basic device information above succesfully. What other details would you like to see? " \
                "Your options are: 0 - Show Running Configuration : 1 - Reload Device" \
                "Enter 0 or 1 as your option. You can enter -1 to quit.")
                

                #Prompt user to save the following information to appropriately named files
                #Reload device
                #Running configuration file (show running-config)
                outoption = input()

                try:
                    if outoption == '0':            
                        print("You selected 0 succesfully.")
                        #print(ipintbr)
                        #print("Printed details succesfully.")
                        try:
                            ipintbr = net_connect.send_command('show running-config')
                            print("Now saving running configuration to a file")
                            with open("ipintbr.txt", "w") as f:
                                f.write(ipintbr)
                        except:
                            print("Failed to print to file")

                    elif outoption == '1':
                        print("You selected 1 succesfully.")
                        runconf = net_connect.send_command('show running-config')
                        print(runconf)
                        print("Printed details succesfully.")
                        try:
                            print("now saving runconf to a file")
                            with open("runconf.txt", "w") as f:
                                f.write(runconf)
                        except:
                            print("Failed to print to file")

                    elif outoption == '-1':
                        print("quitting")
                        exit()
                    else:
                        print("Sorry, was looking for -1, 0 or 1 for selecting a cisco device output")
                except:
                    print("Failed to read input.")


                net_connect.disconnect()

'''


    
