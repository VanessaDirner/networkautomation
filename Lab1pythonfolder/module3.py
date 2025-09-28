
def analysis():
    print("entered module3")

    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 3 - ‘Analyze a “show interface brief” command output’ ")
    
    ## Look for ‘show interface brief’ file
 
    ## 	If it does not exist at the location expected/specified, prompt user for location

    ## Read details of show interface brief
    with open("showipconfig.txt") as file:
        print(file.read())
        ## Ask whether they want a specific interface or all 
        print("Would you like to review a specific interface or see all?")
        response = input()
        ## If they ask for all, print out the details of all
        if response == "all":
            print(file.read())
        ## If they specify a specific interface, print that one out
        else:
            print(file.read(5))

        ## Ask if they want to print out a specific interface or all, or quit 
        
        ## If they say quit, exit option 3. Otherwise go to the beginning of option 3.
        file.close()