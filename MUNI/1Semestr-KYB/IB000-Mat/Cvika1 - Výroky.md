Když se výrok stahuje sám na sebe, tak většinou ani není výrok.
Musí být konkrétní. (auto je červené. není výrok)

Znegování:
Dnes je pátek nebo zítra bude středa. -> Není pátek a zítra nebude středa.
Dívka, se kterou chodím, má modré oči a je zrzka. -> Nemá modré oči nebo není zrzka.
Pokud má objekt tři strany, pak je to čtverec. -> Existuje objekt který má 3 strany a není čtverec.
Alespoň dva jogurty v mojí ledničce jsou prošlé. -> Nanejvýše jeden .. je prošlý.
Ve třídě je právě polovina dívek. -> méně nebo více než polovina
Je překvapivé, že dva studenti dostali ze zkoušky stejný počet bodů. -> 
Pro každé přirozené číslo x existuje přirozené číslo y takové, že x^2 < y.
 -> 


| A   | B   | neg(A disj B) | negA konj negB | negB disj A | negA disj B |
| --- | --- | ------------- | -------------- | ----------- | ----------- |
| 0   | 0   | 1             | 1              | 1           | 1           |
| 0   | 1   | 0             | 0              | 0           | 1           |
| 1   | 0   | 0             | 0              | 1           | 0           |
| 1   | 1   | 0             | 0              | 1           | 1           |

neg(A disj B)   ≡   negA konj negB
neg(A konj B)   ≡   negA disj negB

<=> je podobné ≡ (pozor na to, až později)

toutologie = pravdivá
kontradikce = nepravdivá

**negA disj B   ≡   A => B   ≡   negB implikuje negA**

### Implikace:
"Jestliže jsem se praštil kladivem do palce, pak mně palec bolí"

Jestliže jsem se praštil kladivem do palce = tvrzení A
pak mně palec bolí = tvrzení B
A implikuje B


### Vyjádřete kontrapozici tvrzení:
"Dobré jídlo není levné"
jiný zp zápisu-> Jestliže je jídlo dobré, pak není levné.

negB => negA
Jestliže je jídlo levné, pak není dobré.
nebo -> Levné jídlo není dobré.

### Rozhodněte o pravdivosti následujících tvrzení:
a) Pokud je n zároveň liché a sudé, pak n = 42.  (je, protože neplatí předpoklad)
Pokud je Fi prestižnější než MIT, pak Harvard je v Praze. (pravdivé)
Jestliže je dnes středa, pak je dnes úterý. (nepravdivé ve středu, pravdivé jiný den)


### Anna a Bětka
Následující dvě tvrzení:
- Miluju Annu nebo Bětku.
- Pokud miluju Bětku, tak miluju Annu.

Vyplývá z toho, že některé z děvčat určitě miluji/nemiluji?

| A   | B   | A disj B | B => A |
| --- | --- | -------- | ------ |
| 0   | 0   | 0        | 1      |
| 0   | 1   | 1        | 0      |
| 1   | 0   | **1**    | **1**  |
| 1   | 1   | **1**    | **1**  |

takže s Annou neudělá chybu


### Alice, Bob a Carol
Mějme tři studenty - Alici, Boba a Carol, kteří psali test z IB000. Platí-li zároveň:
- Alice získala méně bodů než Carol,
- Bob získal více bodů než Alice,
- Alice je nejchytřejší, a
- Alice získala více bodů než Bob
pak také platí, že Carol získala více bodů jak Bob.

Najděte všechny minimální podmnožiny předpokladů 1-4 takové, že věta stále ještě platí.

1- a) a d) platí a plyne z ní závěr

2- b) a d) nepravdivý předpoklad

### Další podobné
Jsou li x, y dvě reálná čísla a zároveň platí předpoklady
- x,y jsou kladná číslam
- y<0
- x>1
- x>y
pak pltí také x^2 - y > 0

1- b (x na druhou bude vždy větší nebo rovno nule)
2- c) a d)

### Sestrojte formuli fí, pro tabulku

| A   | B   | C   | fí  |
| --- | --- | --- | --- |
|     |     |     | 0   |
|     |     |     | 0   |
|     |     |     | 0   |
|     |     |     | 1   |
|     |     |     | 0   |
|     |     |     | 0   |
|     |     |     | 1   |
|     |     |     | 0   |
