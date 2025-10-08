# Obvody
## Sčítačky
### Sčítačka MODULO 2

| x   | y   | z   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |
- rovnice:
	- z = neg(x) * y + x * neg(y)
### Polosčítačka

| x   | y   | S   | P   |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 1   | 1   | 0   |
| 1   | 0   | 1   | 0   |
| 1   | 1   | 0   | 1   |
- rovnice:
	- S = neg(x) * y + x * neg(y)
	- P = x * y
### Úplná Sčítačka
#### Pro jeden binární řád
![[Pasted image 20251008140802.png | 400]]
![[Pasted image 20251008140816.png | 250]]
### Vícemístná sčítačka
![[Pasted image 20251008140951.png | 400]]
- poznámka P na začátku je technicky 0 (zem)
- pokud by jsme sčítali ve stejný čas, tak by sčítačka nefungovala
#### Př.:
- Navrhněte sčítačku pro 32 řádů a zapište pravdivostní tabulku (2 × 32 vstupů, 32 výstupů).
- pravd. tabulka by měla 2^64 řádků = 18 × 10^18 
## Sekvenční logické obvody
- Předchozí obvody (and, or, not, xor, multiplexor, sčítačky...) byly tzv. kombinační logické obvody, ve kterých výstup závisel jen na aktuální hodnotě vstupů.
- **Sekvenční logické obvody** mají výstup závislý nejenom na aktuální hodnotě vstupů, ale také i na posloupnosti změn, které předcházely.
![[Pasted image 20251008142225.png | 400]]
### Základní paměťový člen: Klopný obvod RS
- R ... RESET (nulování)
- S .. SET (nastevení)
![[Pasted image 20251008142350.png | 400]]
#### RS řízený nulami:
![[Pasted image 20251008142445.png | 250]]
- zapojeno pomocí dvou nand
![[Pasted image 20251008142702.png | 300]]
#### RS řízený jedničkami
![[Pasted image 20251008142911.png | 350]]
#### RS řízený jedničkami s časovou synchronizací
![[Pasted image 20251008142957.png | 450]]
### Klopný obvod řízený
- Kdy je přesně obvod **otevřený**:
- Hladinou
	- horní
	- dolní
	- ![[Pasted image 20251008144517.png]]
- Hranou
	- čelem impulsu (nástupní hrana)
	- týlem impulsu (sestupná hrana)
	- ![[Pasted image 20251008144526.png]]
#### Klopný obvod D
- D ... Delay (vzorkovací K.o.)
![[Pasted image 20251008144602.png | 350]]
![[Pasted image 20251008144635.png | 400]]
#### Klopný obvod JK
![[Pasted image 20251008144734.png | 350]]
![[Pasted image 20251008144754.png | 400]]
## Typické sekvenční obvody v počítačích
### Sériová sčítačka
![[Pasted image 20251008144842.png | 400]]
### Paralelní registr = střídač
![[Pasted image 20251008144924.png | 400]]
## Přenos informací v systému
- Sériový
	- ![[Pasted image 20251008145027.png | 300]]
- Paralelní:
	- ![[Pasted image 20251008145048.png | 150]]
	- Převod sériová informace -> paralelní pomocí posuvného registru
### Sériový přenos
![[Pasted image 20251008150948.png | 400]]
- Přenosová rychlost
	- v bitech za sekundu
	- v počtu změn za sekundu (baud rate, Bd)
### Přenos paralelně pomocí **sběrnice**.
- Využito paralelních registrů:
![[Pasted image 20251008151116.png | 450]]
### Sériový registr (posuvný registr):
- Jedním taktem signálu CLK se informace posune o jeden D-KO.
![[Pasted image 20251008151226.png | 450]]
![[Pasted image 20251008151242.png | 200]]
## Čítače
![[Pasted image 20251008151318.png | 450]]
![[Pasted image 20251008151558.png | 200]]
## Sčítačka v BCD kódu
- Součet dvou čísel vyjádřený:
![[Pasted image 20251008151656.png | 300]]
![[Pasted image 20251008152935.png | 400]]
## Násobičky
- Sekvenční násobení (bez znaménka)
![[Pasted image 20251008154255.png | 350]]
### Kombinační násobička
![[Pasted image 20251008154400.png | 450]]
## Rotace bitů, logický a aritmetický posun
### Rotace bitů
- Doleva
- ![[Pasted image 20251008154628.png | 300]]
- Doprava
- ![[Pasted image 20251008154646.png | 300]]
### Logický posun (Logical shift)
- Doleva
- ![[Pasted image 20251008154731.png | 300]]
- Doprava
- ![[Pasted image 20251008154746.png | 300]]
### Aritmetický posun (Arithmetic shift)
- Doleva
- ![[Pasted image 20251008154831.png | 300]]
	- Znaménkový but se nemění!
	- ~ násobení x2
- Doprava
- ![[Pasted image 20251008154934.png | 300]]
	- Znaménkový bit se kopíruje do nižšího řádu
	- ~ dělení /2
### Blok operační jednotky
![[Pasted image 20251008155042.png | 400]]

## Obvod pro rotaci vlevo, vpravo a beze změny
![[Pasted image 20251008162008.png | 400]]
### Komparátor
![[Pasted image 20251008162039.png | 300]]
# Paměti
## Parametry
- Hlavní druhy:
	- Vnější/vnitřní paměti
	- registry
- vybavovací doba (čas přístupu k záznamu v paměti) = 10ns ... 100ms
- rychlost toku dat (počet přenesených bitů za sekundu)
- kapacita paměti (počet bitů)
- cena za bit
- přístup
	- přímý
	- sekvenční
- destruktivnost při čtení
- energetická závislost a nezávislost
- statika a dynamika (dynamika - musí se pořád obnovovat (např.: kondenzátory))
- spolehlivost - definujeme v rozmezí teplot (např. 1 porucha za 5000 h, 1 chyba na 1013 bitů toku)

- zápisníková paměť = sada registrů
- řídicí paměť - pro zaznamenání stavu programů
- vyrovnávací paměť (cache) - k vyrovnání rozdílů v toku dat
	- mezi procesorem a pamětí
	- mezi procesorem a V/V zařízením
## Vnitřní paměti
![[Pasted image 20251008162931.png | 450]]
- klasifikace pamětí podle způsobu čtení a zápisu
- registr adresy - cpu řekne čti vlastně
### Fyzická struktura paměti
![[Pasted image 20251008163233.png | 400]]
## Vnitřní paměti pokračování
- Paměť pro čtení a zápis
	- RWM (Read_Write Memory)
	- RAM (Random Access Memory)
- operační paměť počítačů
- nejrozšířenější - polovodičové paměti
	- Bipolární TTL
	- Unipolární NMOS, CMOS
	- SRAM, DRAM
	- energeticky závislé
	- nedestruktivní
### Archaický typ - feritové paměti
![[Pasted image 20251008163902.png | 300]]
- ZÁPIS - koexistencí proudů výběrového a č/z vodiče
- ČTENÍ - zápisem ” 0“ se na č/z vodiči indukuje vysoké nebo nízké napětí, původní hodnotu obnovit zpětným zápisem. → Destruktivní čtení
![[Pasted image 20251008163959.png | 300]]
