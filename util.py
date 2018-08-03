import sys
import json
import re

def find(predicate, list):
	for elem in list:
		if(predicate(elem)):
			return elem
	raise LookupError('Cannot find element!')

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def err_quit(*args, **kwargs):
	eprint('[E]', *args, **kwargs)
	sys.exit(1)

def readlinesFile(file):
	with open(file) as fh:
		return fh.readlines()

def readFile(file):
	with open(file) as fh:
		return fh.read()

def writeFile(file, text):
	with open(file, 'w', encoding='utf8') as fh:
		fh.write(text)

def appendFile(file, text):
	with open(file, 'a', encoding='utf8') as fh:
		fh.write(text)

def toJson(data):
	return json.dumps(data, separators=(',', ':'))

def textToList(text):
	return re.split(r'[\s,]*,[\s,]*', text.strip())