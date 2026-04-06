import pyshark

filters = {
    "HTTP Traffic": "http",
    "HTTPS Traffic": "ssl or tls",
    "IP Address Filtering": "ip.addr == X.X.X.X",  # Replace X.X.X.X with actual IP
    "TCP Port": "tcp.port == 80",
    "UDP Port": "udp.port == 53",
    "ARP Scanning": "arp.dst.hw_mac==00:00:00:00:00:00",
    "IP Protocol Scan": "icmp.type==3 and icmp.code==2",
    "ICMP Ping Sweep": "icmp.type==8 or icmp.type==0",
    "TCP Ping Sweep": "tcp.dstport==7",
    "UDP Ping Sweep": "udp.dstport==7",
    "TCP SYN (Stealth) Scan": "tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size <= 1024",
    "TCP Connect Scan": "tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024",
    "TCP Null Scan": "tcp.flags==0",
    "TCP FIN Scan": "tcp.flags==0x001",
    "TCP Xmas Scan": "tcp.flags.fin==1 && tcp.flags.push==1 && tcp.flags.urg==1",
    "UDP Port Scan": "icmp.type==3 and icmp.code==3",
    "ARP Poisoning": "arp.duplicate-address-detected or arp.duplicate-address-frame",
    "ICMP Flooding": "icmp and data.len > 48",
    "VLAN Hopping": "dtp or vlan.too_many_tags",
    "TCP Packet Loss": "tcp.analysis.lost_segment or tcp.analysis.retransmission",
    "Client De-authentication": "wlan.fc.type_subtype == 12",
    "Client Disassociation": "wlan.fc.type_subtype == 10",
    "Fake AP Beacon Flood": "wlan.fc.type_subtype == 8",
    "Authentication DoS": "wlan.fc.type_subtype == 11"
}


def analyze_pcap(file_path):
    for name, filter_expr in filters.items():
        print(f"\nRunning filter: {name}")
        cap = None

        try:
            cap = pyshark.FileCapture(file_path, display_filter=filter_expr)
            cap.load_packets()

            if len(cap) > 0:
                print(f"Found {len(cap)} packets for filter '{name}'")
                for packet in cap:
                    print(packet)
            else:
                print(f"No packets found for filter '{name}'")

        except Exception as e:
            print(f"Error with filter '{name}': {e}")

        finally:
            if cap is not None:
                cap.close()


if __name__ == "__main__":
    file_path = "your_file.pcap"  # Replace with your actual PCAP file path
    analyze_pcap(file_path)
