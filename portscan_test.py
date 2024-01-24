import subprocess


listed_process = subprocess.run(["nmap", "-sT", "192.168.1.100"], capture_output=True, text=True).stdout.split("\n")[5:-3]
output = "IP_ADDRESS\tOPEN_PORTS\n"
output+="192.168.1.100\t"
for item in listed_process:
	itemized_port = item.split()
	portno = itemized_port[0]
	service = itemized_port[2]
	output+=f"\t{portno} ({service})\n"
print(output)
	
