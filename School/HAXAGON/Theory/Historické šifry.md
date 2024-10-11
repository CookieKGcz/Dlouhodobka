#### [Matematický způsob](https://haxagon.xyz/challenge/6408712c61f808d728839195#matematick%C3%BD-zp%C5%AFsob) [[Vigenere cipher]]

Pokud máte raději vzorce než hledání písmenek v tabulce, tento způsob pro vás bude příjemnější.

Každé písmeno si převeďte na číslo udávající jeho pozici v abecedě počínaje nulou `ABCDEFGHIJKLMNOPQRSTUVWXYZ`. Například A = 0, Z = 25. Vigenèrova šifra používá pro šifrování a dešifrování stejný klíč, kde každé písmeno klíče udává posun jednoho písmena původního textu.

##### [Zašifrování zprávy](https://haxagon.xyz/challenge/6408712c61f808d728839195#za%C5%A1ifrov%C3%A1n%C3%AD-zpr%C3%A1vy-1)

- Původní text: `hello`
- Klíč: `key`

Nejprve převeďte zprávu a klíč na čísla

- Původní text: `7 4 11 11 14`
- Klíč: `10 4 24`

Každé číslo původního textu sečtěte s číslem klíče ve stejné pozici a na výsledek aplikujte modulo 26. Pokud je klíč kratší než původní zpráva, klíč opakujte.

```
(7+10)  % 26 = 17
(4+4)   % 26 = 8
(11+24) % 26 = 9
(11+10) % 26 = 21
(14+4)  % 26 = 18
```

Po převedení čísel opět na písmena získáte zašifrovaný text `rijvs`.
##### [Dešifrování zprávy](https://haxagon.xyz/challenge/6408712c61f808d728839195#de%C5%A1ifrov%C3%A1n%C3%AD-zpr%C3%A1vy-1)

Pro dešifrování zvolte podobný postup, akorát klíč od zašifrovaného textu odečtěte.

```
(17-10) % 26 = 7
(8-4)   % 26 = 4
(9-24)  % 26 = 11
(21-10) % 26 = 11
(18-4)  % 26 = 14
```

Jak můžete vidět, hodnoty po dešifrování jsou stejné jako hodnoty před zašifrováním. Po převedení čísel do textu vznikne původní slovo `hello`.

> Pokud potřebujete prolomit šifru, ale neznáte její klíč můžete použít buďto [dCode](https://www.dcode.fr/vigenere-cipher) nebo [Guballa](https://www.guballa.de/vigenere-solver) Je však potřeba dostatečně dlouhý vstupní zašifrovaný text.

### [One-time pad](https://haxagon.xyz/challenge/6408712c61f808d728839195#one-time-pad) [[One-time pad]]

Šifra přezdívaná one-time pad, česky Vernamova šifra, používala stejného principu jako Vigenèrova šifra, ale musela splnit následující podmínky:

- Klíč musí být vždy alespoň tak dlouhý, jako zpráva.
- Klíč musí být kompletně náhodný. Žádné pseudo náhodné generátory čísel, ale čistě hardwarová náhodnost.
- Klíč může být použit maximálně jednou. Z toho plyne jméno „one-time pad“.
- Klíč musí být udržován v tajnosti.

Pokud dodržíte tyto podmínky, tak je šifra v principu neprolomitelná.

> Klíče byly při válce distribuovány jako tabulky na papíře, ale občas byla pro tisk používaná i silně hořlavá nitrocelulóza. Po použití byl klíč spálen.

### [Scytale](https://haxagon.xyz/challenge/6408712c61f808d728839195#scytale)

Jedná se o úplně nejstarší šifru zaznamenanou v lidské historii. Datuje až do roku 700 před naším letopočtem, kdy byla používaná pro válečnou komunikaci v Řecku.

Jde o transpoziční šifru, kde byl pásek papyru či pergamenu namotán na válec o předem dohodnutém rozměru a ve směru hlavní osy válce na něj byl psán text.

Následující obrázek demonstruje, jak vypadá pásek s textem namotán na válci:

```
       |   |   |   |   |   |   |
       | P | O | M | O | Z |   |
     __| M | I | J | S | E |__ | 
    |  | M | P | O | D | P |
    |  | A | L | B | O | U |
    |  |   |   |   |   |   |
```

Po rozmotání je text na pásku nečitelný: `PMMAOIPLMJOBOSDOZEPU`.

Zjednodušeně by se ale tato šifra dala popsat jako vybírání x-tého písmena. Průměr válce udává kolik písmen překročíte. Například v tomto případě se přeskakují vždy 3 písmena. Pokaždé co dojdete na konec pásku, začnete o jedno písmenu dál:

**P**MMA**O**IPL**M**JOB**O**SDO**Z**EPU (POMOZ)

P**M**MAO**I**PLM**J**OBO**S**DOZ**E**PU (MIJSE)

PM**M**AOI**P**LMJ**O**BOS**D**OZE**P**U (MPODP)

PMM**A**OIP**L**MJO**B**OSD**O**ZEP**U** (ALBOU)

### [Substituce vs transpozice](https://haxagon.xyz/challenge/6408712c61f808d728839195#substituce-vs-transpozice)

Asi jste si všimli, že se v textu často objevují termíny substituce nebo transpozice. Některé šifry jsou substituční, některé transpoziční a některé dokonce obojí najednou. Tak si v tom pojďme udělat pořádek.

#### [Substituce](https://haxagon.xyz/challenge/6408712c61f808d728839195#substituce)

Substituční šifrou se rozumí šifra, která nahrazuje (substituuje) písmena za jiná písmena, ale nemění přitom jejich pořadí. Takže například Caesarova šifra je ukázková substituční šifra.

#### [Transpozice](https://haxagon.xyz/challenge/6408712c61f808d728839195#transpozice)

Na druhou stranu transpoziční šifra je šifra, která přehazuje pořadí písmen (zasazuje je do jiné pozice). Zde je možností mnoho, ale když např. Scytale je ukázková transpoziční šifra.

### [Online nástroje](https://haxagon.xyz/challenge/6408712c61f808d728839195#online-n%C3%A1stroje)

U delších textů nebo úloh, kde jsou šifry komplikovanější, vám přijdou vhod online nástroje. Jak budete v kryptografii postupovat dále, uvidíte, jak užitečné doopravdy jsou. Pro začátek si ale řekněme o těch dvou nejznámějších, [dCode](https://www.dcode.fr/en) a [CyberChef](https://gchq.github.io/CyberChef).

#### [dCode](https://haxagon.xyz/challenge/6408712c61f808d728839195#dcode)

Umí pracovat s mnoha šiframi i včetně těch méně známých. Jeho hlavní výhodou je, že u velké části šifer umí hrubou silou prolomit klíč. Například u Caesarovi šifry je maximálně 26 možností zašifrování, takže když se podíváte na všech 26 výsledků, uvidíte, co je text a co je pouze změť písmen. Toto ale umí i sám dCode. Porovnává výsledky se slovy ze slovníku, takže díky tomu umí prolomit i kratší klíče u Vigenèrovy šifry a mnoha dalších.

Když otevřete stránku [dCode](https://www.dcode.fr/en), v levém horním rohu uvidíte search bar. Ten slouží pro vyhledávání šifer. Zkuste si vyhledat například slovo Vigenere.

Bohužel jeho hlavní limitací je, že dokáže pracovat pouze s jednou šifrou najednou. Nejde v něm řetězit výstupy do vstupů a jeho rozhraní půdobí spíše zastarale.

#### [CyberChef](https://haxagon.xyz/challenge/6408712c61f808d728839195#cyberchef)

Na druhou stanu CyberChef vám vždy uvaří co potřebujete. Hlavně si určitě oblíbíte jeho modul `Magic`, který se pokusí automaticky prolomit zašifrovaný text.

Otevřte si stránku [CyberChef](https://gchq.github.io/CyberChef). V levém horním rohu můžete vyhledávat různé moduly a šifry, dvojklikem modul přidáte. Tím se přidá doprostřed okna a pro jeho odstranění na něj opět jednodušše dvakrát kliknete. Do okna input napíšete váš vstup a po provedení operací, které specifikujete, se vypíše výstup v okně output.

> V nástroji CyberChef se Caesarova šifra jmenuje ROT13.