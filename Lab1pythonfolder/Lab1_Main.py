## The virtual environment for this lab is called lab1.
## ./Lab1pythonfolder/lab1/scripts/activate


## import modules
import module1, module2, module3

## This is an introduction to the program, purpose, author etc.


print("Welcome to my program")
print("A wonderful place for network enthusiasts. This lab 1 assignment will help you with many administrative tasks.")
print("This program was written by Vanessa Dirner in September, 2025.")
print("Let's get started")


## exit option
retries = 0

while (retries < 3):           
     

    ## direct user to make a choice
    print("You are in the main menu selection.")
    print("Pick a number. Your options are:")
    print("'1' for ‘Validate an IP Address and a Subnet Mask’ ")
    print("'2' for ‘Generate Cisco Router Configuration’ ")
    print("'3' for ‘Analyze a “show interface brief” command output’")


    ##Prompt user for a choice
    ## Use a case to select a menu
    menuchoice = input()    
    print("Your input was " + menuchoice)
    
    match menuchoice:
        case "1":
            print("Starting menu choice 1 - ‘Validate an IP Address and a Subnet Mask’")
            module1.ipmodule()
        case "2":
            print("Starting menu choice 2 -  ‘Generate Cisco Router Configuration’")
            module2.routerconfig()
        case "3":
            print("Starting menu choice 3 - ‘Analyze a “show interface brief” command output’")
            module3.analysis()
        case "quit":
            print("Exiting.")
            exit()
        case _:
            print(retries)     
            retries = retries +1       
            if retries == 3:
                print("This is working out. Quitting while I still can.")
                exit()
            else:
                print("Sorry, didn't catch that. Try again:")



