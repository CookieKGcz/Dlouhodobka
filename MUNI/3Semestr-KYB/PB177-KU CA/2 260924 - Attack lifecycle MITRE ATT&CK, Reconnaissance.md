## Attack Lifecycle
- complex attacks -> several steps to accomplish goal
### Cyber Kill Chain
- **Reconnaissance** (harvesting email addresses, discover internet-facing servers)
- **Weaponization** - Prep (selecting backdoor implant and appropriate cnc infrastructure for operation)
- **Delivery** - Launch of the operation (malicious email, compromised websites)
- **Exploitation** - Gaining access to victim (opening attachment of malicious email, visiting the compromised website)
- **Installation**
- **CnC** - Remote controlling of the implants
- **Action on objectives** (exfiltrating sensitive information)
## MITRE ATT&CK
- focus: how adversaries interact with systems
### Components
- Tactics - why
- Techniques - how
- Sub-techniques
- Procedures - specific implementations and uses of (sub)techniques in the real world
### Enterprise tactics
- 15 total:
	1. Reconnaissance
	2. Resource Development
	3. Initial Access
	4. Execution
	5. Persistence
	6. Privilege Escalation
	7. Stealth
	8. Defense Impairment
	9. Credential Access
	10. Discovery
	11. Lateral Movement
	12. Collection
	13. CnC
	14. Exfiltration
	15. Impact
### Enterprise (sub)techniques
- 222 tech and 475 sub-tech
- example: Phishing for Information
	- -> Spearphishing Service, Attachment, Link, Voice
### Use cases
- **Detection and Analysis**
- **Threat Intelligence** - analyst can use a common lang to structure, compare, and analyze threat Intelligence
- **Adversary Emulation and Red Teaming** - red teams can use a common lang and framework to emulate specific threats and plan their operations
- **Assessment and Engineering** - assessing the organizations capabilities and driving engineering decisions, - what tools and logging should be implemented
## Selected MITRE ATT&CK techniques - Reconnaissance
### Recon
- Actively or passively gather information that can be used to support targeting
- info used in other phases of the lifecycle (like initial access, prioritization of objectives...)
- Can be detected but not easily mitigated
	- one way - minimizing the amount and sensitivity of data available to external parties
### Active Scanning
- via network traffic - Scanning IP blocks, Vulnerability Scanning, Wordlist Scanning
#### Scanning IP Blocks
- TCP, UDP, ICMP - waiting for host response
- Horizontal - sending requests to the same port on different hosts
- Vertical - sends req. to different ports on the same host

- Tools: Nmap
- Detection: Monitoring network devices fot uncommon fata flows (may have high false positives)
- Mitigation: Blocking some host response (such as ICMP replies)
#### Wordlist Scanning
- Iterative probing of infrastructure using brute-forcing and crawling techniques
- The goal is identification of content and infrastructure
	- Enum web pages and directories, public buckets on cloud infrastructure

- Tools: dirb, DirBuster, Gobuster, yes3-scanner
- Detection: analysis of network traffic and apps logs
- Mitigation: removing or disabling access to any systems, resources, and infrastructure that are not explicity required to be available externally
#### Vulnerability Scanning
- Checks if the configuration of target host/application align with the target of a specific exploit
- Software and version nums, via server banners, listening ports, or other network artifacts

- Tools: Nmap, Metasploit, Nessus, OpenVAS
- Detection: Analysis of network traffic content and flow
- Mitigation: Minimizing the amount and sensitivity of data available to external parties
### Gather Victim Network Info
#### DNS
- can include:
	- registered name servers, records that outline addressing for targets subdomains, mail servers, and other hosts
	- DNS, MX, TXT and SPF records may reveal the use of third-party cloud and SaaS providers, such as Office 365 or Google Suite
	
	- Tools: dig, nslookup, dnsdumpster
	- Detection: hard to distinguish between legitimate traffic and recon
	- Mitigation: cannot be easily mitigated
#### Phishing for Information
- to elicit sensitive info
- Tools? Evilginx, GoPhish
- Detection: monitoring network and logsss
- Mitigation: use anti-spoofing and email authentication mechanisms to filter messages based on validity checks