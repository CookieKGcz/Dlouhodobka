#WIP #todo 
# Pojem množina
Co je vlastně množina?
- Naivní pohled: ***"Množina je soubor prvků a je svými prvky plně určena"***
	- Něco co něco zahrnuje
	- Musíme být schopni rozhodnout, jestli prvek je skutečně v konkrétní množině. (Zda-li do ní patří)

- Příklad zápisu množin: 
	- ∅, **(prázdná množina)**
	- {a, b}, (složené množinové závorky)
	- {b, a}, (množina je bez pořadí) == {a, b}
	- {a, b, a}, (taky stejné, to že tam je a 2x je jedno (je tam jen jednou))
	- {{a, b}}, (množina v množině) (množina je prvkem množiny)
	- {∅, {∅}, {{∅}}},
	- {x | x je liché přirozené číslo}. (podmíněný zápis, "leží tam všechny takové prvky x, kde x je liché přirozené číslo")
## Co je ale pak prvek?
- prvku sám o sobě **nemá matematický význam**, svého **významu** totiž** nabývá** pouze **ve spojení** ***"být prvkem množiny“***. Prvky množiny tak může být cokoliv, mimo jiné i další množiny.
## Zápis množiny
- Značení množin a jejich prvků:
	- x ∈ M ”x je prvkem množiny M“
	- ∅ je prázdná množina {}.

- Některé vlastnosti vztahu "být prvkem" jsou:
	- a ∈ {a, b},
	- a !∈ {{a, b}}, (jediný prvek množiny je množina (tedy není tam a))
	- {a, b} ∈ {{a, b}}, (platí)
	- a !∈ ∅, (v prázdné množině není nic)
	- ∅ ∈ {∅},
	- ∅ !∈ ∅,

	- rovnost množin dle prvků:
		- {a, b} = {b, a} = {a, b, a},
		- {a, b} 6= {{a, b}}

- **Značení: Počet prvků ([[mohutnost]]) množiny A zapisujeme \[A].**
	- |∅| = 0,
	- |{∅}| = 1,
	- |{a, b, c}| = 3,
	- |{{a, b}, c}| = 2.
## Jednoduché srovnání množin
- Vztah ”být prvkem množiny“ nám přirozeně podává i způsob porovnávání množin mezi sebou. Jedná se o klíčovou část, čili hlavní nástroj teorie množin.

#### Definice:
- Množina A je podmnožinou množiny B, právě když každý prvek A je prvkem B. Píšeme A ⊆ B nebo obráceně B ⊇ A.**

- Říkáme také, že se jedná o inkluzi.
	- Platí {a} ⊆ {a} ⊆ {a, b} !⊆ {{a, b}},
	- ∅ ⊆ {∅}
	- A |⊆ (jen dolní čára je přeškrtnuta == ostrá podmnožina) B, právě tehdy když A ⊆ B a A != B (A je vlastní podmnožinou B).
- Z naivní definice množiny pak přímo vyplývá následující:
#### Definice:
- Dvě množiny jsou si rovny A = B právě tehdy, když A ⊆ B a B ⊆ A.
	- Podle naivní definice jsou totiž množiny A a B stejné, mají-li stejné prvky.
	- Důkaz rovnosti množiny A = B má obvykle dvě části:
		- Odděleně se dokáží inkluze A ⊆ B a B ⊆ A.
## Ukázky nekonečných množin
- Značení: Běžné číselné množiny v matematice:
	- N = {0, 1, 2, 3, . . . } je množina přirozených čísel.
	- Z = {. . . , −2, −1, 0, 1, 2, 3, . . . } je množina celých čísel
	- Z+ = {1, 2, 3, . . . } množina celých kladných čísel
	- Q je množina racionálních čísel (zlomky)
	- R je množina reálných čísle
		- vše samozřejmě s dvojíma linkama
# Množinové operace
## Sjednocení a průnik
### Definice 3.2.
- Sjednocení ∪ a průnik ∩ dvou množin A, B definujeme:
- A ∪ B = {x | x ∈ A nebo x ∈ B}
- A ∩ B = {x | x ∈ A a současně x ∈ B}
![[Pasted image 20251006210134.png | 400]]
- Příklady
	- {a, b, c} ∪ {a, d} = {a, b, c, d},
	- {a, b, c} ∩ {a, d} = {a}

- **Vždy platí "distributivita":**
	- A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) a
	- A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- **a také "asociativita":**
	- A ∩ (B ∩ C) = (A ∩ B) ∩ C (stejně pro ∪)
- **a ”komutativita“:**
	- A ∩ B = B ∩ A (stejně pro ∪). 

#### Definice: 
- Pro libovolný počet množin indexovaných pomocí I (velké i) rozšířeně
$$
\bigcup_{i \in I} A_i = \{\, x \mid x \in A_i \text{ pro nějaké } i \in I \,\},
$$
$$
\bigcap_{i \in I} A_i = \{\, x \mid x \in A_i \text{ pro každé } i \in I \,\}.
$$
->
$$
\begin{gathered}
\text{Nechť } A_i = \{2  · i\}
\text{ pro každé } i \in \mathbb{N}. \\
\text{ Pak } \bigcup_{i \in \mathbb{N}} A_i 
\text{ je množina všech sudých přirozených čísel.}
\end{gathered}$$ $$\text{Nechť } B_i = \{\, x \mid x \in \mathbb{N},\, x \ge i \,\}
\text{ pro každé } i \in \mathbb{N}.
\text{ Pak } \bigcap_{i \in \mathbb{N}} B_i = \emptyset.$$
## Množinový rozdíl
### Definice 3.3.
- Rozdíl \ a symetrický rozdíl ∆ dvou množin A, B definujeme:
$$\begin{gathered}
A \setminus B = \{\, x \mid x \in A \text{ a \textcolor{lightblue}{současně} } x \notin B \,\}, \\
A \triangle B = (A \setminus B) \cup (B \setminus A).\end{gathered}$$
![[Pasted image 20251006221843.png | 500]]
- Příklady:
	- {a, b, c} \ {a, b, d} = {c}
	- {a, b, c}∆{a, b, d} = {c, d}
- **Vždy platí například A \ (B ∩ C) = (A \ B) ∪ (A \ C) apod**

#### Definice:
- Pro libovolný počet množin indexovaných pomocí konečně I.
$$\begin{gathered}
\triangle_{i \in I} \ A_{i} = \{\, x \mid x \in A_{i} \text{ pro lichý počet } i \in I \,\}\end{gathered}$$
## Doplněk k množině
#### Definice:
- Nechť A ⊆ M. Doplňkem A vzhledem k M je množina negA = M \ A

- Jedná se o poněkud specifickou operaci, která musí být vztažena vzhledem k nosné množině M !
- Je-li M = {a,b,c}, pak doplněk{a,b} = c. Je-li M = {a,b}, pak doplněk{a,b} = ∅.

- Vždy pro A ⊆ M platí doplněkdoplněA = A (dvojí doplněk)
- Vždy pro A, B ⊆ M platí:
	- dopl(A ∪ B) = doplA ∩ doplB
	- dopl(A ∩ B) = doplA ∪ doplB
- viz![[Pasted image 20251006223344.png | 400]]
## Potenční množina
### Definice 3.4.
- Potenční množina množiny A, neboli množina všech podmnožin, je definovaná vztahem:
$$2^A = \{ B \mid B \subseteq A \}$$
	= všechny takové množiny B jako když jsou podmnožinou A

- Platí například:
$$\begin{gathered}2^{\{a,b\}} = \{ \emptyset, \{a\}, \{b\}, \{a, b\}\} \\
2^{\emptyset} = \{ \emptyset \} \\
2^{ \{\emptyset, \{ \emptyset \} \}} = \{ \emptyset , \{ \emptyset \}, \{ \{ \emptyset \} \}, \{ \emptyset, \{ \emptyset \} \}\} \\ \end{gathered}$$
### Věta 3.5
- Počet prvků potenční množiny splňuje |2^A| = 2^|A|
### Důkaz:
- Jak vybereme jednu podmnožinu B ⊆ A? Například tak, že pro každý z |A| prvků množiny A se nezávisle rozhodneme, zda jej zařadíme do B nebo ne. To jsou dvě možnosti pro výběr každého prvku b ∈ A a podle principu nezávislých výběrů je celkový počet různých podmnožin A roven:
$$| 2 ^{ A} | = 2 · 2 · 2 · . . . · 2 = 2^{ A }$$
# Kartézský součin
#### Definice:
- Uspořádaná dvojice (a, b) je zadána množinou {{a}, {a, b}}.
#### Fakt:
- Platí (a, b) = (c, d) právě tehdy, když a = c a současně b = d.
	- Co je dle definice (a, a)?
		- (a, a) = {{a}, {a, a}} = {{a}, {a}} = {{a}}.
### Definice 3.6
- **Kartézský součin dvou množin A,B definujeme jako množinu všech uspořádaných dvojic ze složek z A a B**
$$ A × B = \{ (a, b) | a ∈ A, b ∈ B \}$$
- Příklady:
	- {a, b} × {a} = {(a, a),(b, a)}
	- {c, d} × {a, b} = {(c, a),(c, b),(d, a),(d, b)}
- Platí ∅ × X = ∅ = X × ∅ pro každou množinu X.
- Jednoduchá mnemotechnická pomůcka říká |A × B| = |A| · |B|
## Skládání součinu
#### Definice:
- Pro k in N, k > 0 definujeme uspořádanou k-tici (a1, ..., ak) ind.
	- (a1) = a1
	- (a1, a2, ..., ai, ai+1) = ((a1,a2,..., ai), ai+1)
#### Fakt:
- Platí (a1, · · · , ak) = (b1, · · · , bk), právě když ai = bi pro každé 1 <= i <= k.
#### Definice:
- **kartézského součinu více množin> Pro každé k ∈ N definujeme:**
$$A_1 \times A_2 \times \cdots \times A_k = \{(a_1, a_2, \ldots, a_k) \mid a_i \in A_i \text{ pro každé } 1 \leq i \leq k\}.$$
- Například Z^3 = Z × Z × Z = {(i, j, k) | i, j, k ∈ Z}.
- Co je A^0? {∅}, neboť jediná uspořádaná 0-tice je právě prázdná ∅.

Poznámka: Podle uvedené definice není kartézský součin asociativní, tj. obecně nemusí platit, že A x (B x C) = (A x B) x C.
# Porovnání a určení množin
### Věta 3.7
- Pro každé dvě množiny A, B ⊆ M platí dopl(A ∪ B) = doplA ∩ doplB
### Důkaz:
- v obou směrech rovnosti.
![[Pasted image 20251006234430.png]]
### Věta 3.8
- Pro každé tři množiny A, B, C platí A \ (B ∩ C) = (A \ B) ∪ (A \ C)
![[Pasted image 20251006234536.png]]
### Důkaz:
![[Pasted image 20251006234551.png]]
## Charakteristický vektor (pod)množiny
- V případech, kdy všechny uvažované množiny jsou podmnožinami nějaké konečné *nosné množiny* X, což není neobvyklé v programátorských aplikacích, s výhodou využijeme následující reprezentaci množin.
### Definice:
- Mějme nosnou množinu X — {xi, x2, . . .  , xn}- Pro A ⊆ X definujeme charakteristický vektor xA jako:$$\chi_A(x) = \begin{cases} 
c_{i } = 1 & \text{pokud } x \in A \\
 & \text{jinak} \ c_{i } = 0.
\end{cases}$$
- Platí A = B právě když xA = xb.
- Množinové operace jsou realizovány „bitovými funkcemi" sjednocení ∼ OR, průnik ∼ AND, symetrický rozdíl ∼ XOR.
## Princip inkluze a exkluze
- Tento důležitý a zajímavý kombinatorický princip je někdy také nazýván „princip zapojení a vypojení
### Věta 3.9.
- Počet prvků ve sjednocení dvou či tří množin spočítáme:
- |A ∪ B| = |A| + |B| − |A ∩ B|
- |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|
![[Pasted image 20251006235655.png]]
### Příklad 3.10
- Z 1000 televizí jich při první kontrole na výrobní lince má 5 vadnou obrazovku, 10 je poškrábaných a 12 má jinou vadu. Přitom 3 televize mají současně všechny tři vady a 4 jiné jsou poškrábané a mají jinou vadu. Kolik televizí je celkem vadných?
### Řešení:
- Dosazením |A| = 5, |B| = 10, |C| = 12, |A ∩ B ∩ C| = 3, |A ∩ B| = 3 + 0, |A ∩ C| = 3 + 0, |B ∩ C| = 3 + 4 do věty 3.9 zjistíme výsledek 17.
### Poznámka.
- Jen stručně, bez důkazu a bližšího vysvětlení, si uvedeme obecnou formu principu inkluze a exkluze:
$$\left| \bigcup_{j=1}^{n} A_j \right| = \sum_{\emptyset \neq I \subseteq \{1,\ldots,n\}} (-1)^{|I|-1} \cdot \left| \bigcap_{i \in I} A_i \right|$$
# Relace a funkce
- Vedle množin jsou dalším důležitým základním „datovým typem" matematiky relace, které nyní zavedeme a kterým vzhledem k jejich mnohotvárnému použití v informatice věnujeme významnou pozornost i v příštích lekcích.
### Definice 3.11.
- Relace mezi množinami Al, A2, . . . , A^, pro k ∈ N, je libovolná podmnožina kartézského součinu$$R ⊆ A1 × A2 × · · · × A_{k}$$
- Pokud A1 = A2 = · · · = Ak = A, hovoříme o k-ární relaci R na A.

- Příklady relací:
	- {(1, a),(2, a),(2, b)} je relace mezi {1, 2, 3} a {a, b}
	- {(i, 2 · i) | i ∈ N} je binární relace na N
	- {(i, j, i + j) | i, j ∈ N} je ternární relace na N
	- {3 · i | i ∈ N} je unární relace na N
## Funkce mezi množinami
### Definice 3.12
- (Totální) funkce z množiny A do množiny B je relace *f* mezi A a B taková, že pro každé x ∈ A existuje právě jedno y ∈ B takové, že (x, y) ∈ *f*.
- Množina A se nazývá definiční obor funkce *f*. Funkcím se také říká zobrazení.

- Poznámka: Množinu B lze nazvat oborem hodnot, ale častější terminologie je, že oborem hodnot funkce f s definičním oborem A je podmnožina množiny B sestávající z těch y, pro něž existuje x ∈ A takové, že (x, y) ∈ *f*.
![[Pasted image 20251007001316.png]]
### Značení:
- Pro funkce místo (x, y) ∈ *f* píšeme obvykle *f*(x) = y
- Zápis *f* : A -> B říká, že *f*  je funkcí s def. oborem A a oborem hodnot, který je podmnožinou B.

- Příklady funkcí jsou třeba následující.
	- Definujeme funkci *f* : N → N předpisem f (x) = x + 8.
		- Pak *f* = {(x, x + 8) | x ∈ N}
	- Definujeme funkci plus :  N × N → N předpisem plus(i, j) = i + j.
		- Pak plus = plus = {(i, j, i + j) | i, j ∈ N}
## Parciální (částečné) funkce
### Definice:
- Pokud naši Definici 3.12 upravíme tak, že požadujeme pro každé x ∈ A nejvýše jedno y ∈ B takové, že (x, y) ∈ *f*, obdržíme definici parciální funkce z A do B.
![[Pasted image 20251007001917.png]]
Pro nedefinovanou hodnotu používáme znak ⊥.
![[Pasted image 20251007001939.png]]