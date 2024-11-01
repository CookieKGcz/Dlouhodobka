# Upgrade
Kdy?
- oprava známého problému
- nová funkcionalita
- vylepšení výkonu

## Stažení
- pohled Files -> po restartu se načte
- ![[Pasted image 20241023124228.png]]
## Kontrola
- System > Packages
## Auto Upgrade
- System > auto-upgrade

## ==Manuální==
Třeba zjistit architekturu zařízení (==mipsbe==, ppc, x86, mipsle, tile)
![[Pasted image 20241023124607.png]]
Druhy souborů pro upgrade:
- ==NPK== (základní)
- ZIP
### **Provedení**
1. Nahrát  soubory prostřednictvím pohledu "Files"
	1. přetažením / soubor
2. Provést restart
	1. V případě Downgrade (System > Packages)
3. Ověřit načtení nové verze
	1. System > Packages
4. Provést upgrade zavaděče
	1. System > RouterBOARD
#### **Upgrade Zavaděče**
1. Kontrola curr
	1. System > RouterBOARD
2. spouštění vlastního upgrade
	1. System > Routerboard > Upgrade
3. Restart
	1. System > reboot
# Správa
## Uživatelé
- Pohled System > Users
	- i skupin
- Záložky Users Groups
![[Pasted image 20241023131738.png]]
## IP služeb
- Omezení využívání sys prostředků
- Omezení bezpečnostních rizik (otevřené porty)
- Omezení IP
- IP > Services
## Zálohy
- Binární záloha
	- kompletní záloha systému (obsahuje i hesla)
	- obnovení ze zálohy se uskuteční na stejném zařízení
- ==Export konfigurace (má textovou podobu)==
	- úplná nebo částečná záloha
	- generuje soubor se skriptem nebo zobrazí export v konzoli
1. Files Backup (název v "Rx-login")
2. Restore

export
1. Terminal
2. export
3. export file=Rx-login
4. zase ve files
(2 je bin)
![[Pasted image 20241023133535.png]]

## Archivace
