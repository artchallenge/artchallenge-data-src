import sys
import os
import json
import re
from shutil import copyfile
from PIL import Image
import urllib.request
from io import BytesIO
import config
from fix_painting_versions import fixPaintingVersions

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
def appendFile(path, data):
    file = open(path, 'a', encoding='utf8')
    file.write(data)
    file.close()

def main():
    imagePath = input('Festmény fájl elérési útja: ')

    try:
        image = Image.open(imagePath if '://' not in imagePath else BytesIO(urllib.request.urlopen(imagePath).read()))
    except:
        print('A fájl nem található!')
        sys.exit()

    dataPath = join(dirname(realpath(__file__)), 'data')

    artist = input('Festő neve: ')

    artistPath = join(dataPath, 'artists', artist)
    indexPath = join(artistPath, 'paintings', config.indexFileName)

    if not exists(artistPath):
        print('A festő könyvtára még nem létezik!')
        sys.exit()

    painting = input('Festmény neve: ')

    paintingPath = join(dataPath, 'artists', artist, 'paintings', painting)

    if exists(paintingPath):
        print('A festmény könyvtára már létezik!')
        sys.exit()

    metadataPath = join(paintingPath, 'metadata.json')
    versionsPath = join(paintingPath, 'versions')

    metadata = {
        'date': input('Elkészítésének éve: ').strip()
    }

    mkdir(paintingPath)
    appendFile(indexPath, painting + '\n')
    print('Painting könyvtár ✓', paintingPath)
    writeFile(metadataPath, toJson(metadata))
    print('Metadata fájl ✓', metadataPath)
    mkdir(versionsPath)
    print('Versions könyvtár ✓', versionsPath)

    fixPaintingVersions(versionsPath, image)

if __name__ == '__main__':
    main()