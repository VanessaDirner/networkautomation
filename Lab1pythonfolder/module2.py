
def routerconfig():
    print("entered module2")
    
    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 2 - ‘Generate Cisco Router Configuration’ ")
    
    configuration = {
        "hostname": hostname,
        "IP Address": ipaddr
    }

    ## Prompt the user for a hostname
    print("Please enter a hostname:")
    hostname = input()
    ## Validate the hostname given
    print("You've entered", hostname , "as your hostname")
    ## Save the hostname configuration
    exit()
    
    ## Prompt the user for the IP Address
    ipaddr = input()
    ## Validate the IP address given
    import module1
    module1.validateIPAddress()
    ## Save the IP address configuration

    ## Prompt the user for the subnet mask
    ## Validate the subnet mask given
    ## Save the subnet mask configuration

    ## Tell the user the details of the saved configuration
    
    ## do you want to add more configuration? prompt for type of input and value, add to list, save information

    ## Go back to main menu

