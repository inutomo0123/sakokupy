import ipaddress

a = ['192.168.0.0/24', "192.168.1.0/24",
     '192.168.2.0/24', '192.168.3.0/24',
     '192.168.4.0/24', '192.168.5.0/24']

aa = list(map(lambda x: ipaddress.ip_network(x),a))

print(list(ipaddress.collapse_addresses(aa)))
