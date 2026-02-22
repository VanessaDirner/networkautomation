

def action_and_device():

    ## main menu

    print("Hello. Please select what action you'd like to do," \
    " as well as which devices to run it on.")

    ## keeping asking until they pick an option
    quit = False
    choice_selected = False
    device_selected = False
    get_devices = False
    get_addresses = False
    device_selected = False
    devicechoice = None


    while (choice_selected == False) and (quit == False):
        print("What action would you like to complete? " \
        "Your options are: 0 - Push Configuration to Device : 1 - Save Running Configuration. 2 - Compare Configuration Filesss" \
        " You can quit with -1")

        ## we are keeping track of which option they picked with selected_action
        
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
                print("debug- we make it here?")
            elif outoption == '-1':
                print("quitting")
                quit = True
                quit()
            else:
                print("Sorry, was looking for -1, 0, 1, 2 for selecting a cisco device output")
        except Exception as e:
            print("Ran into an issue: ", e)

    all = int(4)
    # print("did we make it here - 2")print("choice selected = ", choice_selected, "get_devices = ", get_devices, "deviceselected = ", device_selected)
    while (choice_selected == True) and (quit == False) and (get_devices == True) and (device_selected == False):
        ##Prompt a User to input an IP Address for a Network Device in the Rack
        print("Which device would you like to connect to. To select an individual device, your options are any of these IPs. ")
        ## for each template, print template and it's count
        ips = ["192.168.6.3", "192.168.6.11", "192.168.6.12"]
        iplist = '192.168.6.3, 192.168.6.11, 192.168.6.12'
        # print(ips)
        # for ip in ips:
        #     # print("Option", index, "is", ip)
        #     optionsindextoIPs.update({index : ip})
        #     index = index + 1
        print("Items list", iplist)
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
            elif(devicechoice > -1 and devicechoice <= len(ips)):
                print("Device choice was ", devicechoice)
                print("selected device is", ips[devicechoice])
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

    return outoption, devicechoice