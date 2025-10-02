import re


def analysis():
    print("entered module3")

    ## This is an introduction to the program, purpose, author etc.
    print("Welcome to module 3 - ‘Analyze a “show interface brief” command output’ ")
    
    ## Look for ‘show interface brief’ file
 
    ## 	If it does not exist at the location expected/specified, prompt user for location

    ## Read details of show interface brief
    try:
        with open("./showipconfig.txt") as file:
            ## parse the file
            ## separate out the lines
            ## read specific parts of lines
            ## skip the first line and assign each line the name of the first string in the line "vlan1"
            
            ## https://www.youtube.com/watch?v=ZLCZkMk69y0 how to read a line
        
            lines = file.readlines()
            file.close

    except:
        print("failed to read file. Please check if the showipconfix.txt file is in the Lab1pythonfolder. If it is, change your running directory to Lab1pythonfolder. Thanks! :)")
        return False
    else:
        print("Read of file succesful.")
  
    ipconfigArray = []
    total_lines = len(lines)
    ## append to an easier to handle data object to read to later
    for line in lines:
        print(line)
        ipconfigArray.append(line)


    
    print("There's a total of", str(total_lines), "file lines.")
    valid = False
    retries = 0
    quit = False
    while valid == False and quit == False and retries < 3:                    
        try:
            line_number = int(input("Enter the line # that you'd like to read. Enter 0 to quit. Line: ")) 
            if(line_number > total_lines or line_number < 1):
                print("The line of the text file is outside the range of actual lines in the file.")
                retries = retries + 1
                print("retries", retries)
                if line_number == 0:
                    print("quit entered. quitting...")
                    quit = True
                elif retries >= 3:
                    print("3 tries occured. quitting module...")         
            else:
                tempvalue = line_number+1
                print(ipconfigArray[tempvalue])
        except:
            print("failed to read your line request. Please try again.")
            print("Invalid value. Try again.")
            retries = retries + 1
            print("retries", retries)
            if line_number == "quit":
                print("quit was entered. Quitting..")
                quit = True
            elif retries >= 3:
                print("3 tries occured. Quitting ip address validation")

        else:
            print("Returning to line input.")

