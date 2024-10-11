Než se vrhneme do čistě matematické a počítačové kryptografie, pojďme se podívat na šifry, které můžeme nazvat „Táborové šifry“. To, protože se s nimi nejčastěji setkáte na různých táborech a podobných akcích.

## [Morseova abeceda](https://haxagon.xyz/challenge/64087146f687a49eae4f7542#morseova-abeceda)

Hovorově „morseovka“, anglicky Morse code, je způsob komunikace, který se používal hlavně v telegrafii. Celá abeceda včetně čísel je tvořena pomocí teček (`.`) a čárek (`-`) neboli krátkého a dlouhého pípnutí.

Jednotlivá písmena jsou oddělována lomítkem (`/`), slova dvěma lomítky (`//`) a věty třemi lomítky (`///`).

Zde je tabulka písmen a jejich překladu v Morseově abecedě. Zapamatovat si jednotlivé znaky je ze začátku poměrně složité, proto existují pomůcky, jako například slova, která začínají písmenem, které překládají a zároveň jejich slabiky jsou buďto krátké nebo dlouhé podle toho, jestli reprezentují tečku nebo čárku.

```
A   .-      Akát
B   -...    Blýskavice
C   -.-.    Cílovníci
D   -..     Dálava
E   .       Erb
F   ..-.    Filipíny
G   --.     Grónská zem
H   ....    Hrachovina
CH  ----    Chléb nám dává
I   ..      Ibis
J   .---    Jasmín bílý
K   -.-     Krákorá
L   .-..    Lupíneček
M   --      Mává
N   -.      Nástup
O   ---     Ó náš pán
P   .--.    Papírníci
Q   --.-    Kvílí orkán
R   .-.     Rarášek
S   ...     Sasanka
T   -       Tón
U   ..-     Učený
V   ...-    Vyučený
W   .--     Wagón klád
X   -..-    Xénokratés
Y   -.--    Ýgar mává
Z   --..    Známá žena

0   -----
1   .----
2   ..---
3   ...--
4   ....-
5   .....
6   -....
7   --...
8   ---..
9   ----.
```

> U pomocných slov je mnoho variant. Toto je pouze jedna z možností.

Např. šifrování slova _ahoj_ je: `.-/..../---/.---//`

Napište na papír krátký vzkaz pro vašeho kamaráda nebo spolužáka sedícího vedle vás a pokuste se ho rozluštit.

### [Variace Morseovy abecedy](https://haxagon.xyz/challenge/64087146f687a49eae4f7542#variace-morseovy-abecedy)

V některý případech je šifrování pomocí standardní Morseovy abecedy příliš jednoduché a existuje několik způsobů jak šifru zkomplikovat. Například prohodit tečky a čárky, napsat každé písmeno pozpátku, celý text napsat pozpátku, zapsat morseovku jako čísla, kde prvočísla jsou tečky a ostatní čísla čárky apod. Morseovku můžete například zapsat i jako obrázek (větve na stromě, zuby na pile, trsy trávy...). Možností je opravdu mnoho a je pouze na vaší kreativitě, jak daleko morseovku dotáhnete.

## [Přeskakovačka](https://haxagon.xyz/challenge/64087146f687a49eae4f7542#p%C5%99eskakova%C4%8Dka)

Další klasickou táborovou šifrou je tzv. „přeskakovačka“. To znamená, že na začátku zprávy je definován počet znaků k přeskočení.

Může se jednat o číslo (1): 1B**S**F**K**X**O**W**C**Q**D**Z**O**A**P**H**O**S**L**X**E** (SKOCDOPOLE)

Nebo o písmeno (B --> 2): BAF**S**MZ**K**VR**O**ZA**C**OU**D**RI**O**TO**P**RO**O**ZA**L**IT**E**S (SKOCDOPOLE)

## [Hadovka](https://haxagon.xyz/challenge/64087146f687a49eae4f7542#hadovka)

Jak už název napovídá, tak se jedná o šifru, kde je text napsán ve směru nějakého „hada“.

Například ve směru:

```
>---  >---
^  ˇ  |  |
|  |  |  ˇ
O  >--^  X
```

Zašifrovaný text:

```
ODODMNNE
KJHIAENJ
AIANTBEE
LZZUOUTD
VDIKDDEE
```

Dešifrovaný text: `VLAKODJIZDIZAHODINUKDOTAMNEBUDETENNEJEDE`.

Variací na směr je mnoho, ale vždy by měl být nějak definován, například šipkou nad zašifrovanou zprávou.

## [Zonovka](https://haxagon.xyz/challenge/64087146f687a49eae4f7542#zonovka)

V této šifře je každé písmeno definováno jako obrázek udávající jeho pozici v šabloně.

Šablona:

```
     |     |   
A B C|D E F|G H I
_____|_____|_____
     |     |
J K L|M N O|P Q R
_____|_____|_____
     |     |   
S T U|V W X|Y Z 
     |     |

```

Zašifrovaný text `AHOJ`:

```
                   _____    _____
     |   |        |     |        |
*    |   |  *     |    *|   *    |
_____|   |_____   |_____|   _____|

```

Existuje i její variace a to s použítím například starého tlačítkového mobilu jako šablony:

![](https://upload.wikimedia.org/wikipedia/commons/7/73/Telephone-keypad2.svg)

Zašifrované písmeno `h`

```
‾‾‾‾‾|
  *  |
_____|
```