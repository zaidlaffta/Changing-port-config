Interface VLAN 244 Configurator for Cisco Switch
Overview
This script (interface_vlan_config.py) connects to a Cisco switch over SSH and configures an interface range (GigabitEthernet1/0/1-48) to:

Mode: Access

VLAN: 244

Requirements
Python 3.x

paramiko library

Install paramiko:

bash
Copy
Edit
pip install paramiko
How to Run
Download or clone the script.

Open a terminal.

Run:

bash
Copy
Edit
python interface_vlan_config.py
Enter:

Switch IP address

SSH username

SSH password

The script will:

Connect to the switch

Enter configuration mode

Apply access mode and VLAN 244 on ports Gi1/0/1 to Gi1/0/48

Save the configuration

Notes
SSH must be enabled on the switch.

User must have enough privileges to configure interfaces.

You can easily modify the interface range in the script if needed.
