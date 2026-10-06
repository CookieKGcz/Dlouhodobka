---
tags: [PV017, pojem]
aliases: [Threat modeling, Modelování hrozeb]
---

# STRIDE

> [!summary] Definice
> **Framework pro modelování hrozeb** (threat modeling) od Microsoftu. Akronym šesti kategorií hrozeb, podle kterých se systematicky prochází každá komponenta systému.

| | Hrozba | Porušená vlastnost* | Příklad ze slajdu (P1, s. 48) |
|---|---|---|---|
| **S** | Spoofing (podvržení identity) | autenticita | e-mail pod cizí identitou; odposlech Wi-Fi jména a hesla; transakce pod cizí identitou; falešná stránka sbírající hesla |
| **T** | Tampering (neoprávněná změna) | integrita | přístup do DB přes default admin credentials; změna vlastních zdravotních údajů v aplikaci VZP; změna stavu onboardingu |
| **R** | Repudiation (popření) | nepopiratelnost | nelze zjistit, kdo poslal příkaz ke smazání záloh |
| **I** | Information disclosure (únik informací) | důvěrnost | získání admin přístupu; únik dat z chybně zpřístupněného cloudového úložiště |
| **D** | Denial of Service | dostupnost | rušení rádiových frekvencí IoT sítě |
| **E** | Elevation of Privilege | autorizace | neoprávněné čtení paměti, kde mohou být uložena hesla |

\* Mapování na vlastnosti je standardní součást STRIDE (kontext navíc ke slajdům) – užitečné pro test: každé písmeno ↔ jedna vlastnost z [[CIA triáda|CIA a rozšiřujících vlastností]].

> [!tip] Mnemotechnika
> S-T-R-I-D-E ↔ **A**utenticita, **I**ntegrita, **N**epopiratelnost, **D**ůvěrnost, **D**ostupnost, **A**utorizace.

## Souvislosti

- Přednáška: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=47|s. 47–48]]
- Související: [[Hrozba]] · [[CIA triáda]] · [[Principy návrhu bezpečnostních opatření]]
