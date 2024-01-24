active_ips = []

with open("active_ips.txt", 'r') as ip_list:
    for line in ip_list:
        active_ips.append(line.strip())

print(repr(active_ips))