from scapy.all import *
# simple script to learn scapy

#load in to memory
packets = rdpcap("2172026_traffic.pcapng")

def packet_overview(packets):
# loop through the packets
    for pkt in packets:
        print(pkt.summary())

# same login applies for other protocols

def http_finder(packets):
    # tcp oriented ? and has to be HTTP via port 80 for verification
    for pkt in packets:
        if TCP in pkt and (pkt[TCP].sport == 80 or pkt[TCP].dport ==80):
            print(pkt.summary())

def dns_finder(packets):
    # UD{} oriented ? and has to be DNS via port 53 for verification
    for pkt in packets:
        if UDP in pkt and (pkt[UDP].sport == 53 or pkt[UDP].dport ==53):
            print(pkt.summary())

def https_finder(packets):
    # tcp oriented ? and has to be HTTPS via port 443 for verification
    for pkt in packets:
        if TCP in pkt and (pkt[TCP].sport == 443 or pkt[TCP].dport ==443):
            print(pkt.summary())













# ------------------ test runs ---------------------
# packet_overview(packets)
http_finder(packets)