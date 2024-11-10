## poznámky/linky:
### Zpracování

Zatím zpracováno podle topologie s třemi routery
![[Pasted image 20241110164209.png]]

Podle topologie mám rozvržené dva útoky 
- útok **HTTP** na Server 1 s Apache webovou službou 
- útok typu **SYN flood** na DNS Server 2

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




![[Pasted image 20241109222603.png]]

Taky zvážit jestli mít jiný server na DNS![[Pasted image 20241110170945.png]]