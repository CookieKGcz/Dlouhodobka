## Struktura programu
### Sekvenční řazení příkazů
- Pod sebe, jeden příkaz na řádek
- Můžeme oddělovat ; na jednom řádku
- Příliš dlouhý řádek můžeme rozdělit na více řádků:
	- použití /
## Cyklus *for*
- for v pythonu je obecnější:
	- range(...) je jeden z druhů
	- dalšími jsou seznamy, množiny
- ### range
	- Základní verze range(stop)
		- postupně procházíme čísla 0 až stop - 1 včetně
	- range(start, stop)
	- range(start, stop, step)
		- procházíme čísla od start, velikost jednoho kroku step, skončíme před stop
	- Počítat pozpátku s neg výrokem
## Vztah cyklů *for* a *while*
```python
total = 0
for i in range(10, 100, 7):
	total += i
```

*Jak napsat cyklus for pomocí cyklu while?*

```python
total = 0
i = 10
while i < 100:
	total += i
	i += 7
```
### Pozor!
- když skončí cyklus range, i = 94
- když skončí while i = 101
	- total je stejný, ale i máme jiné
## Ternární operátor *if ... else*
- nejprve se vyhodnotí podmínka
- Pokud je pravdivá, vyhodnotí se výraz1
- V opačném případě se vyhodnotí výraz2
- Část *else* … je v tomto případě povinná.
## Podprogramy
- programy se dále dělí na podprogramy
- Ty dále můžeme dále dělit na (menší) podprogramy.
- prostě *def*

- Podprogram: úsek kódu, který má navíc název parametry a návratovou hodnotu.

- V Pythonu realizujeme pomocí funkcí:
```python
def ppgm(x_1, …, x_n):
	příkaz_1
	# ...
	příkaz_m
```
- ppgm je **jméno**.
- x_i jsou jména **formálních paramatrů**,
- příkaz_1 … příkaz_m je **tělo** podprogramu.
## Volání podprogramů
- Volání podprogramu - výraz ppgm(e_1, ..., e_m):
	- e_i - výrazy: vyhodnotí se na skutečné parametry (argumenty),
	- jména formálních paramterů se sváží se skutečnými parametry.
- Příkaz return či return expr.
	- Ukončí běh programu, vrátí None či hodnotu výrazu expr.
- Vnořené volání podprogramů
	- podprogramy mohou volat další podprogramy
	- po dokončení vnořeného podprogramu se běh vrátí do místa, odkud se podprogram zavolal
## Funkce: příklad
- *what is the value of series_sum(42)?*
```python
def series_sum(num):
	total = 0
	for i in range(1, num + 1):
		total += i
		return total
```
- Lepší řešení?
```python
return num * (num + 1) // 2
```
## Lokální proměnné podprogramu
- Jejich jméno je viditelné lokálně pouze v daném podprogramu:
	- buď se jedná o formální parametr,
	- nebo vznikají lokálním příkazen.
- Každá invokace funkce má své vlastní lokální proměnné.
	- Stejné jméno, ale jiná kontext!
	- Platí i pro rekurzivní invokace.
## Příklad: lokální proměnné
```python
def inner(n):
	x = 2 * n
	return x + 11
	
def outer(n):
	x = 3 * n
	y = inner(n + 7)
	return x + y
	
x = 17
n = 33
result = outer(9)
```

- x(local) --> 17
- n(local) --> 33
- n(outer) --> 9
- x(outer) --> 27
- n(inner) --> 16
- x(inner) --> 32
- inner se ukončí
- y(outer) --> 43
- outer se ukončí
- result(local) --> 70
## Vedlejší efekty podprogramů
- Mimo vrácení návratové hodnoty podprogram může mít další vně pozorovatelné efekty.
- Chápání se může lišit, ale typicky jde o změnu:
	- hodnoty objektu dostupného v programu i vně daného podprogramu (pokud to typ objektu povoluje)
	- stavu výpočetního systému vně daného běžícího programu
		- Změna obsahu souborů, jejich atributů, přístupových časů, ...
	- Obvykle ale nepočítáme spotřebu paměti, energie apod.
- ![[Pasted image 20250926104704.png | 500]]
## Čisté funkce
- **Čistá funkce** - pokud při jejím provádění nenastane chyba mimo funkci samotnou (výpadek napájení, nedostatek paměti, ...), pak:
	- pro stejné vstupy buď vždy skončí, nebo vždy neskončí;
	- pokud skončí, pak skončí se stejnými hodnotami;
	- nemá mimo svého provedení vrácení výsledku žádný vně pozorovatelný efekt, a to ani dočasně
- Nečistota funkce může být způsobena i podprogramem z ní volaným!
	- Ale pozor: neplatí to vždy!
- **Predikát**: čistá funkce, která vrací True nebo False
- **Procedura**: podprogram, jehož hlavní účel je nějaký vedlejší efekt.
## Doporučení pro psaní funkcí
- Nejprve si ujasnit specifikaci (vstupně/výstupní chování):
	- Jaké potřebuje funkce vstupy?
	- Co bude výstupem funkce?
- Funkce by měly být krátké.
	- "Jedna myšlenka."
	- Funkce by měla vejít na jednu obrazovku.
	- Jen několik úrovní zanoření.
- Co když je funkce příliš dlouhá?
	- Najít v ní menší logické celky.
	- Rozdělit na menší funkce.
## Datové typy
- Co je hodnotou výrazu 3 + "Ježek" v Pythonu?
	- TypeError: unsupported operand type(s) for +: 'int' and 'str'
- Velká část jazyků vyžaduje typové deklarace proměnných:
	- proměnná smí obsahovat hodnoty jen zadaného typu,
	- typová kontrola se provádí před spuštěním programu.
- Proměnné v Pythonu mohou mít hodnoty libovolných typů.
	- Python je silně typovaný dynamický jazyk.
	- Typová kontrola se provádí za běhu!
- Python (od verze 3.6) má nepovinné typové anotace.
	- Umožňují typovou kontrolu před spuštěním programu
## Základní typy hodnot v Pythonu
- Celá čísla - int:
	- od Pythonu 3 libovolně velká
- Čísla s plovoucí řádovou čárkou - float:
	- omezená přesnost (IEEE floating point)
- Řetězce - str:
	- víceřádkové uvnitř """ ... """
- Pravdivostní hodnoty - bool:
- Seznamy, ntice, slovníky, ... (uvidíme později)
## Speciální hodnota *None*
- Explicitní označení "Žádné hodnoty".
- Test na None (dle PEP8)
	- x is None nebo x is not None.
	- Jinde is nepoužívejte - není to totéž, co \==.
## Typové konverze
- Implicitní (dělají se automaticky)
- Explicitní (je třeba si o ně říct)
	- float(num)
	- round(fnum)
	- V knihovně math:
		- floor(fnum)
		- ceil(fnum)
		- trunc(fnum)
## Zásady čitelnosti kódu
- PEP8
## DRY
- Dry = Don't Repeat Yourself
## Příklad: Přestupný rok
Chceme napsat predikát is_leap, který nám řekne, zda je zadaný rok přestupný v gregoriánském kalendáři.
Pravidla:
- Rok je přestupný, pokud je dělitelný číslem 4. 
- Výjimka: Rok není přestupný, pokud je dělitelný 100. 
- Výjimka z výjimky: Rok je přestupný, pokud je dělitelný 400.
### Ne moc pěkné řešení 
```python
def is_leap(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else: return False
		else: return True
	else: return False
```
### Lepší řešení
```python
def is_leap(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

## Příklad: Ciferný součet
- Vstup: přirozené číslo 𝑛. 
- Výstup: ciferný součet čísla 𝑛 (v desítkové soustavě). 
- Příklady konkrétního vstupu a výstupu: 
- 0 → 0 
- 7 → 7 
- 17 → 8 
- 42 → 6 
- 999 → 27 
- 72525 → 21

### Myšlenka řešení i řešení
- Poslední číslice z čísla: zbytek po dělení deseti
- Odebrání poslední číslice: celočíselné dělení deseti
- Opakovat tak dlouho, dokud číslo není 0.

```python
def digit_sum(n):
	result = 0 while n > 0:
		result += n % 10
		n = n // 10
	return result
```

## Výpočet odmocniny
```python
def square_root(x, precision):
	lower = 0.0
	upper = x
	middle = (lower + upper) / 2
	while abs(middle ** 2 - x) > precision:
		if middle ** 2 > x:
			upper = middle
		elif middle ** 2 < x:
			lower = middle
		middle = (lower + upper) / 2
	return middle
```
- nevyjde pro hodnotu < 1 (0.5 atd.)
## Ladění (debugging)
- Příkazový řádek: python -m pdb jméno.py
## Základní typy chyb
- SyntaxError (chyba při spuštění) -> chybějící dvojtečka..
- IdentationError (chyba při spuštění) -> špatné odsazení.
- NameError špatné jméno proměnné: překlep v názvu, chybějící inicializace proměnné.
- TypeError špatný typ pro danou operaci -> sčítaní čísla a řetězce
- IndexError chyba při indexování řetězce, seznamu apod. (uvidíme časem)