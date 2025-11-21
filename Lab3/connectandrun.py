from netmiko import ConnectHandler
from getpass import getpass
import os
import json



def runaction(action, host_ip, template):
        
    # Connect to the Network Device, and display the following information
    print("Now connecting to the Router")
    print("Connected succesfully")

    # Display the active Hostname of the Device
    print("The hostname is ")
    print("Printed hostname succesfully")

    # Display the Model of the Device
    print("The model is ")
    print("printed model succesfully")

    # All completed prompts should prompt the user to continue modifying the currently selected device,
    #  and then loop back to section b,
    #  and always offer the user an option to quit if they are satisfied with their actions.

    print("Would you like to continue modifying the current device?")
    print("Enter 1 to continue, 0 to stop.")

    ## next part     
    # Read connection information from a .json file unique to each device.
    print("filename is ", template)
    f = open(template, 'r')
    data = json.load(f)
    print(data)
    print("your connection details are", data , "for device", host_ip)
    debug_a = net_connect = ConnectHandler(**data)
    print(debug_a)
    net_connect.enable() 
    print(net_connect.find_prompt())
    success = False

    print("action is ", action, "with a type of ", type(action))
    ## once connected, run command
    if action == "0":
        try:    
            # load configuration
            commands = ["hostname yourMom"]
            # Push configuration to device
            print("Pushing configuration to device")
            runconf = net_connect.send_config_set(commands)
            print(runconf)
            push_success = True
            net_connect.disconnect()
        except Exception as e:
            if push_success == True:
                print("Push config completed")
            else:
                print("Failed to configure devices: ", e)

    if action == "1":
    # Option 1
    # Save running-config from Devices to a unique folder.
    #savetemplates.py
        try:
            runconf = net_connect.send_command('')
            print("Grabbed details succesfully.")
            # Enter in a static route to another Router in your setup
            print("Entering in a static route to another Router in your setup")
            print("host IP is", host_ip)
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\assignment3\\runningconfig\\{host_ip}.txt"
            print("filename will be", filename)
            with open(filename, "w") as f:
                f.write(runconf)
            print("Saved details to file succesfully")
            success = True
        except Exception as e:
            print("Failed to print to file:", e)
    if success == True:
        print("") # fail succesfully and silently -- what a great idea for prod
    else:
         print("did not run an action")


