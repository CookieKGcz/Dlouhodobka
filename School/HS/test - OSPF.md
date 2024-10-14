## Obecné - sousedství / LSDB / DR
1. **Který krok podnikne OSPF router ihned po navázání sousedství s jiným routerem?**
	1. pošle sousedům DBD paket.
	2. zvolí DR a BDR.
2. **Kdy je v OSPF síti vyžadována volba DR a BDR?**
	1. když jsou OSPF routery propojeny do společné multiaccess (eth) sítě.
3. **Který krok v OSPF procesu na routeru je charakterizován vytvářením a úpravou link state databáze routeru s pomocí informací z přijatých LSAs?**
	1. vytváření tabulky topologie sítě.
4. **Který krok v OSPF procesu na routeru je charakterizován rozesíláním link-state informací a informací o cenách cest mezi propojenými routery?**
	1. exchanging link state advertisements (výměna LSAs)
5. **Který krok v OSPF procesu na routeru popisuje činnost, která vede k naplnění forwarding database?**
	1. spouštění ==SPF algoritmu==
6. **Jaká tři tvrzení popisují vlastnosti tabulky topologie v OSPF?**
	1. Je to link state databáze, popisuje topologie celé oblasti.
	2. Při konvergenci mají všechny routery v oblasti identické tabulky topologie.
	3. Tabulku topologie lze zobrazit pomocí příkazu show ip ospf database.
7. **Které tři stavy se týkají navazování sousedství mezi dvěma OSPF routery?**
	1. Down
	2. Init
	3. Twoway
8. **Které tři stavy se týkají sync. OSPF databases mezi dvěma OSPF routery?**
	1. ExStart
	2. ExChange
	3. Loading
9. **Který stav je úplný?**
	1. Full
## Area / Multiarea
1. **Co obsahuje OSPF area?**
	1. Routery, které mají ve svých LSDB stejné informace o stavu linek
2. **Jaká je výhoda použití ==Multiarea OSPF== routingu?**
	1. Změny v topologie v jiné oblasti (area) nevyvolá přepočty SPF v jiných oblastech.
## Hello packety
1. **Jaká je funkce OSPF hello packetu?**
	1. Objevovat sousední routery a vytvořit s nimi sousedství.
2. **Který krok v OSPF procesu na routeru je charakterizován odesíláním hello packetů na všechna povolená OSPF rozhraní?**
	1. vytváření sousedů.
3. **Co jako první signalizuje OSPF routeru, že soused je nedostupný?**
	1. router na dané lince nedostává hello packety.
4. **Hello timer musí být stejný!**
5. **Který z těchto hodnot v hello packetech se musí shodovat na obou OSPF routerech aby navázaly fungující sousedství?**
	1. OSPF area
	2. hello interval
	3. dead interval
## Typy paketů
1. **Který packet obsahuje různé typy ==Link-State Advertisements==?**
	1. LSU packet.
2. **Který typ packetu obsahuje výpis LSDB odesílajícího routeru a je používán příjemcem k porovnání s vlastní LSDB?**
	1. DBD database description packet
3. **Jaké je pořadí typů paketů používaných OSPF routerem vedoucím k dosažení konvergence?**
	1. Hello, DBD, LSR, LSU, LSAck
## OSPFv2
1. **Router je součástí OSPFv2 oblasti. Co se stane, pokud dead interval vyprší předtím než router přijme Hello packet od sousedního DROTHER routeru?**
	1. OSPF router odebere tohoto souseda z LSDB.


## OSPFv3
1. 