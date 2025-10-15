from netmiko import ConnectHandler
from getpass import getpass

quit = False


while quit != True:

    rack = 7

    R1template = {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.1',
        'username':'cisco',
        'password':'cisco'
    }

    R2template =  {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.2',
        'username':'cisco',
        'password':'cisco'
    }

    R3template =  {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.3',
        'username':'cisco',
        'password':'cisco'
    }

    SW1template = {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.11',
        'username':'cisco',
        'password':'cisco'
    }

    SW2template =  {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.12',
        'username':'cisco',
        'password':'cisco'
    }

    SW3template = {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.13',
        'username':'cisco',
        'password':'cisco'
    }

    SW4template =  {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.14',
        'username':'cisco',
        'password':'cisco'
    }

    
    SW5template =  {
        'device_type': 'cisco_ios',
        'host':  '192.168.7.15',
        'username':'cisco',
        'password':'cisco'
    }

    ##Identify what Rack you are in within the prompt
    print("You are at rack ", rack)

    ##Prompt a User to input an IP Address for a Network Device in the Rack
    print("Hi, which device would you like to connect to. Your options are: R1, R2, R3, SW1, SW2, SW3, SW4, SW5")

    devicechoice = input()

    ##print("now connecting to machine.", devices[1])
    ##Validate the IP Address entered works for your Rack or series of devices
    print("You selected: ", devicechoice)
    if (devicechoice == "quit"):
        quit = True
    elif(devicechoice == "R1" ):
        print("You selected R1")
        print("loading configuration..", R1template)
    elif(devicechoice == "R2"):
        print("You selected R2")
        print("loading configuration..", R2template)
    elif(devicechoice == "R3" ):
        print("You selected R3")
        print("loading configuration..", R3template)
    elif(devicechoice == "SW1"):
        print("You selected SW1")
        print("loading configuration..", SW1template)
    elif(devicechoice == "SW2"):
        print("You selected SW2")
        print("loading configuration..", SW2template)
    elif(devicechoice == "SW3"):
        print("You selected SW3")
        print("loading configuration..", SW3template)
    elif(devicechoice == "SW4"):
        print("You selected SW4")
        print("loading configuration..", SW4template)
    elif(devicechoice == "SW5"):
        print("You selected SW5")
        print("loading configuration..", SW5template)
    else:
        print("You didn't select one of the options. Try again")

 
    '''
    ##Connect to the Network Device, and display the following information
    net_connect = ConnectHandler(**ciscotemplate)
    net_connect.enable()
    print(net_connect.find_prompt())
    ##Display the active Hostname of the Device
    hostname = net_connect.send_command('hostname')
    ##Display the Model of the Device - show version - a specific line has the model type in it, pip command only get only that
    showver = net_connect.send_command('show version | include Model Number')
    print(showver)

    ipintbr = net_connect.send_command('show ip int brief')
    print(ipintbr)
    ospfneighbor = net_connect.send_command('show ip ospf neighbor')
    print(ospfneighbor)
    runconf = net_connect.send_command('show running-config | include hostname')
    print(runconf)
    net_connect.disconnect()
    '''

    '''
    Prompt user to save the following information to appropriately named files

    Interface information (show ip interface brief)

    OSPF Neighbor Information (show ip ospf neighbor)

    Running configuration file (show running-config)
    '''
    '''


    All completed prompts should loop back to section b, and offer the user an option to quit if they are satisfied with their exports.

    A success or failure message should accompany any task.
    '''


if quit == True:
    print("quitting")
    exit()