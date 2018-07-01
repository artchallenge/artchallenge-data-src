from PIL import Image
import config
import os
import util

join = os.path.join
dirname = os.path.dirname

def fixPaintingVersions(maxPath, image = None):
	versionsPath = dirname(maxPath)
	if image == None:
		image = Image.open(maxPath)
	else:
		image.save(maxPath)
	for width in config.paintingWidths:
		resized = image
		if width < image.width:
			height = int(width * (image.height / image.width))
			resized = image.resize((width, height), Image.LANCZOS)
		resized.save(join(versionsPath, config.nameWidthImage(width)))
	print('Képek átkonvertálása és mentése ✓')

if __name__ == '__main__':
	import sys
	fixPaintingVersions(sys.argv[1])