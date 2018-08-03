import sys
import os
from PIL import Image
from util import toJson, writeFile, appendFile
from fix_image_size import fix_image_size

join = os.path.join
dirname = os.path.dirname
realpath = os.path.realpath
mkdir = os.mkdir
exists = os.path.exists
dirpath = dirname(realpath(__file__))

imagePath = input('Festmény fájl elérési útja: ')
try:
    image = Image.open(imagePath if '://' not in imagePath else BytesIO(urllib.request.urlopen(imagePath).read()))
except:
    print('A fájl nem található!')
    sys.exit(1)

artist = input('Festő neve: ')
dataPath = join(dirpath, 'data')
artistPath = join(dataPath, 'artists', artist)
if not exists(artistPath):
    print('A festő könyvtára még nem létezik!')
    sys.exit()

painting = input('Festmény neve: ')
paintingPath = join(dataPath, 'artists', artist, 'paintings', painting)
if exists(paintingPath):
    print('A festmény könyvtára már létezik!')
    sys.exit()

mainImagePath = join(paintingPath, 'image.jpg')
metadataPath = join(paintingPath, 'metadata.json')
metadata = {
    'date': input('Elkészítésének éve: ').strip()
}

mkdir(paintingPath)
print('Painting könyvtár ✓', paintingPath)
writeFile(metadataPath, toJson(metadata))
print('Metadata fájl ✓', metadataPath)
fix_image_size(mainImagePath, image)
