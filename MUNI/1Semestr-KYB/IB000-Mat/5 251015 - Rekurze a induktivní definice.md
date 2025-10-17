#WIP #todo 
# Posloupnosti a rekurentní vztahy
- Uspořádané fc-tice z daného oboru hodnot H jsou nazývány konečnými posloupnostmi délky k (nad H).
- Pojem posloupnosti zobecňuje toto pojetí na „nekonečnou délku" takto:
### Definice
- Posloupnost (nekonečná) je zobrazením z přirozených čísel N do oboru hodnot H, neboli:
$$p : \mathbb{N} -> H$$
- Místo „funkčního" zápisu n-tého členu posloupnosti jako p(n) častěji používáme „indexovou" formu jako p_n, ve které se celá posloupnost zapíše:
$$(p_{n})_{n \in \mathbb{N}}$$
	- Oborem hodnot H posloupnosti obvykle bývá nějaká číselná množina, ale může to být i jakákoliv jiná množina.
- Poznámka: Třebaže to není zcela formálně přesné, běžně se setkáme s posloupnostmi indexovanými od nuly nebo od jedničky, jak se to v aplikacích hodí. I my se budeme tímto řídit a vždy si určíme počáteční index podle potřeby.
## Příklady posloupnosti
$$p_{0} = 0, p_{1} = 2, p_{i}=2i, \dots$$
	- je posloupnost sudých nezáporných čísel.
- (3, 3.1, 3.14, 1.141, ...) je posl. postupných dekadických rozvojů pi.
- třeba (jablko, hruška, švestka, hruška, hruška, ...) je posloupnost nad druhy ovoce coby oborem hodnot.
- (1, -1, 1, -1, ...) je posloupnost určená vztahem:
$$p_{i} = (-1)^{i}, i\geq 0$$
- avšak pokud bychom chtěli stejnou posloupnost (1, -1, 1, -1, ...) určit indexy od jedné, tj. zadat ji jako: ;tak vztah bude:
$$q_{i}, i\geq 1$$$$q_{i} = (-1)^{i-1}$$
### Definice:
- Posloupnost (p\_n)_{n in N} je
	- rostoucí pokud p_(n+1) > p_n a nerostoucí pokud p_(n+1) <= p_n,
	- klesající pokud p_(n+1) < p_n a neklesající pokud p_(n+1) >= p_n
- platí pro všechna n.
## Rekurentní zadání posloupnosti
### Definice:
- Říkáme, že posloupnost (p_n)\_{n in N} je zadána rekurentně, pokud je dán její počáteční člen po (či několik počátečních členů) a dále máme předpis, jak určit hodnotu členu p_(n + 1) z hodnot p_i pro nějaká i <= n.
![[Pasted image 20251015182351.png]]
## Řešení rekurentní posloupnosti
### Příklad 5.2 Posloupnost f : N -> Z je zadaná rekurentní definicí
![[Pasted image 20251015183318.png]]
![[Pasted image 20251015183730.png]]
### Příklad 5.3 Posloupnost (s_n)\_{n in N} je zadaná rekurentní definicí
![[Pasted image 20251015184542.png]]
# Rekurze s více parametry a indukce
- Kromě přímočarých ukázek rekurze na funkcích s jediným celočíselným parametrem (tj. na posloupnostech) se lze setkat, především v návrhu algoritmů, s rekurzí za přítomnosti více parametrů.
- I pro takové obecnější případy je základním matematickým přístupem použít indukci, avšak nejprve je nutno vhodně **zvolit či vytvořit** jeden celočíselný parametr, podle nějž indukci můžeme vést.
- Samozřejmě takový parametr (i nově vytvořený) opět musí být **zdola ohraničený** a pro každou rekurentně odkazovanou hodnotu musí být **nižší než** pro aktuálně určovanou hodnotu.
Možné přístupy k věci si uvedeme na několika typických ukázkách.

## Přístup fixace parametru
### Příklad 5.4 Mějme funkci m : N x N -> N definovanou rekurentně takto:
![[Pasted image 20251015185708.png]]
![[Pasted image 20251015185730.png]]
## Indukce k součtu parametrů
### Příklad 5.5 Mějme funkci k : N x N -> N definovanou rekurentně takto:
![[Pasted image 20251015190435.png]]
![[Pasted image 20251015190946.png]]
![[Pasted image 20251015191300.png]]
## Přístup se zesílením dokazovaného tvrzení
### Příklad 5.6 Zjistěte, jakou hodnotu v závislosti na celočíselném parametru a nabývá funkce t(a, 1), která je rekurentně definována takto:
![[Pasted image 20251015192215.png]]
![[Pasted image 20251015192355.png]]
# Induktivní definice množin
- Širokým zobecněním rekurentních definic posloupností je následující koncept.
### Definice 5.7 Induktivní definice množiny
- Jedná se obecně o předpis (nějaké) množiny M v následujícím tvaru:
	- Je dáno několik pevných (bázických) prvků a1, a2, ...., ak  in M
	- Je dán soubor induktivních pravidel typu
		- Jsou-li (libovolné prvky) x1, ..., xl in M, pak také y in M
	- V tomto případě je y typicky funkcí y = f_i(x1, ..., xl) (v pravidle číslo i)-
- Pak naše induktivně definovaná množina M je určena jako nejmenší (inkluzí) množina vyhovující všem těmto pravidlům.
![[Pasted image 20251015193447.png]]
## Pokročilý ilustrační příklad
![[Pasted image 20251015193508.png]]
![[Pasted image 20251015193521.png]]
![[Pasted image 20251015193537.png]]