import os
import getpass

def routerconfig():
    print("entered module2")
    
    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 2 - ‘Generate Cisco Router Configuration’ ")
    
    configuration = {
    }

    ## Prompt the user for a hostname
    print("Please enter a hostname:")
    hostname = input()
    ## Validate the hostname given
    print("You've entered", hostname , "as your hostname")
    ## Save the hostname configuration
    configuration.update({"hostname": hostname})
    print(configuration, " configuration updated.")

    
    ## Prompt the user for the IP Address
    print("please enter an ip address")
    ipaddr = input()

    configuration.update({"IP Address": ipaddr})
    print(configuration, "you've added", configuration.get("IP Address"), "as your IP address")

    ## Validate the IP address given
 #   import module1
#    module1.validateIPAddress()
    ## Save the IP address configuration

    ## Prompt the user for the subnet mask
    ## Validate the subnet mask given
    ## Save the subnet mask configuration

    ## Tell the user the details of the saved configuration
    print("your final configuration details are:", configuration)
        
    ## save all details to a file
    filename = "CiscoRouterConfig.txt"

    print("saving configuration to ", filename)

    with open(filename, "a") as f:
        f.write(configuration.get("hostname"))

    ## do you want to add more configuration? prompt for type of input and value, add to list, save information

    ## Go back to main menu


'''
    print("where do you want to save the file?")

    home = os.path.expanduser("")
    environment = os.defpath
    print(home, environment)
    exit()


    path = input()

    fullpath = home + "CiscoRouterConfiguration.txt"

'''

