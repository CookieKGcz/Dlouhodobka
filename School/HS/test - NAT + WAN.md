# NAT
1. Správce sítě chce zobrazit aktivní překlady NAT na hraničním routeru. Který příklad by tento úkol splnil?
	1. show ip nat translations

2. Co je třeba udělat k dokončení konfigurace statického NAT na zařízení R1?![[Pasted image 20250222160540.png]]
	1. Rozhraní S0/0/0 by mělo být nakonfigurováno příkazem ip nat outside

3. Jakou výhodu poskytuje NAT64?
	1. Umožňuje připojit hostitele IPv6 k síti IPv4 převodem adres IPV6 na adresy IPv4

4. Které tvrzení přesně popisuje dynamický NAT?
	1. Poskytuje automatické mapování vnitřních (inside local) na vnitřní globální (inside global) IP adresy.

5. Jaké dva úkony je třeba provést při konfiguraci statického NAT?
	1. Přiřadit zúčastněným rozhraním vnitřní (inside) nebo vnější (outside) roli.
	2. Vytvořit mapování mezi vnitřní lokální (inside local) a vnitřní globální (inside global) adresami.

6. Jaká je nevýhoda NAT?
	1. Není k dispozici možnost koncové (end to end) komunikace.

7. S ohledem na uvedené příkazy, kolik hostů ve vnitřní LAN připojené k R1 může současně komunikovat?![[Pasted image 20250222163012.png]]
	1. 1

8. Jakého typu je adresa 10.131.48.7?
	1. Privátní

9. Jaký překlad adres provádí statický NAT?
	1. **Vnitřní lokální** adresa je přeložena na zadanou **vnitřní globální** adresu

10. Jakou zdrojovou adresu budou mít pakety, které odcházejí z routeru R1 do internetu?![[Pasted image 20250222163555.png]]
	1. 209.165.200.255

11. Je pravdou, že při implementaci NAT pomocí klíčového slova \*\*Overload*\* je každá IP adresa hostitele ve vnitřní síti přeložena na IP adresu platnou ve vnější síti, která je jedinečná pro každého takového hostitele (je tedy mezi nimi vztah jedna k jedné)?
	1. ne

12. Je pravdou, že tunelovací protokoly (např. IPsec), mnohdy nefungují spolu s NAT?
	1. ano

13. PC1 má IP adresu 192.168.10.10 a je připojen k LAN organizace za routerem R1 s veřejným rozhraním IP adresy 209.165.200.226. Webový server na internetu má IP adresu 209.165.201.10. Jaký druh NAT adresy je IP adresa PC1?
	1. Inside Local

14. Poskytovatel internetového připojení (IPS) přidělil společnosti blok IP adres 203.0.113.0/27 Společnost má více než 6000 vnitřních zařízení. Jaký druh NAT by byl nejvýhodnější pro zajištění internetové konektivity?
	2. PAT s použitím poolu adres

15. PC1 má IP adresu 192.168.10.10 a je připojen k LAN organizace za routerem R1 s veřejným rozhraním IP adresy 209.165.200.226. Webový server na internetu má IP adresu 209.165.201.10. Jaký druh NAT adresy je IP adresa Webového serveru?
	1. Outside global

16. Správce sítě nakonfiguroval R2 pro PAT. Proč je konfigurace nesprávná?![[Pasted image 20250222164753.png]]
	1. NAT-POOL2 je přiřazen k nesprávné ACL.

17. PC1 má IP adresu 192.168.10.10 a je připojen k LAN organizace za routerem R1 s veřejným rozhraním IP adresy 209.165.200.226. Webový server na internetu má IP adresu 209.165.201.10. Na jaký druh adresy byla IPv4 adresa pro PC1 přeložena?
	1. Inside Global

18. Jaké označení použije NAT pro globálně routovatelnou IPv4 adresu cílového hosta na internetu?
	1. outside global

19. Na routerech RT1 a RT2 je nokonfigurován NAT. Počítáč posílá požadavek na webová server. Jaká je IPv4 adresa zroje v paketu mezi RT2 a webovým serverem?![[Pasted image 20250222165507.png]]
	1. inside global RT1 - 209.165.200.245

20. Je pravdou, že vedlejším efektem NAT je skutečnost, že skrývá IP adresu hostitele ve vnitřní síti před hostiteli ve vnější síti?
	1. ano

21. Je pravdou, že použití NAT usnadňuje koncovou (end to end) dohledatelnost zdroje a/nebo cíle?
	1. ne

22. Jaký je účel klíčového slova "overload" v příkazu "ip nat inside source list 1 pool NAT_POOL overload"
	1. Umožňuje mnoha vnitřním hostům sdílet jednu nebo několik globálních vnitřních adres

23. Z perspektivy R1 routeru s aplikovaným NAT, která adresa je inside global adresa?![[Pasted image 20250222170050.png]]
	1. 209.165.200.225

24. Zvolte dvě pravdivá tvrzení vyjadřující výhodu či nevýhodu nasazení IPv4 NAT v síti.
	1. NAT přináší problémy pro některé aplikace, které vyžadují end to end spojení.
	2. NAT poskytuje řešení, jak zpomalit vyčerpání veřejných IPv4 adres.

25. Konfiguruje se statický NAT tak, aby umožnil přístup PC1 k webovému serveru v interní íti. Jaké dvě adresy je třeba dosadit na místo A a B pro dokončení konfigurace statického NAT?![[Pasted image 20250222170507.png]]
	1. A = 10.1.0.13
	2. B = 209.165.201.1

# WAN
1. Jaký druh fyzického média používají WAN poskytovatelé k přenosu dat s využitím SONET, SDH a DWDM?
	1. optické vlákno

2. Které dvě tvrzení o fyzické vrstvě (L1) sítí WAN jsou pravdivá?
	1. Popisuje elektrické, mechanické a provozní součásti potřebné k přenosů bitů.
	2. Zahrnuje protokoly jako SDH, SONET a DWDM

3. Městská autobusová společnost chce uživatelům cestujícím v autobusech nabídnout možnost internetového připojení. Které dva druhy WAN infrastruktury by splňovali tyto požadavky?
	1. public infrastructure
	2. cellular

4. Který druh topologie popisuje způsob přenosu dat (virtuální spojení) mezi zdrojem a cílem?
	1. logická topologie

5. Který možnost připojení WAN je založena na technologii Ethernet v sítích LAN?
	1. Metro Ethernet

6. Společnost zvažuje aktualizaci WAN připojení kampusu. Jaké dvě WAN technologie je možné použít pro vytvoření privátní architektury WAN?
	1. Ethernet WAN + MPLS
	2. pronajatá linka

7. Jaká je doporučená technologie pro realizaci spojení prostřednictvím existující veřejné infrastruktury WAN, pokud je třeba zabezpečeným způsobem připojit např.: pobočku k centrále společnosti?
	1. VPN

8. Podnik má 4 pobočky. Centrála potřebuje plnou konektivitu do všech poboček. Pobočky však nemusí být propojeny přímo mezi sebou. Která topologie WAN je nejvýhodnější?
	1. hub-and-spoke

9. Která situace popisuje přenos dat prostřednictvím WAN připojení?
	1. Zaměstnanec sdílí databázový soubor s kolegou, který pracuje v pobočce v jiném městě.

10. Který termín WAN definuje bod, ve kterém se zákaznická přípojka připojuje k síti poskytovatele služeb?
	1. demarkační bod

11. Na jaké vrstvy OSI modelu patří protokoly, které nabízejí provozovatelé WANs pro realizaci svých služeb?
	1. fyzická
	2. linková

12. Které dvě možnosti popisují vlastnosti sítí WAN?
	1. WAN poskytuje síťové služby v rozlehlých zeměpisných oblastech.
	2. Služby sítí WAN jsou poskytovány za poplatek.

13. Jaká topologie sítě WAN je nejvíce odolná proti selhání ?
	1. full mesh

14. Která techologie optických vláken zvyšuje kapacitu přenosu dat využitím současného přenosu optických signálů různých vlnových délek v témže vláknu?
	1. DWDM

15. Jak se nazývá řešení pro sítě WAN, které  používá štítky (labels) ke směřování paketů skrze síť poskytovaltelů?
	1. MPLS