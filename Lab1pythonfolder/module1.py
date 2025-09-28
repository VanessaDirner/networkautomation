
import ipaddress

## definitions

def validateinput(): 
    ## declare validator variable
    validInput = bool(0)


def validateIPNetworkAddress():
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

#validateinput()

validateIPNetworkAddress()