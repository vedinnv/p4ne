from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self ):
        IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False)
    def regular(self):
        return self.is_global and not self.is_loopback and not self.is_multicast and not self.is_link_local and not self.is_reserved


#проверка конструктора класса
#random_network = IPv4RandomNetwork()
#print(random_network)

networklist = []

for i in range(0, 50):
    rand_net = IPv4RandomNetwork()
    if rand_net.regular():
        networklist.append(str(rand_net))

print(networklist)