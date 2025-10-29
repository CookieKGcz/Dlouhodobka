### Příznakový registr F procesoru I8080
- Z (Zero) = 1 při nulovém výsledku operace
		 = 0 při nenulovém
- S (Sign) Kopie znaménkového bitu výsledku operace
- CY (Carry) Kopie bitu přenášeného z nejvyššího řádu výsledku operace
	- ![[Pasted image 20251015155824.png | 300]]
- P (Parity) - = 1 při sudé paritě výsledku
		   - = 0 při liché paritě výsledku 
- AC (Auxilary Carry) přenos mezi bitem 3 a 4 výsledku
	- ![[Pasted image 20251015160015.png | 300]]
```asm6502
S konstantou ale dvojbytový

soucet    db -5
          lda soucet
          adi 5
		  sta soucet
		  hlt
```

```asm6502
soucet    db -5
k5        db 5

          lda k5
          mov b, a (do b přesuň a)
          lda soucet
          add b
		  sta soucet
		  hlt

Příznaky (Flags):
S = 0
Z = 1
A = 1
P = 1
C = 1
```

## Příznaky
- Příznaky nastavují instrukce: ADD, INR (INR nenastavuje CY)
- Příznaky nemění instrukce: LDA, STA, JMP, MOV, CMA

- Fáze instrukce CMP r (Compare Register with A)
- ![[Pasted image 20251022144806.png | 200]]
	- pouze se nastaví příznaky

# Větvení
## Podmíněné skoky
- tj. skoky podle obsahu příznakového registru
- Vzor instrukce: ==***Jpodmínka adresa***==
- ![[Pasted image 20251022150401.png | 350]]
## Instrukce
- JC       CY = 1
- JNC    CY = 0
- JZ       Z = 1
- JNZ    Z = 0
- JP       S = 0
- JM      S = 1
### Příklady
- X ... 100h
- Y ... 101h
```asm6502
X := X + Y

LDA 100h
MOV B, A
LDA 101h
ADD B
STA 100h
```

```asm6502
X := X - Y

LDA 100h
MOV B, A
LDA 101h
CMA
INR A
ADD B
STA 100h
```

```asm6502
if X=Y then ANO else NE;

	LDA 100h
	MOV B, A
	LDA 101h
	CMP B      ; A-B
	JNZ NE
ANO:
	...
	JMP VEN
NE:
	...
VEN:
```

```asm6502
if X<Y then ANO else NE;

	LDA 100h
	MOV B, A
	LDA 101h
	CMP B     ; X-Y
	JP NE
ANO:
	...
	JMP VEN
NE:
	...
VEN:
```

```asm6502
if X<=Y then ANO else NE;

	LDA 100h
	MOV B, A
	LDA 101h
	CMP B     ; X-Y
	JM NE
ANO:
	...
	JMP VEN
NE:
	...
VEN:
```

```asm6502
while i>=X do BLOK;

102h i

OPAKUJ: LDA 100h
	MOV B, A
	LDA 102h
	CMP B     ; i-X
	JP BLOK
	JMP KONEC
BLOK:
	...
	JMP OPAKUJ
KONEC:
```
### Uložení instrukcí v paměti
- for i:= 1 to X do B;
- ![[Pasted image 20251022152645.png | 300]]
```asm6502
soucet    db 1

          lda soucet
zpet      inr a
          jm koencs
          jmp zpet
konec     hlt
```
# Zásobník
- Struktura Last - in, First - out (LIFO)
- Umístění kdekoli v operační paměti
- ![[Pasted image 20251022152944.png | 350]]

- Zásobník roste od vyšších adres k nižším:
- ![[Pasted image 20251022153212.png | 300]]

 - Registr SP  =  Stack Pointer (16bitový)
 - Plnění SP instrukcí LXI SP, hodnota    =    Load Immediate
 - Fáze instrukce:
 - ![[Pasted image 20251022153354.png | 350]]
## Práce se zásobníkem
- Instrukce:
	- PUSH B | D | H | PSW
	- POP B   | D | H | PSW

- Fáze instrukce PUSH B | D | H | PSW
- ![[Pasted image 20251022153535.png | 400]]
- Fl (Flags, příznaky uspořádané do registru)

- Fáze instrukce POP B   | D | H | PSW
- ![[Pasted image 20251022153631.png | 400]]
### Příklad
- LXI SP,1000h
- PUSH B
- PUSH D
- ![[Pasted image 20251022153710.png | 300]]
- Pozor, žádná kontrola podtečení!

## Zásobník a volání podprogramu
- Instrukce:
	- CALL adresa
	- RET
- Příklad:
- ![[Pasted image 20251022153812.png | 400]]

- Fáze instrukce CALL
- ![[Pasted image 20251022153836.png | 350]]

- Fáze instrukce RET:
- ![[Pasted image 20251022153854.png | 300]]
## Instrukce nepřímého ...
??????????
![[Pasted image 20251022162421.png | 300]]
# V/V operace
- Instrukce
	- OUT zapíše obsah A na V/V sběrnici
	- IN přečte obsah V/V sběrnice do A
	- START zahájí V/V operaci
	- FLAG adresa skok na adresu, není-li operace hotova
- ![[Pasted image 20251022162652.png | 350]]
## Příklady
- Přenos A_100h do výstupního zařízení
```asm6502
1000h LDA 100h
1003h OUT
1004h START
1005h FLAG 1005h
1008h
```
- Čtení vstupního zařízení a uložení do A_100h
```asm6502
1000h START
1001h FLAG 1001h
1004h IN
1005h STA 100h
1008h
```
- Pojem `time-out`
