import socket
import punch.ip
import punch.ping.ip as ip
import punch.access_rights as access_rights

class RawSocket:

    def __init__(self, addr):
        if not punch.ip.is_valid_ipv4(addr):
            raise ValueError('can only use valid ipv4 addresses like 1.2.3.4 but got {}'.format(addr))
        self.dest = (addr, 0)
        self.open_icmp_socket()

    def open_icmp_socket(self):
        with access_rights.ensure_rights:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                        socket.IPPROTO_ICMP)
        self.socket.setblocking(1)

    def sendto(self, packet):
        self.socket.sendto(packet, self.dest)

    def recvfrom(self, maxbytes):
        return self.socket.recvfrom(maxbytes)

