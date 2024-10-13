## Možnosti konektivity
- WinBox
	- doporučeno IP (L3)
	- MAC (někdy může blbnout)(L2)
	- RoMON (L2 a L3)
![[Pasted image 20241009133356.png]]

## Web prohlížeč
![[Pasted image 20241009140912.png]]

Také připojení přes seriový port, **ssh**, telnet

Nápověda ==F1== / ==Tab==


## Obnovení výchouí konf tlačítkem ZAKÁZÁNO
- připojit napájení
- hned poté stisknout a držet RESET
- až zabliká kontrolka active, tlačítko uvolnit

## ==Prázdná konfigurace==
system > reset config
zaškrtnout **No Default Conf** a **Do Not Backup**
provést restart
![[Pasted image 20241009143511.png]]

## Pojmenování zařízení
System > Identity
ve tvaru **Rx-login (x je naše pracoviště (11))**

## Zproveznění IP
IP > Adresses
ve tvaru **10.x.0.1 / ==24==** (x je naše pracoviště (11))
a ether 2

## DHCP
IP > DHCP client
ok

## Firewall - NAT
