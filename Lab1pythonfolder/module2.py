import os
import getpass
import json

def routerconfig():
    print("entered module2")
    
    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 2 - ‘Generate Cisco Router Configuration’ ")
    

    ## setup template configuration details

    ## this will hold the ip config
    configuration = {
    }

    ## these are our preset commands before hostname
    en = "Enable"
    conft = "Configure Terminal"
    hostname = "Hostname"
    host = ""
    noshut = "No shutdown"
    leave = "Exit"


    ## Prompt the user for a hostname
    tries = 0 
    valid = False
    while tries <3 and valid == False:
        print("Please enter a hostname:")
        try:
            host = input()
            ## Validate the hostname given
            print("You've entered", host , "as your hostname")
            print(" configuration updated.")
            valid = True
        except:
            print("Sorry, didn't catch that. Would you like to enter that again? ")
            tries = tries + 1
        ## Prompt user for interface

## get interface type and name in cisco formatting to add to configuration
    tries = 0 
    valid = False
    while tries <3 and valid == False:
        print("What interface would you like to configure? Please enter the name accurately for Cisco configuration")
        try:
            interface = input()
            valid = True
        except:
            print("Sorry, didn't catch that. Would you like to enter that again? ")


    ## Validate the IP address given
    import module1
    try:
        print("Now moving on to gathering IP details.")
        CompleteIPAddr = module1.ipmodule()
    except:
        if CompleteIPAddr == False:
            print("Failed to get a valid IP address. Exiting program")
            exit()
    else:
        ## Save the IP address configuration
        configuration.update({"IP Address": CompleteIPAddr})
        print("You've added", configuration.get("IP Address"), "as your IP address")

    
    ##https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python
    ciscoconfig = ("\n".join("{}\t{}".format(k, v) for k, v in configuration.items()))
    
    ciscoconfig = ciscoconfig.replace("'", "")
    ciscoconfig = ciscoconfig.replace(",", "")
    ciscoconfig = ciscoconfig.replace("(", "")
    ciscoconfig = ciscoconfig.replace(")", "")


    ## Tell the user the details of the saved configuration
    print("your final configuration details are: \n",
           en, "\n", conft, "\n",
           hostname, "\n",  interface, 
           ciscoconfig, "\n", noshut, "\n", leave)
    
    ## save all details to a file
    filename = "CiscoRouterConfig.txt"

    print("saving configuration to ", filename)

    ## overwrite existing content - we don't need more than 1 set of config
    with open(filename, "w") as f:
        f.write(ciscoconfig)




'''


    ## do you want to add more configuration? prompt for type of input and value, add to list, save information

    ## Go back to main menu

    print("where do you want to save the file?")

    home = os.path.expanduser("")
    environment = os.defpath
    print(home, environment)
    exit()


    path = input()

    fullpath = home + "CiscoRouterConfiguration.txt"

'''