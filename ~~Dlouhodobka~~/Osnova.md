## Zadání práce:

1. Zpracování písemné zprávy (protokolu). Žák je povinen dodržet minimální rozsah zprávy (protokolu), strukturu a způsob zpracování zprávy (protokolu) včetně povinných částí, použít průběžné citování zdrojů včetně seznamu použité literatury a zdrojů v souladu s ČSN ISO 690.

**Maximální počet bodů: 30**

1. Vypracovat teoretickou část práce na téma Útoky typu DoS, a to v rozsahu maximálně šesti normostran. Při vypracovávání této teoretické části se nejprve zaměřte na vysvětlení principu funkce těchto útoků a vypracování přehledu útoků typu DoS. Dále se zabývejte nástroji používanými pro jejich realizaci a možnostmi prevence a řešeními pro obranu proti těmto druhům útoků. Nakonec se zaměřte na konkrétní nástroje používané proti útokům typu DoS ve firemním prostředí.

**Maximální počet bodů: 10**

1. Vytvořit minimálně dva kyberbezpečnostní scénáře pro různé útoky typu DoS, vždy pro každý databázový útok jeden scénář. Cílem scénáře bude úspěšná realizace tohoto typu útoku na zranitelný server a nalezení řetězce (tzv. flagu) ukrytého na zranitelném serveru. Tento scénář vždy vytvářejte ve virtualizovaném prostředí programu VirtualBox. Součástí každého kyberbezpečnostního scénáře bude zranitelný server a klientské počítače. Nejprve si zvolte některou z metod útoku popsanou v teoretické části. Na jejím základě pak vyberte vhodný operační systém a aplikace, které nainstalujte a nakonfigurujte tak, aby bylo možné daný scénář realizovat. Veškerou instalaci a konfiguraci všech prvků virtuální infrastruktury podrobně dokumentujte. Nakonec vypracujte zprávu o rozsahu maximálně devíti normostran textu.

**Maximální počet bodů: 20**

1. Vytvořit pracovní list, který bude v jednotlivých krocích podrobně popisovat řešení každého kyberbezpečnostního scénáře, tj. postup zneužití vybraného typu útoku a který kromě tohoto postupu stručně představí i použité techniky a nástroje. Součástí pracovního listu budou i kontrolní otázky prověřující pochopení popisovaného postupu.

**Maximální počet bodů: 10**

1. Vytvořit plakát A3, který stručně informuje o náplni práce. Bude obsahovat název a logo školy, název práce, jméno autora a vedoucího práce, cíl práce, zkrácenou anotaci v bodech nebo stručnou charakteristiku, obrazový materiál (schéma, fotografii výrobku, část programu...). Plakát zpracovat graficky zajímavě tak, aby zaujal na první pohled. Jednou plakát vytisknout na A4, přiložit k jednomu z výtisků písemné zprávy (protokolu), ve velikosti A3 uložit v elektronické podobě v těchto formátech: PDF, JPG, PNG.

**Maximální počet bodů: 5**

1. Obhájit práci před zkušební maturitní komisí.

**Maximální počet bodů: 25**

Výstupy praktické maturitní zkoušky jsou školním dílem. Žák souhlasí s tím, že dílo bude škola využívat pro studijní účely, pro výuku a popř. dle tématu i pro organizační zajištění chodu školy bez nároku na finanční odměnu. Výrobek, který financoval žák, je majetkem žáka a může si jej v posledním týdnu v červnu vyzvednout.

Žák se zavazuje, že veřejně odprezentuje ostatním žákům školy výsledky své maturitní práce. V tomto školním roce je veřejná prezentace plánována na poslední březnový týden.

## Povinné části
písemná zpráva (protokol) má tyto povinné části:
- titulní strana (viz šablona)
- čestné prohlášení autora včetně jeho podpisu (viz šablona)
- anotace práce a klíčová slova (obě části v českém a anglickém jazyce, viz šablona)
- obsah vygenerovaný na základě nadpisových stylů (v souladu s ČSN 01 6910)
- úvod a cíl práce (podrobnější charakteristika viz šablona)
- teoretická část (pokud je součástí zadání) a vlastní práce (podrobnější charakteristika viz šablona); v rámci této části práce využívá žák při zpracování víceúrovňového číslování nadpisů v odborném textu (maximálně na prvních 4 úrovních)
- závěr (podrobnější charakteristika viz šablona)
- seznam použité literatury a zdrojů sestavený v souladu s ČSN ISO 690
- přílohy (pouze v případě, že je daná práce obsahuje)
## Osnova - teoretická část
- vysvětlení principu
- přehled útoků
	- **Volume-Based (volumetric) Attacks**
		- UDP floods
			- Reply with an ICMP Destination Unreachable packet
		- ICMP floods
			- ICMP echo-request packets
	- **Protocol Attacks**
		- SYN flood
			- Never sends ACKs
		- Ping of Death
			- Packet larger than the maximum allowable size
	- **Application Layer Attacks** (DDoS)
		- HTTP flood 
			- HTTP GET
			- HTTP POST
		- BGP hijacking
			- reroute Internet traffic - falsely announcing ownership of groups of IP addresses
		- Slowloris (taky nástroj)
			- operates by utilizing partial HTTP requests - keeping connections open
	- **Reflective Attacks**
		- DNS reflection
		- NTP reflection
			- UDP packets with spoofed IP to NTP server > "monlist" command (large response) 
	- **Resource Exhaustion**
		- Local Area Network Denial
	- **DDoS** how exactly
		- botnet
- nástroje pro realizaci
	- LOIC
	- HOIC
	- Slowloris (nástroj)
- možnosti prevence / řešení -> pro obranu
- konkrétní nástroje používané proti útokům ve firemním prostředí
## "Osnova" - scénáře
Cílem scénáře bude úspěšná realizace tohoto typu útoku na zranitelný server a nalezení řetězce (tzv. flagu) ukrytého na zranitelném serveru.

Dokumentovat!
## Pracovní list
potom