import socket

# print /proc/mounts to get the file mounts
prod_mount = "/proc/mounts"
hostnames_file = "/local/hostnames_file"

# find /data/ftp and /data/raw
with open(prod_mount, 'r') as f:
    mounts = [line.split()[1] for line in f.readlines()]

print mounts

with open(hostnames_file, 'w') as h:
    for mount in mounts:
        if mount.__eq__('/data/ftp'):
            # print mount
            hostname = socket.getfqdn()
            # print hostname
            h.write(hostname + "\n")
        if mount.__eq__('/data/raw'):
            # print mount
            hostname = socket.getfqdn()
            # print hostname
            h.write(hostname + "\n")

hostnames = []
# Get unique value from hostnames
with open(hostnames_file, 'r') as g:
    for hostname in g.readlines():
        hostnames.append(hostname.rstrip('\n'))

hostnames_set = set(hostnames)
hostnames_list = list(hostnames_set)


hostnames_list_file = "/local/hostnames_list_file"
with open(hostnames_list_file, 'w') as j:
    for hostname in hostnames_list:
        j.write(hostname + "\n")

