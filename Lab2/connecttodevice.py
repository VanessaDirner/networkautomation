from netmiko import ConnectHandler
from getpass import getpass
import os
import json

def gettemplates():
    
    ciscotemplates = []

    files = os.listdir("./templates")
    print(files)
    counter = 0

    ## get all templates
    for file in files:
        print("file is ",file)
        filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\{file}"
        print("filename is ", filename)
        f = open(filename, 'r')
        data = json.load(f)
        ciscotemplates.append(data)
        print(ciscotemplates[counter])
        counter = counter + 1
        
    return ciscotemplates


#Prompt user to save the following information to appropriately named files
#Reload device
#Running configuration file (show running-config)
def action():
    quit = False
    while quit != True:
        print("What action would you like to complete? " \
        "Your options are: 0 - Reload Device : 1 - Show Running Configuration. You can quit with -1")
        outoption = input()
        try:
            if outoption == '0':            
                print("You selected 0 succesfully.")
                return 0
            elif outoption == '1':
                print("You selected 1 succesfully.")
                return 1
            elif outoption == '-1':
                print("quitting")
                quit = True
                exit()
            else:
                print("Sorry, was looking for -1, 0 or 1 for selecting a cisco device output")
        except:
            print("Failed to read input.")
        print("Looping back to selection menu...")



def devicechoice():
    ciscotemplates = gettemplates()
    print("Started connecting section...")

    all = len(ciscotemplates) + 1

    ##Prompt a User to input an IP Address for a Network Device in the Rack
    print("Which device would you like to connect to. To select an individual device, your options are any of these files. ")
    ## for each template, print template and it's count
    counter = 0 
    for template in ciscotemplates:
        print("Option", counter, "is", ciscotemplates[counter]['host'])
        counter = counter + 1
    print("To select all devices, enter", all)
    print("Enter -1 to quit.")

    devicechoice = int(input())
    ##Validate the IP Address entered works for your Rack or series of devices
    try:
        ## quit value
        if (devicechoice == "-1"):
            print("You entered: ", devicechoice , ", to quit, succesfully")
            print("quit entered, quitting.")
            exit()
        elif(devicechoice >= 0 and devicechoice <= len(ciscotemplates)):
            print("You selected ", devicechoice)
            print("loading configuration..", ciscotemplates[devicechoice], "succesfully")
        elif(devicechoice == all):
            print("You selected all. Preparing devices")
        else:
            print("You didn't select one of the options. Enter an option between 1 and ", len(ciscotemplates) , "Try again")
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
    return devicechoice

                


def runaction(device, action, ciscotemplates):
    #run = True
    if action == 1:
        try:
            # tmp = f"{device}.txt"
            # device_template = ciscotemplates[tmp]
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\{device}.txt"
            print("filename is ", filename)
            f = open(filename, 'r')
            data = f.read
            print(data)
            print("your connection details are", data , "for device", device)
            debug_a = net_connect = ConnectHandler(**data)
            print(debug_a)
            net_connect.enable() 
            print(net_connect.find_prompt())
            #connect_success = True
            net_connect.send_command('reload')
            net_connect.disconnect()
            print("Now reloading device")
        except Exception as e:
            print("Failed to reload device: ", e)
    if action == 0:
        try:
            runconf = net_connect.send_command('show running-config')
            print(runconf)
            print("Printed details succesfully.")
            print("now saving runconf to a file")
            host_ip = ciscotemplates[devicechoice]['host']
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\runningconfig\\{host_ip}.txt"
            print("filename will be", filename)
            with open(filename, "w") as f:
                f.write(runconf)
        except Exception as e:
            print("Failed to print to file:", e)


        #
'''                try:
                    connection = ciscotemplates[devicechoice]
                    print("your connection details are", connection , "as value, and type of", type(connection))
                    debug_a = net_connect = ConnectHandler(**device)
                    print(debug_a)
                    try:
                        net_connect.enable() 
                        print(net_connect.find_prompt())
                        connect_success = True
                        runaction()
                        net_connect.disconnect()
                    except:
                        print("device did not connect. Going back to device choice menu.")
                except:
                    print("Failed to connect. Moving on")
 '''

