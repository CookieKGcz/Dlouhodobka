## Uloha
- Transpotni vrstva je zodpovedna za zarizeni docasne komunikacni relace mezi dvema aplikacemi a za doruceni dat mezi nimi (**end-to-end** komunikace)

## Povinnosti
- Vytvareni a rizeni komunikace mezi aplikacemi na zdrojovem a cilovem uzlu.
- Segmentace dat ado aplikaci pro predani na sitovou vrstvu a slozeni segmentu ve spravnem poradi do datoveho proudu  (data sream) xx
- xx

## Mupltiplexing a Demulitplexing
- Umoznuje soubeznou komunikaci mezi mnoha aplikacemi na uzlu po stejne siti.

## Porty aplikaci
- Na odliseni dat z ruznych aplikaci pouziva portz aplikaci, ktery vklada do hlavicky kazdeho segmentu.
	- 0 - 1023     --     Well Known (Contact) Ports
		- servrove sluzby internetu
		- predeluje IANA
	- 1024 - 49151  -  Registered Ports
	- 4+152 - 65533  Private and/or Dynamic Ports

## Spolehlivost
- IP pretokoly posilaji data nespolehlive - xx
- xx

## TCP
- zajistuje spolehlive doruceni dat - vsechna data dorazi k cilove aplikaci ve spravnem poradi.
- Navazuje, udrzuje a ridi spojeni mezi odesilatelem a prijemcem
- Pouziva potvrzeni prijeti dat
- Ridi segmenty do spravneho poradi
- Pri ztrate segmentu zajisti opakovany prenos

### Hlavicka TCP segmentu
- xx
- xx
- xx
- [[Control Bits (Flags)]]
- Options - pole preomenne delky dle pouzite volby
	- [[Maximum segment size]]
### Faze TCP komunikace
- 1- 
- 2-
- 3-



## UDP
- Neumi zajistit spolehlive doruceni dat k cilove aplikaci
- Nenavazuje spojeni mezi odesilatelem a prijemcem, muze odesilat data broadcastem a multicastem
- Nezajisti, ze vsechny segmenty dat dorazi do cile, nedokaze je seradit
- Neridi tok dat
- Ma mensi naroky na sit
- DHCP, VoIP, xx