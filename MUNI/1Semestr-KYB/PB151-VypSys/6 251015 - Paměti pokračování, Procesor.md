## Permanentní paměti
- paměti určené pouze pro čtení
- základem je ROM (read-only memory)
- ![[Pasted image 20251015140209.png|300]]
### PROM (programable ROM)
- OTP ROM = One time programable
- s tavnou spojkou NiCr
- ![[Pasted image 20251015140353.png|150]]
### EPROM (erasable PROM)
- mazání - působením UV záření (cca 20 min speciální lampou) -> elektrony se rozptýlí.
- programování - elektricky; elektrony se shromáždí na jediné straně přechodu
### EEPROM (electrically EPROM)
- mazání elektrickým proudem = RMM (read mostly memory)
## Asociativní paměť
- = CAM (contents addressable memory)
- ![[Pasted image 20251015140835.png | 450]]
### Zapojení 1 bitu klíče:
- ![[Pasted image 20251015140937.png | 450]]
# Procesor
- synchronní stroj řízený řadičem
- Základní frekvence = **takt procesoru**
- **Strojový cyklus** = čas potřebný k zápisu (čtení) slova z paměti (např. 3 takty)
- **Instrukční cyklus** = čas potřebných pro výběr a provedení instrukce
- Příklad formátu instrukce:
	- ![[Pasted image 20251015141211.png | 500]]
## Charakteristika procesoru
- Fáze procesoru:
	- výběr
		- operačního kódu z paměti
		- operandu / adresy operandu z paměti
	- provedení instrukce
	- přerušení
- Výběr instrukcí je řízen registrem:
	- čítač instrukcí (adres)
	- PC (Program Counter)
	- IP (Instruction Pointer, alternativní název k PC)
- Po provedení instrukce se zvyšuje o délku instrukce. Plní se např. instrukcí skoku, ...
### Počítač
- pracující ve dvojkovém doplňkovém kódu
- registry
	- A - střádač - 8bitový (bajt) (Accumulator)
	- PC - sčítač instrukcí - 16bitový (slovo) (Program Counter)
- paměť
	- 64 KB
	- adresovaná jednotka = bajt
	- PC - 16bitový
	- data - 8bitová

- #### příklad - zapojení mikroprocesoru Intel 8080 (1974) - 8bitový procesor
	- negWR - Write, řízení zápisu do paměti
	- Φ1, Φ2 – impulsy vnějších hodin
		- ![[Pasted image 20251015142349.png |  250]]
	- ![[Pasted image 20251015142405.png | 300]]

### I. část instrukčního souboru
- LDA adresa - Load A Direct
	- naplní registr A obsahem bajtu z paměti
	- uložení instrukce v paměti:
		- ![[Pasted image 20251015142700.png | 350]]
- STA adresa - Store A Direct
	- Uloží reg, A do paměti
	- uložení instrukce v paměti
		- ![[Pasted image 20251015142758.png | 350]]
- JMP adresa - Jump Unconditional
	- nepodmíněný skok na adresu
	- uložení instrukce v paměti:
		- ![[Pasted image 20251015142904.png | 350]]

- Příklad:
	- X := Y;
		- LDA 101h
		- STA 100h
	- Proměnné v paměti:
		- 100h X
		- 101h Y
	- Instrukce v paměti:
		- 200h LDA 101h
		- 203h STA 100h
		- 206h ...
	- ![[Pasted image 20251015143119.png | 450]]
## Instrukce a mikroinstrukce
### Interní registry
- IR - instrukční registr (8bitový)
	- je napojen na dekodér instrukcí (řadič)
- DR - datový registr (8bitový)
	- registr pro čtení/zápis dat z/do paměti
- AR - adresový registr (16bitový)
	- adresa pro čtení/zápis z/do paměti
- TA = (TAh, TAl) - Temporary Address Register (16bitový)
	- TAh (TA High - 8 bitů)
	- TAl (TA Low - 8 bitů)
### Fáze procesoru (mikroinstrukce)
- Fáze instrukce LDA adresa
	- 0 čti při WR
- ![[Pasted image 20251015145506.png | 350]]
- Fáze instrukce STA adresa
- ![[Pasted image 20251015145551.png | 250]]
- Fáze instrukce JMP adresa
- ![[Pasted image 20251015145633.png | 250]]
### Další registry a Fáze MOV
- B, C, D, E, H , L (8bitové)
- instrukce přesunu mezi registry:
	- MOV r1, r2        ri = {A,B,C,D,E,H,L}        r1 ← r2
	- kódování - 1 bajt (kombinace registrů je součástí operačního znaku)
- Fáze MOV r1, r2
	- ![[Pasted image 20251015150313.png | 250]]

### Emulátor
https://is.muni.cz/auth/edutools/brandejs/cpu_emu?cpu=8080


### Aritmetické instrukce
- Fáze instrukce INR r (Increment Register)
- ![[Pasted image 20251015150604.png | 250]]
- Fáze instrukce ADD r (Add Register to A)
- ![[Pasted image 20251015150759.png | 250]]
- Fáze instrukce CMA (Complement A = inverze všech bitů)
- ![[Pasted image 20251015150834.png | 250]]
### Příznakový registr F procesoru I8080
- Z (Zero) - = 1 při nulovém výsledku operace
		  - = 0 při nenulovém
- S (Sign) Kopie znaménkového bitu výsledku operace
- CY (Carry) Kopie bitu přenášeného z nejvyššího řádu výsledku operace
	- ![[Pasted image 20251015155824.png | 300]]
- P (Parity) - = 1 při sudé paritě výsledku
		   - = 0 při liché paritě výsledku 
- AC (Auxilary Carry) přenos mezi bitem 3 a 4 výsledku
	- ![[Pasted image 20251015160015.png | 300]]