graf - ==speciální případ binárních relací==
- vrcholy - nodey
- spojení - hrana
- ![[Pasted image 20251126180308.png | 300]]
## Definice grafu
- Graf je uspořádaná dvojice $G = (V,E)$, kde $V$ je konečná množina vrcholů a $E$ je množina hran - množina vybraných dvouprvkových podmnožin množiny vrcholů.
- ![[Pasted image 20251126180455.png | 200]]
- ![[Pasted image 20251126180510.png | 500]]
## Stupně vrcholů v grafu
- Stupeň vrcholu $v$ v grafu $G$ rozumíme počet hran vycházejících z $v$. Stupeň $v$ v grafu $G$ značíme $d_{G}(v)$.
- ![[Pasted image 20251126181116.png | 500]]
- Definice: Graf je d-regulární, pokud všechny jeho vrcholy mají stejný stupeň $d$.
- Značení: Nejvyšší stupeň v grafu $G$ značíme:
	- ![[Pasted image 20251126181351.png | 150]]
### Věta 10.3
- ==Součet stupňů v grafu je vždy sudý, roven dvojnásobku počet hran.==
## Běžné typy grafů
- **Kružnice délky** $n$ má $n \geq 3$ různých vrcholů spojených "do jednoho cyklu" $n$ hranami:
- ![[Pasted image 20251126181709.png | 350]]

- **Cesta délky** $n \geq 0$ má $n + 1$ různých vrcholů spojených "za sebou" $n$ hranami:
- ![[Pasted image 20251126181801.png | 400]]

- Úplný graf n $n \geq 1$ vrcgolech má n různých vrcholů spojených po všech dvojicích (tj. celkem (n nad 2) hran)
- ![[Pasted image 20251126182116.png | 350]]

- Úplný bipartitní graf na m >= 1 a n >= 1 vrcholech má m + n vrcholů ve dvou skupinách (paritách), přičemž hranami jsou spojeny všechny m * n dvojice z různých skupin:
- ![[Pasted image 20251126182256.png | 350]]

- Hvězda s n >= rameny je zvláštní název pro úplný bipartitní graf K_1,n:
- ![[Pasted image 20251126182348.png | 350]]

### Zmínka o zobecnění grafech
![[Pasted image 20251126182420.png | 500]]
## Podgrafy a isomorfismus
- Definice:
- ![[Pasted image 20251126182621.png | 500]]
## Stejnost grafů a isomorfismus
![[Pasted image 20251126182829.png | 500]]
## Vlastnosti isomorfismu
![[Pasted image 20251126183308.png | 500]]
![[Pasted image 20251126184147.png | 500]]
## Důsledek: Stejnost grafů jako isomorfismus!
![[Pasted image 20251126184927.png | 500]]

## Další (pod)grafové pojmy
![[Pasted image 20251126185116.png | 250]]
![[Pasted image 20251126185133.png | 500]]
## Jak poznat neisomorfní grafy
![[Pasted image 20251126190202.png | 500]]
## Souvislost a komponenty
![[Pasted image 20251126190451.png | 500]]
![[Pasted image 20251126191023.png | 500]]
### Komponenta souvislosti
![[Pasted image 20251126191159.png | 500]]
### Souvislost
![[Pasted image 20251126191307.png | 500]]
## Základy orientovaných grafů
![[Pasted image 20251126191452.png | 500]]
![[Pasted image 20251126191546.png | 500]]
### Souvislost na orientovaných grafech (slabá)
![[Pasted image 20251126191823.png | 500]]
![[Pasted image 20251126192155.png | 500]]
### Souvislost na orientovaných grafech (silná)
![[Pasted image 20251126192230.png | 500]]
![[Pasted image 20251126192530.png | 500]]
## Dodatek: 7 mostů jedním tahem
![[Pasted image 20251126193140.png | 500]]
## Sled a tah v grafu
![[Pasted image 20251126193518.png | 500]]
## Eulerovské grafy
![[Pasted image 20251126193558.png | 500]]