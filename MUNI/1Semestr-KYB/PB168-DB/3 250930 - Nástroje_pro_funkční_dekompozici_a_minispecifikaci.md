https://is.muni.cz/auth/el/fi/podzim2025/PB168/um/is/DFD.pdf
**Konceptováno**:
- Datová vrstva (relační datová vrstva) <> Informační systém <> Data se zobrazují (výstupy)(uživatelská vrstva)
## DFD - Data Flow Diagram
- modelovací nástroj -> umožňuje zobrazit systém jako síť procesů
- funkčně orientovaný pohled na systém
## Komponenty DFD
- proces, funkce, transformace
- Paměť, datastór
- Datový tok, tok
- Terminátor, vnější entita (vstupní/výstupní sestava)
![[Pasted image 20250930162202.png | 400]]
## Příklad notací Gene/Sarson a Yourdon/DeMarco
![[Pasted image 20250930162507.png | 400]]
- šipka z paměti do ověření představuje **čtení**
- aktualizovaný účet = **update**
- potvrzený doklad = **insert**
## Procesy
- ukazují část systému, která transformuje určité vstupy na výstupy.
- pojmenován jediným slovem, frází, jednoduchou větou.
- pokud název obsahuje jméno osoby, skupiny, zařízení,, pak jméno vyjadřuje, kdo provádí nějakou činnost, transformaci dat, místo toho, aby vyjádřilo podstatu transformace
## Toky
- cesta, po které se pohybují datové shluky (informační pakety) z jedné části systému do druhé.
- V některých případech vyjadřují toky pohyb fyzických materiálů. U reálných systémů mohou být na DFD současně toky, které vyjadřují pohyb materiálů a dat.
## Materiálové a datové toky
![[Pasted image 20250930164536.png | 500]]
- Paket má jiný význam, pokud putuje na různě pojmenovaných tocích.
## Divergující toky
- Duplikáty tejného datového paketu jsou zaslány do různých částí.
![[Pasted image 20250930164826.png | 400]]
## Pojmenování datových toků
- Jméno toku by mělo vyjadřovat podstatu transformace
- ![[Pasted image 20250930165027.png | 300]]
- Př.:
	- objednávka - prověřená objednávka
	- řetěz znaků - číslo v daném rozsahu
	- vyplněný formulář - dostatečně vyplněný formulář
	- rastrový obraz - ekvalizovaný rastrový obraz
## Paměť, esenciální paměť
- Paměť modeluje kolekci dat v klidu. Jméno je voleno obvykle jako množné číslo jména, kterým jsou označeny pakety na tocích vedoucích do a z paměti.
- **Esenciální paměť** - data předávaná mezi dvěma a více procesy pracujícími v různém čase.
![[Pasted image 20250930165418.png | 500]]
### Vlastnosti paměti
- pasivní částí systému
- data nejsou přenášena do/z paměti, pokud o to proces explicitně nepožádá

- čtení = nedestruktivní -> paměť se nemění

- tok vedoucí do paměti může mít význam zápisu, změny nebo zrušení. Může vyjadřovat následující sytuace:
	- Jeden nebo více nových paketů je přidáno do paměti; na konec nebo někam mezi existující pakety. 
	- Jeden nebo více paketů je zrušeno, přemístěno z paměti. 
	- Jeden nebo více paketů jsou přeměněny; to může znamenat změnu celého paketu nebo (častěji) části paketu, nebo obdobných částí více paketů.
## Implementační paměť
![[Pasted image 20250930165929.png | 500]]
### Důvody pro implementační paměť
- Oba procesy poběží na stejném počítači, ale není k dispozici dostatek paměti (nebo jiný HW prostředek), kterou by oba procesy použily ve stejném čase.
- Jeden nebo oba procesy budou řešeny na technickém vybavení, které není dostatečně spolehlivé. Paměť slouží jako prostředek pro uchování dosud zpracovaných částí dat a zvyšuje bezpečnost systému. 
- Oba procesy budou implementovány různými programátory. Paměť pak slouží jako rozhraní mezi dvěma nezávisle řešenými subsystémy. 
- Systémový analytik předvídá, že paměť bude v budoucnosti použita pro další, dosud nespecifikované funkce.
## Paměti s nepojmenovanými toky
![[Pasted image 20250930170510.png | 400]]
- Z analytického hlediska je nepodstatné, zda vyjadřujeme situaci, kdy:
	- jediný datový paket je čten z paměti
	- více než jeden datový paket je získán z paměti
	- je čtena pouze část paketu
	- jsou čteny části více než jednoho paketu
## Terminátor
- reprezentuje externí entity, se kterými systém komunikuje
- vně modelovaného systému, toky, které je propojují s procesy (nebo pamětmi) v systému, reprezentují rozhraní mezi systémem a vnějším světem.

- Žádný vztah mezi terminátory nebude ukázán na DFD.
## Celková hierarchie DFD
![[Pasted image 20250930171017.png | 500]]
- to co je o úroveň níže je vidět o úroveň výš
- pokud T1 vede do obousměrně do procesů v nižší úrovni může ale směřovat čtení do jiného sub-procesu/paměti než jeho modifikace (čtení třeba do sub1 a modify do sub3)
## Příklad - Dekompozice zpracování žádosti
1) Vyřizování žádostí
	1) Vstupní kontrola
	2) Zpracování žádostí
		1) Určení komu patří
		2) Vlastní vyřizování
		3) Nestandardní zpracování
	3) Styk s občany
## Doporučení při tvorbě DFD
- Volit **výstižná jména** pro procesy, datové toky, paměti a terminátory. 
- **Systematicky číslovat** procesy. 
- Překreslovat diagramy tak, aby byly co nejestetičtější. (terminátory vně a procesy vevnitř, nekřížit toky pokud možno)
- Vyhnout se příliš jednoduchým nebo příliš složitým DFD. 
- Ověřit vnitřní i externí konzistenci DFD.
## Příklad - Studijní IS
![[Pasted image 20250930172809.png | 500]]
## Vnitřní konzistence DFD (nedělat!)
- "Černý díra" => procesy, které mají pouze vstupy a neprodukují žádná data (skryté rozhraní, ukrytý terminátor)
- "Bilý trpaslíci" => procesy, které mají pouze výstupy (skryté DB rozhraní, ukrytý terminátor)
- neoznačené toky a procesy
	- Podezření: 
		- U nepojmenovaného datového toku byly seskupeny náhodně různé skupiny dat a je obtížné je pojmenovat. 
		- U nepojmenovaného procesu není zřejmá funkce, rozhodnutí bylo "odloženo" na pozdější dobu.
- Paměť výhradně pro čtení či pro zápis. Má smysl pouze na rozhraní mezi systémem a terminátorem (většinou považováno za chybu)
## Vztahy podrobené analýze
![[Pasted image 20250930173342.png | 400]]
## Hierarchie DFD
- DFD 0.úrovně:
	- pohled na hlavní funkce a na rozhraní mezi těmito funkcemi
![[Pasted image 20250930173554.png | 300]]
## Pravidla tvorby víceúrovňových DFD
- číslování procesu se přenáší na nižší úrovně (n, n.1, n.2,...)
- Jméno procesu se stává jménem DFD na nižší úrovni
- Doporučeno DFD na A4 s průměrně 5-7 procesy a pamětmi
- Systém střední velikosti bude mít cca 3-6 úrovní DFD

- Pro zajištění konzistence na jednotlivých úrovních DFD musí souhlasit vstupní a výstupní datové toky u procesů a jim odpovídajících DFD na nižších úrovních.
	- ![[Pasted image 20250930173927.png | 500]]
- Paměť zakreslíme poprvé na úrovni, kde je použita jako rozhraní mezi dvěma a více procesy. Na nižších úrovních ji zopakujeme u všech DFD, které obsahují dekompozici procesů spolupracujících s pamětí na vyšší úrovni.
	- ![[Pasted image 20250930174020.png | 250]]
## Minispecifikace - Strukturovaná angličtina
IF <podmínka>,
	THEN
		<činnost pro platnou podmínku>
	OTHERWISE
		<činnost, když podmínka neplatí>

SELECT:
	CASE 1 (podmínka 1): <činnost pro podmínku 1>
	...
	CASE n (podmínka n): <činnost pro podmínku n>

<úvodní fráze pro opakování>:
	<opakovaná činnost>
<podmínka pro opakování>

<úvodní fráze pro opakování a podmínka opakování>:
	<opakovaná činnost>

REPEAT UNTIL, WHILE DO, FOR EVERY DO
### Přiklad - Stipendia
![[Pasted image 20250930174559.png | 500]]
### Přiklad - Koktejly v letadlech
![[Pasted image 20250930174651.png | 500]]
![[Pasted image 20250930174708.png | 500]]
![[Pasted image 20250930174728.png | 500]]
## Minispecifikace - Úvodní a závěrečné podmínky
Doporučení: Nejprve popsat normální situace, poté připojit podmínky pro řešení chybových situací.
- Precondition 1 - Zákazník uvede číslo_účtu, které se shoduje s číslem účtu vedeným v paměti ÚČTY, jehož stavový_kód je nastaven na hodnotu „platný“.
- Postcondition 1 - Připravena faktura, na které jsou uvedeny číslo_účtu a prodejní_cena.
- Precondition 2 - Podmínka 1 není splněna (číslo_účtu nelze nalézt v paměti ÚČTY, nebo stavový_kód není „platný“).
- Postcondition 2 - Je sestavena chybová zpráva.