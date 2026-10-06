https://www.fi.muni.cz/~kas/pv065/pv065.pdf
# 2 Vývojové prostředí (pokračování)
## Sdílené knihovny
- Dynamicky linkované knihovny/moduly – kód přičleněný k programu až **po spuštění** (shared libs, plug-iny)
- Dynamický linker `/lib/ld.so` – první načtená knihovna, přičleňuje všechny další
### Ovládání dynamického linkeru
- `LD_LIBRARY_PATH` – adresáře oddělené `:`, kde hledat `.so`
- `LD_PRELOAD` – objekt přilinkovaný jako první (např. předefinování knihovní funkce)
	- u **set-uid / set-gid** programů linker tyto proměnné **ignoruje** (bezpečnost)
- `/etc/ld.so.conf`, `/etc/ld.so.conf.d/` – globální konfigurace
- `ldconfig(8)` – generuje symlinky podle verzí + cache
### Linkování v době kompilace vs. v době běhu
- **Compile-time** (Linux libc4/a.out, SunOS 4, SVr3)
	- knihovna leží na **pevné adrese** v adresním prostoru, za běhu se jen přimapuje
	- \+ rychlý start
	- − složitá výroba, nejde linkovat za běhu, omezený adresní prostor (4 GB na 32-bit pro všechny knihovny), problém s verzemi
- **Run-time – ELF** (Executable and Linkable Format; SVR4, Linux libc5+)
	- křížové odkazy řešeny až za běhu
	- **PIC** – position independent code
	- verze symbolů (libc6)
	- \+ plug-iny, možnost předefinovat symbol v knihovně
	- − pomalejší start, PIC potenciálně pomalejší (jeden registr = adresa začátku knihovny), nesdílitelné části kódu (viz `prelink(8)`)
### ldd – závislosti programu
```bash
$ ldd /usr/bin/vi
  libtermcap.so.2 => /lib/libtermcap.so.2.0.8
  libc.so.5 => /lib/libc.so.5.4.36
```
- `-d` – doplní křížové odkazy datových objektů a ohlásí chyby, `-r` – totéž i pro funkce
## Hlavičkové soubory
- rozhraní ke knihovnám (typové kontroly), konstanty (`NULL`, `stdin`, `EAGAIN`), makra (`isspace()`, `ntohl()`)
- jen **deklarace** prototypů, žádné definice funkcí
- umístění: `/usr/include` + podadresáře
- symboly začínající `_` = privátní symboly systému
## Ladění programu
- `-g` – symbolické ladicí informace
- **core** – obraz paměti procesu v době havárie → posmrtná analýza
	- lze vyvolat i uměle: signál `SIGQUIT` (Ctrl-\\)
	- pozor na `ulimit -c`, `systemd-coredump(8)`, `coredumpctl(1)`
- ladění běžícího procesu – služba jádra `ptrace(2)` + `/proc`
- `gdb` (CLI); front-endy cgdb, ddd, kdbg…; IDE eclipse, kdevelop, geany…

# 3 Normy API
## Přehled norem
- **ANSI C** (1989, X3.159-1989) – jazyk C + standardní knihovna (15 hlaviček: `stdlib.h`, `stdio.h`, `string.h`…)
	- nedefinuje procesy → jen základní přenositelnost
	- revize: C99 (`//` komentáře, inline), C11 (vlákna, atomické typy), C17 (jen upřesnění), C23
- **POSIX** (IEEE 1003, Portable Operating System Interface)
	- POSIX.1 – API UNIXu (rev. 2017), POSIX.2 – shell, POSIX.1b – real-time, POSIX.1c – vlákna
- **Single UNIX Specification** (The Open Group = OSF + X/Open)
	- SUSv1 1994 „UNIX 95“, SUSv2 „UNIX 98“, SUSv3 „UNIX 03“, SUSv4 2008 = POSIX:2008
	- zahrnuje POSIX.1 → **současná „definice UNIXu“**
- další: X/Open XPG3/4, FIPS 151, SVID (AT&T, System V), BSD
- kterou normu funkce splňuje → sekce *Conforming To* v manuálu
## Limity
- 3 druhy: **volby** při kompilaci (podporuje job control?), **limity při kompilaci** (max `int`?), **limity při běhu** (max délka jména souboru v tomto adresáři?)
- ANSI C – jen compile-time: `<limits.h>` (`INT_MAX`, `UINT_MAX`), `<float.h>`, `FOPEN_MAX` v `<stdio.h>`
### Detekce verze POSIX
```c
#define _POSIX_C_SOURCE 200809L   /* nebo _POSIX_SOURCE */
#include <unistd.h>
/* _POSIX_VERSION = verze normy, kterou systém splňuje */
```
- viz `feature_test_macros(7)`
### Run-time limity
```c
#include <unistd.h>
long sysconf(int name);                /* globální limity */
long pathconf(char *path, int name);   /* limity závislé na souboru */
long fpathconf(int fd, int name);
```
- `sysconf` – max. počet argumentů, počet CPU, velikost stránky, frekvence časovače…
- `[f]pathconf` – max. počet hard linků, max. délka jména souboru, velikost bufferu roury…
- odpovídající compile-time konstanty: `ARG_MAX`, `CHILD_MAX`, `PIPE_BUF`, `LINK_MAX`, `_POSIX_JOB_CONTROL`…

# 4 Program v uživatelském prostoru
## Start programu
1. linkování: `crt1.o` + objektové moduly + knihovny + libc
2. vstupní bod (dle binárního formátu, obvykle v `crt1.o`)
3. namapování a spuštění dynamického linkeru → sdílené knihovny
4. inicializace (konstruktory statických proměnných v C++, v GCC z `__main`)
5. nastavení globálních proměnných (`environ`)
6. volání `main()`
```c
int main(int argc, char **argv, char **envp);
```
- `argc` = počet argumentů + 1, vždy `argv[argc] == NULL`
- `envp` – pole `jméno=hodnota`
- přepsáním `argv[0]` lze ukládat stav procesu (vidět v `ps`) – nutné u programů s heslem na příkazové řádce
## Ukončení programu
- návratová hodnota jde **rodičovskému procesu**; 8-bit, `0` = úspěch, nenulová = chyba
- ukončení: návrat z `main()` nebo `exit(3)` / `_exit(2)`
```c
#include <stdlib.h>
void exit(int status);               /* EXIT_SUCCESS 0, EXIT_FAILURE 1 */
int atexit(void (*function)(void));  /* registrace úklidové funkce */
void abort(void);

#include <unistd.h>
void _exit(int status);
```
- `exit(3)` – **knihovní funkce**: zavolá funkce z `atexit(3)`, zavře soubory (vyleje stdio buffery), C++ destruktory → pak `_exit(2)`
- `_exit(2)` – **služba jádra**, okamžité ukončení procesu
- `abort(3)` – pošle `SIGABRT` → ukončení + core dump
61/373
