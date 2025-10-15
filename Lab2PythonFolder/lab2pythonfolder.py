import netmiko

'''
Prompt a User to input an IP Address for a Network Device in the Rack

Identify what Rack you are in within the prompt

Validate the IP Address entered works for your Rack or series of devices

Connect to the Network Device, and display the following information

Display the active Hostname of the Device

Display the Model of the Device

Prompt user to save the following information to appropriately named files

Interface information (show ip interface brief)

OSPF Neighbor Information (show ip ospf neighbor)

Running configuration file (show running-config)

All completed prompts should loop back to section b, and offer the user an option to quit if they are satisfied with their exports.

A success or failure message should accompany any task.
'''