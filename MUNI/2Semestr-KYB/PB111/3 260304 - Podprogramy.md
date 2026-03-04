# 3
## 3.1 Podprogramy abstraktně
### 3.1.1 Účel
- podprogram popisuje výpočet
- parametrizace -> různé výpočty
- použití (volání) je výraz
- lze používat opakovaně (i staticky)
### 3.1.2 Zápis
- definice:
	- návratový typ, jméno
	- formální parametry
	- tělo (složený příkaz)
- použití (volání)
	- jméno + skutečné parametry
### 3.1.3 Vstupy a výstupy
- zatím velmi jednoduché
	- parametry
	- návratová hodnota
	- částečná uzavřenost
- důsledek: pouze čisté funkce
### 3.1.4 Sémantika
- čistá
	- nahrazení volání výsledkem
- obecně
	- nahrazení tělem?
	- výsledek + efekt
### 3.1.5 Parametry
- formální parametr ~ proměnná
	- má vlastní objekt
- předání parametru
	- jako inicializace proměnné
	- předání hodnotou
### 3.1.6 Typy
- návratový typ
	- patří výrazu volání
- typy parametrů
	- výraz skutečných param.
- kontrola použití bez těla
## 3.2 Operační paměť
### 3.2.1 Hardwarový zásobník
- oblast v paměti
- speciální registr `sp` = adresa
- souvisí s datovou strukturou
	- last in, first out
	- operace push, pop
	- sp ~ top
### 3.2.2 Sémantika push, pop
```c
push reg
	sub sp, 2 -> sp
	st reg -> sp
	
pop reg
	ld sp -> reg
	add sp, 2 -> sp
```
### 3.2.3 Předání řízení
- vstup: call
	- vstup do podprogramu
	- neřeší parametry
- konec: ret
	- ukončení podprogramu
	- neřeší návratovou hodnotu
### 3.2.4 Sémantika call
- pozastavení aktuálního podprogramu
- call addr (jeden krok!)
	- push pc
	- jmp fn
- provede přímý skok
- volání jsou LIFO -> zásobník
### 3.2.5 Sémantika ret
- ret ~ pop pc
	- nebo: pop X, jmp X
- nepřímý skok
- call/ret "závorkují" výpočet
### 3.2.6 Lokální proměnné
- hodnota se musí zachovat
- "zálohování" registrů
	- na zásobník (push, pop)
	- do rámce
- caller save vs callee save
### 3.2.7 Předávání parametrů
- přednostně v registrech
	- l1, l2, ...
	- další na zásobník
- podobně návratová hodnota (rv)
- složitější typy později
### 3.2.8 Volací sekvence
- $f( e_{1}, e_{2}, \dots, e_{n})$
	- vyhodnoť $e_{1}$ do $l_{1}$
	- vyhodnoť $e_{2}$ do $l_{1}$
	- atd. až po r2
	- call f
### 3.2.9 Rekurze
- použití v těle (definici)
- neznámá hloubka zanoření
- koncová vs obecná
## 3.3 Stav podprogramu
### 3.3.1 Rámec
- privátní paměť podprogramu
- alokuje se na zásobníku
- různé aktivace -> různé rámce
- pevná velikost
### 3.3.2 Dočasné objekty
- pro uložení dočasných hodnot
- zobecnění dočasného registru
- programátorovi nepřístupné
- mapování objekt -> uložiště
### 3.3.3 Přelití registru
- potřebujeme volný registru
- co když jsou všechny "živé"
- přesuneme hodnotu na zásobník
	- stejně jako při "zálohování"
### 3.3.4 Lokální paměť
- lokálních proměnných může být "moc"
- uložíme je na zásobník
- načtení do "dočasných" registrů
- příště: adresa proměnné
### 3.3.5 Tabulka symbolů
- obecně slovník identita -> informace
	- identita ~ jméno proměnné
	- pro překladač: informace = uložiště
- vstupně-výstupní parametr
- nese i informaci o volných registrech
### 3.3.6 Vyhodnocení proměnné
- vyhodnocujeme do R
- "žije" v registru:
	- copy vreg -> R
- "žije" na zásobníku:
	- ld bp, offset -> R
	- offset ~ přihrádka
### 3.3.7 Správa rámců
- při vstupu do programu:
	- push bp
	- copy sp -> bp
	- sub sp, N -> sp
- při výstupu:
	- copy bp -> sp
	- pop bp
### 3.3.8 Překlad podprogramu
- začneme prologem
- pokračujeme překladem těla
	- tělo je složený příkaz
- epilog je součástí return