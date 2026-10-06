---
tags: [PV017, pojem]
aliases: [CIA, Důvěrnost, Integrita, Dostupnost, Confidentiality, Integrity, Availability]
---

# CIA triáda

> [!summary] Definice
> Informace je bezpečná, když je zajištěna její:
> - **Důvěrnost (Confidentiality)** – je přístupná **pouze oprávněným** subjektům,
> - **Integrita (Integrity)** – je modifikovatelná **pouze oprávněnými** subjekty,
> - **Dostupnost (Availability)** – je **dostupná** oprávněným subjektům (do stanovené doby).

## Rozšiřující vlastnosti

| Vlastnost | EN | Význam |
|---|---|---|
| Autenticita | authenticity | pravost, původnost |
| Zodpovědnost, prokazatelnost | accountability | akce lze dohledat k entitě, která je provedla |
| Nepopiratelnost | non-repudiation | schopnost prokázat výskyt události / činnosti |
| Spolehlivost | reliability | bezporuchovost, činnost ve shodě se specifikací |

Whitman & Mattord (2009) navrhují doplnit i *accuracy, authenticity, utility, possession* ([[3 260929 - Přístup k regulaci KB|P3]]).

## Detail jednotlivých vlastností

**Důvěrnost**
- zpřístupnit „správným lidem", zabránit „špatným lidem",
- týká se **uchovávání i přenosu** informací,
- úzce souvisí s ochranou **osobních údajů** ([[GDPR]]),
- typické mechanismy: šifrování, řízení přístupu, NDA.

**Integrita (celistvost)**
- *integrita zdroje* – změny smí dělat jen autorizované subjekty a mechanismy,
- *integrita dat* – data nesmí být nevhodně, náhodně ani záměrně změněna,
- *integrita původu* – data pochází od toho, kdo je validně poskytuje,
- informace mají být **platné** (odrážejí realitu) a **spolehlivé** (za stejných okolností stejná data); aktiva **kompletní a korektní**,
- typické mechanismy: hashe, MAC, digitální podpis, řízení práv k zápisu, logování změn.

**Dostupnost**
- „Nedostupný IS v okamžiku potřeby je přinejmenším stejně špatný jako žádný IS."
- ohrožují ji technické problémy, přírodní jevy, lidské faktory (chyby i útoky),
- typické mechanismy: zálohy, redundance, záložní lokality, DDoS ochrana, BCP/DRP.

## Vrstvový model (P3, slajd 11)

Uprostřed **Information** → trojúhelník **C–I–A** → **Hardware, Software, Communication** → vnější vrstvy **Physical → Personal → Organizational security**. Tedy CIA se chrání na všech vrstvách – technické, fyzické, personální i organizační.

> [!tip] Na zkoušku
> - ITU v definici kyberbezpečnosti řadí cíle jako **1. dostupnost, 2. integrita (vč. autenticity a nepopiratelnosti), 3. důvěrnost**.
> - Každé opatření v [[ISO-IEC 27002]] má atribut „vlastnosti IB" = které z C/I/A chrání.
> - Každá kategorie [[STRIDE]] porušuje jednu vlastnost (S→autenticita, T→integrita, R→nepopiratelnost, I→důvěrnost, D→dostupnost, E→autorizace).

## Souvislosti

- Přednášky: [[1 260915 - Úvod do informační bezpečnosti|P1]] – [[PV017_01_2026_uvod_do_bezpecnosti.pdf#page=20|s. 20–23]] · [[3 260929 - Přístup k regulaci KB|P3]] – [[PV017_03_2026_Pristup_k_regulaci_kyberneticke_bezpecnosti.pdf#page=8|s. 8–11]]
- Související: [[Klasifikace aktiv dle ZoKB]] · [[Safety vs Security]] · [[Kybernetická bezpečnost (pojem)]]
