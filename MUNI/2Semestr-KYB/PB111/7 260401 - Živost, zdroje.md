# 7 
## 7.1 Živost
### 7.1.1 Globální entity
- rozsah platnosti = celý program
- "nesmrtelné" objekty
- globální proměnné (objekty)
- podprogramy
### 7.1.2 Lexikální živost
- lokální proměnné, parametry
- živost ~ rozsah platnosti
- jednoduché ale omezující
- poslední vytvoření zanikne první
### 7.1.3 Dynamická živost
- živost není staticky vymezena
- rozhoduje se za běhu
	- např. v podmíněném příkazu
- významný zdroj chyb
### 7.1.4 Vlastnictví
- entita A vlastní entitu B v případě, kdy je A odpovědná za živost B.
## 7.2 Zdroje
### 7.2.1 Objekt vs zdroj
- zdroj je zobecnění objektu
- abstrakce entity s živostí
- vznik, použití, zánik
	- paralela s objektem
### 7.2.2 Odkaz na instanci
- zobecnění ukazatele
- různé reprezentace
	- celé číslo
		- ukazatel (např. void \*)
### 7.2.3 Zdroje a živost
- Zdroj žije ometenou dobu
- odkazy mohou zdroj "přežít"
- vzniká neplatný odkaz
- -> porušení vstupní podmínky
### 7.2.4 Ruční správa zdrojů
- vznik a zánik řídí programátor
- voláním vyhrazených podprogramů
- triviální implementace
- vyžaduje striktní disciplínu
### 7.2.5 Příklady zdrojů
- otevřený soubor open, close
- dynamická paměť malloc, free
- g_tree_new, g_tree_destroy
- glGenTextures, glDeleteTextures
- pthread_mutex_lock/\_unlock
### 7.2.6 Pseudolexikální živost
- lexikální živost je přirozená
- syntaktické párování vzniku/zániku
- pozor na řízení toku
	- break / continue
	- return uprostřed těla
### 7.2.7 Automatický úklid
- angl. garbage collector, GC
- vyšší jazyky (Python, Java, ...)
- uvolňuje již nepotřebné zdroje
- vyžaduje spolupráci překladače
### 7.2.8 Počítání odkazů
- abychom měli jistotu musíme znát počet odkazů na zdroj
	- navázáno na živost odkazů
- ang. reference count, refcount
- dojde-li na nulu, zdroj uvolníme
### 7.2.9 Konzervativní úklid
- adaptace automatického úklidu
- bez součinnosti překladače
- možno i v C (knihovna)
	- pouze pro objekty
- korektní ale neúplné
### 7.2.10 Složitost
- pro libovolný zdroj
	- počet souběžných instancí
- analogie s pamětí
- lze vyjádřit asymptoticky
- mnoho zdrojů limitováno O(1)
### 7.2.11 Zdroje vs automatický úklid
- úklid není deterministický
- těžké zaručit O(1)
- with v Pythonu
- C++/RAII, Rust
## 7.3 Problémy, chyby a jejich klasifikace
### 7.3.1 Použití neplatného odkazu
- konec živosti objektu
- odkazy dále existují
	- jsou již ale neplatné
	- mrtvý zdroj nesmí být použit
- koordinace je kritická
### 7.3.2 Dvojité zničení
- speciální případ předchozího
- je-li reprezentace recyklovaná
	- uvolní jiný objekt
	- problém se propaguje dál
### 7.3.3 Únik zdroje
- zdroj nebyl zničen
	- striktně - už nebude použit
	- volně - neexistuje odkaz
- situačně závislé
	- použití může být zbytečné
### 7.3.4 Prevence
- jasné vymezení platnosti zdroje
	- pseudolexikální živost
- zapouzdření + invarianty
- statická analýza (automatická)
### 7.3.5 Detekce
- specializované nástroje
- paměť: valgrind, addrsan
- otevřené soubory: valgrind
- profiler využití paměti
### 7.3.6 Problémy GC
- neřeší všechny problémy
	- únik zdroje vs únik odkazu
- méně paměťové efektivní
- pozastavení programu