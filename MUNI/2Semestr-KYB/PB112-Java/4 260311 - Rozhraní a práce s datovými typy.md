# Rozhraní
- speciální datový typ, který definuje ***dohodu*** o poskytování určité funkcionality.
- Říká které metody bude přesně poskytnuta
- Neříkají jak přesně mají být ty metody implementovány

- metody jsou pak implementovány ve třídách
- instance těchto tříd pak poskytují onu funkcionalitu
## Definování rozhraní
- pomocí slova interface
```java
<modifikátor-viditelnosti> <jmén-rozhraní> {
	<deklarace-metody-rozhraní-1>;
	…
	<deklarace-metody-rozhraní-N>;
}
```
- metody jsou implicitně public

- Příklad
	- Na trhu je několik výrobců aut, které lze řídit pomocí programu.
	- Naše firma vytváří program pro automatické řízení aut.
	- Chtěli bychom být schopni řídit ***všechny typy aut od všech výrobců***
		- Pokud by se každé auto řídilo úplně jinak, musel by náš program mít kód specifický pro každé auto.
	- Lepší bude uzavřít s výrobci dohodu o jednotném ovládání aut.
	- Tuto dohodu zapíšeme v Javě právě jako rozhraní.

```java
public interface CarControl {
	void turnWheels(float angleChange);
	void accelerate(float signedMagnitude);
	float getWheelsAngle();
	float getSpeed();
}
```
- Zde nejsou implementace. Neříkáme, jak metody fungují.
## Implementace rozhraní
- Aby třída implementovala rozhraní, tak ***musí obsahovat definice všech metod*** uvedených v implementovaném rozhraní.

```java
<modifikátor> class <jméno-třídy> implements
	<jnéno-rozhraní-1>, …, <jméno-rozhraní-N>
{
	<definice-metod-všech-rozhraní>
	<vše-ostatní-co-můžeme-ve-třídě-definovat>
}
```

- Příklad: Pokračujme v předchozím příkladu
	- Škoda vyrábí auta: Favorit a Felicia
	- Tarta vyrábí auta: Phoenix a Force.
	- S oběma firmami máme dohodu o implementaci rozhraní všemi uvedenými auty. Škoda může definovat software Favorita takto:
```java
public class Favorit implements CarControl {
	public void turnWheels(float angleChange) { … }
	public void accelerate(float signedMagnitude) { … }
	public float getWheelsAngle() { … }
	public float getSpeed() { … }
}
```
## Použití rozhraní
- Rozhraní používáme tak, že
	- Definujeme proměnné a atributy, jejichž typem je Rozhraní.
- Zásadní je, že ***hodnoty*** v proměnných typu rozhraní jsou ***instance tříd***, které implementují ta rozhraní. 
- Proměnné typu rozhraní drží svou hodnotu vždy odkazem.

- Příklad: Pokračujme v příkladu s rozhraním CarControl.
	- Můžeme si definovat metodu pro řízení přijatého auta.
```java
void drive(CarControl car) {
	while (!destinationReached()) {
		if (isCarAhead()) {
			car.accelerate(-1);
			car.turnWheels(5); // change lane
		} else if (car.getSpeed() < MAX_SPEED_IN_CITY)
			car.accelerate(1);
	}
}
```
- Přes proměnnou typu rozhraní lze volat pouze metody rozhraní implementované v odkazované instanci.
- Příklad: Uvažujme definice:
```java
interface I { void f(); }
class A implements I { pubic void f() {} void g() {} }
```
- Použití:
```java
I x = new A();
x.f(); // OK. Volat metodu rozhraní můžeme.
x.g(); // CHYBA! K ničemu dalšímu přístup nemáme.
```
- Když ve třídě implementujeme metody rozhraní, tak můžeme použít anotaci @Override.

- Příklad: Třída A z předchozího příkladu by mohla definovat anotaci takto:
```java
anotaci takto:
	interface I { void f(); }
	class A implements I {
		@Override public void f() {}
		void g() {}
	}
```
- Pokud bychom ve třídě nějakou metodu rozhraní nedefinovali správně, tak Java zahlásí chybu i bez této anotace.

## Vlastnosti rozhraní
- Nelze vytvářet instance.
- Nelze definovat těla metod rozhraní (bloky příkazů).
- Nelze definovat klasické atributy (ani privátní).
- Lze definovat statické metody.
	- Nejsou součástí rozhraní (třídy je nemusí přepisovat)
- Lze definovat klasické privátní metody (s modifikátorem private).
	- Nejsou ale součástí rozhraní (třídy je pak neimplementují).
- Lze uvést „defaultní“ implementaci některým metodám rozhraní.
	- Před návratový typ musíme uvést klíčové slovo default.
- Rozhraní může rozšířit libovolný počet jiných rozhraní.

## Defaultní metody rozhraní
- Důvodem pro zavedení defaultních metod do rozhraní je:
	- Umožnit přidávat do rozhraní postupně další metody.
	- Nezpůsobit přitom chyby v překladu tříd, které nové metody rozhraní ještě neimplementují.
- Příklad (motivační): Uvažme rozhraní
```java
public interface CarDiagnostic { float getFuelAmount(); }
```
- Toto rozhraní může implementovat celá řada tříd, např.
```java
public class Favorit implements CarDiagnostic
{ public float getFuelAmount() { … } }
```
- Nyní můžeme chtít do rozhraní přidat další metodu:
```java
public interface CarDiagnostic {
float getFuelAmount();
boolean hasFuel();
}
```
- Tím jste ale způsobili, že se nepřeloží žádná ze tříd (např. Favorit), které rozhraní implementovaly.

- Pokud ale definujeme přidanou metodu jako defaultní:
```java
interface CarDiagnostic {
	float getFuelAmount();
	default boolean hasFuel()
	{ return getFuelAmount()>0.0f; }
}
```
- tak se přeloží všechny třídy, které rozhraní implementovaly.

## Rozšiřování rozhraní
- Příklad: Pokračujme v našem příkladu s auty. Řekněme, že některá auta podporují automatické tankování v čerpací stanici. Pro ně můžeme definovat rozhraní:
```java
public interface FullCarControl extends CarControl {
	void openFuelPort();
	void closeFuelPort();
	float getRequiredFuelAmount();
	void addFuel(float liters);
}
```
- Pokud např. třída Favorit podporuje toto tankování, tak pro ni změníme definici:
```java
public class Favorit implements FullCarControl {
	// Všechny metody z rozhraní CarControl.
	public void turnWheels(float angleChange) { … }
	public void accelerate(float signedMagnitude) { … }
	public float getWheelsAngle() { … }
	public float getSpeed() { … }
	
	// Všechny nové metody z rozhraní FullCarControl.
	public void openFuelPort() { … }
	public void closeFuelPort() { … }
	public float getRequiredFuelAmount() { … }
	public void addFuel(float liters) { … }
}
```

- V naší firmě můžeme dodat ovládání aut v čerpací stanici:
```java
void drive(CarControl car) { … }
void refuel(FullCarControl car) { … }
```

- Pokud chceme rozšířit více rozhraní najednou, tak to zapíšeme:
```java
<modifikátor> interface <jméno-rozhraní> extends
	<jméno-rozhraní-1>,…, < jméno-rozhraní-N>
{ … }
```

- Příklad: Rozhraní FullCarControl by mohlo rosšiřovat, kromě rozhraní CarControl, též rozhraní CarDiagnostic:
```java
public interface FullCarControl extends
	CarControl, CarDiagnostic
{
	void openFuelPort();
	void closeFuelPort();
	float getRequiredFuelAmount();
	void addFuel(float liters);
}
```

## Implementace více rozhraní
- Již víme, že třída může implementovat více rozhraní.
- Příklad: Pro řízení auta v čerpací stanici můžeme vytvořit separátní rozhraní:
```java
public interface RefuelableCar {
	void openFuelPort();
	void closeFuelPort();
	float getRequiredFuelAmount();
	void addFuel(float liters);
}
```

- Výrobci aut pak mohou definovat odpovídající třídy tak, že budou implementovat ta rozhraní, která podporují. Např.:
```java
public class Favorit implements
	CarControl, RefuelableCar, CarDiagnostic { … }
public class Felicia implements
	CarControl { … }
public class Phoenix implements
	CarControl, CarDiagnostic { … }
… 
```

- Uvedený návrh rozhraní se též promítne do implementace řízení aut v naší firmě:
```java
void drive(CarControl car) { … }
// Zde do refuel posíláme pouze „tankovatelná“auta.
void refuel(RefuelableCar car) { … }
void check(CarDiagnostic car) { … }
```

- Máme tedy metody, které lze použít na všechny instance (auta), které podporují dané rozhraní. Je to přehlednější nežli:
```java
void drive(CarControl car) { … }
// Ale zde jí posíláme auta „plně řiditená“
void refuel(FullCarControl car) { … }
```

## Kdy rozšířovat rozhraní
- Postupujeme stejně jako při posuzování dědičnosti mezi třídami, tj., použijeme „je“ vztah včetně LSP
- Příklad: Pro řízení aut jsme zavedli rozhraní
	- CarControl, RefuelableCar a CarDiagnostic
- Pojďme se podívat na (ne)platnost „je“ vztahu mezi nimi.
	- „Tankování není řízení na silnici“ (nic do řízení nepřidává) => Rozhraní RefuelableCar by nemělo rozšiřovat CarControl.
	- „Řízení na silnici není tankování“ (nic do tankování nepřidává) => Rozhraní by CarControl nemělo rozšiřovat RefuelableCar.
	- Podobným způsobem bychom zjistili, že ani diagnostika auta nic nepřidává do řízení ani tankování. A též opačně.
# Práce s datovými typy
## Boxing a unboxing
- Pro každý primitivní datový typ máme v Javě odpovídající třídu:

| byte | short | int     | long | float | double | char      | boolean |
| ---- | ----- | ------- | ---- | ----- | ------ | --------- | ------- |
| Byte | Short | Integer | Long | Float | Double | Character | Boolean |
- ***Boxing je převod*** hodnoty primitivního datového typu na instanci odpovídající třídy.
	- Všechny tyto třídy obsahují statickou metodu valueOf, která přijímá hodnotu primitivního typu a vrací instanci odpovídající třídy.

- Příklad (boxing)
```java
Integer i = Integer.valueOf(5);
int x = 42; Integer i = Integer.valueOf(x);
Character c = Character.valueOf(‘A’);
Boolean b = Boolean.valueOf(true);
```
- Unboxing je opačný převod, tj. získáme hodnotu primitivního datového typu z instance odpovídající třídy.
```java
int i = x.intValue(); // kde x je typu Integer
short s = x.shortValue(); // kde x je typu Short
Float f = x.floatValue(); // kde x je typu Float
boolean b = x.booleanValue(); // kde x je typu Boolean
```

- Integer a = 10; Java to interpretuje jako: `Integer a = Integer.valueOf(10);`
- Integer c = a + b;
	- Java interpretuje jako:
		- `Integer c = Integer.valueOf(a.intValue() + b.intValue());`

## Třída java.lang.Class
- Instance třídy java.lang.Class nesou informace o třídách v běžící Java aplikaci.
	- Instance obsahují tzv. metadata o třídách a rozhraních
	- Pro každou třídu máme v aplikaci jedinou instanci třídy Class. Jde tedy o singletony.
	- Instanci třídy Class můžeme získat ze třídy klíčovým slovem class a z instance třídy pak voláním metody getClass()

- Příklad: Uvažujme třídu class A {}. Pak výraz
	- `A.class`
- nám dá instanci třídy Class obsahující informace o třídě A. Např. obsahuje jméno třídy (String):
	- `A.class.getName()`
- Uvažujme dále instanci třídy A v proměnné
	- `A x = new A();`
- instanci třídy Class obsahující informace o třídě A získáme voláním:
	- `x.getClass()`
- Přitom platí:
	- `A.class == x.getClass()`
- jde o stejnou instanci třídy Class.

- Ale pozor, voláním
	- `A.class.getClass()`
- získáme instanci třídy Class popisující třídu Class, nikoliv třídu A.
## Operator instanceof
- Často potřebujeme vědět, zda je možné s daným objektem pracovat jako s instancí určité třídy.
- K tomu můžeme použít operátor instanceof takto:
	- `<objekt> instanceof <třída>`
- Výsledkem je hodnota typu boolean. Konkrétně se vyhodnotí na true, pokud \<objekt> je typu \<třída\> nebo jeho typ z \<třída> dědí (přímo nebo nepřímo).
- Výrazy s tímto operátorem proto často tvoří podmínku příkazu „if“.

- Příklad: Uvažujme tyto třídy a proměnnou
```java
class Animal {}
class Dog extends Animal { void bark() {} }
class Boxer extends Dog {}

Object a = new Boxer();
```
- Všechny následující výrazy se vyhodnotí na true:
```java
a instanceof Animal
a instanceof Dog
a instanceof Boxer
a.getClass() != Animal.class
a.getClass() != Dog.class
a.getClass() == Boxer.class
```

