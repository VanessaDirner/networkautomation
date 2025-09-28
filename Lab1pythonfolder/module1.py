print("entered module2")

def validateip():
    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 1 - ‘Validate an IP Address and a Subnet Mask’ ")


    ## Prompt the user for an ip address
    print("Please enter an IP address that you'd like to validate")
    print("Enter the first octet now:")
    try:
        octet1 = input(int)

        ## Validate the ip address given
        if octet1 < 0:
            print(octet1 + "is too small. Must be a number bigger than 1.")
        elif octet1 > 255:
            print(octet1 + "is too big, enter a number smaller than 255")
        elif type(octet1) != int:
            print("Please enter an integer. Please do not spell out a number, and write it out in decimal base 10.")
    except:
        print("ran into an issue, try again")
    else:
        print("no issues were ran into.")
        
    ## check length of ip address segments


    ## Let the user know the result of this validation
    print("Analysis complete.")

    ## if valid, 

    ## if not valid

    ## other details


    ## Then prompt the user for a subnet mask
    print("Please enter a subnet mask that you'd like to validate")

    ## Validate the subnet mask given

    ## Let the user know of the result of the validation
    print("Analysis complete.")

    ## if valid, 

    ## if not valid

    ## other details


    ## Validate the ip address and subnet mask together to make sure they make sense as a unit
    ## Check if they entered a broadcast address or network address (ex. 255 or .0 ending of a /240) (Technically these are still IP addresses)
    ## Show the user the result of this validation
    print("Analyzed IP address in conjunction with the subnet mask. Here's the result:")

    ## if valid, 

    ## if not valid

    ## other details


    ## Go back to main menu
    print("Hope that was helpful. Exiting back to main menu")
    