import subprocess
RED = "\033[31m"
BOLD = "\033[1m"
WHITE = "\033[0m"

listed_process = subprocess.run(["nmap", "-sT", "192.168.1.100"], capture_output=True, text=True).stdout.split("\n")[5:-3]
output = "IP_ADDRESS\tOPEN_PORTS\n"
output+=f"========= {BOLD} 192.168.1.100 {WHITE}=========\n\n"
for item in listed_process:
	itemized_port = item.split()
	portno = itemized_port[0]
	service = itemized_port[2]
	str_amap_process = ' '.join(subprocess.run(["amap", "-b", "192.168.1.100", portno], capture_output=True, text=True).stdout.split("\n")[2:-4])
	output+=f"{RED}{portno} {WHITE}({service})\n{str_amap_process}\n\n"
print(output)

