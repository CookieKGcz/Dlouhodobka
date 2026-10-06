---
tags: [PV017, pojem]
aliases: [Útočník, Attacker model, Klasifikace útočníků, Insider, Outsider]
---

# Model útočníka

> [!summary] Definice
> Popis protivníka, proti kterému systém chráníme – jeho **cílů, metod, schopností, financování** a toho, zda je **insider nebo outsider**. Bez modelu útočníka nelze rozumně odhadnout pravděpodobnost [[Riziko|rizika]].

## Atributy protivníka (P1, s. 54)

1. **Cíle** – často naznačují cílová aktiva vyžadující zvláštní ochranu.
2. **Metody** – předpokládané techniky a typy útoků.
3. **Schopnosti** – výpočetní zdroje (CPU, úložiště, šířka pásma), dovednosti, znalosti, personál, **příležitosti** (např. fyzický přístup).
4. **Úroveň financování** – ovlivňuje odhodlání, metody a schopnosti.
5. **Outsider × insider** – outsider útočí bez předchozího přístupu; **insider má počáteční výhodu** (znalosti, oprávnění na nižší úrovni…).

## Klasifikace útočníků podle IBM (P1, s. 55)

| Třída | Typ | Znalosti a vybavení |
|---|---|---|
| **0** | script kiddies | bez znalosti systému, hotové nástroje, metoda pokus/omyl |
| **1** | chytří nezasvěcení útočníci | často velmi inteligentní, nedostatečné znalosti systému, středně sofistikované vybavení, využívají existující zranitelnosti |
| **1,5** | dobře vybavení lidé zvenku | dobré laboratorní vybavení a základní znalost systému (např. univerzitní laboratoře) |
| **2** | zasvěcení insideři | značné specializované vzdělání a zkušenosti, sofistikované nástroje |
| **3** | dobře finančně podporované organizace | týmy specialistů, dobré finance, detailní analýzy, nejlepší nástroje, **tvorba nových útoků** |

> [!info] Kontext
> Třída 3 odpovídá dnešním **APT** skupinám (státem podporovaným) – např. **APT31** atribuovaná v ČR 2025 ([[3 260929 - Přístup k regulaci KB|P3]]).

## Souvislosti

- Přednáška: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=54|s. 54–55]]
- Související: [[Hrozba]] · [[Riziko]] · [[Obecný model zabezpečování]]
