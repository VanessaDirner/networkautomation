from netmiko import ConnectHandler
from getpass import getpass

quit = False

rack = 7

## save configs all separately because simplicity/not the focus of this LAb


## temp for testing
updevices = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.11', '192.168.7.12', '192.168.7.13', '192.168.7.14', '192.168.7.15', '192.168.7.140']


devicechoice = int()

ciscoTemplate = {
    'device_type': 'cisco_ios',
    'host':  updevices[devicechoice],
    'username':'cisco',
    'password':'cisco'
}



all = len(updevices) + 1

while quit != True:
        ##Prompt a User to input an IP Address for a Network Device in the Rack
        print("Which device would you like to connect to. To select an individual device, your options are between 0 and ", len(updevices))
        print("To select all devices, enter", all)
        print("Enter -1 to quit.")

        devicechoice = input()
        selecteddevice = ''

        ##print("now connecting to machine.", devices[1])
        ##Validate the IP Address entered works for your Rack or series of devices
        try:

            if (devicechoice == "-1"):
                print("You entered: ", devicechoice , ", to quit, succesfully")
                print("quit entered, quitting.")
                quit = True
                exit()
            elif(devicechoice > -1 and devicechoice <= len(updevices)):
                print("You selected ", devicechoice)
                print("loading configuration..", updevices[devicechoice], "succesfully")
                selecteddevice = updevices[devicechoice]
            elif(devicechoice == all):
                print("You selected all. Preparing devices")
            else:
                print("You didn't select one of the options. Enter an option between 1 and ", len(updevices) , "Try again")
        except:
            print("Failed to get details about device choice.")
    
        print("Enter -1 to quit now. Enter anything else to continue")
        leave = input()
        if leave == '-1':
            print("-1 was entered, quitting.")
            quit = True
            exit()
        print("Continuing.")   
        failed = False
        try:
            if devicechoice > -1 and devicechoice <= len(updevices):
                ##Connect to the Network Device, and display the following information
                print("Template is:", ciscoTemplate)
                debug_a = net_connect = ConnectHandler(**ciscoTemplate)
                print(debug_a)
                net_connect.enable() 
                print(net_connect.find_prompt())
            ##Display the active Hostname of the Device
            if devicechoice == all:
                for device in updevices:
                    ##Connect to the Network Device, and display the following information
                    devicechoice = device
                    print("Template is:", ciscoTemplate)
                    debug_a = net_connect = ConnectHandler(**ciscoTemplate)
                    print(debug_a)
                    net_connect.enable() 
                    print(net_connect.find_prompt()) 
        except:
            print("Failed to connect and enumerate details of device." \
            "Since the device cannot be connected to, will not continue. Quitting.")
            failed = True
            quit = True

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


    #All completed prompts should loop back to section b, and offer the user an option to quit if they are satisfied with their exports.

    #A success or failure message should accompany any task.


if quit == True:
    print("quitting")
    exit()


