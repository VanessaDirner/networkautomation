import json

def saving(updevices):
     print(updevices)
     counter = 0
     for device in updevices:
        ##Create template for all devices
        print("Device is:", device)
        ciscoTemplate = {
            'device_type': 'cisco_ios',
            'host':  updevices[counter],
            'username':'cisco',
            'password':'cisco'
        }
        print("Template is:", ciscoTemplate)
        filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\{updevices[counter]}.json" # add filelocation
        print("File name will be", filename)
        ## save templates to files
        counter = counter + 1
        test = json.dumps(ciscoTemplate)
        print(test)
        # try:
        #f = open(filename, "w")
        # with open(filename) as f:
        #     f.write(str(ciscoTemplate))
        with open(filename, 'w') as f:
            json.dump(ciscoTemplate, f, indent=4) #f.write()
        # except Exception as e:
        #     print("Failed to write to file. Continuing to next device.")
        #     print(e)