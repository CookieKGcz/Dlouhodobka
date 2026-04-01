## Typický adresářový strom
- /unix, /bsd, /boot
	- Jádro OS
- /bin/ls, cp, sh
- /dev
	- Adresář speci. souborů
- /etc
	- konfig. souborů systémů
- /lib
	- knihovny
- /mnt
	- připojení dočasných systémů souborů
- /tmp
- /home
- /usr/bin, etc, lib, tmp
	- z kapacitních důvodů
- /usr/include
	- .h soubory pro překladače jazyka C
- /usr/man
- /usr/locla/bin, man, etc, lib
	- lokálně instalované
- /usr/sbin
	- Systémové programy určené zpravidla superuživateli
- /usr/X11, openwin
	- Okénkový systém
- /var
	- Adresář pracovních /admin/ souborů systému
- /var/mail
- /var/spool
	- Dočasné soubory systémových operací
- /var/adm
	- Záznamy o činnosti systému a uživatelů
- /var/tmp
- /var/preserve
	- Pracovní soubory editoru vi, které zůstávají při násilném ukončení editoru
## Přístupová práva
- V i-uzlu pro vyhodnocení přístupových práv jsou:
	- Vlastník souboru (UID)
	- Skupina vlastníka (GID)
	- přístupová práva
		- ve 12 bitech uloženy
- Ve výpisu ls -l
	- -rwx r-x r-x    1 novák student ...
- vlastník, skupina, ostatní
### Soubor
- r - číst
- w - zapisovat
- x - provést
### Adresáře
- r - vypsat
- w - zapisovat, (vytvářet a rušit)
- x - vstoupit
## Sticky bit
- aby soubor mohl zrušit pouze vlastník souboru nebo vlastník adresáře
- drwxrwxrw**t** 9 root root 2048 Mar 18 22:12 tmp
## Osmičkový popis práv:
- 4000 SUID
- 2000 SGID
- 1000 sticky bit
- 0400 r pro vlastníka
- 0200 w pro vlastníka
- 0100 x pro vlastníka
- ...
## Příkaz `umask`
- Zadávání implicitních přístupových práv pro vytváření souborů a adresářů
- interní příkaz shellu
-  `umask nnn`
## Příkaz `chmod`
- Nastavení přístupových práv
- who:
	- u, g, o, a (all)
- perm:
	- X je totéž jako x, ale aplikuje se pouze na adresáře nebo na soubory, které mají alespoň jeden bit x nastavený
- op:
	- + (přidává), - (odebírá), = (absolutní nastavení)
### Příklady použití `chmod`
- chmod go-w soubor
	- zakáže zápis pro skupinu a ostatní
- 644
	- nastaví rw-r--r--
- =rw,+X
	- nastaví `rw` podle `umask` a x pro všechny ugo tehdy, jeli soubor proveditelná alespoň pro jednoho z ugo nebo jde o adresář
- go=
	- smaže všechny bity pro `go`
- a+rwxt
	- typické nastavení pro veřejný pracovní adresář
- u+s
	- nastavení SUID
- g+s
	- nastavení SGID
## Další příkazy
- chown vlastník souboru/adresáře
- newgrp skupina
	- přihlášení do jiné skupiny
- chgrp skupina soubor
	- Změna skupiny nebo adresáře
	- Skupinu smí měnit vlastník souboru (pokud náleží do cílové skupiny) nebo superuž.
## ACL - access control lists
- `-rw-rw-r--+ 1 pv004labstud guestfi 11 27. úno 20.17 ukol_xxx`
# Shell
## Uživatelské rozhraní
- Známé:
	- sh - Bourne shell
	- csh - C-shell
	- ksh - Korn shell
	- bash - Bourne-again shell
- Bourne shell
	- 1979 Stephen Bourne
- Co je shell?
	- Shell je interpretační programový jazyk, Čte příkazy z terminálu nebo ze souboru a provádí je.
- Lexikální analýza příkazového řádku
	- Shell čte ze vstupu "slova" vzájemně oddělená "bílým místem" (mezera tab) a operátory:
		- Řídící operátory:
			- `& && ( ) ; ;; | || nový řádek`
		- Operátory přesměrování:
			- `< > >| << >> <& >& <<- <>`
## Řídící znaky:
- Obrácené lomítko (backslash):
	- na normální znak
- Apostrof
	- mezi ztrácejí svůj řídící význam (vyjma ')
- Uvozovky
	- -||- (vyjma $, ' (obrácený apostrof), \\ (jen takto: `\$ \'(ale norm ubozovky) \" \\ \nový řádek`))
## Přesměrování vstupu a výstupu
- Shell přesměrování - propojení zajistí před provedením příkazu
- File descriptor number (n)
	- příkaz n> soubor
	- příkaz n< soubor
- Každá proces má nastaveno:
	- 0 tzv. standardní vstup
	- 1 tzv. standardní výstup
	- 2 tzv. standardní chybový výstup
- Implicitní varianty:
	- 1>  ==  >
	- 0<  ==  <
- Přesměrování vstupu:
	- příkaz n< soubor
- Přesměrování výstupu:
	- příkaz n> soubor
## Spojování příkazů do kolon
- příkaz | příkaz2 \[ | příkaz3 ... ]
	- roura
- Zápisem "! příkaz | příkaz2 \[ | příkaz3 ... ]"
	- se ukončí kód kolony neguje
- Zápisem "příkaz1 2 > &1 | příkaz2"
	- se na standardní vstup příkazu 2 předá jak standardní výstup, tak i stand. výstup příkazu1
- Asynchronně přes &
## Job control
- Jak dostat úlohu pod správu Job Control?
	- Spustíme li úlohu na pozadí (&), vypíše se identifikace:
		- ping aisa > /dev/null &
		- \[1] 1234
		- Číslo úlohy je 1 a má top-level proces 1234
	- Běží li úloha normálně spuštěná na popředí a cheme s ní nějak naložit, -> znak "susp".
		- ping aisa > /dev/null
		- \^Z
		- \[2]+ Stopped  ping aisa > /dev/null
### Job control - příkazy
- jobs - vypíše seznam řízených úloh
- fg \[job] - úloha se spustí na popředí
- bg \[job] - na pozadí
- kill \[signál job ...] - pošle signál úloze
- wait \[job] - Zahájí čekání na dokončení úlohy a převezme její ukončovací kód.
## Seznamy
- rozumíme posloupnost žádného nebo více příkazů oddělených novým řádkem, středníkem nebo ampersandem &
- Shell příkazy provádí v pořadí, v jakém jsou zapsány
- Pokud zápis končí ampersandem, ihned se zahájí provádění následujícího
- Návratový kód seznamu je návratový kód posledního prováděného procesu
- Příkazy lze oddělovat operátory && a ||.
	- && = druhý příkaz provede pouze tehdy, pokud ukončovací kód předchozího byl 0
	- || = ... nenulový
## Substituce příkazů
- 