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
            ## THIS IS SAVING TO AN ARRAY AND DUMPS OUT AS AN ENTIRE ARRAY IF PRINTED!!!!! :/  to do tomorrow or whenever, just not now
    except:
        print("failed to read file. Please check if the showipconfix.txt file is in the Lab1pythonfolder and try again")
        return False
    else:
        print("Read of file succesful.")
  
    total_lines = len(lines)
    print("There's a total of", str(total_lines), "file lines.")
    for total_lines in lines:
        print(lines)
        print("line printed")
    valid = False
    retries = 0
    quit = False
    line_number = int()
    while valid == False and quit == False and retries < 3:                    
        try:
            line_number = input("Enter the line # that you'd like to read. Enter quit to quit. Line: ")
            if(line_number > total_lines or line_number < 0): ##  or type(line_number) != int
                print("There's a total of", str(total_lines), "file lines.")
                print("The line of the text file is outside the range of actual lines in the file.")
                retries = retries + 1
                print("retries", retries)
                if line_number == "quit":
                    print("quit entered. quitting...")
                    quit = True
                elif retries >= 3:
                    print("3 tries occured. quitting module...")         
            else:
                ## get a list of the strings of all lines, and remove any extra lines/newlines
                line = lines[line_number - 1].rstrip('\n')
                ## remove whitespaces from beginning or end
                line = line.strip()  
                print(line)
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


    '''
         ##  experimental
        interfaceRegexPattern = "^[a-zA-Z]+[0-0]"

        pattern = re.compile(r'interface')
        
        matches = pattern.finditer(line)
        for match in matches:
            print(match)


        ##print(interfaceRegexPattern in line_number)




        ## print out all the line names, ask user which one they want to look at

        print(file.read()) ## default is read all
        print(file.read(2))  ## this means read this many characters

        ## Ask whether they want a specific interface or all 
        print("Would you like to review a specific interface or see all? If so, enter 1")
        response = input(bool)
        print("you entered", response)
        

        ## If they ask for all, print out the details of all
        print(file.read())
        ## If they specify a specific interface, print that one out
        #else:
        print(file.read(5))
 
        ## If they say quit, exit option 3. Otherwise go to the beginning of option 3.
        file.close()

        '''