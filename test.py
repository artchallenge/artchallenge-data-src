import os
import json
import config
import util
import argparse

# define global variables
parser = argparse.ArgumentParser(description='Validate the artchallenge data.')
parser.add_argument('--fix', '-f', action='store_true')
args = parser.parse_args()
fix = args.fix
# TODO actually use the fix variable and fix the errors

# functions
def assertJson(text, _):
	json.loads(text)

assertsByExt = {
	'.json': assertJson
}

structure = {'files':{
	'collections.json': {},
	'artists': {'allFile': {'files': {
		'bio.md': {},
		'metadata.json': {},
		'paintings': {'includesIndex': True, 'allFile': {'files': {
			'metadata.json': {},
			'versions': {'files': dict.fromkeys(config.paintingFiles, {})}
		}}}
	}}}
}}

def checkpath(path, structure):
	expectedFiles = structure.get('files')
	expectedAllFile = structure.get('allFile')
	print('checking', path)
	if expectedAllFile != None or expectedFiles != None:
		files = set(os.listdir(path))
		if structure.get('includesIndex'):
			files.remove(config.indexFileName)
			indexedFiles = util.readlines(os.path.join(path, config.indexFileName))
			for line in indexedFiles:
				assert line[0] != '\n', 'Az .index fájl az utolsó sor kivételével nem tartalmazhat üres sorokat!'
			assert indexedFiles[-1][-1] == '\n', 'Az .index fájl utolsó sora egy üres sor kell hogy legyen! (most ez "' + indexedFiles[-1] + '")'
			indexedFiles = set([file.rstrip('\n') for file in indexedFiles if file != '\n'])
			assert files == indexedFiles, 'Az .index fájl tartalma invalid!'
		else:
			assert config.indexFileName not in files, 'Ennek a könyvtárnak nem lehet .index fájlja!'
		if expectedAllFile != None:
			for file in files:
				checkpath(os.path.join(path, file), expectedAllFile)
		elif expectedFiles != None:
			expectedFileSet = set(expectedFiles.keys()) 
			assert expectedFileSet == files, 'Ennek a könytárnak pontosan ezen fájlokat kell tartalmaznia: ' + str(expectedFileSet)
			for file in files:
				checkpath(os.path.join(path, file), expectedFiles[file])
	else:
		_, ext = os.path.splitext(path)
		assertByExt = assertsByExt.get(ext)
		if assertByExt != None:
			assertByExt(util.read(path), structure)

# do it!
checkpath('data', structure)
print('Test passed!')