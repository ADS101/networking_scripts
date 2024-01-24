import subprocess

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

