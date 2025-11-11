import connectandrun
import savetemplates

# Validate the IP Address entered works for your Rack or series of devices
valid_devices = ['192.168.7.1', '192.168.7.2']

IPs_and_templates = savetemplates.saving(valid_devices)
print("Result of module is", IPs_and_templates)


# Identify what Rack you are in within the prompt
print("you are at rack 7")

# Prompt a User to input an IP Address for a Router in the Rack
print("Enter an IP Address for a Router in the Rack")

device_input = '192.168.7.1' # input()

counter = int()
valid = True

while valid == False:
    for x in valid_devices:
        if device_input == valid_devices[counter]:
            print("You selected", valid_devices[counter])
            print("that is a valid IP address")
            valid = True
        else:
            if valid == False:
                print("still looking for a match, latest option was ", valid_devices[counter])
        counter = counter + 1

connectandrun.runaction(device_input, IPs_and_templates)