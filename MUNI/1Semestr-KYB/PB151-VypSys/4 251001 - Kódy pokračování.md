## Vícebajtová kódování
### UNICODE
- standard definuje i název znaku, převodní tabulky malá-velká písmena atp.
- nevýhody: násobná délka textu, větší znaková sada
### UCS-2
- = universal coded char. set
- základní způsob zápisu unicode znaků, 2 bajty na znak
- zastaralé -> UTF-16
### UCS-4
- 4 bajty na znak
- zastaralé, používá se UtF-32 (skoro totéž)
## UTF-8
- Nejpoužívanější zobrazení Unicode znaků
- Pokud je znak ve ASCII-7 -> zobrazí se beze změny v 1 bajtu, tzn. nejvyšší bajt je roven nule
- UTF-8 je kompatibilní s ASCII
- Pokud znak není v ASCII, je zapsán dvěma až čtyřmi bajty -> 21 datových bitů, cca 2 mil. znaků (Před Unicode 4.0 šesti bajty)
	- 1. bajt: počet jedniček zleva vyjadřuje délku sekvence, následuje nula, která je oddělovač
	- Další bajty, v nejvyšších dvou bitech vždy 10
![[Pasted image 20251001141033.png]]
- České znaky mají malé hodnoty, lze všechny zapsat dvěma bajty
- Příklad: "Příliš"
- ![[Pasted image 20251001141143.png | 300]]
	- ř: 1100 0101 1001 1001  "ř" v unicode U+0159 (hexa)
- Ordinální hodnota se zapisuje U+00ED (tj. U+hexa číslice)
### Postup transformace znaků
- "ř" v unicode U+0159 (hexa)
- ordinální hodnota ř binárně:
	- 0000 0001 0101 1001
- Binární hodnota nemá více než 11 významných bitů, proto ji lze uložit do 2bojtového UTF-8. Dvoubajtové UTF-8 se vkládá do následující formy:
	- 110x xxxx 10xx xxxx
	- vložíme postupně
- Binární ordinální hodnotu znaku ř dosadíme do dvoubajtové formy na místa znaků x. Začneme vždy zprava, tj. od řádu 2^0.
- Nadbytečné levostranné nuly ignorujeme.
	- 1100 0101 1001 1001
- Převedeno do hexadecimální soustavy: C5 99

- Pomocí UTF-8 lze zobrrazit maximálně 2^21 možných znaků
- Jak rozpoznám úvodní bajt od následujících?
- Nikdy nejsou pro zakódování znaku použity bajty s hodnotou 0FE (11111110) a 0FF (11111111)
- Proto se někdy používá kód U+FEFF jako označení, že následuje UTF-8. Nazývá se BOM = Byte-Order Mark.
- Nalezne.li se U+FEFF, jde o Little-Endian uložení
- Ovšem pro UTF-8 nemá endianita smysl, protože se ukládá po jednotlivých bajtech.
## Detekční kódy
- 1 chyba znamená inverzi hodnoty jednoho bitu
- zavedení nadbytečnosti (redundance)
- parita
	- sudá / lichá
- Kód 2 z 5:
	- ![[Pasted image 20251001143554.png | 100]]
- Zachytí všechny 1násobné chyby a 40 % 2násobných chyb
## Opravné kódy
- Příklad: Ztrojení ![[Pasted image 20251001143736.png | 200]]
- Dokáže opravit 1 chybu a detekovat 2 chyby
## Kódová (Hammingova) vzdálenost
- Definice: Kódová vzdálenost d = počet bitů, v nichž se liší dvě sousední platné kódové kombinace.
- Znázornění pomocí Hammingovy krychle:
	- trojrozměrná (xyz)
	- dvojrozměrná (xy)
	- jednorozměrná (x)
### Trojrozměrná/Dvoj./Jedno.
- Dvě platné kódové kombinace (xyz): 000 až 111 (d=3) (krychle)
- dvojroz. - kostka 00 až 11 (d=2)
- d=1, prostě linka
## Detekce a oprava k chyb
- Vztahy:
	- Detekce k chyb: d>=k+1
	- Oprava k chyb: d>=2k+1
![[Pasted image 20251001144440.png | 400]]
## Booleova algebra
- Boolova algebra je nauka o operacích na množině {0,1}
- Definice:
	- B.A. je množina B o alespoň 2 prvcích nad níž jsou definovány operace operace sčítání, násobení a negace splňující tyto axiomy:
		- (předp.: a, b, c ∈ B) :
			- a + b ∈ B
			- a . b ∈ B
		- Existuje prvek 0, pro který platí: a + 0 = a
		- Existuje prvek 1, pro který platí: a . 1 = a
	- Komutativní zákon:
		- a + b = b + a
		- a . b = b . a
	- a + (b . c) = (a + b) . (a + c)
	- a . (b + c) = (a . b) + (a . c)
	- Pro každý prvek a existuje prvek ¬a ∈ B:
		- a · ¬a = 0
		- a + ¬a = 1
### Základní operace
- B. A. užívá jen 3 základní operace:
	- Logický součin "AND ∧ ∩ × . "
	- Logický součet "OR ∨ ∪ + "
	- Negace "NOT (x s čárou nad) ¬ ∼ (před operandem)"
- Způsoby popisů:
	- Pravdivostní tabulka
	- ![[Pasted image 20251001145223.png | 200]]
	- Graficky v rovině = Vennovy diagramy
	- ![[Pasted image 20251001145156.png | 300]]
	- Mat. aparát
## Využití Booleovy algebry
- Základní prvek: relátko -> sepnuto rozepnuto
- spínací / rozepínací kontakt (záleží co kam přinesu (1 a 0))
## Zapojení kontaktů
- sériové a AND(.) ¬b
- ![[Pasted image 20251001153234.png | 500]]
- paralelní a OR(+) ¬b
- ![[Pasted image 20251001153258.png | 450]]

- Příklady:
	- Pračka smí začít topit, když je napuštěn dostatek vody (a) a současně nejsou otevřena dvířka (b), tj. a . b
	- Automobil musí automaticky rozsvítit světla, když prší (a) nebo není dostatek světla (b), tj. a + b
## Obvodové znázornění Booleovy algebry
- ![[Pasted image 20251001153643.png | 400]]

- Př: f = a · ¬c +¬b · c
- ![[Pasted image 20251001153911.png | 400]]
## Minimalizace počtu operací B-algebry
- Proč minimalizovat? Méně výrazů znamená menší počet součástek, nižší cenu a rychlejší zpracování
- Jak minimalizovat?
	1. Matematické úpravy Př: ¬x¬yz + ¬xyz = ¬xz(¬y + y) = ¬xz
	2. Využitím jednotkové krychle f = ¬x¬yz + ¬xyz + x¬y¬z + x¬z
		1. ![[Pasted image 20251001154210.png | 300]]
		2. f = ¬xz + x¬z
	3. Karnaughova mapa - normalizací Vennova diagramu
## Shefferova algebra
- Je vybudovaná na jedné logické funkci = negace logického součinu NAND
- Pro libovolný počet proměnných f = ¬x ¬· ¬y
- ![[Pasted image 20251001154453.png | 200]]
- Pomocí operace NAND lze realizovat všechny operace Booleovy algebry
- Platí zákon komutativní: ¬(x · y) = ¬(y · x) 
- Neplatí zákon asociativní: ¬(¬(x · y) · z)  ̸= ¬(x · ¬(y · z))  ̸= ¬(x · y · z)
## Peirceova algebra
- Vystavěna na operaci negace logického součtu NOR - obdobné jako S-algebra
- Převod minimalizované formy B-algebry na S-algebru:
	- opakovaná aplikace de Morganových pravidel >> ¬(a + b) = ¬a . ¬b
	- ![[Pasted image 20251001154851.png | 200]]
## Fyzikální podstata signálu
- ![[Pasted image 20251001155031.png | 400]]
- ![[Pasted image 20251001155056.png | 400]]
### Průběh signálu
- Změny signálu v praxi nejsou diskrétní, nýbrž spojité.
- ![[Pasted image 20251001155146.png | 400]]
### Zakázané pásmo
- hodnota signálu nelze číst
- ![[Pasted image 20251001160405.png | 400]]
- pozitivní logika - L je 0 H je 1, negativní to má naopak
## Technologie TTL (transistor-transistor logic)
- Základní stavební prvek je tranzistor NPN
- Parametry:
	- napájecí napětí +5V
	- L<0,8V   L ∼ 0,4V
	- H>2,0V   H ∼ 2,4V
- Tři vývody: báze, kolektor, emitor
- Malou změnou proudu mezi bází a emitorem ovlivňujeme velké změny proudu mezi kolektorem a emitorem.
- Napájení se postupem času snižuje
## Invertor v TTL
- f = neg y
- ![[Pasted image 20251001160941.png | 300]]
- nízká na bázi uzavírá vysoký proud otevírá ( vysoká = 1)
## NAND pomocí dvou tranzistorů
- ![[Pasted image 20251001161933.png | 300]]
- ![[Pasted image 20251001162012.png | 200]]
## NOR pomocí dvou trenzistorů
- ![[Pasted image 20251001162435.png | 400]]
- ![[Pasted image 20251001162502.png | 200]]
## Nonekvivalence - XOR
- exkluzivní or
- ̸ ≡ • ⊕ • =1 • M2
- ![[Pasted image 20251001162620.png | 150]]

- Využití obvodu nonekvivalence
- Př: generátor parity : y = a ⊕ b ⊕ c ⊕ d = (a ⊕ b) ⊕ (c ⊕ d)
	- ![[Pasted image 20251001163053.png | 300]]
## Logické obvody
- Multiplexor : Z = A . X + neg A . Y
- 4vstupý multiplexor - 4 datové vstupy, 2 adresové vstupy
- ![[Pasted image 20251001163325.png | 500]]
##