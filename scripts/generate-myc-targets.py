import json

# Mycelium Public Nodes
with open("./myc-public-peers.json", "r") as file:
    hosts = json.loads(file.read())

# Generate mycelium IP targets
for host in hosts:
    print(f"++ Mycelium_{host['Node ID']}_{host['Region']}")
    print(f"menu = Mycelium {host['Node ID']} {host['Region']} IPv4")
    print(f"title = Mycelium {host['Node ID']} {host['Region']} IPv4")
    print(f"host = {host['Mycelium IP']}")
    print()

# Generate IPv4 targets
for host in hosts:
    print(f"++ Mycelium_{host['Node ID']}_{host['Region']}_IPv4")
    print(f"menu = Mycelium {host['Node ID']} {host['Region']} IPv4")
    print(f"title = Mycelium {host['Node ID']} {host['Region']} IPv4")
    print(f"host = {host['IPv4']}")
    print()
