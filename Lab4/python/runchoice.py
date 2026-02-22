import ansible_runner
import subprocess



def run_it(outoption, devicechoice):

    ips = ["192.168.6.3", "192.168.6.11", "192.168.6.12"]
    # Backup

    if outoption == '1':
        print("Backing up configuration...")
        # if devicechoice == 0:
        #     host = "rt3"
        # if devicechoice == 1:
        #     host = "sw1"
        # if devicechoice == 2:
        #     host = "sw2"
        if devicechoice == 4:
                    backupconfig = [
                "ansible-playbook",
                "//home/vanessa/Documents/networkautomation/Lab4/playbooks/backupconfiguration.yaml",
                "-i", "./inventory/hosts.ini",
                "--limit", "all",
                # "--check",
                "--diff"
            ]
        else:
            backupconfig = [
                "ansible-playbook",
                "//home/vanessa/Documents/networkautomation/Lab4/playbooks/backupconfiguration.yaml",
                "-i", "./inventory/hosts.ini",
                "--limit", ips[devicechoice],
                # "--check",
                "--diff"
            ]

        result = subprocess.run(backupconfig, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)


    ## Compare versions
    if outoption == '2':
        print("Comparing configuration...")
        compareconfig = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/compare.yaml",
            "-i", "./inventory/hosts.ini"
        ]

        result = subprocess.run(compareconfig, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

    # Push config to device .3 Router
    if outoption == '0' and devicechoice == 0:
        print("selected 0 0 ")
        pushRt3config = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/push_rt3_conf.yaml",
            "-i", "./inventory/hosts.ini",
            # "--check",
            "--diff"
        ]

        result = subprocess.run(pushRt3config, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

    # Push config to device .11 SW1PC
    if outoption == '0' and devicechoice == 1:
        pushSw11config = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/push_sw11_conf.yaml",
            "-i", "./inventory/hosts.yaml",
            # "--check",
            "--diff"
        ]

        result = subprocess.run(pushSw11config, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

    # Push config to device .12 SW2Serv
    if outoption == '0' and devicechoice == 2:
        pushSw12config = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/push_sw12_conf.yaml",
            "-i", "./inventory/hosts.yaml",
            # "--check",
            "--diff"
        ]

        result = subprocess.run(pushSw12config, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)


    # Push config to all devices
    if outoption == '0' and devicechoice == 4:
        pushRt3config = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/push_rt3_conf.yaml",
            "-i", "./inventory/hosts.ini",
            # "--check",
            "--diff"
        ]

        result = subprocess.run(pushRt3config, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

        pushSw11config = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/push_sw11_conf.yaml",
            "-i", "./inventory/hosts.yaml",
            # "--check",
            "--diff"
        ]

        result = subprocess.run(pushSw11config, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)

        pushSw12config = [
            "ansible-playbook",
            "/home/vanessa/Documents/networkautomation/Lab4/playbooks/push_sw12_conf.yaml",
            "-i", "./inventory/hosts.yaml",
            # "--check",
            "--diff"
        ]

        result = subprocess.run(pushSw12config, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        