from netmiko import ConnectHandler

# Validate the IP Address entered works for your Rack or series of devices
valid_devices = {'192.168.7.1' : 'R1',
                  '192.168.7.2' : 'R2'}

##IPs_and_templates = savetemplates.saving(valid_devices)
R1template = {
    'device_type': 'cisco_ios',
    'host':  '192.168.7.1',
    'username':'cisco',
    'password':'cisco'
}

R2template =  {
    'device_type': 'cisco_ios',
    'host':  '192.168.7.2',
    'username':'cisco',
    'password':'cisco'
}

R3template =  {
    'device_type': 'cisco_ios',
    'host':  '192.168.7.3',
    'username':'cisco',
    'password':'cisco'
}



# Identify what Rack you are in within the prompt
print("you are at rack 7")

# Prompt a User to input an IP Address for a Router in the Rack
print("Enter an IP Address for a Router in the Rack")




while quit != True:

    gotob = False

    while gotob == False:

        ##Identify what Rack you are in within the prompt
        print("You are at rack ", rack)

        ##Prompt a User to input an IP Address for a Network Device in the Rack
        print("Hi, which device would you like to connect to. Your options are: R1, R2, R3, SW1, SW2, SW3, SW4, SW5." \
        "Enter 0 to quit.")

        devicechoice = input()
        devicechoice = devicechoice.upper()
        selecteddevice = ''

        ##print("now connecting to machine.", devices[1])
        ##Validate the IP Address entered works for your Rack or series of devices
        try:
            print("You entered: ", devicechoice , ", to quit, succesfully")
            if (devicechoice == "0"):
                print("quit entered, quitting.")
                quit = True
                exit()
            elif(devicechoice == "R1" ):
                print("You selected R1")
                print("loading configuration..", R1template, "succesfully")
                selecteddevice = R1template
                gotob = True
            elif(devicechoice == "R2"):
                print("You selected R2")
                print("loading configuration..", R2template, "succesfully")
                selecteddevice = R2template                
                gotob = True
            elif(devicechoice == "R3" ):
                print("You selected R3")
                print("loading configuration..", R3template, "succesfully")
                selecteddevice = R3template
                gotob = True
            else:
                print("You didn't select one of the options. Try again")
        except:
            print("Failed to get details about device choice.")


    while gotob == True:
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
            net_connect = ConnectHandler(**selecteddevice)
            net_connect.enable() 
            print(net_connect.find_prompt())

            ##Display the active Hostname of the Device
            hostname = net_connect.send_command('show running-config | include hostname')

            ##Display the Model of the Device - show version - a specific line has the model type in it, pipe command only get only that
            showver = net_connect.send_command('show version | include Model Number')
            print(showver)
        except:
            print("Failed to connect and enumerate details of device." \
            "Since the device cannot be connected to, will not continue. Quitting.")
            failed = True
            quit = True

        if failed == False:
            print("displayed basic device information above succesfully. What other details would you like to see? " \
            "Your options are: 1 - Create a Loopback Interface with a valid IP address, 2 - Enter in a static route to another Router in your setup," \
            " 3 - Display and validate the IP Route Table is correct, 4 - Save your configuration to an appropriately named file" \
            "Enter 1 2 or 3 as your option. You can enter 0 to quit.")

            #Prompt user to save the following information to appropriately named files
            #Interface information (show ip interface brief)
            #OSPF Neighbor Information (show ip ospf neighbor)
            #Running configuration file (show running-config)
            outoption = input()

        quit = False
        while quit != False:
            try:
                if outoption == '1':            
                    print("You selected 1 succesfully.")
                    ipintbr = net_connect.send_command('show ip int brief')
                    print(ipintbr)
                    print("Printed details succesfully.")
                    try:
                        print("Now saving ipintbr to a file")
                        with open("ipintbr.txt", "w") as f:
                            f.write(ipintbr)
                    except:
                        print("Failed to print to file")
                elif outoption == '2':
                        ospfneighbor = net_connect.send_command('show ip ospf neighbor')
                        print(ospfneighbor)
                        print("Printed details succesfully.")
                        try:
                            print("now saving ospfneighbor to a file")
                            with open("ospfneighbor.txt", "w") as f:
                                f.write(ospfneighbor)
                        except:
                            print("Failed to print to file")
                elif outoption == '3':
                    print("You selected 3 succesfully.")
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

if quit == True:
    print("quitting")
    exit()



print("Connected succesfully")



# Display the Model of the Device
print("The model is ")
print("printed model succesfully")

# Prompt user to pick one of the following options to have it be performed on the device you are connecting to:
print("Which option would you like to perform.")
print("Option 1: Create a Loopback Interface with a valid IP address")
print("Option 2: Enter in a static route to another Router in your setup")
print("Option 3: Display and validate the IP Route Table is correct")
action = 1




connectandrun.runaction(device_input, IPs_and_templates)