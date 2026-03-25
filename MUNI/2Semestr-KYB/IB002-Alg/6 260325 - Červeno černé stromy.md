- = binární vyhledávací strom splňující podmínky:
	1. Každý uzel je obarvený červenou, nebo černou barvou
	2. Kořen stromu je černý
	3. Každý vnitřní uzel má právě dva syny
	4. Listy stromu nenesou žádnou hodnotu, jsou označeny nil, a mají černou barvu
	5. Když je uzel červený, tak jeho otec je černý
	6. Pro každý uzel stromu platí, že všechny cesty z něj do listů obsahují stejný počet černých uzlů

- ![[Pasted image 20260325101506.png|400]]
- ![[Pasted image 20260325100553.png|200]]
- ![[Pasted image 20260325100615.png|350]]
- ![[Pasted image 20260325100641.png|240]]
- ![[Pasted image 20260325100701.png|350]]

- ![[Pasted image 20260325100740.png|350]]

- výška uzlu x je rovna počtu hran na nejdelší cestě z x do listu
- **černá výška** uzlu x, bh(x), je rovna počtu **černých** uzlů na cestě z x do listu
	- barvu uzlu x nezapočítávám do černé výšky uzlu x
	- díky vlastnosti 6 je černá výška dobře definovaná


- **Každý uzel červ. čer. stromu s výškou h má černou výšku alespoň h/2.**
	- Z vlastnosti 6 plyne, že v nejhorším případě je každý druhý uzel na cestě červený
- **V červeno č. stromu má každý podstrom s kořenem x alespoň $2^{bh(x)} - 1$ vnitřních uzlů.**

- Č. č. strom s *n* vnitřními uzly má výšku nejvýše
$$2\log_{2}{n + 1}$$
## Operace
- Search, Maximum, Minimum, Successor a Predecessor
- složitost O(log n)

- Insert a delete modifikují strom
### Rotace
- ![[Pasted image 20260325102322.png|400]]
- rotace zachovává vlastnost binárního vyhledávacího stromu
- O(1)
- může změnit výšku uzlů
- ![[Pasted image 20260325102520.png|350]]
```python
function LeftRotate( T , x )
	y = x .right
	if y is None then return
	x.right = y.left
	if y.left is not None then
		y.left.parent = x
	y.parent = x.parent
	if x.parent is None then
		T.root = y
	else
		if x == x.parent.left then
			x.parent.left = y
		else
			x.parent.right = y
	y.left = x
	x.parent = y
```

### Přidání nového uzlu
- uzel do stromu přidáme stejným postupem jako do binárního vyhl. stromu
- jakou barvou máme obarvit nový uzel? (obě špatně ale červenou)
	- musíme vykonat korekci
#### Případ 1
- ![[Pasted image 20260325103447.png|500]]
#### Případ 2
- ![[Pasted image 20260325103514.png|500]]
#### Případ 3
- ![[Pasted image 20260325103540.png|500]]

#### Příklad:
- ![[Pasted image 20260325103719.png|400]]
- ![[Pasted image 20260325103732.png|400]]
- ![[Pasted image 20260325103744.png|400]]
- ![[Pasted image 20260325103801.png|400]]

```python
function RbInsert(T, a)
	BstInsert (T, a)
	a.color = red
	while a 6= T.root ∧ a.parent.color == red do
		if a.parent == a.parent.parent.left then
			d = a.parent.parent.right
			if d.color == red then
				#case 1
				a.parent.color = black
				d.color = black
				a.parent.parent.color = red
				a = a.parent.parent
			else
				if a == a.parent.right then
					#case 2
					a = a.parent
					LeftRotate (T, a)
				else
					#case 3
					a.parent.color = black
					a.parent.parent.color = red
					RightRotate (T, a.parent.parent)
		else
			stejně jako then se záměnou left a right
	T.root.color = black
```
#### Složitost přidání nového uzlu
- case 1: změna obarvení 3 uzlů
- case 2 a 3: jedna nebo dvě rotace a změna obarvení 2 uzlů
- celková složitost O(log n)

### Odstranění uzlu
- uzel ze stromu odstraníme stejným postupem jako z binárního vyhledávacího stromu
- v případě, že odstraněný uzel měl červenou barvu, vlastnosti stromu zůstávají zachované
- v případě, že měl černou barvu, může dojít k porušení vlastnosti 4 (stejná černá výška)
- černou barvu z odstraněného uzlu přesouváme směrem ke kořenu tak, abychom obnovili platnost vlastnosti 4
#### Nemá syna
- ![[Pasted image 20260325105748.png|400]]
#### Má jednoho syna
- ![[Pasted image 20260325105847.png|400]]
#### Má dva syny
- ![[Pasted image 20260325105913.png|400]]
### Korekce dvou barev
#### Uzel *a* má červenou a černou barvu
- obarvi uzel *a* na černou barvu
- ![[Pasted image 20260325110542.png|500]]
#### Případ 1
- uzel a má dvě černé barvy; bretr c uzlu a je červený
- ![[Pasted image 20260325110636.png|500]]
#### Případ 2
- uzel a má dvě černé barvy+ bratr c a jeho synové d, e mají černou barvu
- ![[Pasted image 20260325110724.png|350]]
#### Případ 3
- uzel a má dvě černé barvy; bratr c a jeho pravý syn e mají černou barvu, levý syn d je červený
- ![[Pasted image 20260325110820.png|500]]
#### Případ 4
- uzel a má dvě černé bravy; bratr c má černou barvu, jeho pravý syn e má červenou barvu
- ![[Pasted image 20260325110916.png|500]]
#### Složitost odstranění uzlu a korekce dvou barev
- O(log n)

## Červenou černé stromy - **Rank prvku**
### Pořadí (rank) prvku
- rank prvku
	- množina *A* obsahující *n* vzájemně různých čísel
	- číslo $x \in A$ má rank *i* právě když v *A* existuje přesně *i* - 1 čísel menších než *x*
- problém ranku
	- určit rank zadaného čísla
	- najít číslo se zadaným rankem
- řešení
	- jestliže prvky A jsou uložené v poli, tak v čase O(n) můžeme najít číslo s rankem *i* a určit rank daného čísla
	- existuje efektivnější řešení?
	- při použití č. č. stromů dokážeme oba problémy vyřešit v čase O(log n)
### Rozšíření RB stromů
- x
### Princip
- ![[Pasted image 20260325112436.png|400]]
### Vyhledání klíče s daným rankem
```python
function RbSelect(x, i)
	r = x.left.size + 1
	if i == r then
		return x
	else
		if i < r then
			return RbSelect (x.left, i)
		else
			return RbSelect (x.right, i − r)
```
