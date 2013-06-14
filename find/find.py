import punch.ping.ping as ping
import select
import socket
import punch.ping.icmp as icmp
import punch.find.candidate as candidate

class Finder(candidate.Candidate):

    Packet = icmp.Echo

    def candidates(self):
        candidates = []
        while 1:
            rd, wt, er = select.select([self.sock.socket], [], [], 0)
            if rd:
                pkt, who = self.sock.recvfrom(4096)
                candidates.append(who[0])
            else:
                break
        return candidates


def test_ping_works(host = 'twitter.com'):
    import time
    name, alias, ips = socket.gethostbyname_ex(host)
    print('ping host {} '.format(name))
    if alias: print(alias)
    print('ips: {}'.format(ips))
    ip = ips[0]
    f = Finder(ip)
    while 1:
        f.send()
        time.sleep(0.5)
        candidates = f.candidates()
        print(candidates)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        args = (sys.argv[1],)
    else:
        args = ()
    test_ping_works(*args)#'1.2.3.4')
