# Přehled základních důkazových technik
- **Přímé odvození.** To je způsob, o kterém jsme se dosud bavili.

- **Kontrapozice** (také **obměnou** - „obrácením", či **nepřímý důkaz**).
	- Místo věty „Jestliže platí *předpoklady*, pak platí *závěr*." (A => B)
	- budeme dokazovat ekvivalentní větu
		- „Jestliže neplatí *závěr*, pak neplatí alespoň jeden z *předpokladů*."
			- negB => negA

- **Důkaz sporem.** Místo věty
	- „Jestliže platí *předpoklady*, pak platí *závěr*."
	- budeme dokazovat větu
		- „Jestliže platí *předpoklady* a platí *opak závěru*, pak platí.. . "
		- - nějaké zjevně nepravdivé tvrzení, nebo případně
		- - závěr (tj. opak jeho opaku) či opak jednoho z předpokladů.

- **Matematická indukce**. Pokročilá technika.
## Příklad důkazu kontrapozicí
### Definice
- Prvočíslo je celé číslo p > 1, které nemá jiné dělitele než 1 a p.
### Příklad 4.1
- Na důkaz kontrapozicí (obměnou)
	- Věta. Jestliže p je prvočíslo větší než 2, pak p je liché.
### Důkaz
- obměněného tvrzení:
- Místo uvedeného znění věty budeme dokazovat, že
	- je-li p sudé, pak p není větší než 2 nebo p není prvočíslo.
- Připomínáme, že podle definice je p sudé, právě když lze psát p = 2 • k, kde k je celé. Jsou jen dvě snadno řešitelné možnosti:
	- k <= 1. Pak p = 2 • k není větší než 2
	- k > 1. Pak p = 2 • k není prvočíslo podle definice.
## Příklady důkazu sporem
### Příklad 4.2
- Jiný, kratší přístup k Důkazu 4.1
- Věta. Jestliže p je prvočíslo větší než 2, pak p je liché.
### Důkaz sporem
- Nechť tedy p je prvočíslo větší než 2, které je sudé. Pak p = 2-k pro nějaké k > 1, tedy p není prvočíslo, ***spor*** (s předpokladem, že p je prvočíslo).
### Příklad 4.3
- Věta. Číslo sqr(2) není racionální.
### Důkaz sporem
- Nechť sqr(2) je racionální, tj. nechť existují celá kladná čísla r, s taková, že sqr(2) = r/s. Můžeme navíc předp., že r je nejmenší možné takové.
	- Pak 2 = r^2 / s^2, tedy r^2 = 2 . s^2, proto r^2 je dělitelné dvěma. Z toho plyne, že i r je dělitelné dvěma (proč?).
	- Jelikož r je dělitelné dvěma, je r^2 dělitelné čtyřmi, tedy r^2 = 4 . m pro celé nějaké celé m.
	- Pak ale také 4 . m = 2 . s^2, tedy 2 . m = s^2 a proto s^2 je dělitelné dvěma.
	- Z toho plyne, že s je také dělitelné dvěma. Celkem dostáváme, že r' = r/2 i s' = s/2 jsou celá, platí sqr(2) = r/s = r'/s' a přitom r' < r, což je ***spor***.
# Věty typu "právě tehdy (když)"
- Uvažujme nyní (v matematice poměrně hojné) věty tvaru
	- „Nechť platí předpoklady P. Pak tvrzení A platí právě tehdy, platí-li tvrzení B."
- Příklady jiných jazykových formulací téže věty jsou:
	- Nechť platí předpoklady P. Pak tvrzení A platí tehdy a jen tehdy, když platí tvrzení B.
	- Za předpokladů P je tvrzení B nutnou a postačující podmínkou pro platnost tvrzení A. (nutnou ==   A impl >= B) (postačující ==   B >= A)
	- Za předpokladů P je tvrzení A nutnou a postačující podmínkou pro platnost tvrzení B.
- Plný důkaz vět tohoto tvaru má vždy dvě části(!). Je třeba dokázat:
	- Jestliže platí předpoklady P a tvrzení A, pak platí tvrzení B.
	- Jestliže platí předpoklady P a tvrzení B, pak platí tvrzení A.
### Příklad 4.4
- Na důkaz typu "právě tehdy (když)"
- Věta. Pro dvě množiny A,B platí, že 2^A = 2^B právě tehdy když A^2 = B^2.
### Důkaz
- Nezapomínáme, že našim úkolem je dokázat oba směry tvrzení (implikace zleva doprava a zprava doleva). Přitom obě implikace budeme dokazovat obměnou, symbolicky jako **2A ^ 2B <^=> A2 ^ B2**.
- Začneme s prvním směrem: Je-li 2A ^ 2B, pak existuje množina X taková, že X ⊆ A a X !⊆ B (nebo naopak - což se řeší symetricky).
	- X ⊆ B přitom podle definice znamená, že pro nějaké y ∈ X platí y !∈ B. Zároveň však y ∈ A. Proto (y, y) ∈ A^2, ale {y, y) !∈ B^2, neboli A^2 != B^2.
- V opačném směru postupujeme z předpokladu A^2 != B^2. Zase z toho odvodíme, že existuje uspořádaná dvojice taková, že (x, y) ∈ A^2, ale (x, y) !∈ B^2.
	- Z posledního vyplývá, ze x !∈ B nebo y !∈ B. Opět bez újmy na obecnosti můžeme vzít jen případ x !∈ B. Avšak z (x, y) ∈ A^2 vidíme, že x ∈ A.
	- Proto {x} ∈ 2^A, ale {x} !∈ 2^B, neboli 2^A !∈ 2^B.
# Matematická indukce
- Jde o důkazovou techniku aplikovatelnou na tvrzení tohoto typu:
	- "Pro každé přirozené (celé) m >= k0 platí T(n)"
- Zde k0 je nějaké pevné přir. číslo a T(n) je tvrzení parametrizované číslo n.
- Příkladem je třeba tvrzení:
	- Pro každé n >= 0 platí, že n přímek dělí rovinu nejvýše na (1/2)n(n + 1) + 1 oblastí.
- Princip matematické indukce říká (coby axiom), že k důkazu věty
	- "Pro každé přirozené (celé) n >= k0 platí T(n)"
- stačí ověřit platnost těchto dvou tvrzení:
	- T(k0) (tzv. báze neboli základ indukce)
	- Pro každé k >= k0; jestliže platí T(k), (indukční předpoklad)
	- pak platí také T(k + 1). (indukční krok)
## Příklady důkazů indukcí
### Příklad 4.6
- Velmi jednoduchá a přímočará indukce
- Věta. *Pro každé přiroz. n >= 1 je stejná pravděpodobnost, že při současném hodu n kostkami bude výsledný součet sudý, jako, že bude lichý.*
### Důkaz:
- Základ indukce je zde zřejmý: Na jedné kostce (poctivé!) jsou tři lichá a tři sudá čísla, takže obě skupiny padají se stejnou pravděpodobností.
- Indukční krok pro k > 1: Nechť psk pravděpodobnost, že při hodu k kostkami bude výsledný součet sudý, a plk je pravděpodobnost lichého. Podle indukčního předpokladu je
$$p_{sk} = p_{lk} = \frac{1}{2}$$
- Hoďme navíc (k + 1)-ní kostkou. Podle toho, zda na ní padne liché nebo sudé číslo, je pravděpodobnost celkového sudého součtu rovna
$$\frac{3}{6}p_{lk} + \frac{3}{6}p_{sk} = \frac{1}{2}$$
- a stejně pro pravděpodobnost celkového lichého součtu.
### Příklad 4.7
- Ukázka skutečné důkazové „síly" principu matematické indukce.
- Věta. Pro každé n > O platí, že n přímek dělí rovinu nejvýše na
$$\frac{1}{2}n(n+1)+1$$
- oblastí
- ![[Pasted image 20251008185643.png | 300]]
### Důkaz
- Pro bázi indukce postačí, že n = 0 přímek dělí rovinu na jednu oblast. (Všimněte si také, že 1 přímka dělí rovinu na dvě oblasti.)
- Mějme nyní rovinu rozdělenou n = k přímkami na nejvýše 1/2 k(k + 1) + 1 oblastí. Další, (k + 1)-ní přímka je rozdělena průsečíky s předchozími přímkami na nejvýše k + 1 úseků a každý z nich oddělí novou oblast roviny. Celkem tedy bude rovina rozdělena našimi přímkami na nejvýše tento počet oblastí:
$$\frac{1}{2}k(k + 1) + 1 + (k + 1) = \frac{1}{2}k(k + 1) + \frac{1}{2}2(k + 1) + 1 = \frac{1}{2}(k + 1)(k + 2) + 1$$
- A toto je přesně naše tvrzení pro n = k + 1, takže jsme hotovi.
### Příklad 4.8
- Další indukční důkaz rozepsaný v podrobných krocích.
#WIP #todo 
![[Pasted image 20251008190145.png]]
# Komentáře k matematické indukci
- Základní trik všech důkazů matematickou indukcí je vhodná reformulace tvrzení T(n + 1) tak, aby se „odvolávalo" na tvrzení T(n).
	- Dobře se vždy podívejte, v čem se liší tvrzení T(n + 1) od tvrzení T(n). Tento „rozdíl" budete muset v důkaze zdůvodnit.

- Dokud se matematickou indukci teprve učíte, používejte následující.

- Zaveďte si další proměnnou k a formulujte svá tvrzení a úpravy stylem „platí-li naše tvrzení T(n) pro n := k, pak bude platit i pro n := k + 1".

- Pozor, občas je potřeba *zesílit* tvrzení T(n), aby indukční krok správně „fungoval" (a jsou situace, kde tento trik velmi pomáhá).

- Často se chybuje v důkazu indukčního kroku, neboť ten bývá většinou výrazně obtížnější než báze, ale o to *zrádnější* jsou chyby v samotné zdánlivě snadné bázi!
	- Dejte si dobrý pozor, od které hodnoty n >= k0 je indukční krok univerzálně platný a jestli báze nezahrnuje více než jednu hodnotu...
### Příklad 4.9
- Kdy je vhodné (a v zásadě také nutné) indukční tvrzení zesílit...
- Věta. Pro každé n >= 1 platí
$$s(n) = \frac{1}{2} + \frac{1}{2^2} + \frac{1}{2^3} + \dots + \frac{1}{2^n} < 1$$
### Důkaz
- Báze indukce je zřejmá, neboť 1/2 < 1.
- Co však indukční krok? Předpoklad s(n) < 1 je sám o sobě „příliš slabý" na to, aby bylo možno tvrdit také:
$$s(n + 1) = s(n) + \frac{1}{2^{n + 1}} < 1$$
- Neznamená to ještě, že by celé tvrzení nebylo platné, jen je potřeba náš indukční předpoklad zesílit. Budeme raději dokazovat silnější
$$„Pro \ každé \ přirozené \ n > 1 \ platí \ s(n) \leq 1 — \frac{1}{2^n}    < 1 . \ "$$
- To platí pro bázi n = 1, neboť \ < 1 — \, a dále už úpravou jen dokončíme zesílený indukční krok:
$$s(n + 1) = s(n) + \frac{1}{2^{n + 1}} \leq 1 - \frac{1}{2^n} + \frac{1}{2^{n + 1}} = 1 - \frac{1}{2^{n + 1}}$$
## Rozšíření předpokladu; silná indukce
- Mimo zesilování tvrzení indukčního kroku jsme někdy okolnostmi nuceni i k rozšiřování samotné báze indukce a s ní indukčního předpokladu na více než jednu hodnotu parametru n.
	- Můžeme například předpokládat platnost (parametrizovaných) tvrzení T{n) i T(n + 1) zároveň, a pak odvozovat platnost T(n + 2).
		- Toto lze samozř. zobecnit na tři i více předpokládaných parametrů.c
	- Můžeme dokonce předpokládat platnost tvrzení T(j) pro všechna j = k0, k0 + 1,..., n najednou a dokazovat T(n + 1)
	- (vznešeně se této variantě indukce říká ***silná indukce***).
		- Toto typicky využijeme v případech, kdy indukční krok „rozdělí" problém T(n + 1) na dvě menší části a z nich pak odvodí platnost T(n + 1).
- Fakt: Obě prezentovaná „rozšíření" jsou v konečném důsledku jen speciálními instancemi základní matematické indukce; nejsou o nic „silnější" ve striktním matematickém smyslu a použité rozšířené možnosti pouze zjednodušují formální zápis důkazu.
### Příklad 4.10
- a
![[Pasted image 20251008192732.png]]
### Příklad 4.11
- Ukázka s vhodným použitím silné indukce:
- Věta. Každé přirozené číslo n >= 2 lze zapsat jako součin prvočísel (může být jen jednoho a prvočísla nemusí být různá).c
### Důkaz:
- **Báze indukce**. Nechť n = 2, pak n je prvočíslem a součinem jednoho prvočísla, c
- **Indukční krok**. Pokud nemá n vlastní dělitele, je n prvočíslem vzhledem k předpokladu n >= 2, což je shodné s bází.
- Jinak napíšeme n = a - b, kde platí a, b >= 2 a zároveň a, b < n, a proto lze na obě čísla a, b použít indukční předpoklad.

- Tudíž každé z nich lze napsat jako součin prvočísel a jelikož ta nemusí být různá, prostě oba součiny sloučíme do jednoho, jehož výsledkem je a • b = n.
## Závěrem malý "problém"
### Příklad 4.12
![[Pasted image 20251008193339.png]]