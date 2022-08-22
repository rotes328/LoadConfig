from os import environ
from time import sleep
from netmiko import ConnectHandler, NetmikoTimeoutException


def main():

    user_name = environ.get("CiscoUser")
    password = environ.get("CiscoPassword")
    configfile = "csr02.txt"
    writemem = "write memory"
    hostip = "192.168.4.201"

    device = {
        "device_type": "cisco_xe",
        "host": hostip,
        "username": user_name,
        "password": password,
        "port": "22"
    }

    try:
        with ConnectHandler(**device) as router:
            try:
                with open(configfile, 'r') as config:
                    result = router.send_config_set(config)
                    writememory = router.send_command_timing(writemem)
                sleep(10)
                showbgp = router.send_command_timing("show ip bgp su")
                print(showbgp)
            except FileNotFoundError:
                print("File not found.")
    except NetmikoTimeoutException:
        print("Unable to reach on SSH. Confirm port, IP address, ACL.")

if __name__ == "__main__":
    main()
