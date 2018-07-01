## Felépítés
- Festő könyvtára: `artists > [festő neve]`
	- A festő alapvető adatai: `metadata.json` (object)
		- `genres` (string array)
		- `birth` (dátum)
		- `death` (dátum)
	- A festő rövid életrajza: `bio.md`
	- A festő festményének könyvtára: `paintings > [festmény címe]`
		- A festmény alapvető adatjai: `metadata.json` (object)
			- `date` (dátum)
		- A festmény különbözö méretei: `versions > [méret].[fájl kiterjesztés]`
			- `[méret]`: `[szélesség]x[magasság]` vagy `max`
- Gyűjtemény: `collections > [gyűjtemény neve].json` (object)
	- `includes` (festmény array)

## JSON adattípusok
A `string`, `number` és `array` adattípusokért látogasd meg a [JSON specifikációt](https://json.org/).
- festmény: `[festő neve]` alakú `string`; vagy két tagból álló `array`, aminek első eleme `[festő neve]` alakú string, második eleme pedig `[festmény neve]` alakú `string`-ekből álló `string array`; példák:
	- `"Csontváry Kosztka Tivadar"`
	- `["Csontváry Kosztka Tivadar", ["Magányos cédrus", "Római híd Mosztarban"]]`
- dátum: `évszám` vagy `évszámintervallum`
- évszám: `[évszám]` alakú `string`, vagy ha lehet reprezentálni `number`-ként, akkor lehet `number` is; példák:
	- `1992`
	- `"1993"`
	- `"~1867"`
	- `"?"`
- évszámintervallum: `[évszám]-[évszám]` alakú `string`; példák:
	- `"1991-1992"`
	- `"?-1907"`
	- `"-99--14"` (meaning from BC 99 to BC 14)
- \[évszám\]: alapvetően sima integer (`/-[1-9]\d*|0/`), de
	- helyettesítheti egy `?`: az évszám ismeretlen 
	- kezdődhet `~`-vel: az integer csak körülbelüli érték

## Automatizált bővítés
- Az `add-artist.py` fájl futattasával lehet egyszerűen hozzáadni művészt
- Az `add-painting.py` fájl futattásával lehet egyszerűen hozzáadni festményt
Mindkettő esetében az elkészült fájlokat még érdemes átnézni valamint bővíteni manuálisan (pl. `bio.md`).

## Hogy kell futtatni a .py fájlokat és hogyan tudom a bővített adatbázist (ide) publikálni?
### Windows
1. Telepítsd a Gittet Git Bash-sal együtt ([Git letöltési linkje](https://git-scm.com/download/win))
2. Telepítsd a Pythont ([Python letöltési linkje](https://www.python.org/downloads/)) (**FONTOS: Az installer elején kérdezni fogja, hogy hozzáadja-e a Pythont a PATH-hoz. Ezt az opciót jelöld be!**)
3. Tanulj meg navigálódni a Git Bash-ban (`cd`-vel)
4. Tanuld meg a git alapjait (add, commit, push és clone parancsok fognak kelleni)
5. Egy általad preferált helyre helyezd el az adatbázis respositoryját (`git clone git@github.com:artchallenge/artchallenge-data.git`)
6. Navigálj bele a respositoryba könyvtárába
7. Itt már futtathatod a python fájlokat `py [fájlnév]` paranccsal (a `[fájlnév]` helyén a fájlnak a neve szerepeljen)
8. Amikor kész vagy, push-olhatod a respositoryt