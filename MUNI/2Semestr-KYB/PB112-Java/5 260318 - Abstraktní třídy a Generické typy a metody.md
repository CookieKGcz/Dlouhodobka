# Abstraktní třídy
## Definice
- definovaná pomocí klíčového slova abstract takto:
```java
<modifikátor> abstract class <jméno>
	<nic-nebo-extends> <nic-nebo-implements>
{
	<nic-nebo-abstraktní-metody>
	<nic-nebo-atributy-metody-atd>
}
```
- Abstraktní metoda je metoda def. pomocí klíčového slova abstrakt takto:
```java
<modifikátor> abstract <návratový-typ> <jméno>(
	<nic-nebo-seznam-parametrů>
	);
```
- Smyslem abstraktní metody je vynutit si její implementaci v podtřídě, která už není abstraktní.

- Pro abstraktní metodu platí, že:
	- Nemá implementaci
		- implementace bude v podtřídách
	- nemůže být statická
		- podtřídy by ji nemohly přepsat
	- nemůže být private
		- -||-
	- Nemůže být deklarována se slovem final
		- -||-

- Smyslem je poskytnout data, metody a rozhraní, které jsou společné pro všechny třídy v dané hierarchii dědičnosti.
	- Třída nepopisuje kompletní objekty
- Pro abstraktní třídu platí:
	- Nelze vytvářet její instance
	- Nelze třídu definovat s klíčovým slovem final.
	- Můžeme v ní definovat vše co v ne-abstraktních třídách

## Příklad
- Příklad: Podívejme se použití abstraktní třídy v hierarchii tříd zvířat. Zavedeme si abstraktní třídu Animal takto.
```java
public abstract class Animal {
	protected boolean isTired;
	public Animal() { isTired = false; }
	public void sleep() { isTired=false; }
	abstract void makeSound(); //vynucení
}
```
- Může ale sloužit jako společná rodičovská třída pro mnoho tříd definující kompletní zvířata. Např. pes a kočka:
```java
public class Dog extends Animal {
	public Dog() { super(); }
	@Override
	void makeSound() { System.out.println("Woof!"); }
}

public class Cat extends Animal {
	public Cat() { super(); }
	@Override
	void makeSound() { System.out.println("Meow!"); }
}
```

## Abstraktní třída vs Rozhraní
- Nejprve si položme otázku, zda buď abstraktní třídy nám stačí (tj. nepotřebujeme rozhraní) anebo je to přesně naopak.

| Vlastnost                       | Abstraktní třída | Rozhraní            |
| ------------------------------- | ---------------- | ------------------- |
| Klasické atributy               | Ano              | Ne                  |
| Konstruktory                    | Ano              | Ne                  |
| Klasické metody                 | Ano              | Ano, pomocí default |
| Abstraktní metody               | Ano              | Ano                 |
| Vícenásobné rozšíření (extends) | Ne               | Ano                 |
- Důležité je též znát rozdíl ve významu (účelu) obou pojmů.

| Konstrukt        | Význam / Účel                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Abstraktní třída | Definice dat (atributů) a chování (metod) společných pro všechny instance v podtřídách této třídy. |
| Rozhraní         | Specifikace schopností pro objekty tříd, které spolu mohou, ale nemusí být ve vztahu dědičnosti.   |
- Abstraktní třída silně souvisí s dědičností tříd, které ji rozšiřují.
- Rozhraní nesouvisí s dědičností tříd, které ho implementují.
### Příklad
- Chceme pracovat s objekty, které umí létat. Měli bychom si položit tyto otázky:
	- „umět létat“ je schopnost (dovednost)
	- Nijak nesouvisí s typem objektu (může to být pták, letadlo, netopýr).
	- Objekty s touto schopností tedy mohou být zcela nezávislé z pohledu dědičnosti.
- Proto nám vychází, že zavedeme ==rozhraní== (ne abstraktní třídu):
	- `interface Flyable { void fly(); }`
- Třídy Bird, Airplane a Bat budou toto rozhraní implementovat.



- Vytváříme software pro různá elektronická zařízení (např. chytré telefony, tablety, notebooky).
- Pracujeme s jednou hierarchií tříd dědících z abstraktní třídy
- ElectroDevice (např. class Tablet extends ElectroDevice).
	- Společná data budou např. cena, velikost paměti, typ procesoru, apod.
	- Abstraktní metody budou např. getUserInput(), lockScreen(), apod.
- Jednotlivá zařízení mohou ale mít jen některé ze schopností (Connectable, Updateable, Monitorable)
	- Notebook je Conn. ale není Monitorable (bez GPS)

- Uvedené schopnosti tedy nelze všechny dát do ElectroDevice.
- Nemůžeme je definovat ani jako abstraktní třídy, protože bychom pak nemohli definovat:
```java
class Notebook extends
	ElectroDevice, Connectable, Updatable // Nelze dědit z více tříd.
{ … }
```
- Proto schopnosti Connectable, Updatable, Monitorable definujeme jako rozhraní.



- Vytváříme hru, kde každá entita ve hře má unikátní identifikátor.
	- Toto společné „id“ můžeme dát do bázové třídy.
	- Neměli bychom ale vytvářet instance bázové třídy, protože nejde o žádnou reálnou entity ve hře.
- Jelikož máme společná data a nechceme vytvářet instance, tak entitu definujeme pomocí abstraktní třídy:
```java
abstract class Entity {
	protected final long id;
	protected Entity(long id) { this.id = id; }
}
```




- Chceme zpracovávat data uložená v souborech v různých formátech (např. JSON, CSV, XML). Jednotlivé třídy by měly tedy být „datové procesory“.
- Procesor by měl být schopen vykonat tyto operace:
	- Načíst data se souboru (v jeho formátu).
	- Zpracovat načtená data.
	- Uložit zpracovaná data do souboru (opět v jeho formátu).
- Důležité je, že chceme vynutit, aby každý procesor vykonal ty tři operace přesně v uvedeném pořadí.

- Kdybychom definovali DataProcessor jako rozhraní:
```java
public interface DataProcessor {
	void readData();
	void processData();
	void saveData();
}
```
 - tak nemáme zaručeno, že každá třída implementující rozhraní bude volat ty metody ve správném pořadí. Mohli bychom sice zavést defaultní metodu process():
```java
default void process() {
	readData(); processData(); saveData();
}
```
- ale implementující třída může metodu process() přepsat.

- Pomocí abstraktní třídy lze přepsání zabránit:
```java
public abstract class DataProcessor {
	public final void process() { // slovo final zabrání přepisování metody v potomcích
		readData(); processData(); saveData();
	}
	protected abstract void readData(); // protected -> nechceme nám někdo volal metody jinak než přes process().
	protected abstract void processData();
	protected abstract void saveData();
}
```
# Generické typy a metody
## Motivace
- Uvažujme tuto třídu „krabice“, do které si můžeme vložit libovolný objekt:
```java
class Box {
	private Object x;
	public void set(Object o) { x = o; }
	public Object get() { return x; }
}

Box box=new Box();
box.set(42);
String s=(String)box.get(); // CHYBA ZA BĚHU PROGRAMU! Konvertujeme Int na Str
```
- Generické typy nám umožní tuto chybu zachytit již ==při překladu== programu.
## Definice
- Generický typ je taková třída nebo rozhraní, jenž je ==parametrizována== jedním nebo více ==typovými parametry== (proměnnými)
- Generickou třídu vytvoříme tak, že za jméno třídy napíšeme seznam typových parametrů v tomto tvaru:
	- `< <jméno-parametru-1>, …, <jméno-parametru-N> >`

- Generické rozhraní definujeme zcela stejně - seznam typových parametrů mezi < a > za jménem rozhraní.
- Příklad: Definujme třídu Box z předchozího příkladu jako generickou:
```java
class Box<T> {
	private T x;
	public void set(T o) { x = o; }
	public T get() { return x; }
}
```

## Konvence pro typové parametry
- Proměnné v programu typicky pojmenováváme celými slovy a často malými písmeny.
- Abychom od nich odlišili typové parametry, tak pro používáme tato jména:
	- E : Jako ==Element== – pro typ prvků v kolekci objektů.
	- K : Jako ==Key== – pro typ klíče pro porovnání objektů v kolekci.
	- N : Jako ==Number== – pro číselné typy (Integer, Double,…)
	- T : Jako ==Type== – jakýkoliv typ bez bližšího určení.
	- V : Jako ==Value== – tedy typ hodnoty (typicky přiřazené ke klíči).
	- S,U,W,… : Podobně jako T, pokud máme více typových parametrů.

## Generické typy
- Proměnnou generického typu (třídy nebo rozhraní) definujeme tak, že před názvem proměnné uvedeme instancovaný generický typ.
- Příklad: Použijme generickou třídu Box stejným způsobem, jako v úvodním příkladu:
```java
Box<Integer> box=new Box<Integer>();
box.set(42);
String s=(String)box.get(); // chyba při překladu
```

- Datové typy, které dosazujeme za typové parametry při instancování generického typu nazýváme ==typové argumenty==.
- Překladač Javy umí odvozovat vhodné dosazení typů za typové parametry ze souvisejícího kódu.
	- `Box<Integer> box=new Box<>();`
	- v `Box<>` si to odvodí


- Příklad: Definujme generickou třídu „pár“ takto:
```java
class Pair<K, V> {
	private final K key;
	private final V value;
	Pair(K k, V v) { key = k; value = v; }
	K getKey() { return key; }
	V getValue() { return value; }
}
```
## Horní meze typového parametru
- Typový parametr T představuje libovolný typ.
- Můžeme chtít, aby T představoval pouze libovolný typ, který dědí přímo nebo nepřímo z nějaké třídy nebo implementuje určité rozhraní.
- To zajistíme uvedením horní meze typového parametru. Použijeme tuto syntaxi pro T v seznamu typových parametrů:
	- `T extends C & l1 & ... & ln`

- Do třídy Util z předchozího příkladu vložte metodu sum, která přijme dvě krabice s čísli do parametrů stejného typu a vrátí součet těch čísel jako hodnotu typu double.
```java
static <T extends Number> double sum(Box<T> a, Box<T> b) {
	return a.get().doubleValue() + b.get().doubleValue();
}

//použití
Box<Integer> a = Util.box(42);
Box<Integer> b = Util.box(24);
double d = Util.sum(a,b);

Box<Float> a = Util.box(42.0f);
Box<Float> b = Util.box(3.1415f);
double d = Util.sum(a,b);
```

```java
Box<A> a = Util.box(new A());
Box<A> b = Util.box(new A());
double d = Util.sum(a,b);
```
- Pokud by ale třída A nedědila z Number, tak bychom dostali chybu při překladu. Toto použití vede k chybě při překladu:
```java
Box<Integer> a = Util.box(42);
Box<Double> b = Util.box(3.1415);
double d = Util.sum(a,b); // zde se překladači nepodaří odvodit spol typ pro typový param. T.
```
## Dolní mez typového parametru?
- Pro typový parametr nelze definovat dolní mez v hierarchii dědičnosti.
	- Je to možné pouze pro zástupný typový parametr, ale na něj se podíváme později.
- Příklad: Předpokládejme, že bychom mohli typovému parametru stanovit dolní mez (i když to nelze). Ukažme si to na příkladu třídy Box.
```java
class Box<T „je libovolná nadtřída třídy“ Integer> { // nelze v Javě vůnec napsat
	private T x;
	public void set(T o) { x = o; }
	public T get() { return x; }
}
```
## Zástupný typový parametr
- Místo typové proměnné v generickém typu nebo metodě můžeme použít zástupný typový parametr (wildcard).
- Označuje se symbolem otazník: ?
	- `Box<?> x = new Box<Integer>();`
	- Použití zástupného parametru. Proměnná x je typu krabice s hodnotou neznámého typu.
	- Do proměnní x můžeme vložit instanci Box\<Integer>, protože Box \<\?\> představuje i typ Box\<Integer>.
- Proměnnou x můžeme použít klasickým způsobem:
- `Integer i = (Integer)x.get();`

- Příklad: Přidejte do třídy Util metodu, která vypíše obsah krabice (každý objekt, který v ní může být). Předpokládejte, že v krabici vždy něco je.
```java
static void printBox(Box<Object> b) {
	System.out.println("Box has: " + b.get());
}


Util.printBox(Util.box(42));
Box<Object> o = Util.box(42);
Util.printBox(o);

//už nebude fungovat
Box x = Util.box(42);
Util.printBox(x);
```
- Opět narážíme na problém s odvozením typu překladačem.
	- Pokud máme instancovaný typ, tak odvození se již nemusí povést.
- Každopádně, obecné řešení dostaneme použitím zástupného parametru:
```java
static void printBox(Box<?> b) {
	System.out.println("Box has: " + b.get());
}
```

## Meze pro zástupný typový parametr
- Zástupný parametr lze omezit buď zdola nebo shora (ne však z obou směrů zároveň).
- Pro stanovení horní meze H použijeme syntaxi:
	- `<? extends H>`
- Pro stanovení dolní meze D použijeme syntaxi:
	- `<? super D>`

- Příklad: Vraťme se k metodě sum, která byla definována takto:
```java
static <T extends Number> double sum(Box<T> a, Box<T> b) {
	return a.get().doubleValue() + b.get().doubleValue();
}
```
- Víme, že její toto použití vedlo k chybě při překladu:
```java
Box<Integer> a = Util.box(42);
Box<Double> b = Util.box(3.1415);
double d = Util.sum(a,b);
```
- Problém lze vyřešit i bez použití typového parametru.

- Stačí použít zástupný parametr v parametrech metody:
```java
static double sum(Box<? extends Number> a, Box<? extends Number> b) {
	return a.get().doubleValue() + b.get().doubleValue();
}
```
- Parametry a,b teď mohou nezávisle získat instance třídy Box s objektem libovolné třídy dědící z Number.

- Dolní mez zástupného parametru nám umožňuje uvažovat všechny typy, kde typový parametr je nějakou nadtřídou dané meze (nebo přímo tou mezí).
- Příklad: Uvažujme tyto třídy
	- `class A {}   class B extends A {}   class C extends B {}`
- Definujeme proměnnou x takto:
	- `Box<? super B> x;`

- Můžeme do ní vložit instance tříd Box a Box **, ale nelze** do ní vložit instanci třídy Box.
## Podtyp
- V Javě existuje mezi typy vztah (relace) podtypu:
	- „typ A je(není) podtypem typu B“
- V této relaci jsou třídy, které jsou ve vztahu dědičnosti.
	- Pokud máme `class A {}    class B extends A {}`
	- tak B je podtypem A.
- Pro generické typy je ale relace podtypu definována nezávisle na dědičnosti.

- Pokud máme typy
	- `Box<Number> Box<Integer>`
- tak Box\<Integer> není podtypem Box\<Number>. Není to ani opačně. Mezi těmito typy tedy není žádný vztah z hlediska relace podtypu, i přes to, že typ Integer je podtypem typu Number. Proto nemůžeme psát:
	- `Box<Number> x = new Box<Integer>();`

- B -> A značí, že B je podtypem A.
- ![[Pasted image 20260318092507.png|300]]
- Mezi generickými typy můžeme vytvářet vztahy stejně jako mezi negenerickými typy.

- Příklad: Pokud zavedeme třídu MagicBox takto:
	- `class MagicBox<T> extends Box<T> {}`
- tak můžeme psát:
	- `Box<Integer> x = new MagicBox<Integer>();
- protože bude platit podtypová relace:
	- ![[Pasted image 20260318092636.png|150]]
## Podtyp se zástupným typovým parametrem
- Datový typ se zástupným parametrem je automaticky nadtypem každého typu, kde je zástupný parametr nahrazen.
- Příklad: Typy Box\<Integer>, Box\<Double>, MagicBox\<Integer> jsou podtypy typu Box\<?>.
- Můžeme tedy psát:
```java
Box<?> x = new MagicBox<Integer>();
Box<?> y = new Box<Integer>();
Box<?> z = new Box<Double>();
```
- ![[Pasted image 20260318092823.png|220]]

- Generický datový typ C (třída nebo rozhraní) se zástupným parametrem s horní/dolní mezí M je automaticky nadtypem každého typu C\<X>, kde X je M nebo jeho podtypem/nadtypem.
- Příklad: Uvažujme opět třídy
	- `class A {}    class B extends A {}    class C extends B {}`
- Pak bude platit
	- `Box<B>, Box<C> jsou podtypy Box<? extends B>.`
	- `Box<B>, Box<A> jsou podtypy Box<? super B>.`
- ![[Pasted image 20260318093016.png|400]]