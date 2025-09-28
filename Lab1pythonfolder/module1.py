def ipmodule():
    import ipaddress, Lab1_Main, module2, module3
    ## definitions

    ## reference: https://stackoverflow.com/questions/63192480/check-if-valid-ip-address-from-user-input
    def validateIPAddress():
        valid = False
        retries = int(0)
        quit = False
        while valid == False and retries < 3 and quit != True:
            try:
                address = ipaddress.ip_address(input('Enter IP address: '))
                print(address)
            except ValueError:
                print(ValueError.with_traceback)
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
                subnet = ipaddress.ip_network(input('Enter your network address and subnet in CIDR notation: '))
                print(subnet)
            except ValueError:
                print(ValueError.with_traceback)
                print("Invalid value. Try again. A valid subnet example would be 10.1.1.0 /24")
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


    print("entered module1")

    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 1 - ‘Validate an IP Address and a Subnet Mask’ ")

    ## Prompt the user for an ip address
    print("Please enter an IP address that you'd like to validate")

    ## process first octet
    print("Enter the ip address in dotted decimal notation format now:")

    ## declare variable for ip address with type of ipaddress
    ipaddr = ipaddress.ip_address
    ipnetw = ipaddress.ip_network
    ipfullvalue = ""
    retryValidation = int(0)

    ipaddr = validateIPAddress()

    print("back out of function. returned value is:", ipaddr)

    ipnetw = validateSubnet()

    print("back out of function. subnet value is ", ipnetw)

    answer = compareIpAddresstoSubnet()
    print("The provided IP address is part of the provided subnet. ", answer)

    return True


