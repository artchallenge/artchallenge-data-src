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
