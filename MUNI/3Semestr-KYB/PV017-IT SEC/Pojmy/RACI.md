---
tags: [PV017, pojem, role]
aliases: [Matice RACI, RACI matrix, Responsible Accountable Consulted Informed]
---

# Matice RACI

> [!summary] Definice
> Nástroj pro přiřazení odpovědností k činnostem: **R**esponsible (provádí) · **A**ccountable (odpovídá a schvaluje – **vždy jen jeden**) · **C**onsulted (konzultován) · **I**nformed (informován).

## Příklad z P4 (ilustrativní)

| Činnost | Vedení | Manažer KB | IT provoz | Garant aktiva | Auditor KB |
|---|---|---|---|---|---|
| Schválení bezpečnostní politiky | **A** | R | C | C | I |
| Analýza rizik | I | **A/R** | C | R | I |
| Akceptace zbytkového rizika | **A/R** | C | I | C | I |
| Zavedení technického opatření | I | **A** | R | C | I |
| Rozhodnutí o hlášení incidentu | I | **A/R** | C | C | I |
| Audit KB | **A** | C | C | C | R |

## Co si z tabulky odnést

- Politiku **schvaluje vedení** (A), připravuje manažer KB (R).
- **Akceptace zbytkového rizika je výhradně věc vedení** (A/R) – ne IT.
- O hlášení incidentu rozhoduje **manažer KB** (musí být určeno předem, vč. zastupitelnosti).
- Audit provádí auditor (R), odpovědnost (A) má vedení – auditor nepodléhá manažerovi KB.
- Každý řádek má **právě jedno A**.

## Souvislosti

- Přednáška: [[4 261006 - Role řízení KB|P4]] – [[PV017_04_2026_Role_rizeni_kyberneticke_bezpecnosti.pdf#page=37|s. 37]]
- Související: [[Bezpečnostní role]] · [[CISO]] · [[Model tří linií]]
