---
tags: [PV017, pojem]
aliases: [Common Vulnerabilities and Exposures]
---

# CVE – Common Vulnerabilities and Exposures

> [!summary] Definice
> **Bezplatný slovník (katalog) známých zranitelností**, který organizacím pomáhá zlepšit kyberbezpečnost. Provozuje nezisková organizace **MITRE**. Záznam CVE popisuje jednu **známou** zranitelnost.

## Klíčové body

- Každá položka: **standardní identifikátor** + stav, stručný popis, odkazy na zprávy a doporučení.
- Formát ID: `CVE-YYYY-NNNN…` – `YYYY` = rok přidělení ID nebo zveřejnění zranitelnosti, `NNNN…` = pořadové číslo (4 a více číslic), např. `CVE-2014-12345`, `CVE-2016-7654321`.
- **Na rozdíl od databází zranitelností CVE neobsahuje** informace o riziku, dopadu, opravě ani další technické detaily.
- Příklad ze slajdu 42: **CVE-2023-28858** – redis-py nechal po zrušení async příkazu otevřené spojení a mohl poslat data jinému klientovi (souvisí s výpadkem/únikem u ChatGPT v březnu 2023).

> [!info] Kontext navíc
> Riziko a závažnost doplňují jiné zdroje: **NVD** (National Vulnerability Database, NIST) přidává skóre **CVSS**, CPE (dotčené produkty) a odkazy na opravy. Proto „CVE ≠ databáze zranitelností".

## Souvislosti

- Přednáška: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=41|s. 41–42]]
- Související: [[Zranitelnost]]
