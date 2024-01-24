# Script to ping all IP addresses in a /24 subnet
import subprocess
import time
import threading
import os
from scanner_lib import pingHost

# Establishing font colours
RED = "\033[31m"
BOLD = "\033[1m"
WHITE = "\033[0m"

# Get network, start IP and end IP from user
network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
startip = int(input("Enter starting IP: "))
endip = int(input("Enter ending IP: "))
iprange = endip-startip

print(f"\nOkay, pinging all IPs in network {network}, between IPs {startip} and {endip}...")

# Warning for user if they want to scan a large amount of users.
if int(endip)-int(startip) > 40: 
	print("NOTE: Selected port range is large, so prepare for a long wait.")

print(f"\nOkay, pinging all IPs in network {network}...")
threads=100
hostsList = [i for i in range(startip, endip)]
hostsPinged = 0

while hostsPinged < len(hostsList):
    if hostsPinged + threads > len(hostsList):
        threads = iprange - hostsPinged
    for i in range(threads):
        t = threading.Thread(target=pingHost, args=(network, hostsList[hostsPinged+i],))
        t.start()
    t.join()
    hostsPinged = hostsPinged + threads
    print(f"Pinged {hostsPinged}", end="\r")
    time.sleep(.01)

activeHosts = []
with open("active_ips.txt", "r") as ip_list:
    curr_hosts = [line.strip() for line in ip_list]
    for line in ip_list:
        if line.strip() in curr_hosts:
            continue
        activeHosts.append(line.strip())

threads = 3
hostsMapped = 0
print("IP_ADDRESS\tOPEN_PORTS\n")
for host in activeHosts:
    print(f"Pinging IP {host}")
	process_nmap_listed = subprocess.run(["nmap", "-sT", f"{host}"], capture_output=True, text=True).stdout.split("\n")[5:-3]
	print(f"========={BOLD} {host} {WHITE}=========\n")
	if len(process_nmap_listed) > 0:
		for item in process_nmap_listed:
			itemized_port = item.split()
			portno = itemized_port[0]
			service = itemized_port[2]
			str_amap_process = ' '.join(subprocess.run(["amap", "-b", f"{host}", portno], capture_output=True, text=True).stdout.split("\n")[2:-4])
			print(f"{RED}{portno} {WHITE}({service})\n{str_amap_process}\n\n")
	else:
		print(f"\t\tNo open ports.")


	

