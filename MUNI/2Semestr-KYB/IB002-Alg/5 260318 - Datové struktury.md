## Datové typy
### Datový typ
- rozsah hodnot, které může nabývat proměnná daného datového typu
- množina operací, které jsou pro daný datový typ povolené / definované
- nezávisí na konkrétní implementaci
### Jednoduchý (skalární) datový typ
- data zabírají vždy konstantní (typicky malé) množství paměti
- zpřístupnění hodnoty skalárního typu trvá konstantní čas
- číselné a znakové typy, typ pravdivostních hodnot, výčtový typ
### Složený datový typ
- Statický
	- pevná velikost; časová složitost zpřístupnění prvku je konstantní
	- k-tice, pole fixní délky
- Dynamický
	- neomezená velikost; časová složitost zpřístupnění prvku je funkcí závislou na velikosti
	- seznam, zásobník, fronta, slovník, strom, graf
### Dynamické datové typy
- množina objektů; v průběhu výpočtu můžeme do množiny prvky přidávat a odebírat resp. množinu jinak modifikovat
- každý prvek dyn. mn. je reprezentovaný jako objekt, jehož atributy můžeme zkoumat a modifikovat za předpokladu, že máme ukazatele / referenci na tento objekt
- jeden z atributů objektu je jeho identifikátor - klíč
- jestliže všechny prvky mají různé klíče, často mluvíme o množině obsahující klíče
### Základní operace
- Search(S, k)
- Insert(S, x)
- Delete(S, x)
- Maximum(S)
- Minimum(S)
- Successor(S, x)
- Predecessor(S, x)
# Binární vyhledávácí stromy
## Problém rezervací
- online rezervační systém
	- je daná množina rezervací R délky k
	- rezervace t může být potvrzena právě tehdy když v R není žádná rezervace v intervalu (T - k, t + k) a současně t je aktuální
	- operace: ověřování rezervace, přidání potvrzené rezervace do R, odstraňování "prošlých" rezervací
- příklad
	- k = 3, R = \{21, 26, 29, 36}
	- rezervace 24 nemůže být potvrzena protože je v kolizi s rezervací 26
	- rezervace 33 může být potvrzena

## Vyhledávací stromy
- datová struktura pro reprezentaci množiny prvků, nad kterými je definované úplné uspořádání
## Binární vyhledávací stromy (BVS)
- kořenový strom, v němž každý uzel má nejvýše dva následníky
- každý uzel stromu představuje jeden objekt, obsahující:
	- klíč key
	- ukazatel left, right a parent na levého syn, na pravého syna a na otce; ukazatel má hodnotu None právě když uzel nemá příslušného syna resp. otce
- klíče všech objektů jsou porovnatelné a vzájemně různé
- pro všechny uzly binárního vyhledávacího stromu platí: jestliže
	- y je uzel v levém podstromu uzlu x, tak y.key < x.key
	- y je uzel v pravém podstromu uzlu x, tak y.key > x.key

- ![[Pasted image 20260318102033.png|300]]
## BVS: Procházení stromu
- cílem je projít strom tak, aby každý uzel byl navštíven právě jednou
- využití: provedení operace nad každým uzlem, výpis klíčů, kontrola vlastností stromu, ...

- strom procházíme rekurzivně
- začínáme v koření stromu
## BVS: Výpis klíčů
- klíče uložené v BVS můžeme vypsat v pořadí
- preorder
	- hodnotu klíče uloženého v kořeni vypíšeme ==před== vypsáním klíčů uložených v jeho levém a pravém podstromě
- inorder
	- ==mezi==
- postorder
	- ==po==

- ![[Pasted image 20260318102457.png|400]]
- ![[Pasted image 20260318102527.png|400]]

```python
function Inorder(x)
	if x != None then
		Inorder (x.left)
		print (x.key)
		Inorder (x.right)
```
- Inorder (T .root) vypíše klíče uložené v BVS T v pořadí od nejmenšího po největší
- časová složitost výpisu všech klíčů stromu T je Θ(n), kde n je počet uzlů stromu T

```python
function Preorder( x )
	if x != None then
		print ( x .key )
		Preorder ( x .left )
		Preorder ( x .right )

function Postorder( x )
	if x != None then
		Postorder ( x .left )
		Postorder ( x .right )
		print ( x .key )
```
## BVS: Vyhledávání ve stromu
- #todo 
```python
function Search(x, k)
	if x is None or k == x.key then
		return x
	if k < x.key then
		return Search (x.left, k)
	else
		return Search (x.right, k)
```
## BVS: Minimální  a max. klíč
```python
function Minimum(x)
	if x is None then
		return None
	while x.left is not None do
		x = x.left
	return x
	
function Maximum(x)
	if x is None then
		return None
	while x.right is not None do
		x = x.right
	return x
```

