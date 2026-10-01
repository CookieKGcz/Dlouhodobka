- about second and third in the 15 tactics
# Resource Development
## Resource Dev
- adversaries creating, purchasing compromising/stealing resources that can be used ti support targeting.
- Example for other use in cycle:
	- CnC from purchased domains
	- using email accounts for phishing as a part of Initial access.
	- stealing code signing certificates to help with defense evasion.
## Techniques
- https://attack.mitre.org/tactics/TA0042/
## Acquire Access
- Obtaining an existing access to targeted system.
- Online services available to sell access to previously compromised systems.
- Variety of forms:
	- planted backdoors
	- external remote service (VPN, VNC, RDP, SSH)
- Cannot be detected nor mitigated (takes place outside of org)
## Acquire Infrastructure
- Buying, leasing, renting, or obtaining infrastructure which can be used during targeting.
- Include:
	- physical / cloud services
	- domains
	- third-party web services.
- Helps with staging, launching and executing the operation.
- Examples:
	- renting a botnet
	- setting up Google Drive to host malicious download
	- using GitHub to host malware linked in spearphishing e-mails.
- Cannot be easily detected or mitigated
- related: https://attack.mitre.org/techniques/T1584/
## Establish Accounts
- used to build a persona to further operations
- Development of public information, presence, history and appropriate affiliations.
- Detection: only monitoring social media activity related to your org
- Mitigation: difficult, outside of the scope of enterprise defenses and controls
- related: https://attack.mitre.org/techniques/T1586/
## Develop Capabilities and Obtain Capabilities
- Capabilities are malware, software (including licenses), exploits, code-signing and SSL/TLS certs, and information relating to vulnerabilities.
- These techniques are building capabilities in-house (Develop) or purchasing, freely downloading, or stealing them (Obtain)
- Cannot be detected nor mitigated
## Stage Capabilities
- uploading, installing, or setting up capabilities
- staged on infrastructure
- Examples:
	- staging web resources for a link target to be used with spearphishing
	- upload malware tools to a location accessible to a victim network
# Initial Access
## Initial Access
- various entry vectors to gain initial foothold within the network
- -> limited-used or continued access
## Content Injection
- injecting malicious content into systems through online network traffic
- manipulating traffic to inject their own content
- example: injecting content into DNS, HTTP, SMB
- Detection: unusual network traffic, sus files written to disk
- Mitigation: traffic encryption, restriction of web-based content
## Drive-by compromise
- gaining access to a system through a user visiting a website over the normal course of browsing
- users web browser is typically targeted for exploitation
- Detection:
	- abnormal behaviors of browser processes, inspect URLs for potentially known-bad domains or parameters, new files written to disk, new network connections to untrusted hosts or delivering known malicious scripts
- Mitigation:
	- isolating or sandboxing, restriction of web content
- Difficult for attackers
## Exploit Public-Facing Application
- exploiting a weakness in an internet-facing host
- mainly web servers
- Very common and frequently used
- Tools: Hydra, Medusa, Ncrack, Metasploit, sqlmap, wpscan, burp, nikto,....
- Detection:
	- web app firewalls -> improper inputs in logs, deep packet inspection
- Mitigation:
	- updating, network segmentation, isolation, least privilege for service accounts, vuln scanning
## External Remote Services
- Leveraging external-facing remote services
- such as vpns, vncs
- Attacker usually must use valid credentials of existing accounts
- Detection:
	- auth loags
	- analyze for unusual access patterns
	- windows of activity
	- monitoring network traffic of remote services
- Mitigation:
	- Disable unnecessary remotely available services or limit access to hem through centrally managed concentrators
	- MFA
## Hardware Additions
- Accessories, network hardware
- MitM things
- examples: USB rubber ducky, LAN Tap
- Detection:
	- Configuration management databases (CMDB)
	- detection of computer systems of network devices
	- monitor for newly constructed drives
- Mitigation:
	- network access control policies (802.1x)
	- block unknown devices
## Phishing
- sending messages to gain access to victim system
- Detection:
	- sus email activity
	- references to uncategorized or known-bad sites
	- call logs from corporate devices
	- monitor for newly constricted files from a phishing messages to gain access to victim systems
- Mitigation:
	- Antivirus/Antimalware - quarantine sus files
	- Audit, IPS, Restrict web-based content, software config, user training
## Replication Through Removable Media
- copying malware to removable media and taking advantage of autorun features
## Supply Chain Compromise
- manipulation of products or product delivery mechanisms prior to receipt by a final consumer
## Trusted Relationship
## Valid Accounts
##