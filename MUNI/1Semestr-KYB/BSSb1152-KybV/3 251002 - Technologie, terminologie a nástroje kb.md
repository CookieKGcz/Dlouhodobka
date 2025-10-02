#kyber
## Naše vymezení
- **mimo** EWar (rušičky) a InfoWar (čistě obsahová stránka -> manipulace (propaganda))
- kybernetické útoky -> změna zařízení která jsou připojená do sítě
## Archetypy útoků
- akvizice informací
	- a následná diseminace/exploitace
- šíření informací
	- propaganda
- disrupce
	- procesů a služeb
- destrukce
	- dat/zařízení
## Confidentiality, Integrity, Availability
- vztahují buď k systému takovým nebo k datům
- = důvěrnost (přístup k datům kdo by k nim přístup neměl mít), integrita (data zůstávají v původním stavu (nejsou změněny)), dostupnost (data stále existují, jsou v původním stavu, ale nemůžeme se k ním dostat)
## Východiska
- většina škod je neúmyslná
	- bugy ,nehody, přírodní katastrofy, ...
- případné útoky zevnitř
	- insideři -> [[3 250930 - Základní terminologie BSS]]
- útoky v zásadě spočívají v nalezení a využití nějaké existující slabiny
	- lidské, strukturální, implementační, technické
	- neexistuje dokonalý systém
## Častá tvrzení
- "biliony útoků" -> počítáme i automatizované nástroje
- "jsme čím dál zranitelnější" -> spíše naopak, akorát roste množství systémů, více na nich záleži...
- airgap - absence připojení k vnějšímu světu
## Síťové útoky
- DDoS
	- botnenty, CnC, LOIC
	- na dostupnost
- MitM
	- na důvěrnost i integritu
## Sociální inženýrsví
- využití lidských vlastností (hloupost, naivity...)
- phising, spearphising (skupina), whalephising (jedinec)
- slabost a opakování hesel
- přenosná média
## Kryptologie a bezpečnsot
### Historie
- od antiky - césarova šifra
- pozvolný vývoj až do novověku
- vývoj ++ války
	- enigma
### Prolamování kódu
- frekvenční analýza
- repetice
- chyby operátorů
- kódové knihy
- hrubá síla (modernější doba)
### Steganografie
- kdysi a dnes
- text, obrázky, hudba, neviditelný inkoust
- správy schované v již "veřejným" textu/obrázku...
### Hash
- + salt
### "Security through obscurity"
- dat, algoritmu, klíče
## Symetrické a Asymetrické šifry
- sym. používá stejný klíč na šifrování a dešifrování zprávy
- asym - použití veřejného a privátní klíče (různé kombinace šifrování, pro co to chceme využít)
## Řízení přístupu
- identifikace, autorizace, authentizace

- hlavně co jste, co znáte, co máte
- biometrika (co jste)
	- výhody - rychlost, nemusíme nic mít/pamatovat
	- nevýhody - nejednoznačnost, musí být nastavena tolerance
		- FAR (false acceptence rate), FRR (false rejection rate)
	- rozděluje na fyzické(obličej, otisk prstu, zornice, DNA) a behavioral(jak mluvíme, píšeme na klávesnici, podpis...)
