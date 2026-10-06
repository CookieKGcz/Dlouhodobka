---
tags: [PV017, pojem, regulace]
aliases: [Regulatorní pyramida, Chytrá regulace, Smart regulation, Command and control, Ko-regulace, Samoregulace]
---

# Regulatorní mix a regulatorní pyramida

> [!summary] Myšlenka
> Regulátor nemá jen „zákaz + pokutu". **Chytrá regulace nevolí jeden nástroj, nýbrž jejich pořadí.**

## Nástroje (P3, s. 33)

| Nástroj | Příklad |
|---|---|
| **Command and control** | povinnost, kontrola, sankce (ZoKB, NIS2) |
| **Ko-regulace a samoregulace** | normy a **certifikace** (ISO 27001, EUCC) |
| **Ekonomické nástroje** | **pojištění**, veřejné zakázky (požadavky v zadání) |
| **Podpůrné nástroje** | **hlášení, varování, CSIRT** |

## Regulatorní pyramida

```mermaid
flowchart BT
    A["Poradenství, osvěta, varování<br/>(většina případů)"] --> B["Kontrola, doporučení, nápravná opatření"]
    B --> C["Opatření a příkazy regulátora"]
    C --> D["Sankce – pokuty, zákaz činnosti<br/>(výjimečně)"]
```

Od **poradenství** přes **nápravu** k **sankci** – regulátor eskaluje jen tehdy, když mírnější nástroj nezabral.

> [!info] Kontext navíc
> Koncept *responsive regulation* a regulatorní pyramidy pochází od Ayrese a Braithwaitea (1992). Typy pravidel: **deskriptivní / preskriptivní · performativní · chytrá** (P3, s. 31).

## Souvislosti

- Přednáška: [[3 260929 - Přístup k regulaci KB|P3]] – [[PV017_03_2026_Pristup_k_regulaci_kyberneticke_bezpecnosti.pdf#page=31|s. 31–33]]
- Související: [[Lessigovy modality regulace]] · [[Technologická neutralita]] · [[Rizikově orientovaný přístup]] · [[Compliance]]
