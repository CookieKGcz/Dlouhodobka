Cleanup pass done with Claude on 2026-10-06. Every change is listed below with the old and new text.
A backup of all notes from before the cleanup is in `_backup-before-cleanup-2026-10-06.zip` (in the Roann folder).
Blank notes were left untouched on purpose.

# Renames to do in Obsidian
(Do these with Obsidian's rename so links update automatically.)
- [ ] Folder `Factions/AA-current-1295-Factions/Ardees Mist Realm` → `Ardess Mist Realm`
- [ ] Note `Ardees Mist Realm.md` → `Ardess Mist Realm.md` (links to it update automatically if 'Automatically update internal links' is on in Settings → Files & links)
- [ ] Note `Kaspion Empire/In/Lavrass.md` → `Lavras.md`
- [ ] Note `Kaspion Empire/In/The Great Vofonia School.md` → `The Great Vafonia School.md`
- [ ] Note `Tynead Kingdom/In/Keilnorn.md` → `Kelinorn.md`
- [ ] Note `Ardees Mist Realm/In/Porst.md` → `Porstt.md`
- [ ] Note `Ardees Mist Realm/In/Arrys.md` → `Aryss.md` (it's the lake)
- [ ] Note `World_INFO/Calendar/Days/Unam.md` → `Umam.md`
- [ ] Note `World_INFO/Calendar/Days/Panael.md` → `Penael.md`
- [ ] Note `Gunlags Dominion/In/The forest of Silent.md` → `The Silent Forest.md`
- [ ] Note `Gunlags Dominion/In/The past of Omens.md` → `The Path of Omens.md`
- [ ] Note `Haford Empire/In/Batun Towers.md` → `Batun Tower.md`
- [ ] Note `Haford Empire/In/Round black-forest.md` → `Round Blackforest.md`
- [ ] Note `Kaspion Empire/In/Seville.md` → `Skovell.md` (real-world name replaced)
- [ ] Note `Kaspion Empire/In/Tranmere.md` → `Tranmor.md` (real-world name replaced)
- [ ] Note `Equipment/Necklase of Adaptaion.md` → `Necklace of Adaptation.md`
- [ ] Note `Important_Places/Buraeu of Central Kaspion.md` → `Bureau of Central Kaspion.md`
- [ ] Note `World_INFO/Space_INFO/Galaxy/Andromeda.md` → `Aurael.md` (real galaxy name replaced)

# Map label fixes
(These are on the map images, so they need fixing in the map tool.)
- [ ] 'The spears of Ithelion' → 'The spears of Iremorth'
- [ ] Remove the old 'Thesaur-bourg' label under 'Thelion'
- [ ] Remove the big blue 'Lavraas' label, keep 'Lavras'
- [ ] 'The Forest of Silent' → 'The Silent Forest'
- [ ] 'The past of Omens' → 'The Path of Omens'
- [ ] 'Clyne Collage' → 'Cliyne College'
- [ ] Remove the leftover old labels 'Monernorn' (under Manenorn) and 'Ijulavik' (next to Julavik)
- [ ] 'xxxxxxx Kingdom' → 'Iremorth Kingdom' and 'XXXXXXX rep.' → 'Collio Republic'
- [ ] Merge the small 'Iremorth' label and the covered 'xxxx Kingdom' into one 'Iremorth Kingdom' label
- [ ] 'Round blackforest' → 'Round Blackforest'
- [ ] 'Seville' → 'Skovell'
- [ ] 'Tranmere' → 'Tranmor'

# Changes

## Overview merge (Roann.md → AA-Roann.md) and era notation (b.g.a. / a.g.a., linked to Golden Age)

- `AA-Roann.md` (1x): `x The thing before, with the start of magic.....` → `x The thing before, with the start of magic..... #todo`
- `AA-Roann.md` (1x): `around the 740k B age` → `around the 740k [[Golden Age|b.g.a.]] age`
- `AA-Roann.md` (1x): `About 100k B - 80k B we` → `About 100k - 80k [[Golden Age|b.g.a.]] we`
- `AA-Roann.md` (1x): `In 20k B the` → `In 20k [[Golden Age|b.g.a.]] the`
- `AA-Roann.md` (1x): `This gradually` → `This gradually #todo`
- `AA-Roann.md` (1x): `great union age(200 B[^1]),` → `great union age (200 [[Golden Age|b.g.a.]][^1]), where first kinds of trades between other kingdoms or territories were finally made possible.` — trade sentence merged in from Roann.md
- `AA-Roann.md` (1x): `after the year -+ 20 A[^2]` → `after the year -+ 20 [[Golden Age|a.g.a.]][^2]` — kept ~20 (Roann.md said 3)
- `AA-Roann.md` (1x): `haven't had some fun in a while)` → `haven't had some fun in a while) #todo`
- `AA-Roann.md` (1x): `The asteroid/[[THE Rift]]` → `The asteroid/[[THE Rift]] #todo`
- `AA-Roann.md` (1x): `[^1]: B stands for` → `[^1]: b.g.a. stands for`
- `AA-Roann.md` (1x): `[^2]: A stands for` → `[^2]: a.g.a. stands for`
- `AA-Roann.md` (1x): `- [[Races]] ⏎ -` → `- [[Races]] ⏎ - #todo`
- `AA-Roann.md` (1x): `Circumference: 24'028 km ⏎ days in a year: 986` → `Circumference: 24'028 km ⏎ r = 3824km ⏎ days in a year: 986 ⏎  ⏎ In the Newtonian theory, the gravity given by a certain mass M at distance R is given by 𝑔=G...` — radius + gravity lines merged in from Roann.md
- `Characters/Deceased/Miric Abdul.md` (1x): `[[b.g.a]]` → `[[Golden Age|b.g.a.]]`
- `Characters/Deceased/Miric Abdul.md` (1x): `[[a.g.a]]` → `[[Golden Age|a.g.a.]]`
- `World_INFO/Dictionary/The Korion.md` (1x): `[[a.g.a.]]` → `[[Golden Age|a.g.a.]]`
- `World_INFO/Dictionary/Golden Age.md` (1x): `The beginning of the [[Miric Calendar]]. Also known as [[a.g.a]] (after the golden age), or [[b.g.a]].` → `The beginning of the [[Miric Calendar]] (year 0). Years after it are written a.g.a. (after the start of the Golden Age), years before it b.g.a. (before the s...`
- `World_INFO/Calendar/Miric Calendar.md` (1x): `in the later stages of year 0 a.g.a.` → `in the later stages of year 0 [[Golden Age|a.g.a.]]`
- `World_INFO/Calendar/Miric Calendar.md` (1x): `=  B in short` → `=  b.g.a. in short`
- `World_INFO/Calendar/Miric Calendar.md` (1x): `=  A in short` → `=  a.g.a. in short`
- `World_INFO/Calendar/Miric Calendar.md` (1x): `Year: 1295 [[a.g.a.]]` → `Year: 1295 [[Golden Age|a.g.a.]]`
- `World_INFO/Hypotheses/Trapped in the unknown.md` (1x): `[[b.g.a]]` → `[[Golden Age|b.g.a.]]`
- `World_INFO/Space_INFO/Moons-bios/Oliruf.md` (1x): `279 (asmga)` → `279 [[Golden Age|a.g.a.]]`
- `World_INFO/Space_INFO/Moons.md` (1x): `279 (asmga)` → `279 [[Golden Age|a.g.a.]]`

## Names: Ardess Mist Realm, Thelion, Lavras

- `Important_Places/Casted continent.md` (1x): `[[Thlion-bourg]]` → `[[Thelion]]` — Dino city is now called Thelion

## Names: Aryss duplicate

- `Factions/AA-current-1295-Factions/Ardees Mist Realm/Ardees Mist Realm.md` (1x): `- [[Ardess]] ⏎ - [[Arrys]]` → `- [[Ardess]]` — the lake was listed twice; kept the entry in the landmarks part of the list

## Faction lists: Thelion, Pollia Islands

- `Factions/AA-current-1295-Factions/Ardees Mist Realm/Ardees Mist Realm.md` (1x): `- [[Terst]]` → `- [[Terst]] ⏎ - [[Thelion]]` — added the old Dino city (no note created yet)
- `Factions/AA-current-1295-Factions/Haford Empire/Haford Empire.md` (1x): `- [[Pollia city]]` → `- [[Pollia city]] ⏎ - [[Pollia Islands]]` — matches the map and canvas

## Names: Fymor link, Iremorth's old name

- `Map/Map-Factions.canvas` (1x): `, [[Fymor]]` → `, [[Fymor the city of Iron tower|Fymor]]`
- `Factions/AA-current-1295-Factions/Iremorth Kingdom/Iremorth Kingdom.md` (1x): `Consist of:` → `The kingdom was once called Thelion. The city of [[Thelion]] still carries the old name. ⏎  ⏎ Consist of:`

## Spelling fixes

- `AA-Roann.md` (2x): `increasement` → `increase`
- `AA-Roann.md` (1x): `casing to exist` → `ceasing to exist`
- `AA-Roann.md` (1x): `poping` → `popping`
- `AA-Roann.md` (1x): `thought only to picked` → `taught only to picked`
- `AA-Roann.md` (1x): `The believes` → `The beliefs`
- `Factions/AA-current-1295-Factions/Kaspion Empire/In/Deep hole.md` (1x): `Hearth of` → `Heart of`
- `Factions/AA-current-1295-Factions/Kaspion Empire/In/Deep hole.md` (1x): `below 2st layer` → `below 2nd layer`
- `Factions/AA-current-1295-Factions/Kaspion Empire/In/Deep hole.md` (1x): `tell the tail` → `tell the tale`
- `Factions/AA-current-1295-Factions/Kaspion Empire/In/Deep hole.md` (1x): `Silance` → `Silence`
- `Factions/AA-current-1295-Factions/Kaspion Empire/In/Deep hole.md` (1x): `be worry of` → `beware of`
- `Factions/AA-current-1295-Factions/Kaspion Empire/In/Deep hole.md` (1x): `are more thicker and` → `are thicker and`
- `World_INFO/Dictionary/Dwelling-Delving gears.md` (1x): `- ### Rank 4 (6st l.) ⏎ 	- All things that are on rank 1-2` → `- ### Rank 4 (6th l.) ⏎ 	- All things that are on rank 1-3`
- `World_INFO/Classification of documents.md` (2x): `pose a thread` → `pose a threat`
- `World_INFO/Classification of documents.md` (1x): `Raonn` → `Roann`
- `World_INFO/Classification of documents.md` (1x): `Legendry` → `Legendary`
- `World_INFO/Laws_+_Orders.md` (1x): `Penisuela` → `Peninsula`
- `World_INFO/Laws_+_Orders.md` (1x): `Norther part` → `Northern part`
- `World_INFO/Laws_+_Orders.md` (1x): `braking` → `breaking`
- `World_INFO/Laws_+_Orders.md` (1x): `trade routs` → `trade routes`
- `Races/Races.md` (1x): `common spices` → `common species`
- `Races/Races.md` (1x): `then the common` → `than the common`
- `Important_Places/The Great Lake.md` (1x): `wast body` → `vast body`
- `Factions/AA-current-1295-Factions/Shiva Islands/Shiva Islands.md` (1x): `swomp-ish` → `swamp-ish`
- `Factions/AA-current-1295-Factions/Collio Republic/In/Congress of Collio.md` (1x): `brake out` → `break out`
- `Characters/Alive/Tynead/Ricia Tyne.md` (1x): `here pristine` → `her pristine`
- `Characters/Alive/Tynead/Ricia Tyne.md` (1x): `she would dirtied it` → `she would dirty it`
- `Important_Places/Bethadh.md` (1x): `easily prayed beings` → `easily preyed-upon beings`
- `Factions/AA-current-1295-Factions/Tynead Kingdom/In/Elemental city of Echath.md` (1x): `maid in` → `made in`

## Bethadh legend rewrite, hidden asides

- `Important_Places/Bethadh.md` (1x): `Legends says that, first it was an oak tree, which decided to give its life to a dying elf, who in return swore its loyalty and life. But not all stories end...` → `Legends say that it was first an ordinary oak tree, which gave its life to save a dying elf. In return, the elf swore it loyalty and life, and for centuries ...` — new legend: the elf repays the oak by becoming its soul; old text kept below
- `AA-Roann.md` (1x): `(pretty shitty start ngl)` → `%%(pretty shitty start ngl)%%`
- `History/AA - Creation of the World/When Life and Death meets.md` (1x): `\- unknown ⏎  ⏎ Bruh` → `\- unknown ⏎  ⏎ %%Bruh%%`
- `World_INFO/Schools/Major schools.md` (1x): `them! *XD*` → `them! %%*XD*%%`
- `Characters/Alive/Tynead/Ricia Tyne.md` (1x): `(prob could take a diff test, but choose *exploration and adventuring* because cringy ass shit mind) :/` → `%%(prob could take a diff test, but choose *exploration and adventuring* because cringy ass shit mind) :/%%`

## Astronomy: Alkes as an old 1.0-solar-mass star, new moon orbits, calendar moon phases

- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `## Star:` → `## Star: ⏎ Alkes is an old star, about 9.5 billion years old and near the end of its stable life. It has swollen to ~1.45× the Sun's size and shines ~2.1× as...`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Class            | F5.9V         |      |` → `| Class            | G1 IV (aging) |      |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Mass             | 1.208         | Msol |` → `| Mass             | 1.000         | Msol |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Current Age      | 4.300         | Gyr  |` → `| Current Age      | 9.500         | Gyr  |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Maximum Age      | 5.673         | Gyr  |` → `| Maximum Age      | ~10.5 (end of main sequence) | Gyr  |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Radius           | 1.114         | Rsol |` → `| Radius           | 1.445         | Rsol |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Density          | 0.874         | Dsol |` → `| Density          | 0.331         | Dsol |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Temperature      | 6612          | K    |` → `| Temperature      | 5800          | K    |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `| Star Color       | 6612 - White  |      |` → `| Star Color       | 5800 - Yellow-white |      |`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `for orbit of 986 days the AU should be 1.938` → `for orbit of 986 days the AU should be 1.938 (correct now that Alkes is 1.0 solar mass)`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `|Star Mass|1.208|Msol|ℹ|2.40271E+30|kg|` → `|Star Mass|1.000|Msol|ℹ|1.98847E+30|kg|`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `|Star Radius|1.114|Rsol|ℹ|775,532|km|` → `|Star Radius|1.445|Rsol|ℹ|1,005,287|km|`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `|Star Density|0.874|Dsol|ℹ|1.231218497|g/cm³|` → `|Star Density|0.331|Dsol|ℹ|0.466|g/cm³|`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `|System Inner Limit|0.0078|AU|ℹ|1.16|million km|` → `|System Inner Limit|0.0101|AU|ℹ|1.51|million km|` — scaled with the new radius (1.5× star radius, same rule as before)
- `World_INFO/Space_INFO/Moons.md` (1x): `Takes 738 days to orbit.` → `Takes 48 days to orbit.`
- `World_INFO/Space_INFO/Moons.md` (1x): `Around Dardiel orbits other two moons (sub-moons) Seliel and Liviel. More info in their bio.` → `Takes 71 days to orbit. Around Dardiel orbits other two moons (sub-moons) Seliel and Liviel: Seliel circles Dardiel every 3 days, Liviel every 8 days. More i...`
- `World_INFO/Space_INFO/Moons.md` (1x): `Takes them 0.87 years to orbit.` → `Takes them 110 days to orbit.`
- `World_INFO/Space_INFO/Moons.md` (1x): `Similar sizes (2300 - 2600 km r). Takes 1.22 years to orbit.` → `Similar sizes (1600 - 1800 km r). Takes 160 days to orbit.`
- `World_INFO/Space_INFO/Moons.md` (1x): `Takes 26.67 years to orbit.` → `Takes about 190 days to orbit, the farthest a moon can be and still be held by Roann.`
- `World_INFO/Space_INFO/Moons-bios/Anael.md` (1x): `Takes 738 days to orbit.` → `Takes 48 days to orbit.`
- `World_INFO/Space_INFO/Moons-bios/Dardiel.md` (1x): `Around Dardiel orbits` → `Takes 71 days to orbit. Around Dardiel orbits`
- `World_INFO/Space_INFO/Moons-bios/Seliel.md` (1x): `Orbits around [[Dardiel]].` → `Orbits around [[Dardiel]] every 3 days.`
- `World_INFO/Space_INFO/Moons-bios/Liviel.md` (1x): `Orbits around [[Dardiel]].` → `Orbits around [[Dardiel]] every 8 days.`
- `World_INFO/Space_INFO/Moons-bios/Xoniel.md` (1x): `Takes them 0.87 years to orbit.` → `Takes them 110 days to orbit.`
- `World_INFO/Space_INFO/Moons-bios/Zupiel.md` (1x): `Takes them 0.87 years to orbit.` → `Takes them 110 days to orbit.`
- `World_INFO/Space_INFO/Moons-bios/Alerog.md` (1x): `Similar sizes (2300 - 2600 km r). Takes 1.22 years to orbit.` → `Similar sizes (1600 - 1800 km r). Takes 160 days to orbit.`
- `World_INFO/Space_INFO/Moons-bios/Anopo.md` (1x): `Similar sizes (2300 - 2600 km r). Takes 1.22 years to orbit.` → `Similar sizes (1600 - 1800 km r). Takes 160 days to orbit.`
- `World_INFO/Space_INFO/Moons-bios/Oliruf.md` (1x): `Takes 26.67 years to orbit.` → `Takes about 190 days to orbit, the farthest a moon can be and still be held by Roann.`
- `World_INFO/Calendar/Miric Calendar.md` (1x): `986 days in year` → `986 days in year ⏎  ⏎ Moon columns (left to right): Kiruf, Ala, Anael, Dardiel, Seliel, Liviel, Xoniel, Zupiel, Alerog, Anopo, Oliruf. Seliel and Liviel trav...` — all 986 rows of moon phases were also recomputed from the new orbit times (events and day names unchanged)

## Astronomy: gravity, Mu Arae note

- `AA-Roann.md` (1x): `is given by 𝑔=GM/R2` → `is given by 𝑔=GM/R2 ⏎ Gravity: ~1 g (Earth-like). With r = 3824km that needs a very dense planet, ~9.2 g/cm³ (Earth is 5.5), so Roann is a mostly-metal world...`
- `World_INFO/Space_INFO/Solar_System/Alkes.md` (1x): `for orbit of 986 days` → `Note: if these were Roann's real neighbours, Quijote (1.65 Jupiter masses at 1.52 AU) would be too close to Roann at 1.94 AU to be stable. It would have to s...`

## Ages, travel speed (~40 km/day), map stretch rule, France comparison

- `AA-Roann.md` (1x): `28px -- is about 168,196km ~ 168 km =about 6.5 days of travel on horse (without the 6th night), with calc - ~30km a day on horse` → `28px -- is about 168,196km ~ 168 km = about 4 days of travel on horse, with calc - ~40km a day on horse ⏎ Map stretch: the map is a flat 2:1 picture of the g...`
- `AA-Roann.md` (1x): `is half the length of a France (1000 km).` → `is about twice the length of France (1000 km).`
- `Map/Distance-Height WIP.md` (1x): `28px -- is about 168,196km ~ 168 km = x1.5 cca in reality (252km) = about 4.2 days of travel on horse (without the 4th night), with calc - ~60km a day on horse` → `28px -- is about 168,196km ~ 168 km = about 4 days of travel on horse, with calc - ~40km a day on horse`
- `Map/Distance-Height WIP.md` (1x): `(normal conditions with rough terrain and no interference)` → `(normal conditions with rough terrain and no interference) ⏎  ⏎ Map stretch: east–west distances × cos(latitude). ×~0.75 around Tynead Castle and Batun (~40–...`
- `Characters/Deceased/Miric Abdul.md` (1x): `Death around 16 [[Golden Age|a.g.a.]].` → `Death around 16 [[Golden Age|a.g.a.]].  ⏎ He made the calendar at only 7, a child prodigy, and died young at about 23.`

## Collio decisions

- `Factions/AA-current-1295-Factions/Collio Republic/The history of the Skigness peninsula.md` (1x): `Curently the Collian Republic is made up of:` → `Before the union, the cities of the Skigness peninsula were free city-states. Nobody invaded them, because the trade on [[The Great Lake]] was too useful to ...`
- `Factions/AA-current-1295-Factions/Collio Republic/In/Collios Northern Stronghold.md` (1x): `An exclave of the [[Collio Republic]] within the [[Iremorth Kingdom]]` → `An exclave of the [[Collio Republic]] within the [[Iremorth Kingdom]]. It began as a Collian trading post and grew into a fortified trade city.`
- `Factions/AA-current-1295-Factions/Collio Republic/In/Congress of Collio.md` (1x): `## Ideas` → `The Congress and [[Cliyne College]] have grown into one big twin city. ⏎  ⏎ ## Ideas`
- `Factions/AA-current-1295-Factions/Collio Republic/In/Cliyne College.md` (1x): `Just a question, there's an unmarked city next to it on the map, what's that?` → `Cliyne College and the [[Congress of Collio]] have grown into one twin city. The unmarked city next to the College on the map is part of it. ⏎  ⏎ Just a ques...`

## Irion, hex count, canvas link

- `Factions/AA-current-1295-Factions/Collio Republic/In/Irion.md` (1x): `strong military and discipline` → `strong military and discipline. Irion is Roann's fantasy Sparta: a militarised city where every citizen trains for war from childhood.`
- `Factions/AA-current-1295-Factions/Collio Republic/In/Irion.md` (1x): `Pwease >~<)` → `Pwease >~<) → Approved.`
- `AA-Roann.md` (1x): `~200 hexagons on map` → `~143 hexagons across the map at the equator (28 px each)`
- `Map/Distance-Height WIP.md` (1x): `~200 hexagons on map` → `~143 hexagons across the map at the equator (28 px each)`
- `Map/Map-Factions.canvas` (1x): `[[Crypt of the Old One ]]` → `[[Crypt of the Old One]]`
