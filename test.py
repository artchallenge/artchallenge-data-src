import os
import json
from util import find, readFile, err_quit
import argparse
import re
from functools import partial
from PIL import Image


parser = argparse.ArgumentParser(description='Validate the artchallenge data.')
parser.add_argument('--fix', '-f', action='store_true')
args = parser.parse_args()
fix = args.fix


def assertJson(text, _):
	json.loads(text)

assertsByExt = {
	'.json': assertJson
}

maxFileSize = 1000 * 100 # 100kB


def matchFilename(filename, expected):
	specialSyntax = re.search(r'\[(.*?)\]', expected)
	if specialSyntax == None:
		return expected == filename
	else:
		return any(
			matchFilename(filename, re.sub(r'\[(.*?)\]', item, expected))
			for item
			in specialSyntax.group(1).split('|')
		)

def matchFilenames(filenames, expecteds):
	filenameSet = set(filenames)
	expectedSet = set(expecteds)
	assert len(filenameSet) == len(expectedSet)
	return dict(
		(expected, find(lambda filename: matchFilename(filename, expected), filenameSet))
		for expected
		in expectedSet
	)


structure = {'files':{
	'collections.json': {},
	'artists': {'allFile': {'files': {
		'bio.md': {},
		'metadata.json': {},
		'paintings': {'allFile': {'files': {
			'metadata.json': {},
			'image.[jpg|jpeg|jpe|jif|jfif|jfi]': {}
		}}}
	}}}
}}


def checkpath(path, structure):
	expectedFiles = structure.get('files')
	expectedAllFile = structure.get('allFile')
	print('checking', path)
	if expectedAllFile != None or expectedFiles != None:
		files = set(os.listdir(path))
		if expectedAllFile != None:
			for file in files:
				checkpath(os.path.join(path, file), expectedAllFile)
		elif expectedFiles != None:
			expectedFileSet = set(expectedFiles.keys())
			try:
				filenameMatches = matchFilenames(files, expectedFileSet)
			except:
				err_quit('Ennek a könytárnak pontosan ezen fájlokat kell tartalmaznia: ' + str(expectedFileSet))
			for expectedFile in expectedFileSet:
				checkpath(os.path.join(path, filenameMatches[expectedFile]), expectedFiles[expectedFile])
	else:
		if os.path.getsize(path) > maxFileSize:
			if not fix:
				err_quit('Ez a fájl túl sok helyet foglal! A maximális fájl méret 100kB!')
			Image.

		assert os.path.getsize(path) <= maxFileSize, 
		_, ext = os.path.splitext(path)
		assertByExt = assertsByExt.get(ext)
		if assertByExt != None:
			assertByExt(readFile(path), structure)


try:
	checkpath('data', structure)
except Exception as err:
	err_quit(str(err))

print('Test passed!')