import json

def saving(valid_devices):
    print("valid devices are",valid_devices)
    IPs_and_templates = {}
    counter = 0
    for device in valid_devices:
        try:
            ##Create template for all devices
            # print("Device is:", device)
            ciscoTemplate = {
                'device_type': 'cisco_ios',
                'host':  valid_devices[counter],
                'username':'cisco',
                'password':'cisco'
            }
            # print("Template is:", ciscoTemplate)
            # add filelocation
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\assignment3\\templates\\{valid_devices[counter]}.json" 
            # print("File name will be", filename)
            ## save templates to files
            counter = counter + 1
            test = json.dumps(ciscoTemplate)
            with open(filename, 'w') as f:
                json.dump(ciscoTemplate, f, indent=4) #f.write()
            ## Associate IP to template
            IPs_and_templates.update({device: filename})
            # print("Saving IP to template:",IPs_and_templates)
        except Exception as e:
            print("Failed to write to file. Continuing to next device.")
            print(e)
    print("Final list of IPs and their associated templates:", IPs_and_templates)
    print("Saved to templates succesfully")
    return IPs_and_templates

# valid_devices = ['192.168.7.1', '192.168.7.2']
# print("Go to function")
# IPs_and_templates = saving(valid_devices)
# print("Result of module is", IPs_and_templates)
# exit()   