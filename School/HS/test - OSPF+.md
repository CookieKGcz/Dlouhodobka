*Kdy je v OSPF síti vyžadována volba DR a BDR?*
- když jsou OSPF routery připojeny do společné multiaccess sítě
*Která tři tvrzení popisují výsledky volby OSPF procesu v topologii na obrázku?*
![[Pasted image 20241102211712.png]]
- R2 bude vybrán jako DR
- R3 bude vybrán jako BDR
- Router-ID na routeru R4 bude 172.16.1.1
*Jaký krok podnikne OSPF router ihned po navázaní sousedství s jiným routerem?*
- pošle sousedům DBD paket
- zvolí DR a BDR
*Jaký příkaz použijeme k ověření nastavení sousedství s připojeným OSPF routerem?*
- show ip ospf neighbour
*Správce kondiguruje na routeru single area OSPFv2. Jdna ze inzerovaných sítí je 128.107.0.0 255.255.252.0. Jakou wildcard mask správce pro tuto síť použije?*
- 0.0.3.255
*Síťový technik zadává při konfiguraci routeru následující příkazy: R1(config)# router ospf 11 R1(config)# network 10.10.10.0 0.0.0.255 area 0 Co v příkazu představuje číslo 11*
- ID OSPF procesu na R1
*Jaké je pořadí typů paketů používaných OSPF routerem vedoucím k dosažením konvergence?*
- Hello, BDB. LSR, LSU, LSAck
*Jaká je hodnota OSPF cost z routeru B k počítačům v síti 172.16.1.0/24?*
![[Pasted image 20241102212859.png]]
- 65
*Který OSPF paket obsahuje různé typy Link-State Advertisments?*
- LSU paket
*Jaký příkaz je třeba použít po změně hodnoty Router-ID na OSPFv2 routeru HQ?*
- clear ip ospf process
*Jakým příkazem získal správce sítě tento výstup?*
![[Pasted image 20241102213441.png]]
- show ip ospf interface serial0/0/1
*Který krok v OSPF procesu na routeru je charakterizován rozesíláním link-state informací a informací o cenách cest (cost) mezi propojenými routery?*
- exchanging link-state advertisements (váměna LSAs)
*Který krok v OSPF procesu na routeru je charakterizován odesílaním hello paketů na všechna povolená OSPF rozhraní?*
- establishing neighbor adjacencies (vytváření sousedství)
*Pokud nemá router Branch1 ručně nakonfigurováno router-ID, jakou hodnotu router-ID nastaví OSPF proces automaticky?*
![[Pasted image 20241102214056.png]]
- 192.168.1.100
*Jaký příkaz se používá k ověření toho, zda je OSPF proces povolen a jaké sítě propaguje ostatním OSPF routerům?*
- show ip protocols
*Správce sítě nakonfiguroval OSPF timery na zobrazené hodnoty. Jaký je výsledek této konfigurace?*
![[Pasted image 20241102214315.png]]
- Nenaváže se komunikace
*==Jaké dva účely plní router-ID na OSPF routeru?==*
- jednoznačně identifkuje OSPF router v OSPF oblasti
- používá se při výběru DR a BDR
*==Jaká tři tvrzení popisují vlastnosti tabulky topologie v OSPF?==*
- Je to link-state databáze, popisující topologii celé oblasti
- Při konvergenci mají všechny routery v oblasti identické tabulky topologie.
- Tabulku topologie lze zobrazit pomocí příkazu show ip ospf database.
*OSPF router má tři directly connected sítě.. 172.16.0.0/24, 172.16.1.0/24, 172.16.2.0/24. Jaký příkaz je nutné použít pro inzerování pouze sítě  172.16.1.0 sousedním OSPF routerům?*
- network 172.16.1.0 0.0.0.255 area 0
*Které ktři OSPF stavy se týkají navazování sousedství mezi dvěma OSPF routery?*
- Down, Init, Two-way
*Jaká je funkce OSPF hello paketů?*
- Objevovat sousední routery a vytvořit s nimi sousedství.
*Jaké dva účely plní router-ID na OSPF routeru?*
- jednoznačně identifikuje OSPF router v OSPF oblasti
- používá se při výběru DR a BDR
*Který krok v OSPF procesu na routeru popisuje činnost, která vede k naplnění forwarding database?*
- spouštění SPF algoritmu
*Jaký příkaz použije síťový technik k ověření správné konfigurace Hello a Dead intervalů na seriové lince propojující jeho OSPFv2 router s jiným OSPFv2 routerem?*
- show ip ospf interface serial 0/0/0
*Jaká je výchozí hodnota cost na OSPF routeru pro jakoukoliv linku s šířkou pásma 100Mb/s nebp výšší?*
- 1
*Síťový technik na síťovém rozhraní OSPF routeru ručně nakonfiguroval hello interval na 15 sekund. Jaká bude hodnota dead intervalu?*
- 60 sek
*Na kterém OSPF routeru či routerech v OSPF area 0 na obrázku bude nakonfigurována static default route?*
![[Pasted image 20241102220134.png]]
- R0-A
*Co jako první signalizuje OSPF routeru, že soused je nedostupný?*
- router na dané lince nedostává hello pakety
*Správce sítě nakonfiguroval OSPF v2 na obou CISCO routerech. PC1 se ale nemůže připojit k PC2. Jaký je nejpravděpodobnější problém?*
![[Pasted image 20241102220457.png]]
- Rozhraní Fa0/0 na routeru R2 nebylo aktivováno pro použití OSPFv2
*Router je součástí OSPFv2 oblasti. Co se stane , pokud dead interval vyprší předtím, než router přijme Hello paket od sousedního DROTHER routeru?*
- OSPF router odebere tohoto souseda z LSDB.
*Které z těchto hodnot v hello paketech se musí shodovat na obou OSPF routerech, aby navázaly fungující sousedství?*
- OSPF area
- hello interval
- dead interval
*==Pokud se switch restartuje a všechny OSPF routery budou muset obnovit sousedství, které routery se stanou novými DR a BDR?==*
![[Pasted image 20241102221434.png]]
- Router R4 se stane DR a router R1 se stane BDR.
*Co obsahuje OSPF area?*
- Routery, které mají ve svých LSDB stejné informace o stavu linek.
*Jaká je výhoda použití Multiarea OSPF routingu?*
- Změny topologie v jedné oblasti (area) nevyvolá přepočty SPF v jiných oblstech.
*Jakou hodnotu router-ID OSPF router vždy preferuje?*
- IP adresu, která je nakonfigurována pomocí příkazu router-id
*Který typ OSPF paketu obsahuje zkrácená výpis LSDB odesílajícího routeru a je používán příjemcem k porovnání s vlastní LSDB?*
- DBD paket
*Jaká OSPF datová struktura je v okamžiku konvergence identická na všech OSPF routerch oblsti?*
- link-state database
*Předpokládáme, že routery B, C a D mají výchozí hodnotu priority a router A má nastavenou prioriotu 0. Jaký závěr lze vyvodit ohledně procesu volby DR/BDR?*
- Pokud DR selže, novým DR bude router B