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
- Adresu zapisujeme ve tvaru ==*segment : offset*==
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
- Instrukcemi PUSH/POP se mění pouze offset, nikoli segment.
- Zásobník proto "nevyteče" ze 64KB segmentu.
- ![[Pasted image 20251105141904.png | 300]]
## Registry procesoru 8086
![[Pasted image 20251105142001.png | 500]]
### Implicitní přiřazení segmentových registrů

| Při přístupu k      | se použije registr     | Operace                                                                                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| instrkcím           | **CS** (Code Segment)  | Výběr operačního kódu nebo přímého operandu.                                                                                   |
| zásobníku           | **SS** (Stack Segment) | Při všech přístupech k zásobníku nebo ve spojitosti s registrem BP.                                                            |
| datům               | **DS** (Data Segment)  | Při všech přístupech k datům v paměti vyjma zásobníku a přímých operandů. V řetězcových operacích segmentuje zdrojový operand. |
| alternativním datům | **ES** (Extra Segment) | V řetězcových operacích pro segmentování cílového operandu.                                                                    |

| Registr s offsetem          | Implicitně použitý segmentový registr |
| --------------------------- | ------------------------------------- |
| SP                          | SS                                    |
| BP                          | SS                                    |
| BX                          | DS                                    |
| SI                          | DS                                    |
| DI                          | DS (ES v řetězcových operacích)       |
| BP v kombinaci s SI nebo DI | SS                                    |
| BX v kombinaci s SI nebo DI | DS                                    |
- **Explicitní přiřazení** segmentového registru offsetovému lze zadat např.:
	- MOV AH, CS: \[BX]       Nepřímá adresa CS:BX (nikoli DS:BX)
	- ADC  AH, ES: \[Adresa]   Přímá adresa segmentovaná přes ES
### Příznakový registr 8086
![[Pasted image 20251105143043.png | 500]]
- **CF** (Carry Flag) obsahuje přenos z nejvyššího bitu, a to jak při práci s 8 nebo 16bitovým operandem.
- **PF** (Parity Flag) se nastaví na jedničku, pokud dolní osmice bitů výsledku právě provedené operace obsahuje sudý počet ”1“ (sudá parita výsledku).
- **AF** (Auxiliary Carry Flag) je rozšířením příznaku CF pro přenos přes hranici nejnižšího půlbajtu operandu (vždy z bitu 3 do 4 bez ohledu na šířku operandu). Má význam v BCD aritmetice.
- **ZF** (Zero Flag) je nastaven při nulovém výsledku právě dokončené operace.
- **SF** (Sign FLag) je kopií znaménkového bitu výsledku operace

- **OF** (Overflow Flag) se nastaví na jedničku, pokud při právě dokončené operaci došlo k aritmetickému přeplnění (výsledek spadá mimo rozsah zobrazení).
- **TF** (Trap Flag) uvádí procesor do krokovacího režimu, ve kterém je po provedení první instrukce generováno přerušení (INT 1). Příznak lze nastavit pouze přes zásobník instrukcí IRET.
- **IF** (Interrupt Enable Flag) nulový zabrání uplatnění vnějších maskovatelných přerušení (generovaných signálem INTR)
- **DF** (Direction Flag) řídí směr zpracovávání řetězcových operací.

## Zásobník
- Zásobník procesor implementuje jako strukturu LIFO kdekoli v operační paměti. Všechny odkazy na zásobník jsou segmentovány přes registr SS.
- Příklad: Dno zásobníku je na adrese SS:0A1A. Zásobník byl do současného stavu naplněn posloupností instrukcí, které zapsaly hodnoty: 0AA01, 11AA, 3C00.
- ![[Pasted image 20251105143535.png | 500]]

- Výběr a zápis do zásobníku řídí registr SP (Stack Pointer), ketrý obsahuje adresu právě zapsané položky.

- PUSH
	- Instrukce PUSH provede činnosti v následujícím pořadí:
		1. sníží obsah SP o dvě
		2. na adresu SS:SP uloží obsah 16bitového operandu.
- POP
	- Instrukce POP provede tyto akce:
		1. operand naplní 16bitovým obsahem adresy SS:SP
		2. zvýší obsah SP o dvě

- Procesor 8086 nemá žádný prostředek, kterým by hlídal maximální mez naplnění zásobníku.
### Přerušení v 8086
- Vnější (gen. technickými prostředky)
	- nemaskovatelná (signál NMI)
	- maskovatelná (signál INTR)
- Vnitřní (gen. programově)
	- instrukcí INT n
	- chybou při běhu programu
#### Vektor adres rutin obsluhující přerušení
![[Pasted image 20251105145633.png | 400]]

- ==Každé přerušení provede akce v tomto pořadí:==
	1. do zásobníku se uloží registr příznaků (F),
	2. vynulují se příznaky IF a TF,
	3. do zásobníku se uloží registr CS,
	4. registr CS se naplní 16bitovým obsahem adresy n × 4 + 2,
	5. do zásobníku se uloží registr IP,
	6. registr IP se naplní 16bitovým obsahem adresy n × 4

- ==Návrat do přerušeného procesu a jeho pokračování zajistí instrukce IRET, která provede činnosti v tomto pořadí:==
	1. ze zásobníku obnoví registr IP,
	2. ze zásobníku obnoví registr CS,
	3. ze zásobníku obnoví příznakový registr (F)
### Srovnání návratu z přerušeného procesu
- "Náš" procesor
- ![[Pasted image 20251105145947.png | 100]]
- Procesor 8086:
- ![[Pasted image 20251105150014.png | 100]]
### Rezervovaná přerušení 8086
![[Pasted image 20251105150052.png | 400]]

- **INT 0** při dělení nulou v instrukcích DIV a IDIV. Obsah CS:IP uložený do zásobníku ukazuje za (v 80286 a vyšších na) instrukci, která přerušení způsobila.
- **INT 1** po provedení instrukce, je-li TF=1.
- **INT 2** po přijetí signálu NMI (v 8086 pouze chyba parity v paměti), který nelze zakázat nulovou hodnotou příznaku IF.
- **INT 3** se používá společně s přerušením INT 1 v ladících systémech. Přerušení 03h se vygeneruje po dekódování speciální jednobajtové instrukce INT 3 (s operačním kódem 0CCh). Přerušení uloží do zásobníku obsah CS:IP ukazující na bajt bezprostředně za touto instrukcí.
- **INT 4** provede instrukce INTO (Interrupt on Overflow), je-li v okamžiku jejího dekódování nastaven příznak OF=1. CS:IP ukazuje na bajt za touto instrukcí
#### Krokovací režim (TF = 1)
![[Pasted image 20251105150354.png | 200]]
##### Počáteční spouštění krokovacího režimu
![[Pasted image 20251105150437.png | 400]]
##### Počáteční nastavení procesoru
- Procesor je inicializován aktivní úrovní signálu RESET.
- ![[Pasted image 20251105150537.png | 200]]
- Tzn., že první instrukce, kterou bude procesor po inicializaci signálem RESET zpracovávat, je umístěna na adrese 0FFFF:0000h, tj. 0FFFF0h (15 bajtů od konce).
### Adresovací techniky
![[Pasted image 20251105150710.png | 450]]
### Instrukce MOV
- Instrukce MOV příznaky nemění!!
- ![[Pasted image 20251105150806.png | 400]]
- Po instrukci MOV SS, je po dobu trvání následující instrukce zakázáno přerušení !
