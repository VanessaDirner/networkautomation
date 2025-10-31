def saving(updevices):
    for device in updevices:
        ##Create template for all devices
        devicechoice = device
        print("Device is:", device)
        ciscoTemplate = {
            'device_type': 'cisco_ios',
            'host':  updevices[devicechoice],
            'username':'cisco',
            'password':'cisco'
        }
        print("Template is:", ciscoTemplate)
        try:
            debug_a = net_connect = ConnectHandler(**ciscoTemplate)
            print(debug_a)
            net_connect.enable() 
            print(net_connect.find_prompt()) 
        except:
            print("")
