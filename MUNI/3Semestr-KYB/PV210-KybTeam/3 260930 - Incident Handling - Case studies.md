- Jan Vykopal
## Spear phishing at MU (2020)
- 16. 4. NÚKIB warning about spear-phishing campaign (threat level High)
	- CSIRT-MU warns admins (MS Teams) and users (web, IS pop-up, FB...) — not legally binding for MU, but prevention
- 19. 4. (Sunday) phishing arrives — "Kalendář plánu mezd 2020", fake `id.muni.cz.<something>.com` URL
### CSIRT-MU actions
- Block phishing domain on university DNS
- Check network data — who accessed the site from MU network?
- Phishing site loaded CSS/JS from MU servers -> HTTP referrer in logs shows victims
	- removed CSS, then injected **JS redirect** to CSIRT-MU warning page if not on muni.cz
- Informed NÚKIB + the 10 users who filled in creds
### Escalation
- Attacker changed passwords in IS, sent ~94k spam mails from 2 accounts
- **Microsoft blocked all MU email** (Friday night, silently)
	- false-positive "compromised admin" detection (audit log bug) + spam detection combined -> whole org blocked
- Weekend recovery, accounts blocked, escalation to management, forensics from many teams (network, IS, mail, web, IdM)
- Attacker kept accessing new accounts -> finally reset passwords of all accounts accessed from any attacker IP
- Closure 11. 5. — ~1 month of work. Is it really over? (unused stolen creds may still exist)
- Attribution hints: Czech IS version, weekends/off-hours, IPs from Nigeria, spam server in USA
### 6 months later
- US DoJ -> Czech police (NCOZ) asks MU for cooperation
- spam was a **smoke screen** for a financial fraud from user2's mailbox
- data still existed only because the incident was archived (normally log rotation / retention would delete it)
### Role of CSIRT
- Coordination inside org, ad-hoc solutions (JS redirect), monitoring + log collection, regulations, communication with externals (police)

## Long-term phishing campaign (APT, 2020–2024)
- Same actor for 4+ years -> APT
- Topics: payroll (almost all ~7000 employees check it monthly), account cancellation, voice mail, meeting reminder
- Sent from compromised accounts at other universities (Amsterdam, Olomouc, Granada, Regensburg...)
- Link text looks legit, real URL hidden under HTML link
- Phishing site = 1:1 copy of IS MU login, static footer date "5. 6. 2020 16:28" reused for years -> fingerprint
- Voice mail HTML attachment with pre-filled name -> 42 accounts compromised
### Attacks from MU
- Compromised MU accounts -> VPN -> (SSH scan + SSH server) -> MU SMTP -> phishing to other universities in their language
- On servers: templates, recipient lists (40–150k addresses), sending script; no persistence, no malware, no data theft
- Goal unclear — farming accounts just to get more accounts
### Defender perspective
- Technical: rate-limit sending mail, enforce **MFA**
- Process: reporting to management, someone has to connect the dots across orgs (GÉANT CERT? NIS2 SOCs?)
- Users: training, simulated phishing

## Discussion of real incidents
- Incident 1 — **data breach** (single org, in-house app, personal data)
	- notify affected, management, DPO + regulator, police, pentest, share lessons learned
- Incident 2 — **cryptomining** on HPC (multiple orgs, SSH + known CVE-2019-15666, unprotected keys)
	- remove access, forensics, educate admins, detection, share IoCs with community, police
- Common: report to authorities, inform users
