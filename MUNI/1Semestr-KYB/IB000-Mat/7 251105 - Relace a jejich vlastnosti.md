## Zopakování kartézského součinu a relace
### Definice:
- Kartézský součin dvou množin A, B definujeme jako množinu všech uspořádaných dvojic ze složek z A a B
$$A \times B = \{(a, b) \ a \in A,b \in B\}.$$
### Definice kartézského součinu více množin:
- Pro každé A; G N definujeme
$$A_{i} \times A_{2} \times \dots \times A_{k} = \{(a_{i}, a_{2}, \dots , a_{k}) | a_{i} \in A_{i}  \ pro \ každé \ 1 \leq i \leq k\}$$
• Například Z^3 = ZxZxZ = {(i, j, k) \ i, j, k \in Z}
Definice: Relace mezi množinami A_{1},A_{2}, . . . ,pro k \in N, je libovolná podmnožina kartézského součinu
$$R  \ podmnož \ A_{i} \times A_{2} \times \dots \times A_{k}$$
Pokud A_{1} = A_{2} = • • • = A_{k} = A, hovoříme o k-ární relaci R na A.
# Reprezentace konečných relací
- Ukládání dat - především sleduje vztahy mezi objekty (stejně jako relace).
	-> relační databáze jako obecná ukázka použití relace.
### Příklad 7.1. Tabulka relační databáze prezentuje obecnou relaci.
- Definujme následující množiny („elementární typy")
	- ZNAK = {a, • • • , z, A, • • • , Z, mezera},
	- ČÍSLICE = {0,1,2, 3,4, 5, 6, 7,8,9}.
- Dále definujeme tyto množiny („odvozené typy")
	- JMÉNO = ZNAK^15,     PŘÍJMENÍ = ZNAK^20,     VEK = ČÍSLICE^3,
	- ZAMESTNANEC „in" JMÉNO x PŘÍJMENÍ x VEK.
Relaci „typu" ZAMESTNANEC pak lze reprezentovat tabulkou:

| jméno     | příjmení | věk |
| --------- | -------- | --- |
| Jan       | Novák    | 42  |
| Petr      | Vichr    | 28  |
| Pavel     | Zíma     | 26  |
| Stanislav | Novotný  | 52  |
## Reprezentace binárních relací na množině
![[Pasted image 20251105181929.png]]
![[Pasted image 20251105182405.png]]
# Vlastnosti binárních relací na množině
![[Pasted image 20251105182619.png]]
![[Pasted image 20251105182633.png]]
## Ukázkové binární relace
### Příklad 7.3. Jak poznat vlastnosti relací z matice:
![[Pasted image 20251105183952.png]]
### Příklad 7.4. Několik příkladů relací definovaných v přirozeném jazyce.
![[Pasted image 20251105184637.png]]
# Uzávěry relací
![[Pasted image 20251105185616.png]]
![[Pasted image 20251105191554.png]]
![[Pasted image 20251105191624.png]]

# Tranzitivní relace
![[Pasted image 20251105191644.png]]
![[Pasted image 20251105191702.png]]
![[Pasted image 20251105191715.png]]