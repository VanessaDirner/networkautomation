from netmiko import ConnectHandler
from getpass import getpass
import os
import json

def gettemplates():
    
    ciscotemplates = []

    files = os.listdir("./templates")
    print(files)
    counter = 0

    ## get all templates
    for file in files:
        print("file is ",file)
        filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\{file}"
        print("filename is ", filename)
        f = open(filename, 'r')
        data = json.load(f)
        ciscotemplates.append(data)
        print(ciscotemplates[counter])
        counter = counter + 1
        
    return ciscotemplates




                


def runaction(device, action, ciscotemplates):
    #run = True
    # tmp = f"{device}.txt"
    # device_template = ciscotemplates[tmp]
    filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\templates\\192.168.7.12.json"
    print("filename is ", filename)
    f = open(filename, 'r')
    data = json.load(f)
    print(data)
    print("your connection details are", data , "for device", device)
    debug_a = net_connect = ConnectHandler(**data)
    print(debug_a)
    net_connect.enable() 
    print(net_connect.find_prompt())

    ## once connected, run command
    if action == 1:
        try:
            #connect_success = True
            net_connect.send_command('reload')
            net_connect.disconnect()
            print("Now reloading device")
        except Exception as e:
            print("Failed to reload device: ", e)
    if action == 0:
        # try:
            runconf = net_connect.send_command('show running-config')
            print(runconf)
            print("Printed details succesfully.")
            print("now saving runconf to a file")
            print("type is:") 
            type(device)
            host_ip = ciscotemplates[device]['host']
            print("host IP is", host_ip)
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\runningconfig\\{host_ip}.txt"
            print("filename will be", filename)
            with open(filename, "w") as f:
                f.write(runconf)
        # except Exception as e:
        #     print("Failed to print to file:", e)


        #
'''                try:
                    connection = ciscotemplates[devicechoice]
                    print("your connection details are", connection , "as value, and type of", type(connection))
                    debug_a = net_connect = ConnectHandler(**device)
                    print(debug_a)
                    try:
                        net_connect.enable() 
                        print(net_connect.find_prompt())
                        connect_success = True
                        runaction()
                        net_connect.disconnect()
                    except:
                        print("device did not connect. Going back to device choice menu.")
                except:
                    print("Failed to connect. Moving on")
 '''

