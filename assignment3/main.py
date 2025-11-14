import connectandrun
import savetemplates


# Validate the IP Address entered works for your Rack or series of devices
valid_devices = {'192.168.7.1' : 'R1',
                  '192.168.7.2' : 'R2'}

##IPs_and_templates = savetemplates.saving(valid_devices)
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



# Identify what Rack you are in within the prompt
print("you are at rack 7")

# Prompt a User to input an IP Address for a Router in the Rack
print("Enter an IP Address for a Router in the Rack")

## temporary input
device_input = input()

counter = int(0)
valid = False

#while valid == False and counter > 3:
for x in valid_devices:
    if device_input in  valid_devices.keys():
        print("You selected", valid_devices.get(device_input))
        print("that is a valid IP address")
        valid = True
    else:
        if valid == False:
            print("still looking for a match, latest option was ", valid_devices.get(device_input))
    counter = counter + 1

# Connect to the Network Device, and display the following information
print("Now connecting to the Router")
dictionaryname = valid_devices.get(device_input)
## next part 
print("filename is ", dictionaryname)


print("your connection details are", devices.get(dictionaryname) , "for device", device_input)
exit()
# debug_a = net_connect = ConnectHandler(**data)
# print(debug_a)
# net_connect.enable() 
# print(net_connect.find_prompt())
success = False
print("Connected succesfully")

# Display the active Hostname of the Device
print("The hostname is ")
print("Printed hostname succesfully")

# Display the Model of the Device
print("The model is ")
print("printed model succesfully")

# Prompt user to pick one of the following options to have it be performed on the device you are connecting to:
print("Which option would you like to perform.")
print("Option 1: Create a Loopback Interface with a valid IP address")
print("Option 2: Enter in a static route to another Router in your setup")
print("Option 3: Display and validate the IP Route Table is correct")
action = 1




connectandrun.runaction(device_input, IPs_and_templates)