---
tags: [PV017, pojem]
aliases: [Útok, Attack, Bezpečnostní incident, Security incident, Incident, Kybernetický incident]
---

# Útok a bezpečnostní incident

> [!summary] Definice
> - **Útok (attack)** – pokus o způsobení škody na aktivech; útočník **využije zranitelnost** v ochraně aktiva → útok = **realizovaná hrozba**.
> - **Bezpečnostní incident (security incident)** – **událost, která může ohrozit** bezpečnost informací.

## Klíčové body

- Útok způsobuje škodu: snížení hodnoty, zničení, znepřístupnění, zveřejnění důvěrného aktiva…
- Každý útok je incident, ale **ne každý incident je útok** (výpadek, chyba, přírodní katastrofa).
- **Generická kategorizace útoků / incidentů** (P1, s. 50):
  - **přírodní katastrofy** – hurikán, zemětřesení, požár → zálohovat **ve vzdálené lokalitě**,
  - **externí útoky** – krádeže dat o kartách a lidech, hackeři, profesionálové,
  - **interní útoky** – např. Wikileaks z interně zcizených dat,
  - **selhání a neúmyslné lidské chyby** – výpadek napětí, disků, káva v klávesnici, smazaná data.

> [!example] Ransomware v českých nemocnicích
> **Benešov** (11. 12. 2019) – 3 týdny omezení, škoda **59 mil. Kč**, řetězec Emotet → TrickBot → Ryuk (skupina Wizard Spider), nešlo o cílený útok · **FN u sv. Anny Brno** (2020) – 4 týdny · **PN Kosmonosy** (2020) – 10 dní.

> [!example] Globální incidenty (P3)
> Stuxnet 2010 (první fyzické škody) · Yahoo 2013–14 (> 3 mld. účtů) · Equifax 2017 · WannaCry 2017 · SolarWinds 2020 (supply chain) · CrowdStrike 2024 (**nebyl útok** – chybná aktualizace).

## Řízení a hlášení

Incidenty se detekují, vyhodnocují (je významný?), hlásí v lhůtách **24 h / 72 h / 1 měsíc** a končí poučením (lessons learned) → [[Hlášení incidentů]].

## Souvislosti

- Přednášky: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=50|s. 50–51]] · [[3 260929 - Přístup k regulaci KB|P3]] – [[PV017_03_2026_Pristup_k_regulaci_kyberneticke_bezpecnosti.pdf#page=4|s. 4–6]] · [[4 261006 - Role řízení KB|P4]] – [[PV017_04_2026_Role_rizeni_kyberneticke_bezpecnosti.pdf#page=23|s. 23]]
- Související: [[Hrozba]] · [[Zranitelnost]] · [[Riziko]] · [[Hlášení incidentů]]
