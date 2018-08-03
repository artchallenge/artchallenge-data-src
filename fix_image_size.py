import argparse
from PIL import Image
import urllib.request
from io import BytesIO

parser = argparse.ArgumentParser(description='Validate the artchallenge data.')
parser.add_argument('path', help='path of the image')
args = parser.parse_args()

def fix_image_size(path, image):
	width = 750
	height = int(width * (image.height / image.width))
	resized = image.resize((width, height), Image.LANCZOS)
	image.save(path, quality=75)

def main(path):
	image = Image.open(path if '://' not in path else BytesIO(urllib.request.urlopen(path).read()))
	fixImageSize(path, image)

if __name__ == '__main__':
	main(args.path)