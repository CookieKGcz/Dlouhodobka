## Hamiltonovský cyklus
### algoritmus I
vyberme počáteční vrchol (jedno jaký -> cyklus)
v <- poč. vrchol
```
WHILE existule nenavštívený vrchol DO
	vyber nenavštívený vrchol, který je nejblíž k v
	v <- vybraný vrchol OD
vrať se do počátečního vrcholu
return pořadí, v němž byly vrcholy nevštíveny
```
- není ovšem korektní
	- vracíme se vícekrát přes stejnou cestu

### algo. II
```
WHILE existují vrcholy, které nejsou spojeny cestou DO
	vyber dva vrcholy, které nejsou spojeny cestou
		a jejichž vzdálenost je nejmenší
	vybrané vrcholy spoj hranou OD
přidaním hrany vytvoř cyklus
```
- bohužel
![[Pasted image 20260218101732.png | 400]]
- korektní alg by byl prozkoumat každý z n! cyklů grafu a vyber nejkratší
	- složitostí by byl ale nepoužitelný

### Časová složitost
- časová složitost výpočtu je součet cen všech vykonaných operací
- časová složitost algoritmu je funkce délky vstupu

- složitost v nejhorším případě
	- maxim. délka výpočtu na vstupu délky n
- složitost v nejlepším případě
	- minim. délka výpočtu na vstupu délky n
- průměrná složitost
	- průměr složitostí výpočtů na všech vstupech délky n

- ==složitost = časová složitost v nejhorším případě==
### Prostorová složitost
- velikost potřebné paměti
### Příklad - Vyhledávání
- vstup = A\[0 ... n-1] a číslo x
- výstupem je index _i_ pro který A\[i] = x, resp. hodnota -1 když nevyskytuje
```python
def Linear_Search(A, x)
	index = −1
	for i = 0 to n − 1 do
		if A[i] == x then
			index = i
	return index
```
- každý průchod for cyklem znamená 2 testy: v řádku 2 testujeme nerovnost $i \leq n - 1$, v řádku 3 testujeme rovnost A\[i] == x
- optimalizace?

- první výskyt x ukončí prohledávání
```python
def Better_Linear_Search(A, x)
	for i = 0 to n - 1 do
		if A[i] == x then
			return i
	return -1
```
- každý průchod while = 2 testy

- použití sentinelu (zarážky)
```python
def Even_Better_Linear_Search(A, x)
	last = A[n - 1]
	A[n - 1] = x
	i = 0
	while A[i] != x do
		i = i + 1
	if i < n - 1 and last = x then
		return i
	else
		return -1
```
- každý průchod while = 1 test a 2 testy na konci
- výpočet je ukončený okamžitě po nalezení x
#### Časová složitost - rozpitvané
- jde o linear_search(A,x)
	- 1 řádek = index = -1
	- 5 je return
- délka vstupu je n
- označme $t_{i}$ složitost operace na řádku _i_;
- operace z řádků 1 a 5 se vykonají jednou
- řádek se vykoná n + 1 krát (protože + 1 je tam že i v poslední iteraci která už neprojde se stále musí checknoou podmínka)
- řádek 3 se vykoná n ktrát
- přiřazení v řádku 4 se vykoná úměrně počtu výskytů x v poli

- složitost je v nejlepším případě: $t_{1} + t_{2} * (n + 1) + t_{3} * n + t_{4} * 0 + t_{5}$
- složitost je v nejhorším případě: $t_{1} + t_{2} * (n + 1) + t_{3} * n + t_{4} * n + t_{5}$

- složitost je funkce c * n + d, kde c a d jsou konstanty nezávislé na n = lineární složitost

### Insert sort
- vstup: posloupnost čísel A\[0 ... n - 1]
- výstup: seřazená posloupnost A\[0 ... n - 1]
```python
def InsertSort(A)
	for j = 1 to n- 1 do
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key do
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = key
```

| řádek | cena    | počet                        |
| ----- | ------- | ---------------------------- |
| 1     | $c_{1}$ | $n$                          |
| 2     | $c_{2}$ | $n - 1$                      |
| 3     | $c_{3}$ | $n - 1$                      |
| 4     | $c_{4}$ | $\sum_{j=1}^{n-1} (t_j + 1)$ |
| 5     | $c_{5}$ | $\sum_{j=1}^{n-1} (t_j)$     |
| 6     | $c_{6}$ | $\sum_{j=1}^{n-1} (t_j)$     |
| 7     | $c_{7}$ | $n - 1$                      |
- složitost v nejlepším případě - lineární
$$T (n) = c_{1}n + c_{2}(n - 1) + c_{3}(n - 1) + c_{4}\sum_{j=1}^{n-1} (t_j + 1) + c_{5}\sum_{j=1}^{n-1} (t_j)$$
$$+ c_{6}\sum_{j=1}^{n-1} (t_j) + c_{7}(n - 1)$$
$$= c_{1}n + c_{2}(n - 1) + c_{3}(n-1) + c_{4}(n - 1) + c_{7}(n-1)$$
	 $\leq an + b$


- složitost v nejhorším případě - kvadratická
$$\textcolor{white}{T (n) = c_{1}n + c_{2}(n - 1) + c_{3}(n - 1) + c_{4}\left( \frac{(n+2)(n-1)}{2} \right)}$$
$$\textcolor{white}{+c_{5}\left( \frac{n(n-1)}{2} \right)+ c_{6}\left( \frac{n(n-1)}{2} \right) + c_{7}(n - 1)}$$
$$\textcolor{white}{= \left( \frac{c_{4}}{2}+\frac{c_{5}}{2}+\frac{c_{6}}{2}\right)n^2 + \left( c_{1} + c_{2} + c_{3} + \frac{c_{4}}{2}-\frac{c_{5}}{2}-\frac{c_{6}}{2} \right)n - (c_{2}+c_{3}+c_{4}+c_{7})}$$
	$\leq an^2 + bn + c$
### Typy notací
- $\textcolor{orange}{f \in O(g)}$ znamená, že $C * g(n)$ je $\textcolor{orange}{\text{horní hranicí}}$ pro f(n)
- $\textcolor{lightgreen}{f \in Ω (g)}$ znamená, že $C * g(n)$ je $\textcolor{lightgreen}{\text{dolní hranicí}}$ pro f(n) (omega)
- $\textcolor{cyan}{f \in Θ(g)}$ znamená, že $C_{1} * g(n)$ je $\textcolor{cyan}{\text{horní hranicí}}$ pro f(n) a $C_{2}$ \* g(n) je $\textcolor{cyan}{\text{dolní hranicí}}$ pro f(n)

- f, g jsou funkce, f, g : N -> N
- C, C1, C2 jsou konstanty nezávislé na _n_
### $\textcolor{orange}{O}$ notace
- $f \in O(g)$ právě když existují kladné konstanty $n_{0}$ a $c$ takové, že pro všechna n >= $n_{0}$ platí $f(n) \leq cg(n)$
- funkce $f$ **neroste asymptoticky rychleji** než funkce $g$
- alternativní definice $\textcolor{orange}{f \in O(g)}$ právě když $\lim_{ n \to \infty }sup{\frac{f(n)}{g(n)} < \infty}$

- příklady:
	- $3n^2-10n \in O (n^2)$, protože $3n^2-10n \leq \textcolor{green}{3} n^2$ pro všechna $n \geq \textcolor{green}{0}$
	- $3n^2-10n \in O (n^3)$, protože $3n^2-10n \leq n^3$ pro všechna $n \geq10$
	- $3n^2-10n \notin O (n)$, protože $c > 0$ je $3n^2-10n > cn$ pro všechna $n > 10 + c$
### $\textcolor{lightgreen}{Ω}$ notace
- $f \in Ω(g)$ právě když existují kladné konstanty $n_{0}$ a $c$ takové, že pro všechna n >= $n_{0}$ platí $f(n) \geq cg(n)$
- funkce $f$ **neroste asymptoticky pomaleji** než funkce $g$

- příklady:
	- $3n^2-10n \in Ω (n^2)$, protože $3n^2-10n > {2} n^2$ pro $n > {10}$
	- $3n^2-10n \notin Ω (n^3)$, protože $c > 0$ je $3n^2-10n < cn^3$ pro $n > \frac{10}{c}$
	- $3n^2-10n \in Ω (n)$, protože $3n^2-10n > n$ pro  $n > 4$
### $\textcolor{cyan}{Θ}$ notace
- $f \in Θ(g)$ právě když existují kladné konstanty $n_{0}$, $c_{1}$ a $c_{2}$ takové, že pro všechna n >= $n_{0}$ platí $c_{1}g(n) \leq f(n) \leq c_{2}g(n)$
- funkce $f$ a $g$ rostou **asymptoticky stejně rychle**

- příklady:
	- $3n^2-10n \in Θ (n^2)$, protože $3n^2-10n \in O(n^2)$ a současně $3n^2-10n \in Ω (n^2)$
	- $3n^2-10n \notin Θ (n^3)$, protože $3n^2-10n \notin Ω (n^3)$
	- $3n^2-10n \notin Θ (n)$, protože $3n^2-10n \notin O (n)$
### Asymptotická notace - vlastnosti
- ![[Pasted image 20260218225108.png | 500]]
## Složitost jako funkce délky vstupu
### Násobení matic
```
function MM(A[0 ... n − 1, 0 ... n − 1], B[0 ... n − 1, 0 ... n − 1])
	for i = 0 to n − 1 do
			for j = 0 to n − 1 do
				C[i, j] = 0
				for k = 0 to n − 1 do
					C[i, j] = C[i, j] + A[i, k]B[k, j]
	return C
```
- velikost vstupu: n
- počet aritmetických operací (+, \*): $x$ #todo 
- složitost: $T(n) \in Θn^3$

## Korektnost algoritmů
- vstupní podmínka
	- formulace co je na vstupu algoritmu
- výstupní podmínka
	- pro každý vstup splňující vstupní podmínku určuje, jak má vypadat výsledek odpovídající danému vstupu

- algoritmus je (totálně) korektní jestliže pro každý vstup splňující vstupní podmínku výpočet skončí a výsledek splňuje výstupní podmínku

- ==úplnost== (konvergence)
	- pro každý vstup splňující vstupní podmínku výpočet skončí
- částečná korektnost (parciální korektnost)
	- pro každý vstup, který splňuje vstupní podmínku a výpočet na něm skončí, výstup splňuje výstupní podmínku
### Důkaz korektnosti
- analýza efektu cyklu
	- u vnořených cyklů začínáme od cyklu nejhlubší úrovně
	- pro každý cyklus určíme jeho invariant
	- ==invariantem cyklu je takové tvrzení, které platí před vykonáním a po vykonání každé iterace cyklu==
	- dokážeme, že invariant cyklu je pravdivý
	- využitím invariantu
		- dokážeme konečnost výpočtu cyklu
		- dokážeme efekt cyklu
#### Důkaz pravdivost invariantu cyklu
- inicializace
	- invariant je platný před začátkem vykonávání cyklu
- iterace
	- jestliže invariant platí před iterací cyklu, zůstává v platnosti i po vykonání iterace
- ukončení
	- cyklus skončí a po jeho ukončení platný invariant garantuje požadovaný efekt cyklu

### Příklad - řazení vkládáním
- #todo 
- 