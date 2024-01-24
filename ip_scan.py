# Script to ping all IP addresses in a /24 subnet
import subprocess
import time
import threading
import os


def pingHost(network, host):
    active_hosts = []
    # Iterate over all usable IPs in this subnet
    #for host in range (startip, endip):
    attemptedHostPings = ""
    process = subprocess.run(["ping", "-c", "2", f"{network}.{str(host)}"], capture_output=True, text=True)
    exitcode = process.returncode 
    # If ping was successful, add to list of active hosts.
    if exitcode == 0:
        active_host = f"{network}.{host}"
        with open("active_ips.txt", "a") as ipfile:
            ipfile.write(active_host + "\n")
            ipfile.close()


# Get network, start IP and end IP from user
network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")

print(f"\nOkay, pinging all IPs in network {network}...")
threads=100
hostsList = [i for i in range(254)]
hostsPinged = 0

while hostsPinged < len(hostsList):
    if hostsPinged + threads > len(hostsList):
        threads = 254 - hostsPinged
    for i in range(threads):
        t = threading.Thread(target=pingHost, args=(network, hostsList[hostsPinged+i],))
        t.start()
    t.join()
    hostsPinged = hostsPinged + threads
    print(f"Pinged {hostsPinged}", end="\r")
    time.sleep(.01)


with open("active_ips.txt", "r") as ip_list:
    print(ip_list.read())
    ip_list.close()
