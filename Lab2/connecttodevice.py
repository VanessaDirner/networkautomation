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


while quit != True:

 

        ##Prompt a User to input an IP Address for a Network Device in the Rack
        print("Which device would you like to connect to. Your options are between 0 and ", len(updevices))
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
            elif(devicechoice > -1 and devicechoice < len(updevices)):
                print("You selected ", devicechoice)
                print("loading configuration..", updevices[devicechoice], "succesfully")
                selecteddevice = updevices[devicechoice]
                gotob = True
            else:
                print("You didn't select one of the options. Enter an option between 1 and ", len(updevices) , "Try again")
        except:
            print("Failed to get details about device choice.")
    
        print("Enter 0 to quit now. Enter anything else to continue")
        leave = input()
        if leave == '0':
            print("0 was entered, quitting.")
            quit = True
            exit()
        print("Continuing.")   
        failed = False
        try:
            ##Connect to the Network Device, and display the following information
            print("In loop....")
            print("Template is:", ciscoTemplate)
            debug_a = net_connect = ConnectHandler(**ciscoTemplate)
            print(debug_a)
            net_connect.enable() 
            print(net_connect.find_prompt())
            ##Display the active Hostname of the Device
        except:
            print("Failed to connect and enumerate details of device." \
            "Since the device cannot be connected to, will not continue. Quitting.")
            failed = True
            quit = True

        if failed == False:
            print("displayed basic device information above succesfully. What other details would you like to see? " \
            "Your options are: 1 - IP Interface Brief, 2 - Show IP OSPF Neighbor, 3 - Show Running Configuration" \
            "Enter 1 2 or 3 as your option. You can enter 0 to quit.")
            

            #Prompt user to save the following information to appropriately named files
            #Interface information (show ip interface brief)
            #OSPF Neighbor Information (show ip ospf neighbor)
            #Running configuration file (show running-config)
            outoption = input()

            try:
                if outoption == '0':            
                    print("You selected 0 succesfully.")
                    ipintbr = net_connect.send_command('show running-config')
                    print(ipintbr)
                    print("Printed details succesfully.")
                    try:
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
                elif outoption == '0':
                    print("quitting")
                    exit()
                else:
                    print("Sorry, was looking for 1, 2 or 3 for selecting a cisco device output")
            except:
                print("Failed to read input.")


            net_connect.disconnect()


    #All completed prompts should loop back to section b, and offer the user an option to quit if they are satisfied with their exports.

    #A success or failure message should accompany any task.


if quit == True:
    print("quitting")
    exit()


