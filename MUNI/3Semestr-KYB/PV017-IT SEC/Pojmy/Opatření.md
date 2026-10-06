---
tags: [PV017, pojem]
aliases: [Control, Bezpečnostní opatření, Measure, Security control, Preventivní opatření, Detekční opatření, Nápravné opatření]
---

# Opatření (control)

> [!summary] Definice
> **Opatření (control, measure, security enforcing function)** = prostředek, který **modifikuje riziko**; nástroj pro **snížení / eliminaci rizika**.

## Klíčové body

- Plné odstranění rizika bývá **neefektivní** → opatření riziko typicky **redukují**, neodstraňují.
- Opatření se mají implementovat **jen pro specifická, identifikovaná rizika**.
- Realizace přes [[Bezpečnostní mechanismus|mechanismy]] (SW, HW, administrativa).
- Typické opatření = **kombinace technologie a procesů** (výrazná role politiky a vzdělávání).
  - *Antivir:* SW v bráně i v PC + procedura aktualizací + výchova uživatelů.

## Zásady výběru (P1, s. 59)

- **dle kontextu a analýzy rizik!**
- **podmínka efektivnosti: cena opatření ≤ výše škody**,
- s každým aktivem se druží více rizik; na každé identifikované riziko efektivní opatření; jedno opatření může řešit více rizik,
- návod k volbě best practices: [[ISO-IEC 27002]].

## Typy podle vztahu k incidentu (atribut 27002)

| Typ | Kdy působí | Příklad |
|---|---|---|
| **Preventivní** | má incidentu **zabránit** | firewall, MFA, školení |
| **Detekční** | působí **při výskytu** | IDS, SIEM, monitoring logů |
| **Nápravné** | působí **po výskytu** | obnova ze záloh, incident response, záplata |

## Kategorie opatření

- ISO 27002:2022: **organizační · lidské zdroje · fyzická · technologická** (37 + 8 + 14 + 34 = 93).
- Ve smyslu zákona: **organizační a technická** bezpečnostní opatření ([[4 261006 - Role řízení KB|P4]]).

> [!tip] Opatření × mechanismus
> **Opatření** = *co* děláme s rizikem (funkce, cíl). **Mechanismus** = *čím* to realizujeme (digitální podpis, šifrování, biometrie).

## Souvislosti

- Přednášky: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=57|s. 57–64]] · [[2 260922 - ISMS a role v organizaci|P2]] – SoA v MediCloud
- Související: [[Riziko]] · [[Řízení rizik]] · [[ISO-IEC 27002]] · [[Prohlášení o aplikovatelnosti (SoA)]] · [[Principy návrhu bezpečnostních opatření]]
