from scapy.all import ARP, Ether, srp, conf
import sys
from termcolor import colored

# IP Address for the destination
#target_ip = "192.168.1.1/24"
target_ip = input(colored("Enter Network To Sweep (ex. 192.168.1.1/24): ", 'yellow', 'on_red'))

# create ARP packet
arp = ARP(pdst=target_ip)

# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# stack them
packet = ether/arp

# send packet
result = srp(packet, timeout=3)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print(colored("Available Devices On The Network:", 'yellow'))
print("")
print(colored("IP" + " "*18+"MAC", 'cyan'))
for client in clients:
    print(colored("{:16}    {}".format(client['ip'], client['mac']), 'green'))

