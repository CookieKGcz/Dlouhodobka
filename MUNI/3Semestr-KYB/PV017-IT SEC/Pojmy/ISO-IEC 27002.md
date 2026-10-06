---
tags: [PV017, pojem, norma]
aliases: [ISO 27002, 27002, ISO/IEC 27002, Katalog opatření]
---

# ISO/IEC 27002

> [!summary] Definice
> **Kodex nejlepších praktik** (code of practice) pro **opatření** bezpečnosti informací. Říká, **která opatření** může/má systém obsahovat; **neříká, jak je prosazovat** – k tomu navádí [[ISO-IEC 27001]]. Sama **není certifikovatelná**.

## ISO/IEC 27002:2022 – struktura

**93 opatření · 4 témata · 5 atributů**

| Téma | Počet | Příklady |
|---|---|---|
| **Organizační** | 37 | politiky pro IB, management identit, odezva na incidenty, kontinuita |
| **Lidské zdroje** | 8 | prověřování, disciplinární řízení, práce na dálku, dohody o mlčenlivosti |
| **Fyzická** | 14 | fyzický vstup, prázdný stůl a obrazovka, paměťová média, bezpečná likvidace zařízení |
| **Technologická** | 34 | koncová zařízení, bezpečná autentizace, kryptografie, bezpečné programování |

> [!tip] Mnemotechnika počtů
> **37 – 8 – 14 – 34** (O – L – F – T), součet **93**.

## Atributy (hashtagy u každého opatření)

1. **Typ opatření** – `#Preventivní` · `#Detekční` · `#Nápravné`
2. **Vlastnosti IB** – `#Důvěrnost` · `#Integrita` · `#Dostupnost`
3. **Koncepty kybernetické bezpečnosti** – `#Identifikace` · `#Ochrana` · `#Detekce` · `#Odezva` · `#Obnova` (≈ funkce NIST CSF)
4. **Provozní schopnosti** – 15 kategorií (správa a řízení, bezpečnost aplikací, fyzická bezpečnost, bezpečnost dodavatelských vztahů, právní požadavky a soulad…)
5. **Domény bezpečnosti** – `#Správa_a_řízení_a_ekosystém` · `#Ochrana` · `#Obrana` · `#Odolnost`

> [!example] 5.33 Ochrana záznamů
> Preventivní · C + I + A · Identifikace, Ochrana · Právní požadavky a soulad, Management aktiv, Ochrana informací · Obrana

## Souvislosti

- Přednášky: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=59|s. 59–64]] · [[2 260922 - ISMS a role v organizaci|P2]] – [[PV017_02_2026_ISMS.pdf#page=6|s. 6]]
- Související: [[Opatření]] · [[ISO-IEC 27001]] · [[Prohlášení o aplikovatelnosti (SoA)]] · [[Rodina norem ISO 27k]]
