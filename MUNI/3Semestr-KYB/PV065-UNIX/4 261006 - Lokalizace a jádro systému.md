https://www.fi.muni.cz/~kas/pv065/pv065.pdf
# 4 Program v uživatelském prostoru (pokračování)
## Lokalizace (locales)
- přizpůsobení národnímu prostředí **bez rekompilace**, nastavitelné per uživatel i per kategorie
### Kategorie
| Kategorie     | Ovlivňuje                                     |
| ------------- | --------------------------------------------- |
| `LC_COLLATE`  | třídění řetězců                               |
| `LC_CTYPE`    | typy znaků (písmeno, číslice, velká/malá)     |
| `LC_MESSAGES` | jazyk vypisovaných zpráv (GNU gettext)        |
| `LC_MONETARY` | formát měny (symbol, umístění, desetinná místa) |
| `LC_NUMERIC`  | formát čísel (oddělovač desetin, tisícovek)   |
| `LC_TIME`     | formát času, názvy dnů a měsíců               |
### Názvy locales
- `jazyk[_teritorium][.charset][@modifikátor]` – jazyk dle ISO 639 (`cs`), teritorium dle ISO 3166 (`CZ`)
- např. `cs_CZ.UTF-8`, `cs`, `en_GB`, `de@EURO`
### Proměnné prostředí
- `LANG` – výchozí hodnota pro všechny kategorie
- `LC_*` – jednotlivé kategorie
- `LC_ALL` – přebíjí vše
- priorita: `LC_ALL` > `LC_*` > `LANG`
### Locales v C
```c
#include <locale.h>
char *setlocale(int category, char *locale);

setlocale(LC_ALL, "");   /* volat po startu – jinak platí locale "C" */
```
- `locale == NULL` → jen vrátí aktuální nastavení; `""` → nastaví podle proměnných prostředí
- `strcoll(3)` – jako `strcmp(3)`, ale podle `LC_COLLATE`
- `strxfrm(3)` – převede řetězec tak, aby šel porovnat obyčejným `strcmp(3)` (vyplatí se při opakovaném porovnávání)
- české třídění (ČSN): `č ř š ž ch` jsou samostatná písmena (ch za h), ostatní diakritika (á, ň, ť…) rozhoduje až sekundárně, velikost písmen až potom
	- plagiát < plachta < pláně < plánička < Plánička < plaňka < plankton < plášť < plat < plát
- `nl_langinfo(3)` – info o locale: `CODESET`, `D_T_FMT`, `DAY_1–7`, `MON_1–12`, `RADIXCHAR`, `YESEXPR`, `CRNCYSTR`…
### Katalogy zpráv
- pro `LC_MESSAGES`, GNU gettext; zdrojové `.po`, zkompilované `.mo`
```
msgid "Height of title bar."
msgstr "Výška titulku."
```
### Znakové sady
```c
#include <iconv.h>
iconv_t iconv_open(char *tocharset, char *fromcharset);
size_t iconv(iconv_t cd, char **inbuf, size_t *inleft, char **outbuf, size_t *outleft);
int iconv_close(iconv_t cd);
```
- cílové kódování + `//TRANSLIT` (transliterace) nebo `//IGNORE`; CLI `iconv(1)`
### Příkazová řádka
```bash
$ locale          # aktuální nastavení
$ locale -a       # dostupné locales
$ locale charmap  # UTF-8
$ locale mon      # leden;únor;březen;...
```
- `localedef(8)` – vytvoří binární podobu locale

# 5 Jádro systému
## Start systému
1. **Firmware** (ROM, na PC BIOS) – test HW, zavedení systému z média, často PROM monitor
2. **Primární zavaděč** – v boot bloku disku, pevná délka; na PC **MBR** (včetně tabulky oblastí) → zavede sekundární
3. **Sekundární zavaděč** – načte jádro a předá mu parametry; někdy CLI, umí číst FS; k zavedení používá firmware
- **UEFI** – jednoduchý OS: rozpozná partitions, VFAT, vlastní formát spustitelných souborů, EFI shell, EFI proměnné, secure boot (Linux: `grub.efi`, `linux.efi`)
### Parametry jádra
- systémová konzola, kořenový disk, parametry ovladačů; ostatní se předají do user-space – viz `bootparam(7)`
### Průběh inicializace jádra
1. virtuální paměť (co nejdřív)
2. konzola (příp. dvoufázově – `early_printk()`)
3. CPU, sběrnice (autokonfigurace), zařízení
4. **proces 0** (idle task / swapper / scheduler)
5. vlákna jádra (kflushd, kswapd…)
6. ostatní CPU + jejich idle procesy
7. připojení kořenového FS
8. **proces 1** – obvykle `/sbin/init` → dál už user-space
### Zařízení
- UNIX v7: blokové/znakové, **statické** tabulky `bdevsw[]`, `cdevsw[]`
- Linux: blokové/znakové/SCSI/síťové, **dynamické** tabulky; hot-plug (USB…)
- ovladač = funkce pro open/read/write/řídící operace + privátní data zařízení
### Iniciální ramdisk (initrd)
- načten sekundárním zavaděčem spolu s jádrem → jádro nemusí mít vestavěné ovladače (jen konzolu + FS ramdisku)
- na ramdisku se inicializují moduly a určí kořenový svazek → připojení root FS → init
- Linux: komprimovaný obraz FS nebo `cpio(1)` archív, skript `/linuxrc`
- bootovací zprávy: `dmesg(8)`, `/var/log/dmesg`
## Architektura jádra
- konfigurace: System V (`/etc/system`), BSD (`/sbin/config`), Linux (`make`, `.config`, `/proc/config.gz`)

| Typ             | Princip                                                                  | Pozn.                                                          |
| --------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------- |
| **Monolitické** | jeden soubor, všechny ovladače uvnitř, paměť sdílená všemi částmi jádra  | chyba jednoho ovladače může rozbít zbytek jádra                |
| **Mikrojádro**  | v jádře jen nutné minimum, zbytek jako procesy-servery (VM, zařízení, disky) | Mach, L4, minix, QNX; předávání zpráv → malá propustnost, velká latence |
| **Modulární**   | moduly přidávané za běhu (obdoba `.so` v user-space) – ovladače, FS, protokoly | Linux; definované rozhraní, ne oddělený adresní prostor        |

- Linux moduly: závislosti `depmod(8)`, dynamická registrace `register_chrdev()`, `register_blkdev()`, `register_netdev()`, `register_fs()`…; dohledání ovladače podle ID sběrnice (PCI ID)
- historie: Tanenbaum vs. Torvalds – „Linux is obsolete“ (1992)
## Procesy v jádře
- **kontext** = stav systému příslušný běhu jednoho procesu/vlákna; **přepnutí kontextu** = výměna běžícího procesu za jiný
- při startu běží kontext procesu 0 → později idle task (nesmí se zablokovat)
- Linux: `struct task_struct`, makro `current`
- pod jakým kontextem běží služby jádra?
	- UNIX – v **kontextu volajícího procesu**; proces má 2 režimy: user-space a kernel-space
	- mikrojádro – předá řízení jinému procesu (serveru)
	- v obou případech nutno řešit přístup do user-space (např. buffer u `write(2)`)
116/373
