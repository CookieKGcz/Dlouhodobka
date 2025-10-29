# Přerušení
## Multiprogramové zpracování
- "okamžik přerušení procesu"
- ![[Pasted image 20251029141355.png|400]]
## Přerušovací systém (Interrupt System)
- program (statický) vs. proces (dynamický)
- umožňuje přerušení běžícího procesu a aktivuje rutinu pro obsluhu přerušení
### Činnost při přerušení
1. Přerušení provádění procesu
2. Úklid PC, A, ...
3. Provedení obslužné rutiny
4. Obnovení PC, A ... a tím pokračování v provádění procesu
## Kdy lze přerušit proces?
- pouze pro provedení instrukce (nikoli během ní -> instrukce musí dokončit všechny své fáze)
- je-li to povoleno (každý procesor má příznak, kterým se přerušení zakazuje a povoluje)
	- Např. IF (interrupt FLAG)
	- Instrukce STI (přerušení povoleno, tj. IF:=1)
	- Instrukce CTI (přerušení zakázáno, tj. IF:=0)

- procesor nelze přerušit bezprostředně po zahájení obsluhy předchozího přerušení
- přerušení se vyvolá signálem Interrupt (žádost o přerušení)
- ![[Pasted image 20251029141953.png | 400]]

- fáze:
- ![[Pasted image 20251029142019.png | 400]]
## Příklad konstrukce programu pro obsluhu přerušní
- 100h   PUSH PSW      úklid registru A a příznaků
- 101h   PUSH B            úklid registru B a C
- 102h   PUSH D           úklid registru D a E
- 103h   PUSH H           úklid registru H a L
- 104h   ...                      obsluha přerušní

- ...        POP H              obnovení registrů H a L
- ...        POP D              obnovení registrů D a E
- ...        POP B              obnovení registrů B a C
- ...        POP PSW         obnovení registru A a příznaků
-           STI                    povolení přerušení
-           RET                   návrat do přerušeného procesu

## Signál RESET
- Nastavení počítače do počátečních podmínek a předání řízení zaváděcímu programu v permanentní paměti
- Příklad: Rozdělení paměti 'našeho' pomyslného počítače:
- ![[Pasted image 20251029142627.png | 300]]

- Signál Reset se uplatní kdykoli - tj. i uvnitř fází instrukce
- **Fáze RESET:**
	- ![[Pasted image 20251029142737.png | 250]]
- Činnosti po zapnutí počítače:
	1. vyčkání asi 1s (doba náběhu a ustálení zdroje)
	2. generování signálu RESET
# Virtuální paměť
- ![[Pasted image 20251029143242.png | 450]]

- každý obsah na paměť obsahuje virtuální adresu:
- ![[Pasted image 20251029152204.png | 450]]
## Algoritmus LRU - Least Recently Used
- Výběr nejdéle nepoužívané položky:
	1. Ve VP vybavit každý blok čítačem, který se při:
		- volání daného bloku nuluje
		- volání jiného bloku inkrementuje o jedničku
- V případě potřeby se vyřadí blok s nejvyšší hodnotou
	2. Pomocí neúplné matice s prvky nad hlavní diagonálou
		- každý prvek je jednobitová paměť
		- při volání bloku i se:
			- jedničkuje i -tý řádek
			- nuluje i -tý sloupec
		- nejdéle nepoužité paměťové místo má:
			- v řádku nuly
			- ve sloupci jedničky
	- ![[Pasted image 20251029152956.png | 300]]
# Vyrovnávací (cache) paměť, použití LRU
- ![[Pasted image 20251029153041.png | 400]]
- Není nutné vždy přepisovat blok z VP zpět do OP.
- Který blok při zaplnění VP vyhodit? (Použití LRU)
## Použití cache paměti - Jedna paměť, jedna cache a dva různé přístupy
- V cache může být nevalidní informace, pokud je do paměti přístup jinou cestou, než přes cache:
	- Napojení OP na VP a na kanál:
	- ![[Pasted image 20251029153501.png | 400]]
	- V multiprocesorových systémech při sdílení jedné paměti více procesory
# Architektura procesorů Intel - Procesor 8086
## Procesor Intel 8086 a 8088
- Procesor  8086
	- 16bitový procesor
	- 1978 - 1982
	- základní procesor řady INTEL x86
	- frekvence max. 10 MHz
- Procesor 8088
	- 16bitový procesor do 8bitového prostředí
	- 1979 - 1982
## Zapojení 8086 a 8088
![[Pasted image 20251029153938.png | 400]]
![[Pasted image 20251029154019.png | 400]]

- **INTR** - Signál žádosti o maskovatelné přerušení.
- **neg(TEST)** - Signál testovatelný instrukcí WAIT. Při neg(TEST) = L program pokračuje další instrukcí.
- **NMI** - Signál nemaskovatelného přerušení 
- **RESET** - Signál okamžitě ukončí aktivitu CPU a předávající řízení instrukce na adrese 0FFFF0h
- **neg(LOCK)** - Uzamčení sběrnice pro procesor, který nastavil neg(LOCK) = L instrukčním prefixem LOCK.
- **M/neg(IO)** - Rozlišuje, zda adresa patří 
## Typy dat zpracovávané procesory Intel
- Little-Endian (na nižší adrese nižší řád):
- ![[Pasted image 20251029160135.png | 500]]
## Adresace paměti procesoru 8086
- Adresu zapisujeme ve tvaru *segment : offset*
- ![[Pasted image 20251029160247.png | 500]]
- Zápis 01A5:0012_16 představuje tedy dvacetibitovou adresu 01A62_16

- Procesor  8086 pro uložení segmentu poskytuje čtyři 16bitové segmentové registry:
	- **CS** (Code segment) je určen pro výpočet adresy instrukce,
	- **DS** (data segment) slouží pro výpočet adresy dat,
	-  **SS** (Stack segment) se použije při přístupu k zásobníku a
	- **ES** (Extra segment) je může obsahovat pomocný datový segment
### Umísťování procesu/segmentu do paměti
- Do instrukcí typu 'LDA adresa' se na místo adresy vkládá offset.
- Segmentovým registrem se určuje, kde je segment umístěn v paměti.
- ![[Pasted image 20251029161231.png | 300]]
### Zásobník v paměti
str 241 cca