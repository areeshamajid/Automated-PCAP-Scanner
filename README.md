# Automated-PCAP-Scanner

Automated PCAP Scanner is a Python-based network traffic analysis tool that scans `.pcap` files using PyShark and predefined Wireshark display filters to detect suspicious traffic patterns, reconnaissance activity, scanning behaviour, and selected attack indicators. It is designed to reduce repetitive manual filtering during packet analysis and speed up investigation workflows. 
---
## Overview 
Manually loading a PCAP into Wireshark, trying different display filters, and hunting through results can be slow and repetitive, especially when you want to check for multiple attack patterns. Wireshark’s display filter language is powerful, but you normally have to apply each filter one at a time through the GUI.

Automated PCAP Scanner automates that workflow. It uses PyShark (a Python wrapper for TShark) to run a curated set of Wireshark display filters in a single pass over your capture file, then reports what it finds for each category (reconnaissance, scans, poisoning, flooding, etc.). Instead of spending time typing and re‑typing filters, you run one script and focus on interpreting the results.

This makes it particularly useful for:
- Quickly triaging PCAPs from labs, CTFs, or assignments.
- Getting a fast “first look” at what kind of malicious or suspicious activity may be present.
- Helping beginners see how common attack patterns map to Wireshark display filters.

---

## Features 
- **Automated display filtering**: Runs multiple Wireshark display filters in one go, instead of manually applying them one by one in the GUI, saving time on repetitive analysis work.
 **Reconnaissance & scan detection**: Checks for ARP scans, ICMP ping sweeps, TCP/UDP ping sweeps, SYN/FIN/NULL/Xmas scans, and UDP port scan patterns using ICMP responses.
- **Attack indicators**: Looks for ARP poisoning, ICMP flooding, VLAN hopping hints, and TCP retransmission/loss that might signal instability or scanning side effects.
- **Wireless attack patterns**:Includes filters for de‑authentication, disassociation, fake beacon floods, and authentication DoS in 802.11 captures.
- **Simple to extend**: All detections live in a single Python dictionary of {name: wireshark_display_filter}, so you can add or modify filters without changing core logic.
​- **CLI-friendly**: Works as a simple script: point it at a PCAP, run it, and review the printed results.

---

## Technologies Used

- Python 3
- PyShark
- Wireshark

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/areeshamajid/Automated-PCAP-Scanner
cd Automated-PCAP-Scanner
```

### 2. Install dependencies 
```bash
pip install pyshark
```
### 3. Install Wireshark 
**Ubuntu**
```bash
sudo apt install wireshark
```
**Windows** 
Install Wireshark from the official installer and make sure TShark is included during installation. 

---
## Project Structure

```
Automated-PCAP-Scanner/
│
├── automated_pcap_scanner.py
└──  README.md
```

---

## Usage

> **Note:** This project does not include sample PCAP files. You must provide your own `.pcap` file from Wireshark, tcpdump, a lab environment, or a CTF dataset.

1. Open `automated_pcap_scanner.py` and update the file path:

```python
file_path = "path/to/your/file.pcap"
analyze_pcap(file_path)
```

2. Run the script:

```bash
python automated_pcap_scanner.py
```

The script will loop through all predefined filters, apply each display filter to the PCAP, print the number of matches found, and print packet details for matching packets.

---

## Example Output

```
Running filter: TCP SYN (Stealth) Scan
Found 142 packets for filter 'TCP SYN (Stealth) Scan'

Running filter: ARP Poisoning
Found 3 packets for filter 'ARP Poisoning'

Running filter: ICMP Flooding
No packets found for filter 'ICMP Flooding'
```

---

## Detection Filters

The scanner uses a dictionary of named Wireshark display filters covering a broad range of traffic types and attack patterns.

| Filter Name | Display Filter |
|---|---|
| HTTP Traffic | `http` |
| HTTPS Traffic | `ssl or tls` |
| IP Address Filtering | `ip.addr == X.X.X.X` |
| TCP Port | `tcp.port == 80` |
| UDP Port | `udp.port == 53` |
| ARP Scanning | `arp.dst.hw_mac==00:00:00:00:00:00` |
| IP Protocol Scan | `icmp.type==3 and icmp.code==2` |
| ICMP Ping Sweep | `icmp.type==8 or icmp.type==0` |
| TCP Ping Sweep | `tcp.dstport==7` |
| UDP Ping Sweep | `udp.dstport==7` |
| TCP SYN (Stealth) Scan | `tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size <= 1024` |
| TCP Connect Scan | `tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024` |
| TCP Null Scan | `tcp.flags==0` |
| TCP FIN Scan | `tcp.flags==0x001` |
| TCP Xmas Scan | `tcp.flags.fin==1 && tcp.flags.push==1 && tcp.flags.urg==1` |
| UDP Port Scan | `icmp.type==3 and icmp.code==3` |
| ARP Poisoning | `arp.duplicate-address-detected or arp.duplicate-address-frame` |
| ICMP Flooding | `icmp and data.len > 48` |
| VLAN Hopping | `dtp or vlan.too_many_tags` |
| TCP Packet Loss | `tcp.analysis.lost_segment or tcp.analysis.retransmission` |
| Client De-authentication | `wlan.fc.type_subtype == 12` |
| Client Disassociation | `wlan.fc.type_subtype == 10` |
| Fake AP Beacon Flood | `wlan.fc.type_subtype == 8` |
| Authentication DoS | `wlan.fc.type_subtype == 11` |

---

## Use Cases

- Quickly reviewing suspicious capture files
- Identifying common scan signatures in a lab or test environment
- Automating repetitive filtering tasks during packet analysis
- Learning how Wireshark display filters map to attack patterns
- Supporting basic blue-team and network forensics workflows

---

## Future Improvements

- Add command-line arguments for flexible file input
- Export results to CSV or JSON
- Generate a summary report instead of printing all packet details
- Improve handling for large PCAP files
- Allow optional selection of specific filters at runtime

---

## Disclaimer

This project is intended for **educational, defensive, and authorised analysis purposes only**. Do not use it on systems, networks, or data you do not have explicit permission to inspect. The author accepts no responsibility for misuse.

---

## Author

**Areesha Majid**  
GitHub: [@areeshamajid](https://github.com/areeshamajid)


