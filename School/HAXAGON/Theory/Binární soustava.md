## [Jak počítače ukládají data](https://haxagon.xyz/challenge/65d496a031563c5830987951#jak-po%C4%8D%C3%ADta%C4%8De-ukl%C3%A1daj%C3%AD-data)

Když se bavíme o tom, jak počítače ukládají data, musíme se podívat na jejich základní "jazyk" – jedničky a nuly neboli binární soustavu.

A proč vlastně počítače používají jedničky a nuly? To protože elektrické součástky, jako například tranzistory, mohou snadno rozpoznat a manipulovat pouze se dvěma stavy – **zapnuto** nebo **vypnuto**. Jednička znamená zapnuto a nula znamená vypnuto.

Než se vrhneme na binární soustavu, vysvětleme si, jak funguje číselná soustava, kterou všichni dobře známe a používáme denně – decimální soustava. Díky ní se naučíte základní principy, které Vám umožní lépe pochopit i ostatní typy soustav.

## [Decimální soustava](https://haxagon.xyz/challenge/65d496a031563c5830987951#decim%C3%A1ln%C3%AD-soustava)

Decimální neboli desítková soustava, jak název naznačuje, se skládá z **deseti** symbolů - `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` – které se různě opakují, aby vyjadřovali číselné hodnoty.

Vezměte si pro příklad číslo 472472. Intuitivně víte, že:

- Číslice 44 úplně vlevo znamená "čtyři sta",
- Číslice 77 uprostřed znamená "sedmdesát",
- Číslice 22 úplně vpravo znamená "dva".

Když všechny hodnoty sečtete (400+70+2400+70+2), dostanete konečný výsledek 472472.

Dvojka byla na pozici jednotek, sedmička na pozici desítek a čtyřka na pozici stovek.

Pozice udávají řády (jednotky, desítky, stovky tisíce...), ==přičemž nejnižší řád je vpravo a každý další==, vždy ==desetkrát vyšší==, řád je o pozici dále vlevo. Číslice na jednotlivých pozicích udávají kolikrát se daný řád vynásobí.

Celková hodnota čísla je pak součtem dílčích **násobků příslušné mocniny deseti**.

- Násobek je tedy číslo (0-9), které se nachází na dané pozici.
- Pozice je stupeň mocniny (v desítkové soustavě je to stupeň mocniny čísla deset).
- Nejnižší pozice (úplně vpravo) odpovídá jednotkám, protože první mocnina, na kterou desítku umocňujeme je nula. Tedy začínáme deseti na nultou (100100) a výstupem budou jednotky, protože cokoliv umocněno na nultou je 11.

Číslo 472472 je také možné zapsat jako 4×102+7×101+2×1004×102+7×101+2×100.

|4|7|2|
|---|---|---|
|4×1024×102|7×1017×101|2×1002×100|
|400|70|2|

Po sečtení 400+70+2400+70+2 je výsledkem číslo 472472.

## [Binární soustava](https://haxagon.xyz/challenge/65d496a031563c5830987951#bin%C3%A1rn%C3%AD-soustava)

Teď, když jsme se podívali na to, jak funguje stará známá desítková soustava, se pojďme podívat na počítači oblíbenou – binární soustavu.

Binární – dvojková – soustava je založena na použití pouze dvou symbolů `0` a `1`.

Všechno platí velmi podobně jako u decimální soustavy, pouze s jedinou změnou: kde byla `10` je teď `2`.

Celková hodnota čísla je pak součtem dílčích **násobků příslušné mocniny dvou**.

- Násobek je tedy číslo (v tomto případě číslo 0 nebo 1), které se nachází na dané pozici.
- Pozice je stupeň mocniny (ve dvojkové soustavě je to stupeň mocniny čísla dva).
- Nejnižší pozice (úplně vpravo) opět odpovídá jednotkám, protože první mocnina, na kterou dvojku umocňujeme je nula. Tedy začínáme dvěma na nultou (2020) a výstupem budou opět jednotky, protože cokoliv umocněno na nultou je 1. Dalším řádem budou dvojky, čtyřky, osmičky, šestnáctky…

Například číslo `1101` (v binární soustavě) můžete rozložit na 1×23+1×22+0×21+1×201×23+1×22+0×21+1×20.

|1|1|0|1|
|---|---|---|---|
|1×231×23|1×221×22|0×210×21|1×201×20|
|8|4|0|1|

Což je 8+4+0+18+4+0+1, v desítkové soustavě číslo 1313.

Jednoduše řečeno, každá číslice v binární soustavě určuje, zda se daná mocnina čísla 2 v dané pozici vyskytuje, či nikoliv. Binární soustava se používá v počítačích kvůli tomu, že počítačové komponenty, jako jsou tranzistory, diskové jednotky atd., mohou snadno rozpoznat a manipulovat s pouze dvěma stavy – zapnuto a vypnuto. To činí binární soustavu ideální pro ukládání a manipulaci s daty v počítačových systémech.

### [Bit vs Byte](https://haxagon.xyz/challenge/65d496a031563c5830987951#bit-vs-byte)

S těmito termíny jste se už mohli setkat, například když domlouváte rychlost internetu nebo když kupujete nový telefon a řešíte jeho kapacitu.

#### [Bit](https://haxagon.xyz/challenge/65d496a031563c5830987951#bit)

Bit je jednociferné binární číslo, tedy nejmenší možná jednotka. Je buďto `1` nebo `0`.

Značí se **malým** `b`, takže například 10 bitů je `10b`.

V dnešní době se už bitů a bytů používá tolik, že místo toho, abychom řekli například jeden tisíc bitů, radši řekneme jeden kilobit (**1kb**).

Zde je tabulka násobků jednotky bit:

|Počet bitů|Slovy|Zkratkou|
|---|---|---|
|1 bit|1 bit|1b|
|1 000 bitů|1 kilobit|1kb|
|1 000 000 bitů|1 megabit|1Mb|
|1 000 000 000 bitů|1 gigabit|1Gb|

#### [Byte](https://haxagon.xyz/challenge/65d496a031563c5830987951#byte)

Byte _(čteme [bajt])_ je osm bitů, například `10110001`. To je jeden byte s hodnotou `177` v decimální soustavě.

Značí se **velkým** `B`, takže například 10 bytů je `10B`.

Zde je tabulka násobků jednotky byte:

|Počet bytů|Slovy|Zkratkou|
|---|---|---|
|1 byte|1 byte|1B|
|1 000 bytů|1 kilobyte|1kB|
|1 000 000 bytů|1 megabyte|1MB|
|1 000 000 000 bytů|1 gigabyte|1GB|

### [Převod mezi binární a decimální soustavou](https://haxagon.xyz/challenge/65d496a031563c5830987951#p%C5%99evod-mezi-bin%C3%A1rn%C3%AD-a-decim%C3%A1ln%C3%AD-soustavou)

Na začátku jsme si decimální i binární soustavu dopodrobna vysvětlili. Teď je čas přetvořit teorii v praxi.

#### [Z binární do decimální](https://haxagon.xyz/challenge/65d496a031563c5830987951#z-bin%C3%A1rn%C3%AD-do-decim%C3%A1ln%C3%AD)

Postup si vysvětlíme na jednom příkladu: cílem je převést číslo `1101` z binární soustavy do decimální.

To, jestli začnete zprava či zleva, je na Vás, ale zprava se snadněji dopočítávají exponenty mocnin. Princip je takový, že k jednotlivým bitům přiřadíte jejich hodnoty a ty spolu sečtete. Samozřejmě sčítejte pouze ty bity, které mají hodnotu `1`.

|1|1|0|1|
|---|---|---|---|
|1×231×23|1×221×22|0×210×21|1×201×20|
|8|4|0|1|

Což je 8+4+0+18+4+0+1, v desítkové soustavě číslo 1313.

#### [Z decimální do binární](https://haxagon.xyz/challenge/65d496a031563c5830987951#z-decim%C3%A1ln%C3%AD-do-bin%C3%A1rn%C3%AD)

Opět si postup vysvětlíme na příkladu: cílem je převést číslo `13` z decimální soustavy do binární.

Nejjednodušší způsob převodu je opakované dělení dvěma.

- Číslo v desítkové soustavě vydělte dvěma a zaznamenejte zbytek.
- Opakujte tento postup do té doby, až výsledkem bude 0.
- Výsledky získané z těchto zbytků (odspoda nahoru) tvoří binární číslo.

13÷2=613÷2=6 (zbytek **1**)

6÷2=36÷2=3 (zbytek **0**)

3÷2=13÷2=1 (zbytek **1**)

1÷2=01÷2=0 (zbytek **1**)

Zapište zbytky odspoda nahoru a tím Vám vznikne výsledek `1101`.

### [Aritmetické operace](https://haxagon.xyz/challenge/65d496a031563c5830987951#aritmetick%C3%A9-operace)

I s binárními čísly se dají provádět aritmetické operace. Pokud umíte sčítat a odečítat pod sebou, tak Vám to nebude dělat žádný problém.

#### [Sčítání](https://haxagon.xyz/challenge/65d496a031563c5830987951#s%C4%8D%C3%ADt%C3%A1n%C3%AD)

Budeme sčítat dvě čísla, například `1101` + `1001`. Napište si je pod sebe

```
   1101
 + 1001
```

Začněte s nejnižšími řády (pravými) a postupně se posouvejte k řádům vyšším. Je důležité si všimnout, že pokud dochází k přetečení (když se sečte `1` + `1`), zapisujete `0` a přenášíte `1` na další pozici nalevo.

1. Vezměte bity na nejnižších pozicích obou čísel `1` a `1` a sečtěte je. Zde dojde k přetečení, protože nejvyšší hodnota, kterou může mít jeden bit je `1`. Výsledkem je tedy `10` – **zapíšete `0`** a jedničku přenesete na další pozici.
    
2. Na druhém řádu jsou bity `0` a `0`, jejichž součet je také `0`. Z předchozího kroku je ale nutné přidat přetečenou `1`, takže **zapíšete `1`**.
    
3. Na třetím řádu jsou bity `1` a `0`, ty opět sečtěte, výsledek je `1` a přetečení nenastane. **Zapíšete `1`**.
    
4. Na čtvrtém řádu jsou bity `1` a `1`, které opět sečtěte. Zde dojde k přetečení a výsledkem je `10`. Vzhledem k tomu, že už jste na konci obou čísel, **zapište `10`**.
    

Celkový výsledek je `10110`, což si můžeme ověřit i v decimální soustavě: `1101` (13) + `1001` (9) = `10110` (22).

Tady vidíte, že stačí dodržet principy sčítání pod sebou a pouze pamatovat na to, že se nacházíte v binární soustavě.

#### [Odečítání](https://haxagon.xyz/challenge/65d496a031563c5830987951#ode%C4%8D%C3%ADt%C3%A1n%C3%AD)

Jestli už umíte sčítat, tak odečítání je vlastně to stejné. Stačí si vzpomenout, jak funguje odečítání pod sebou v desítkové soustavě a principy přenést do binární.