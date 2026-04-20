# Network Monitoring
## Active Network Monitoring
- actively sent network probes
- +
	- detailed info
	- various ways of monitoring
- -
	- inserts a traffic into the network
	- the monitoring object is aware of being monitored
- Tools
	- nmap
	- Shodan - https://www.shodan.io/
	- Internet Census -  https://internetcensus2012.github.io/InternetCensus2012/paper.html
### Nmap
- Využívání TCP handshaku s SYN a RST
- -> open ports
- -> OS detection
## Passive Network Monitoring
- monitored only by observation of network traffic at the observation point
- +
	- transparent monitoring
	- does not increase link utilization
- -
	- limited info gathered from data
	- encrypted traffic issues
- Tools
	- Wireshark (tshark), tcpdump
	- Zeek - https://zeek.org/
## Packet Capture
### Network HUBs and Switches
- hub - broadcasts all packets
- switch - corresponding MAC address
- promiscuous mode - captures all frames passing the card interface
### Network TAPS and SPANS
- ![[Pasted image 20260420101720.png|150]]![[Pasted image 20260420101747.png|300]]

- Methods
	- mirroring method - port mirroring or SPAN
	- in-line method - bridging hosts or network taps, hubs
# Intrusion Detection
- intrusion/incident - event on a host or network that violates security policy, or is a threat to put a system in an unauthorized state.
- Intrusion detection - passive network monitoring + analyzing events, to identify and report intrusions.
- IDS - automates event analysis
- IPS - automates active responses to mitigate/stop in-progress attacks
## Architecture of Intrusion Detection Systems (IDS)
- Host-based IDS
	- -> events derived from logs, audit records ...
	- -> centrally collected
- Network-based IDS
	- -> from packets provided at strategic vantage point
	- network wide views
## Intrusion Detection Problem - I
- True Positive - (TP) - intrusion detected
- False Positive - (FP) - false alarm
- False Negative - (FN) - intrusion **missed**
- True Negative - (TN) - normal operation
## Intrusion Detection Problem - II
- Evaluation of Detection Methods
- ![[Pasted image 20260420103009.png|400]]
## Intrusion Detection Methods - I
- Approaches
	- signature-based - detects only already-known attacks
	- specification-based - can detect non-conforming behavior (new attack)
	- anomaly-based - can detect new attacks (anomalies)
# Vulnerability Assessment
- process of identifying, quantifying and prioritizing the vulnerabilities in a system
- Tools
	- reconnaissance tools - network mapping
	- vulnerability scanners - vulnerability scanning
	- penetration testing tools and exploitation toolkits - penetration testing
- -> pen-testing yay
## Network Mapping
- Port Scanning
	- open ports - nmap
	- TCP/UDP connection req - port status open , closed, blocked
- OS and App fingerprinting
	- OS - p0f, nmap
	- open port identifies the service listening, and version
## Vulnerability Scanning
- CVE - common vuln. exposures
	- list of publicly known info-sec vuln.
	- each entry contains an ID number, description, public reference
- examples:
	- Shellshocs
	- Log4Shell
	- Heartbleed
## Vulnerability Scanners
- automated -> from outside -> vuln. and insecure configs. and hosts.
## Penetration Testing
- attempted breach
- Tools
	- metasploit
	- generally Kali
# Network-Based Attacks
## DDoS
- excessive traffic
- goal - disrupt normal operations to make services unavailable to legitimate users.
- botnet -> CnC server ...
	- Volume-based -> UDP floods
	- Protocol-based - SYN floods
	- Aplication-layer-based - HTTP floods
- Impact - service downtime, revenue and rep dmg. Could be high recovery costs
- Mitigations - firewalls, traffic limiting/filtering, and DDoS protection services
## Spoofing
- can create secondary victims
- Ex:
	- SYN flood
		- ![[Pasted image 20260420105923.png|350]]
## DDoS Mitigation - Ingress nad Egress Filtering
- Filters mitigate IP source address spoofing, and thus DoS attacks that employ it (TCP SYN, UDP, ICMP flooding)
## Address Resolution Attacks - ARP Spoofing
- Local network attack - ARP - mapping IPv4 to MAC
- -> MAC flood -> switch functions as a hub
	- traffic sent to everyone connected to the network
- Mitigations -> ARP static entries, switch port sec
## Other ARP shit
- make the attackers MAC (in the hosts system) to be that of a gateway for example
	- classic MitM
