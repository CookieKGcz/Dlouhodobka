## poznámky/linky:
### Zpracování

Zatím zpracováno podle topologie s třemi routery
![[Pasted image 20241123211956.png]]

Podle topologie mám rozvržené dva útoky 
- útok **HTTP** na Server 1 s Apache webovou službou 
- útok typu **SYN flood** na DNS bind9 Server 2

Pro boty a victim servery používám alpine linux, kvůli jeho minimálním potřebám na systém https://alpinelinux.org/downloads/.
Pro útočníka, základní Kali linux.
A pro simulování internetu/(síť jako mezi-bod) používám RouterOS od MikroTiku.

#### Komunikace
Pro komunikaci používám vnitřní sítě - např.: mezi Routery R1 a R2 je vnitřní síť intnetR1_R2, nebo mezi R1 a Kali je vnitřní síť intnetToKali
- viz všechny sítě na R1![[Pasted image 20241110165143.png]]
Také všechny routery mají nastavené bridge interface pro přímou komunikaci s počítačem (hlavně pro bezproblémové připojení s WinBox)

A specificky na R1 je nastavená NAT, která poskytuje komunikaci do internetu pro celou topologii, a ještě DHCP client, pro IPv4 adresu od locálního/domácího routeru
- Dynamic a Static Routy na R1![[Pasted image 20241110165725.png]]
- IP na R1                                                           ![[Pasted image 20241110165812.png]]
- src-nat na R1![[Pasted image 20241110170050.png]]
- ověření - traceroute z kali na seznam.cz![[Pasted image 20241110170548.png]]

Komunikace mezi sítěmi 

#### Útoky
1. HTTP flood as botnet - útok na apache server
	-  LOICo?
		- ![[Pasted image 20241108210738.png]]
	- scapy
		- ![[Pasted image 20241108210617.png]]
	- Socks5 requests
1. **SYN flood**/UDP flood/ICMP flood?
	- hping3?
		- ![[Pasted image 20241108210703.png]]
	- scapy
		- ![[Pasted image 20241108210617.png]]
### Okrajové
#### diagram/topologie
Internet - Router OS
##### Simple
![[Pasted image 20241101230930.png]]
##### More Realistic
![[Pasted image 20241108224414.png]]
![[Pasted image 20241108224415.png]]



server s ip 176.16.1.20 je nově na .21 (ubuntu server)
![[Pasted image 20241110170945.png]]

Taky zvážit jestli mít jiný server na DNS![[Pasted image 20241110170946.png]]


## Commands used for initial configuration
### ==DNS server==
!!
debian ---- debian
!!
`vi /etc/network/interfaces`
![[Pasted image 20241123173735.png]]
`service reboot networking` or `service networking reboot`


`apk add bind`
`apk add bind-utils`


`vi /etc/bind/named.conf.options`
![[Pasted image 20241123211714.png]]
`vi /etc/bind/named.conf.local`
![[Pasted image 20241123211731.png]]
`vi /etc/bind/db.victim.com`
![[Pasted image 20241123211826.png]]
`vi /etc/bind/db.1.16.176.in-addr.arpa`
![[Pasted image 20241123211810.png]]

`vi /etc/bind/named.conf`
![[Pasted image 20241123211900.png]]

==IF== firewall is active
`firewall-cmd --permanent --add-service=dns
`firewall-cmd --reload`


Restarting
`service bind start` ==\_\_\_\_\_\_?\_\_\_\_\_\_==
`service named start` ==\_\_\_\_\_\_?\_\_\_\_\_\_==
`sudo systemctl restart/start named`

curr. problem on alpine
![[Pasted image 20241123174746.png]]

**switched to UBUNTU**
`/etc/init.d/named status` resolve success
![[Pasted image 20241123211257.png]]
![[Pasted image 20241123211346.png]]
![[Pasted image 20241123212150.png]]
![[Pasted image 20241123212228.png]]
### Apache/HTTP server
`vi /etc/network/interfaces`
![[Pasted image 20241123211443.png]]
 `apk add apache2`those not needed? `php7-apache7 php7-gd`
  
 `vi /etc/apache2/http.conf`
 ![[Pasted image 20241123175655.png]]
  `vi /var/www/localhost/htdocs/index.html`
  ![[Pasted image 20241123180143.png]]
  `/etc/init.d/apache2 start`
![[Pasted image 20241123180416.png]]
### Bots
!!
root --- alpine
!!
`vi /etc/network/interfaces`
+==dns==
![[Pasted image 20241123180650.png]]
`reboot` just reboot it for g.m.
### Kali
![[Pasted image 20241123223200.png]]

## Attacks
### LOIC?
#### installation
`sudo apt install monodevelop` or `mono-devel` ==or== `mono-complete`
`git clone https://github.com/nicolargo/loicinstaller.git`
`chmod 777 loic.sh`
`./loic.sh install`
`./loic.sh update`
`cd LOIC`  
`./loic.sh run`
![[Pasted image 20241123231138.png]]

### Scapy? - HTTP
### Hping3?
### Scapy? - TCP




# Zkráceně proces
![[Pasted image 20250217181049.png]]
1. Malware -import> victim, ten spustí script, který kontaktuje CnC server (ten si to uloží do "databáze")
2. Bot začne "Beaconing", každou x dobu se koukne jestli nemá další instrukce
3. Server odpoví HTTP zprávou na x port ig
DONE
![[Pasted image 20250217133223.png]]
![[Pasted image 20250217133236.png]]
![[Pasted image 20250217133300.png]]
![[Pasted image 20250217172733.png]]
![[Pasted image 20250217172756.png]]

1. Další krok je dát jak bot_beacon, tak i script na CnC(který by měl getovat payload) do CRONtabů.
2. Dále Udělat script na HTTP GET flood a TCP SYN flood

https://raspberrypi.stackexchange.com/questions/4123/running-a-python-script-at-startup
![[Pasted image 20250219155504.png]]

![[Pasted image 20250219171740.png]]
 +startupbind

TODO
- na bots zavést beacon na startup a udělat script na listening -> od cnc
- na cnc udělat script který pošle message všem botům aby zapli beacon
![[Pasted image 20250220160644.png]]
![[Pasted image 20250220160702.png]]
![[Pasted image 20250220162316.png]]

TODO
- HTTP flood script
- Do smth about the bandwidth problem
![[Pasted image 20250226221315.png]]
- na botb.py scriptu payload.py dát jako absolutní cestu




### Redoing routers to ubuntu vms
![[Pasted image 20250303174914.png]]




![[Pasted image 20250308182134.png]]
![[Pasted image 20250308182354.png]]
