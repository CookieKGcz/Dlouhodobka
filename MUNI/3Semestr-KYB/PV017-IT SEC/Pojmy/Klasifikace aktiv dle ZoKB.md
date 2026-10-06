---
tags: [PV017, pojem]
aliases: [Hodnocení aktiv, Klasifikace aktiv, Stupnice důvěrnosti, Stupnice integrity, Stupnice dostupnosti]
---

# Klasifikace (citlivých) aktiv dle ZoKB

> [!summary] Myšlenka
> Aktiva se hodnotí **zvlášť z hlediska důvěrnosti, integrity a dostupnosti** na čtyřstupňové škále **nízká – střední – vysoká – kritická**. Úroveň určuje, jak silná opatření/mechanismy jsou nutná.

## Důvěrnost

| Úroveň | Popis | Ochrana |
|---|---|---|
| **Nízká** | veřejně přístupná / určená ke zveřejnění (např. dle zákona o svobodném přístupu k informacím); narušení neohrožuje oprávněné zájmy | žádná |
| **Střední** | neveřejná, **know-how** organizace; ochrana nevyžadována předpisem ani smlouvou | prostředky pro **řízení přístupu** |
| **Vysoká** | neveřejná; ochrana **vyžadována předpisy nebo smlouvou** | **řízení a zaznamenávání** přístupu; přenosy chráněny **kryptograficky** |
| **Kritická** | nadstandardní ochrana (strategické obchodní tajemství, citlivé osobní údaje) | **evidence osob**, které přistoupily, + ochrana **i proti kompromitaci administrátory** |

## Integrita

| Úroveň | Popis | Ochrana |
|---|---|---|
| **Nízká** | nevyžaduje ochranu integrity | žádná |
| **Střední** | narušení → poškození zájmů s **méně závažnými** dopady | standardní nástroje (omezení práv pro zápis) |
| **Vysoká** | narušení → **podstatné** dopady na ostatní aktiva | sledování **historie změn** a **identity** toho, kdo změnu provedl |
| **Kritická** | narušení → **velmi vážné, přímé** dopady | **jednoznačná identifikace** autora změny (např. **digitální podpis**) |

## Dostupnost

| Úroveň | Max. výpadek | Ochrana |
|---|---|---|
| **Nízká** | tolerováno delší období (cca **do 1 týdne**) | pravidelné zálohování |
| **Střední** | max. **pracovní den** | běžné zálohování a obnova |
| **Vysoká** | max. **několik málo hodin**; výpadek řešit neprodleně | **záložní systémy**; obnova může vyžadovat zásah obsluhy |
| **Kritická** | nepřípustný ani výpadek v řádu **minut** | záložní systémy, obnova **krátkodobá a automatizovaná** |

> [!info] Kontext navíc
> Škály pocházejí z prováděcí vyhlášky k *původnímu* ZoKB (vyhl. č. 82/2018 Sb.). Nový [[ZoKB]] (264/2025 Sb.) s vyhláškami 409/2025 a 410/2025 Sb. na principu hodnocení aktiv podle C/I/A staví dál.

> [!tip] Jak si to zapamatovat
> S každým stupněm roste **doložitelnost**: střední = řídím přístup → vysoká = **zaznamenávám** → kritická = **prokážu konkrétní osobu** (i vůči adminům, digitální podpis, automatizace).

## Souvislosti

- Přednáška: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=67|s. 67–69]], plné verze [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=82|s. 82–84]]
- Související: [[Aktivum]] · [[CIA triáda]] · [[Bezpečnostní mechanismus]] · [[ZoKB]]
