## Třída HashMap
- implementuje Map založená na hashovací tabulce
- Hašovací tabulku je v zásadě pole, jehož prvky obsahují jednosměrně zřetězené seznamy párů klíč-hodnota.
	- Umožňuje rychlé vyhledání hodnoty v mapě pro zadaný klíč.
	- Prvku pole se říká kbelík (bucket).
	- Kbelík obsahuje jednosměrný seznam instancí typu Node<K,V>.
	- Hašovací tabulka je tedy definována jako pole kbelíků typu Node<K,V>\[].
	- A třída Node obsahuje (kromě jiných) tyto atributy:
		- key, value
		- next

- Vyhledání hodnoty v mapě pro zadaný klíč key typu K se provede pomocí hašovací tabulky takto:
	- Nejprve vypočteme hash:
		- h = key.hashCode()
	- Z hashe se nalezne index i kbelíku:
		- i = h % length (kapacita)
	- Sekvenčně se prochází uzly v seznamu ve kbelíku na indexu i.
- Efektivita silně závisí na kvalitě implementace metody hashCode klíčů.
	- pokud špatně tak máme linked list
	- ideální je pokud hashCode vrací co nejvíce různé hodnoty
- Pokud je v kbelíku vídce než jeden uzel, tak se těmto uzlům též říkáme ==kolize==.
- Velikost tabulky se může zvětšovat

- Příklad: Uvažujme obchod s auty. Chceme si udržovat pro každý typ auta počet aut v obchodě. Typ auta je reprezentován jako String. Požadujeme rychlé vyhledání počtu aut pro daný typ. Jde tedy o zobrazení f ze String do Integer. Proto si definujeme proměnnou:
	- `Map<String, Integer> f = new HashMap<>();`
- Do mapy můžeme prvky vkládat:
	- `f.put("Favorit", 3); f.put("Felicia", 5); f.put("Force", 1);`
- Nyní můžeme efektivně zjistit počet aut pro zadaný typ:
	- `int count = f.get("Force");`
	- `count = f.get("Phoenix");` // Chyba!
- Pokud si zákazník nějaké auto koupí, tak musíme hodnotu v mapě snížit.
- Řekněme, že zákazník chce koupit auto
	- `String toBuy = "Favorit"; `
- Pak naši mapu f upravíme takto:
	- `f.put(toBuy, f.get(toBuy) - 1);`
- Ale pozor, následující kód fungovat nebude:
	- `Integer value = f.get(toBuy);`
	- `value = value - 1;`
- Nyní náš kód vylepšeme tak, že nejprve ověříme, zda vůbec je daný typ auta k dispozici. Pokud dále počet aut klesne na 0, tak daný typ auta z mapy odstraníme.
```java
if (f.containsKey(toBuy)) {
	int value = f.get(toBuy) - 1;
	if (value == 0) f.remove(toBuy);
	else f.put(toBuy, value);
}

// Verze, kde klíč v mapě hledáme pouze jednou:

Integer value = f.get(toBuy);
if (value != null) {
	if (value == 1) f.remove(toBuy);
	else f.put(toBuy, value - 1);
}

```

## Třída TreeMap
- Třída TreeMap<K,V> implementuje rozhraní Map pomocí ==červeno-černého stromu== (red-black tree).
- Červeno-černý strom je binární vyhledávací strom,
	- jehož každý uzel je buď červený nebo černý a
	- na kterém je průběžně prováděno ==vyvažování==.
- Vyhledávací strom má v uzlech klíče typu K a pro každý uzel x ve stromu platí:
	- Pokud si vezmu libovolný uzel y, do kterého vede cesta přes hrany z uzlu x, přes jeho ==levou== hranu, tak platí x.compareTo(y) >= 0.
	- Pokud si vezmu libovolný uzel y, do kterého vede cesta přes hrany z uzlu x, přes jeho ==pravou== hranu, tak platí x.compareTo(y) <= 0.
- Pro barvy v červeno-černém stromu platí přesná pravidla.
	- Jsou důležité pro všechny operace prováděné nad mapou.
	- Porušení pravidel při operaci vede na zmíněné vyvažování, které zajistí jejich opětovnou platnost

- Příklad: Vraťme se k předchozímu příkladu s obchodem s auty. Přidejme na mapu f požadavek, aby šel efektivně vypsat seznam typů aut v obchodě podle abecedy s odpovídajícími počty kusů.
- Jelikož musíme vzít v potaz uspořádání klíčů (typů aut), tak je vhodné použít TreeMap místo HashMap:
	- `Map<String, Integer> f = new TreeMap<>();`
- Nyní můžeme vypsat požadovaný seznam takto:
```java
for (Map.Entry<String, Integer> e : f.entrySet())
System.out.println(e.getKey() + " -> " + e.getValue());
```
- Vypíší se 3 řádky s texty: Favorit -> 3, Felicia -> 5, Force -> 1.
- Můžeme dále požadovat výpis v jiném pořadí, např. v opačném.
- To lze provést tak, že definujeme komparátor a vložíme jej do ==nové== instance TreeMap (komparátor nelze v mapě měnit).
```java
class CarTypeComparator implements Comparator<String> {
	@Override public int compare(String a, String b) {
		return -1 * a.compareTo(b);
	}
}
```
- A nyní vytvoříme instanci TreeMap s komparátorem takto:
```java
Map<String, Integer> f = new TreeMap<>(
	new CarTypeComparator());
```
- Cyklus uvedený výše vypíše: Force -> 1, Felicia -> 5, Favorit -> 3.
# Iterátory
- Formálně je Iterátor\<E> rozhraní v balíku java.util. Je též součástí Java Collections Frameworku.
	- Nedefinuje ale ani kolekce ani mapy
	- Pojí se k procházení, neboli ==iterování==, prvků v kolekci nebo mapě.
- Intuitivně, specifikuje schopnost iterovat kolekci nebo mapu jeden prvek po druhém, aniž by bylo nutné znát, jak jsou prvky interně uloženy.
## Iterátor vs. Iterable
- Vzpomeňme si na rozhraní Iterable\<T>, které
	- Implementují všechny kolekce (mapy ne).
	- Umožňuje procházet kolekce jednotným způsobem jeden prvek za druhým pomocí for-each cyklu ve tvaru:
		- `for (T <proměnná> : <výraz>) <příkaz-nebo-blok>`
- Podle specifikace jazyka je for-each cyklus syntaktický cukr (zkráceným zápisem) pro klasický cyklus for v tomto tvaru:
```java
// hasNext() Dokud existuje prvek ve , který jsme ještě neiterovali, tak vrací true.
for (Iterator<T> it = <výraz>.iterator(); it.hasNext(); ) {
	// Proměnná, která osahuje aktuálně iterovaný prvek kolekce
	// Metoda next nám vrátí další prvek v kolekci , který jsme ještě neiterovali.
	T <proměnná> = it.next();
	<příkaz-nebo-blok>
}
```
- Na kolekci <výraz> jsme mohli zavolat metodu iterátor, protože rozhraní Iterable\<T> definuje metodu:
	- `Iterator<T> iterator();`
	- Tedy každá kolekce musí umět poskytnout iterátor.
- Ale pozor, třídy implementující rozhraní Map<K,V>, tedy HashMap<K,V> a TreeMap<K,V>, rozhraní Iterable\<T> neimplementují. Tento kód je proto chybný:
```java
Map<String, Integer> map = new HashMap<>();
for (Map.Entry<String, Integer> e : map) { … } // CHYBA! Neimplementuje Iterable => neposkytuje iterator.
```


## Použití iterátoru
- Příklad: Vraťme se k příkladu s obchodem s auty. Definovali jsme mapu f typu Map<String, Integer>. Úkolem je smazat z mapy páry klíč-hodnota, kde hodnota je menší než 4 a zbylé páry vypsat.
- Pomocí iterátorů můžeme obě věci udělat najednou:
```java
for (Iterator<Map.Entry<String, Integer>> it =
		map.entrySet().iterator(); it.hasNext(); ) {
	Map.Entry<String, Integer> e = it.next();
	if (e.getValue() < 4)
		it.remove();
	else
		System.out.println(e.getKey() + " -> " + e.getValue());
}
```

- Též se často iterátory používají ve while cyklu
- Příklad: Uvažujme tento kód:
```java
class A { int x; A(int v) { x = v; } }
List<A> list = new ArrayList<>();
list.add(new A(1)); list.add(new A(4)); list.add(new A(3));
```
- Snižte hodnotu atributu x ve všech prvcích seznamu o jedna a zrušte všechny, které budou pak mít hodnotu menší než 3.
```java
Iterator<A> it = list.iterator();
while (it.hasNext()) {
	A a = it.next();
	a.x = a.x - 1;
	if (a.x < 3) it.remove();
}
```

# Algoritmy
- Pomocná (utility) třída Collections v balíku java.util obsahuje statické metody, které představují algoritmy Java Collections Frameworku.
	- Všechny tyto metody pracují výhradně nad kolekcemi nebo je vrací.
- Algoritmy lze rozdělit do několika kategorií. My se zmíníme o těchto:
	- Řazení, Zamíchání, Manipulace s daty, Vyhledávání, Kompozice a Hledání extrémních hodnot.
## Řazení
- Algoritmus řazení přeskupuje prvky v seznamu (rozhraní List) tak, aby byly seřazeny vzestupně podle zadaného uspořádání (přirozeného nebo přes komparátor).
- Implementace je založena algoritmu řazení slučováním (merge sort). Funguje takto:
	- Pokud neseřazený seznam má aspoň dva prvky, tak:
		- Jej rozdělí na dva o přibližně stejné velikosti (lišící se max. o jedna).
		- Na oba seznamy aplikuje tentýž algoritmus. Tím dostane dva seřazené seznamy.
		- Dokud tyto seznamy nejsou oba prázdné, tak porovnává jejich první prvky a ten menší přesune do výsledného seznamu. Pokud se jeden seznam vyprázdní, tak ten zbylý se celý rovnou přesune na konec výsledného seznamu.
	- Pokud je seznam prázdný, nebo obsahuje jen jeden prvek, tak je seřazený a není tedy nutné nic s ním dělat.

- Metody pro řazení seznamu mají tyto dvě základní definice:
	- `public static <T extends Comparable<? super T>> void sort(List<T> list)`
	- `public static <T> void sort(List<T> list, Comparator<? super T> c)`
- Příklad: Seřaďte takto vytvořený seznam čísel vzestupně a pak též sestupně:
```java
List<Integer> x = new ArrayList<>();
x.add(2); x.add(7); x.add(4); x.add(5);
```
- Seznam seřadím vzestupně přirozeným uspořádáním:
	- `Collections.sort(x);`
- Pro opačné uspořádání musíme definovat ještě komparátor:
```java
class Cmp implements Comparator<integer> {
	@Override public int compare(Integer a, Integer b) {
		return -1 * a.compareTo(b);
	}
}
Collections.sort(x, new Cmp());
```
## Zamíchání
- Algoritmus zamíchání (shuffle) se snaží zničit jakoukoli stopu uspořádání v zadaném seznamu.
	- Pro svou činnost potřebuje objekt, který je schopen vracet náhodná čísla. Může to být libovolný objekt implementující zhraní
		- `java.util.random.RandomGenerator`
	- Pro algoritmus míchání je důležité, že rozhraní definuje metodu
		- `int nextInt(int bound)`
	- která vrátí pseudonáhodně vybranou celočíselnou hodnotu mezi nulou (včetně) a zadanou hodnotou bound (exkluzivní).
- Zamíchání můžeme provádět např. pomocí těchto metod:
	- `public static void shuffle(List<?> list, RandomGenerator rnd)`
		- pak něco na způsob:
			- `for (int i=size; i>1; i--) swap(list, i-1, rnd.nextInt(i));`
	- `public static void shuffle(List<?> list)`
## Manipulace s daty
```java
public static void reverse(List<?> list)

public static <T> void fill(List<? super T> list, T obj)
// Nahradí všechny prvky seznamu list zadaným prvkem obj.

public static <T> void copy(List<? super T> dst, List<? extends T> src)
// Zkopíruje všechny prvky ze seznamu src do dst.
// Velikost seznamu dst musí být větší nebo rovna velikosti seznamu src.

public static void swap(List<?> list, int i, int j)

public static boolean addAll(Collection c, T... elems)
// Přidá všechny zadané prvky v poli elems do zadané kolekce c.
```
## Vyhledávání
- Algoritmus pro vyhledání prvku key typu T v ==seřazeném== seznamu list je k dispozici v těchto dvou verzích podle toho, zda se má při hledání použít přirozené uspořádání nebo definované přes komparátor:
	- `public static <T> int binarySearch(List<? extends Comparable<? super T>> list, T key)`
	- `public static <T> int binarySearch(List<? extends T> list, T key, Comparator<? super T> c)`

- Pokud je prvek key obsažen v seznamu list, tak je vrácen index toho prvky v seznamu.
- Jinak je vrácena záporná hodnota –(\<pos>+1), kde \<pos> je index, na kterém by se prvek key měl v seznamu nacházet, kdyby v seznamu byl. Konkrétně pro \<pos> platí:

- Algoritmus hledá prvek metodou půlení intervalu (binary search).
## Kompozice
- Uvedeme si tyto dva algoritmy:
```java
public static int frequency(Collection<?> c, Object o)
// Vrací počet prvků e v kolekci c takových, že Objects.equals(o, e)==true.
// Schematicky lze tento algoritmus zapsat jako:
	// int result = 0; for (Object e : c) if (o.equals(e)) result++; return result;
// Algoritmus též řeší případ, kdy o == null.

public static boolean disjoint(Collection c1, Collection c2)
// Vrací hodnotu true, pokud zadané kolekce nemají žádný společný prvek.
// V zásadě jde o to zjistit zda nějaký prvek c1 je též v c2. Schematicky lze tento algoritmus zapsat jako:
	// for (Object e : c1) if (c2.contains(e)) return false; return true;
// Algoritmus ve je skutečnosti implementován lépe. Bere např. v potaz, zda c1 nebo c2 implementuje Set (je efektivní volat contains na množině).
```
## Hledání extrémních hodnot
- Jde o algoritmy „min“ a „max“ pro nalezení nejmenšího a největšího prvku v kolekci.
```java
public static <T extends Object & Comparable<? super T>> T min/max(Collection<? extends T> coll)
// přirozené uspořádání

public static <T> T min/max(Collection<? extends T> coll,
Comparator<? super T> comp)
// Comparator
```

# Nemodifikovatelné kolekce a mapy
- Připomeňme si, že kolekce je nemodifikovatelná, když všechny její mutátory hází výjimku UnsupportedOperationException.
- Rozlišujeme dva typy nemodifikovatelných kolekcí a map:
	- Nezávislé nemodifikovatelné kolekce a mapy.
		- Přímo drží data v sobě.
		- Vytváří se pomocí statických metod v rozhraních List, Set, Map
	- Nemodifikovatelné pohledové kolekce a mapy.
		- Instance pohledové kolekce nebo mapy si drží odkaz na původní kolekci nebo mapu.

- Hlavní rozdíl mezi oběma typy kolekcí/map je v tom, že ty nezávislé jsou skutečně nemodifikovatelné.
	- Pohledová kolekce toto garantovat nemůže.
- 