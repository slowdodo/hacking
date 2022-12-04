import dpkt
import netifaces
import socket
import time

# Get local IP address
ip_address = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create DNS response packet with multiple resource records
dns = dpkt.dns.DNS(id=1, qr=1, aa=1, qdcount=1, ancount=3,
                   qd=dpkt.dns.DNSQR(name='www.example.com', type=1),
                   an=[
                       dpkt.dns.DNSRR(name='www.example.com', type=1, ttl=60, rdata=ip_address),
                       dpkt.dns.DNSRR(name='www.example.com', type=28, ttl=60, rdata=ip_address),
                       dpkt.dns.DNSRR(name='www.example.com', type=5, ttl=60, rdata='example.com'),
                   ])

# Send packet repeatedly at 1 second intervals
while True:
    sock.sendto(bytes(dns), ('192.168.1.1', 53))
    time.sleep(1)