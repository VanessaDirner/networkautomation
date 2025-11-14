from netmiko import ConnectHandler

# Validate the IP Address entered works for your Rack or series of devices
valid_devices = {'192.168.7.1' : 'R1',
                  '192.168.7.2' : 'R2'}

while quit != True:

    gotob = False

    while gotob == False:

        ##Identify what Rack you are in within the prompt
        print("You are at rack 7")

        # Prompt a User to input an IP Address for a Router in the Rack
        print("Enter an IP Address for a Router in the Rack")

        ##Prompt a User to input an IP Address for a Network Device in the Rack
        print("Hi, which device would you like to connect to. Your options are: ", valid_devices, 
              "IP must be one of these to work. Enter 0 to quit.")

        try:
            devicechoice = input("Enter the router IP address: ")
            if (devicechoice == "0"):
                print("You entered: ", devicechoice , ", to quit, succesfully")
                print("quit entered, quitting.")
                quit = True
                exit()
            else:
                def build_template(ip):
                    return {
                        "device_type": "cisco_ios",
                        "host": ip,
                        "username": "cisco",
                        "password": "cisco"
                    }
                selecteddevice = build_template(devicechoice)
                print("Generated template:", selecteddevice)
                gotob = True
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
            print("Attempting to connect to device")
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
            
            outoption = input()

        quit = False
        while quit != False:
            try:
                if outoption == '1':            
                    print("You selected 1 succesfully.")
                    createloopback = net_connect.send_command('interface loopback 33')
                    addloopbackip = net_connect.send_command('ip address 192.168.7.1 255.255.255.0')
                    print("Created", createloopback, "with ip address of", addloopbackip, "succesfully.")
                elif outoption == '2':
                        createiproute = net_connect.send_command('ip route 10.0.3.2 255.255.255.0')
                        print("Created", createiproute, "succesfully.")
                elif outoption == '3':
                    print("You selected 3 succesfully.")
                    runconf = net_connect.send_command('show running-config')
                    print(runconf)
                    print("Printed details succesfully.")
                elif outoption == '4':
                    print("You selected 4 succesfully.")
                    runconf = net_connect.send_command('show ip route')
                    print(runconf)
                    print("Printed details succesfully.")
                    try:
                        print("now saving running configuration to a file")
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
