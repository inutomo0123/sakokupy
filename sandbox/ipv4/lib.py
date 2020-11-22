import ipaddress as ipa


def add(start, value):
    '''ipaddressに個数を足す
    '''

    return {'start': start,
            'end': str(ipa.ip_address(start) + value)}


print(add('192.168.0.0', 128))
print(add('192.168.0.0', 4096))

#def subnet(start, value):
#
#    return ipa.ipaddress(start) ^ (ipa.ip_address(strart) + value)
#
#print(subnet('192.168.0.0', 128))


#print(b and a)


#print(ipa.ip_network(a))

c = ipa.ip_address("217.77.224.1")
#print(c.packed)
#print(c + 4096)

d = ipa.ip_network("217.77.224.0/24")
print(d)
print(list(d.subnets()))

e = ipa.ip_network("217.77.225.0/24")
print(e)

print(d and e)
