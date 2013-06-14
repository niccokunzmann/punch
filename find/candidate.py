import punch.ping.icmp as icmp
import punch.find.raw_socket as raw_socket
import socket


class Candidate:

    Packet = icmp.Unreachable

    def __init__(self, addr):
        self.sock = raw_socket.RawSocket(addr)
        self.id = 1234 # maybe changable
        self.seq = 1234 # maybe changable
        self.addr = addr

    def send_packet(self):
        pkt = self.Packet()
        pkt.id = self.id
        pkt.seq = self.seq
        pkt.data = b'python pinger'
        buf = pkt.assemble()
        self.sock.sendto(buf)
        self.plen = len(buf)

    def send(self):
        """send a packet to the outside."""
        self.send_packet()

def test_answer_ping(host = socket.gethostbyname(socket.gethostname())):
    import time
    print('answering to {}'.format(host))
    c = Candidate(host)
    while 1:
        c.send()
        time.sleep(0.3)
        print('sent')

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        args = (socket.gethostbyname(sys.argv[1]),)
    else:
        args = ()
    test_answer_ping(*args)#'1.2.3.4')
