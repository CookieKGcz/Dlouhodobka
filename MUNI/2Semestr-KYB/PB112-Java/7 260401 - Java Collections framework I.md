# Java Collections framework
## Java Collections framework
- (JCF) je jednotná architektura pro ukládání a manipulaci se skupinami objektů.
	- = sada rozhraní, abstraktních a konkrétních tříd.
	- Objekty se nazývají prvky nebo též elementy. U map pak používáme pojmy klíč a hodnota.
- Kód je v balíku java.util a skládá se z:
	- Rozhraní: Definují různé způsoby práce se skupinami objektů.
	- Implementací: Konkrétní implementace rozhraní.
	- Algoritmy: Efektivní implementace metod pracujících s kolekcemi.
## Rozhraní a jejich implementace
- ![[Pasted image 20260401080248.png|500]]
## Kolekce vs mapy
- Hlavní důvod pro oddělení kolekcí a map je pohled na prvky.
	- Prvek v kolekci je atomický. Neuvažuje se jeho vnitřní struktura.
	- Prvek v mapě je dvojice - klíč a hodnota.
		- uvažuje se tedy jeho vnitřní struktura
- To se též odráží ve způsobu, jak lze prvky procházet
	- kolekcích postupně v mapách pouze klíče/pouze hodnoty/páry (klíč, hodnota)
## JCF vs pole
- Pole není kolekce ani mapa i přesto, že poskytuje způsob pro ukládání, přístup a manipulaci se skupinami objektů.
- JCF ale poskytuje převody kolekcí na pole (i naopak).
# Rozhraní definují kolekce
## Rozhraní Collection
- Definuje mimo jiné tyto metody:
	- boolean add(E, e);
		- zajistí, aby kolekce obsahovala zadaný prvek
		- Vrátí hodnotu true, pokud se tato kolekce v důsledku volání změnila
		- Vrátí hodnotu false, pokud tato kolekce neumožňuje duplikáty a již obsahuje zadaný prvek
	- boolean remove(Object o);
		- Odebere z kolekce nějaký prvek e takový, že Objects.equals(o, e)\=\=true, pokud kolekce obsahuje jeden takový prvek.
	- boolean contains(Objects o);
		- Vrací hodnotu true tehdy a jen tehdy, když tato kolekce obsahuje alespoň jeden prvek e takový, že Objects.equals(o, e)\=\=true
	- int size();
		- Vrátí počet prvků v této kolekci
	- boolean isEmpty();
		- Vrátí hodnotu true, pokud tato kolekce neobsahuje žádné prvky
	- void clear();
		- Odebere všechny prvky z této kolekce
- Většina kolekcí spravuje úložiště pro své prvky
	- pohledové kolekce využívají jiné kolekce na ukládání.
- Metoda, které modifikuje skupinu objektů v kolekci se nazývají mutátor
## Rozraní Iterable
- Rozhraní Iterable\<T> definuje schopnost sekvenčně procházet prvky typu T v kolekci.
- For-each:
	- `for (T <proměnná> : <výraz>) <příkkaz-nebo-blok>`
- Příklad: Napište metodu, která sečte celá čísla uložená v kolekci celých čísel.
```java
int sum(Iterable<Integer> numbers) {
	int s = 0;
	for (Integer x : numbers) s = s + x;
	return s;
}
```

- Jelikož for-each cyklus lze použít pro podtypy Iterable, tak bychom mohli metodu též definovat takto:
```java
int sum(Collection<Integer> numbers) {
	int s = 0;
	for (Integer x : numbers) s = s + x;
	return s;
}
```
## Rozhraní List
- Rozhraní List\<E> (seznam) představuje kolekci, v níž jsou prvky uloženy v určitém pořadí
	- jde o sekvenci prvků. Má smysl mluvit o začátku a konci sekvence
	- Můžeme k prvkům přistupovat podle jejich pozice.
	- Příklad: Zobrazme si v paměti instanci třídy implementující List, obsahující prvky 42, 4, 24, 2 v tomto pořadí.
	- ![[Pasted image 20260401082653.png|500]]
	- Seznam přepisuje chování těchto metod z rozhraní Collection:
		- boolean add(E e);
			- Připojí zadaný prvek na konec seznamu
		- boolean remove(Object o);
			- Odstraní první výskyt prvku (na nejmenším indexu)
	- Definuje:
		- void add(int index, E elem);
			- Vloží prvek na zadanou pozici v tomto seznamu
		- E remove(in index);
		- E set(int index, element);
		- E get(int index);
		- int indexOf(Object o);

- Rozhraní List poskytuje získání pohledové kolekce přes metodu subList:
	- List\<E> subList(int fromIndex, int toIndex);
		- vrátí pohledový seznam (from včetně, to bez)
	- Příklad: Nechť list je proměnná typu List a platí list.size()\=\=10. Vymažte ze seznamu prvky na indexech 3, 4 a 5
## Rozhraní Queue
- Rozraní Queue\<E>(fronta) definuje kolkci, která ukládá prvky do sekence. Pořadí prvků toto rozhraní ale nedefinuje.
	- Prvkům nejsou přiřazeny indexy.
	- Lze odebírat jen ze začátku fronty
- Nejběžnější způsob = FIFO
- Nejčastěji implementují datovou strukturu minimová halda.

| Operace       | Hází výjimku | Vrací hodnotu     | Situace                 |
| ------------- | ------------ | ----------------- | ----------------------- |
| Vložení prvku | add(e)       | offer(e) -> false | Překroční max. kapacity |
| Rušení prvku  | remove()     | poll() -> null    | Fronta je prázdná       |
| Získání prvku | element()    | peek() -> null    | Fronta je prázdná       |
## Rozhraní Deque
- Rozhraní Deque\<E> (balíček) definuje kolekci, která uchovává prvky v určitém implementačně daném pořadí a lze přidávat a odebírat prvky z ==obou konců==
	- sekvence
	- prvky nejsou přiřazeny indexy
	- "Double Ended Queue"
- Definuje:
	- `void addFirst/offerFirst(E e);`
	- `void addLast/offerLast(E e);`
	- `E removeFirst/pollFirst();`
	- `E removeLast/pollLast();`
	- `E getFirst/peekFirst();`
	- `E getLast/peekLast();`

| Operace       | Hází výjimku | Vrací hodnotu      | Situace                 |
| ------------- | ------------ | ------------------ | ----------------------- |
| Vložení prvku | add*(e)      | offer*(e) -> false | Překroční max. kapacity |
| Rušení prvku  | remove*()    | poll*() -> null    | Deque je prázdná        |
| Získání prvku | get*()       | peek*() -> null    | Deque je prázdná        |
- můžeme používat i LIFO s Deque
## Rozhraní Set
- Rozhraní Set\<E> (množina) definuje kolekci, která neobsahuje žádné duplicitní prvky
	- může taky obsahovat pouze jeden odkaz na null
- Chování množny není specifikováno, pokud se hodnota prvku v množině změní způsobem, který ovlivní porovnávání objektů metodu equals.
- Definuje:
	- boolean addAll(Collection\<? extends E> c);
		- přidá prvky z kolekce do množiny
	- boolean retainAll(Collection\<?>c);
	- boolean removeAll(Collection\<?>c);
	- boolean containsAll(Collection\<?>c);
## Rozhraní SortedSet
- Rozhraní SortedSet\<E> (seřazená množina) definuje kolekci, která neobsahuje žádné duplicitní prvky, a která dále poskytuje úplné uspořádání svých prvků.
	- Prvky seřazené množiny lze procházet ve vzestupném pořadí.
	- Pokud má seřazená množina správně implementovat rozhraní Set, tak používané uspořádání musí být konzistentní s equals.
- Definuje:
	- E fisrt();
	- E last();
	- SortedSet\<E> subSet(E fromElement, E toElement);
		- Vrátí pohledovou množinu pro prvky mezi zadaným prvkem fromElement včetně a prvkem toElement bez něj.
		- Pokud jsou fromElement a toElement stejné, vrácená pohledová množina je prázdná.
- Chování množiny není specifikováno, pokud se hodnota prvku v množině změní způsobem, který ovlivní srovnávání objektů v uspořádání.
# Rozhraní definující mapy
## Rozhraní Map
- Rozhraní Map<K,V> (mapa; zobrazení) definuje schopnost objektu mapovat klíče na hodnoty
	- Mapa nemůže obsahovat duplicitní klíče.
	- Každý klíč můžeme mapovat maximálně na jednu hodnotu.
	- Jde o model pojmu funkce (zobrazení) 𝑓:𝐾 → 𝑉 z matematiky.
	- Umožňují procházet obsah mapy jako
		- Množinu Set\<K> klíčů,
		- Kolekci hodnot nebo
		- Množinu Set< Map.Entry<K, V>> párů klíč–hodnota, kde rozhraní Entry<K, V> reprezentuje pár klíč–hodnota. Definuje metody jako getKey, getValue, setValue.
- Definuje:
	- int size();
	- boolean isEmpty();
	- void clear();
	- boolean containsKey(Object key);
	- V get(Object key);
	- V put(K key, V value);
	- V remove(Object o);
- Mapy též podporují pohledové kolekce (view collections)
	- Prvky neukládají, ale spoléhají se na podpůrnou kolekci.
- Pohledové kolekce můžeme získat pomocí metod:
	- Set\<K> keySet();
	- Collection\<V> values();
	- Set<Map.Entry<K, V>> entrySet();
## Rozhraní SortedMap
- Rozhraní SortedMap<K,V> (uspořádaná mapa/zobrazení) definuje schopnost objektu mapovat klíče na hodnoty. Přitom dále poskytuje úplné uspořádání svých klíčů.
	- Klíče jsou seřazeny pomocí svého přirozeného uspořádání nebo pomocí komparátoru (instance třídy implementující Comparator\<K>).
	- Klíče seřazené množiny lze procházet ve vzestupném pořadí.
	- Pokud má seřazená množina správně implementovat rozhraní Map, tak používané uspořádání musí být konzistentní s equals.
- Definuje:
	- K firstKey();
	- K lastKey();
	- SortedMap<K,V> subMap(K fromKey, E toKey);
# Implementace rozhraní kolekcí
## Třída ArrayList
- Seznam je reprezentován prostým polem objektů (Object[]).
	- Délka pole představuje aktuální kapacitu seznamu, tj. kolik prvků lze do seznamu vložit (než je třeba vytvořit větší pole).
- Dále se uchovává aktuální počet prvků v seznamu.
- ArrayList je efektivní pro vkládání nebo rušení prvků z konce.
- Není ale efektivní při vkládání nebo rušení prvků z vnitřku seznamu.
- Je velmi efektivní pro získání nebe zapsání hodnoty na daném indexu.

- Příklad: Použití ArrayListu:
```java
List<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.add("Cherry");
System.out.println("Second item: " + list.get(1)); // Banana
for (String item : list)
	System.out.println(item); // Apple, Banana, Cherry
list.remove("Banana");
System.out.println("Has Cherry? " + list.contains("Cherry")); // True
```
## Třída LinkedList
- Seznam je realizován jako dvojitě zřetězený seznam.
	- Seznam se skládá z propojených uzlů (Node), ve kterých jsou hodnoty uloženy.
```java
class Node<E> {
	E item;
	Node<E> next;
	Node<E> prev;
}
```
- Instance seznamu si drží odkazy na první a poslední uzel.
- Třída LinkedList je efektivní při vkládání nebo rušení prvků na začátku i konci seznamu.
- LinkedList ale není efektivní při získávání hodnoty na daném indexu.
- Má větší paměťové nároky než ArrayList.
## Třída ArrayDeque
- Třída ArrayDeque implementuje Deque pomocí pole.
	- Prvky jsou v poli uloženy cyklicky mezi indexy head a tail.
	- head je index prvního prvku a tail je pozice za posledním prvkem.
## Třída PriorityQueue
- Prioritní frontu použijeme v případě, že chceme prvky z fronty získávat v pořadí podle uspořádání definovaném na prvcích.
	- V klasické (ne prioritní) frontě chceme prvky získávat v pořadí v jakém byly do fronty vloženy, tj. FIFO.
- implementuje prioritní frontu jakožto ==minimovou vyváženou binární haldu==.
- Binární halda je stromová struktura
	- Souvislý orientovaný graf, bez cyklů, ...
- Halda je vyvážená, pokud má všechna „patra“ zaplněná, případně kromě posledního.
- Důležité je, že vyváženou binární haldu lze vždy uložit v poli
## Třída HashSet
- Třída HashSet\<E> je implementována pomocí mapy. 
	- Prvky množiny jsou klíče v mapě. Mapa je definována takto:
		- `HashMap<E, Object>`
	- Všechny klíče (prvky) jsou mapovány jeden a tentýž objekt:
		- `static final Object PRESENT = new Object();`
## Třída TreeSet
- Třída TreeSet\<E> je implementována pomocí mapy typu TreeMap\<E, Object>
