# Reprezentace grafu
## Graf a jeho reprezentace
- graf
	- orientovaný /neorientovaný
	- ohodnocené hrany / vrcholy
	- jednoduché / násobné hrany

- reprezentace grafu
	- seznam následovníků
	- matice sousednosti

- složitost grafových algoritmů je funkcí počtu vrcholů a hran
- používáme zjednodušenou notaci, např. O(V + E) resp. O(n + m)
	- V (E) je množina vrcholů (hran) grafu, n = |V|, m = |E|
## Matice sousednosti
- ![[Pasted image 20260408100507.png|500]]
- graf G = (V,E) je reprezentovaný maticí A = ($a_{ij}$) rozměrů $|V| \times |V|$, kde
$$a_{ij} =
\begin{cases}
1 & \text{pokud } (i,j) \in E \\
0 & \text{jinak}
\end{cases}$$
- prostorová složitost: $Θ(V^2)$
- vhodné pro husté grafy
- časová slož. výpisu všech sousedů _u_ je $Θ(V)$
- časová slož. ověření zda $(u,v) \in E$ je $Θ(1)$
## Seznam následníků
- ![[Pasted image 20260408101003.png|500]]
- graf G = (V,E) je reprezentovaný polem Adj velikosti |V|
- položka v Adj je seznamem následníků vrchol?
- prostorová složitost: $Θ(V + E)$
- vhodné pro řídké grafy
- časová složitost výpisu všech sousedů vrcholu u je $Θ(deg(u))$
- č. s. ověření zda $(u,v) \in E$ je $O(deg(u))$
## Srovnání

|                          | matice soudednosti | seznam následníků | hashovací tabulka |
| ------------------------ | ------------------ | ----------------- | ----------------- |
| test $\{u,v\} \in E$     | $O(1)$             | $O(V)$            | $O(1)$            |
| test $(u,v) \in E$       | $O(1)$             | $O(V)$            | $O(1)$            |
| seznam sousedů vrcholu v | $O(V)$             | $O(1 + deg(v))$   | $O(1 + deg(v))$   |
| seznam hran              | $O(V^2)$           | $O(V+E)$          | $O(1)$            |
| přidání hrany            | $O(1)$             | $O(1)$            | $O(1)$*           |
| odstranění hrany         | $O(1)$             | $O(V)$            | $O(1)$*           |
\*očekávaná složitost
## Průzkum grafu
- pro daný graf G a jeho vrchol s je cílem
	- navštívit všechny vrcholy grafu dosažitelné z vrcholu s
	- průzkum realizovat maximálně efektivně, tj. se složitostí $O(V+E)$

- ![[Pasted image 20260408101840.png|300]]
- ![[Pasted image 20260408101850.png|300]]
- ![[Pasted image 20260408101901.png|400]]
- ![[Pasted image 20260408101913.png|400]]
- ![[Pasted image 20260408101924.png|400]]
- ![[Pasted image 20260408101933.png|400]]
## Základní způsoby průzkumu grafu
- do šířky
- do hloubky
### Implementace průzkumu do hloubky
- křída
	- proměnná označující jestli jsme hranu prošli
- klubko
	- položená niť vyznačuje cestu z výchozího do aktuálního vrcholu, cestu si pamatujeme jako posloupnost vrcholů na této cestě
	- pro uložení cesty použijeme ==zásobník==
	- odmotávání nitě odpovídá přidání vrcholu do zásobníku
	- namotávání nitě při návratu odpovídá odebírání vrcholu ze zásobníku
### Implementace průzkumu do šířky
- v počítači vlny nasimulujeme tak, že při vstupu do nového vrcholu uložíme všechny s ním sousedící vrcholy do ==fronty==
- frontu průběžně zpracováváme
# Průzkum do šířky
## Průzkum do šířky - strategie
- cílem prozkoumat všechny vrcholy dosažitelné z daného vrcholu _s_
	- postupujeme od iniciálního vrcholu _s_ po vrstvách
	- $L_{0} = \{s\}$
	- $L_{1} =$ všechny vrcholy, do kterých vede hrana z _s_
	- $L_{2} =$ všechny vrcholy, které nepatří do L0 ano do L1 a vede do nich hrana z vrcholu patřícího do  L1
	- ...
- ![[Pasted image 20260408103016.png|300]]
- ![[Pasted image 20260408103027.png|320]]
- ![[Pasted image 20260408103038.png|330]]
- ![[Pasted image 20260408103100.png|330]]
- ![[Pasted image 20260408103112.png|300]]
- ![[Pasted image 20260408103125.png|300]]
- ![[Pasted image 20260408103133.png|320]]
- ![[Pasted image 20260408103156.png|380]]
- ![[Pasted image 20260408103210.png|400]]
```python
function BFS((V, E),s)
	foreach u ∈ V \ {s} do
		u.visited = False
	s.visited = True
	Q = ∅
	Enqueque (Q,s)
	while Q not empty do
		u = Dequeque(Q)
		foreach (u, v) ∈ E do
			if not v.visited then
				v.visited = True
				Enqueque (Q, v)
```
- ![[Pasted image 20260408103359.png|400]]
- ![[Pasted image 20260408103414.png|400]]
- ![[Pasted image 20260408103426.png|400]]
- ![[Pasted image 20260408103436.png|400]]
- ![[Pasted image 20260408103447.png|400]]
- ![[Pasted image 20260408103457.png|400]]
- ![[Pasted image 20260408103507.png|400]]
- ![[Pasted image 20260408103530.png|400]]
- ![[Pasted image 20260408103540.png|400]]
## Průzkum do šířky - složitost
- operace vložení a odstranění vrcholu z fronty
	- mají konstantní složitost
	- každý vrchol je ve frontě maximálně jednou
	- celkově O(V)
- seznam následníků každého vrcholu se prochází maximálně jednou
	- při reprezentaci grafu seznamem následníků má průzkum všech seznamů následníků složitost celkově O(E)
- inicializace má slož. O(V)
- celková složitost BFS je O(V + E)
## Průzkum do šířky: atributy vrcholu
- chceme zjistit nejen to, zda je vrchol dosažitelný, ale zajímá nás i cesta z _s_ do _v_ a její délka
- v.color
	- #todo
	- str 417
- v.$\pi$
	- #todo
- v.d
	- #todo 
```python
function BFS((V, E),s)
	foreach u ∈ V \ {s} do
		u.color = white; u.d = ∞; u.π = None
	s.color = gray; s.d = 0; s.π = None
	Q = ∅
	Enqueque (Q,s)
	while Q not empty do
		u = Dequeque(Q)
		foreach (u, v) ∈ E do
			if v.color = white then
				v.color = gray
				v.d = u.d + 1
				v.π = u
				Enqueque (Q, v)
		u.color = black
```
## BFS Strom
- algoritmus BFS definuje přes atributy $\pi$ graf předchůdců, tzv BFS strom
- pro graf G = (V, E) a iniciální vrchol _s_ je BFS strom $G_{\pi} = (V_{\pi}, E_{\pi})$ definovaný předpisem
	- $V_{\pi} = \{v \in V| v.\pi \neq None\} \ucap \{s\}$
	- $E_{\pi} = \{(v.\pi, v)| v \in V_{\pi} \setminus \{s\} \}$
- Pro každý vrchol _v_ $\in V{\pi}$ obsahuje BFS strom právě jednu cestu z _s_ do _v_.
- ![[Pasted image 20260408105512.png|500]]
- ![[Pasted image 20260408105525.png|400]]
- BFS strom grafu není určen jednoznačně, závisí od pořadí, ve kterém zkoumáme následníky vrcholu
- ![[Pasted image 20260408105625.png|400]]
## BFS strom a hrany grafu
- #todo 
## BFS strom a nejkratší cesty
- #todo 
## Aplikace a algoritmy využívající BFS
- P-2-P networks
- Crawlers in Search Engines
- GPS
- broadcasting
- garbage collection
- testování bipartitnosti
# Průzkum do šířky (Bipartitní grafy)
- Bipartitní graf neobsahuje cyklus liché délky
- ![[Pasted image 20260408110805.png|300]]
## Testování bipartitnosti s využitím BFS
- #todo 
- ![[Pasted image 20260408110834.png|400]]
- #todo 
# Průzkum do hloubky
## Průzkum grafu do hloubky - motivace
- ![[Pasted image 20260408111657.png|500]]
## Formulace problému
- průzkum do šířky a stejně tak i průzkum do hloubky je možné použít buď k prozkoumání té části grafu, která je dosažitelná z iniciálního vrcholu, anebo k prozkoumání celého grafu
- průzkum se dá aplikovat a orientované i neorientované grafy
## Průzkum do hloubky - strategie
- na začátku výpočtu a vždy po dokončení průzkumu vybereme jeden z dosud neprozkoumaných vrcholů a zvolíme ho za nový iniciální vrchol
- označ iniciální vrchol jako objevený
- vyber neprozkoumanou hranu (u, v), která vychází z naposledy objeveného vrcholu _u_, a když její koncový vrchol _v_ ještě nebyl prozkoumán, tak ho označ jako objevený
- když všechny hrany vycházející z naposledy objeveného vrcholu _u_ byly prozkoumány, tak ukonči průzkum vrcholu _u_ a pokračuj vrcholem, ze kterého byl vrchol _u_ objeven
- průzkum končí když jsou prozkoumány všechny vrcholy dosažitelné z iniciálního vrcholu

- pro manipulaci s vrcholy používáme zásobník
- ![[Pasted image 20260408112817.png|400]]
- ![[Pasted image 20260408112827.png|400]]
- ![[Pasted image 20260408112837.png|400]]
- ![[Pasted image 20260408112846.png|400]]
- ![[Pasted image 20260408112857.png|400]]
- ![[Pasted image 20260408112910.png|400]]
- ![[Pasted image 20260408112922.png|400]]
- ![[Pasted image 20260408112931.png|400]]
- ![[Pasted image 20260408112942.png|400]]
- ![[Pasted image 20260408112956.png|400]]
- ![[Pasted image 20260408113012.png|400]]
- ![[Pasted image 20260408113021.png|400]]
- ![[Pasted image 20260408113036.png|400]]
## Atributy vrcholu
- barva v.color
	- #todo 
- předchůdce v.$\pi$
	- #todo 
- časové značky v.d a v.f
	- #todo 
- ![[Pasted image 20260408113158.png|400]]

```python
function DFS((V, E))
	foreach u ∈ V do u.color = white; u.π = None
		time = 0
	foreach u ∈ V do
		if u.color == white then DfsVisit ((V, E), u)

function DfsVisit((V, E), u)
	time + = 1
	u.d = time
	u.color = gray
	foreach v ∈ Adj[u] do
		if v.color == white then
			v.π = u
			DfsVisit ((V, E), v)
	u.color = black
	time + = 1
	u.f = time
```
## Složitost
- Oba cykly v DFS mají složitost $Θ(V)$
- DfsVisit se pro každý vrchol grafu volá jednou, protože bezprostředně po zavolání dostává vrchol šedivou barvu
- Každá hrana se v cyklu procedury DfsVisit prozkoumá rávě jednou, protože bezprostředně po první návštěvě hrany se pro její koncový vrchol volá DfsVisit a koncový vrchol dostává šedivou barvu
- zbylé operace souvisí přímo s průzkumem vrcholů a mají konstantní složitost
- celková slož. DFS je $O(V+E)$
## DFS LES
- 