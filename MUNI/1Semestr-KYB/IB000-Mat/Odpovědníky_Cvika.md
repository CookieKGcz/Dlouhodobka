# 1
Vyplňte následující pravdivostní tabulky formulí výrokové logiky s výrokovými proměnnými _X,Y,Z..._ Logickou hodnotu pravda zatrhnete jako 1 (vpravo) a nepravdu jako 0. Odpověď musí být uvedená a správná v každém řádku tabulky, jinak nedostanete kladné body.
a)  V první tabulce vyplňte (zvlášť) vyhodnocení dvou jednoduchých formulí:

|     |     |     |                                                                                                                    |                                                                                                                    |
| --- | --- | --- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| _X_ | _Y_ | _Z_ | (Y \wedge \neg X)                                                                                                  | \neg (X \Rightarrow \neg Z)                                                                                        |
| 0   | 0   | 0   | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 |
| 1   | 0   | 0   | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 |
| 0   | 1   | 0   | 0 ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*1 | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 |
| 1   | 1   | 0   | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 |
| 0   | 0   | 1   | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 |
| 1   | 0   | 1   | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 | 0 ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*1 |
| 0   | 1   | 1   | 0 ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*1 | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 |
| 1   | 1   | 1   | ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*0 1 | 0 ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")*1 |

b)  V druhé tabulce pak vyplňte vyhodnocení formule složené z předchozích dvou:

|     |     |     |                                                              |
| --- | --- | --- | ------------------------------------------------------------ |
| _X_ | _Y_ | _Z_ | (Y \wedge \neg X)\,\Rightarrow\, \neg (X \Rightarrow \neg Z) |
| 0   | 0   | 0   | *1                                                           |
| 1   | 0   | 0   | *1                                                           |
| 0   | 1   | 0   | *0                                                           |
| 1   | 1   | 0   | *1                                                           |
| 0   | 0   | 1   | *1                                                           |
| 1   | 0   | 1   | *1                                                           |
| 0   | 1   | 1   | *0                                                           |
| 1   | 1   | 1   | *1                                                           |


Odpovězte následující otázky o formulích výrokové logiky s výrokovými proměnnými _X,Y,Z..._
a)  Je výroková formule $(\neg X \vee \neg Y) \,\wedge\, (Z \wedge Z)$ splnitelná (tj. někdy pravdivá)?   ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")\*ano   ne  
b)  Je výroková formule $(\neg X \Rightarrow \neg Y) \,\Rightarrow\, (Z \Rightarrow Z)$ tautologií (vždy pravdivá)?   ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")\*ano   ne  
c)  Jsou tyto dvě výrokové formule $(\neg X \wedge \neg X) \,\Rightarrow\, \neg (Y \vee Z)$  a  $(X \wedge X) \,\vee\, \neg (Y \vee Z)$ mezi sebou logicky ekvivalentní?   ![správně](https://is.muni.cz/pics/icons/checked_green.gif?fakulta=1433;obdobi=9783;studium=1408641 "správně")\*ano   ne


Odpovězte následující otázky o formulích výrokové logiky s výrokovými proměnnými X,Y,Z...
a)  Je výroková formule  $(X \vee X) \,\Rightarrow\, \neg (Y \Rightarrow Z)$ splnitelná (tj. někdy pravdivá)?   *ano   ne  
b)  Je výroková formule  $(X \vee Y) \,\wedge\, (Z \wedge Z)$ tautologií (vždy pravdivá)?   ano   \*ne  
c)  Jsou tyto dvě výrokové formule  $(\neg X \vee Y) \,\wedge\, (Z \Rightarrow Z)$  a   $(X \Rightarrow Y) \,\wedge\, (Z \Rightarrow Z)$ mezi sebou logicky ekvivalentní? \*ano


a)  O každé z následujících dvou výrokových formulí s výrokovými proměnnými X,Y,Z rozhodněte, zda ji lze ekvivalentně vyjádřit jen pomocí disjunkce a konjunkce bez negací:
   $\neg (Z \vee Y)$    ano   správně\*ne  
  $\neg (X \Rightarrow Z)$    ano   správně\*ne  

b)  Vyjádřete výrokovou formuli  $\neg (Z \vee Y)\,\vee\, (X \Rightarrow Z)$ ekvivalentní formulí používající pouze logické operace negace a implikace.
Ekvivalentní formuli s použitím pouze spojek implikace -> a negace ! napište sem:
(!Z -> Y) -> (X -> Z)




Vezměme si následující příklad matematické věty s několika předpoklady a jedním závěrem.
   Máme tři kuličky, červenou, zelenou a modrou, mohou být různých velikostí i materiálů. Platí-li zároveň
\*A;  modrá kulička je těžší než červená,
B;  zelená kulička je ze všech největší,
správně\*C;  červená kulička je ze všech nejlehčí,
správně\*D;  červená kulička je větší než modrá,
   pak platí také, že červená kulička má menší (průměrnou) hustotu než modrá.

Najděte a výše zatrhněte některou minimální podmnožinu z uvedených předpokladů {A,B,C,D} takovou, že z jejich konjunkce ještě vyplývá uvedený závěr; tj., že uvedená věta zůstává pravdivou s takto redukovanou podmnožinou předpokladů. ("Minimální" podmnožina předpokladů znamená, že věta je za těchto předpokladů pravdivá, ale odebráním libovolného z nich se stane nepravdivou. Minimální podmnožina nemusí být jednoznačná, do odpovědi se uvádí jedna taková.)

Doplňkově odpovězte (odpovídat zde nemusíte, ale pak nedosáhnete na plné body), zda je vaše zatržená minimální podmnožina předpokladů jedinou splňující zadání, nebo jich lze v tomto příkladě nalézt více:    ;  jediná   správně\*;  více minimálních možností


Vezměme si následující příklad matematické věty s několika předpoklady a jedním závěrem.
   Je-li KLMN čtyřúhelník a zároveň platí předpoklady
správně\*A;  strana KN má stejnou délku jako strana LM,
správně\*B;  u vrcholu K je pravý úhel,
správně\*C;  u vrcholu L je pravý úhel,
D;  strana KN má stejnou délku jako strana KL,
   pak platí také, že KLMN je obdélníkem nebo čtvercem.

Najděte a výše zatrhněte některou minimální podmnožinu z uvedených předpokladů {A,B,C,D} takovou, že z jejich konjunkce ještě vyplývá uvedený závěr; tj., že uvedená věta zůstává pravdivou s takto redukovanou podmnožinou předpokladů. ("Minimální" podmnožina předpokladů znamená, že věta je za těchto předpokladů pravdivá, ale odebráním libovolného z nich se stane nepravdivou. Minimální podmnožina nemusí být jednoznačná, do odpovědi se uvádí jedna taková.)

Doplňkově odpovězte (odpovídat zde nemusíte, ale pak nedosáhnete na plné body), zda je vaše zatržená minimální podmnožina předpokladů jedinou splňující zadání, nebo jich lze v tomto příkladě nalézt více:    správně*;  jediná   ;  více minimálních možností



Uvažme množinu všech kladných celých čísel jako univerzum $\mathcal U$. Rozhodněte, zda je formule $\exists k.(k=k^2)$ uzavřená.
správně\*Ano, je uzavřená.
Není uzavřená.

Je následující tvrzení pravdivé?
Uvažme nějaké (neprázdné) univerzum $\mathbf U$. Predikátová formule $\forall y:\,\phi$ se vyhodnotí jako pravdivá právě tehdy, když je formule $\phi$ vyhodnocena jako pravdivá pro nějakou volbu $y$ z univerza $\mathbf U$.
Ano, je pravdivé.
správně\*Není pravdivé.

Je následující tvrzení pravdivé?
Formule $\lnot(\forall x. (\phi \lor \psi))$ a $\exists x. (\phi \lor \psi)$ jsou ekvivalentní.
správně\*Není pravdivé.
Ano, je pravdivé.



# 2
a)  Vyplňte následující pravdivostní tabulku formule výrokové logiky s výrokovými proměnnými X,Y,Z. Logickou hodnotu pravda zatrhnete jako 1 (vpravo) a nepravdu jako 0. Odpověď musí být uvedená a správná v každém řádku tabulky.

X	Y	Z	$\neg  [\,(\neg X \Rightarrow Z) \,\Rightarrow\, X\,]$
0	0	0	správně\*0 1
1	0	0	\*0 1
0	1	0	správně\*0 1
1	1	0	\*0 špatně1
0	0	1	0 správně\*1
1	0	1	správně\*0 1
0	1	1	0 správně\*1
1	1	1	správně\*0 1
b)  Poté vyjádřete tutéž výrokovou formuli $\neg  [\,(\neg X \Rightarrow Z) \,\Rightarrow\, X\,]$ jí ekvivalentní formulí v normálním tvaru používající pouze logické operace negace, konjunkce a disjunkce.
Ekvivalentní formuli s použitím pouze spojek konjunkce &, disjunkce | a negace ! napište sem:
(X | Z) & !X



Uvažujme formule výrokové logiky, ve kterých X,Y,Z,T... jsou výrokové proměnné. Odpovězte následující tři otázky.

a)  Je formule  $$[\,(X\wedge \neg Y)\wedge (Z\Rightarrow \neg T)\,]$$ v normálním tvaru?    \*ano   špatněne  

b)  Formuli  $\neg [\,(\neg Y\vee Z)\wedge X\,]$ je za úkol převést do normálního tvaru. Výsledkem je tato (neúplná) ekvivalentní formule  $[\,(Y \,\odot\, \neg Z)\vee \neg X\,]$. Určete, která výroková spojka patří na místo $\odot :$    $\vee$   správně\*$\wedge$   $\Rightarrow$  

c)  Také formuli  $\neg [\,\neg (Y\Rightarrow \neg Z)\wedge \neg X\,]$ je za úkol převést do normálního tvaru. Proveďte takový převod a napište výsledek.
Ekvivalentní formuli v normálním tvaru pište sem (logické operátory zapište coby & |, implikaci -> a negaci ! ):
(Y -> !Z) | X



Uvažujme formule výrokové logiky, ve kterých X,Y,Z,T... jsou výrokové proměnné. Odpovězte následující tři otázky.

a)  Je formule  $[\,(X\vee Y)\wedge (\neg Z\wedge \neg T)\,]$ v normálním tvaru?    správně\*ano   ne  

b)  Formuli  $\neg [\,\neg (Y\Rightarrow Z)\wedge \neg X\,]$ je za úkol převést do normálního tvaru. Výsledkem je tato (neúplná) ekvivalentní formule  $[\,(Y \,\odot\, Z)\vee X\,]$. Určete, která výroková spojka patří na místo $\odot :$    $\vee$   $\wedge$   správně\* $\Rightarrow$ 

c)  Také formuli  $\neg [\,(Y\vee Z)\wedge X\,]$ je za úkol převést do normálního tvaru. Proveďte takový převod a napište výsledek.
Ekvivalentní formuli v normálním tvaru pište sem (logické operátory zapište coby & |, implikaci -> a negaci ! ):
(!Y & !Z) | !X



Rozhodněte, zdali jsou pravdivé následující tři uzavřené formule predikátové logiky nad univerzem \mathbb N všech přirozených čísel (včetně nuly):
  $\forall x\, \exists y\, ( -2x+y = 27 )$    správně\*pravdivá   nepravdivá 
  $\forall x\, \exists y\, ( 6x-3y = 21 )$    pravdivá   správně\*nepravdivá 
  $\forall x\, \exists y\, ( -4x+y = 14 )$    správně\*pravdivá   nepravdivá 




Vezměme si následující příklad matematické věty s několika předpoklady a jedním závěrem.
   Jsou-li x,y dvě reálná čísla a zároveň platí předpoklady
správně\*A;  x,y jsou přirozená čísla,
správně\*B;  x<0,
C;  y<2,
\*D;  x>x^2,
   pak platí také y^2<0.

Najděte a výše zatrhněte některou minimální podmnožinu z uvedených předpokladů {A,B,C,D} takovou, že z jejich konjunkce ještě vyplývá uvedený závěr; tj., že uvedená věta zůstává pravdivou s takto redukovanou podmnožinou předpokladů. ("Minimální" podmnožina předpokladů znamená, že věta je za těchto předpokladů pravdivá, ale odebráním libovolného z nich se stane nepravdivou. Minimální podmnožina nemusí být jednoznačná, do odpovědi se uvádí jedna taková.)
Všechny správné minimální podmnožiny předpokladů jsou BD, DA, BA. (Pozor, IS v tomto případě nezobrazuje dobře odpovědi u checkboxů!)

Doplňkově odpovězte (odpovídat zde nemusíte, ale pak nedosáhnete na plné body), zda je vaše zatržená minimální podmnožina předpokladů jedinou splňující zadání, nebo jich lze v tomto příkladě nalézt více:    ;  jediná   správně\*;  více minimálních možností



Mezi všemi studenty sedícími v jedné (neprázdné, ale jinak jakkoliv velké) posluchárně na přednášce IB000 jsou libovolně vybraní studenti označeni X,Y,Z. Upozorňujeme, že vybraní studenti nemusí být nutně různí (například může někdy nastat, že X a Y značí téhož studenta) a že řady a sloupce číslujeme od 1. Pak je pravdivá následující matematická věta:

  Jestliže pro takto libovolně zvolené studenty X,Y,Z platí zároveň předpoklady
A;  X sedí ve druhé řadě,
správně\*B;  Z sedí v první či druhé řadě,
správně\*C;  Y sedí jednu řadu před řadou Z (tj. není mezi nimi další řada), bez ohledu na sloupce,
D;  Z sedí v nejlevějším sloupci,
   pak platí také, že  X sedí ve stejném sloupci jako Y  nebo  Y sedí v první řadě.

Najděte a výše zatrhněte některou minimální podmnožinu z uvedených předpokladů {A,B,C,D} takovou, že z jejich konjunkce ještě vyplývá uvedený závěr; tj., že uvedená věta zůstává pravdivou s takto redukovanou podmnožinou předpokladů. ("Minimální" podmnožina předpokladů znamená, že věta je za těchto předpokladů pravdivá, ale odebráním libovolného z nich se stane nepravdivou. Minimální podmnožina nemusí být jednoznačná, do odpovědi se uvádí jedna taková.)

Doplňkově odpovězte (odpovídat zde nemusíte, ale pak nedosáhnete na plné body), zda je vaše zatržená minimální podmnožina předpokladů jedinou splňující zadání, nebo jich lze v tomto příkladě nalézt více:    správně*;  jediná   ;  více minimálních možností