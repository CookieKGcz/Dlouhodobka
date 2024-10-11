### [Úvod](https://haxagon.xyz/challenge/641822879487384990a085be#%C3%BAvod)

V této úloze se podíváme na symetrickou kryptografii. Začneme od těch nejjednodušších šifer a skončíme u AES, což se standard používaný dodnes.

Symetrickou šifrou se rozumí šifra, která pro zašifrování a odšifrování používá stejný klíč. Úplně nejjednodušší symetrickou šifrou je XOR šifra.

### [XOR šifra](https://haxagon.xyz/challenge/641822879487384990a085be#xor-%C5%A1ifra)

Používá logického operátoru XOR neboli e**X**clusive **OR**. V zápisu se značí znakem: `⊕`. Například A XOR B je `A ⊕ B`.

A ve schématech se značí:![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric1/xor.png)

Předpokládám, že jste se již s logickými operátory setkali, ale pro osvěžení paměti máte níže jeho pravdivostní tabulku.

|A (zpráva)|B (klíč)|Výsledek|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

_Pravdivostní tabulka operace XOR_

Jedním z hlavních důvodů, proč je XOR v kryptografii tak užitečný, je jeho dokonalá vyváženost. Pokud použijete skutečně náhodný klíčový bit, tak je pro daný vstup 0 nebo 1 stejně pravděpodobné, že výsledek bude 0 nebo 1.

#### [Jak funguje?](https://haxagon.xyz/challenge/641822879487384990a085be#jak-funguje)

XOR šifra funguje tak, že pro zašifrování aplikuje XOR na bit původní zprávy a bit klíče. To se provede pro všechny bity původní zprávy. Pokud je klíč kratší než původní zpráva, tak se klíč opakuje.

Pojďme si společně zašifrovat slovo `ahoj` klíčem `OKNO`:

Nejprve převeďte původní zprávu i klíč do binární soustavy. To můžete buďto udělat ručně pomocí ASCII tabulky nebo použít nějaký online nástroj

- Původní zpráva: `01100001 01101000 01101111 01101010`
- Klíč: `01001111 01001011 01001110 01001111`

Teď už stačí pouze aplikovat XOR na jednotlivé bity původní zprávy a klíče. To klidně můžete udělat "v ruce" pomocí pravdivostní tabulky. Výsledkem by mělo být:

```
00101110 00100011 00100001 00100101
```

> Klíč je stejně dlouhý, jako původní zpráva, takže ho není potřeba opakovat.

Krása XORu spočívá v symetrii šifrování a odšifrování. Pro odšifrování šifrovaný text opět bit po bitu XORujte s klíčem. Výsledek je stejný, jako původní zpráva

```
01100001 01101000 01101111 01101010
```

Pokud binární čísla převedete na znaky, tak dostanete původní `ahoj`.

### [Bloková vs proudová šifra](https://haxagon.xyz/challenge/641822879487384990a085be#blokov%C3%A1-vs-proudov%C3%A1-%C5%A1ifra)

Jedná se o další způsob rozdělování šifer.

- Bloková šifra funguje tak, že vstupní data rozdělí do bloků o fixní délce (například 64 nebo 128 bitů) a každý blok je šifrován samostatně.
    
- Proudová šifra šifruje vstupní data postupně po jednotlivých bitech/znacích.
    

Všechny předchozí šifry (Caesarova, Morseovka, XOR ...) byly proudové šifry. Teď se podíváme na první blokovou šifru se jménem DES.

### [DES](https://haxagon.xyz/challenge/641822879487384990a085be#des)

**D**ata **E**ncryption **S**tandard vznikl v sedmdesátých letech. Algoritmus vyvíjeli v IBM a práci konzultovali s NSA. Zprvu si lidé mysleli, že NSA chce do algoritmu přidat různé backdoory, ale později se objevilo, že změnami udělali algoritmus opravdu bezpečnější. Ale o útocích a kryptoanalýze si povíme až později. Teď se pojďme podívat do jádra algoritmu.

Jedná se o blokovou symetrickou šifru

- Její blok má 64 bitů
- Její klíč má efektivně 56 bitů

#### [Jak DES funguje?](https://haxagon.xyz/challenge/641822879487384990a085be#jak-des-funguje)

Začneme vrchní strukturou a postupně budeme prozkoumávat jednotlivé části.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric1/des-top.png)_Vrchní struktura DESu_

Zde je vidět vrchní struktura algoritmu DES. Dovnitř vstupuje 64 bitů plaintextu (jeden blok), 56bitový klíč a výstupem je 64 bitů (jeden blok) ciphertextu.

Uvnitř se dějí tři věci

- První je modul `Initial permutation` (IP). Zde se přehází pořadí vstupních bitů plaintextu podle předem definované tabulky. Tento modul nezávisí na klíči.
- V prostřední sekci probíhá šifrování dat. Tato část závisí na klíči.
- Na závěr v posledním modulu `Final permutation` (FP) se opět přehází bity. Jedná se o inverzní operaci k `IP`.

#### [Initial permutation](https://haxagon.xyz/challenge/641822879487384990a085be#initial-permutation)

Značí se `IP` a přehazuje bity podle tabulky, která udává, ze kterého bitu vstupu je brán bit výstupu. První buňka (levá, horní) značí první bit výstupu a obsah této buňky udává, z kolikátého bitu vstupu se berou data výstupu.

|||||||||
|---|---|---|---|---|---|---|---|
|58|50|42|34|26|18|10|2|
|60|52|44|36|28|20|12|4|
|62|54|46|38|30|22|14|6|
|64|56|48|40|32|24|16|8|
|57|49|41|33|25|17|9  |1|
|59|51|43|35|27|19|11|3|
|61|53|45|37|29|21|13|5|
|63|55|47|39|31|23|15|7|

_Tabulka IP_

Tabulku čtěte po řádcích, takže 1. bit výstupu se bere z 58. bitu vstupu, 2. bit výstupu se bere z 50. bitu vstupu... až poslední 64. bit výstupu se bere ze 7. bitu vstupu.

Pokud si stále nejste jisti, jak IP funguje, tak Vám určitě pomůže obrázek

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric1/IP_fin.png)_Znázornění IP_

#### [Final permutation](https://haxagon.xyz/challenge/641822879487384990a085be#final-permutation)

Značená `FP`, je inverzní k IP. To, že je něco inverzní znamená, že je to opačná operace k té původní. Příklad pro vysvětlení: původní data --> IP --> FP = původní data.

FP funguje opět na identickém principu jako IP. Udává, ze kterého bitu vstupu je brán bit výstupu.

|||||||||
|---|---|---|---|---|---|---|---|
|40|8|48|16|56|24|64|32|
|39|7|47|15|55|23|63|31|
|38|6|46|14|54|22|62|30|
|37|5|45|13|53|21|61|29|
|36|4|44|12|52|20|60|28|
|35|3|43|11|51|19|59|27|
|34|2|42|10|50|18|58|26|
|33|1|41|9|49|17|57|25|

_Tabulka FP_

Tabulku čtěte po řádcích, takže 1. bit výstupu se bere z 40. bitu vstupu, 2. bit výstupu se bere z 8. bitu vstupu... až poslední 64. bit výstupu se bere ze 25. bitu vstupu.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric1/FP_fin.png)_Znázornění FP_

Jak můžete vidět podle znázornění, tak FP opravdu dělá opak IP.

#### [Feistelova šifra](https://haxagon.xyz/challenge/641822879487384990a085be#feistelova-%C5%A1ifra)

Teď už přituhuje, pojďme se podívat do té sekce mezi IP a FP, tam, kde se data šifrují

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric1/feistel-des.png)

Na vstupu je 64 bitů permutovaného plaintextu. 64bitový výsledek směřuje do modulu `Final permutation`.

Zde se nachází Feistelova šifra. 64bitový blok plaintextu se na začátku rozdělí na dvě poloviny. Každá obsahuje 32 bitů. Levou polovinu budeme označovat L a pravou R.

R jde do funkce F, která přijme 32 bitů R a 48 bitů sub klíče. Výsledek této funkce je XORnutý s L a vede do dalšího kroku z pravé strany, jako R, zatímco původní R vede do dalšího kroku z levé strany, jako L. Takto se to opakuje šestnáctkrát.

Jak to, že se teď bavíme o 48bitovém klíči, když původní měl 56? To z toho důvodu, že pro každý z šestnácti kroků je vytvořen z původního 56bitového klíče jeden 48bitový. Každý krok tedy používá odlišný 48bitový klíč.

Po všech šestnácti krocích vede výsledek do `Final permutation`, kde se bity opět přehází a takto vznikne jeden zašifrovaný 64bitový blok.

### [To be continued](https://haxagon.xyz/challenge/641822879487384990a085be#to-be-continued)

V příští úloze se podíváme pod pokličku funkce F ve Feistelově šifře a všechny její kroky si zkusíte ručně provést. Je to jednodušší, než se zdá :)
### [Úvod](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#%C3%BAvod)

Minule jsme se naučili, jak funguje iniciální a finální permutace a Feistelova šifra v algoritmu DES. Vstupní data se za IP rozdělí na dvě poloviny a prochází Feistelovou šifrou.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric1/feistel-des.png)_Feistelova šifra v algoritmu DES_

Dnes se podíváme na funkci F ve Feistelově šifře.

### [Funkce F](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#funkce-f)

V matematice jste se už určitě setkali s funkcemi, například `f(x) = 2x`. `f` je jméno funkce a `(x)` značí, že je závislá na proměnné x. Za rovná se je předpis funkce `2x`. To už všichni dobře znáte a není to nic nového. Funkce ale může být mnohem více abstraktní a složitější. Jako například funkce F v algoritmu DES. Opět to je funkce, akorát je závislá na vstupních datech (32 bitech) a sub klíči (48 bitů).

Proč mají vstupní data 32 bitů už víte, jedná se o polovinu bloku. A proč sub klíč má 48 bitů si také určitě pamatujete, protože se z původních 56 bitů vytvoří pro každý krok ve Feistově šifře odlišný 48bitový sub klíč.

Ano, je to podstatně velký skok z Caesarovi nebo XOR šifry :) Generaci sub klíčů vynecháme, ale pojďme se podívat, jak funguje funkce F, která se dá rozdělit do čtyř kroků:

- Expanze (E)
- Mixování klíče (XOR)
- Substituce (S-boxy)
- Permutace (P)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Data_Encription_Standard_Flow_Diagram.svg/250px-Data_Encription_Standard_Flow_Diagram.svg.png)

#### [Expanze (E)](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#expanze-e)

Z původních 32 bitů (poloviny bloku) vytvoří 48 bitů.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric2/flowE.png)

Funguje stejně, jako tabulka IP a FP

Používá se tabulka, která udává, ze kterého bitu vstupu je brán bit výstupu. První buňka (levá, horní) značí první bit výstupu a obsah buňky udává, z kolikátého bitu vstupu se berou data.

|||||||
|---|---|---|---|---|---|
|32|1|2|3|4|5|
|4|5|6|7|8|9|
|8|9|10|11|12|13|
|12|13|14|15|16|17|
|16|17|18|19|20|21|
|20|21|22|23|24|25|
|24|25|26|27|28|29|
|28|29|30|31|32|1|

Tabulku čtěte po řádcích. První bit výstupu se bere z 32. bitu vstupu, druhý bit výstupu se bere z 1. bitu vstupu... až poslední 48. bit výstupu se bere z 1. bitu vstupu. Asi jste si všimnuli, že se některé vstupní bity používají vícekrát, ano právě opakováním některých vstupních bitů se z původních 32 bitů vytvoří 48.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric2/crypto-symetric-2_expansion.png)

_Znázornění expanze_

#### [Mixování klíče (XOR)](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#mixov%C3%A1n%C3%AD-kl%C3%AD%C4%8De-xor)

Zde je to jednoduché, XORne se 48 bitů expandované poloviny bloku s 48bitovým sub klíčem.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric2/flowXOR.png)

> Znak `⊕` značí v nákresu XOR.

#### [Substituce (S-boxy)](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#substituce-s-boxy)

**S**ubstitution-**box**

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric2/flowSBOX.png)

Zde se výsledek předchozího kroku rozdělí po šesti bitech a každá šestice putuje do jednoho S-boxu, první S-box je označen S1, druhý S2 atd...

Jednotlivé S-boxy se řídí tabulkou a podle ní z šestic vytvoří čtveřice. Substituují (nahrazují) za původních 6 bitů 4.

Zde je tabulka S-boxu 1 (S1). Řádek se vybírá pomocí dvou vnějších bitů a sloupec pomocí čtyř vnitřních bitů. Výsledek je v desítkové soustavě

|S1|x0000x|x0001x|x0010x|x0011x|x0100x|x0101x|x0110x|x0111x|x1000x|x1001x|x1010x|x1011x|x1100x|x1101x|x1110x|x1111x|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**0yyyy0**|14|4|13|1|2|15|11|8|3|10|6|12|5|9|0|7|
|**0yyyy1**|0|15|7|4|14|2|13|1|10|6|12|11|9|5|3|8|
|**1yyyy0**|4|1|14|8|13|6|2|11|15|12|9|7|3|10|5|0|
|**1yyyy1**|15|12|8|2|4|9|1|7|5|11|3|14|10|0|6|13|

Například číslo **1**0011**0** se rozdělí na dva **vnější** bity **10** a čtyři vnitřní bity 0011. V tabulce to je třetí řádek a čtvrtý sloupec. Výsledek je v desítkové soustavě 8, po převedení do binární je 1000.

Pozor! Každý S-box má odlišnou tabulku, tabulky pro všechny S-boxy naleznete [zde](https://en.wikipedia.org/wiki/DES_supplementary_material#Substitution_boxes_(S-boxes))

Jak jsem již zmínil, tak výsledek každého S-boxu je čtyř-bitové číslo, ale na wikipedii jsou hodnoty výsledků jednotlivých S-boxů v desítkové (decimální) soustavě. Takže ještě musíte čísla převést do binární. Pozor na to, když například výsledkem bude v desítkové soustavě `2`, tak v binární bude `0010`. Výsledek musí mít vždy **čtyři bity!**

Výsledkem substituce je 32 bitů.

#### [Permutace (P)](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#permutace-p)

32bitový výsledek z předchozích osmi S-boxů se přehází v finálním P-boxu. To z toho důvodu, aby po permutaci byly bity z jednotlivých S-boxů rovnoměrně rozprostřeny pro vstup do S-boxů v dalším opakování funkce F.

![](https://gitlab.com/H4nz11/haxagon_public/-/raw/main/crypto-symetric2/flowPermutation.png)

Opět se řídí tabulkou a funguje na identickém principu jako IP nebo FP. Udává, ze kterého bitu vstupu se bere bit výstupu. První buňka (levá, horní) značí první bit výstupu a obsah buňky udává, z kolikátého bitu vstupu se berou data.

|||||||||
|---|---|---|---|---|---|---|---|
|16|7|20|21|29|12|28|17|
|1|15|23|26|5|18|31|10|
|2|8|24|14|32|27|3|9|
|19|13|30|6|22|11|4|25|

Tabulku čtěte po řádcích. První bit výstupu se bere z 16. bitu vstupu, druhý bit výstupu se bere z 7. bitu vstupu... až poslední 32. bit výstupu se bere z 25. bitu vstupu.

### [Dešifrování](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#de%C5%A1ifrov%C3%A1n%C3%AD)

Krása symetrického algoritmu, jako je DES je v tom, že pro dešifrování stačí v podstatě udělat pouze všechny kroky pozpátku.

### [To be continued](https://haxagon.xyz/challenge/641abe6bcf76208fd29fed70/#to-be-continued)

V příští úloze se podíváme na kryptografické útoky na DES, jako třeba Deep Crack, jak NSA i IBM znalo techniky kryptoanalýzy, které byly veřejností objeveny až o mnoho let později a na nástupce DESu, jako Triple DES a dodnes používané AES.