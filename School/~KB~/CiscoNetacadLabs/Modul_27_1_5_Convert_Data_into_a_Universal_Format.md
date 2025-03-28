## PART1
(username: analyst / password: cyberops)
c)
![[Pasted image 20250321092905.png]]

![[Pasted image 20250321092840.png]]
![[Pasted image 20250321092946.png]]

Were the Unix Epoch timestamps converted to Human Readable format? Were the other fields modified? Explain.
- Ano, byly. Jediné co se změnilo byl 3 sloupec, který byl konvertován do normální podoby


Compare the contents of the file and the printed output. Why is there the line, ||Wed 31 Dec 1969 07:00:00 PM EST?
- pravděpodobně, protože je uložený new-line v originálním soubor, který se bral defaultně jako začátek?
![[Pasted image 20250321093928.png]]

d)
![[Pasted image 20250321094202.png]]
Smazali jsme new-line, takže output už je správný

e)
![[Pasted image 20250321094320.png]]
What was printed by the command above? Is this expected?
- ano, jelikož jsme output commandu vložili do souboru applicationX_in_human.log

## Part 2
![[Pasted image 20250321094955.png]]
a)
In the context of timestamp conversion, what character would work as a good delimiter character for the Apache log file above?
- mezera
How many columns does the Apache log file above contain?
 - 7
In the Apache log file above, what column contains the Unix Epoch Timestamp?
- 4
b)
![[Pasted image 20250321095117.png]]
c + d)
![[Pasted image 20250321095414.png]]
- output se změnil v timestampu jak bylo určeno, ale jejich obsah je chybný
- ne, pravděpodobně kvůli závorkám \[], protože je asi potřeba čistý text

e)
![[Pasted image 20250321095910.png]]
f) 
Was the script able to properly convert the timestamps this time? Describe the output
- Ano, teď máme dva printy první nekonvertlý s odstraněnými závorky a druhý už konvertlý

## Part3
![[Pasted image 20250321100640.png]]
![[Pasted image 20250321100952.png]]
For each one of the tools listed above, describe the function, importance, and placement in the security analyst workflow.
### Elasticsearch
- Function: "search and analytics engine" (built on Apache Lucene). ukládá a indexuje logy z různých zdrojů
- Importance: Efektivně ukládá a vyhledává velké objemy logů. Podporuje analýzu bezpečnostních dat v reálném čase. Umožňuje bezpečnostním týmům odhalovat anomálie a korelace mezi událostmi.
- Placement: úložistě a vyhledávání (logy z firewallů, IDS/IPS systémů... jsou indexovány v Elasticsearch -> umožňuje rychlejší vyhledávání)
### Logstash
- Function: nástroj pro zpracování dat, který shromažďuje, upravuje a přeposílá logy z různých zdrojů
- Importance: Čistí a strukturuje surová bezpečnostní data pro lepší analýzu. Obohacuje logy o další informace (např. reputace IP adres, geolokace).
- Placement: zpracování a sběr dat (předzpracování logů (před elsticsearch))
### Kibana
- Function: nástroj pro vizualizaci a tvorbu dashboardů -> Poskytuje vizuální analýzu v reálném čase, přehledné dashboardy a možnosti alertingu.
- Importance: Pomáhá bezpečnostním analytikům vizualizovat hrozby. Umožňuje efektivní reakci na incidenty díky identifikaci vzorců útoků. Podporuje proaktivní vyhledávání hrozeb pomocí dotazů a automatických upozornění.
- Placement: Vizualizace a analýza (plus monitoring)


