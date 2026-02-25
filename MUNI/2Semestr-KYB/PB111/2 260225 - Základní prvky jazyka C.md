# 2
## 2.1 Hodnoty, objekty, proměnné
### 2.1.1 Hodnota
- později složitější
- 12, XII, $(1100)_{2}$, 0xc
### 2.1.2 Operace
- procuje s hodnotami
- hodnoty je třeba si pamatovat
- realizace výpočetním strojem
- příklad: součet dvou hodnot
### 2.1.3 Objekt
- abstrakce (zobecnění) paměťové buňky
- pamatuje si hodnotu
- má identitu
	- různost při stejné hodnotě
	- stejnost během výpočtu
### 2.1.4 Proměnná
- vazba jména na objekt
- syntaktický rozsah platnosti
- ==vazba je neměnná (pevná)==
- platnost jména - živost objektu
### 2.1.5 Typ
- vlastnost hodnoty
- určuje přípustné operace
- určuje chování operací
- pouze v době překladu
### 2.1.6 Deklarace
- proti py nový prvek
- typ jméno = výraz;
- vytvoří **zároveň** objekt i vazbu
- bez inicializace => zapovězená hodnota
## 2.2 Výrazy
### 2.2.1 Elementární výrazy
- název proměnné: x (typ dle proměnné
- číselný literál:
	- typu int: 3, -1, 0x1f
	- typu unsigned: 3u, 0x1fu
### 2.2.2 Aritmetické a logické operace
- popisují hodnotu, žádný vedlejší efekt
- $e_{1}+e_{2}\dots,e_{1} \text{\%} \  e_{2}$
- $e_{1} \ll e_{2}, e_{1} \gg e_{2}$
- $e_{1} \& \ e_{2}, e_{1} | e_{2}, e_{1} \^ e_{2}$
- $-e_{1}, ~e_{1}, !e_{1}$
### 2.2.3 Výpočet hodnoty výrazu
- vyhodnocení do registru R
- var ~ copy A -> R
- 2.2.2
	- vyhodnoť $e_{1}$ do $t_{1}$
	- vyhodnoť $e_{2}$ do $t_{2}$
	- add $t_{1}$, $t_{2}$ $\to R$
### 2.2.4 Kontrola typů
- ověření správnosti operace x hodnoty
- vkládá implicitní konverze
	- přesná pravidla jsou složitá
- špatně utvořený program zamítne
### 2.2.5 Implicitní konverze
1. povýšení - vše menší než int
	- vejde se do int -> int
	- jinak unsigned
2. stejná znaménkovost -> pouze zvětšení
3. různá vede na:
	- známkový je-li striktně větší
	- jinak na neznaménkový
### 2.2.6 Přiřazení
- var = $e_{1}$ (pozor na levou stranu)
- proběhne typová konverze pravé strany
- výraz s vedlejším efektem
- provede zápis do objektu
- hodnota je to, co bylo zapsáno
### 2.2.7 Logické operátory
- binární $e_{1} \&\& \ e_{2}, e_{1} || e_{3}$
- ternární $e_{1} ? e_{2} : e_{3}$
### 2.2.8 Vyhodnocení booleovských operací (strojový kód)
- vyhodnocení $e_{1} \&\& \ e_{2}$ do R:
	- vyhodnoť $e_{1}$ do R
	- je-li R true, vyhodnoť $e_{2}$ do R
- vyhodnocení $e_{1} || e_{2}$ do R
	- vyhodnoť $e_{1}$ do R
	- je-li R false, vyhodnoť $e_{2}$ do R

```
	ei1 ... ein ;
	jz ti, end
	...
end:
```
## 2.3 Příkazy
### 2.3.1 Výrazový příkaz
- $e_{1}$; – jakýkoliv výraz
- provede vedlejší efekty
- hodnota je zapomenuta
### 2.3.2 Složený příkaz
- sekvence příkaz
- uzavřena do složených závorek
- připouští navíc deklarace
	- rozsah platnosti jmen
### 2.3.3 Podmíněný příkaz
- if ( expr ) stmt 
- if ( expr ) stmt1 else stmt2
### 2.3.4 Cyklus do ... while
- do stmt while ( expr );
### 2.3.5 Řízení iterace
- break; – ukončí cyklus
- continue; – ukončí aktuální iteraci
### 2.3.6 Cyklus while
- while ( expr ) stmt
### 2.3.7 Cyklus for
- for ( decl; expr1 ; expr2 ) stmt
- zjednodušená verze:
	- for ( e1; e2; e3 ) stmt
	- podmínka je e2