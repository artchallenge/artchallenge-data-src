from PIL import Image
from glob import iglob
from os import path
splitext = path.splitext
getfilesize = path.getsize

maxFileSize = 1000 * 1000 # 1MB

def fix_image(path):
	with Image.open(path) as image:
		basename = splitext(path)[0]
		path = basename + '.jpg'

		width = image.width
		print('width: ' + str(width))
		while getfilesize(path) > maxFileSize:
			width -= 50
			print('reduced width: ' + str(width))
			height = int(width * (image.height / image.width))
			image = image.resize((width, height), Image.LANCZOS)
			image.save(path)

def main():
	for path in iglob('data/artists/*/paintings/*/image.*'):
		print(path)
		fix_image(path)

if __name__ == '__main__':
	main()