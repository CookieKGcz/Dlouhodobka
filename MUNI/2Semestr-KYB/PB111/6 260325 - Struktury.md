### 6.1.1 Složená hodnota
- hodnota složená z jiných hodnot
- podhodnoty = složky
- příklad: uspořádaná dvojice
- příklad: seznam (v Pythonu)
### 6.1.2 Složené typy
- typ složené hodnoty
- určuje typy složek
- vztahuje se i na objekty
### 6.1.3 Složené hodnoty vs objekty
- složený objekt -> má podobjekty
- složená hodnota -> má složky
- podobjekt obsahuje hodnotu
- složky musí "pasovat" na podobjekt
### 6.1.4 Záznamový typ
- ang Record type
- obecná, běžná konstrukce
- pevné typy a pořadí složek
- x
### 6.1.5 Struktura
- záznamový typ v C
- zavedení klíčovým slovem struct
- tělo: typy a jména složek
- jméno typu: struct jméno
- literál neexistuje
```c
struct pair
{
	int a;
	int b;
};

int main()
{
	struct pair var;
}
```
### 6.1.6 Neúplný typ
- deklarace: struct foo;
- nelze vytvořit hodnotu
- uvnitř vlastní definice
- lze deklarovat ukazatel
### 6.1.7 Inicializace
- proměnné lze inicializovat
- x
### 6.1.8 Přístup ke složce
- výraz tvaru e1.jméno
- může se vyhodnotit na objekt
	- když je e1 objekt
	- při dočasném zhmotnění \[...]
- adresy musí být "pohromadě"
### 6.1.9 Nepřímý přístup
- výraz tvaru e1 -> jméno
- je vždy objektem (l-hodnotou)
- e1 musí být typu ukazatel
- vstupní podmínka: platnost e1
### 6.1.10 Přiřazení
- uložení hodnoty do objektu
- u struktur proběhne po složkách
- rekurzivně do podstruktur
### 6.1.11 Předání do podprogramu
- stejně jako jiné hodnoty
- předání = inicializace
	- nelze složená inicializace
	- inicializace kopií
### 6.1.12 Pole v struktuře
```c
struct foo
{
	int val[ 3 ];
};

struct bar
{
	int val_1, val_2, val_3;
};


struct array
{
	int data[ 3 ];
}

int f( struct array a )
{
	assert( a.data[ 0 ] == 1 );
}
```
### 6.1.13 Dočasné zhmotnění
- co znamená přístup do pole
	- e1\[e2] \*(e1 + e2)
	- f().foo\[1]?
- při přístupu vytvoříme objekt
- zanikne s koncem vyhodnocení
## 6.2 Zřetězený seznam
### 6.2.1 Princip
- složený ze samostatných uzlů
- uložených v nezávislých objektech
- každý reprezentuje jeden prvek
- ukazatel na další uzel
### 6.2.2 Reprezentace
- struktura pro uzel
- lze mít samostatnou hlavu
- struct node \*next
- pevný typ uložené hodnoty
### 6.2.3 Typ a hodnota
- z pohledu C není hodnota
- vyšší úroveň abstrakce
	- reprezentace = soubor objektů
	- operace = podprogramy
	- žádná automatická kontrola
### 6.2.4 Výhody
- jednoduchá implementace
- velmi flexibilní
	- fronta
	- zásobník
	- seznam
### 6.2.5 Nevýhody
- nahodilý přístup do paměti
- větší paměťová režie
- nelze indexovat
- nešikovná abstrakce
### 6.2.6 Dvojité řetězení
- jednodušší odstranění uzlu
- složitější přidání uzlu
- výrazně větší režie
- omezené použití (plánovače, malloc)
### 6.2.7 Iterace
- při práci s celým seznamem
- typické využití cyklu for:
	- struct node \*n = head
	- podmínka n
	- posun n = n->next
### 6.2.8 Vložení uzlu
- potřebujeme znát pozici
- ukazatel na předchozí uzel
- na začátek -> triviální
- na konec -> ukazatel navíc
### 6.2.9 Odstranění
- opět potřebujeme znát pozici
- ukazatel na předchozí uzel
- na začátek -> triviální
- na konec -> dvojité zřetězení


Z 5. týdne 3. ukázka.! #todo 