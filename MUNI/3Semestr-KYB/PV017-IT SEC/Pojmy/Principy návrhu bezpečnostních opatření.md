---
tags: [PV017, pojem]
aliases: [Saltzer Schroeder, Least privilege, Fail-safe defaults, Economy of mechanism, Separation of privilege, Psychological acceptability, Open design, Complete mediation, Least common mechanism, Security through obscurity, Princip nejmenších práv]
---

# Principy návrhu a implementace bezpečnostních opatření

> [!summary] Myšlenka
> Principy vycházejí z myšlenek **jednoduchosti a omezení**, zároveň očekávají **důkladnou a komplexní** ochranu. Každý externí systém je vůči bezpečné aplikaci implicitně **nedůvěryhodný**.

| # | Princip | EN | Podstata | Příklad (P1) |
|---|---|---|---|---|
| 1 | Nejmenších práv | **Least Privilege** | každý dostane jen **nejmenší nutná** práva | middleware: přístup na internet, čtení DB, zápis logů – ale ne root |
| 2 | Bezpečného výchozího stavu | **Fail-safe Defaults** | co **není výslovně povoleno, je zakázáno** | firewall „deny all"; expirace a složitost hesel zapnuté by default |
| 3 | Ekonomiky mechanismu | **Economy of Mechanism** | mechanismy co **nejjednodušší** → méně chyb, snazší testování, méně předpokladů, menší attack surface | online help s vyhledáváním → SQLi; pouze pro přihlášené → menší riziko; centrální validace → výrazně menší; odstranit vyhledávání → riziko zmizí |
| 4 | Oddělení oprávnění | **Separation of Privilege** | oprávnění **ne na základě jediné podmínky** | `su` = heslo **a** správná skupina; admin OS nemůže nakupovat akcie |
| 5 | Psychologické přijatelnosti | **Psychological Acceptability** | mechanismus nesmí ztěžovat přístup víc, než kdyby nebyl | uznání lidského faktoru |
| 6 | Otevřeného designu | **Open Design** | bezpečnost **nesmí záviset na utajení** návrhu či implementace | ✗ *security through obscurity* – klíč pod rohožkou; zásadní pro kryptografii |
| 7 | Úplného zprostředkování | **Complete Mediation** | **každý** přístup k objektu se kontroluje | omezuje cachování výsledků kontrol → jednodušší implementace |
| 8 | Nejmenšího společného mechanismu | **Least Common Mechanism** | mechanismy pro přístup k prostředkům **nesdílet** | sdílené prostředky = kanál pro únik / interferenci |

> [!info] Kontext navíc
> Jde o klasické principy **Saltzera a Schroedera** („The Protection of Information in Computer Systems", 1975). Open Design souvisí s **Kerckhoffsovým principem**: šifra má být bezpečná, i když útočník zná vše kromě klíče.

> [!tip] Na zkoušku – typické přiřazení
> - „deny by default" → **fail-safe defaults**
> - „dvě podmínky pro root" / „admin ≠ běžný uživatel aplikace" → **separation of privilege**
> - „odstraňte nepotřebnou funkci" → **economy of mechanism**
> - „utajený algoritmus" → porušení **open design**
> - „ověřit oprávnění při každém přístupu, ne jen při prvním" → **complete mediation**

## Souvislosti

- Přednáška: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=71|s. 71–75]]
- Související: [[Opatření]] · [[Bezpečnostní mechanismus]] · [[STRIDE]]
