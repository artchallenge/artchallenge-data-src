import sys
import os
from util import writeFile, toJson, textToList

join = os.path.join
dirname = os.path.dirname
realpath = os.path.realpath
mkdir = os.mkdir
exists = os.path.exists
dirpath = dirname(realpath(__file__))

artist = input('Festő neve: ')
dataPath = join(dirpath, 'data')
artistPath = join(dataPath, 'artists', artist)
metadataPath = join(artistPath, 'metadata.json')
bioPath = join(artistPath, 'bio.md')
paintingsPath = join(artistPath, 'paintings')

if exists(artistPath):
    print('A festő könyvtára már létezik!')
    sys.exit()

metadata = {
    'birth': input('Születési éve: ').strip(),
    'death': input('Halálozási éve: ').strip(),
    'nationality': input('Nemzetisége: ').strip(),
    'genres': textToList(input('Stílusok (vesszővel elválasztva): '))
}

mkdir(artistPath)
print('Artist könyvtár ✓', artistPath)
writeFile(metadataPath, toJson(metadata))
print('Metadata fájl ✓', metadataPath)
writeFile(bioPath, '')
print('Biography fájl ✓', bioPath)
mkdir(paintingsPath)
print('Paintings könyvtár ✓', paintingsPath)