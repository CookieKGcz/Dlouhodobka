# Statické atributy a metody
## Statické atributy
- ve třídě -> a neleží v žádné instancí třídy.
	- nazýváme statické
	- definujeme pomocí `static`
	- pro práci se statickým atributem nepotřebujeme žádnou instanci třídy
	- z vnějšku
		- <jméno-třídy>.<jméno-statického-atributu>
- statické atributy jsou uloženy na haldě

- class A { **static** int x; int y; void f() { y = x; } }
	- Přiřazení ze statického do klasického atributu.
- A.x = 1;                                    <- nepotřebuji instanci třídy
- A u = new A(); A v = new A();
- u.f();                                         <- nastaví u.y na 1
- A.x = 2; v.f();                            <- nastaví v.y na 2

- Upravte třídu class A { int id; } tak, že v i-té vytvořené instanci třídy A bude atribut id obsahovat hodnotu i.
- Řešení: Do třídy zavedeme statický atribut, který bude iniciálně 1 a s každou vytvořenou instancí se v konstruktoru inkrementuje.
```java
class A {
	static int counter = 1;
	int id;
	A() {
		id = counter;
		counter = counter + 1;
	}
}
```
- Použití:
	- `A u = new A();` -> `u.id==1, A.counter==2`
	- `A v = new A();` -> `v.id==2, A.counter==3`
## Inicializace statických atributů
- JVM nejprve automaticky nastaví statické atributy na defaultní hodnoty
- Přiřazením přímo v definici atributu, např.: static int counter = 1;
- Ve statickém bloku (static initializer) ve třídě, tj. syntaxí:
	- `static <blok>`

- Příklad: Uveďte varianty inicializace statických atributů třídy `class A { static int x; static A a; }`
```java
Varianta 1:
class A {
	static int x=1;
	static A a=new A();
}

Varianta 2:
class A {
	static int x=1;
	static A a;
	static { a=new A(); }
}

Varianta 3:
class A {
	static int x;
	static A a;
	static {
		x = 1;
		a=new A();
	}
}

Varianta 4:
class A {
	static { a=new A(); }
	static int x=2;
	static A a=null;
	static { x = 1; }
}
```

- Inicializace statických atributů dané třídy se provede
	- Pouze jednou. 
	- Před prvním použitím statických atributů. 
	- Před vytvořením první instance třídy.
## Statické metody
- nejsou svázané s žádnou instancí třídy
	- Takové metody nazýváme statické.
	- Ve statické metodě není k dispozici „this“ instance.
	- Z vnějšku třídy zavoláme statickou metodu přes jméno třídy:
		- `<jméno-třídy>.<jméno-statické-metody>(<hodnoty-parametrů>)`
- Příklad: Uvažujme tuto třídu A se statickou metodou f:
- `class A { static int f(int x) { return x + 1; } }`
- A.f(42);      <- nepotřebujeme instanci třídy

- A u = new A();
- u.f(42);       <- nevhodné !


- Příklad:
```java
class A {
	int y=1; void setY(int value) { // Klasický atribut a metoda/setter
		y = value;
	}    
	static A x = new A();
	static { f(x.y); }    // Volání statické metody f s hodnotou 1
	static void f(int x) {
		A.x.setY(x + 41);   // Nutné - kolikze jména x s paramentrem
	}
	static { setY(42); }    // CHYBA ! Nelze volat slasickou metodu
	static void error() { 
		this.y=42; y=42; setY(42); // CHYBA ! this. není k dispozici
	}
}
```
### Příklad: Metoda main
- Vykonávání programu začíná ve statické metodě s názvem main. Je typicky definovaná takto:
	- `public static void main(String[] args) { … }`
### Příklad: Singleton
- Pokud potřebujeme zajistit, aby v celém programu existovala **nejvýše jedna instance** **třídy**, tak tu třídu definujeme jako **Singleton**.

- Příklad: Definujte třídu A jako singleton.
```java
class A {
	private A() {} // Zabrání vytváření instancí z vnějšku třídy.
	private static A instance;  // K držení jediné instance. Iniciálně je null.
	public static A getInstance() {  // Přístup k jediné instanci.
		if (instance == null) instance = new A();
		return instance;
	}
}
```
## Import static
- Z vnějšku třídy se na statické atributy a metody odkazujeme přes jméno třídy (a tečku).
- nemusí být nejlepší z pohledu čitelnosti programu.
- Proto Java umožňuje importovat vybrané statické atributy a metody do daného .java souboru.
	- `import static <plné-jméno-třídy>.<jméno-statické-metody/atributu>;`

- Příklad:
```java
	package p; // Třída musí být v nějakém (ne defaultním) balíku
	class A { public static int increment(int x) { return x+1; } }
Použití v B.java:
	import static p.A.increment;
	class B {
		int foo() {
			return increment(42);
			// Díky importu nemusíme psát „p.A.“ před jméno metody.
		}
	}
```

# Konstanty
## Konstanty
- Konstanta je proměnná, jejíž hodnotu můžeme nastavit pouze jednou.
	- Nepočítá se do toho inicializace proměnné na defaultní hodnoty, kterou provádí JVM automaticky
	- pomocí klíčového slova `final`
	- Jména konstant, které jsou statické atributy třídy, typicky píšeme velkými písmeny.

- Příklad:
```java
class SimpleMath {
	static final double PI; static {
	// Statický atribut, který je současně konstantou.
		PI = 3.14159;
		// První přiřazení do konstanty nastaví její hodnotu.
	}
	static double circleLength(double radius) {
		final double length = 2.0 * PI * radius;
		// Lokální proměnná, která je konstantou.
		// Rovnou je jí nastavena hodnota.
		lenght = 42.0; // CHYBA ! Konstanta už byla nastavena, takže další přiřazení již není možné.
		return length;
	}
}
```

- Příklad:
```java
class Vector {
	final float x; final float y;
	Vector(final float x, final float y) {
	// Oba parametry jsou konstanty. Nelze je v metodě už měnit.
		this.x = x;
		this.y = y;
	}
}

```
- Uvažme nyní toto použití třídy vektor:
```java
Vector u = new Vector(1.0f, 2.0f);
float x = u.x; // Číst z konstanty můžeme.
u.x = x;  // CHYBA ! Znovu do konstanty zapsat už nelze.
```
- Příklad: Uvažme třídu class `A { int x=42; }` a toto její použití:
```java
// Proměnná a je konstantou (nelze změnit odkaz).
// Proměnná x třídy A není konstantou.
final A a = new A();
a.x = 1;
a = new A(); // CHYBA ! Znovu do konstanty zapsat už nelze.
```
## Záznam (record)
- datový typ, jehož atributy jsou konstanty
- Definujeme jej touto syntaxí:
```java
<modifikátor> record <jméno-záznamu>(
	<typ-1> <jméno-atributu-1>,
	…
	<typ-N> <jméno-atributu-N>
) {
	<nic-nebo-atributy-a-metody>
}
```
- V záznamu budou všechny atributy, které uvedeme. Každý z nich je definován jako privátní konstanta, tedy takto:
	- `private final <typ-i> <jméno-atributu-i>;`
- Java též automaticky vytvoří tzv. canonical konstruktor:
```java
public <jméno-záznamu>(<typ-1> <jméno-atributu-1>, …,
						<typ-N> <jméno-atributu-N>) {
	this.<jméno-atributu-1> = <jméno-atributu-1>; …
	this.<jméno-atributu-N> = <jméno-atributu-N>;
}
```
- Dale se vytvoří getter pro každý atribut:
	- `public <typ-i> <jméno-atributu-i>() {return <jméno-atributu-i>;}`

- **Hodnoty** (instance) záznamu jsou umístěny **na haldě**.
	- Vytváříme je pomocí operátoru new
- Proměnné typu záznam drží své hodnoty **odkazem**.
- Každý záznam implicitně dědí ze třídy `java.lang.Record`.

- Příklad: Vytvořte typ záznamu osob, kde každá osoba má jméno a věk. Uveďte příklad použití záznamu
- Řešení:
```java
public record Person(String name, int age) {}
Použití záznamu:
	Person a = new Person("John", 25);
	String s = a.name();
	int x = a.age();
	Person b = new Person("Alice", 20);
	a = b;
```

- Chování záznamu se dá dobře představit (a zapamatovat) tak, když se ho pokusíme vyjádřit pomocí třídy.
	- Přesně to udělat nejde, protože třída nemůže dědit z java.lang.Record.
	- Nedostaneme tedy validní Java kód. To ale nevadí, jde nám o představu chování.

- Příklad: Navrhněte třídu, která bude modelovat chování záznamu v předchozím příkladu.
- Řešení:
```java
public final class Person extends java.lang.Record { // normálně nejde
	// privátní konstanty
	private final String name;
	private final int age;

	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	// gettery
	public String name() { return name; }
	public int age() { return age; }

	@Override public boolean equals(Object o) { ... }
}
```


- V bloku záznamu můžeme definovat:
	- statické atributy, bloky, metody
	- klasické metody
	- vlastní verzi canonical konstruktoru
	- další konstruktory. Ty ale musí vždy volat canonical konstruktor
- V bloku záznamu **nemůžeme** definovat klasické atributy.

- Příklad: Přidejte kód do bloku záznamu `record Person(String name, int age) {}`
- Řešení:
```java
record Person(String name, int age) {
	public static final String SPECIES;
	static { SPECIES = "Homo sapiens"; }
	public static Person create(String name, int age) {
		return new Person(name, age);
	}

	private final int height; // CHYBA ! Klasické atributy do bloku nelze vkládat.
	public boolean isAdult() { return age >= 18; }
	public Person(String name, int age) {
		this.name = name == null ? "Unknown" : name;
		this.age = Math.max(age, 0);
	}
}
```

- Příklad: Uvažujme tuto třídu a záznam: `class A { int x; } record R(A a) {}`
- Podívejme se na toto jejich použití:
```java
R r = new R(new A());
r.a().x = 42;
```
- ![[Pasted image 20260304085944.png | 500]]
## Pomocná třída (utility class)
- Pomocná (nebo též užitková) třída obsahuje pouze statické metody a konstanty (případně též statické atributy).
- koncept
- Slouží jako sada algoritmů (podprogramů) a konstant, které mají být k dispozici zbytku programu.

- Příklad: Upravte třídu SimpleMath uvedenou dříve aby byla pomocnou třídou.
```java
// final zakážeme ze třídy dědit 
public final class SimpleMath {
	//private zakážeme vytvářet instance
	private SimpleMath() {}
	public static final double PI = 3.14159; // stat. konst.
	public static double circleLength(double radius) { … }
	// stat. metoda
}

```

# Výčtový typ
## Výčtový typ
- Pokud chceme vytvořit datový typ, který definuje malý počet hodnot, tak je vhodné použít **výčtový typ**. Má tuto syntaxi:
```java
<modifikátor-přístupu> enum <jméno-typu> {
	<název-hodnoty-1><nic-nebo-hodnoty-parametrů-1>,
	…
	<název-hodnoty-N><nic-nebo-hodnoty-parametrů-N>;
	<nic-nebo-atributy-metody>
}
```

- Příklad: Definujte výčtový typ, jehož hodnoty budou planety Merkur a Země. Vytvořte proměnnou s hodnotou Země.
- Řešení:
```java
enum Planet { MERCURY, EARTH; }
Planet p = Planet.EARTH;
```
- Výčtový typ T poskytuje (kromě jiného) tyto metody:
	- String name(): Vrátí jméno hodnoty (instance).
		- Bude platit:
			- Planet.MERCURY.name().equals(“MERCURY”) && Planet.EARTH.name().equals(“EARTH”)

- `int ordinal()`:
	- Vrátí pořadí hodnoty v typu. Číslováno je od 0.
		- Planet.MERCURY.ordinal() == 0 && Planet.EARTH.ordinal() == 1
- `int compareTo(T x)`:
	- Vrátí hodnotu: `this.ordinal() - x.ordinal()`
		- Pokud x je null nebo není typu T, tak dojde k chybě výpočtu
- `static T valueOf(String x)`:
	- Vrátí hodnotu typu T, která má jméno x.
		- Pokud x je null nebo žádná hodnota nemá jméno x, tak dojde k chybě výpočtu
- `static T[] values()`:
	- Vrátí pole všech hodnot typu v jejich pořadí.

- Každý výčtový typ implicitně dědí z třídy java.lang.Enum.
	- Ze třídy java.lang.Enum nejde dědit jinak, než definicí výčtového typu.

- Chování výčtového typu se dá dobře pochopit tak, že si ho namodelujeme pomocí třídy.
	- Nepůjde o reálný kód, pouze o představu chování.
- Příklad: Navrhněte třídu, která bude modelovat chování: `enum Planet { MERCURY, EARTH; }`
```java
final class Planet extends Enum<Planet> {
	private Planet(String name, int ordinal)
		{ super(name, ordinal); }
	public static final Planet MERCURY = new Planet("MERCURY", 0);
	public static final Planet EARTH = new Planet("EARTH", 1);
	private static final Planet[] VALUES = { MERCURY, EARTH };
	public static Planet[] values() { return VALUES.clone(); }
}
```
- Hodnoty výčtového typu leží na haldě.
- Proměnné výčtového typu drží své hodnoty odkazem.

- Příklad:
```java
public enum Planet {
	MERCURY(3.30e23, 2.44e6), EARTH(5.97e24, 6.37e6);

	private static final double G = 6.67e-11;
	public final double mass;
	public final double radius;

	// Konstrukor
	Planet(double mass, double radius)
	{ this.mass = mass; this.radius = radius; }
	// Metoda
	double surfaceGravity()
	{ return G * mass / (radius * radius); }
}
```
- Uvedený enum může použít třeba takto:
```java
final Planet p = Planet.MERCURY;
double mass = p.mass;
double accel = p. surfaceGravity();
```

- Příklad: Navrhněte třídu, která bude modelovat chování enumu v předchozím příkladu.
- Řešení: Uvedeme pouze klíčové části ve třídě class Planet. Zbytek je totiž stejný jako v příkladě uvedeném dříve.
```java
public static final Planet MERCURY =
	new Planet("MERCURY", 0, 3.30e23, 2.44e6);
public static final Planet EARTH =
	new Planet("EARTH", 1, 5.97e24, 6.37e6);
	
public final double mass;
public final double radius;

// konstrukor
private Planet(String name, int ordinal, double mass, double radius) {
	super(name, ordinal);
	this.mass = mass;
	this.radius = radius;
}
```

# Komentáře
## Komentáře
- ignorován překladačem
## Javadoc
- Dále můžeme uvádět informace v návěštích tvaru:
	- `@<jméno-návěští> <další-informace>`
- Příklady návěští:
	- @author <jméno-autora>
- @param <jméno-parametru> \<popis-parametru>
- @return <popis-toho-co-metoda-vrací>
- @see <třída>
- @see <třída>#<jméno-metody>(<seznam-typů-parametrů>)
- @see <třída>#\<atribut>
- @see \<a href=“\<URL>”> \<popis-odkazu> \</a>
- {@link \<odkaz> \<nic-nebo-popis-odkazu>}
	- \<odkaz> je ve stejném tvaru jako v @see.
- {@code <kód>}
	- Vysází <kód> ve fontu pro kód přímo do textu. Kód by měl být krátký.
- {@snippet : <kód>}
	- Vysází <kód> ve fontu pro kód jako samostatný blok kódu. Může být dlouhý.
- @version \<verze>
