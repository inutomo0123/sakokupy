#print("{:08b}".format(30))
#print("{:08b}".format(32))
#print("{:08b}".format(30 & 32))
#print("{:08b}".format(30 | 32))
#print("{:08b}".format(30 ^ 32))

#print(list(map(lambda x: int(x), "192.168.100.10".split("."))))

def get_list(ip):
    return list(map(lambda x: int(x), ip.split(".")))


#ip = get_list("192.168.29.41")
#mask = get_list("255.255.255.0")


def get_net_list(ip, mask):
    return list(map(lambda i, m:
                    i & m,
                    get_list(ip),
                    get_list(mask)))


print(get_net_list("172.31.131.120", "255.255.128.0"))


a = "192.168.0.0"
b = "192.168.3.255"

c = ["192.168.0.0/24",
     "192.168.1.0/24",
     "192.168.2.0/24",
     "192.168.3.0/24"]

aa = get_list(a)
bb = get_list(b)


def get_net(a, b):
    return list(map(lambda a, b:
                    a & b,
                    get_list(a), get_list(b)))


print(get_net(a, b))
