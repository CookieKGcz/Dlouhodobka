## GCD
- greatest common divisor
- Vstup: přirozená čísla a, b; (alespoň jedno není 0)
- Výstup: (největší) přirozené, dělí a i b.
### Neideální algoritmus
- projede všechny čísla od 1 do menšího a, b.
- pro každé vyzkoušíme, zda dělí a i b.
- pro 0 by to nefungovalo (for loop), takže se ještě přidá if
```python
def gcd_naive(a, b): 
	if a == 0 or b == 0:
		return max(a, b)
	best = 0
	for i in range(1, min(a, b) + 1):
		if a % i == 0 and b % i == 0:
			best = i
	return best
```
### Školní algoritmus
- Rozložit a i b na součin prvočísel
- vybrat, co je společné, vynásobit
- např.: 504 = 2^3 . 3^2 . 7, 540 = 2^2 . 3^3 . 5  => 2^2 . 3^2 = 36
### Eukleidův algoritmus
- základní myšlenka: pokud a > b, pak gcd(a,b) = (a-b,b)
```python
def gcd(a, b):
	if a == 0:
		return b
	while b != 0:
		if a > b:
			a -= b
		else: b -= a
	return a
```
- V nejhorším případě může být pomalejší než naivní algoritmus; kdy? -> Co když jedno z čísel bude 1?
### Vylepšený Eukleidův algoritmus
- Lepší myšlenka: pokud a > b, pak gcd(a,b) = gcd(a mod b, b)
- a místo odčítání použijeme rovnou zbytek po dělení
```python
def gcd(a, b):
	while b != 0:
		aux = a % b
		a = b
		b = aux
	return a
```
- Poznámka: S využitím ntic (tuples) by se tělo cyklu dalo napsat takto: a, b = b, a % b
### Rekurzivní Eukleidův algoritmus
- o rekurzi bude řeč později
```python
def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)
```
### Efektivita algoritmů gcd
- Časová náročnost algoritmu (v nejhorším případě):
	- naivní, "školní": exponenciální vůči počtu cifer
	- Eukleidův (s odčítáním): exponenciální vůči počtu cifer
	- Eukleidův (s mod): lineární vůči počtu cifer
- Různé algoritmy mohou řešit tentýž problém různě rychle.
## Seznamy
### Motivace pro seznamy
- Chceme zpracovávat větší množství položek
- Nechceme psát opakovaně stejný kód
- Nemusíme předem znát počet položek
Příklady:
- Seznam studentů seřazených nějakým zp.
- Úlohy čekající na zpracování
- Cesta grafem
- Reprezentace herního plánu (šachy)
### About Seznamy
- *Sekvence libovolného počtu položek*
- Podobné typy běžně dostupné v jiných jazycích:
	- pole (array) - pevná délka, všechny položky stejného typu
	- dynamické pole, různé jiné druhy seznamů,...
- Seznamy v pythonu - obecnější než pole:
	- umí měnit velikost,
	- smí obsahovat položky různých druhů (každá položka odkazuje na objekt, jako proměnné)
	- Omezíme se ale na položky stejného typu (výjimka None)
### Vytvoření seznamu
- Výčtem prvků:
```python
s = []
s = [3, 1, 4, 1, 5]
s = ["ABC", 3.14, -7]
s = [[1, 2], [3, 4]]
s = ["pes", "kočka", 0.01, ["velbloud", -13], []]
```
- Tzv. list comprehension (intenzionální zápis seznamu)
```python
s = [2 * x for x in range(10)]
s = [x ** 2 for x in range(1, 10) if x % 2 == 0]
s = [3 * x for x in [5, 17, 23, 40]]
s = [[a, b, c] for a in range(1, 10)
	for b in range(1, 10)
	for c in range(1, 10)
	if a ** 2 + b ** 2 == c ** 2]
```
### Seznamy - Základní operace
- Zjištění délky seznamu: len(s)
- Přidání prvku na konec seznamu: s.append(x)
- Odebrání prvku z konce seznamu: s.pop().

- Indexování (výběr) s\[0], s\[1], ...
	- pro čtení i zápis
- Indexování od konce: s\[-1], s\[-2], ...

- Kopie seznamu s.copy()
	- Totéž jako \[x for x in s]
### Indexování seznamů
- Indexování od nuly
	- první prvek seznamu je s \[0]
	- má své důvody (https://en.wikipedia.org/wiki/Zero-based_numbering)
### Procházení seznamu
- Máme seznamy my_list a chceme postupně projít všechny jeho prvky - jak na to?
-  Ne úplně vhodné řešení
```python
for i in range(len(my_list)): # BAD
	do_something(my_list[i])
```
-  Lepší řešení
```python
for element in my_list:
	do_something(element)
```

- Co když potřebujeme jak prvky seznamu, tak jejich indexy?
```python
for i, element in enumerate(my_list):
	do_something(i, element)
```
- i bude postupně nabývat hodnot 0, 1, 2...
- element bude prvek my_list\[i]

- **Doporučení**:
	- Nemodifikujte datovou strukturu, kterou zrovna procházíte v cyklu `for`.
```python
for elem in my_list:
	if elem > 2:
		my_list.pop() # BAD
```
- **Alternativa**:
	- `while` cyklus s vhodnou podmínkou
	- Prochází kopie: `for` elem `in` my_list.copy()
### Odbočka - Proměnné
- Proměnná v Pythonu
	- Má jméno, existuje v nějakém kontextu, může mít typ a může mít vazbu (odkaz) na objekt ("místo v paměti")
- Přiřazení v různých jazycích:
	- Ve stylu C (Pascal apod.):
		- změna hodnoty uložené v objektu
		- (vazba proměnné k objektu je pevná)
	- Ve stylu Pythonu:
		- přesměrování odkazu (vazby) na jiný objekt
		- (vazba proměnné objektu se může měnit)
- pozn.: U neměnných (immutable) typu čísla, řetězce nepozorujeme v Pythonu žádný rozdíl
### Odbočka - Proměnné v Py
- **Ilustrace přiřazení:**
![[Pasted image 20251003110455.png | 400]]
### Seznamy a proměnné v Py
```python
s = [1, 2, 3]
t = s
s.append(4)
```
- Jakou hodnotu má proměnná t?
	- \[1, 2, 3, 4]
	- přiřazení proměnné v Pythonu mění vazbu !!
- s.copy()
	- pozor, jedná se o mělkou kopii (jen kopie hlavní úrovně seznamu (vadí když v seznamu máme seznamy))
		- U seznamy seznamů apod. nutno případně provést i **kopie zanořených seznamů**!
### Seznamy a volání funkcí v Py
```python
def fun_1(x):
	x = 17

y = 10
fun_1(y)
```
- Jakou hodnotu má proměnná y?
	- 10
	- fun_1 nemění hodnotu skutečného parametru. (ani nemůže, čísla jsou v Pythonu neměnná)
	- Změní vazbu formálního parametru x

```python
def fun_2(s):
	s.append(17)

t = [1, 2]
fun_2(t)
```
- Jakou hodnotu má proměnná t? \[1, 2, 17]
	- fun_2 mění hodnotu skutečného parametru.
		- Vazba formálního parametru na skutečný funguje stejně jako přiřazení, s a t pak odkazují na stejný objekt.
	- Vyzkoušejte změnit tělo funkce na s = \[17] nebo s\[0] = 17 a pozorujte efekt.

```python
def fun_3(s):
	s.append(17)
	s = [4, 5] # už se vazba mění
	s.append(19)
	
t = [1, 2]
fun(t)
```
- Jakou hodnotu má proměnná t? \[1, 2, 17]
	- s bude mít ve funkci na konci hodnotu \[4, 5, 19]

```python
def fun_4(t):
	t.append(0)

def fun_5(a, b, c):
	s = [a, b, c]
	fun_4(s)
	
fun_5(1, 2, 3)
```
- Jsou uvedené funkce čisté?
	- fun_4 ne, fun_5 ano
### Vsuvka: další příklad na čistotu
```python
def fun_6(n, do_print):
	if do_print:
		print(n)
	return n+1

def fun_7(n):
	return fun_6(n, False)
	
fun_7(0)
```
- Jsou uvedené funkce čisté?
	- fun_6 ne, fun_7 ano
		- pokud nemáme záruku že to vždy bude false tak by byla taky nečistá
### Seznamy  - Odvozené operace
- Součet prvků seznamu: sum(s)
	- Součet prázdného seznamu je 0
- Maximum/minimum neprázdného seznamu: max(s), min(s)
- (další přibydou později)
- Umíme i naprogramovat pomocí základních fce:
```python
def my_sum(data):
	total = 0
	for element in data:
		total += element
	return total
```
## Ntice
### Ntice (Tuples)
- *Kolekce pevné velikosti, s pevnou hlavní typovou úrovní prvků.*
- Hodnoty prvků se dají měnit, pokud to jejich typ připouští.
- V tomto předmětu nebudeme ntice indexovat.
- Zápis: kulaté závorky místo hranatých,
	- v jistých situacích se kulaté závorky smí vynechat
- `s = (1, "A", 3)`
- Typická použití - jednoduchá strukturovaná data:
	- souřadnice (x, y),
	- barva pixelu (red, green, blue)
	- vracení více hodnot z funkce, ...
- Ntice velikosti 1: (x,) - Pythonovská specialita
### Použití ntic
- Rozbalení ntice
```python
data = ("Rick Sanchez", "C-137", "Earth")
name, dimension, planet = data

children = [
	(1, "Henry"),
	(8, "Kali"),
	(11, "Jane"),
]

for number, name in children:
	pass # do something with number, name
	
a, b = 10, 17
```
- Prohození hodnot proměnných (SWAP)
```python
a, b = b, a # the same as (a, b) = (b, a)
```
- Vracení více hodnot z funkce
```python
def minmax(a, b):
	return min(a, b), max(a, b)

x, y = minmax(9.7, 3.14)

quot, rem = divmod(17, 5) # standard Python function
```
### Porovnání seznamů a ntic
- **Lexikografické uspořádání** (Jako ve slovníku)
	- Na dvojicích:
	- `(a, b) < (c, d)`
	- je totéž, co
	- `a < c or (a == c and b < d)`
	- Na nticích stejné délky:
		- podobně; výsledek je podle první dvojice, která se nerovná.
	- Na nticích různé délky/seznamech:
		- podobně; je-li s vlastním prefixem (začátkem) t, pak s < t.
### Příklad: Řešení hádanky z 1. přednášky
```python
def solve_hens_pigs_puzzle(heads, legs):
	for hens in range(heads + 1):
		pigs = heads - hens
		if 2 * hens + 4 * pigs == legs:
			return (hens, pigs)
	return None
```
### Příklad: Dělitelé čísla
```python
def divisors(num):
	result = []
	for divisor in range(1, num + 1):
		if num % divisor == 0:
			result.append(divisor)
	return result
```
- Dalo by se nějak vylepšit?
	- Počítat jen do num // 2 (a přidat num na konec)
	- Využít toho, že divisor a num // divisor jsou oba děliteli, menší z těch dvou dělitelů je <= odmocnině z num.
- Pro zajímavost (použití intenzionálních seznamů):
```python
def divisors_alt(num):
	return [divisor for divisor in range(1, num + 1)
		if num % divisor == 0]
```
### Příklad: Prvočísla – Eratosthenovo síto
implementace:
```python
def sieve(limit):
	result = []
	is_prime = [True for _ in range(limit)]
	
	for p in range(2, limit):
		if is_prime[p]:
			result.append(p)
			for mult in range(p * p, limit, p):
				is_prime[mult] = False
	
	return result
```
### Vnořené seznamy
### Příklad: Nulová matice zadaných rozměrů
### Příklad: Matice souřadnic
### Odbočka: Násobení matic
### Příklad: Násobení matic