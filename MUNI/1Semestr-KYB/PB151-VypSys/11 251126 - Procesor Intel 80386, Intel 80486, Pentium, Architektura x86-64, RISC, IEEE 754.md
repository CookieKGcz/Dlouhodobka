# Intel 80386
- 32 bitový CPU
- od 1986 cca do 1994
- 16 MHz až 40 MHz
- "zakladatel" architektury IA-32
- 32bit. adresová sběrnice -> max 4GB RAM
- 32bitová datová sběrnice
- alternativní název i 386DX
## Popis signálů procesoru Intel 80386
![[Pasted image 20251126140634.png | 500]]
- čtvercový keramický integrovaný obvod
	- spodní povrch PGA piny
	- 132 vývodů
- D0 - D31
	- 32bitová obousměrná datová sběrnice
- A2 - A31
	- 32bitová adresová sběrnice adresující 32 bitová slova
- BE0 - BE3
	- Bližší určení přenášených bajtů v rámci dvojslova.
- BS16
	- Volba 16bitového přenosu dat.
- NA
	- (Next Adress) Slouží k zahájení výběru obsahu další adresy při proudovém zpracování
- D/C, ADS, W/R
	- signály určené pro řízení sbrnice
## Registry procesoru 80386
- ![[Pasted image 20251126141113.png | 400]]
## EFLAGS
- příznakový registr
- ![[Pasted image 20251126141201.png | 500]]

## Adresace v chráněném režimu 80386
- **Selektor** je stejný jako v 80286
- **Offset** je 32bitový
- **Limit segmentu** může mít velikost až 4GB - 1.
- **Báze segmentu** je 32bitová (tj. 0 až 4 GB - 1).
- **Logická adresa** (v terminologii 80286 se nazývá virt. adresa) je složena z 16bitového sektoru a 32bitového offsetu (tj. adresujeme 64 TB virt. paměti). Tato adresa je algoritmem segmentační jednotky převedena na lineární adresu.
- **Lineární adresa** je 32bitová adresa (tj. adresuje 4GB). Není-li v činnosti stránkovací jednotka, potom linární adresa ukazuje už přímo do fyzické paměti.
- **Fyzická adresa** je transformována činností stránkovací jednotky z lineární adresy. Je rovněž 32bitová (tj. adresuje 4 GB fyz. paměti). Není-li stránkovací jednotka zapnuta, je fyzická adresa totožná s lineární adresou.
## Transformace virt. adresy na fyzickou
- ![[Pasted image 20251126142009.png | 500]]
## Řídící registry 80386
- ![[Pasted image 20251126142045.png | 500]]
- Nejnižších 16 bitů CR0 je nazýván MSW (Pro kompatibilitu s 80286)
	- PE (Protected Mode Enable) zapíná chráněný režim. Vynulováním se přepne zpět do reálného režimu.
	- ET (Extention Type) sděluje typ instalovaného matematického koprocesoru (80287 = 0, 80387 = 1). Bit nastavuje procesor během inicializace (po přijetí signálu RESET)
	- PG (Paging) zapíná stránkovou jednotku určenou k transformaci lineárních na fyzické adresy.
- Registr CR2, jeli PG=1, obsahuje lineární adresu, která způsobila výpadek stránky.
- Výpadek stránky má za následek generování přerušení INT 14.
- Registr CR3 (jeli PG=1) obsahuje fyzickou adresu stránkového adresáře právě aktivního procesoru.
- Dolních 12 bitů se při zápisu do tohoto registru ignoruje, protože stránkový adresář smí začít pouze na hranici 4KB stránky.
- Ladící registry: DR0, DR1, DR2, DR3, DR6, DR7
- Testovací registry: TR6 a TR7
## Popisovače segmentů
- ![[Pasted image 20251126142730.png | 500]]
- G (Granularity)
	- = 0 ... jednotka limitu je 1 B (Max. 1 MB)
	- = 1 ... jednotka limitu je 4 KB (Max. 4 GB)
- AVL (Available for Programmer Use)
	- "s" závisí na typu popisovače
- B (Big)
	- = 0 ... segment podle pravidel 80286 (max. 64 KB), implicitní velikost položky ukládané do zásobníku je 16 bitů,
	- = 1 ... segment podle pravidel 80386 (max. 4 GB), zásobník lze plnit od adresy FFFFFFFFh, implicitní velikost položky ukládané do zásobníku je 32 bitů
### Popisovač systémového segmentu
- Bit "s" není použit.
- ![[Pasted image 20251126143403.png | 400]]
### Popisovač instrukčního segmentu
- D (default)
	- = 0 ... implicitní velikost adres operandů je 16 bitů,
	- = 1 ... implicitní velikost adres operandů je 32 bitů
- Explicitní určení velikosti zajišťují instrukční prefixy:
	- 66h mění implicitní velikost operandu a 
	- 67h mění implicitní velikost adresy
- ![[Pasted image 20251126143618.png | 500]]
## Stránkování
- logická adresa --> lineární adresa --> fyzická adresa
- Selektor_16 : Offset_32    32 b                    32 b

- Rámec a stránka kapacity 4 kB
- Zapnutí stránkování PG:=1 (vit v CR0)

- ![[Pasted image 20251126143948.png | 500]]
- Každý proces má vlastní stránkový adresář (CR3 je uloženo v TSS)

### Položka stránkové tabulky a adresáře
- ![[Pasted image 20251126144233.png | 500]]
- Adresa rámce je horních 20 bitů adresy rámce.
	- AVL (Available)
	- D (Dirty) nastavuje procesor při změně obsahu rámce. Ve stránkovém adresáři je tento bit nedefinoán.
	- A (Accessed) nastavuje procesor při každém použití tohoto specifikátoru.
	- U (User Accesible) Pracuje-li proces na úrovní oprávnění CPL=3, smí k této stránce přistupovat při U=1. Procesy s CPL < 3 smějí přistupovat ke všem stránkám bez ohledu na hodnotu bitu U.
	- W (Writeable) Pracuje-li proces na úrovni CPL=3, smí do této stránky zapisovat při W=1. Procesy CPL < 3 smějí zapisovat do všech stránek bez ohledu na hodnotu bitu W
	- P (Present) Je-li P = 0, není obsah stránky ve fyzické paměti. Zpřístupnění takové stránky vyvolá INT 14 a CR2 je adresa stránky.

- Vyhodnocení bitů U a W ze stránkového adresáře a stránkové tabulky:
	- Použije se dvojice mající nižší numerickou hodnotu: ” UW“. 
	- Příklad: Je-li U a W ve stránkovém adresáři 10 (CPL=3 smí číst a provádět) a ve stránkové tabulce 01 (pro CPL=3 nepřístupné), vybere se varianta U=0 a W=1.

## TLB - Translation Look-aside Buffer
- ![[Pasted image 20251126150752.png | 500]]
### Vyprázdnění TLB
- Vyprázdnění TLB je nastavení V:= 0 do všech položek.
- Automaticky vždy při naplnění CR3.
- Ručně musíme TLB vyprázdnit při každé změně stránkovacích tabulek nebo při nastavení P=0 některé z položek.
### TSS 80386
- ![[Pasted image 20251126151339.png | 500]]

## Mapa přístupných V/V bran
- Pro kontrolování V/V instrukcí pouze tehdy, je-li CPL>IOPL.
- Je-li bit mapy = 0 ... V/V operace se povolí,
-  = 1 ... generuje se INT 13.
- Pracuje-li V/V instrukce se slovem nebo dvojslovem ... testují se všechny odpovídací bity.
- ![[Pasted image 20251126151625.png | 500]]
## Rezervovaná přerušení
- INT 1 Ladící přerušení
	1. při čtení/zápisu z/do paměti byl detekován ladící bod (Trap),
	2. při výběru instrukce byl detekován ladící bod (Fault),
	3. po provedení instrukce v krokovacím režimu (Trap),
	4. při přepnutí na proces mající v TSS T=1 (Trap),
	5. nedovoleným přístupem k ladícím registrům při GD=1 (Fault).
- INT 14 Výpadek stránky (Page Fault)
	- Přerušení generuje stránkovací jednotka při:
		1. proces nemá dostatečnou úroveň oprávnění pro přístup ke stránce,
		2. ve stránkovacích tabulkách je detekováno P=0.

- Při přerušení je naplněn CR2 lineární adresou, která vyvolala přerušení. Chybové slovo má zvláštní tvar:
	- ![[Pasted image 20251126152405.png | 400]]
	- P (Present)
	- W (Write)
	- U (User Level)
# Procesor Intel 80486
- 32bitový precesor
- od 1988 cca do 1993,
- 25 MHz až 120 MHz,
- 32bitová adresová sběrnice, tj. max GB RAM,
- 32bitová datová sběrnice
- obsahuje vyrovnávací paměť (cache)
- obsahuje novou technologii blízkou RISC,
## Zapojení procesu 80486
![[Pasted image 20251126152729.png | 500]]
## Schéma činnosti vyrovnávací paměti
![[Pasted image 20251126153130.png | 500]]
# Procesor Intel Pentium
- Pentium z řecky penta, tj. 5
- 32bitový procesor,
- od 1993 do 1999
- 60 až 300 MHz
- od 1995: Pentium MMX, PRo, II, III, 4, D, Xeon,
	- velikost cache, počet jader...
## Rysy procesoru (rozšíření o Intel486)
- superskalární architekturu
- dynamické předvídání skoků
- zřetězenou FPU
- zkrácení doby provádění instrukcí
- oddělené 8KB datové a instrukční vyrovnávací paměti
- protokol MESI pro řízení datové vyrovnávací paměti
- 64bitovou datovou sběrnici
- zřetězování cyklů sběrnice

- adresové priority
- vnitřní kontrolu parity
- kontrolu správné funkce znásobením čipů s procesorem
- sledování provádění
- monitorování výkonnosti
- ladění prostřednictvím IEEE 1149.1 Boundery Scan
- režim správy systému a
- rozšíření v režimu V86
## Blokový diagram procesoru Pentium
![[Pasted image 20251126154806.png | 500]]
## Zřetězené provádění instrukcí
- PF
	- Prefetch - výběr instrukce
- D1
	- Instruction Decode
- D2
	- Address Generate
- EX
	- Execute
- WB
	- Write Back - Dokončení instrukce

- ![[Pasted image 20251126154951.png | 400]]
## Předvídání podmíněných skoků
- Branch Target Buffer - BTB
	- Při výběru instrukce se testuje obsah BTB na shodu s adresou vybírané instrukce. Pokud se adresa v BTB najde, zkoumá se obsah bitů historie.
	- ![[Pasted image 20251126161532.png | 400]]
## Párování instrukcí
- Instrukce mohou být spojeny do páru za splnění následujících podmínek.
	- Obě instrukce v páru musí být ” jednoduché“ podle dále uvedené definice.
	- Mezi instrukcemi v páru nesmí být vztah ” čtení až po zápisu“ nebo ” zápis až po čtení“.
	- Žádná z instrukcí nesmí mít výpočet adresy složen ze dvou částí: z přímé hodnoty a zároveň z přírůstku.
	- Instrukce s prefixy (vyjma 0F před podmíněným skokem) lze provádět pouze ve frontě ” u“.
### Jednoduché instrukce
- jsou ty, které nevyžadují mikrokód a provedou se během jednoho hodinového cyklu. Výjimkou jsou instrukce aritmeticko-logické jednotky (ALU) mem,reg a reg,mem, které se provádějí ve dvou nebo třech taktech a jsou považovány za jednoduché.

- považujeme:
	1. mov reg, reg/mem/imm
	2. mov mem, reg/imm
	3. alu reg, reg/mem/imm
	4. alu mem, reg/imm
	5. inc reg/mem
	6. dec reg/mem
	7. push reg/mem
	8. pop reg
	9. lea reg,mem
	10. jmp/call/jcond near
	11. nop
- Podmíněné a nepodmíněné skoky smějí být párovány pouze jako druhé instrukce v páru.

## Režim správy systému
- ***System Management Mode – SMM*** – Režim SMM je transparentní (neviditelný) pro aplikace i operační systém z těchto důvodů:
	- Jedinou možností, jak SMM zapnout, je externí nemaskovatelné přerušení přivedené speciálním signálem.
	- Procesor zahájí provádění instrukcí určených pro SMM ze separátního adresového prostoru a separátní paměti (tzv. SMRAM – System Management RAM).
	- Při přepínání do SMM procesor ukládá obsah všech registrů do zvláštní části SMRAM.
	- Všechna přerušení, která normálně operační systém či aplikace obsluhuje, jsou během SMM zakázána.
	- Stav před přepnutím do režimu SMM se vrátí provedením instrukce RSM.
- SMM je podobný reálném režimu. Nejsou v něm úrovně oprávnění, privilegované instrukce nebo mapování adres. V SMM lze provádět V/V operace a adresovat celou 4GB kapacitu fyzické operační paměti.

# Architektura x86-64
- x86-64 tzv. AMD64
	- plnohodnotně 64bitová architektura
	- firma AMD (Advanced Micro Devices) od roku 1999
	- první procesor AMD Opteron 2003
	- zpětně kompatibilní s x86
	- procesory Opteron, Athlon, Turion, Sempron
## Dvě architekrury
- IA-64
	- irmy Intel a Hewlett-Packard
	- kompatibilní s x86
	- jiná instrukční sada v 64bitovém režimu: EPIC a VLIW
	- procesory Itanium
...
...
...
## Registrová sktruktura
![[Pasted image 20251126162443.png | 500]]


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# RISC | Mikroprocesor i860
- 8086 - i486 = CISC - (Complex Instruction Set Computer)
- i860 = RISC - (Reduced Instruction Set Cumputer)
- ![[Pasted image 20251126160605.png | 400]]
## Jednotky i860
- **Prováděcí jednotka**:
	- Registry r_0 - r_31  32bitové
	- r_0 je vždy = 0
	- operace zápisu se ignoruje
	- pro 64bitové operace se sdružují do dvojic
- **Techniky**:
	- Registr Bypassing
		- Je-li výsledek předchozí operace vstupem do další bere se ze sběrnice
	- Delayed Branch
		- Před skokem se provede ještě následující instrukce
		- BR návěští
		- OR r0,r0,r0
	- 2 varianty podmíněného skoku:
		- ![[Pasted image 20251126160820.png | 350]]
- **FPU**:
	- Registry f0 - f31 32bitové
	- f0, f1 vždy 0
	- **Sčítačka** – sčítání a převody mezi jednoduchou a dvojnásobnou přesností
	- **Násobička** – násobení a výpočet 1/x
	- **Duální instrukční mód** – jedna instrukce vyvolá dvě paralelní akce: jednu v násobičce a jednu ve sčítačce
	- **Využití**: vyčíslování řad, FFT, ...
- Stránkovací jednotka: Stejná jako v 80386
- Grafická jednotka: Pro 3D grafiku z-Buffer
- Využití i860:
	- grafické a unixové stanice
	- jako speciální grafický koprocesor (Grafika v reálném čase)
# IEEE 754 | Matematický koprocesor Intel 80x87 k procesoru 80x86
- ![[Pasted image 20251126161213.png | 500]]
### Typy dat pro koprocesor 80x87
![[Pasted image 20251126161258.png | 500]]
![[Pasted image 20251126161317.png | 500]]