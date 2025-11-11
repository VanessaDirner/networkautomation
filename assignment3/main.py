# Identify what Rack you are in within the prompt
print("you are at rack 7")

# Prompt a User to input an IP Address for a Router in the Rack
print("Enter an IP Address for a Router in the Rack")

# Validate the IP Address entered works for your Rack or series of devices
valid_devices = ['192.168.7.1', '192.168.7.2']
device_input = input()

counter = int()
valid = False

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
    
exit()

# Connect to the Network Device, and display the following information
print("Now connecting to the Router")
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

# Create a Loopback Interface with a valid IP address
print("Creating a Loopback Interface with a valid IP address")

# Enter in a static route to another Router in your setup
print("Entering in a static route to another Router in your setup")

# Display and validate the IP Route Table is correct
print("Displaying and validating that the IP Route Table is correct")

# Save your configuration to an appropriately named file.
print("Saving your configuration to an appropriately named file.")

# All completed prompts should prompt the user to continue modifying the currently selected device,
#  and then loop back to section b,
#  and always offer the user an option to quit if they are satisfied with their actions.

print("Would you like to continue modifying the current device?")
print("Enter 1 to continue, 0 to stop.")

# A success or failure message should accompany any task.