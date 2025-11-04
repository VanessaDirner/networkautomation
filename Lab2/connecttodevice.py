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




                


def runaction(action, host_ip, template):
    print("filename is ", template)
    f = open(template, 'r')
    data = json.load(f)
    print(data)
    print("your connection details are", data , "for device", host_ip)
    debug_a = net_connect = ConnectHandler(**data)
    print(debug_a)
    net_connect.enable() 
    print(net_connect.find_prompt())

    print("action is ", action, "with a type of ", type(action))
    ## once connected, run command
    if action == "0":
        try:
            print("Now reloading device")
            #connect_success = True
            net_connect.send_command('reload')
            net_connect.send_command_timing("\n")
            net_connect.disconnect()
        except Exception as e:
            print("Failed to reload device: ", e)
    if action == "1":
        try:
            runconf = net_connect.send_command('show running-config')
            print(runconf)
            print("Printed details succesfully.")
            print("now saving runconf to a file")
            print("host IP is", host_ip)
            filename = f"C:\\Users\\Vanessa\\Documents\\GitHub\\networkautomation\\Lab2\\runningconfig\\{host_ip}.txt"
            print("filename will be", filename)
            with open(filename, "w") as f:
                f.write(runconf)
        except Exception as e:
            print("Failed to print to file:", e)
    else:
         print("did not run an action")
