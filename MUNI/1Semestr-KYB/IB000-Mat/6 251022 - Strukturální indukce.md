#WIP #todo
## Zopakování na začátek
### Definice 6.0 Induktivní definice množiny
- Jedná se obecně o popis (nějaké) množiny M v následujícím tvaru:
	- Je dáno několik pevných *bázických* prvků a1, a2, ..., ak in M.
	- Je dán soubor *induktivních pravidel* typu:
		- Jsou-li (libovolné prvky) x1, ..., xl in M, pak také y in M.

	 - V tomto případě je y typicky funkcí:
$$y = f_{i}(x_{1}, \dots, x_{l})$$
- Pak naše induktivně definovaná množina M je určena jako nejmenší (inkluzí) množina vyhovující všem těmto pravidlům.
- ![[Pasted image 20251022175733.png | 400]]
## Jednoznačnost induktivních definic
### Definice:
- Řekneme, že daná induktivní definice množiny M je ==jednoznačná==, právě když každý prvek M lze odvodit z bázických prvků pomocí induktivních pravidel právě ==jedním způsobem==.
	- Induktivní definice množiny přirozených čísel N je jasně jednoznačná.
	- Podobně je jednoznačná následující definice množiny M podmn. N;
	- ![[Pasted image 20251022180318.png | 500]]
### Příklad 6.1 Jednoznačnost induktivní definice 01-řetězců
![[Pasted image 20251022182137.png | 500]]
![[Pasted image 20251022182641.png | 500]]
## Induktivní definice funkcí
- Induktivně definovaná množina povětšinou nemá valný význam sama o sobě, avšak poskytuje definiční obor pro následnou induktivně definovanou funkci.
	- Pro ilustraci z informatického světa si vezměte, že induktivní definice množiny mnohdy definuje prostě jen syntaxi, tedy správný způsob zápisu nějaké instrukce či programu, □ale k tomu je nutno také podat definici sémantiky, tedy významu toho správně zapsaného - co se má vlastně provést nebo vykonat.
### Definice 6.2 Induktivní definice funkce z induktivní množiny.
- Nechť množina M je daná jednoznačnou induktivní definicí. Pak říkáme, že funkce F : M -> X je definována induktivně (vzhledem k induktivní definici M), pokud je řečeno:
	- Pro každý z bázických prvků a1, a2, ..., ak in M je určeno F(a_i) = c_i
	- Pro každé induktivní pravidlo typu
		- "Jsou-li (libovolné prvky) x1, ..., x_l in M, pak také f(x1, ..., x_l) in M"
		- je definováno
$$F(f(x_{1}, \dots, x_{l})) \ na \ základě \ hodnot \ F(x_{1}), \dots, F(x_{l})$$
### Ilustrační příklady
- Ilustrujme si induktivní definici funkce dětskou hrou na „tichou poštu". Definičním oborem je řada sedících hráčů, kde ten první je bazickým prvkem a každý následující (mimo posledního) odvozuje hráče sedícího hned za ním (nebo vedle) jako další prvek hry.
- Hodnotou *bázického* prvku je první (vymyšlené) posílané slovo. Induktivní pravidlo pak následujícímu hráči přiřazuje slovo, které je odvozeno („zkomolením") ze slova předchozího hráče. Výsledkem hry pak je hodnota-slovo posledního hráče.


- Pro další příklad se podívejme třeba do manuálu unixového příkazu `test EXPRESSION`: 
```
EXPRESSION is true or false and sets exit status. It is one of:

( EXPRESSION )             EXPRESSION is true
! EXPRESSION               EXPRESSION is false
EXPRESSI0N1 -a EXPRESSI0N2 both EXPRESSI0N1 and EXPRESSI0N2 are true
EXPRESSI0N1 -o EXPRESSI0N2 either EXPRESSI0N1 or EXPRESSI0N2 is true
[-n] STRING                the length of STRING is nonzero
STRING1 = STRING2          the strings are equal
```
- No, problematická je otázka jednoznačnosti této definice - jednoznačnost není vynucena (jen umožněna) syntaktickými pravidly, jinak je pak dána nepsanými konvencemi implementace příkazu.
- To je pochopitelně z matematického hlediska špatně, ale přesto jde o pěknou ukázku z praktického života informatika.
## Použití strukturální indukce
![[Pasted image 20251022185140.png | 500]]
![[Pasted image 20251022185910.png | 500]]
### Příklad 6.4 Jednoduché aritmetické výrazy a jejich význam
![[Pasted image 20251022190549.png | 500]]
### Příklad pokračování 6.5 Důkaz správnosti přiřazeného "významu" Val : SExp -> N.
![[Pasted image 20251022191103.png | 500]]
## Nazpět k matematické logice
![[Pasted image 20251022191448.png | 500]]
## Sémantika výrokové logiky
![[Pasted image 20251022192222.png | 500]]
## Převod formulí do normálního tvaru
![[Pasted image 20251022192604.png | 500]]
![[Pasted image 20251022192945.png | 500]]
## Důkaz pro normální tvar formule
![[Pasted image 20251022193719.png | 500]]
![[Pasted image 20251022193803.png | 500]]
![[Pasted image 20251022193815.png | 500]]
