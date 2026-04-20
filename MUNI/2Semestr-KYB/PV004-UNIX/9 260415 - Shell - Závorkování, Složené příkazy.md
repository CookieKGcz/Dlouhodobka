- (seznam)
	- Posloupnost příkazů seznam se provede ve vnořeném shellu
	- Tzn. že proměnné nastavené uvnitř závorek se po opuštěšní pravé závorky ztrácejí
- { seznam;}
	- Posloupnost příkazů 'seznam' se provede v aktuálním shellu
## Složené příkazy
```sh
for jméno [ in slovo ] do seznam; done
```
- příkaz expanduje 'slovo' a postupně vytvářet položky přiřazuje proměnné 'jméno' a provádí posloupnost příkazů 'seznam'
- Není li 'in slovo;' zadáno, potom se 'seznam' provede pro každý poziční parametr.
- Příklady:
```sh
for JMENO in *; do echo $JMENO; done
for POLOZKA in a b c d
	do
		echo $POLOZKA
done
```
```sh
echo Zadej akci a soubor:
read AKCE SOUBOR
case $AKCE in
	smaz|remove|delete) rm $SOUBOR;;
	vytvor|create) touch $SOUBOR;
					chmod 777 $SOUBOR;;
esac
```

```sh
if seznam; then seznam; [ elif seznam; then seznam; ] ...
[ else seznam; ] fi
```
- Provede se 'if seznam;', Pokud jeho návratový kód je nulový (OK), provede se 'then seznam;'. Jinak se provede 'elif seznam;' nebo 'else seznam;'.

```sh
while seznam; do seznam; done
until seznam; do seznam; done
```
- Seznam 'do seznam;' se provádí tak dlouho, dokud je návratový kód:
	- 'while seznam;' nulový
	- 'until seznam;' nenulový

```sh
break [n]
```
- Ukončí n-tou úroveň cyklu for, while, until.

```sh
continue [n]
```
- Zahájí další iteraci cyklu.

```sh
true
```
- Návratový kód vždy 0 (false opačně)

- Příklad: Použití while a read pro čtení dat ze souboru:
```sh
while IFS=: read LOG PAS NUID NGID NAM HOM SHE
do
echo $NUID $LOG
done < /etc/passwd
0 root
1 bin
2 daemon
3 adm
...
```
