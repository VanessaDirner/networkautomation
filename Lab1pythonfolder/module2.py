import os
import getpass
import json

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

    ## Validate the IP address given
    import module1
    try:
        CompleteIPAddr = module1.ipmodule()
    except:
        if CompleteIPAddr == False:
            print("Failed to get a valid IP address. Exiting program")
            exit()
    else:
        ## Save the IP address configuration
        configuration.update({"IP Address": CompleteIPAddr})
        print("You've added", configuration.get("IP Address"), "as your IP address")

    
    ## Prompt the user for the subnet mask
    ## Validate the subnet mask given
    ## Save the subnet mask configuration
    
    ##https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python
    ciscoconfig = ("\n".join("{}\t{}".format(k, v) for k, v in configuration.items()))
    
    ciscoconfig = ciscoconfig.replace("'", "")
    ciscoconfig = ciscoconfig.replace(",", "")
    ciscoconfig = ciscoconfig.replace("(", "")
    ciscoconfig = ciscoconfig.replace(")", "")


    ## Tell the user the details of the saved configuration
    print("your final configuration details are: \n",
           ciscoconfig)
    
    ## save all details to a file
    filename = "CiscoRouterConfig.txt"

    print("saving configuration to ", filename)

    ## overwrite existing content - we don't need more than 1 set of config
    with open(filename, "w") as f:
        f.write(ciscoconfig)

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