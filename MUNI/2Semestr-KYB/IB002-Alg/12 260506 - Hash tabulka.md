## Slovník
- Insert, search, delete (S, x)
- složitost:
	- v nejhorším případě Θ(n)
	- očekávaný případ O(1)
## Přímé adresování
- každý objekt reprezentované množiny prvků má unikátní klíč z univerza:
- $U = \{0,1, \dots, m -1\}$

- implementace
	- tabulka (pole) $T[0 \dots m - 1]$
	- každý slot (pozice) v T odpovídá jednomu klíči z U
	- když reprezentovaná množina obsahuje objekt x s klíčem k, tak T\[k] obsahuje ukazatel na x
	- v opačném případě je T\[k] prázdné (None)
- Složitost operací je konstantní

- schéma
- ![[Pasted image 20260506101946.png|400]]

## Výhody x Nevýhody přímého adresování
- +
	- konstantní složitost všech operací
	- jednoduchá implementace
- -
	- v případě, že univerzum U je veliké, tak uchovávání tabulky velikosti univerza je neefektivní resp. nemožné
	- v případě, že množina aktuálně uložených klíčů je malá ve srovnání s velikostí universa, tak větší část paměti alokované pro tabulku T je nevyužitá
	- problém objektů se stejným klíčem
## Hashovací tabulka
- každý prvek reprezentované množiny má klíč univerza U
- hash fce h: $U \to \{0,1,\dots,m-1\}$

- implementace
	- tabulka (pole) $T[0 \dots m - 1]$
	- když reprezentovaná množina obsahuje prvek x s klíčem $k \in U$, tak $T[h(k)]$ obsahuje ukazatel na x

- rozdíl mezi přímou adresací a hashovací tabulkou je v určení pozice na kterou se uloží prvek x s klíčem k: $T[k]$ vs $T[h(k)]$
- při hashování může být |U| >> m

- schéma:
- ![[Pasted image 20260506102727.png|400]]
### Problémy k řešení
- Řešení kolizí
	- situace, kdy prvky x a x' s klíči k a k' zahashujeme na stejnou pozici, tj. h(k) = h(k')
		- zřetězené hashování (chaining)
		- otevřená adresace (open adressing)
- Výběr hashovací fce
	- hashovací fce musí být deterministická
	- minimalizovat počet kolizí
	- efektivní výpočet funkce
## Výběr hashovací fce
- Problém
	- vždy nějaké kolize
- řešení
	- vybíráme vždy jinou hash fce
- složitost
	- závisí na výběru hash fce
## Množina $H$ hashovacích fce z $U$ do {0,1,...,m-1} je
- uniformní
	- když pro uniformně vybranou fce z H a každý klíč k in U je pravděpodobnost zahashování klíče na každou z pozic tabulky stejná,
	- $Pr_{h \in H}[h(k) = i] = \frac{1}{m}$ pro všechna $k \in U$ a $i \in \{0,1,\dots,m-1\}$
- univerzální
	- když pro každou dvojici klíčů je pravděp. kolize co nejmenší
	- $Pr_{h \in H}[h(k) = h(k')] \leq \frac{1}{m}$ pro všechna $k, k' \in U, k \neq k'$
- téměř univerzální
	- $Pr_{h \in H}[h(k) = h(k')] \leq \frac{2}{m}$ pro všechna $k, k' \in U, k \neq k'$
- r-uniformní
	- když pro každých r vzájemně různých klíčů $k_{1}, \dots, k_{r}$ a pozici $i_{1},\dots,i_{r}$ je pravděpodobnost kolize stejná
$$Pr_{h \in H}[\cap_{j=1}^{r} h(k) = i_{j}] \leq \frac{1}{m^r}$$
# Zřetězené hashování
## Zřetězené hashování
- každá položka tabulky obsahuje seznam prvků zahashovaných na stejnou pozici
- pro operaci vkládání prvku x do hashovací tabulky T předpokládáme, že prvek x se v tabulce nevyskytuje; samotné vkládání se realizuje jako přidání prvku na začátek seznamu $T[h(x.key)]$
- prvek x vyhledáváme v seznamu $T[h(x.key)]$
- prvek x odstraníme vymazáním ze seznamu $T[h(x.key)]$

- schéma:
- ![[Pasted image 20260506104922.png|380]]


gg str 594 cca

# Příklady hashovacích fce
## Metoda dělení
- h(k) = k mod m

- +
	- rychlost
- -
	- závislost na volbě m
	- pro m = 2^p je hodnota h(k) vždy p nejpravějších bitů z binárního zápisu čísla k
	- dobrou volbou pro m je prvočíslo, které není příliš blízko mocnině 2
## Metoda binárního násobení
- reprezentujeme množinu binárních čísel délky w
- velikost tabulky (univerza) je mocninou dvojky, m = 2^p 

- cílem je zahashovat w-bitové čísla na p-bitové
- pro zvolenou konstantu A, 0 < A < 1,
$$h_{A}(k) = |\_m * (k * A \ mod \ 1) \_|$$
 - ![[Pasted image 20260506110050.png|350]]
 - příklad:
	 - ![[Pasted image 20260506110117.png|400]]
## Metoda násobení
- zvolíme prvočíslo p takové, že žádný klíč není větší než p
- pro libovolné čísla $a \in \{1,2,\dots,p-1\}$ a $b \in \{1,2,\dots,p-1\}$ definujeme hashovací fce předpisem
$$h_{ab}(k) = ((ak + b) \ mod \ b) \ mod \ m)$$
# Otevřená adresace
- všechny objekty ukládáme přímo do tabulky
- hashovací fce je typu $h : S \times \{ 0,1,\dots,m-1\}\to \{0,1,..,m-1\}$, přičemž požadujeme, aby pro každý klíč $k \in S$ sekvence sond
$$(h(k, 0), h(k, 1), . . . h(k, m − 1))$$
- byla permutací posloupnosti (0,1,...,m-1)
- při vyhledávání se systematicky zkoumají (sondují) pozice tabulky, dokud není nalezen hledaný klíč nebo není jasné, že klíč v tabulce není
