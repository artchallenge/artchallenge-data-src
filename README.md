[![Build Status](https://travis-ci.org/artchallenge/artchallenge-data-src.svg?branch=master)](https://travis-ci.org/artchallenge/artchallenge-data-src)

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
		- A festmény képe: `image.jpg`
- Gyűjtemények: `collections.json` (object array)
	- `name` (string)
	- `references` (festmény array)

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
	- `"-99--14"` (ie. 99-től ie. 14-ig)
- \[évszám\]: alapvetően sima integer (`/-[1-9]\d*|0/`), de
	- helyettesítheti egy `?`: az évszám ismeretlen 
	- kezdődhet `~`-vel: az integer csak körülbelüli érték

## Szkriptek használata
A főkönyvtárban találhatóak szkriptek a gyakori problémák automatizálására.
Ezek python3 segítségével futtathatóak. ([A python3-at innen tudod letölteni.](https://www.python.org/downloads/))
**FONTOS:** Windows-on a PATH változóban benne kell hogy legyen a python3.
Ezt letöltéskor automatikusan megcsinálja, ha bejelölöd a "Python hozzáadása a PATH-hoz" opciót.

## Letöltés
Bár a GitHub webes felületén keresztül is lehet hozzájárulni a project-hez,
a respository lekérése után lehet a megszokott környezetben dolgozni,
valamint a szkripteket futtatni, ami nagy előny a webes felülettel szemben.
A [letöltési utasítások itt](https://git-scm.com/downloads), [a használati utasítások pedig itt](https://git-scm.com/book/en/v2) találhatóak.
