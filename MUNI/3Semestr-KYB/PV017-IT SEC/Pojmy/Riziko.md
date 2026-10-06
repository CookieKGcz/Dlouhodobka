---
tags: [PV017, pojem]
aliases: [Risk, Rizika, Zbytkové riziko, Residual risk, Matice rizik]
---

# Riziko (risk)

> [!summary] Definice
> **Velikost rizika = pravděpodobnost provedení útoku × výše škody (dopad).**
> - *užší smysl:* pravděpodobnost, že se v daném zranitelném místě uplatní hrozba,
> - *širší smysl:* pravděpodobnost výskytu incidentu × způsobená škoda / dopad útoku.

## Klíčové body

- **Pravděpodobnost uplatnění hrozby** je dána:
  - snadností / obtížností využití zranitelností aktiva,
  - množstvím a schopnostmi potenciálních útočníků → [[Model útočníka]].
- Rizika mohou být různě závažná: **katastrofická / velká, akceptovatelná, nevýznamná**.
- Riziko vzniká z **existence hrozby** a **existence zranitelnosti** a míří na **aktivum** → [[Obecný model zabezpečování]].
- **Zbytkové riziko (residual risk)** = riziko, které zůstane po aplikaci opatření; o jeho **akceptaci prokazatelně rozhoduje vedení** (formální záznam: vlastník, odůvodnění, zbytkové skóre, podmínky, platnost, datum přezkumu).
- **Risk appetite (apetit k riziku)** = kolik rizika je organizace ochotna nést; stanovuje vedení / řídicí výbor ([[Governance, management a provoz|governance]]).

## Kvantifikace – matice P × D (MediCloud, P2)

R = P × D na škále 1–4 → hodnoty 1–16.

| D \ P | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **4** | 4 | 8 | 12 | 16 |
| **3** | 3 | 6 | 9 | 12 |
| **2** | 2 | 4 | 6 | 8 |
| **1** | 1 | 2 | 3 | 4 |

**Rozhodovací hranice:** 1–3 **akceptovat** · 4–7 **posoudit** · 8–16 **řešit**.

> [!tip] Registr rizik
> „Registr rizik umožňuje **prioritizovat**, ne jen vyjmenovat obavy." U každého rizika: aktivum, hrozba, zranitelnost, možný incident, dopad, **vlastník rizika**.

## Souvislosti

- Přednášky: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=53|s. 53]] · [[2 260922 - ISMS a role v organizaci|P2]] – [[PV017_02_2026_ISMS.pdf#page=28|s. 28–30]] · [[4 261006 - Role řízení KB|P4]] – [[PV017_04_2026_Role_rizeni_kyberneticke_bezpecnosti.pdf#page=20|s. 20]]
- Související: [[Řízení rizik]] · [[Opatření]] · [[Hrozba]] · [[Zranitelnost]] · [[Plán zvládání rizik (RTP)]]
