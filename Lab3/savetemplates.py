import json

def saving(updevices):
    print(updevices)
    IPs_and_templates = {}
    counter = 0
    for device in updevices:
        try:
            ##Create template for all devices
            print("Device is:", device)
            ciscoTemplate = {
                'device_type': 'cisco_ios',
                'host':  updevices[counter],
                'username':'cisco',
                'password':'cisco'
            }
            print("Template is:", ciscoTemplate)
            # add filelocation
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab3\\templates\\{updevices[counter]}.json" 
            print("File name will be", filename)
            ## save templates to files
            counter = counter + 1
            test = json.dumps(ciscoTemplate)
            with open(filename, 'w') as f:
                json.dump(ciscoTemplate, f, indent=4) #f.write()
            ## Associate IP to template
            IPs_and_templates.update({device: filename})
            print("Saving IP to template:",IPs_and_templates)
        except Exception as e:
            print("Failed to write to file. Continuing to next device.")
            print(e)
   ##print("Final list of IPs and their associated templates:", IPs_and_templates)
    return IPs_and_templates