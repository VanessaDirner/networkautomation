## reference: https://stackoverflow.com/questions/63192480/check-if-valid-ip-address-from-user-input

def ipmodule():
    import ipaddress
    ## definitions

    def validateIPAddress():
        ## Prompt the user for an ip address
        print("Please enter an IP address that you'd like to validate.")
        ## process first octet
        print("Enter the ip address in dotted decimal notation format now:")
        ## for example, your current IP address and subnet mask is: ->
        valid = False
        retries = int(0)
        quit = False
        while valid == False and retries < 3 and quit != True:
            try:
                address = ipaddress.ip_address(input('Enter IP address: '))
                print(address)
            except ValueError:
                print("Invalid value. Try again.")
                retries = retries + 1
                print("retries", retries)
                if ipaddr == "quit":
                    print("quit was entered. Quitting..")
                    quit = True
                elif retries >= 3:
                    print("3 tries occured. Quitting ip address validation")
            else:
                print("Valid IP address")
                valid = True
                return address

    def validateSubnet():
        valid = False
        retries = int(0)
        quit = False
        while valid == False and retries < 3 and quit != True:
            try:
                subnet = ipaddress.ip_network(input('Enter network address as well as subnet in CIDR notation: \n'))
                print(subnet)
            except ValueError:
                print("Invalid value. Try again.  \n A valid subnet example would be: 10.1.1.0/24.")
                retries = retries + 1
                print("retries", retries)
                if ipaddr == "quit":
                    print("quit was entered. Quitting..")
                    quit = True
                elif retries >= 3:
                    print("3 tries occured. Quitting ip network validation")
            else:
                print("Valid subnet")
                valid = True
                return subnet

    ## reference: https://stackoverflow.com/questions/819355/how-can-i-check-if-an-ip-is-in-a-network-in-python
    def compareIpAddresstoSubnet():
        isipinnetwork = ipaddress.ip_address(ipaddr) in ipaddress.ip_network(ipnetw)
        return isipinnetwork


    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to Module 1 - ‘Validate an IP Address and a Subnet Mask’ ")

    invalidconfiguration = True
    retries = 0
    
    while invalidconfiguration == True and retries < 3:
            
        ## declare variable for ip address with type of ipaddress
        ipaddr = ipaddress.ip_address
        ipnetw = ipaddress.ip_network
        
        ipaddr = validateIPAddress()

        if ipaddr == None:
            print("Sorry, but you did not complete IP address validation. Exiting module 1")
            exit()
        ipnetw = validateSubnet()

        if ipnetw == None:
            print("Sorry but you did not configure a subnet succesfully. Exiting module 1.")
            exit()

            
        answer = compareIpAddresstoSubnet()
        
        ## https://www.w3schools.com/python/python_tuples_unpack.asp
        ipfullvalue = ipaddr.compressed, ipnetw.netmask.compressed
        (validatedIPaddr, validatedSubnetMask) = ipfullvalue
            
        print("Your IP Address and subnet mask are:")
        print(validatedIPaddr)
        print(validatedSubnetMask)
        print("Thanks for entering those details.")

        if answer == True:
            print("The provided IP address is part of the provided subnet.")
            invalidconfiguration = False
        elif answer == False:
            print("The provided IP address is NOT part of the provided subnet. ")
            print("Let's do that again.")
            retries = retries + 1
            invalidconfiguration = True
            

        ## Finally, we can leave if config is accurate
        if invalidconfiguration == False:
           return validatedIPaddr, validatedSubnetMask


