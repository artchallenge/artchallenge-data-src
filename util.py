from functools import partial

def operateFile(filename, callback, flags = 'r'):
	fh = open(filename, flags)
	result = callback(fh)
	fh.close()
	return result

readlines = partial(operateFile, callback = lambda fh: fh.readlines())
read = partial(operateFile, callback = lambda fh: fh.read())