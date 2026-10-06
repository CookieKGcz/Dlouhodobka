https://www.fi.muni.cz/~kas/pv065/pv065.pdf
# 4 Program v uživatelském prostoru (pokračování)
## Argumenty příkazové řádky
- konvence: `-lt` (písmena), `-f x.sed` (s argumentem), `--` (konec přepínačů), `--full-time`, `--color never`, `--color=never`
- soubor `-Z` smažu: `rm -- -Z` nebo `rm ./-Z`
### getopt
```c
#include <unistd.h>
int getopt(int argc, char **argv, char *optstring);
extern char *optarg;
extern int optind, opterr, optopt;
```
```c
while ((c = getopt(argc, argv, "ab:")) != -1) {
	switch (c) {
	case 'a': opt_a = 1; break;
	case 'b': option_b(optarg); break;   /* "b:" = -b má argument */
	case '?': usage();
	}
}
```
- `:` za písmenem → přepínač vyžaduje argument (v `optarg`)
- vrací `-1` po posledním přepínači; `optind` = index prvního nepřepínačového argumentu
- dlouhé přepínače: `getopt_long(3)` (`<getopt.h>`, pole `struct option`)
- knihovna POPT – modulární, reentrantní, uživatelské aliasy přepínačů
## Chyby služeb jádra
- při chybě vrací `-1` nebo `NULL`, důvod v globální proměnné **`errno`** (`<errno.h>`)
- konstanty viz `errno(3)`, možné chyby konkrétní služby → její manpage
- `errno` platí jen do příští chyby → kontrolovat hned po volání
```c
retry: if (somesyscall(args) == -1) {
	switch (errno) {
	case EACCES: permission_denied(); break;
	case EAGAIN: sleep(1); goto retry;
	case EINVAL: blame_user(); break;
	}
}
```
### Textový popis chyby
```c
#include <stdio.h>
void perror(char *msg);   /* "msg: No such file or directory" */

#include <string.h>
char *strerror(int errnum);
int strerror_r(int errnum, char *buf, size_t len);   /* reentrantní */
```
## Proměnné prostředí
- pole řetězců `jméno=hodnota`; přístup přes 3. argument `main()` nebo globální `environ`
```c
#include <stdlib.h>
char *getenv(char *name);
int putenv(char *str);                              /* "PROMENNA=hodnota" */
int setenv(char *name, char *value, int rewrite);   /* rewrite != 0 → přepíše existující */
int unsetenv(char *name);
int clearenv();                                     /* není v POSIX.1-2001 */
```
- `putenv` řetězec nekopíruje – stane se přímo součástí prostředí (nepředávat lokální proměnnou)
## Dynamická paměť
```c
#include <stdlib.h>
void *malloc(size_t size);                 /* ≥ size bajtů, neinicializováno */
void *calloc(size_t nmemb, size_t size);   /* nmemb × size, vynulováno */
void *realloc(void *ptr, size_t size);     /* může přesunout data! */
void free(void *ptr);
```
- vrácený ukazatel je **zarovnán** pro libovolný typ (nezarovnaná proměnná by mohla ležet přes hranici slova)
- po `realloc` **nepoužívat původní ukazatel**
- pozor: některé systémy neakceptují `free(NULL)`
### alloca – alokace na zásobníku
```c
#include <alloca.h>
void *alloca(size_t size);
```
- uvolní se automaticky po návratu z funkce, **nelze `free()`**, specifické pro kompilátor
- (stack clash – třída bezpečnostních chyb)
### brk / sbrk – nízkoúrovňová alokace
```c
#include <unistd.h>
int brk(void *end_of_data_segment);
void *sbrk(int increment);
```
- nastavení velikosti datového segmentu – používá je `malloc(3)`
- většina implementací `malloc` neumí vrátit uvolněnou paměť zpět OS
### Typické chyby
- uvolnění nealokované paměti, vícenásobné uvolnění (double free), přetečení/podtečení, použití po `realloc`
- těžko se detekují → Electric Fence (využívá MMU, i jako `LD_PRELOAD`), Valgrind, vestavěné kontroly v glibc
## Nelokální skoky
- jako `goto` přes hranice funkcí – vyskočení z vnořených funkcí (např. při fatální chybě)
```c
#include <setjmp.h>
int setjmp(jmp_buf env);                /* uloží návratové místo, poprvé vrací 0 */
void longjmp(jmp_buf env, int retval);  /* skok zpět do setjmp, ten teď vrátí retval */
```
- `jmp_buf` obsahuje návratovou adresu a vrchol zásobníku
```c
jmp_buf env;
int main() {
	if (setjmp(env) != 0)
		dispatch_error();
	/* ... */
	somewhere_else();
}
void somewhere_else() {
	if (fatal_error)
		longjmp(env, errno);
}
```
## Dynamické linkování za běhu (libdl)
- přidávání kódu za běhu (plug-iny), linkovat s `-ldl` (v glibc ≥ 2.34 už součást libc)
```c
#include <dlfcn.h>
void *dlopen(char *file, int flags);     /* přidá objekt, vyřeší odkazy, zavolá _init */
void *dlsym(void *handle, char *symbol); /* adresa symbolu */
int dlclose(void *handle);               /* počítadlo použití, zavolá _fini */
char *dlerror();                         /* text poslední chyby */
```
- `flags` – **právě jedno** z:
	- `RTLD_NOW` – odkazy vyřešit hned, chyba při nedefinovaných symbolech
	- `RTLD_LAZY` – řeší se až při použití (jen funkce)
	- volitelně `| RTLD_GLOBAL` – symboly k dispozici i později linkovaným objektům
```c
void *knihovna = dlopen("/lib/libm.so", RTLD_LAZY);
double (*kosinus)(double) = dlsym(knihovna, "cos");
printf("%f\n", (*kosinus)(1.0));
dlclose(knihovna);
```
86/373
