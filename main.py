# interface_vlan_config.py
# Zaid Laffta
# 1/21/2025

import paramiko
import time

def configure_interfaces(ip, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

        shell = client.invoke_shell()
        time.sleep(1)

        shell.send('enable\n')
        time.sleep(1)
        shell.send('configure terminal\n')
        time.sleep(1)

        # Change this range as needed
        shell.send('interface range GigabitEthernet1/0/1-48\n')
        time.sleep(0.5)
        shell.send('switchport mode access\n')
        shell.send('switchport access vlan 244\n')
        time.sleep(0.5)

        shell.send('end\n')
        shell.send('write memory\n')
        time.sleep(2)

        output = shell.recv(5000).decode('utf-8')
        print(output)

        client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip = input("Enter the switch IP address: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    configure_interfaces(ip, username, password)
