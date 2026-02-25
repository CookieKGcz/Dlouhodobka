# Řídící struktury
## Podmíněný příkaz
- if (<výraz-typu-boolean>) <true-blok-nebo-příkaz>
- else <false-blok-nebo-příkaz>
- "int max()"
	- ![[Pasted image 20260225081656.png | 250]]
## Větvení podle hodnot
- výpočet lze větvit též podle hodnoty výrazu příkazem switch
```java
switch (<výraz>) {
	case <hodnota-1> -> <blok-nebo-příkaz-1>
	…
	case <hodnota-N> -> <blok-nebo-příkaz-N>
	default -> <blok-nebo-příkaz> (můžeme vynechat)
}
```
- ![[Pasted image 20260225082134.png | 250]]
- starší syntaxe:
	- ![[Pasted image 20260225082330.png | 350]]
	- pro daný case můžeme uvést více než jeden příkaz i bez bloku
	- pro daný case se vykonají všechny příkazy za ním uvedené až do nejbližšího slova break nebo do konce celého příkazu.
## Cyklus
- příkaz, který umožňuje vykonávat příkaz nebo blok opakovaně
### Cyklus s podmínkou na začátku
- while (<výraz-typu-boolean>) <příkaz-nebo-blok>
- Příklad: Máme proměnné n,sum typu int. Pomocí cyklu „while“ spočtěte součet čísel od 1 do n a vložte výsledek do proměnné sum.
```java
sum=0;
int i = 1;
while (i <= n) {
	sum = sum + i;
	i = i + 1;
}
```
### Cyklus s podmínkou na konci
- Cyklus s podmínkou na konci má v Javě tuto syntaxi:
	- do <příkaz-nebo-blok> while (<výraz-typu-boolean>)
- Příklad: Máme proměnné n,sum typu int. Pomocí cyklu „dowhile“ spočtěte součet čísel od 1 do n a vložte výsledek do proměnné sum. Předpokládá se, že vždy platí n>=1.
```java
sum=0;
int i = 1;
do {
	sum = sum + i;
	i = i + 1;
} while (i <= n);
```
## Cyklus for
- Cyklus for je cyklus s podmínkou na začátku s tuto syntaxí:
- for (<příkaz-1>, …, <příkaz-N>;
	- <výraz-typu-boolean>;
	- <příkaz-N+1>,…, <příkaz-N+M>) <příkaz-nebo-blok>
- Vyhodnocení cyklu for je ekvivalentní vyhodnocení bloku:
```java
{
	<příkaz-1>; … <příkaz-N>;
	while (<výraz-typu-boolean>) {
		{ <příkaz-nebo-blok> }
		<příkaz-N+1>; … <příkaz-N+M>;
	}
}
```
- Příklad: Máme proměnné n,sum typu int. Pomocí cyklu „for“ spočtěte součet čísel od 1 do n a vložte výsledek do proměnné sum.
```java
sum=0;
for (int i = 1; i <= n; i = i + 1)
	sum = sum + i;
```
## Vnořené cykly
- Příklad: Pro dané číslo 𝑛 vypočtěte hodnotu $s = \sum_{j = 1}^{n}{\sum_{i = 1}^{j}{i}}$
```java
s=0;
for (int j = 1; j <= n; j = j + 1)
	for (int i = 1; i <= j; i = i + 1)
		s = s + i;
```
## Návěští cyklu
- Každý z uvedených tří typů cyklů můžeme označit návěštím:
	- <jméno-návěští>: <příkaz cyklu>
- Příklad: Přiřaďte návěští cyklům z předchozího příkladu.
```java
s=0;
outer:
for (int j = 1; j <= n; j = j + 1)
	inner:
	for (int i = 1; i <= j; i = i + 1)
		s = s + i;

```
## Příkaz break
- Do těla cyklu (každého z uvedených typů) lze vložit příkaz
	- break <jméno-návěští-cyklu-nebo-nic>;
- Vykonáním příkazu break se ukončí vykonávání cyklu, k němuž se break vztahuje.
- Příklad: Sečtěte všechna čísla od 1 do n, ale nejvýše do čísla 42. Řešení:
```java
sum=0;
loop:
for (int i = 1; i <= n; i = i + 1) {
	if (i > 42)
		break loop;
	sum = sum + i;
}
```
- Příklad: Pro dané číslo 𝑛 vypočtěte hodnotu $sum = \sum_{j = 1}^{n}{\sum_{i = 1}^{j}{i}}$ Skončete s největší hodnotou 𝑗, pro kterou 𝑠𝑢𝑚 nepřesáhne 1000.
```java
sum=0;
outer:
for (int j = 1; j <= n; j = j + 1) {
	int s=0;
	for (int i = 1; i <= j; i = i + 1) {
		if (sum + s + i > 1000)
			break outer;
		s = s + i;
	}
	sum = sum + s;
}
```
## Příkaz continue
- Do těla cyklu (každého z uvedených typů) lze vložit příkaz
	- continue <jméno-návěští-cyklu-nebo-nic>;
- Vykonáním příkazu continue se ukončí vykonávání těla cyklu, k němuž se continue vztahuje. Cyklus samotný se neukončí.
- Příklad: Sečtěte všechna čísla od 1 do n. Vynechte číslo 42.
```java
sum=0;
loop:
for (int i = 1; i <= n; i = i + 1) {
	if (i == 42)
		continue loop;
	sum = sum + i;
}
```
# Pole
- Pole je posloupnost proměnných stejného typu.
	- Počet proměnných nelze měnit. Tomuto počtu říkáme délka pole.
	- Každá proměnná je jednoznačně určena svým pořadím, tzv. indexem
		- První hodnota v poli má index 0
		- Indexem může být pouze hodnota typu int.
- Pole je v Javě datovým typem.
- Hodnoty typu pole jsou vždy umístěny na haldě.
- Proměnná typu pole drží vždy svou hodnotu odkazem.
## Datový typ pole
- Pokud T je libovolný datový typ, tak zápisem
	- T\[]
- definujeme datový typ pole (proměnných) typu T.
	- Pokud T je typ int, pak int\[] je pole typu int.
	- Pokud T je typ třída A, pak A\[] je pole typu A.
	- Pokud T je typ float\[], pak float\[]\[] je pole typu float[].
## Vytváření proměnných a hodnot typu pole
- Pokud T je libovolný datový typ (klidně i pole), tak proměnnou typu T\[] definujeme zápisem:
	- T\[] <jméno-proměnné>
- Délka pole x typu T\[] je typu int a získáme ji výrazem: x.length
## Přístup do pole
- Nechť T je libovolný typ, 𝑖 hodnota typu int, x proměnná typu T\[]. Pak výraz
	- x\[𝑖]
- označuje 𝑖-tou proměnnou v poli x, pokud 0 ≤ 𝑖 < 𝑛, kde 𝑛 je počet proměnných v poli x.
## Příklady polí
- Podívejme se na příklady proměnných a hodnot typu pole.
```java
int[] a;
a = new int[2];
int[] b = new int[3];
b[1] = 42;
int[][] c = new int[2][3];
c[0] = new int[3];
c[1] = b;
c[0][2] = c[1][1];
```
- ![[Pasted image 20260225085935.png | 300]]
# Řetězec
- Řetězec přestavuje sekvenci znaků, tj. text.
- Řetězec v Javě je instance třídy
	- java.lang.String
	- java.lang se importuje automaticky
- Instance třídy String vytváříme operátorem new
	- new String(“<sekvence-znaků>”)
- nebo zkráceně
	- “<sekvence-znaků>”
- Příklad: String s = “Hello!”;
- Třída String obsahuje celou řadu metod. Zde zmíníme jen pár.
	- int length(): Vrátí počet znaků v řetězci.
	- boolean isEmpty(): Dotaz na prázdnost sekvence znaků
	- char charAt(int i): Vrátí i-tý znak v řetězci, počítáno od 0.

- String concat(String str): Vrátí nový řetězec, která má stejné znaky jaké jsou v this instanci a za nimi má znaky jaké jsou v instanci str.
	- Objekty this ani str nejsou změněny.
	- Místo volání můžeme concat můžeme použít operátor +, např.:
```java
String a = “abc”;
String b = “012”;
String c = b + a;
a = a + b;
```
- V c bude řetězec “012abc”. Stejný výsledek bychom dostali pomocí: String c = b.concat(a);
- Po vykonání příkazu instance “abc” přestane být dosažitelná. Proměnná a bude odkazovat na novou instanci “abc012”.

- Zda jsou řetězce v proměnných x a y stejné zjistíme voláním metody equals následovně: x.equals(y)
# Třídy a vztahy mezi nimi
## Přetížení metody
- Ve třídě můžeme mít více stejně pojmenovaných metod. Musí se ale vzájemně lišit počtem parametrů nebo typem aspoň jednoho parametru. Takovéto metody nazýváme přetížené.
## Konstruktory
- Konstruktor je metoda třídy, jejíž účelem je provést inicializaci vytvořené instance.
	- Musí se jmenovat stejně jako třída.
	- Konstruktor nikdy nic nevrací. Nemá proto ani návratový typ.
	- Můžeme mít více konstruktorů (jakožto přetížené metody).
	- Konstruktor bez parametrů je tzv. defaultní konstruktor.
```java
class Vector {
	float x; float y;
	Vector() { x=0.0f; y =0.0f; }
	Vector(float x, float y) { this.x=x; this.y=y; }
}
```
- V bloku konstruktoru lze zavolat jiný konstruktor syntaxí
	- this(<výraz-1>, …, <výraz-n>)
- kde n je počet parametrů volaného konstruktoru.
- Příklad: V předchozím příkladě by šlo konstruktor
	- Vector() { x=0.0f; y =0.0f; }
- definovat též zavoláním druhého konstruktoru
	- Vector() { this(0.0f, 0.0f); }
## Dědičnost
- Atributy třídy definují vlastnosti a metody chování instancí.
- Java umožňuje aby jedna třída zdědila vlastnosti a chování (tj. atributy a metody) jiné třídy.
	- Třída, ze které se dědí, se nazývá bázová, nadtřída nebo též rodič
	- Třída, která dědí, se nazývá odvozená, podtřída nebo též potomek.
- Mezi podtřídou a nadtřídou by měl platit „je“ vztah. Tedy, že
	- „každá instance podtřídy je (rozšířenou) instancí nadtřídy“
- Příklad: Uvažujme třídy Animal a Dog. Jelikož je pravda, že
	- „každý pes je zvířete“
- tak dává smysl, aby třída Dog dědila ze třídy Animal.
- Opačné tvrzení
	- „každé zvíře je pes“
- není pravdivé => třída Animal nebude dědit ze třídy Dog.

- Abychom pravdivost „je“ vztahu mohli správně určit, je nutné též znát Liskovové principu zastoupení (LSP; Liskov Substitution Principle), který k „je“ vztahu přidáme. Zní takto:
	- „Každou podmínku, kterou splňují instance nadtřídy, musí též splňovat všechny instance podtřídy.“
- Příklad: Uvažujme třídy Rectangle a Square. Rozhodněte, zda je dobré dědit třídu Square ze třídy Rectangle
- Řešení: Jelikož „každý čtverec je obdélník (se stejně dlouhými stranami)“, tak to vypadá, že zdědit třídu Square ze třídy Rectangle je v pořádku.

- Uvažujme ale tento postup:
	- Nastav šířku na 6.
	- Nastav výšku na 7.
	- Ověř, že plocha je 42.
- Tento postup splňují všechny instance třídy Rectangle. Ale nesplní jej žádná instance třídy Square (v bodech 1. a 2. musí proběhnout srovnání délek stran => plocha pak vyjde jiná než 42).
- LSP není splněn => Square by dědit z Rectangle ==neměl==

- Všimněte si, že třída Square nerozšiřuje třídu Rectangle. Naopak ji omezuje. Toto „omezování“ je často indikátorem k porušení LSP.
- V Javě definujeme třídu B jako podtřídu třídy A takto:
	- class B extends A { … }
- V B budou všechny atributy a metody třídy A.
- Ale ne všechny budou v B přístupné. Konkrétně, nepřístupné budou atributy a metody označené private (a package-private, pokud třídy leží v jiných balících).

- Příklad: Uvažujme tyto třídy
```java
class Animal { int age; void eat() {} }
class Dog extends Animal {}
```
- pak můžeme psát:
```java
Dog a = new Dog();
a.age=5;
a.eat();
```

- V souladu s LSP nám Java umožňuje definovat proměnnou typu nadtřídy pro instance podtřídy.
- Příklad: Navažme na předchozí příklad třídou Animal, ze které dědí třída Dog. Můžeme též psát:
```java
Animal a = new Dog();
a.age=5;
a.eat();
```
## Volání konstruktoru nadtřídy
- Pokud třída B dědí ze třídy A, pak v každém konstruktoru B musí být zavolán nějaký konstruktor A před prvním přístupem na jakýkoliv atribut nebo metodu v B (včetně zděděných).
	- Volání se provede pomočí klíčového slova ==super==.
	- Příklad:
```java
class A { A(int x) {} }
class B extends A { B(int x) { super(x); } }
```
- Pokud volání super(…) neuvede a v nadtřídě je defaultní nebo žádný konstruktor, pak překladač sám dodá příkaz super(); na začátek bloku konstruktoru.
## Hierarchie tříd
- Mezi třídami definujeme vztah dědičnosti. Tvoříme tak vlastně strom dědičnosti, který se nazývá hierarchie tříd.
- Každá třída v Javě vždy dědí (přímo nebo nepřímo) ze třídy
	- java.lang.Object
- Pokud tedy napíšeme class A { … }, tak pro Javu je to pouze zkratka za class A extends Object { … }.
## Přepsání metody v podtřídě
- Motivační příklad: Uvažujme tyto třídy:
```java
class Employee { void work() {} }
class Worker extends Employee {}
class Accountant extends Employee {}
```
- Jelikož práce dělníka a účetního se liší, tak implementace metody work by měla být jiná pro třídy Worker a Accountant.
- Chceme tedy přepsat metodu work v podtřídách.

- V Javě přepíšeme metodu v nadtřídě tak, že v podtřídě vytvoříme metodu se stejným:
	- jménem
	- seznamem parametrů
	- typem návratové hodnoty
- V podtřídě tedy bude metoda původní (z nadtřídy), tak její přepsaná verze. Která z nich se bude volat?
	- Bude se volat přepsaná metoda.
	- Pro volání původní metody, musíme použít klíčové slovo super.

```java
class A { int x=0; void f() { x = 1; } }
class B extends A { void f() { super.f(); x += 1; } }
class C extends B { void f() { super.f(); x += 2; } }
```
- Podívejme se na volání f v tomto kódu:
```java
A a=new C();
a.f();
```
1. Zavolá se metoda ve třídě C, protože jsme vytvořili instanci třídy C. Typ proměnné a na to nemá vliv.
2. Díky použití slova „super“ ve volání super.f() se zavolá metoda f v nadtřídě B.
3. Ze stejného důvodu dojde dále k zavolání metody f ve nadtřídě A třídy B. Tam se nastaví x na 1.
4. Vrátíme se do metody f ve třídě B a přičteme k x číslo 1. Tedy x bude 2
5. Vrátíme se do metody f ve třídě C a přičteme k x číslo 2. Tedy x bude 4.

## Anotace @Override
- Pokud před definici metody napíšeme anotaci
	- @Override
- tak se při překladu třídy zkontroluje, že metoda skutečně překrývá odpovídající metodu v nadtřídě.
	- Anotace není povinná.
	- Dokáže ale včas odhalit chybu. Je tedy velmi užitečná.
## Kompozice
- V objektovém návrhu se dále používá vztah „má“ mezi třídami:
	- „každá instance třída A má (obsahuje) instanci třídy B“
- Nejde o dědičnost ale o kompozici tříd.
- Typicky se kompozice vylučuje s dědičností.
- Příklad: Uvažujme třídy Animal a Heart. Jelikož platí, že:
	- „každé zvíře má srdce“
		- tak použijeme kompozici:
			- `class Animal { Heart heart; }`
			- Vidíme též, že dědičnost („je“ vztah) zde neplatí.