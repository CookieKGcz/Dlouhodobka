## Heapsort
- cílem je seřadit posloupnost prvků P
- najdeme největší prvek x posloupnosti P
- prvek x přidáme na začátek posloupnosti již seřazených prvků
- odstraníme prvek x z P
- Postup opakujeme dokud posloupnost P není prázdná

- co potřebujeme
	- datovou strukturu nad kterou dokážeme
		- efektivně najít nevětší prvek
		- efektivně z ní odstranit největší prvek
## Kořenový strom
- strom s vyznačeným vrcholem r nazýváme kořenovým stromem s kořenem r
- u kořenových stromů používáme pojmy rodič, děti/synové, sourozenci, následník
- kořen nemá žádného rodiče, ostatní vrcholy jsou potomky kořene
- listem je každý vrchol, který nemá potomky
- místo slova vrchol často používá termín ***uzel***

- podstrom určený vrcholem x je podgraf indukovaný všemi následníky vrcholu x; tento podstrom je opět kořenovým stromem s kořenem x

### Vlastnosti
- ==stupeň vrcholu== v kořenovém stromě T je počet jeho synů

- ==hloubka vrcholu== x v T je délka cesty z kořene do x; kořen je tedy v hloubce nula
- ==výška vrcholu== x v T je délka nejdelší cesty  z x do listu; list má tedy výšku nula
- ==hloubka stromu== = výška stromu T je délka nejdelší cesty od kořene k listu

- ==k-tá hladina stromu== T je množina všech vrcholů stromu T ležících v hloubce k; hladiny začínáme počítat od nulté

- ==binární strom== je strom, ve kterém má každý vrchol nejvýše dva syny; tyto často označujeme jako levého a pravého syna
- ==k-ární strom== je strom, ve kterém má každý vrchol nejvýše k synů

- ![[Pasted image 20260311100853.png| 400]]
## Stromová datová struktura
- reprezentuje strom v počítači
- data jsou uloženy v uzlech stromu
### Reprezentace stromu
- ![[Pasted image 20260311101138.png | 300]]
## Halda a binární halda
### Halda
- stromová datová struktura splňující vlastnost haldy
- kořenový strom má vlastnost haldy právě tehdy, když pro každý uzel *v* a pro každého jeho syna *w* platí $v.key \geq w.key$
- ![[Pasted image 20260311101602.png|300]]
### Binární halda
- je úplný binární strom s vlastností haldy
- binární strom je úplný, pokud jsou všechny jeho hladiny kromě poslední úplně zaplněny a v poslední hladině leží listy co nejvíce vlevo
- ![[Pasted image 20260311101623.png|300]]
- ![[Pasted image 20260311101655.png|350]]

## Binární halda a její reprezentace v poli
- #todo 
### Reprezentace
- ![[Pasted image 20260311101837.png|400]]
- pro daný index *i* vypočteme indexy synů a otce uzlu *i* předpisem
```python
def Parent(i)
	if i > 0 then
		return (i − 1) // 2
	else
		return None

def Left(i)
	return 2i + 1

def Right(i)
	return 2i + 2
```
## Vybudování haldy
- vstupem je posloupnost klíčů uložená v poli A\[0 ... n - 1]
- A.size = n
- klíče v poli přeuspořádáme tak, aby na konci výpočtu tvořili haldu

- v odpovídajícím binárním stromu postupujeme ==od listů směrem ke kořeni==
- na každý uzel aplikujeme operaci Heapify
- ![[Pasted image 20260311102518.png| 200]]![[Pasted image 20260311102534.png|200]]
- ![[Pasted image 20260311102556.png| 400]]
- ![[Pasted image 20260311102611.png| 400]]
- ![[Pasted image 20260311102622.png|400]]
- ![[Pasted image 20260311102638.png|400]]
### Heapify
- postupujeme od uzlu n - 1 k uzlu 0
- nechť *i* je aktuálně zpracovaný uzel; pak všechny uzly *j*, pro $i < j \leq n - 1$, splňují vlastnost haldy
- po zpracování uzlu *i* splňují vlastnost haldy všechny uzly $j \geq i$

```python
def Heapify(A, i)
	largest = i
	if Left(i) < A.size ∧ A[Left(i)] > A[largest] then
		largest = Left(i)
	if Right(i) < A.size ∧ A[Right(i)] > A[largest] then
		largest = Right(i)
	if largest != i then
		Swap (A[i], A[largest])
		Heapify (A, largest)
```
- složitost O(h), kde h je hloubka stromu s kořenem *i*
- korektnost indukcí vzhledem k hloubce

```python
def BuildHeap(A)
	A.size = len(A)
	for i = A.size  2 downto 0 do
		Heapify (A, i)
```

## Algoritmus řazení haldou, Heapsort
- ![[Pasted image 20260311103926.png|400]]
- ![[Pasted image 20260311103936.png|400]]
- ![[Pasted image 20260311103949.png|400]]

```python
algorithm HeapSort(A)
	BuildHeap (A)
	for i = A.size − 1 downto 1 do
		Swap(A[i], A[0])
		A.size −= 1
		Heapify (A, 0)
```
- složitost
	- funkce BuildHeap má složitost O(n)
	- každé z n - 1 volání Heapify má složitost O(log n)
		- O(n log n)
# Řazení haldou - Prioritní fronta
## Prioritní fronta
- datový typ pro reprezentaci množiny prvků, nad kterými je definováno uspořádání
- požadujeme efektivní realizaci operací
	- Insert(S, x) vloží prvek x do množiny S
	- Maximum(S) vrátí největší prvek množiny S
	- ExtractMax(S) odstraní z množiny S největší prvek
	- IncreaseKey(S, x, k) nahradí prvek x prvkem k za předpokladu, že k >= x

- implement. jako haldu
### Maximum
### ExtractMax
- odstranění maxim. prvku se implementuje stejně jako v alg. řazení haldou; složitost operace je O(log n)
```python
function ExtractMax(A)
	if A.size = 0 then
		return None
	max = A[0]
	A[0] = A[A.size − 1]
	A.size −= 1
	Heapify (A, 0)
	return max
```
- ![[Pasted image 20260311110132.png|400]]
- ![[Pasted image 20260311110142.png|400]]
- ![[Pasted image 20260311110151.png|400]]
- ![[Pasted image 20260311110202.png| 400]]
### IncreaseKey
- #todo 
```python
function IncreaseKey(A, i, key)
	A[i] = key
	while i > 0 and A[Parent(i)] < A[i] do
		Swap (A[i], A[Parent(i)])
		i = Parent(i)
```
### Insert
- víme přesně kam
- na konec pole vložíme nový prvek, který je menší než všechny ostatní prvky, symbolicky ho označujeme -∞
- zvýšíme hodnotu vloženého prvku na hodnotu prvku, který chceme vložit do fronty
- O(log n)
```python
function Insert(A, key)
	A.size + = 1
	A[A.size − 1] = −∞
	IncreaseKey (A, A.size − 1, key)
```

# Linear time sorting
- nejsou univerzální!!
## Counting sort - Řazení počítáním
- vstupní podmínka: vstupní posloupnost obsahuje celá čísla z intervalu 0, ..., k, kde k je nějaké pevné dané přirozené číslo

### Jednoduchá varianta
- ![[Pasted image 20260311111329.png| 400]]
### Stabilní varianta
- ![[Pasted image 20260311111539.png|400]]
- ![[Pasted image 20260311111549.png|400]]
- ![[Pasted image 20260311111604.png|400]]
- ![[Pasted image 20260311111620.png|400]]

```python
algorithm CountingSort(A, k)
	for i = 0 to k do
		C[i] = 0
	for j = 0 to len(A) − 1 do
		C[A[j]] += 1
	for i = 1 to k do
		C[i] += C[i − 1]
	for j = len(A) − 1 downto 0 do
		B[C[A[j]] − 1] = A[j]
		C[A[j]] −= 1
```

## Radix sort
- řazení čísel podle číslic na jednotlivých bitech
- postup zleva doprava (most sign. digit)
- postup zprava doleva (least sign. digit)
- dá se použít i pro řazení položek, které nemají číselný charakter
- používá se např. když potřebujeme seřadit položky vzhledem k různým klíčům
```python
algorithm RadixSort(A, d)
	for i = 1 to d do
		pouˇzij stabiln´ı ˇrazen´ı a seˇrad’ poloˇzky podle ite ˇc´ıslice
```

- ![[Pasted image 20260311112916.png| 400]]
- ![[Pasted image 20260311112926.png|400]]
## Bucket sort
- vstupní podmínka:
	- posloupnost obsahuje čísla z intervalu \[0 ... 1]
	- čísla rovnoměrně pokrývají celý interval

- interval rozdělíme na stejně velké podintervaly
- vstupní čísla rozdělíme dle jejich hodnoty do košů
- seřadíme prvky v každém koši

- ![[Pasted image 20260311113321.png|400]]
