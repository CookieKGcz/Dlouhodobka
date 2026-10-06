- Jan Vykopal, Pavel Čeleda, Martin Laštovička
## Course organization
- Goal: role and services of a CSIRT in an org, work role of *Incident Response* (NIST NICE ~30 tasks — triage, scope/impact, resolve, coordinate, communicate...)
- Grading: Pass/Fail colloquium
	- 10/15 pts from 3 HWs (no resubmissions)
		- HW1: 23. 9. – 14. 10.
		- HW2: 11. 11. – 25. 11.
		- HW3: 25. 11. – 9. 12.
	- 3 tabletop exercises (TTX) in teams of 3, end of semester (week 12–14)
- Questions during class via Claper (event code `pv210`)
- Related courses: PB177 Cyber Attacks, PA211, PV297, PV280, PV300, PA232 Privacy and Anonymity Technologies

## Incident Handling Demo — DDoS from Eduroam
- Report: hosting of a Czech e-shop got L7 HTTPS flood, sent logs to abuse contact of the IPs (`whois` -> abuse@muni.cz)
- Registration: auto into Request Tracker, gets ID
- Triage: verify in network flows, class. *Availability – DDoS*, priority low, 1 handler
- Analysis: 4 devices in Eduroam, part IPv6-only, need pre-NAT IPs to find users
- Cause: **proxyware** (Honeygain / Repocket) — users install it to earn money, bandwidth gets abused for attacks
- Action: mail users -> uninstall + AV scan, report back in 5 days
- Closure: final class. *DDoS* (orig. report) + *Intrusions – System Compromise* (user tickets)
- Post analysis: proxyware explicitly banned, warning for all users, new detection method

## CSIRT in an organization
- First CERT: CERT/CC 1988 after the **Morris worm** (CMU, funded by DARPA)
- Communities: TF-CSIRT (EU), FIRST (global)
- Regulations
	- CZ: Cybersecurity act 2014, **NÚKIB** (NCISA), GovCERT.CZ (gov + critical infra), CSIRT.CZ (national, rest of internet)
	- EU: NIS (2016) -> **NIS2** (2022), in CZ law new act from 1. 11. 2025; ENISA supports it
### Glossary
- **Mission statement** — what do you do
- **Constituency** — for whom (CSIRT-MU: students + staff, 147.251.0.0/16, 2001:718:801::/48, muni.cz)
- **Sponsorship / Affiliation** — who pays (CSIRT-MU is part of ÚVT/ICS MU)
### CSIRT types by constituency
- National, Government, Military, ISP, Vendor, Commercial, Academic, CSIRT as a Service
- 74 CSIRTs in CZ (Trusted Introducer)
### Properties
- Authority over constituency: full / **shared** (CSIRT-MU) / none
- Place in org: under sysadmins (bad, conflict of responsibility) / management-legal / **standalone unit** (CSIRT-MU)
- Mandate: legal duty / internal directive (MU Directives 9/2017, 10/2017) / good intentions
- Level of support: on site / support (CSIRT-MU helps admins) / coordination
- Business model: 8/5 (min ~4 FTE) vs 24/7 (4x more hours, expensive)
- **CSIRT vs SOC** — CSIRT resolves + prevents + vuln handling + education; SOC detects + monitors (often 24/7)
- **PSIRT** — vulnerabilities in vendor's own products
### CSIRT Services (FIRST framework)
- 5 areas, 21 services, 76 functions — no team does everything, define your subset
	- Information security event management
	- Information security incident management
	- Vulnerability management
	- Situational awareness
	- Knowledge transfer

## Activity: leaked credentials on PasteBin
- Immediate: verify, notify users, reset passwords, ask site to remove, check anomalous logins, inform management, PR
- Preventive: HIBP notifications, pentest, incident response plan
- By law: report under Cybersecurity Act, GDPR -> DPO + supervisory authority
