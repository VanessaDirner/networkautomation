
import ipaddress

## definitions

def validateinput(): 
    ## declare validator variable
    validInput = bool(0)

## exit while loop once ip address passes basic validation
    while validInput == 0:
    ## read user input
        try:
            ipaddr = input()
        except:
            print("ran into an issue, try again. Are you entering a number in base 10 format?")
            validInput = bool(0)
        else:
            print("Read number as " , ipaddr , ". Will now review the entered information.")
            validInput = bool(1)
            if ipaddr == "quit":
                print("quit was entered. Quitting..")
                exit()
            validateIPAddress()
                    

def validateIPAddress():    
    validIPaddress = bool(0)
    while validIPaddress == 0:
        try:
            ##  run ip address through ip address validation
            print("Printing IP address", ipaddress.ip_address(ipaddr))
            #validIPaddress = bool(1)
        except:
            print("Failed to parse IP address. Please re-enter a IP address again.")
            validateinput()
        else:
            print("not sure in which case we get here.. things are probably working.")
            exit()



print("entered module1")

## This is an introduction to the program, purpose, author etc.
print("Welcome to module 1 - ‘Validate an IP Address and a Subnet Mask’ ")

## Prompt the user for an ip address
print("Please enter an IP address that you'd like to validate")

## process first octet
print("Enter the ip address in dotted decimal notation format now:")

## declare variable for ip address with type of ipaddress
ipaddr = ipaddress

retryValidation = int(0)

validateinput()
