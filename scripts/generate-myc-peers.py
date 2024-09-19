# This script just generates a --peers arg for mycelium, currently using IPv4 and TCP only

import json

# Mycelium Public Nodes
with open("./myc-public-peers.json", "r") as file:
    hosts = json.loads(file.read())

ipv4s = [host["IPv4"] for host in hosts]
peers = "--peers "
for ip in ipv4s:
    peers += f"tcp://{ip}:9651 "

print(peers)
