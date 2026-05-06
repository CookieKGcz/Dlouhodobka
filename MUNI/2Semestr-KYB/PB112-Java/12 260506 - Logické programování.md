## Logické paradigma
- popisuje vztahy mezi objekty světa prostřednictvím relací
	- program mechanicky vypočte výsledek

- Program je databáze faktů a pravidel
	- Všechny fakta tvoří databázi faktů. Podobně máme též databázi pravidel.
- Program také obsahuje cíl, který se má dokázat
- Výpočet je dokazování cíle metodou SLD rezoluce.
- Výsledek výpočtu je pravdivostní hodnota a případně též možné hodnoty volných proměnných, pro které je cíl dokazatelný.

- Prolog je příkladem programovacího jazyka logického paradigmatu
## Seznámení s Prologem
- Fakta:
```prolog
<jméno>.
nebo
<jméno>(< param1>,…, <paramN >).
```
- Jméno i parametry musí začínat malým písmenem.
- Za faktem musí být tečka.

- Databáze faktů v programu:
```prolog
je_teplo.
neprsi.
kamaradi(vincenc, kvido). /* Znají se od mateřské školy. */
kamaradi(vincenc, ferenc). /* Poznali se na pískovišti. */
```

- Dotazy:
```prolog
?-<cíl>
```
- ?-je_teplo   ->   true
- ?-prsi          ->   CHYBA, není v databázi
- ?-kamaradi(vincenc, ferenc) -> true
- ?-kamaradi(ferenc, vincenc) -> false

- Jména začínají velkým písmenem nebo podtržítkem.
- Lze použít v pravidlech i dotazech.
```prolog
?-kamaradi(vincenc, X).
/* Co jsme našli */
X = kvido ;
X = ferenc.
```

```prolog
?- kamaradi(X, Y).
X = vincenc,
Y = kvido ;
X = vincenc,
Y = ferenc.
```

- Pravidla
	- tvar: `<B>:-<A>`Hlava:-Tělo
	- "pokud platí \<A>, pak platí B"
		- A => B
```prolog
clovek(X) :- vedec(X).
– „pokud platí vedec(X), pak platí clovek(X)“.
clovek(X) :- umelec(X).
– „pokud platí umelec(X), pak platí clovek(X)“.
```
- Disjunkce Konjunkce
```prolog
clovek(X) :- vedec(X); umelec(X).
– „pokud platí vedec(X) nebo umelec(X), pak platí clovek(X)“.

borec(X) :- vedec(X), umelec(X).
– „pokud platí vedec(X) a umelec(X), pak platí borec(X)“.
```

## Syntaxe prologu
- Termy jsou základní kameny faktů, pravidel a dotazů a dělíme je na:
	- Atomy, Čísla, Proměnné a Strukturované termy
- Atomy:
	- a, b, john, 'John', '2', 'John Doe', jara_cimrman
	- ?-atom(a). -> true
	- ?-atom(X). -> false
- Čísla:
	- ?-A is 1.5\*2.
	- A = 3.0.
	- ?-3.0 =:= 1.5\*2 -> true
	- ?-number(1) -> true
	- ?-number(1+1) -> false
- Proměnné:
	- Velkým počátečním písmenem
	- Hodnotou uloženou v proměnné může být libovolný term
	- Prolog není striktně typovaný
	- Anonymní proměnná "\_"

- Strukturované termy
	- Funktor je jméno relace spolu s informací, kolik má parametrů.
		- Pro výpočet parametrů máme pojem arita funktoru
	- Strukturovaný term je funktor následovaný sekvencí argumentů
	- Argument může být libovolný term