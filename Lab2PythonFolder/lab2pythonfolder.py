from netmiko import ConnectHandler
from getpass import getpass

quit = False


while quit != True:

    devices = {'R1':'192.168.7.1', 'R2':'192.168.7.2', 'R3':'192.168.7.3', 'SW1':'192.168.7.11', 'SW2':'192.168.7.12', 'SW3':'192.168.7.13', 'SW4':'192.168.7.14','SW5':'192.168.7.15'}

    rack = 7

    ciscotemplate = {
        'device_type': 'cisco_ios',
        'host':  devices['R1'],
        'username':'cisco',
        'password':'cisco'
    }

    ##Prompt a User to input an IP Address for a Network Device in the Rack
    print("Hi, which device woud you like to connect to. Your options are: ", devices.keys)

    devicechoice = input()

    ##print("now connecting to machine.", devices[1])
    ##Validate the IP Address entered works for your Rack or series of devices
    print("You selected: ", input)
    ##Identify what Rack you are in within the prompt
    print("You are at rack ", rack)

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