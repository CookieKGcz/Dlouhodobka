## Maximální a minimální prvek - iterativně
- vstup: posloupnost čísel
- výstup: maximální a minimální prvek posloupnosti
- velikost vstupu: délka posloupnosti (počet čísel)
```python
def MinMax_Iterative(S[0 ... n - 1])
	if n == 1 then return S[0], S[0]
	if S[0] ≤ S[1] then
		min el = S[0]; max el = S[1]
	else
		max el = S[0]; min el = S[1]
	for i = 2 to n − 1 do
		if S[i] > max el then max el = S[i]
		if S[i] < min el then min el = S[i]
	return min el, max el
```
- složitost výpočtu = počet porovnání prvků vstupní posloupnosti pro n > 1 celkem 1 + 2(n - 2)
## Maximální a minimální prvek - rekurzivně
- posloupnost rozděl na dvě podposloupnosti
- najdi minimální a max prvek v obou podposl.
- kombinuj řešení podproblémů: maximální prvek posloupnosti je větší z maximálních prvků podposl.; symetricky pro minim. prevek
```python
def MinMax_Rec(S, I, r)
	if r = l then
		return S[l], S[r]
	if r = l + 1 then
		if (S[l] ≤ S[r] then
			return S[l], S[r]
		return S[r], S[l]
	if r > l + 1 then
		l min, l max = MinMax Rec (S, l,(l + r)  2)
		r min,r max = MinMax Rec (S,(l + r)  2 + 1,r)
	return Min(l min,r min), Max(l max,r max)
```
- iniciální volání MinMax_Rec (S, 0, len(S) - 1)
## Korektnost rekurzivních algoritmů
- #todo 
## Maximální a minimální prvek - korektnost
- ukážeme, že algoritmus je konvergentní a parciálně korektní

- ==konvergence==:
	- každé rekurzivní volání se provede pro neprázdnou posloupnost poloviční délky
	- délka posloupnosti klesne na 2 nebo 1
	- maximální a min prvek posloupnosti délky nevýše 2 najde algo. přímo
- ==parciální korektnost==:
	- dokážeme indukcí vzhledem k délce vstupní posloupnosti

	- báze indukce - pro n = 1 a n = 2 se provedou se příkazy na řádcích 1, resp. 2
	- indukční předpoklad - algoritmus vypočítá korektní výstup pro všechny posloupnosti délky nejvýše n - 1 (n > 1)
	- dokážeme platnost tvrzení pro n
		- #todo 
## Složitost rekurz. algoritmů
- #todo 
$$
T(n) = 
\begin{cases}
B(n), \text{pro n} \leq \text{c} \\[4pt]
\displaystyle \sum_{i=1}^{k} T(n_i) + D(n) + C(n).
\end{cases}
$$
