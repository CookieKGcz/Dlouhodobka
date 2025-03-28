# Part 1: Investigate an SQL Injection Attack
## Step 2: Filter for HTTP traffic.
a)
Scroll through the results and answer the following questions: 
What is the source IP address? 
- 209.165.200.227
What is the destination IP address? 
- 209.165.200.235
What is the destination port number?
- HTTP takže 80

c)
What is the timestamp of the first result? 
- JUne 12th 2020, 21:30:09.445
What is the event type? 
- bro_http
What is included in the message field? These are details about the HTTP GET request that was made by the client to the server. Focus especially on the uri field in the message text.
- ![[Pasted image 20250328113905.png]]
- username, cc id, cc number, cc v (? version) z credit cards... a nakonec i heslo
What is the significance of this information?
- prakticky krádež kreditních karet 

## Step 3: Review the results.
d)
What do you see later in the transcript as regards usernames? 
- ![[Pasted image 20250328114558.png]] uživatelské jména a hesla k nim
Give some examples of a username, password, and signature that was exfiltrated
- ![[Pasted image 20250328114705.png]]
- ![[Pasted image 20250328114716.png]]
- ![[Pasted image 20250328114725.png]]
- ![[Pasted image 20250328114743.png]]

# Part 2: Analyze DNS exfiltration.
## Step 2: Review the DNS-related entries.
e)Locate information about the DNS - Client and DNS - Server. Record the IP addresses of DNS client and server.
![[Pasted image 20250328115328.png]]
## Step 3: Determine the exfiltrated data.
c)
![[Pasted image 20250328115719.png]]
Were the subdomains from the DNS queries subdomains? If not, what is the text? 
- CONFIDENTIAL DOCUMENT
- DO NOT SHARE
- This document contains information about the last security breach.

What does this result imply about these particular DNS requests? What is the larger significance?
- exfiltrace dat byla úspěšná a máme další security breach :) (dokud se to nevyřeší další threat actoři mohou exfiltrovat další data) (plus musí se ohlížet také na to, že data byla rozkouskována předtím, než byla poslána zpět útočníkovy)

What may have created these encoded DNS queries and why was DNS selected as the means to exfiltrate data?
- Jelikož DNS provoz je normální, může se použít na utajení nějaké komunikace stejně jako s HTTP provozem atd.
- Proč jsou vytvořeny -> může být nějaký virus či komplexní útok na nějakou zranitelnost hosta