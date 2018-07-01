import sys
import os
import json
import re

join = os.path.join
dirname = os.path.dirname
realpath = os.path.realpath
mkdir = os.mkdir
exists = os.path.exists
toJson = lambda data: json.dumps(data, separators=(',', ':'))
def writeFile(path, data):
    file = open(path, 'w', encoding='utf8')
    file.write(data)
    file.close()

artist = input('Festő neve: ')
dataPath = join(dirname(realpath(__file__)), 'data')
artistPath = join(dataPath, 'artists', artist)
metadataPath = join(artistPath, 'metadata.json')
bioPath = join(artistPath, 'bio.md')
paintingsPath = join(artistPath, 'paintings')
indexFileName = '.index'

if exists(artistPath):
    print('A festő könyvtára már létezik!')
    sys.exit()

metadata = {
    'birth': input('Születési éve: ').strip(),
    'death': input('Halálozási éve: ').strip(),
    'nationality': input('Nemzetisége: ').strip(),
    'genres': re.split(r'[\s,]*,[\s,]*', input('Stílusok (vesszővel elválasztva): ').strip())
}

mkdir(artistPath)
print('Artist könyvtár ✓', artistPath)
writeFile(metadataPath, toJson(metadata))
print('Metadata fájl ✓', metadataPath)
writeFile(bioPath, '')
print('Biography fájl ✓', bioPath)
mkdir(paintingsPath)
writeFile(join(paintingsPath, indexFileName), '')
print('Paintings könyvtár ✓', paintingsPath)