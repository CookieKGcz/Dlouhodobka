# Part 1: Review Alerts in Sguil
f)
What kind of transactions occurred between the client and the server in this attack?
- Útočník si vytvořil údaje pro usera myroot v /etc/shadow a v /etc/passwd (pravděpodobně na zpětné připojení)
# Part 2: Pivot to Wireshark
b)
What did you observe? What do the text colors red and blue indicate?
- TCP follow stream s dotazy (commandy) útočníka a odpovědi napadeného zařízení.

The attacker issues the whoami command on the target. What does this show about the attacker role on the target computer?
- Přes jaký účet se dostal do napadeného zařízení. (metasploitable)

Scroll through the TCP stream. What kind of data has the threat actor been reading?
- Data v /etc/shadow (hesla) a v /etc/passwd (údaje o uživatelích).

# Part 3: Pivot to Kibana
e)
What are the source and destination IP addresses and port numbers for the FTP traffic?
- ![[Pasted image 20250404091620.png]]
f)
![[Pasted image 20250404091739.png]]
h)
What are the user credentials to access the FTP site?
- ![[Pasted image 20250404091926.png]]
cleková komunikace s FTP
![[Pasted image 20250404092030.png]]
j)
What are the different types of files? Look at the MIME Type section of the screen.
- ![[Pasted image 20250404092204.png]]

Scroll to the Files - Source heading. What are the file sources listed?
- ![[Pasted image 20250404092313.png]]

i)
What is the MIME type, source and destination IP address associated with the transfer of the FTP data? When did this transfer occur?
- ![[Pasted image 20250404092427.png]]![[Pasted image 20250404092415.png]]
- Došlo 11th June 2020 v 3:53

m)
What is the text content of the file that was transferred using FTP?
- ![[Pasted image 20250404092606.png]]
- CONFIDETIA DOCUMENT
- DO NOT SHARE
- This document contains information about the last security breach.

With all the information has gathered so far, what is your recommendation for stopping further unauthorized access?
- Účet byl napadnut (metasploitable), takže lepší zabezpečení a vyhledal bych si jak přesně se to stalo
- Lepší FTP zabezpečení, aby se nedalo jen tak stahovat.